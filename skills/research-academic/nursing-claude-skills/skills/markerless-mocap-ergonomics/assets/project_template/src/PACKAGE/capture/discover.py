"""相機探索與能力查詢。

錄製前必須執行本模組，原因有二：

1. 多台網路攝影機共用同一 USB 控制器時，OpenCV 可能在第 3 台之後
   靜默回傳空影格而不拋出例外。必須實際抓幀驗證，不能只看 isOpened()。
2. 網路攝影機支援的解析度與幀率組合因型號而異，且 OpenCV 對不支援的
   組合通常是「靜默降級」而非報錯。必須回讀確認實際生效值。
"""

from __future__ import annotations

import logging
import platform
from dataclasses import dataclass, field

import cv2

logger = logging.getLogger(__name__)

# Windows 上 MSMF 後端在多相機同時開啟時不穩定（開啟緩慢、偶發失敗），
# DirectShow 相對可靠。其他平台使用預設後端。
PREFERRED_BACKEND = cv2.CAP_DSHOW if platform.system() == "Windows" else cv2.CAP_ANY

# 常見的解析度與幀率組合，依生物力學需求排序。
# 對翻身作業而言，時間解析度（幀率）與空間解析度同等重要：
# 幀率不足會使角速度估計失真，進而影響動態負荷指標。
PROBE_MODES: list[tuple[int, int, int]] = [
    (1920, 1080, 60),
    (1280, 720, 60),
    (1920, 1080, 30),
    (1280, 720, 30),
    (640, 480, 30),
]


@dataclass
class CameraMode:
    """實際生效的擷取模式。"""

    width: int
    height: int
    fps: float
    frames_ok: bool  # 是否能實際取得非空影格


@dataclass
class CameraInfo:
    """單台相機的探索結果。"""

    index: int
    backend: str
    opened: bool
    supported_modes: list[CameraMode] = field(default_factory=list)
    note: str = ""

    @property
    def best_mode(self) -> CameraMode | None:
        """回傳最適合生物力學量測的可用模式。

        排序依 PROBE_MODES 的順序，即優先高幀率高解析度。
        """
        for mode in self.supported_modes:
            if mode.frames_ok:
                return mode
        return None


def _probe_mode(cap: cv2.VideoCapture, width: int, height: int, fps: int) -> CameraMode:
    """設定並回讀單一模式，實際抓幀驗證。"""
    # MJPG 為多數網路攝影機支援高幀率的必要條件。
    # 未設定時 OpenCV 常取得未壓縮 YUY2 格式，USB 頻寬會限制幀率至個位數。
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FPS, fps)

    actual_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    actual_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    actual_fps = float(cap.get(cv2.CAP_PROP_FPS))

    # 實際抓幀。isOpened() 為 True 不代表能取得有效影像。
    frames_ok = False
    for _ in range(3):
        ok, frame = cap.read()
        if ok and frame is not None and frame.size > 0:
            frames_ok = True
            break

    return CameraMode(width=actual_w, height=actual_h, fps=actual_fps, frames_ok=frames_ok)


def probe_camera(index: int, backend: int = PREFERRED_BACKEND) -> CameraInfo:
    """探索單一相機索引。"""
    cap = cv2.VideoCapture(index, backend)
    backend_name = cap.getBackendName() if cap.isOpened() else "n/a"

    if not cap.isOpened():
        cap.release()
        return CameraInfo(index=index, backend=backend_name, opened=False, note="無法開啟")

    modes: list[CameraMode] = []
    seen: set[tuple[int, int]] = set()
    try:
        for w, h, fps in PROBE_MODES:
            mode = _probe_mode(cap, w, h, fps)
            key = (mode.width, mode.height)
            # 同一實際解析度只保留最高幀率者（PROBE_MODES 已依幀率降序）
            if key in seen:
                continue
            seen.add(key)
            modes.append(mode)
    finally:
        cap.release()

    return CameraInfo(index=index, backend=backend_name, opened=True, supported_modes=modes)


def discover_cameras(max_index: int = 10) -> list[CameraInfo]:
    """掃描相機索引 0..max_index-1。

    注意：索引與實體相機的對應關係在重新插拔 USB 後可能改變。
    正式錄製前應以 scripts/00_discover_cameras.py 的預覽功能確認對應。
    """
    found: list[CameraInfo] = []
    for idx in range(max_index):
        info = probe_camera(idx)
        if info.opened:
            logger.info("相機 %d 可用（後端 %s）", idx, info.backend)
            found.append(info)
    return found


def verify_concurrent_open(indices: list[int], backend: int = PREFERRED_BACKEND) -> dict[int, bool]:
    """驗證多台相機能否「同時」開啟並取得有效影格。

    這是錄製前的必要檢查。單台逐一測試成功，不代表同時開啟也會成功——
    USB 頻寬不足時，後開啟的相機通常回傳空影格而非拋出例外。
    """
    caps: dict[int, cv2.VideoCapture] = {}
    result: dict[int, bool] = {}
    try:
        for idx in indices:
            cap = cv2.VideoCapture(idx, backend)
            cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
            caps[idx] = cap

        for idx, cap in caps.items():
            ok = False
            for _ in range(5):
                got, frame = cap.read()
                if got and frame is not None and frame.size > 0:
                    ok = True
                    break
            result[idx] = ok
            if not ok:
                logger.warning(
                    "相機 %d 在多機同時開啟時無法取得影格，"
                    "可能為 USB 頻寬不足；請改接不同 USB 控制器或降低解析度",
                    idx,
                )
    finally:
        for cap in caps.values():
            cap.release()
    return result
