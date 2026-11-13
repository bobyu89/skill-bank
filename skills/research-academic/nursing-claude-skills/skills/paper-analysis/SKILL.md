---
name: paper-analysis
description: |
  專為學術論文閱讀、分析與文獻整理設計的完整工作流程。適用論文類型包括：學術研究論文、系統性回顧（Systematic Review）、Meta-analysis、RCT、AI 模型開發/驗證研究、診斷準確性研究、觀察性研究，以及投稿期刊論文。

  當使用者說以下任何一種時，必須使用此 skill：
  - 「幫我分析/閱讀這篇論文」
  - 「整理文獻」、「文獻回顧」、「幫我看 paper」
  - 「這篇 RCT/systematic review/meta-analysis 在說什麼」
  - 「這篇 AI 模型/deep learning/machine learning 論文怎麼樣」
  - 「幫我看這個 AI 的準確性/performance」
  - 「幫我做文獻摘要表」、「critical appraisal」
  - 「這篇能投哪裡」、「論文結構怎麼樣」
  - 上傳 PDF 且內容為學術論文時
  
  輸出格式：Markdown 摘要、結構化分析報告，或 PDF 文件。
---

# 論文分析 Skill

## 概覽

此 skill 協助使用者對學術論文進行深度閱讀、批判性評讀與文獻整理。依照論文類型採用不同分析框架，輸出結構清晰的中文或英文摘要報告。

---

## 使用流程

1. **⚡ 執行可信度快速評估** → 三核心問題 + 評估矩陣（先定錨，再深挖）
2. **判斷論文類型** → 選擇對應分析框架
3. **執行結構化分析** → 依框架逐項解析
4. **輸出報告** → Markdown 或 PDF，結尾附引用信心聲明

---

## 論文類型與對應框架

### 1. 一般學術研究論文（Original Research）

使用 **IMRAD 框架**分析：

| 項目 | 分析要點 |
|------|---------|
| **Introduction** | 研究背景、研究缺口（research gap）、研究目的/假說 |
| **Methods** | 研究設計、樣本、變項定義、統計方法 |
| **Results** | 主要發現、數據呈現方式、統計顯著性 |
| **Discussion** | 結果詮釋、與文獻比較、限制、未來研究方向 |
| **Conclusion** | 核心主張、臨床/實務意涵 |

---

### 2. RCT（隨機對照試驗）

使用 **CONSORT 框架** + **RoB 2 偏誤評估**：

```
## RCT 分析架構

### 基本資訊
- 標題 / 作者 / 期刊 / 年份 / IF
- 研究設計（parallel / crossover / cluster RCT）
- 試驗註冊號（ClinicalTrials.gov）

### PICO
- P（Population）：研究族群、納入/排除標準
- I（Intervention）：介入措施、劑量、頻率
- C（Comparator）：對照組設計（安慰劑/active control）
- O（Outcome）：主要/次要結果指標、追蹤時間點

### 方法學品質（RoB 2）
- 隨機化流程（D1）
- 分配隱藏（D2）
- 盲化（D3）
- 資料完整性（D4）
- 選擇性報告（D5）
- 整體偏誤風險：低 / 疑慮 / 高

### 結果摘要
- 主要結果（含 95% CI、p-value、effect size）
- NNT / NNH（若適用）
- 不良事件

### 批判性評論
- 優點
- 限制
- 臨床適用性
```

---

### 3. 系統性回顧 / Meta-analysis

使用 **PRISMA 框架** + **GRADE 證據品質**：

```
## Systematic Review / Meta-analysis 分析架構

### 基本資訊
- 標題 / 研究問題 / PROSPERO 註冊號

### 研究問題（PICO/PICOS）

### 文獻搜尋策略
- 搜尋資料庫、關鍵字、搜尋時間範圍
- 篩選流程（PRISMA flow diagram 說明）
- 納入文獻數量與特性

### 統計方法（Meta-analysis 適用）
- 效應量指標（OR / RR / MD / SMD）
- 異質性（I² 值，Q test）
- 統計模型（fixed / random effects）
- 發表偏誤評估（Funnel plot, Egger's test）

### 主要發現
- 統合效應量（含 95% CI）
- 次族群分析（subgroup analysis）
- Sensitivity analysis

### 證據品質（GRADE）
- High / Moderate / Low / Very Low
- 降級原因（偏誤風險、不一致性、不精確性等）

### 批判性評論
- 方法學優缺點
- 臨床意涵
```

---

### 4. AI 模型開發 / 驗證研究

使用 **TRIPOD 框架** + **AI 特有方法學評估**：

```
## AI 模型開發/驗證論文分析架構

### 基本資訊
- 標題 / 作者 / 期刊 / 年份
- 研究類型：模型開發 / 外部驗證 / 開發+驗證

### 臨床問題
- 目標任務（分類/偵測/分割/預測）
- 目標族群與臨床情境
- 預測目標（outcome）

### 資料集
- 資料來源（單中心/多中心/公開資料集）
- 樣本數（訓練 / 驗證 / 測試）
- 資料時間範圍、地區
- 標註方式（gold standard 定義，標註者資格）
- 資料不平衡問題（class imbalance）

### AI 方法與模型架構
- 模型類型：CNN / Transformer / LLM / 傳統 ML
- 具體架構（ResNet / EfficientNet / ViT / GPT 等）
- 預訓練 / Fine-tuning / 從頭訓練
- 輸入格式（影像/文字/結構化資料）
- 資料增強（data augmentation）策略

### 訓練細節
- 超參數（learning rate / batch size / epochs）
- 損失函數（loss function）
- 硬體環境（GPU 規格）
- 可重現性（code/data 是否公開）

### 模型效能指標
- 分類任務：AUC / sensitivity / specificity / F1 / accuracy
- 偵測/分割：IoU / Dice coefficient / mAP
- 預測任務：RMSE / MAE / C-statistic / calibration
- 95% CI 與統計檢定方式

### 臨床實用性評估
- 與臨床醫師/現行標準的比較
- Subgroup 分析（不同年齡/性別/疾病嚴重度）
- 外部驗證（external validation）結果
- 計算複雜度 / 推論時間（inference time）
- 臨床整合可行性

### 可解釋性（Explainability）
- Grad-CAM / SHAP / attention map 等視覺化
- 錯誤案例分析（failure case analysis）

### 偏誤與限制（PROBAST 精神）
- 選樣偏誤（資料來源代表性）
- 標記偏誤（labeling bias）
- 過擬合風險（overfitting）
- 缺乏前瞻性驗證
- 僅限單一機構/族群

### 批判性評論
- 方法學亮點
- 主要弱點
- 臨床落地可行性
```

---

### 5. 診斷準確性研究（Diagnostic Accuracy）

使用 **STARD 框架**：

```
## 診斷準確性研究分析架構

### 基本資訊
- 目標疾病 / 診斷工具（index test）/ 參考標準（reference standard）

### 研究族群
- 納入/排除標準
- 疾病盛行率（prevalence）

### 診斷方法
- Index test 執行方式、判讀標準（cutoff）
- Reference standard 定義（是否為真正 gold standard？）
- 盲化（index test 判讀者是否知道 reference standard 結果）

### 效能指標
- Sensitivity / Specificity
- PPV / NPV（在研究族群盛行率下）
- LR+ / LR−
- AUC / ROC curve
- 95% CI

### 偏誤評估
- 驗證偏誤（verification bias）
- 疾病譜偏誤（spectrum bias）

### 臨床意涵
- 適合做 screening 或 confirmation？
- 與現行診斷方式比較
```

---

### 6. 觀察性研究（Cohort / Cross-sectional / Case-control）

```
## 觀察性研究分析架構

### 研究設計
- 類型：前瞻性 cohort / 回溯性 cohort / cross-sectional / case-control
- 追蹤時間（cohort 適用）

### 研究族群
- 來源、樣本數、代表性

### 暴露/預測因子 與 結果
- 暴露定義與測量方式
- 結果定義與測量方式
- 混淆因子（confounders）控制方法

### 統計分析
- 主要統計方法（logistic regression / Cox regression 等）
- 調整變項
- 效應量（OR / HR / RR，含 95% CI）

### 偏誤評估（NOS 量表精神）
- 選樣偏誤
- 測量偏誤
- 混淆偏誤

### 批判性評論
- 因果推論的侷限
- 臨床意涵
```

---

### 7. 投稿期刊論文評估

```
## 投稿評估框架

### 論文優勢
- 創新性 / novelty
- 方法嚴謹度
- 臨床/實務重要性

### 論文弱點
- 方法學問題
- 樣本數 / power
- 偏誤風險
- 統計問題

### 建議目標期刊
| 期刊名稱 | Impact Factor | 範疇符合度 | 建議理由 |
|---------|--------------|-----------|---------|

### 修改建議
- 必要修改（Major）
- 建議修改（Minor）
```

---

## 文獻整理輸出格式

當使用者需要整理多篇文獻時，依主題輸出對應的**文獻摘要表**：

### 一般文獻摘要表
```markdown
| # | 作者/年 | 研究設計 | 樣本數 | 介入/主題 | 主要結果 | 偏誤風險 | 備註 |
|---|--------|---------|-------|---------|---------|---------|-----|
```

### AI 論文專屬摘要表
```markdown
| # | 作者/年 | 任務 | 模型架構 | 資料集(n) | 驗證方式 | 主要指標 | 外部驗證 | 限制 |
|---|--------|------|---------|---------|---------|---------|---------|-----|
```

---

## ⚡ 通用可信度快速評估模組（Quick Credibility Check）

> 適用所有論文類型。在套用各框架之前，**先執行此模組**，用問題導向而非填表導向來定錨批判性思考。

---

### 三個核心問題（必答）

```
Q1. 這個研究的「對象」能代表你真正關心的病人或情境嗎？
Q2. 這個結果有沒有在不同環境被獨立重複驗證？
Q3. 如果把這個研究結論用在臨床，最可能在哪個環節失敗？
```

這三題沒有標準答案，但任何一題答不出來或答案令人不安，就是值得深挖的紅旗。

---

### 可信度評估矩陣

對每篇論文，依下列五個維度快速評分（🟢 無疑慮 / 🟡 需注意 / 🔴 重大問題）：

| 維度 | 評估問題 | 評級 | 說明 |
|------|---------|------|-----|
| **① 資料真實性** | 資料從哪來？能代表目標族群嗎？標注/測量品質如何？ | 🟢/🟡/🔴 | |
| **② 方法嚴謹度** | 研究設計能回答研究問題嗎？統計方法合適嗎？ | 🟢/🟡/🔴 | |
| **③ 結果可重現性** | 有獨立外部驗證嗎？程式碼/資料有公開嗎？ | 🟢/🟡/🔴 | |
| **④ 臨床情境符合度** | 研究環境與真實臨床的落差有多大？ | 🟢/🟡/🔴 | |
| **⑤ 利益衝突風險** | 資金來源？作者背景？發表偏誤可能性？ | 🟢/🟡/🔴 | |

**整體可信度判斷：**
- 5🟢 → 高可信度，可直接引用
- 3🟢 2🟡 → 中等可信度，引用時需說明限制
- 任一🔴 → 低可信度，引用需謹慎並特別說明

---

### 論文類型專屬紅旗（Red Flags）

**RCT 紅旗：**
- 🚩 未事先登錄試驗（no trial registration）
- 🚩 主要結果中途更換（outcome switching）
- 🚩 脫落率 >20% 且未做 ITT 分析

**AI 論文紅旗：**
- 🚩 只有內部驗證，無外部驗證
- 🚩 測試集與訓練集來自同一資料庫
- 🚩 標注者資格不明或 kappa 未報告
- 🚩 資料集過小（影像分類 < 1000 張）
- 🚩 未報告 95% CI，只報告 point estimate

**診斷準確性紅旗：**
- 🚩 Reference standard 本身不是 gold standard
- 🚩 Case-control design（高估 AUC）
- 🚩 盛行率未報告（PPV/NPV 無法外推）

**Systematic Review 紅旗：**
- 🚩 未登錄 PROSPERO
- 🚩 只納入英文文獻（語言偏誤）
- 🚩 I² > 75% 卻仍做 meta-analysis 且不解釋

---

### 給寫作用的「引用信心聲明」

分析完成後，輸出一句可直接用於寫作的引用建議：

```
【高信心】本研究方法嚴謹，結果可直接作為論點支撐。
【中信心】本研究提供初步證據，建議與其他文獻合併引用，並於 limitation 說明其資料來源限制。
【低信心】本研究存在 [具體問題]，引用時需明確說明為 preliminary evidence，不宜作為主要論點依據。
```

---

### Markdown 輸出（預設）
- 使用結構化標題（##、###）
- 重要數據**粗體**標示
- 統計數字完整呈現（含 CI 和 p-value）
- 結尾附「一句話摘要（Take-home message）」

### PDF 輸出（使用者要求時）
- 參考 `/mnt/skills/public/pdf/SKILL.md`
- 使用 `reportlab` 製作格式化報告
- 包含論文基本資訊頁首、分析內容、評讀結論

---

## 重要注意事項

1. **語言**：使用者用中文提問 → 中文回答；英文提問 → 英文回答
2. **統計數字**：務必精確呈現，不可四捨五入省略 CI
3. **批判性**：分析須客觀，指出研究限制不等於否定研究價值
4. **不確定性**：若論文資訊不足以完整填寫某項，標示「論文未報告」
5. **倫理**：涉及病人資料的論文，關注 IRB 與知情同意的描述

---

## 快速範例

**範例 A：RCT**
使用者輸入「幫我分析這篇 RCT」→ 採用 CONSORT + RoB 2，輸出 PICO + 方法學品質 + 結果摘要

**範例 B：AI 模型論文**
使用者輸入「這篇 deep learning 論文的 performance 怎樣」→ 採用 TRIPOD 框架，重點分析：資料集品質、模型架構、AUC/sensitivity/specificity、是否有外部驗證、臨床落地可行性

**範例 C：整理多篇 AI 文獻**
使用者輸入「幫我整理這幾篇 AI 診斷論文」→ 輸出 AI 專屬摘要表（任務/模型/指標/驗證方式欄位）

---

## 延伸參考
- 若需製作 PDF 報告 → 讀取 `/mnt/skills/public/pdf/SKILL.md`
- 若需製作簡報 → 讀取 `/mnt/skills/public/pptx/SKILL.md`
- 若課堂內容需整理為簡報 → 讀取 `/mnt/skills/user/grad-lecture-to-slides/SKILL.md`
