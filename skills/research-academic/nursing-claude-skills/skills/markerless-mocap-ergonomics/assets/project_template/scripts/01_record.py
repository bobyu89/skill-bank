"""步驟 01：多相機同步錄製一次試作。

錄製流程提醒：
    1. 執行本腳本後會有倒數；倒數結束即開始錄製。
    2. **錄製開始後的前 2 秒內觸發一次 LED 閃光**（所有相機都要看得到）。
    3. 閃光後再開始動作。
    4. 閃光是事後對齊各相機時間軸的唯一依據，漏做則該次試作無法使用。

用法：
    python scripts/01_record.py --trial T001 --duration 30
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from {{PACKAGE}}.capture.config import load_camera_config  # noqa: E402
from {{PACKAGE}}.capture.webcam import MultiCameraRecorder  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description="多相機同步錄製")
    parser.add_argument("--trial", required=True, help="試作代碼，如 T001")
    parser.add_argument("--duration", type=float, default=30.0, help="錄製秒數")
    parser.add_argument("--countdown", type=int, default=5, help="開始前倒數秒數")
    parser.add_argument("--config", type=Path, default=ROOT / "configs" / "cameras.yaml")
    parser.add_argument("--out", type=Path, default=ROOT / "data" / "raw")
    args = parser.parse_args()

    settings = load_camera_config(args.config)
    session_dir = args.out / f"{datetime.now():%Y%m%d}_{args.trial}"

    if session_dir.exists() and any(session_dir.iterdir()):
        print(f"錯誤：{session_dir} 已存在且非空。請更換試作代碼，避免覆蓋既有資料。")
        return 1

    recorder = MultiCameraRecorder(settings)

    print(f"開啟 {len(settings)} 台相機……")
    reports = recorder.open_all()

    # 設定未生效時必須讓使用者知道。自動對焦未關會使校正失效，
    # open_camera() 已將其視為致命錯誤；其餘項目在此僅警告。
    for rep in reports:
        if not rep.all_ok:
            print(f"\n相機 {rep.name} 有設定未生效：")
            for chk in rep.failures():
                print(f"    {chk.prop_name}：要求 {chk.requested}，實際 {chk.actual}")
            print("    請確認這些差異是否可接受後再繼續。")

    try:
        for i in range(args.countdown, 0, -1):
            print(f"  {i} …")
            time.sleep(1.0)
        print(">>> 開始錄製。請立即觸發 LED 閃光，閃光後再開始動作。")

        result = recorder.record(session_dir, args.duration)
    finally:
        recorder.close_all()

    print(f"\n錄製完成：{session_dir}")
    print(f"實際時長 {result.duration_s:.2f} 秒\n")
    for name, stats in result.per_camera.items():
        print(
            f"    {name}：{stats['frames']:.0f} 幀，"
            f"實際 {stats['actual_fps']:.1f} fps（目標 {stats['target_fps']:.0f}），"
            f"掉幀 {stats['dropped']:.0f}"
        )

    warnings = result.quality_warnings()
    meta = {
        "trial": args.trial,
        "recorded_at": datetime.now().isoformat(),
        "duration_s": result.duration_s,
        "cameras": {s.name: s.__dict__ for s in settings},
        "stats": result.per_camera,
        "quality_warnings": warnings,
    }
    with (session_dir / "meta.json").open("w", encoding="utf-8") as fh:
        json.dump(meta, fh, ensure_ascii=False, indent=2)

    if warnings:
        print("\n品質警告（本次試作已標記為品質可疑）：")
        for w in warnings:
            print(f"    - {w}")
        print("\n建議重錄，或於後續分析中將本次試作列為敏感度分析對象。")
        return 2

    print("\n品質檢查通過。下一步：python scripts/02_check_sync.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
