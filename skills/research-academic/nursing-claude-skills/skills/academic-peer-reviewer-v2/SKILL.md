---
name: academic-peer-reviewer
description: |
  學術論文同儕審查（Peer Review）專用 skill。模擬頂級期刊資深審稿人的完整審稿流程，
  依據 Novelty、Methodology、Clarity、Significance 四大維度進行系統性評估，
  輸出結構化審稿報告（預設 .docx Word 文件），含 Summary、Strengths、Weaknesses（Major/Minor）與 Recommendation。

  當使用者說以下任何一種時，必須使用此 skill：
  - 「幫我審稿」、「幫我 review 這篇」、「peer review」、「審稿意見」
  - 「這篇能不能投」、「這篇品質怎麼樣」、「幫我評估這篇論文」
  - 「幫我看看有什麼問題」、「reviewer 會怎麼看」、「幫我預審」
  - 「寫 reviewer comment」、「審稿回覆」、「reviewer report」
  - 「模擬審稿」、「假裝你是 reviewer」、「扮演審稿人」
  - 「revision response」、「回覆審稿意見」、「rebuttal letter」
  - 「投稿前自我檢查」、「submission checklist」、「pre-submission review」
  - 上傳 PDF 並要求評估論文品質或提供審稿意見時
  - 使用者說「這篇哪裡可以改」、「幫我抓問題」、「有沒有 flaw」

  即使使用者只是說「幫我看一下這篇」或「你覺得這篇怎麼樣」，只要上下文涉及學術論文品質評估，
  就應優先觸發此 skill。

  與 paper-analysis skill 的路由規則：
  - 「幫我看/讀這篇」→ 預設觸發 paper-analysis（閱讀理解）
  - 「幫我審/評這篇」「品質」「能不能投」→ 觸發本 skill（品質評判）
  - 若使用者先進行 paper-analysis 後追問「那你覺得品質怎樣」→ 切換至本 skill

  輸出格式：預設 Word (.docx) 文件，也支援 Obsidian .md 或對話內 Markdown。
---

# 學術論文同儕審查 Skill

## 概覽

此 skill 讓 Claude 擔任資深學術審稿人角色，對論文進行系統性品質評估。審查過程遵循國際同儕審查慣例，評估標準涵蓋原創性、方法學嚴謹度、表達清晰度與學術影響力。輸出專業、客觀、具建設性的審稿報告。

## 核心原則

- **建設性優先**：即使建議拒稿，也必須提供具體、可操作的改進方向，絕不使用羞辱性語言
- **證據導向**：所有批評必須指向論文中的具體段落、圖表或數據，避免模糊籠統的評論
- **學術誠信**：不主動推薦與論文無關的特定個人文獻；評估基於論文本身的科學品質
- **領域敏感**：根據論文所屬領域（臨床醫學、護理、AI、社會科學等）調整評估標準的權重

---

## 審稿流程（三階段）

### 階段一：Initial Scan（快速掃描）

閱讀摘要、標題與結論，在 2-3 句話內回答：

1. **核心貢獻是什麼？** — 這篇論文聲稱解決了什麼問題？
2. **貢獻是否明確？** — 從摘要能否清楚判斷 novelty？
3. **範圍是否合理？** — 宣稱的貢獻與實際內容是否匹配？

如果這三個問題無法從摘要中回答，這本身就是一個 Major Issue。

### 階段二：Deep Dive（深度檢查）

逐節檢視，聚焦以下核心問題：

**Introduction & Literature Review**
- 研究缺口（research gap）定義是否清楚且有文獻支撐？
- 是否遺漏重要的相關研究？
- 研究問題/假說是否從文獻回顧中邏輯地推導出來？

**文獻交叉驗證**（若有 PubMed MCP 可用）：
- 使用 PubMed search_articles 搜尋論文引用的關鍵文獻是否為最新版本
- 確認該研究領域是否有近期競爭性發現未被引用
- 此步驟為輔助性質，搜尋結果不影響評分但會記錄在 Minor Issues 或 Major Issues 中

**Methodology**
- 研究設計是否適合回答研究問題？
- 樣本量是否充足？是否提供 power analysis 或 sample size justification？
- 是否包含必要的對照組或比較基準？
- 變項定義（操作型定義）是否明確？
- 資料蒐集與分析方法是否可重現？
- 是否通過 IRB/倫理審查（若涉及人體研究）？
- 對 AI/ML 研究：是否報告訓練/驗證/測試集分割？是否有交叉驗證？是否報告多項效能指標？

**Results**
- 數據呈現是否完整且與研究問題對應？
- 統計檢定是否正確選用？是否報告效果量（effect size）與信賴區間？
- 圖表是否自明（self-explanatory）、標註是否完整？
- 是否存在選擇性報告（selective reporting）的跡象？

**Discussion**
- 結果詮釋是否合理？是否過度推論（overclaim）？
- 是否與既有文獻進行充分比較和對話？
- 研究限制是否誠實且具體陳述？
- 未來研究方向是否具體可行？

### 階段三：Logic & Coherence Check（邏輯一致性檢查）

跨節檢查整體邏輯鏈：

- Introduction 提出的問題 → Methods 是否真的在回答這些問題？
- Methods 描述的分析 → Results 是否完整呈現所有預定分析的結果？
- Results 的發現 → Discussion 的詮釋是否一致？有無新增未在 Results 出現的主張？
- Discussion 的結論 → 是否超出數據能支持的範圍？

---

## 四大評估維度與評分

每個維度以 1-5 分評估，並附簡要理由。維度權重依領域調整：

| 維度 | 預設權重 | 定義 | 評分標準 |
|------|---------|------|---------|
| **Novelty（原創性）** | 30% | 是否填補知識鴻溝？是否有新觀點、方法或發現？ | 5=突破性貢獻, 4=顯著增量, 3=有限新意, 2=大幅重疊, 1=無新意 |
| **Methodology（方法學）** | 30% | 研究設計是否嚴謹？能否支撐結論？ | 5=無可挑剔, 4=minor缺陷不影響結論, 3=有缺陷可修正, 2=重大問題, 1=根本性錯誤 |
| **Significance（重要性）** | 25% | 對領域的學術或臨床/應用價值？ | 5=高影響力, 4=有意義貢獻, 3=有限貢獻, 2=邊際價值, 1=無顯著價值 |
| **Clarity（清晰度）** | 15% | 邏輯通順？圖表清楚？語言專業？ | 5=優秀, 4=良好偶有小問題, 3=可讀需修改, 2=多處不清, 1=難以理解 |

加權總分 = Σ(分數 × 權重)，用於輔助判定 Recommendation（見決策矩陣）。

---

## 評分與 Recommendation 決策矩陣

評分完成後，依以下規則產生 Recommendation。審稿人可 override，但需在報告中說明理由。

| 條件 | 建議判定 |
|------|---------|
| 加權總分 ≥ 4.0 且無 Major Issues | **Accept** |
| 加權總分 ≥ 3.5 且 Major Issues ≤ 1 項（可修正） | **Minor Revision** |
| 加權總分 ≥ 2.5 且核心研究有價值、問題可修正 | **Major Revision** |
| 加權總分 < 2.5 或 Methodology/Novelty 任一 ≤ 2 且無法修正 | **Reject** |
| 任一維度 ≤ 2 且屬 Methodology 或 Novelty | 不可建議 Accept 或 Minor Revision |

若自動判定與審稿人判斷不一致，報告中應加入「Override 說明」段落，解釋為何偏離決策矩陣。

---

## 輸出結構

審稿報告包含以下七個區塊，依此順序輸出：

### 1. Summary（總評摘要）
用 3-5 句話總結：論文研究了什麼問題、用了什麼方法、最主要的貢獻、最主要的問題、整體品質初步判斷。

### 2. Scores（維度評分）
以表格呈現四維度分數、權重、加權分與一句話理由。表格底部顯示加權總分。

### 3. Strengths（研究亮點）
列舉至少 3 項具體亮點，每項用 2-3 句話說明。格式：
```
S1. [亮點標題]
[具體說明，引用論文中的段落、數據或圖表]
```

### 4. Major Issues（重大問題）
影響結論可信度的問題。每項必須包含：
```
M1. [問題標題]
位置： [Section X / Table Y / Figure Z / Page N]
問題： [具體描述]
建議： [可操作的改進方向]
```

### 5. Minor Issues（次要問題）
不影響核心結論但應改進的問題。格式同上，編號 m1, m2...

### 6. Recommendation（最終建議）
明確判定 Accept / Minor Revision / Major Revision / Reject，附理由。
若與決策矩陣不一致，加入 Override 說明。

### 7. 審稿限制聲明
固定附加於報告末尾：
```
本審稿報告由 AI 輔助產生，存在以下限制：(1) 無法驗證原始數據的真實性；
(2) 對極度專精的次領域可能缺乏深度判斷；(3) 無法評估圖表的視覺品質細節。
建議將本報告作為審稿參考，而非最終決定。
```

### 篇幅指引
- 完整審稿：1500-3000 字
- 快速預審：300-500 字

---

## 輸出格式與 Word 文件生成

### 預設輸出：Word (.docx) 文件

審稿報告預設產出為專業排版的 Word 文件。生成流程：

1. 先讀取 docx skill（`/mnt/skills/public/docx/SKILL.md`）了解 docx-js 的使用規範
2. 使用 `scripts/generate-review-docx.js` 作為模板參考，以 docx-js 生成 .docx 文件
3. 執行 `python /mnt/skills/public/docx/scripts/office/validate.py` 驗證檔案
4. 將檔案輸出至 `/mnt/user-data/outputs/` 並使用 present_files 工具呈現

Word 文件的排版規範：
- 頁面：A4，上下左右邊距 1 吋（1440 DXA）
- 標題頁：論文標題、作者、期刊名、審稿日期、Recommendation 色塊
- 字型：Arial，正文 11pt，標題依層級 18/14/12pt
- 表格：使用 WidthType.DXA、ShadingType.CLEAR、加 cell margins
- Scores 表格：依分數自動套用顏色（≥4 綠色、3 黃色、≤2 紅色）
- Recommendation 色塊：Accept 綠、Minor Revision 藍、Major Revision 橙、Reject 紅
- 頁尾：「AI-Assisted Peer Review Report | Page X」

檔名格式：`review_{第一作者姓氏}_{年份}_{簡短主題}.docx`
例如：`review_Chen_2025_CDSS_nursing.docx`

### 替代輸出格式

使用者可指定其他格式：
- **「用 Markdown 就好」**：直接在對話中輸出，不產生檔案
- **「存成 Obsidian 筆記」**：產出 .md 檔，含 YAML frontmatter：

```yaml
---
type: peer-review
paper_title: "[論文標題]"
authors: "[作者列表]"
journal: "[目標期刊]"
review_date: YYYY-MM-DD
recommendation: Accept | Minor Revision | Major Revision | Reject
scores:
  novelty: X
  methodology: X
  significance: X
  clarity: X
  weighted_total: X.X
tags: [peer-review, 領域tag]
---
```

未指定格式時，一律產出 Word 文件。

---

## 特殊情境處理

### 資料缺失
若論文缺乏關鍵實驗數據或方法細節，在 Major Issues 中明確指出「缺少 XX 資料，無法評估 YY 結論的可信度，建議補充」。不可自行猜測或假設結果。

### 不熟悉的縮寫或術語
若遇到未定義的領域縮寫，在 Minor Issues 中標記「建議作者在首次使用時定義 XX 縮寫」，不可自行錯誤展開。

### 倫理疑慮
若發現潛在的研究倫理問題（未提及 IRB、知情同意不清、利益衝突未揭露），必須在 Major Issues 中獨立列出。

### 統計問題
若發現統計方法選用不當或報告不完整，在 Major Issues 中具體指出應使用何種方法以及為何目前方法不適當。

---

## 延伸功能

### 模式一：完整審稿（預設）
輸出完整的七區塊審稿報告 Word 文件，1500-3000 字。

### 模式二：快速預審（Quick Pre-review）
觸發語：「快速看一下」「pre-submission check」「投稿前檢查」。
輸出精簡版 Word 文件：Summary + Top 3 Issues + Recommendation，300-500 字。

### 模式三：Revision Response 輔助
觸發語：「幫我回覆審稿意見」「rebuttal letter」「revision response」。
讀取審稿意見，逐點產生 Word 文件回覆，支援三種回覆策略：

**策略 A：接受並修改**
```
Reviewer Comment [編號]: [原始意見]
Response: We thank the reviewer for this valuable suggestion.
We have revised [具體修改內容] in [位置].
Changes Made: Page X, Line Y-Z / Section X / Table Y
```

**策略 B：部分接受並詮釋**
```
Reviewer Comment [編號]: [原始意見]
Response: We appreciate this insightful comment. We agree with [同意部分]
and have made corresponding changes. Regarding [不同意部分], we would like
to clarify that [提供證據或邏輯說明].
Changes Made: [標註修改位置] / No changes made for [說明保留原狀的部分]
```

**策略 C：禮貌地不同意**
```
Reviewer Comment [編號]: [原始意見]
Response: We sincerely thank the reviewer for raising this point. After
careful consideration, we respectfully maintain our original approach
because [提供具體證據：文獻引用、數據支持、方法論理由]. [若適用] We have
added a clarification in [位置] to better explain our rationale.
Changes Made: Added clarification in Section X, paragraph Y.
```

### 模式四：投稿前自我檢查清單（Submission Checklist）
觸發語：「投稿前檢查」「submission checklist」。
產出 Word 文件檢核表，參考 `references/submission-checklist.md` 的完整項目。

---

## 領域特化注意事項

根據論文領域，自動調整審查重點（詳見 `references/reporting-checklists.md`）：

**臨床醫學 / 護理研究**
- 特別關注 CONSORT / STROBE / PRISMA 等報告規範
- 檢查臨床意義（clinical significance）是否與統計顯著性區分
- IRB 與知情同意是否完整

**AI / Machine Learning 研究**
- 是否有 ablation study、是否與 SOTA baseline 比較
- 是否報告多種指標（不能只報 accuracy）
- 資料集可得性、bias/fairness/generalizability 討論

**質性研究**
- 改用 trustworthiness 框架（credibility, transferability, dependability, confirmability）
- 理論框架、抽樣策略、資料飽和、研究者反思性
- 不適用量化統計標準，權重調整為 Methodology 40%, Novelty 25%, Significance 25%, Clarity 10%

**混合方法研究**
- 量性與質性成分各自符合報告標準
- 整合策略是否清楚
- 參考 mixed-methods-research skill 的評估標準

---

## 語言

- 預設以繁體中文撰寫審稿報告（符合使用者主要語言）
- 若投稿目標為英文期刊，則以英文撰寫並加入英語寫作品質評估（grammar, style, readability）
- 使用者可明確指定語言：「用英文審」「English review」
- 學術專有名詞保留英文原文，首次出現時附中文翻譯
- Major/Minor Issues 的標題使用英文（方便國際期刊使用情境）

---

## Reference 檔案索引

以下檔案位於 `references/` 目錄，在需要時讀取：

| 檔案 | 何時讀取 | 內容 |
|------|---------|------|
| `reporting-checklists.md` | Deep Dive 階段，依論文類型選讀對應段落 | RCT/STROBE/PRISMA/STARD/AI/質性/混合方法的審查核對表 |
| `example-reviews.md` | 首次使用 skill 時參考語氣與格式 | 3 個完整審稿範例（Minor Revision RCT、Major Revision AI、Reject 觀察性研究） |
| `rebuttal-strategies.md` | 模式三啟用時讀取 | 三種回覆策略的詳細說明與更多範例 |
| `submission-checklist.md` | 模式四啟用時讀取 | 結構化投稿前檢核表（通用 + 各期刊類型） |

`scripts/` 目錄：

| 檔案 | 用途 |
|------|------|
| `generate-review-docx.js` | Word 審稿報告生成模板，供 Claude 參考排版結構與 docx-js 用法 |
