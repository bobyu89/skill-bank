---
name: pubmed-daily-bundle
description: |
  每日自動化 PubMed 文獻搜尋、全文抓取、分析與打包的完整排程 skill。
  專為 CDSS（臨床決策支援系統）與 AI 輔助護理教育兩大主題設計，限定 PMC 開放全文。

  當使用者說以下任何一種時，必須使用此 skill：
  - 「幫我執行今天的文獻排程」、「執行今日文獻搜尋」
  - 「幫我找 PubMed 文獻」、「搜尋 CDSS / 護理教育論文」
  - 「跑一次文獻排程」、「文獻打包」、「PubMed bundle」
  - 「今天要看哪些論文」、「給我今天的文獻」
  - 使用者提到 CDSS、clinical decision support、nursing education + AI 等關鍵字並要求找文獻

  輸出格式：互動式大綱預覽（使用者選擇）→ Obsidian .md 筆記 + PMC 全文 PDF → ZIP 打包下載
---

# PubMed Daily Bundle Skill

## 概覽

這個 skill 是 Bob 的個人每日文獻學習排程系統，整合以下五個步驟：

```
① PubMed 搜尋（PMC only）
    ↓
② 大綱預覽 → 使用者選擇是否深入分析
    ↓（有興趣的篇目）
③ paper-analysis SKILL 全文批判性分析
    ↓
④ Obsidian Markdown 筆記生成（含 wikilink）
    ↓
⑤ PMC 全文 PDF + .md 筆記 → ZIP 打包下載
```

---

## 使用流程

### Step 1 — 判斷執行模式

根據使用者輸入判斷模式：

| 輸入 | 執行模式 |
|------|---------|
| 「執行今日排程」/ 無指定 | **排程模式**：依週期主題自動選擇關鍵字組合搜尋 |
| 「搜尋 [特定主題]」 | **指定模式**：使用者指定主題，覆蓋預設關鍵字 |
| 「繼續上次的文獻」 | **延續模式**：搜尋近 3 天內的 related articles |

---

### Step 2 — 執行 PubMed 搜尋

**必要篩選條件（每次都要加）：**
- `free full text[filter]` — 限定 PMC 開放全文
- `date_from: 2020`, `date_to: 2025` — 近 5 年
- `max_results: 8` — 預先抓多一點，後續篩出 3–5 篇
- `sort: pub_date` — 最新優先

**關鍵字組合**（依本週週期輪替，見下方排程表）：
讀取 `references/keyword_strategy.md` 取得完整 MeSH + 自由詞組合。

**週期輪替排程：**
| 星期 | 主題 | 使用關鍵字組合 |
|------|------|--------------|
| 一 / 四 | CDSS 主題 | `QUERY_CDSS` |
| 二 / 五 | 護理教育主題 | `QUERY_NURSING_EDU` |
| 三 / 六 | 交叉主題 | `QUERY_CROSS` |
| 日 | 週回顧（不搜新文） | — |

取得 PMID 後，立即用 `convert_article_ids` 確認哪些有 PMCID（無 PMCID 的直接排除）。

---

### Step 3 — 大綱預覽與使用者選擇

取得 metadata 後，對每篇輸出：

```
篇 N of M  [主題標籤]
標題（完整）
作者 / 期刊 / 年份 / DOI
研究問題：[一句話，聚焦 PICO 的 P + O]
大綱：
  ① [研究設計與方法一句話]
  ② [主要發現與數據]
  ③ [臨床/教育意涵]
[有興趣，深入分析] [略過此篇]
```

**等待使用者逐篇選擇後**，才進入 Step 4。
若使用者說「全部分析」，則所有篇目進入 Step 4。
若使用者說「只要前 N 篇」，則按順序取前 N 篇。

---

### Step 4 — 深度分析（呼叫 paper-analysis SKILL）

對每篇選定文獻：

1. 讀取 `/mnt/skills/user/paper-analysis/SKILL.md`
2. 判斷論文類型（SR → PRISMA、AI 模型 → TRIPOD、RCT → CONSORT、觀察性 → STROBE）
3. 執行完整分析框架：
   - PICO / 研究問題
   - 方法學品質（含可信度評估矩陣）
   - 主要發現（含完整數據）
   - 批判性評論（優點 / 限制 / 紅旗）
   - 引用信心聲明

---

### Step 5 — Obsidian 筆記生成

讀取 `/mnt/skills/user/obsidian-markdown/SKILL.md`，依以下規格輸出每篇 `.md`：

**檔名格式：** `@AuthorYear_KeywordTopic.md`

**必要 frontmatter 欄位：**
```yaml
---
title:
aliases: ["@AuthorYear_Topic"]
date: YYYY-MM-DD
tags:
  - literature/[研究類型]
  - topic/CDSS 或 topic/AI-nursing-education
  - status/read
source: PubMed
pmid:
doi:
journal:
year:
authors:
credibility: 高/中/低可信度
zotero: 待手動加入
---
```

**筆記結構：**
- Take-home message callout
- 可信度評估矩陣（表格）
- 基本資訊表
- PICO / 研究問題
- IMRAD / PRISMA 分析
- 批判性評論
- 反向連結 wikilink（接入 `[[CDSS-MOC]]` 或 `[[AI-in-Nursing-MOC]]`）
- 個人反思 + todo task list

---

### Step 6 — 打包 ZIP

執行 `scripts/bundle_generator.py`，打包內容：

```
PubMed_Session_YYYY-MM-DD/
├── 00_INDEX.pdf              ← 封面 + 所有文獻索引一覽
├── 01_@Author_Topic.pdf      ← PMC 全文 PDF（帶研究問題 highlight）
├── 01_@Author_Topic.md       ← Obsidian 筆記
├── 02_...
└── ...
```

呼叫方式：
```python
# 在 bash_tool 中執行
python3 /path/to/scripts/bundle_generator.py \
  --articles '[{"pmcid":"PMCxxxxx","title":"...","doi":"...","authors":"...","journal":"...","year":"2025","topic_tag":"CDSS","rq":"...","author_key":"Author2025_Topic"}]' \
  --full-text-json '/path/to/full_text_result.json' \
  --notes-dir '/path/to/obsidian_notes/' \
  --output '/mnt/user-data/outputs/PubMed_Bundle_YYYY-MM-DD.zip'
```

完成後用 `present_files` 呈現 ZIP 檔給使用者。

---

## 依賴的其他 Skills

此 skill 在 Step 4–5 會主動呼叫：
- `/mnt/skills/user/paper-analysis/SKILL.md`
- `/mnt/skills/user/obsidian-markdown/SKILL.md`

執行前先讀取這兩個 SKILL.md，確保分析格式正確。

---

## 重要注意事項

1. **PMC 全文優先**：沒有 PMCID 的文獻直接跳過，不向使用者呈現
2. **每日不重複**：若同一篇 PMID 出現過，標記 `[已讀]` 並排除（未來可擴充 session log）
3. **ZIP 命名**：統一用 `PubMed_Bundle_YYYY-MM-DD.zip`
4. **Zotero 整合**：目前為手動，筆記中的 `zotero: 待手動加入` 提醒使用者
5. **引用合規**：所有輸出必須標示 `Based on articles retrieved from PubMed` 並附 DOI 連結

---

## 參考資源

- 關鍵字策略：`references/keyword_strategy.md`
- PDF + ZIP 生成腳本：`scripts/bundle_generator.py`
