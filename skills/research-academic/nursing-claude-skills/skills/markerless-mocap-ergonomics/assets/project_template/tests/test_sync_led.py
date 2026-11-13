"""LED 閃光同步偵測的合成資料測試。

這些測試不需要相機，可在任何機器上執行。核心要驗證的是：
即使單台相機的絕對偵測值帶有系統性偏差，**相機之間的相對偏移**
仍能被準確還原——因為同步校正只需要相對量，系統性偏差會相互抵消。
"""

from __future__ import annotations

import numpy as np
import pytest

from {{PACKAGE}}.capture.sync_led import (
    MIN_FLASH_CONTRAST,
    detect_flash_onset,
    frame_index_to_time,
)

FPS = 60.0
# 相對偏移的容許誤差（幀）。0.15 幀 @ 60fps 約等於 2.5 毫秒，
# 遠優於不做次幀內插時的 16.7 毫秒（一個幀間隔）。
TOL_FRAMES = 0.15


def _synth_series(
    n: int,
    onset_frame: float,
    baseline: float = 30.0,
    contrast: float = 100.0,
    noise_sd: float = 0.0,
    seed: int = 0,
) -> np.ndarray:
    """產生含閃光的合成亮度序列。

    模型：LED 於 onset_frame 時刻點亮，亮度在一個幀間隔內線性上升到平台。
    這近似真實情況——過渡幀的亮度反映 LED 在該幀曝光期間點亮的時間比例。
    """
    idx = np.arange(n, dtype=float)
    vals = baseline + contrast * np.clip(idx - onset_frame, 0.0, 1.0)
    if noise_sd > 0:
        rng = np.random.default_rng(seed)
        vals = vals + rng.normal(0.0, noise_sd, size=n)
    return vals


class TestDetectFlashOnset:
    def test_detects_plateaus_and_contrast(self) -> None:
        series = _synth_series(n=40, onset_frame=10.0, baseline=25.0, contrast=120.0)
        onset = detect_flash_onset(series)

        assert onset.baseline == pytest.approx(25.0, abs=1.0)
        assert onset.plateau == pytest.approx(145.0, abs=1.0)
        assert onset.contrast == pytest.approx(120.0, abs=2.0)
        assert onset.is_reliable

    def test_onset_lands_in_transition_region(self) -> None:
        series = _synth_series(n=40, onset_frame=12.0)
        onset = detect_flash_onset(series)
        # 偵測值應落在過渡區附近，而非序列的其他位置
        assert 12.0 <= onset.frame_index <= 13.5

    def test_monotonic_in_true_onset(self) -> None:
        """真實閃光時刻愈晚，偵測到的幀索引也應愈晚。"""
        detected = [
            detect_flash_onset(_synth_series(40, onset_frame=t)).frame_index
            for t in (10.0, 10.3, 10.6, 10.9, 11.2)
        ]
        assert detected == sorted(detected)

    @pytest.mark.parametrize("delta_frames", [0.0, 0.25, 0.4, 0.8, 1.0, 2.3])
    def test_relative_offset_recovered(self, delta_frames: float) -> None:
        """核心測試：兩台相機之間的相對時間偏移應被準確還原。

        單台相機的絕對偵測值帶有系統性偏差（源自線性內插對斜坡模型的近似），
        但該偏差對所有相機一致，因此相減後抵消。同步校正只需要相對量。
        """
        base_onset = 15.0
        a = detect_flash_onset(_synth_series(60, onset_frame=base_onset))
        b = detect_flash_onset(_synth_series(60, onset_frame=base_onset + delta_frames))

        recovered = b.frame_index - a.frame_index
        assert recovered == pytest.approx(delta_frames, abs=TOL_FRAMES)

    def test_robust_to_sensor_noise(self) -> None:
        """感測器雜訊不應破壞偵測（平台估計採中位數）。"""
        clean = detect_flash_onset(_synth_series(60, onset_frame=20.0)).frame_index
        noisy = detect_flash_onset(
            _synth_series(60, onset_frame=20.0, noise_sd=2.0, seed=42)
        ).frame_index
        assert noisy == pytest.approx(clean, abs=TOL_FRAMES)

    def test_low_contrast_flagged_unreliable(self) -> None:
        """LED 太暗或被遮擋時，必須標記為不可信而非回傳看似正常的結果。"""
        series = _synth_series(40, onset_frame=10.0, contrast=MIN_FLASH_CONTRAST / 2)
        onset = detect_flash_onset(series)
        assert not onset.is_reliable

    def test_search_end_limits_range(self) -> None:
        """限縮搜尋範圍可避免動作造成的亮度變化被誤判為閃光。"""
        series = _synth_series(120, onset_frame=15.0)
        # 在第 80 幀注入一個更大的亮度躍升，模擬動作或燈光變化
        series[80:] += 200.0

        limited = detect_flash_onset(series, search_end=60)
        assert 15.0 <= limited.frame_index <= 16.5

        unlimited = detect_flash_onset(series)
        assert unlimited.frame_index >= 79.0  # 被較大的躍升吸引

    def test_rejects_too_short_series(self) -> None:
        with pytest.raises(ValueError, match="序列過短"):
            detect_flash_onset(np.zeros(5))

    def test_rejects_non_1d(self) -> None:
        with pytest.raises(ValueError, match="一維"):
            detect_flash_onset(np.zeros((10, 10)))


class TestFrameIndexToTime:
    def test_integer_index_exact(self) -> None:
        ts = np.arange(10, dtype=float) / FPS
        assert frame_index_to_time(3.0, ts) == pytest.approx(3.0 / FPS)

    def test_fractional_index_interpolates(self) -> None:
        ts = np.arange(10, dtype=float) / FPS
        assert frame_index_to_time(3.5, ts) == pytest.approx(3.5 / FPS)

    def test_handles_irregular_intervals(self) -> None:
        """實際錄製的幀間隔並不等長，內插必須採用真實時戳而非假設等距。"""
        ts = np.array([0.0, 0.010, 0.030, 0.035])
        assert frame_index_to_time(1.5, ts) == pytest.approx(0.020)

    def test_clamps_beyond_last_frame(self) -> None:
        ts = np.array([0.0, 0.1, 0.2])
        assert frame_index_to_time(99.0, ts) == pytest.approx(0.2)

    def test_rejects_empty(self) -> None:
        with pytest.raises(ValueError, match="為空"):
            frame_index_to_time(0.0, np.array([]))


def test_end_to_end_offset_in_milliseconds() -> None:
    """整合情境：相機 B 的時戳因驅動緩衝而系統性延遲 8 毫秒。

    驗證還原出的偏移量接近真值——這正是同步校正實際要做的事。
    """
    delay_s = 0.008
    onset_frame = 20.0

    ts_a = np.arange(60, dtype=float) / FPS
    ts_b = ts_a + delay_s

    # 兩台相機看到同一次物理閃光，但 B 的時戳整體晚了 delay_s
    a = detect_flash_onset(_synth_series(60, onset_frame))
    b = detect_flash_onset(_synth_series(60, onset_frame))

    t_a = frame_index_to_time(a.frame_index, ts_a)
    t_b = frame_index_to_time(b.frame_index, ts_b)

    assert (t_b - t_a) == pytest.approx(delay_s, abs=0.001)
