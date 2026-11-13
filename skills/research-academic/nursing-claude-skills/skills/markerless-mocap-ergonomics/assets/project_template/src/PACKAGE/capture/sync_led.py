"""LED 閃光同步：以視覺事件取代硬體觸發。

網路攝影機沒有硬體觸發腳位，各相機的取樣時刻彼此獨立。本模組以一個
所有相機都能看見的 LED 閃光作為共同時間基準，事後對齊各相機時間軸。

原理：閃光在某兩幀之間發生時，過渡幀的亮度會落在暗、亮兩個平台之間。
利用這個中間值做線性內插，可將對齊精度推進到「次幀」等級——
即優於 1/fps 的時間解析度。以 60 fps 為例，單靠找「第一個變亮的幀」
只能達到 16.7 ms 精度，加入次幀內插後通常可達 2–5 ms。

流程：
1. 錄製開始後、動作開始前，觸發一次 LED 閃光。
2. 對每台相機的影片計算亮度時序，偵測閃光起始的次幀位置。
3. 以任一相機為基準，計算其餘相機的時間偏移量。
4. 後續三維重建時，以此偏移量校正各相機的幀時戳。

純運算邏輯（detect_flash_onset）與影像 I/O 分離，以便用合成資料測試。
"""

from __future__ import annotations

import csv
import logging
from dataclasses import dataclass
from pathlib import Path

import numpy as np

logger = logging.getLogger(__name__)

# cv2 僅在讀取影片時需要。刻意延遲載入，使純運算函式
# （detect_flash_onset、frame_index_to_time）能在未安裝 OpenCV 的環境測試。
# 這對應 CLAUDE.md 的要求：每個模組都要能在沒有相機的情況下測試。


@dataclass
class FlashOnset:
    """閃光起始偵測結果。"""

    frame_index: float  # 次幀精度的幀索引（可為小數）
    baseline: float  # 閃光前亮度平台
    plateau: float  # 閃光後亮度平台
    contrast: float  # plateau - baseline，用於判斷偵測可信度

    @property
    def is_reliable(self) -> bool:
        """對比不足時代表 LED 太暗、距離太遠或被遮擋，偵測結果不可信。"""
        return self.contrast >= MIN_FLASH_CONTRAST


# 亮度以 0–255 計。對比低於此值時，雜訊可能被誤判為閃光。
MIN_FLASH_CONTRAST = 8.0


def detect_flash_onset(
    brightness: np.ndarray,
    search_end: int | None = None,
    plateau_window: int = 3,
) -> FlashOnset:
    """從亮度時序偵測閃光起始，回傳次幀精度的幀索引。

    Args:
        brightness: 每幀亮度（一維陣列）
        search_end: 只在前 search_end 幀內搜尋。閃光應在動作開始前觸發，
            限縮搜尋範圍可避免動作本身造成的亮度變化被誤判。
        plateau_window: 估計亮暗平台時取用的幀數

    Returns:
        FlashOnset；呼叫端應檢查 is_reliable。

    Raises:
        ValueError: 序列過短無法偵測。
    """
    series = np.asarray(brightness, dtype=np.float64)
    if series.ndim != 1:
        raise ValueError("brightness 必須為一維陣列")

    end = len(series) if search_end is None else min(search_end, len(series))
    if end < 2 * plateau_window + 2:
        raise ValueError(f"序列過短（{end} 幀），無法可靠偵測閃光")

    window = series[:end]

    # 最大正梯度處即為閃光發生的過渡區。
    diffs = np.diff(window)
    rise_idx = int(np.argmax(diffs))

    # 以過渡區前後的區段估計暗、亮平台。取中位數以抵抗單幀雜訊。
    pre_start = max(0, rise_idx - plateau_window)
    baseline = float(np.median(window[pre_start : rise_idx + 1]))

    post_end = min(end, rise_idx + 1 + plateau_window + 1)
    plateau = float(np.median(window[rise_idx + 1 : post_end]))

    contrast = plateau - baseline
    if contrast <= 0:
        return FlashOnset(float(rise_idx), baseline, plateau, contrast)

    # 次幀內插：找亮度跨越中點的位置。
    # 過渡幀的亮度反映 LED 在該幀曝光期間點亮的時間比例，
    # 因此中點交越處即為閃光起始的最佳線性估計。
    midpoint = baseline + contrast / 2.0
    i0, i1 = rise_idx, rise_idx + 1
    v0, v1 = window[i0], window[i1]

    if v1 == v0:
        sub = 0.0
    else:
        sub = float(np.clip((midpoint - v0) / (v1 - v0), 0.0, 1.0))

    return FlashOnset(
        frame_index=float(i0) + sub,
        baseline=baseline,
        plateau=plateau,
        contrast=contrast,
    )


def brightness_series(
    video_path: Path,
    roi: tuple[int, int, int, int] | None = None,
    max_frames: int | None = None,
) -> np.ndarray:
    """計算影片每幀的平均亮度。

    Args:
        video_path: 影片檔路徑
        roi: (x, y, w, h)。強烈建議指定 LED 所在的小區域——
            全畫面平均會被人員移動稀釋，大幅降低閃光對比。
        max_frames: 只讀取前 N 幀
    """
    import cv2  # 延遲載入，見模組開頭說明

    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise RuntimeError(f"無法開啟影片 {video_path}")

    values: list[float] = []
    try:
        while max_frames is None or len(values) < max_frames:
            ok, frame = cap.read()
            if not ok or frame is None:
                break
            if roi is not None:
                x, y, w, h = roi
                frame = frame[y : y + h, x : x + w]
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            values.append(float(gray.mean()))
    finally:
        cap.release()

    return np.asarray(values, dtype=np.float64)


def load_timestamps(csv_path: Path) -> np.ndarray:
    """讀取錄製時產生的時戳 CSV，回傳單調時鐘秒數陣列。"""
    times: list[float] = []
    with csv_path.open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            times.append(float(row["t_monotonic_s"]))
    return np.asarray(times, dtype=np.float64)


def frame_index_to_time(frame_index: float, timestamps: np.ndarray) -> float:
    """將次幀索引轉換為時間，對小數部分做線性內插。"""
    if len(timestamps) == 0:
        raise ValueError("時戳序列為空")
    i0 = int(np.floor(frame_index))
    frac = frame_index - i0
    i0 = max(0, min(i0, len(timestamps) - 1))
    i1 = min(i0 + 1, len(timestamps) - 1)
    return float(timestamps[i0] + frac * (timestamps[i1] - timestamps[i0]))


@dataclass
class SyncReport:
    """多相機同步分析結果。"""

    reference: str
    offsets_s: dict[str, float]  # 各相機相對基準的時間偏移（秒）
    onsets: dict[str, FlashOnset]

    @property
    def max_spread_ms(self) -> float:
        """各相機偏移量的最大差距（毫秒），即整體同步誤差。"""
        if not self.offsets_s:
            return 0.0
        vals = list(self.offsets_s.values())
        return (max(vals) - min(vals)) * 1000.0

    def unreliable_cameras(self) -> list[str]:
        return [name for name, o in self.onsets.items() if not o.is_reliable]


def compute_sync_offsets(
    session_dir: Path,
    camera_names: list[str],
    roi: tuple[int, int, int, int] | None = None,
    search_frames: int = 300,
    reference: str | None = None,
) -> SyncReport:
    """分析一次錄製中所有相機的閃光時刻，計算彼此的時間偏移。

    Args:
        session_dir: 含 <name>.avi 與 <name>_timestamps.csv 的目錄
        camera_names: 相機名稱清單
        roi: LED 所在區域，建議指定
        search_frames: 在前 N 幀內搜尋閃光
        reference: 基準相機名稱，預設取 camera_names[0]

    Returns:
        SyncReport；呼叫端應檢查 max_spread_ms 與 unreliable_cameras()。
    """
    ref = reference or camera_names[0]
    if ref not in camera_names:
        raise ValueError(f"基準相機 {ref} 不在清單中")

    onsets: dict[str, FlashOnset] = {}
    flash_times: dict[str, float] = {}

    for name in camera_names:
        video = session_dir / f"{name}.avi"
        stamps = session_dir / f"{name}_timestamps.csv"
        if not video.exists() or not stamps.exists():
            raise FileNotFoundError(f"相機 {name} 缺少影片或時戳檔")

        series = brightness_series(video, roi=roi, max_frames=search_frames)
        onset = detect_flash_onset(series, search_end=search_frames)
        onsets[name] = onset

        if not onset.is_reliable:
            logger.warning(
                "相機 %s 的閃光對比僅 %.1f，低於門檻 %.1f；"
                "請確認 LED 在該相機視野內且未被遮擋，或縮小 roi",
                name,
                onset.contrast,
                MIN_FLASH_CONTRAST,
            )

        flash_times[name] = frame_index_to_time(onset.frame_index, load_timestamps(stamps))

    t_ref = flash_times[ref]
    offsets = {name: t - t_ref for name, t in flash_times.items()}

    return SyncReport(reference=ref, offsets_s=offsets, onsets=onsets)
