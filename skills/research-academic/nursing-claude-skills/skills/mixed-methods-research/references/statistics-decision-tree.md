# 統計方法完整決策樹

> 含假設前提檢驗、效應量計算、論文寫作格式

---

## 第一層：確認研究問題類型

```
你的研究問題是？
├─ 描述現狀（樣本特徵）→ 描述統計
├─ 兩組或多組差異 → 差異分析
├─ 變項間的關聯強度 → 相關分析
├─ 用某些變項預測結果 → 迴歸分析
└─ 量表/問卷的品質 → 信效度分析
```

---

## 一、描述統計（Descriptive Statistics）

| 資料類型 | 集中趨勢 | 分散程度 | 呈現方式 |
|---------|---------|---------|---------|
| 連續型（等距/等比） | Mean（平均數） | SD（標準差） | M = x.xx, SD = x.xx |
| 順序型（Ordinal） | Median（中位數） | IQR（四分位距） | Mdn = x, IQR = x–x |
| 類別型（Nominal） | Mode（眾數） | 次數與百分比 | n = xx (xx%) |

---

## 二、差異分析（Group Comparison）

### 2.1 兩組比較

**前提假設檢驗（必做）：**
```
Step 1｜常態性檢定
  → Shapiro-Wilk（n < 50，推薦）或 Kolmogorov-Smirnov（n ≥ 50）
  → p > .05 → 不拒絕常態假設 → 可用參數統計

Step 2｜變異數同質性（Independent t-test 才需要）
  → Levene's Test
  → p > .05 → 變異數同質 → 用 equal variance t-test
  → p < .05 → 變異數不同質 → 用 Welch's t-test（SPSS 自動輸出）
```

| 情況 | 統計方法 | 效應量 |
|-----|---------|-------|
| 常態 + 獨立樣本 | Independent t-test | Cohen's d |
| 常態 + 配對樣本 | Paired t-test | Cohen's d |
| 非常態 + 獨立樣本 | Mann-Whitney U | r = Z/√N |
| 非常態 + 配對樣本 | Wilcoxon Signed-Rank | r = Z/√N |

**Cohen's d 解讀：**
- d = 0.20：小效應（small）
- d = 0.50：中效應（medium）
- d = 0.80：大效應（large）

**APA 寫法：**
```
t(df) = x.xx, p = .xxx, 95% CI [x.xx, x.xx], d = x.xx
```

---

### 2.2 三組以上比較（ANOVA）

**前提假設：**
- 各組資料常態分配
- 變異數同質性（Levene's test p > .05）
- 觀察值獨立

```
One-way ANOVA 流程：

Step 1｜整體 F 檢定
  → F(df_between, df_within) = x.xx, p = .xxx, η² = .xx

Step 2｜若整體顯著（p < .05）→ 事後比較（Post-hoc）
  → Tukey HSD：各組樣本數相等時（推薦）
  → Games-Howell：變異數不同質時
  → Bonferroni：控制型一錯誤，較保守

Step 3｜計算效應量 η²（Eta-squared）
  → η² = SS_between / SS_total
  → η² = .01：小；.06：中；.14：大
```

**非常態替代方案：** Kruskal-Wallis H test（事後比較用 Dunn's test）

**重複測量（Repeated Measures ANOVA）：**
- 額外假設：球形性（Sphericity）→ Mauchly's test
- 若違反：使用 Greenhouse-Geisser 校正

---

## 三、相關分析（Correlation）

| 資料類型 | 統計方法 | 係數符號 |
|---------|---------|---------|
| 兩個連續型 + 常態 | Pearson's r | r |
| 兩個連續型 + 非常態 | Spearman's ρ（rho） | ρ |
| 兩個二元類別 | Phi coefficient（φ） | φ |
| 一連續 + 一類別（二元） | Point-biserial | r_pb |

**相關強度解讀（Cohen, 1988）：**
- |r| = .10：弱（weak）
- |r| = .30：中（moderate）
- |r| = .50：強（strong）

**APA 寫法：**
```
r(df) = .xx, p = .xxx
ρ(df) = .xx, p = .xxx
```

⚠️ **注意**：相關≠因果。需避免「A 影響 B」的語言，改用「A 與 B 顯著相關（r = .xx）」。

---

## 四、迴歸分析（Regression）

### 4.1 簡單線性迴歸（Simple Linear Regression）

**假設前提：**
```
□ 線性關係（Scatter plot 確認）
□ 殘差常態性（Residual plot）
□ 變異數同質性（Homoscedasticity）
□ 觀察值獨立性
□ 無極端值（Cook's Distance < 1）
```

**APA 寫法：**
```
B = x.xx, SE = x.xx, β = .xx, t(df) = x.xx, p = .xxx
整體模型：F(df1, df2) = x.xx, p = .xxx, R² = .xx
```

### 4.2 多元迴歸（Multiple Regression）

**額外假設：**
- 多元共線性（Multicollinearity）：VIF < 10（嚴格 < 5）
- 若 VIF 過高：刪除相關變項或使用 Ridge Regression

**進入法策略選擇：**
| 方法 | 使用時機 |
|-----|---------|
| Enter（同時進入） | 有明確理論依據，所有 IV 同等重要 |
| Hierarchical（階層） | 控制干擾變項後，測試新增 IV 的貢獻（ΔR²） |
| Stepwise | 探索性研究（需謹慎，易 overfitting） |

### 4.3 邏輯迴歸（Logistic Regression）

適用：DV 為二元類別（0/1）

**關鍵輸出：**
- Odds Ratio（OR）與 95% CI
- Nagelkerke R²（偽 R²）
- Hosmer-Lemeshow goodness of fit

---

## 五、信效度分析

### 5.1 Cronbach's α 解讀

| α 值 | 解讀 |
|-----|------|
| ≥ .90 | 優秀（excellent）|
| .80–.89 | 良好（good）|
| .70–.79 | 可接受（acceptable）|
| .60–.69 | 存疑（questionable）|
| < .60 | 不可接受（unacceptable）|

**若 α < .70 的處理：**
1. 查看「Item-Total Correlation」，刪除 < .30 的題目
2. 查看「α if item deleted」，刪除刪去後 α 顯著提升的題目
3. 重新審視題目語意是否符合構念

### 5.2 因素分析（Factor Analysis）

**EFA（探索性）vs CFA（驗證性）：**
| | EFA | CFA |
|-|-----|-----|
| 目的 | 探索潛在因素結構 | 驗證理論假設的因素結構 |
| 使用時機 | 量表初步發展 | 量表修訂或跨文化驗證 |
| 樣本數 | n > 200 或 n:item ≥ 5:1 | n > 200（推薦 ≥ 300） |

**EFA 前提檢驗：**
- KMO > .60（建議 > .80）
- Bartlett's test of sphericity：p < .05

**CFA 適配指標：**
| 指標 | 好的標準 |
|-----|---------|
| χ²/df | < 3（或 < 5） |
| CFI | ≥ .90（理想 ≥ .95） |
| RMSEA | < .08（理想 < .06） |
| SRMR | < .08 |

---

## 六、樣本數計算指引

使用 **G*Power 3.1** 計算，需設定：
- 統計考驗力（Power）：1 - β = .80（最低）
- 型一錯誤率（α）：= .05（雙尾）
- 效應量（Effect Size）：依理論或先導研究設定

**常用效應量預設值（若無先前研究）：**
| 方法 | 小效應 | 中效應 | 大效應 |
|-----|-------|-------|-------|
| t-test | d = .20 | d = .50 | d = .80 |
| ANOVA | f = .10 | f = .25 | f = .40 |
| Correlation | r = .10 | r = .30 | r = .50 |
| Regression | f² = .02 | f² = .15 | f² = .35 |

---

## 七、常見統計錯誤警示

| 錯誤 | 正確做法 |
|-----|---------|
| p < .05 就說「有因果關係」 | 只能說「統計上顯著相關/差異」 |
| 忽略效應量，只報告 p 值 | 必須同時報告 effect size 與 CI |
| 多重比較不校正 | 使用 Bonferroni 或 FDR 校正 |
| 小樣本用參數統計 | n < 30 應考慮非參數統計 |
| 將 Likert 資料直接做 Pearson | 考慮 Spearman 或 Polychoric correlation |
| 過度詮釋統計顯著性 | 區分統計顯著性與臨床/實務顯著性 |
