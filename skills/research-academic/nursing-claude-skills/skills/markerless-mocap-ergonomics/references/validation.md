# 效度驗證與負荷指數建構

---

## 免標記系統效度的既有證據

理解這些數字很重要——它們界定了合理的預期，也說明為何不能外推。

| 研究 | 系統 | 結果 |
|---|---|---|
| Turner et al. (2024) | OpenCap（兩支 iPhone） | 矢狀面髖膝 CMC > 0.94；額狀面 0.47–0.78；橫斷面 0.51–0.60；整體 MAE 3.85° |
| Horsak et al. (2023) | OpenCap | 整體 RMSE 5.8°、峰值誤差 11.3°；病理性步態誤差顯著高於生理性 |
| Song et al. (2023) | 標記式對照，8 種動作 | 踝膝角度 R ≥ 0.877、RMSE ≤ 5.9°；髖關節 RMSE 6.7–15.9°，跑步等快速動作最差 |
| Scataglini et al. (2024) | 系統性回顧＋統合分析（22 篇） | 時空參數 ICC 0.81–0.98；髖膝矢狀面中至優；踝與非矢狀面偏低 |

### 兩個一致的結構性發現

1. **平面依賴性：** 矢狀面準確度明顯優於額狀面與橫斷面。
2. **動作依賴性：** 快速、遮蔽、非典型動作的誤差顯著較高。

### 為何不能外推到職業作業

上述驗證幾乎都在**單人、無遮蔽、矢狀面為主**的步態或運動任務。
職業作業（搬運、翻身、組裝）通常同時具備：

- 軀幹**扭轉**（非矢狀面——文獻中效度最差的平面）
- 人員**近距離互動**（高遮蔽）
- **快速施力**（誤差最大的速度區間）

三項挑戰疊加，效度必須**獨立驗證**，不可引用步態文獻的數字宣稱可用。
這正是這類研究的核心科學貢獻所在。

---

## 驗證設計

### 參照系統

| 選項 | 優點 | 限制 |
|---|---|---|
| 實驗室光學（Vicon 等） | 黃金標準 | 需貼標記；標記可能被遮擋或影響動作；僅限實驗室 |
| 慣性 IMU（Xsens 等） | 可攜、現場可用 | 軟組織假影；磁干擾；需自身校正 |

建議以 IMU 為主要參照（現場可行），若機構有光學系統則作次級對照。

**時間對齊：** IMU 與相機需對齊到共同時間軸。可用同一個 LED 閃光
（若 IMU 系統有事件標記功能），或請受試者做一個明顯的同步動作（如快速拍手）。

### 分層分析（關鍵）

**不要只報告單一總體 ICC。** 應至少依下列維度分層：

| 分層維度 | 為什麼 |
|---|---|
| **運動平面** | 矢狀 / 額狀 / 橫斷面的效度結構性不同 |
| **角速度區間** | 捲簾快門誤差與速度成正比；快速段是最弱環節 |
| **遮蔽程度** | 以「該幀該關節的有效相機數」量化，分層報告 |
| **關節** | 軀幹、髖、膝、肩的效度差異大 |

分層報告不是為了「找出好看的數字」，而是為了讓讀者判斷結果
在其應用情境下是否可信。籠統的單一數字會掩蓋真正重要的結構。

### 統計方法

**ICC（組內相關係數）**
- 必須註明**模型、型式與定義**（如 ICC(2,1)、two-way random, absolute agreement）。
  不同選擇得到不同數值，未註明則無法解讀。
- 報告 **95% 信賴區間**，並以區間下界判讀（Koo & Li, 2016 的建議）。
- 判讀分級（Koo & Li, 2016）：< 0.5 差、0.5–0.75 中等、0.75–0.9 良好、> 0.9 優異。

**RMSE 與 MAE**
- 以度為單位，直接對應臨床可解釋性。
- 文獻常引用的臨床理想閾值為 2–5°；多數免標記系統目前落在 4–6°。

**Bland-Altman 分析**（Bland & Altman, 1986）
- 揭露**系統性偏誤**（bias）與一致性界限（limits of agreement）。
- 這對捲簾快門的評估特別重要——ICC 可能很高但存在固定偏誤，
  只有 Bland-Altman 能看出來。
- 檢查偏誤是否隨數值大小變化（比例偏誤）。

### Go/No-Go 門檻的設定與誠實處理

建議門檻：主要關節角度 ICC ≥ 0.75。

**若未達標，正確做法是：**
- 分平面、分速度區間誠實報告，明確界定「在什麼條件下可用、什麼條件下不可用」。
- 縮小宣稱範圍，而非調整統計方法直到數字好看。

一個界定清楚的有限結論，學術價值高於一個含糊的全面宣稱。
審查者能看出後者。

---

## 複合式工作負荷指數（CWI）

### 動機

單一運動學指標（如軀幹角度）無法完整代表工作負荷。
主觀量表反映感知負荷，生理訊號反映生理成本，運動學反映機械負荷——
三者不完全重疊，融合後才能構成完整圖像。

### 建構流程

1. **標準化：** 各指標轉為可比較的尺度（z 分數或依理論上限正規化）。
2. **維度縮減：** 以因素分析或 PCA 檢視指標間的結構。
   若各維度高度相關，代表資訊冗餘，可精簡。
3. **權重設定：** 可用因素負荷量、專家共識、或迴歸至外部效標。
   **權重必須記錄且可重現**——這是後續能否被他人複製的關鍵。
4. **收斂效度檢驗：** CWI 與 NASA-TLX、Borg CR-10、HRV 指標的相關。
5. **區辨效度檢驗：** CWI 是否能區辨已知負荷不同的情境
   （如有無輔具、單人 vs 雙人）。

### 常用的多模態指標

| 模態 | 指標 | 注意事項 |
|---|---|---|
| 運動學 | 軀幹角度暴露時間、REBA、L5/S1 力矩積分 | 需定義「暴露」的閾值與累積方式 |
| 生理 | HRV（SDNN、RMSSD、LF/HF） | 感測器須能輸出 **R-R 間期原始值**；僅輸出平均心率者無法計算 |
| 生理 | 表面肌電 RMS（豎脊肌） | 需 MVC 正規化才能跨個體比較 |
| 主觀 | NASA-TLX、Borg CR-10 | NASA-TLX 有加權與未加權（raw）兩版，須說明採用何者 |

### 統計分析

多因子受試者內設計應以**線性混合模型**（linear mixed model）分析，
以受試者為隨機效果。報告主效果、交互作用與**效果量**（不只 p 值）。

量化介入效果時，報告百分比降幅與 95% 信賴區間，例如：
「床高最適化使軀幹力矩峰值降低 18.3%（95% CI [12.1, 24.5]）」。
這種表述方式對實務決策者有意義，單純的 p < .05 沒有。

---

## 主要參考文獻

- Bland, J. M., & Altman, D. G. (1986). Statistical methods for assessing agreement between two methods of clinical measurement. *The Lancet, 327*(8476), 307–310. https://doi.org/10.1016/S0140-6736(86)90837-8
- Horsak, B., et al. (2023). Concurrent validity of smartphone-based markerless motion capturing to quantify lower-limb joint kinematics in healthy and pathological gait. *Journal of Biomechanics, 159*, Article 111801. https://doi.org/10.1016/j.jbiomech.2023.111801
- Koo, T. K., & Li, M. Y. (2016). A guideline of selecting and reporting intraclass correlation coefficients for reliability research. *Journal of Chiropractic Medicine, 15*(2), 155–163. https://doi.org/10.1016/j.jcm.2016.02.012
- Scataglini, S., et al. (2024). Accuracy, validity, and reliability of markerless camera-based 3D motion capture systems versus marker-based systems in gait analysis: A systematic review and meta-analysis. *Sensors, 24*(11), Article 3686. https://doi.org/10.3390/s24113686
- Song, K., et al. (2023). Markerless motion capture estimates of lower extremity kinematics and kinetics are comparable to marker-based across 8 movements. *Journal of Biomechanics, 157*, Article 111751. https://doi.org/10.1016/j.jbiomech.2023.111751
- Turner, J. A., Chaaban, C. R., & Padua, D. A. (2024). Validation of OpenCap: A low-cost markerless motion capture system for lower-extremity kinematics during return-to-sport tasks. *Journal of Biomechanics, 171*, Article 112200. https://doi.org/10.1016/j.jbiomech.2024.112200
