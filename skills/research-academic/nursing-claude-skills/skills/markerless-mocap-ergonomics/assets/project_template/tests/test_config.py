"""相機設定解析測試。

設定錯誤若到錄製當下才發現，代價是浪費受試者的時間，
因此驗證必須在載入階段就完成，而非等到開相機時才失敗。
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from {{PACKAGE}}.capture.config import (
    CameraSettings,
    load_camera_config,
    parse_camera_config,
)

REPO_ROOT = Path(__file__).resolve().parents[1]


class TestCameraSettings:
    def test_defaults_are_biomechanics_appropriate(self) -> None:
        """預設應為 720p60——快速動作的角速度估計需要足夠時間解析度。"""
        s = CameraSettings(index=0, name="cam")
        assert s.fps == 60
        assert (s.width, s.height) == (1280, 720)

    @pytest.mark.parametrize(
        ("kwargs", "match"),
        [
            ({"index": -1, "name": "cam"}, "索引不可為負"),
            ({"index": 0, "name": ""}, "必須有名稱"),
            ({"index": 0, "name": "cam", "fps": 0}, "幀率必須為正"),
            ({"index": 0, "name": "cam", "width": 0}, "解析度無效"),
        ],
    )
    def test_rejects_invalid(self, kwargs: dict, match: str) -> None:
        with pytest.raises(ValueError, match=match):
            CameraSettings(**kwargs)


class TestParseCameraConfig:
    def test_merges_defaults_with_per_camera(self) -> None:
        cfg = {
            "defaults": {"width": 1920, "height": 1080, "fps": 30},
            "cameras": [
                {"name": "a", "index": 0},
                {"name": "b", "index": 1, "fps": 60},  # 個別設定應覆蓋預設
            ],
        }
        settings = parse_camera_config(cfg)
        assert settings[0].fps == 30
        assert settings[1].fps == 60
        assert settings[0].width == 1920

    def test_works_without_defaults_section(self) -> None:
        cfg = {"cameras": [{"name": "a", "index": 0}]}
        assert len(parse_camera_config(cfg)) == 1

    def test_rejects_duplicate_names(self) -> None:
        """名稱是機位識別依據，重複會導致輸出檔互相覆蓋。"""
        cfg = {"cameras": [{"name": "a", "index": 0}, {"name": "a", "index": 1}]}
        with pytest.raises(ValueError, match="名稱重複"):
            parse_camera_config(cfg)

    def test_rejects_duplicate_indices(self) -> None:
        """同一實體相機不可指派給兩個機位，否則外參會張冠李戴。"""
        cfg = {"cameras": [{"name": "a", "index": 0}, {"name": "b", "index": 0}]}
        with pytest.raises(ValueError, match="索引重複"):
            parse_camera_config(cfg)

    def test_rejects_unknown_keys(self) -> None:
        """拼錯的設定項若被靜默忽略，使用者會誤以為設定已生效。"""
        cfg = {"cameras": [{"name": "a", "index": 0, "fsp": 60}]}
        with pytest.raises(ValueError, match="無法辨識"):
            parse_camera_config(cfg)

    def test_rejects_missing_required_field(self) -> None:
        cfg = {"cameras": [{"name": "a"}]}
        with pytest.raises(ValueError, match="設定不完整"):
            parse_camera_config(cfg)

    def test_rejects_missing_cameras_section(self) -> None:
        with pytest.raises(ValueError, match="缺少 cameras"):
            parse_camera_config({"defaults": {}})


class TestShippedConfig:
    """驗證 repo 內附的設定檔本身有效，避免使用者第一次執行就踩雷。"""

    def test_shipped_config_is_valid(self) -> None:
        settings = load_camera_config(REPO_ROOT / "configs" / "cameras.yaml")
        assert len(settings) >= 2, "三角測量至少需要兩台相機"
        assert all(s.fps >= 60 for s in settings), "翻身作業需要 60 fps 以上"

    def test_shipped_config_is_utf8_readable(self, tmp_path: Path) -> None:
        """Windows 預設 cp950 會使中文註解讀取失敗，必須明確指定 UTF-8。"""
        src = REPO_ROOT / "configs" / "cameras.yaml"
        text = src.read_text(encoding="utf-8")
        assert "病床" in text  # 確認中文註解確實存在且可讀

        roundtrip = tmp_path / "copy.yaml"
        roundtrip.write_text(text, encoding="utf-8")
        assert yaml.safe_load(roundtrip.read_text(encoding="utf-8"))["cameras"]
