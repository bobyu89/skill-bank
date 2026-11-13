"""多網路攝影機同步錄製。

設計要點：

1. 每台相機獨立執行緒。單執行緒輪詢會使各相機的實際取樣時刻串接累加，
   相機愈多偏差愈大；獨立執行緒讓每台相機維持自身節奏。
2. 時戳於 read() 回傳後立即取得並與該幀綁定寫入 CSV，不事後推算。
3. 所有自動功能關閉後回讀驗證（見 CLAUDE.md 開發鐵則一）。
   自動對焦若未關閉，會在錄製中途改變相機內參，使校正結果失效——
   而且產生的資料表面上完全正常，極難察覺。
"""

from __future__ import annotations

import csv
import logging
import platform
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path

import cv2

from {{PACKAGE}}.capture.config import CameraSettings

logger = logging.getLogger(__name__)

PREFERRED_BACKEND = cv2.CAP_DSHOW if platform.system() == "Windows" else cv2.CAP_ANY

__all__ = [
    "CameraOpenReport",
    "CameraSettings",
    "MultiCameraRecorder",
    "RecordingResult",
    "open_camera",
]


@dataclass
class PropertyCheck:
    """設定回讀驗證結果。"""

    prop_name: str
    requested: float
    actual: float
    ok: bool


@dataclass
class CameraOpenReport:
    """相機開啟後的設定驗證報告。"""

    name: str
    index: int
    checks: list[PropertyCheck] = field(default_factory=list)

    @property
    def all_ok(self) -> bool:
        return all(c.ok for c in self.checks)

    def failures(self) -> list[PropertyCheck]:
        return [c for c in self.checks if not c.ok]


def _set_and_verify(
    cap: cv2.VideoCapture,
    prop: int,
    value: float,
    prop_name: str,
    tol: float = 0.51,
) -> PropertyCheck:
    """設定相機屬性並回讀驗證。

    部分 UVC 驅動會靜默忽略設定請求（set() 仍回傳 True），
    因此必須回讀比對，不可信任 set() 的回傳值。
    """
    cap.set(prop, value)
    actual = cap.get(prop)
    ok = abs(actual - value) <= tol
    if not ok:
        logger.warning("%s 設定未生效：要求 %s，實際 %s", prop_name, value, actual)
    return PropertyCheck(prop_name=prop_name, requested=value, actual=actual, ok=ok)


def open_camera(
    settings: CameraSettings, backend: int = PREFERRED_BACKEND
) -> tuple[cv2.VideoCapture, CameraOpenReport]:
    """開啟相機、關閉所有自動功能並驗證設定。

    Raises:
        RuntimeError: 相機無法開啟，或無法關閉自動對焦。
    """
    cap = cv2.VideoCapture(settings.index, backend)
    if not cap.isOpened():
        raise RuntimeError(f"無法開啟相機 {settings.name}（索引 {settings.index}）")

    report = CameraOpenReport(name=settings.name, index=settings.index)

    # MJPG 為取得高幀率的前提；未設定時多數相機會退回未壓縮格式並受限於 USB 頻寬。
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

    report.checks.append(
        _set_and_verify(cap, cv2.CAP_PROP_FRAME_WIDTH, settings.width, "width")
    )
    report.checks.append(
        _set_and_verify(cap, cv2.CAP_PROP_FRAME_HEIGHT, settings.height, "height")
    )
    report.checks.append(_set_and_verify(cap, cv2.CAP_PROP_FPS, settings.fps, "fps", tol=1.01))

    # --- 關閉自動功能（CLAUDE.md 鐵則一）---
    # 自動對焦是最危險的一項：它會改變焦距，等同改變相機內參，
    # 使校正失效。且失效是漸進的、不會報錯。
    autofocus = _set_and_verify(cap, cv2.CAP_PROP_AUTOFOCUS, 0, "autofocus", tol=0.01)
    report.checks.append(autofocus)
    if not autofocus.ok:
        cap.release()
        raise RuntimeError(
            f"相機 {settings.name} 無法關閉自動對焦（回讀值 {autofocus.actual}）。"
            "自動對焦會使相機校正失效，不得在此狀態下錄製。"
            "請改用支援手動對焦的機型，或以廠商工具鎖定對焦後重試。"
        )

    # DirectShow 的慣例與直覺相反：0.25 = 手動、0.75 = 自動。
    # 此慣例因驅動而異，故回讀後僅警告不中止。
    auto_exposure_manual = 0.25 if backend == cv2.CAP_DSHOW else 1
    report.checks.append(
        _set_and_verify(
            cap, cv2.CAP_PROP_AUTO_EXPOSURE, auto_exposure_manual, "auto_exposure(manual)", tol=0.26
        )
    )
    if settings.exposure is not None:
        report.checks.append(
            _set_and_verify(cap, cv2.CAP_PROP_EXPOSURE, settings.exposure, "exposure", tol=1.01)
        )
    if settings.gain is not None:
        report.checks.append(_set_and_verify(cap, cv2.CAP_PROP_GAIN, settings.gain, "gain"))

    report.checks.append(
        _set_and_verify(cap, cv2.CAP_PROP_AUTO_WB, 0, "auto_white_balance", tol=0.01)
    )

    # 縮小內部緩衝，降低影格滯留造成的時戳誤差。
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    return cap, report


class _CameraWorker(threading.Thread):
    """單台相機的擷取執行緒。"""

    def __init__(
        self,
        cap: cv2.VideoCapture,
        settings: CameraSettings,
        out_dir: Path,
        stop_event: threading.Event,
        start_barrier: threading.Barrier,
    ) -> None:
        super().__init__(name=f"cam-{settings.name}", daemon=True)
        self.cap = cap
        self.settings = settings
        self.out_dir = out_dir
        self.stop_event = stop_event
        self.start_barrier = start_barrier

        self.frames_written = 0
        self.frames_dropped = 0
        self.error: Exception | None = None

    def run(self) -> None:
        video_path = self.out_dir / f"{self.settings.name}.avi"
        stamp_path = self.out_dir / f"{self.settings.name}_timestamps.csv"

        # 以 MJPG 寫出，與網路攝影機原生格式一致，避免重新編碼引入額外壓縮失真。
        writer = cv2.VideoWriter(
            str(video_path),
            cv2.VideoWriter_fourcc(*"MJPG"),
            float(self.settings.fps),
            (self.settings.width, self.settings.height),
        )

        try:
            if not writer.isOpened():
                raise RuntimeError(f"無法建立影片檔 {video_path}")

            with stamp_path.open("w", newline="", encoding="utf-8") as fh:
                csv_writer = csv.writer(fh)
                csv_writer.writerow(["frame_index", "t_monotonic_s", "t_unix_s"])

                # 所有執行緒在此對齊後才開始擷取，避免各相機起始時間差過大。
                # 這只縮小起始偏差，絕對同步仍須依賴 LED 閃光（見 sync_led 模組）。
                self.start_barrier.wait()

                while not self.stop_event.is_set():
                    ok, frame = self.cap.read()
                    # 時戳緊接在 read() 之後取得，不做任何前置處理，
                    # 以免處理耗時混入時戳誤差。
                    t_mono = time.perf_counter()
                    t_unix = time.time()

                    if not ok or frame is None or frame.size == 0:
                        self.frames_dropped += 1
                        continue

                    writer.write(frame)
                    csv_writer.writerow([self.frames_written, f"{t_mono:.6f}", f"{t_unix:.6f}"])
                    self.frames_written += 1

        except Exception as exc:  # noqa: BLE001 — 執行緒錯誤須帶回主執行緒
            self.error = exc
            logger.exception("相機 %s 擷取執行緒發生錯誤", self.settings.name)
        finally:
            writer.release()


@dataclass
class RecordingResult:
    """錄製結果摘要。"""

    out_dir: Path
    duration_s: float
    per_camera: dict[str, dict[str, float]]

    def quality_warnings(self) -> list[str]:
        """回傳品質疑慮清單。

        掉幀率超過 0.5% 或實際幀率明顯低於設定值時，該次試作應標記為品質可疑
        （對應設計書 FR-06）。
        """
        warnings: list[str] = []
        for name, stats in self.per_camera.items():
            total = stats["frames"] + stats["dropped"]
            if total > 0:
                drop_rate = stats["dropped"] / total
                if drop_rate > 0.005:
                    warnings.append(f"{name}：掉幀率 {drop_rate:.2%} 超過 0.5% 門檻")
            if stats["actual_fps"] < stats["target_fps"] * 0.9:
                warnings.append(
                    f"{name}：實際幀率 {stats['actual_fps']:.1f} 低於目標 "
                    f"{stats['target_fps']:.0f} 的 90%"
                )
        return warnings


class MultiCameraRecorder:
    """多相機同步錄製協調器。"""

    def __init__(self, settings: list[CameraSettings], backend: int = PREFERRED_BACKEND) -> None:
        if not settings:
            raise ValueError("至少需要一台相機")
        self.settings = settings
        self.backend = backend
        self._caps: dict[str, cv2.VideoCapture] = {}
        self._reports: list[CameraOpenReport] = []

    def open_all(self) -> list[CameraOpenReport]:
        """開啟所有相機並回傳設定驗證報告。

        任一相機開啟失敗時，會釋放已開啟者後再拋出例外，避免相機被佔用。
        """
        try:
            for s in self.settings:
                cap, report = open_camera(s, self.backend)
                self._caps[s.name] = cap
                self._reports.append(report)
                logger.info(
                    "相機 %s 已開啟（%dx%d @ %d fps）", s.name, s.width, s.height, s.fps
                )
        except Exception:
            self.close_all()
            raise
        return self._reports

    def close_all(self) -> None:
        for cap in self._caps.values():
            cap.release()
        self._caps.clear()

    def record(self, out_dir: Path, duration_s: float) -> RecordingResult:
        """錄製指定秒數。

        Args:
            out_dir: 輸出目錄，將建立 <name>.avi 與 <name>_timestamps.csv
            duration_s: 錄製長度（秒）
        """
        if not self._caps:
            raise RuntimeError("請先呼叫 open_all()")

        out_dir.mkdir(parents=True, exist_ok=True)
        stop_event = threading.Event()
        barrier = threading.Barrier(len(self.settings))

        workers = [
            _CameraWorker(self._caps[s.name], s, out_dir, stop_event, barrier)
            for s in self.settings
        ]

        t0 = time.perf_counter()
        for w in workers:
            w.start()

        try:
            time.sleep(duration_s)
        finally:
            stop_event.set()
            for w in workers:
                w.join(timeout=10.0)
        elapsed = time.perf_counter() - t0

        errors = [(w.settings.name, w.error) for w in workers if w.error is not None]
        if errors:
            names = ", ".join(n for n, _ in errors)
            raise RuntimeError(f"以下相機錄製失敗：{names}") from errors[0][1]

        per_camera = {
            w.settings.name: {
                "frames": float(w.frames_written),
                "dropped": float(w.frames_dropped),
                "actual_fps": w.frames_written / elapsed if elapsed > 0 else 0.0,
                "target_fps": float(w.settings.fps),
            }
            for w in workers
        }
        return RecordingResult(out_dir=out_dir, duration_s=elapsed, per_camera=per_camera)

    def __enter__(self) -> MultiCameraRecorder:
        self.open_all()
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close_all()
