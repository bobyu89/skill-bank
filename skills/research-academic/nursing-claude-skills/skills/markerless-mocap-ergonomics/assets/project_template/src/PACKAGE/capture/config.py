"""相機設定的資料結構與載入。

刻意與 webcam.py 分離：設定是純資料，不應因為要讀一份 YAML
就必須安裝 OpenCV。這讓設定的驗證邏輯能獨立測試
（對應 CLAUDE.md：每個模組都要能在沒有相機的情況下測試）。
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass
class CameraSettings:
    """單台相機的擷取設定。

    exposure 採 DirectShow 的 log2 秒慣例（-6 約等於 1/64 秒）。
    數值愈小曝光愈短、動態模糊愈少，但需要愈強的照明。
    翻身作業屬快速動作，建議在照明充足下盡量縮短曝光。
    """

    index: int
    name: str
    width: int = 1280
    height: int = 720
    fps: int = 60
    exposure: float | None = -6.0
    gain: float | None = None

    def __post_init__(self) -> None:
        if self.index < 0:
            raise ValueError(f"相機 {self.name} 的索引不可為負：{self.index}")
        if not self.name:
            raise ValueError("相機必須有名稱（name 會成為輸出檔名與機位識別依據）")
        if self.fps <= 0:
            raise ValueError(f"相機 {self.name} 的幀率必須為正：{self.fps}")
        if self.width <= 0 or self.height <= 0:
            raise ValueError(f"相機 {self.name} 的解析度無效：{self.width}x{self.height}")


def parse_camera_config(cfg: dict[str, Any]) -> list[CameraSettings]:
    """由設定字典建立相機設定清單。

    每台相機的設定由 defaults 與該相機的個別設定合併而成，
    個別設定優先。

    Raises:
        ValueError: 設定缺少必要欄位、名稱重複或索引重複。
    """
    if "cameras" not in cfg:
        raise ValueError("設定檔缺少 cameras 區段")

    defaults = cfg.get("defaults") or {}
    settings: list[CameraSettings] = []

    for i, cam in enumerate(cfg["cameras"]):
        merged = {**defaults, **cam}
        unknown = set(merged) - set(CameraSettings.__dataclass_fields__)
        if unknown:
            raise ValueError(f"第 {i + 1} 台相機有無法辨識的設定項：{sorted(unknown)}")
        try:
            settings.append(CameraSettings(**merged))
        except TypeError as exc:
            raise ValueError(f"第 {i + 1} 台相機設定不完整：{exc}") from exc

    names = [s.name for s in settings]
    if len(set(names)) != len(names):
        dupes = sorted({n for n in names if names.count(n) > 1})
        raise ValueError(f"相機名稱重複：{dupes}。名稱是機位識別依據，必須唯一")

    indices = [s.index for s in settings]
    if len(set(indices)) != len(indices):
        dupes = sorted({i for i in indices if indices.count(i) > 1})
        raise ValueError(f"相機索引重複：{dupes}。同一索引不可指派給兩個機位")

    return settings


def load_camera_config(path: Path) -> list[CameraSettings]:
    """從 YAML 檔載入相機設定。"""
    with path.open("r", encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh)
    if not isinstance(cfg, dict):
        raise ValueError(f"{path} 不是有效的 YAML 對應結構")
    return parse_camera_config(cfg)
