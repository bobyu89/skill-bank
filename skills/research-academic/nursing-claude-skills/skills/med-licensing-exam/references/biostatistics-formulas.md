# 生物統計公式速查表

## 2×2 Table 基本架構

```
              Disease +    Disease -
Test +    |     TP      |     FP     |  → PPV = TP/(TP+FP)
Test -    |     FN      |     TN     |  → NPV = TN/(TN+FN)
              ↓               ↓
         Sensitivity    Specificity
       = TP/(TP+FN)   = TN/(TN+FP)
```

## 核心公式

| 指標 | 公式 | 記憶重點 |
|------|------|----------|
| Sensitivity (SN) | TP / (TP+FN) | 找出真正病人的能力，高 SN → 篩檢用 |
| Specificity (SP) | TN / (TN+FP) | 排除健康人的能力，高 SP → 確診用 |
| PPV | TP / (TP+FP) | 受**盛行率**影響 |
| NPV | TN / (TN+FN) | 受**盛行率**影響 |
| LR+ | SN / (1-SP) | >10 強力支持診斷 |
| LR- | (1-SN) / SP | <0.1 強力排除診斷 |
| Accuracy | (TP+TN) / Total | |

## 相對風險與勝算比

| 指標 | 公式 | 適用研究 |
|------|------|----------|
| RR (Relative Risk) | [a/(a+b)] / [c/(c+d)] | Cohort study |
| OR (Odds Ratio) | (a×d) / (b×c) | Case-control study |
| ARR (絕對風險降低) | Control rate - Treatment rate | RCT |
| NNT | 1 / ARR | 越小越好 |
| NNH | 1 / ARI | 越大越安全 |

## 混淆陷阱

- **Prevalence ↑ → PPV ↑, NPV ↓**（高盛行率族群中篩檢，陽性預測值更高）
- **SN 高的試驗**：陰性結果有意義（rule OUT，口訣：**SnNout**）
- **SP 高的試驗**：陽性結果有意義（rule IN，口訣：**SpPin**）

## 研究設計比較

| 設計 | 時序 | 適用 | 可算 |
|------|------|------|------|
| RCT | 前瞻 | 治療效果 | RR, ARR, NNT |
| Cohort | 前瞻 | 暴露→疾病 | RR, IR |
| Case-Control | 回溯 | 罕見疾病 | OR |
| Cross-sectional | 橫斷 | 盛行率 | Prevalence, OR |

## 常考計算範例

**NNT 計算**：
- 治療組事件率 = 10%，對照組 = 20%
- ARR = 20% - 10% = 10% = 0.1
- NNT = 1/0.1 = **10**（需治療 10 人，預防 1 個事件）
