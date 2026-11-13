# Revision Response 回覆策略指南

## 目錄
1. [策略總覽](#策略總覽)
2. [策略 A：接受並修改](#策略A)
3. [策略 B：部分接受並詮釋](#策略B)
4. [策略 C：禮貌地不同意](#策略C)
5. [通用撰寫原則](#通用原則)
6. [常見情境對應策略](#情境對應)

---

## 策略總覽 {#策略總覽}

| 策略 | 適用場景 | 核心語氣 | 比例估計 |
|------|---------|---------|---------|
| A. 接受並修改 | 審稿人指出確實存在的問題 | 感謝 + 具體修改 | ~50-60% |
| B. 部分接受 | 建議有道理但不完全適用 | 感謝 + 部分修改 + 解釋保留部分 | ~20-30% |
| C. 禮貌不同意 | 有充分理由維持原狀 | 感謝 + 證據 + 維持但加說明 | ~10-20% |

黃金法則：每個回覆都以感謝開頭，每個不同意都附帶證據。

---

## 策略 A：接受並修改 {#策略A}

### 模板

```
Reviewer Comment [X]:
[原始意見的忠實摘要]

Response:
We thank the reviewer for this valuable observation. We have [具體修改動作].
Specifically, we [修改的詳細內容].

Changes Made:
- [Page X, Line Y-Z]: [描述修改]
- [Table/Figure Z]: [描述修改]
```

### 範例

**Reviewer:** "The authors should report effect sizes alongside p-values."

```
Response:
We thank the reviewer for this important suggestion. We have added Cohen's d
for all pairwise comparisons and partial eta-squared for ANOVA results
throughout the Results section.

Changes Made:
- Table 2 (Page 8): Added Cohen's d column for primary outcomes
- Table 3 (Page 10): Added partial η² for interaction effects
- Section 3.2 (Page 9, Lines 12-15): Added narrative interpretation of
  effect sizes
```

---

## 策略 B：部分接受並詮釋 {#策略B}

### 模板

```
Reviewer Comment [X]:
[原始意見的忠實摘要]

Response:
We appreciate this insightful comment. We agree that [同意的部分] and have
made corresponding changes. Regarding [不同意的部分], we would like to
clarify that [解釋原因，附證據或引用].

Changes Made:
- [位置]: [描述已做的修改]
- No changes made for [保留原狀的部分]: [簡述理由]
```

### 範例

**Reviewer:** "The sample size of 120 appears small. A larger sample with over 500 participants would strengthen the findings considerably."

```
Response:
We appreciate the reviewer's concern about sample size adequacy. We agree
that larger samples generally increase statistical power, and we have added
a formal a priori power analysis to the Methods section demonstrating that
our sample of 120 provides >80% power to detect medium effect sizes
(d=0.50) at α=0.05 (G*Power 3.1). While a sample of 500+ would certainly
narrow confidence intervals, our current sample meets established guidelines
for the analytical approach used (Tabachnick & Fidell, 2019).

We have also added a discussion of sample size as a study limitation.

Changes Made:
- Section 2.3 (Page 6, Lines 8-14): Added power analysis
- Section 5.3 (Page 16, Line 22): Added sample size limitation
```

---

## 策略 C：禮貌地不同意 {#策略C}

### 模板

```
Reviewer Comment [X]:
[原始意見的忠實摘要]

Response:
We sincerely thank the reviewer for raising this important point. After
careful consideration, we respectfully maintain our original approach
because [理由一：文獻支持]. Furthermore, [理由二：方法論論據].

To address the reviewer's concern, we have added [補充說明/額外分析]
to strengthen transparency.

Changes Made:
- [位置]: Added clarification regarding [相關段落]
```

### 範例

**Reviewer:** "The authors should use a mixed-effects model instead of repeated-measures ANOVA."

```
Response:
We sincerely thank the reviewer for this methodological suggestion. After
careful consideration, we respectfully maintain our use of repeated-measures
ANOVA for the following reasons: (1) our data meet the sphericity assumption
(Mauchly's test: χ²=3.21, p=0.36), (2) we have no missing data points due
to our study design, and (3) when assumptions are met, RM-ANOVA and
mixed-effects models produce equivalent results (Barr et al., 2013).

To address the reviewer's concern, we have added a supplementary analysis
using linear mixed-effects models (lme4 package, R), confirming that results
are consistent across both approaches (Supplementary Table S2).

Changes Made:
- Section 2.5 (Page 7, Lines 18-22): Added explicit reporting of
  sphericity test results
- Supplementary Materials: Added Table S2 with mixed-effects model results
  for comparison
```

### 策略 C 的注意事項

- 永遠不要讓語氣變成「你錯了」，而是「我們有理由這樣做」
- 即使維持原狀，也應至少做一個小修改（如加入說明段落），展示你認真考慮了建議
- 提供可驗證的證據：文獻引用、補充分析、數據
- 如果審稿人的建議在理論上更好但實務上不可行（如需要額外 6 個月收資料），誠實說明限制

---

## 通用撰寫原則 {#通用原則}

1. **逐條回覆**：不要合併多個 comment 的回覆，每條獨立回應
2. **先摘要再回覆**：用自己的話重述審稿意見，確認理解正確
3. **具體標註修改位置**：Page, Line, Section, Table/Figure 都要標
4. **新增內容用顏色或標記**：在修改稿中用紅字或追蹤修訂標示所有變更
5. **不要防禦性語氣**：避免 "The reviewer misunderstood..." 改為 "We may not have been sufficiently clear..."
6. **回覆長度與問題嚴重性成正比**：Major comment 需要詳細回覆，editorial comment 可以簡短

---

## 常見情境對應策略 {#情境對應}

| 審稿人的要求 | 建議策略 | 備註 |
|-------------|---------|------|
| 要求增加實驗/數據 | B 或 C | 若有資源做就做(A)；沒資源則解釋為何足夠(C) |
| 質疑統計方法 | A 或 C | 若確實有更好方法(A)；若方法合理(C+補充分析) |
| 要求引用更多文獻 | A | 通常直接加入即可 |
| 認為 novelty 不足 | C | 重新強調貢獻，加入更清楚的差異比較表 |
| 語言/格式問題 | A | 直接修正 |
| 要求刪除某段 | B 或 C | 審慎考慮；若內容重要可精簡而非刪除 |
| 建議完全不同的研究設計 | C | 禮貌說明此為不同研究問題，可列為 future work |
