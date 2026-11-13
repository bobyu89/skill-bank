"""步驟 02：分析 LED 閃光，計算各相機的時間偏移。

本腳本輸出的 sync.json 是後續三維重建的必要輸入——
沒有它，各相機的幀無法對應到同一時刻，三角測量結果會失真。

用法：
    python scripts/02_check_sync.py data/raw/20260801_T001
    python scripts/02_check_sync.py data/raw/20260801_T001 --roi 800 100 200 200
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from {{PACKAGE}}.capture.sync_led import compute_sync_offsets  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

# 同步誤差門檻（毫秒）。超過此值時三角測量會因各相機看到的不是同一時刻
# 而產生系統性誤差，尤其在快速動作時更明顯。
MAX_ACCEPTABLE_SPREAD_MS = 10.0


def main() -> int:
    parser = argparse.ArgumentParser(description="以 LED 閃光計算相機時間偏移")
    parser.add_argument("session_dir", type=Path, help="錄製輸出目錄")
    parser.add_argument(
        "--roi",
        type=int,
        nargs=4,
        metavar=("X", "Y", "W", "H"),
        help="LED 所在區域。強烈建議指定——全畫面平均會被人員移動稀釋，大幅降低閃光對比",
    )
    parser.add_argument("--search-frames", type=int, default=300, help="在前 N 幀內搜尋閃光")
    parser.add_argument("--reference", help="基準相機名稱，預設取第一台")
    args = parser.parse_args()

    if not args.session_dir.exists():
        print(f"找不到目錄 {args.session_dir}")
        return 1

    names = sorted(p.stem for p in args.session_dir.glob("*.avi"))
    if not names:
        print(f"{args.session_dir} 中沒有 .avi 影片")
        return 1

    print(f"分析 {len(names)} 台相機：{', '.join(names)}\n")

    roi = tuple(args.roi) if args.roi else None
    if roi is None:
        print("提醒：未指定 --roi，將以全畫面平均亮度偵測。")
        print("      若對比不足，請用影片播放器找出 LED 位置後以 --roi 指定。\n")

    report = compute_sync_offsets(
        args.session_dir,
        names,
        roi=roi,
        search_frames=args.search_frames,
        reference=args.reference,
    )

    print(f"基準相機：{report.reference}\n")
    for name in names:
        onset = report.onsets[name]
        offset_ms = report.offsets_s[name] * 1000.0
        flag = "" if onset.is_reliable else "  ← 對比不足，結果不可信"
        print(
            f"    {name}：偏移 {offset_ms:+7.2f} ms  "
            f"（閃光於第 {onset.frame_index:.2f} 幀，對比 {onset.contrast:.1f}）{flag}"
        )

    unreliable = report.unreliable_cameras()
    print(f"\n整體同步誤差（最大差距）：{report.max_spread_ms:.2f} ms")

    if unreliable:
        print(f"\n以下相機的閃光偵測不可信：{', '.join(unreliable)}")
        print("可能原因：LED 不在該相機視野內、被遮擋、或距離太遠導致對比不足。")
        print("請調整 LED 位置或以 --roi 縮小偵測範圍後重試。")
        return 1

    out = args.session_dir / "sync.json"
    with out.open("w", encoding="utf-8") as fh:
        json.dump(
            {
                "reference": report.reference,
                "offsets_s": report.offsets_s,
                "max_spread_ms": report.max_spread_ms,
                "roi": list(roi) if roi else None,
            },
            fh,
            ensure_ascii=False,
            indent=2,
        )
    print(f"\n已寫出 {out}")

    if report.max_spread_ms > MAX_ACCEPTABLE_SPREAD_MS:
        print(
            f"\n警告：同步誤差 {report.max_spread_ms:.2f} ms 超過 "
            f"{MAX_ACCEPTABLE_SPREAD_MS:.0f} ms 門檻。"
        )
        print("快速動作的三維重建會因此產生系統性誤差。建議檢查是否有相機掉幀嚴重。")
        return 2

    print("同步品質良好。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
