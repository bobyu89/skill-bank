# SEM 結構方程模式與路徑分析完整指引

> 適用於 TAM、UTAUT、TPB 等理論模型驗證

---

## 一、何時使用 SEM？

```
使用 SEM 的判斷邏輯：
├─ 有潛在變項（Latent Variable）需測量？
│     ├─ 是 → SEM（Full SEM with measurement model）
│     └─ 否 → Path Analysis（觀察變項路徑分析）
│
├─ 有中介效果（Mediation）需驗證？
│     └─ SEM 或 Process Macro（Hayes, 2018）
│
├─ 有調節效果（Moderation）需驗證？
│     └─ SEM 多群組分析 或 交互作用項
│
└─ 只需確認變項間關聯？
      └─ 迴歸分析即可，不需 SEM
```

⚠️ **SEM 最低樣本數建議**：
- 經驗法則：每個估計參數需 10-20 個觀察值
- 絕對最低：n ≥ 200（Kline, 2016 建議）
- 理想：n ≥ 300
- 使用 G*Power 或 Monte Carlo 模擬確認

---

## 二、SEM 兩階段分析流程

### Stage 1：測量模型（Measurement Model / CFA）

先確認量表的因素結構正確，再進行路徑分析。

```
CFA 檢驗清單：
□ 因素負荷量（Factor Loading）≥ 0.50（理想 ≥ 0.70）
□ 組合信度（CR, Composite Reliability）≥ 0.70
□ 平均變異萃取量（AVE, Average Variance Extracted）≥ 0.50
□ 區辨效度（Discriminant Validity）：
    → Fornell-Larcker 準則：各構念 √AVE > 構念間相關
    → HTMT（Heterotrait-Monotrait）< 0.85（嚴格 < 0.90）
```

**CFA 適配指標（Model Fit）：**

| 指標 | 可接受標準 | 良好標準 | 說明 |
|-----|---------|---------|------|
| χ²/df | < 5 | < 3 | 卡方與自由度比（大樣本易顯著，參考即可） |
| CFI | ≥ .90 | ≥ .95 | 比較適配指標 |
| TLI | ≥ .90 | ≥ .95 | Tucker-Lewis 指標 |
| RMSEA | < .08 | < .06 | 近似誤差均方根（附 90% CI） |
| SRMR | < .08 | < .05 | 標準化殘差均方根 |

⚠️ **不要只報告 χ² p-value**：大樣本幾乎必顯著，需搭配其他指標。

### Stage 2：結構模型（Structural Model / Path Analysis）

確認測量模型適配後，加入路徑關係：

```
結構模型報告要素：
□ 路徑係數（Standardized β）
□ 顯著性（p-value 或 95% CI）
□ R²（各內生變項的解釋變異量）
□ 直接效果（Direct Effect）
□ 間接效果（Indirect Effect）→ Bootstrap 法（n=5000）
□ 總效果（Total Effect）= 直接 + 間接
□ 整體模型適配指標（同 CFA）
```

---

## 三、CB-SEM vs. PLS-SEM 選擇

| 比較項目 | CB-SEM（AMOS/Mplus/lavaan） | PLS-SEM（SmartPLS） |
|---------|--------------------------|-------------------|
| 目的 | 理論驗證（Theory testing） | 預測導向（Prediction） |
| 樣本需求 | n ≥ 200（嚴格） | n ≥ 100 或 10×最大路徑數 |
| 資料分配假設 | 需多變量常態性 | 無分配假設 |
| 適用情境 | TAM、TPB 等成熟理論驗證 | 探索性模型、小樣本 |
| 適配指標 | χ², CFI, RMSEA, SRMR | SRMR, f², Q²（預測相關性） |
| 形成性指標 | 不易處理 | 原生支持 |

**建議**：你的 TAM 論文屬理論驗證，優先用 CB-SEM（AMOS 或 lavaan）。若樣本 < 150，可考慮 PLS-SEM。

---

## 四、中介效果與調節效果

### 4.1 中介效果（Mediation）

```
經典中介模型（Baron & Kenny, 1986 → 已被取代）：
現代作法：直接用 Bootstrap 間接效果檢定

判斷邏輯：
IV → Mediator → DV

Bootstrap 間接效果 95% CI：
  → 不包含 0 → 間接效果顯著
  → 包含 0 → 間接效果不顯著

效果分類：
  → 直接效果顯著 + 間接效果顯著 → 部分中介（Partial Mediation）
  → 直接效果不顯著 + 間接效果顯著 → 完全中介（Full Mediation）
```

### 4.2 調節效果（Moderation）

```
調節模型：IV × Moderator → DV

SEM 中的操作方式：
  → 連續型調節變項：建立交互作用項（IV × Mod）
  → 類別型調節變項：多群組分析（Multi-group SEM）

報告格式：
  → 交互項顯著：β_interaction = .xx, p = .xxx
  → 多群組：Δχ² 或 參數差異檢定
```

---

## 五、TAM 模型專用分析模板

```
TAM（Technology Acceptance Model）路徑假設：

H1: 感知易用性（PEOU）→ 感知有用性（PU）    β = ?
H2: 感知易用性（PEOU）→ 使用意圖（BI）       β = ?
H3: 感知有用性（PU）→ 使用意圖（BI）          β = ?
H4: 使用意圖（BI）→ 實際使用（AU）            β = ?

外部變項（可擴充）：
  → 系統品質（System Quality）→ PEOU, PU
  → 自我效能（Self-efficacy）→ PEOU
  → 護理年資 → 調節 PEOU → BI

報告範例（APA）：
「結構模型顯示感知有用性正向且顯著預測使用意圖
（β = .42, p < .001, 95% CI [.31, .53]），
感知易用性對使用意圖的直接效果不顯著（β = .08, p = .312），
但透過感知有用性的間接效果顯著
（indirect effect = .18, 95% Bootstrap CI [.11, .27]），
支持完全中介假設。整體模型解釋使用意圖 52% 的變異量（R² = .52）。」
```

---

## 六、常見 SEM 錯誤與修正

| 錯誤 | 修正建議 |
|-----|---------|
| Heywood case（負的誤差變異） | 檢查樣本數、模型設定、共線性 |
| 模型不適配但硬報告 | 考慮修正指標（MI）但需理論支持 |
| 刪題只看 MI 不看理論 | 每次刪題都需有理論依據 |
| 忽略 common method bias | Harman 單因素檢定 或 CMV marker 變項 |
| Bootstrap 次數不足 | 建議 n = 5000（至少 2000） |
| 過度修飾模型（overfitting） | 交叉驗證或 split-sample |

---

## 七、奠基文獻

- Hair, J. F., Black, W. C., Babin, B. J., & Anderson, R. E. (2019). *Multivariate data analysis* (8th ed.). Cengage.
- Kline, R. B. (2016). *Principles and practices of structural equation modeling* (4th ed.). Guilford.
- Hair, J. F., Hult, G. T. M., Ringle, C. M., & Sarstedt, M. (2022). *A primer on partial least squares structural equation modeling (PLS-SEM)* (3rd ed.). Sage.
- Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly, 13*(3), 319–340.
- Hayes, A. F. (2018). *Introduction to mediation, moderation, and conditional process analysis* (2nd ed.). Guilford.
