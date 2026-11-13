#!/usr/bin/env python3
"""Rebuild README.md from sources.json and the SKILL.md files under skills/."""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SK = os.path.join(ROOT, "skills")


def frontmatter(path):
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return {}
    m = re.match(r"﻿?---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    try:
        import yaml
        d = yaml.safe_load(m.group(1))
        if isinstance(d, dict):
            return d
    except Exception:
        pass
    out = {}
    for key in ("name", "description"):
        k = re.search(rf"^{key}:\s*[>|]?-?\s*(.*(?:\n[ \t]+.*)*)", m.group(1), re.M)
        if k:
            out[key] = k.group(1)
    return out


def clean(s, n=180):
    s = re.sub(r"\s+", " ", str(s or "")).strip().strip("\"'").replace("|", "\\|")
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def top_skills(base):
    """SKILL.md files under base that are not nested inside another skill."""
    found = []
    for root, dirs, files in os.walk(base):
        dirs.sort()
        if "SKILL.md" in files:
            found.append(os.path.join(root, "SKILL.md"))
            dirs[:] = []
    return found


def anchor(title, folder):
    return re.sub(r"[^\w\- ]", "", f"{title} {folder}".lower()).replace(" ", "-")


def main():
    src = json.load(open(os.path.join(ROOT, "sources.json"), encoding="utf-8"))
    by_cat = {}
    for e in src["entries"]:
        base = os.path.join(SK, e["path"])
        if e.get("entry"):
            e["skills"] = [os.path.join(base, e["entry"])]
        else:
            e["skills"] = top_skills(base)
        e["single"] = len(e["skills"]) == 1 and os.path.dirname(e["skills"][0]) == base
        by_cat.setdefault(e["path"].split("/")[0], []).append(e)

    total = sum(len(e["skills"]) for e in src["entries"])
    L = ["# Skill Bank", "",
         f"SKILL 收藏庫，依功能與用途分類，目前共 {total} 個。", "",
         "**找 SKILL 的方法**：在本頁用 Ctrl/Cmd + F 搜尋關鍵字（中文用途、英文名稱、原始說明都在表格裡），或從下方分類進去。", "",
         "本頁由 `scripts/build_index.py` 依 `sources.json` 產生，請勿手動編輯。略過未存的大型素材列在 [SKIPPED.md](SKIPPED.md)。", "",
         "## 分類總覽", "", "| 分類 | 收什麼 | 數量 |", "|---|---|---|"]
    for folder, title, what in src["categories"]:
        n = sum(len(e["skills"]) for e in by_cat.get(folder, []))
        L.append(f"| [{title}](#{anchor(title, folder)}) | {what} | {n} |")
    L.append("")

    def source(e):
        v = f" {e['version']}" if e.get("version") else ""
        return f"[{e['repo']}](https://github.com/{e['repo']}){v} `{e['commit']}`（{e['license']}）"

    for folder, title, what in src["categories"]:
        L += [f"## {title} (`{folder}`)", ""]
        ents = sorted(by_cat.get(folder, []), key=lambda e: e["path"])
        if not ents:
            L += ["尚無。", ""]
            continue
        L += ["| 名稱 | 數量 | 用途 | 關鍵字 | 來源 | 存入日期 |", "|---|---|---|---|---|---|"]
        for e in ents:
            name = e["path"].split("/", 1)[1]
            if e["single"]:
                link = os.path.relpath(e["skills"][0], ROOT)
                L.append(f"| [{name}]({link}) | 1 | {e['zh']} | {e['keywords']} | {source(e)} | {e['date']} |")
            else:
                L.append(f"| [{name}](#{e['path'].replace('/', '-')}) | {len(e['skills'])} | {e['zh']} | {e['keywords']} | {source(e)} | {e['date']} |")
        L.append("")
        for e in ents:
            if e["single"]:
                continue
            name = e["path"].split("/", 1)[1]
            L += [f'<a id="{e["path"].replace("/", "-")}"></a>', "", f"### {name}（{len(e['skills'])} 個）", "",
                  f"{e['zh']}。資料夾：[`skills/{e['path']}`](skills/{e['path']})", "",
                  "| SKILL | 原始說明 |", "|---|---|"]
            base = os.path.join(SK, e["path"])
            for p in e["skills"]:
                fm = frontmatter(p)
                rel = os.path.relpath(os.path.dirname(p), base)
                label = clean(fm.get("name") or os.path.basename(rel), 60)
                group = os.path.dirname(rel)
                if group:
                    label = f"{group}/{label}"
                L.append(f"| [{label}]({os.path.relpath(p, ROOT)}) | {clean(fm.get('description'))} |")
            L.append("")

    L += ["## 參考資源（不是 SKILL）", "",
          "以下是軟體、函式庫或 MCP 伺服器本身，repo 裡沒有可存的 SKILL，只記錄連結備查。", "",
          "| 資源 | 是什麼 | 備註 | 記錄日期 |", "|---|---|---|---|"]
    for r in src["references"]:
        L.append(f"| [{r['repo']}](https://github.com/{r['repo']}) | {r['what']} | {r['note']} | {r['date']} |")
    open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"{total} skills indexed")


if __name__ == "__main__":
    main()
