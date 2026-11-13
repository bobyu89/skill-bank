"""建立無標記動作捕捉專案骨架。

產生的專案包含已測試的擷取層（相機探索、多執行緒錄製、LED 同步次幀內插）、
開發鐵則文件與合成資料測試。建立後立即執行 pytest 應全數通過。

用法：
    python scaffold.py <目標目錄> --package <套件名> --project "<專案名稱>"

範例：
    python scaffold.py ./myproject --package myload --project "產線作業負荷量測"
"""

from __future__ import annotations

import argparse
import keyword
import re
import shutil
import sys
from pathlib import Path

TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "assets" / "project_template"

# 樣板中以字面目錄名 PACKAGE 存放套件，建立時改為實際套件名。
PACKAGE_PLACEHOLDER_DIR = "PACKAGE"

# 以副檔名判斷是否需要做佔位符替換。二進位檔直接複製。
TEXT_SUFFIXES = {".py", ".md", ".toml", ".yaml", ".yml", ".txt", ".cfg", ".json"}

# 樣板中不能直接叫 .gitignore（可能被版控工具忽略而未納入 skill）
RENAME_ON_COPY = {"gitignore": ".gitignore"}


def validate_package_name(name: str) -> None:
    """套件名必須是合法的 Python 識別字，否則 import 會失敗。"""
    if not re.fullmatch(r"[a-z][a-z0-9_]*", name):
        raise ValueError(
            f"套件名 '{name}' 不合法。請使用小寫字母開頭，"
            "僅含小寫字母、數字與底線（例如 myload、nurse_load）"
        )
    if keyword.iskeyword(name):
        raise ValueError(f"套件名 '{name}' 是 Python 保留字")


def substitute(text: str, package: str, project: str) -> str:
    return text.replace("{{PACKAGE}}", package).replace("{{PROJECT}}", project)


def scaffold(target: Path, package: str, project: str, force: bool = False) -> list[Path]:
    """建立專案骨架，回傳已建立的檔案清單。"""
    validate_package_name(package)

    if not TEMPLATE_DIR.exists():
        raise FileNotFoundError(f"找不到樣板目錄 {TEMPLATE_DIR}")

    if target.exists() and any(target.iterdir()) and not force:
        raise FileExistsError(
            f"{target} 已存在且非空。請指定其他目錄，或加上 --force 覆寫。"
        )

    created: list[Path] = []

    for src in sorted(TEMPLATE_DIR.rglob("*")):
        if src.is_dir():
            continue

        rel = src.relative_to(TEMPLATE_DIR)
        parts = [package if p == PACKAGE_PLACEHOLDER_DIR else p for p in rel.parts]
        parts[-1] = RENAME_ON_COPY.get(parts[-1], parts[-1])

        dst = target.joinpath(*parts)
        dst.parent.mkdir(parents=True, exist_ok=True)

        if src.suffix in TEXT_SUFFIXES or src.name in RENAME_ON_COPY:
            # 明確指定 UTF-8：Windows 預設 cp950 會使中文註解讀寫失敗
            content = src.read_text(encoding="utf-8")
            dst.write_text(substitute(content, package, project), encoding="utf-8")
        else:
            shutil.copy2(src, dst)

        created.append(dst)

    # data/ 不進版控但執行時需要，先建好避免首次錄製失敗
    (target / "data" / "raw").mkdir(parents=True, exist_ok=True)

    return created


def main() -> int:
    parser = argparse.ArgumentParser(
        description="建立無標記動作捕捉專案骨架",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("target", type=Path, help="目標目錄")
    parser.add_argument(
        "--package",
        required=True,
        help="Python 套件名（小寫、可含底線，如 myload）",
    )
    parser.add_argument("--project", required=True, help="專案顯示名稱")
    parser.add_argument("--force", action="store_true", help="目標目錄非空時仍覆寫")
    args = parser.parse_args()

    try:
        created = scaffold(args.target, args.package, args.project, args.force)
    except (ValueError, FileExistsError, FileNotFoundError) as exc:
        print(f"錯誤：{exc}", file=sys.stderr)
        return 1

    print(f"已建立 {len(created)} 個檔案於 {args.target.resolve()}\n")
    for p in created:
        print(f"    {p.relative_to(args.target)}")

    print(
        f"""
下一步：

    cd {args.target}
    python -m venv .venv
    .venv\\Scripts\\activate        # Windows；macOS/Linux 用 source .venv/bin/activate
    pip install -e ".[dev]"
    pytest                         # 應全數通過

確認測試通過後，接相機並執行：

    python scripts/00_discover_cameras.py

開發前請先讀 CLAUDE.md 的開發鐵則，以及 docs/ROADMAP.md 的階段順序。
特別注意：自動對焦未關閉會使相機校正失效，且不會有任何錯誤訊息。
"""
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
