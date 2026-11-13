"""步驟 00：探索相機並驗證多機同時開啟。

每次重新插拔 USB、更換 hub 或增加相機後都必須重跑本腳本，
因為相機索引可能改變，且 USB 頻寬是否足夠只有實測才知道。

用法：
    python scripts/00_discover_cameras.py
    python scripts/00_discover_cameras.py --preview 0 1 2
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from {{PACKAGE}}.capture.discover import (  # noqa: E402
    discover_cameras,
    verify_concurrent_open,
)

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")


def preview(indices: list[int]) -> None:
    """同時顯示多台相機畫面，供人工確認索引與實體相機的對應關係。

    按 q 離開。錄製前務必用此功能確認每個索引對應哪個機位，
    否則後續三維重建會因相機外參張冠李戴而完全錯誤。
    """
    import cv2

    from {{PACKAGE}}.capture.discover import PREFERRED_BACKEND

    caps = {i: cv2.VideoCapture(i, PREFERRED_BACKEND) for i in indices}
    for cap in caps.values():
        cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

    print("預覽中，按 q 結束。請記下每個視窗標題的索引對應哪個機位。")
    try:
        while True:
            for idx, cap in caps.items():
                ok, frame = cap.read()
                if ok and frame is not None:
                    cv2.imshow(f"camera index {idx}", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        for cap in caps.values():
            cap.release()
        cv2.destroyAllWindows()


def main() -> int:
    parser = argparse.ArgumentParser(description="探索可用相機並驗證多機同時開啟")
    parser.add_argument("--max-index", type=int, default=10, help="掃描的最大索引")
    parser.add_argument(
        "--preview", type=int, nargs="*", help="預覽指定索引的畫面以確認機位對應"
    )
    args = parser.parse_args()

    if args.preview:
        preview(args.preview)
        return 0

    print(f"掃描相機索引 0..{args.max_index - 1}\n")
    cameras = discover_cameras(max_index=args.max_index)

    if not cameras:
        print("找不到任何相機。請確認相機已連接且未被其他程式占用。")
        return 1

    print(f"找到 {len(cameras)} 台相機：\n")
    for cam in cameras:
        print(f"[索引 {cam.index}] 後端 {cam.backend}")
        for m in cam.supported_modes:
            flag = "可用" if m.frames_ok else "無法取得影格"
            print(f"    {m.width}x{m.height} @ {m.fps:.0f} fps  — {flag}")
        best = cam.best_mode
        if best:
            print(f"    建議模式：{best.width}x{best.height} @ {best.fps:.0f} fps")
        print()

    indices = [c.index for c in cameras]
    print(f"驗證 {len(indices)} 台相機同時開啟……")
    print("（單台可用不代表多台同時可用；USB 頻寬不足時通常靜默失敗）\n")
    results = verify_concurrent_open(indices)

    failed = [i for i, ok in results.items() if not ok]
    for idx, ok in results.items():
        print(f"    索引 {idx}：{'通過' if ok else '失敗'}")

    if failed:
        print(f"\n索引 {failed} 在多機同時開啟時失敗。建議依序嘗試：")
        print("  1. 將相機分接到不同的 USB 控制器（不同側的實體埠，非同一 hub）")
        print("  2. 使用外接供電的 USB hub")
        print("  3. 降低解析度（1080p 改 720p）")
        return 1

    print("\n全數通過。可進行下一步：相機校正。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
