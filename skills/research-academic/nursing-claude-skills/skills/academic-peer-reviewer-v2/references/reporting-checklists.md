# 審稿常用報告規範速查表

依論文類型快速查找應遵守的報告規範，供審稿時逐項核對。

## 目錄
1. [RCT → CONSORT](#rct)
2. [觀察性研究 → STROBE](#strobe)
3. [系統性回顧 / Meta-analysis → PRISMA](#prisma)
4. [診斷準確性研究 → STARD](#stard)
5. [AI / Machine Learning 研究](#aiml)
6. [質性研究](#qualitative)
7. [混合方法研究](#mixed)
8. [常見統計審查要點](#statistics)

---

## RCT（隨機對照試驗）→ CONSORT

核對要點：
- 標題是否標示為 RCT？
- 是否有 CONSORT flow diagram（受試者流程圖）？
- 隨機化方法：序列產生、分配隱藏、盲法
- 主要結局指標是否預先定義且明確？
- ITT（intention-to-treat）分析是否執行？
- 是否註冊臨床試驗（trial registration number）？
- 不良事件是否報告？

---

## 觀察性研究 → STROBE

核對要點（依 cohort / case-control / cross-sectional 微調）：
- 研究設計是否在標題或摘要中明確標示？
- 納入排除標準是否清楚？
- 暴露與結果的測量方式是否明確？
- 是否處理潛在混淆因子（confounders）？
- 是否報告 missing data 的數量與處理方式？
- 是否提供 effect size + 95% CI？

---

## 系統性回顧 / Meta-analysis → PRISMA

核對要點：
- 是否提供 PRISMA flow diagram？
- 搜尋策略是否完整可重現（資料庫、關鍵字、搜尋日期）？
- 納入/排除標準是否明確？
- 品質評估工具為何（RoB 2, NOS, CASP 等）？
- 若為 meta-analysis：異質性指標（I², Q test）是否報告？
- 是否進行敏感度分析（sensitivity analysis）？
- 是否評估 publication bias（funnel plot, Egger's test）？
- 是否事先註冊 protocol（PROSPERO）？

---

## 診斷準確性研究 → STARD

核對要點：
- Index test 與 reference standard 是否清楚定義？
- 是否報告 sensitivity, specificity, PPV, NPV, LR+, LR-？
- 是否有 STARD flow diagram？
- 受試者是否代表目標族群（spectrum bias）？
- 盲法：解讀者是否不知道另一項檢測的結果？
- 是否報告 indeterminate / inconclusive results？

---

## AI / Machine Learning 研究

核對要點：
- 資料集來源、大小、分佈是否清楚？
- 訓練/驗證/測試集是否獨立且不重疊？
- 是否使用交叉驗證（cross-validation）？
- 是否報告多項效能指標（accuracy, precision, recall, F1, AUC-ROC, AUC-PR）？
- 是否與 baseline / SOTA 模型比較？
- 是否有 ablation study 說明各組件貢獻？
- 是否報告 confidence interval 或 statistical test？
- 是否討論 external validation / generalizability？
- 是否討論 bias, fairness, interpretability？
- 程式碼與資料是否公開或有可得性聲明？

---

## 質性研究

核對要點（改用 trustworthiness 框架）：
- 理論框架 / 研究取徑是否清楚（現象學、紮根理論、民族誌等）？
- 抽樣策略是否適當（purposive, theoretical, snowball 等）？
- 是否達到資料飽和（data saturation）？如何判定？
- 資料蒐集方式是否詳細描述（訪談指引、觀察紀錄）？
- 編碼過程是否透明（initial coding, axial coding, theme development）？
- 是否有 inter-coder reliability 或 member checking？
- 研究者反思性（reflexivity）是否陳述？
- 是否提供 thick description 支持可轉移性？

---

## 混合方法研究

核對要點：
- 混合設計類型是否明確（convergent, explanatory sequential, exploratory sequential 等）？
- 量性與質性成分是否各自符合該方法的報告標準？
- 整合策略（integration）是否清楚說明？
- 整合發生在哪個階段（設計、方法、詮釋）？
- 若有 joint display，是否清楚呈現兩種資料的對話？

---

## 常見統計審查要點

不論研究類型，以下統計問題經常出現：

| 問題類型 | 檢查要點 |
|---------|---------|
| 多重比較 | 是否校正（Bonferroni, FDR 等）？ |
| 效果量 | 是否報告 Cohen's d, η², OR 等？ |
| 信賴區間 | 是否報告 95% CI 而非僅 p-value？ |
| 常態性假設 | 是否檢驗（Shapiro-Wilk 等）？非常態時是否改用無母數檢定？ |
| 樣本量 | 是否有 a priori power analysis？是否可能 underpowered？ |
| Missing data | 缺失量、缺失模式、處理方法（listwise, MICE, etc.）？ |
| 選擇性報告 | 是否所有預定分析的結果都有報告？ |
