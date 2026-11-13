#!/usr/bin/env python3
"""
PubMed Daily Bundle Generator
==============================
用法：
    python3 bundle_generator.py \
        --articles '[{"pmcid":"PMCxxxxx","title":"...","doi":"...","authors":"...","journal":"...","year":"2025","topic_tag":"CDSS","rq":"...","author_key":"Author2025_Topic"}]' \
        --full-text-json '/path/to/full_text_result.json' \
        --notes-dir '/path/to/obsidian_notes/' \
        --output '/mnt/user-data/outputs/PubMed_Bundle_YYYY-MM-DD.zip'

說明：
    - articles: 文章 metadata 的 JSON 字串（list of dicts）
    - full-text-json: PubMed:get_full_text_article 的原始結果 JSON 路徑
    - notes-dir: 已生成的 Obsidian .md 筆記資料夾路徑
    - output: 最終 ZIP 輸出路徑
"""

import argparse
import json
import os
import re
import zipfile
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)

TODAY = datetime.now().strftime("%Y-%m-%d")

# ── 樣式系統 ──────────────────────────────────────────────────────────────────

def build_styles():
    base_text = dict(fontName="Helvetica", leading=14, textColor=colors.HexColor("#222222"))
    return {
        "cover_title": ParagraphStyle("CoverTitle", fontName="Helvetica-Bold", fontSize=22,
            leading=28, spaceAfter=10, textColor=colors.HexColor("#0F6E56"), alignment=1),
        "cover_sub": ParagraphStyle("CoverSub", fontName="Helvetica", fontSize=12,
            leading=18, spaceAfter=6, textColor=colors.HexColor("#555555"), alignment=1),
        "cover_meta": ParagraphStyle("CoverMeta", fontName="Helvetica", fontSize=10,
            leading=15, textColor=colors.HexColor("#888888"), alignment=1),
        "h1": ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=16,
            leading=20, spaceBefore=16, spaceAfter=8, textColor=colors.HexColor("#1a1a2e")),
        "h2": ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=12,
            leading=16, spaceBefore=12, spaceAfter=5, textColor=colors.HexColor("#0F6E56")),
        "body": ParagraphStyle("Body", **{**base_text, "fontSize": 9.5, "spaceAfter": 5}),
        "meta": ParagraphStyle("Meta", **{**base_text, "fontSize": 9,
            "textColor": colors.HexColor("#666666")}),
        "doi": ParagraphStyle("DOI", **{**base_text, "fontSize": 9,
            "textColor": colors.HexColor("#185FA5"), "spaceAfter": 10}),
        "note": ParagraphStyle("Note", fontName="Helvetica-Oblique", fontSize=8.5,
            leading=13, textColor=colors.HexColor("#888888"), spaceBefore=16),
        "idx_title": ParagraphStyle("IdxTitle", fontName="Helvetica-Bold", fontSize=10,
            leading=14, spaceBefore=10, spaceAfter=2, textColor=colors.HexColor("#1a1a2e")),
        "idx_meta": ParagraphStyle("IdxMeta", **{**base_text, "fontSize": 9,
            "textColor": colors.HexColor("#555555"), "spaceAfter": 2}),
        "idx_rq": ParagraphStyle("IdxRQ", fontName="Helvetica-Oblique", fontSize=9,
            leading=13, textColor=colors.HexColor("#333333"), spaceAfter=6),
    }


def safe(text: str) -> str:
    """ASCII-safe + XML-escape for ReportLab."""
    t = str(text).encode("ascii", "replace").decode("ascii")
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def hr(color="#cccccc", thickness=0.5, space=8):
    return HRFlowable(width="100%", thickness=thickness,
                      color=colors.HexColor(color), spaceAfter=space)


# ── INDEX PDF ─────────────────────────────────────────────────────────────────

def make_index_pdf(articles_meta: list, filepath: str, st: dict):
    doc = SimpleDocTemplate(filepath, pagesize=A4,
        leftMargin=2.2*cm, rightMargin=2.2*cm,
        topMargin=2.5*cm, bottomMargin=2.2*cm,
        title=f"PubMed Literature Bundle — {TODAY}")
    story = []

    story.append(Spacer(1, 1.5*cm))
    story.append(Paragraph("PubMed Literature Bundle", st["cover_title"]))
    story.append(Paragraph("CDSS &amp; AI-Assisted Nursing Education", st["cover_sub"]))
    story.append(Spacer(1, 0.4*cm))
    story.append(hr("#1D9E75", 2, 10))
    story.append(Paragraph(
        f"Session date: {TODAY} &nbsp;&nbsp;|&nbsp;&nbsp; Articles: {len(articles_meta)} "
        "&nbsp;&nbsp;|&nbsp;&nbsp; Source: PubMed Central (Open Access)", st["cover_meta"]))
    story.append(Spacer(1, 1*cm))
    story.append(hr())

    story.append(Paragraph("Contents — Article Index", st["h1"]))
    story.append(Spacer(1, 0.3*cm))

    for i, m in enumerate(articles_meta, 1):
        story.append(Paragraph(f"{i}. {safe(m['title'])}", st["idx_title"]))
        story.append(Paragraph(
            f"Authors: {safe(m['authors'])} &nbsp;|&nbsp; "
            f"Journal: {safe(m['journal'])} &nbsp;|&nbsp; Year: {m['year']}",
            st["idx_meta"]))
        story.append(Paragraph(
            f"PMCID: {m['pmcid']} &nbsp;|&nbsp; PMID: {m.get('pmid','')} "
            f"&nbsp;|&nbsp; DOI: https://doi.org/{m['doi']}",
            st["idx_meta"]))
        story.append(Paragraph(f"Research question: {safe(m['rq'])}", st["idx_rq"]))
        story.append(Paragraph(
            f"Files: {safe(m['author_key'])}.pdf &nbsp;/&nbsp; {safe(m['author_key'])}.md",
            st["meta"]))
        story.append(hr("#eeeeee", 0.5, 4))

    story.append(Spacer(1, 1*cm))
    story.append(hr())
    story.append(Paragraph(
        "All articles retrieved from PubMed Central (PMC) Open Access. "
        "For personal academic use only. Cite original sources in publications.",
        st["note"]))

    doc.build(story)
    print(f"[INDEX] {filepath}")


# ── ARTICLE PDF ───────────────────────────────────────────────────────────────

SECTION_KW = {
    "abstract", "introduction", "background", "methods", "method",
    "results", "discussion", "conclusion", "conclusions", "references",
    "acknowledgements", "acknowledgments", "supplementary", "funding",
    "ethics", "limitations", "implications", "summary", "impact",
    "objective", "objectives", "findings", "participants", "statistical",
    "figure", "table", "appendix", "conflict", "authors", "strengths",
    "weakness", "availability", "data sharing",
}


def make_article_pdf(full_text: str, meta: dict, filepath: str, st: dict):
    doc = SimpleDocTemplate(filepath, pagesize=A4,
        leftMargin=2.2*cm, rightMargin=2.2*cm,
        topMargin=2.2*cm, bottomMargin=2.2*cm,
        title=meta["title"], author="PubMed Central",
        subject=f"PMID:{meta.get('pmid','')} | {meta['doi']}")
    story = []

    # 頁首
    story.append(Paragraph(
        f"PubMed Central — Full Text &nbsp;|&nbsp; {safe(meta['topic_tag'])}", st["meta"]))
    story.append(hr("#1D9E75", 2, 8))
    story.append(Paragraph(safe(meta["title"]), st["h1"]))
    story.append(Paragraph(
        f"Authors: {safe(meta['authors'])} &nbsp;|&nbsp; "
        f"{safe(meta['journal'])} &nbsp;{meta['year']}", st["meta"]))
    story.append(Paragraph(
        f"PMCID: {meta['pmcid']} &nbsp;|&nbsp; PMID: {meta.get('pmid','')}", st["meta"]))
    story.append(Paragraph(f"DOI: https://doi.org/{meta['doi']}", st["doi"]))

    # 研究問題 highlight
    rq_data = [[Paragraph(
        f"<b>Research question:</b> {safe(meta['rq'])}", st["body"])]]
    rq_table = Table(rq_data, colWidths=[16.6*cm])
    rq_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E1F5EE")),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#9FE1CB")),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(rq_table)
    story.append(Spacer(1, 10))
    story.append(hr())

    # 全文內容
    for line in full_text.split("\n"):
        stripped = line.strip()
        if not stripped:
            story.append(Spacer(1, 3))
            continue
        s = safe(stripped)
        words = stripped.lower().split()
        is_section = (
            len(stripped) < 65
            and len(words) <= 7
            and not stripped.endswith(".")
            and any(kw in stripped.lower() for kw in SECTION_KW)
        )
        story.append(Paragraph(s, st["h2"] if is_section else st["body"]))

    # 頁尾
    story.append(Spacer(1, 20))
    story.append(hr())
    story.append(Paragraph(
        f"Source: PubMed Central | {meta['pmcid']} | Retrieved {TODAY} "
        "| For personal academic use only.", st["note"]))

    doc.build(story)
    print(f"[PDF] {filepath}")


# ── ZIP 打包 ──────────────────────────────────────────────────────────────────

def make_zip(bundle_dir: str, zip_path: str):
    session_label = f"PubMed_Session_{TODAY}"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for fname in sorted(os.listdir(bundle_dir)):
            fpath = os.path.join(bundle_dir, fname)
            if os.path.isfile(fpath):
                zf.write(fpath, os.path.join(session_label, fname))
    size_kb = os.path.getsize(zip_path) // 1024
    file_count = len([f for f in os.listdir(bundle_dir) if os.path.isfile(
        os.path.join(bundle_dir, f))])
    print(f"[ZIP] {zip_path} ({size_kb} KB, {file_count} files)")
    return size_kb


# ── 解析 PMC 全文 JSON ────────────────────────────────────────────────────────

def load_full_texts(json_path: str) -> dict:
    """從 PubMed MCP 回傳的 JSON 解析出 pmcid → full_text 的對照表"""
    with open(json_path) as f:
        raw = json.load(f)

    # MCP 結果可能包在 list[{"type":"text","text":"...json..."}]
    if isinstance(raw, list) and raw and "text" in raw[0]:
        parsed = json.loads(raw[0]["text"])
    elif isinstance(raw, dict):
        parsed = raw
    else:
        parsed = {"articles": raw}

    result = {}
    for a in parsed.get("articles", []):
        ids = a.get("identifiers", {})
        pmcid = ids.get("pmcid", "")
        if pmcid:
            result[pmcid] = a.get("full_text", "")
    return result


# ── 主程式 ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--articles", required=True, help="JSON string of article metadata list")
    parser.add_argument("--full-text-json", required=True, help="Path to PMC full text JSON")
    parser.add_argument("--notes-dir", required=True, help="Dir containing .md Obsidian notes")
    parser.add_argument("--output", required=True, help="Output ZIP path")
    args = parser.parse_args()

    articles_meta = json.loads(args.articles)
    full_texts = load_full_texts(args.full_text_json)
    st = build_styles()

    bundle_dir = os.path.join(os.path.dirname(args.output), f"_bundle_{TODAY}")
    os.makedirs(bundle_dir, exist_ok=True)

    # 1. 封面索引 PDF
    index_path = os.path.join(bundle_dir, "00_INDEX.pdf")
    make_index_pdf(articles_meta, index_path, st)

    # 2. 各篇 PDF + 複製 .md 筆記
    for i, meta in enumerate(articles_meta, 1):
        pmcid = meta["pmcid"]
        key = meta["author_key"]
        prefix = f"{i:02d}_"

        # 全文 PDF
        full_text = full_texts.get(pmcid, "")
        if not full_text:
            print(f"[WARN] No full text for {pmcid}, skipping PDF")
        else:
            pdf_path = os.path.join(bundle_dir, f"{prefix}{key}.pdf")
            make_article_pdf(full_text, meta, pdf_path, st)

        # Obsidian .md 筆記
        md_src = os.path.join(args.notes_dir, f"@{key}.md")
        if os.path.exists(md_src):
            import shutil
            md_dst = os.path.join(bundle_dir, f"{prefix}@{key}.md")
            shutil.copy2(md_src, md_dst)
            print(f"[MD] {md_dst}")
        else:
            print(f"[WARN] Note not found: {md_src}")

    # 3. ZIP
    size_kb = make_zip(bundle_dir, args.output)
    print(f"\n✓ Bundle complete: {args.output} ({size_kb} KB)")
    print(f"  Contents: {sorted(os.listdir(bundle_dir))}")


if __name__ == "__main__":
    main()
