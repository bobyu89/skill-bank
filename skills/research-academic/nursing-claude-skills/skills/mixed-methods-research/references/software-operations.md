# 統計與質性分析軟體操作對照指引

> 涵蓋 SPSS、R/lavaan、Python、NVivo、ATLAS.ti 及 AI 輔助編碼

---

## 一、量性分析：SPSS 操作對照

### 1.1 描述統計

```
SPSS 路徑：Analyze → Descriptive Statistics → Descriptives / Frequencies
對應指令：
  DESCRIPTIVES VARIABLES=age score /STATISTICS=MEAN STDDEV MIN MAX.
  FREQUENCIES VARIABLES=gender education /ORDER=ANALYSIS.
```

### 1.2 獨立樣本 t-test

```
SPSS 路徑：Analyze → Compare Means → Independent-Samples T Test
操作步驟：
  1. Test Variable(s)：放入連續型 DV
  2. Grouping Variable：放入分組變項 → Define Groups（1, 2）
  3. 輸出判讀：先看 Levene's Test
     → p > .05 → 看 Equal variances assumed 那行
     → p < .05 → 看 Equal variances not assumed（Welch's t）
```

### 1.3 ANOVA

```
SPSS 路徑：Analyze → Compare Means → One-Way ANOVA
操作步驟：
  1. Dependent List：DV
  2. Factor：分組 IV
  3. Post Hoc：勾選 Tukey（等變異）或 Games-Howell（不等變異）
  4. Options：勾選 Descriptive, Homogeneity of variance test
```

### 1.4 迴歸分析

```
SPSS 路徑：Analyze → Regression → Linear
操作步驟：
  1. Dependent：DV
  2. Independent(s)：IV（可選 Enter / Stepwise / Hierarchical）
  3. Statistics：勾選 Estimates, Model fit, Collinearity diagnostics
  4. 判讀：VIF < 5, Durbin-Watson 1.5-2.5
```

### 1.5 信度分析

```
SPSS 路徑：Analyze → Scale → Reliability Analysis
操作步驟：
  1. Items：放入量表所有題目
  2. Model：Alpha
  3. Statistics：勾選 Item, Scale, Scale if item deleted
  4. 判讀：Cronbach's α ≥ .70, item-total correlation > .30
```

### 1.6 CFA（需 AMOS 插件）

```
AMOS 操作步驟：
  1. 繪製測量模型圖（橢圓=潛在變項, 矩形=觀察指標）
  2. 連結觀察指標至潛在變項
  3. 為每個觀察指標加上誤差項（e1, e2...）
  4. 設定一個負荷量 = 1（識別條件）
  5. Analyze → Calculate Estimates
  6. 查看 Output：
     → Model Fit：CMIN/DF, CFI, TLI, RMSEA, SRMR
     → Standardized Regression Weights（因素負荷量）
     → Squared Multiple Correlations（R²）
```

---

## 二、量性分析：R / lavaan 操作對照

### 2.1 CFA

```r
library(lavaan)

# 定義測量模型
model_cfa <- '
  PEOU =~ peou1 + peou2 + peou3 + peou4
  PU   =~ pu1 + pu2 + pu3 + pu4
  BI   =~ bi1 + bi2 + bi3
'

# 執行 CFA
fit_cfa <- cfa(model_cfa, data = mydata, estimator = "MLR")

# 輸出結果
summary(fit_cfa, fit.measures = TRUE, standardized = TRUE)

# 信效度指標
library(semTools)
reliability(fit_cfa)        # CR, AVE
htmt(model_cfa, mydata)     # HTMT 區辨效度
```

### 2.2 SEM（結構模型）

```r
model_sem <- '
  # 測量模型
  PEOU =~ peou1 + peou2 + peou3 + peou4
  PU   =~ pu1 + pu2 + pu3 + pu4
  BI   =~ bi1 + bi2 + bi3

  # 結構模型（路徑）
  PU ~ PEOU
  BI ~ PU + PEOU

  # 間接效果定義
  indirect := a * b
'

fit_sem <- sem(model_sem, data = mydata, se = "bootstrap", bootstrap = 5000)
summary(fit_sem, fit.measures = TRUE, standardized = TRUE, ci = TRUE)

# 路徑圖
library(semPlot)
semPaths(fit_sem, what = "std", layout = "tree2",
         edge.label.cex = 1.2, sizeMan = 8, sizeLat = 10)
```

### 2.3 中介效果 Bootstrap

```r
# 使用 lavaan 內建 bootstrap
parameterEstimates(fit_sem, boot.ci.type = "perc", level = 0.95,
                   ci = TRUE, standardized = TRUE)

# 或使用 mediation 套件
library(mediation)
med_model <- lm(mediator ~ IV, data = mydata)
out_model <- lm(DV ~ IV + mediator, data = mydata)
med_result <- mediate(med_model, out_model,
                      treat = "IV", mediator = "mediator",
                      boot = TRUE, sims = 5000)
summary(med_result)
```

---

## 三、量性分析：Python 操作對照

### 3.1 基本統計

```python
import pandas as pd
from scipy import stats

# 描述統計
df.describe()

# 獨立樣本 t-test
t_stat, p_val = stats.ttest_ind(group1, group2)

# ANOVA
f_stat, p_val = stats.f_oneway(g1, g2, g3)

# Pearson 相關
r, p = stats.pearsonr(x, y)
```

### 3.2 SEM（使用 semopy）

```python
import semopy

model_desc = """
PEOU =~ peou1 + peou2 + peou3 + peou4
PU   =~ pu1 + pu2 + pu3 + pu4
BI   =~ bi1 + bi2 + bi3
PU ~ PEOU
BI ~ PU + PEOU
"""

model = semopy.Model(model_desc)
model.fit(df)
print(model.inspect())
stats_result = semopy.calc_stats(model)
print(stats_result.T)
```

### 3.3 信度（使用 pingouin）

```python
import pingouin as pg

# Cronbach's alpha
alpha = pg.cronbach_alpha(data=df[['item1','item2','item3','item4']])
print(f"Cronbach's α = {alpha[0]:.3f}")
```

---

## 四、質性分析軟體操作

### 4.1 NVivo 操作指引

```
NVivo 工作流程：
Step 1｜匯入資料
  → Import → Files → 選擇逐字稿（.docx / .txt）
  → 建立 Case Node 對應每位受訪者

Step 2｜建立編碼架構
  → 右鍵 → New Code → 依主題建立層級式編碼
  → 建議結構：
      主題 1
        ├─ 子主題 1a
        └─ 子主題 1b
      主題 2
        └─ 子主題 2a

Step 3｜編碼操作
  → 選取文字段落 → 拖曳至對應 Code
  → 或右鍵 → Code Selection → 選擇既有/新建 Code

Step 4｜查詢與分析
  → Explore → Matrix Coding Query（交叉比較主題 × 受訪者）
  → Explore → Word Frequency（詞頻分析輔助）
  → Explore → Coding Comparison Query（編碼者間一致性）

Step 5｜視覺化
  → Explore → Charts → Hierarchy Chart（主題階層）
  → Explore → Maps → Concept Map（概念關聯）
```

### 4.2 ATLAS.ti 操作指引

```
ATLAS.ti 工作流程：
Step 1｜建立專案 → New Project → 匯入逐字稿
Step 2｜Open Coding → 選取文字 → Apply Codes
Step 3｜Code Manager → 整理與歸類 codes
Step 4｜Network View → 建立 code 之間的關聯圖
Step 5｜Code Co-occurrence → 分析 code 共現頻率
Step 6｜Export → 匯出編碼報告（Excel / Word）
```

### 4.3 AI 輔助質性編碼流程

```
使用 Claude 輔助質性分析的最佳實踐：

⚠️ 重要原則：AI 是「協作編碼者」，不是「自動編碼器」

Step 1｜去識別化
  → 替換姓名、機構名、地名
  → 確認無可辨識個資

Step 2｜初始編碼（AI 協作）
  → 貼上去識別化的逐字稿片段
  → 請 Claude 建議 initial codes
  → 研究者審閱、修改、確認

Step 3｜主題建構（研究者主導）
  → 研究者整合 codes → 形成主題
  → Claude 可協助：
      - 檢查主題與 code 的邏輯一致性
      - 建議可能遺漏的 negative cases
      - 協助撰寫主題定義

Step 4｜信效度確保
  → 同儕詰辯：請另一位研究者獨立編碼 20% 逐字稿
  → 計算 Cohen's Kappa（κ ≥ .70）
  → 若使用 AI 輔助，需在方法章節揭露

揭露聲明範例：
「本研究初始編碼階段輔以 AI 工具（Claude, Anthropic）協助
  產生初始編碼建議，所有編碼由研究者逐一審閱、修改與確認，
  最終主題建構由研究者獨立完成。」
```

---

## 五、軟體選擇決策樹

```
你的分析需求是？
├─ 量性 + 基本統計（t-test, ANOVA, regression）
│     ├─ 有 SPSS 授權 → SPSS（最直覺）
│     ├─ 免費方案 → JASP（介面類似 SPSS）或 jamovi
│     └─ 程式碼偏好 → R + tidyverse / Python + scipy
│
├─ SEM / CFA / 路徑分析
│     ├─ 圖形化介面 → AMOS（需 SPSS 授權）或 SmartPLS
│     ├─ 程式碼 → R + lavaan（推薦，免費）
│     └─ Python → semopy（較新，社群較小）
│
├─ 質性編碼
│     ├─ 功能完整 + 學校授權 → NVivo
│     ├─ 免費替代 → ATLAS.ti Web（免費版有限制）
│     ├─ 輕量級 → Taguette（開源免費）
│     └─ AI 輔助 → Claude + 研究者審閱
│
└─ 混合方法
      → 質性用 NVivo/ATLAS.ti + 量性用 SPSS/R
      → 整合分析在論文中以 Joint Display 表格呈現
```

---

## 六、奠基文獻

- Field, A. (2024). *Discovering statistics using IBM SPSS statistics* (6th ed.). Sage.
- Rosseel, Y. (2012). lavaan: An R package for structural equation modeling. *Journal of Statistical Software, 48*(2), 1–36.
- Bazeley, P., & Jackson, K. (2013). *Qualitative data analysis with NVivo* (2nd ed.). Sage.
- Friese, S. (2019). *Qualitative data analysis with ATLAS.ti* (3rd ed.). Sage.
