# 生物力學計算：關節角度、REBA/RULA、腰椎負荷

---

## 先固定定義，再寫程式

關節角度的數值**完全取決於定義方式**：參考座標系、旋轉順序（Euler sequence）、
中立位定義。不同定義得到不同數值，且都「看起來合理」。

**因此：在寫第一行計算程式碼之前，先把定義寫成文件並固定下來。**
中途更改會使先前蒐集的資料無法與後續比較——這在多年期研究中是災難。

建議採用 ISB（International Society of Biomechanics）建議的座標系定義，
理由是可與國際文獻比較。若因骨架模型限制而偏離，必須明確記載偏離之處。

### 軀幹角度的實務定義

以骨盆座標系為參考，軀幹向量取自骨盆中心指向肩中心：

```python
def trunk_angles(pelvis_l, pelvis_r, shoulder_l, shoulder_r):
    """回傳軀幹屈曲、側彎、旋轉角度（度）。

    骨盆座標系：
      x 軸（前）= 骨盆法線方向
      y 軸（左）= 左髖 - 右髖
      z 軸（上）= x × y
    軀幹向量 = 肩中心 - 骨盆中心
    """
```

**注意兩件事：**
- 屈曲角度應以**重力方向**或**骨盆座標系**為參考？前者反映絕對姿勢（與 REBA 一致），
  後者反映脊椎相對彎曲。兩者在人彎腰同時骨盆前傾時差異很大。REBA 用的是前者。
- 旋轉角度在軀幹接近直立時數值不穩定（萬向鎖）。需檢查並標記此情形。

---

## REBA 自動評分

REBA（Rapid Entire Body Assessment；Hignett & McAtamney, 2000）
專為醫療照護等產業的**不可預期工作姿勢**設計，比 RULA 更適合搬運類作業。

### 計分結構

```
Group A（軀幹、頸、腿）→ Table A → +力量/負重分數 → Score A
Group B（上臂、前臂、腕）→ Table B → +握持分數 → Score B
Score A + Score B → Table C → +活動分數 → REBA 總分
```

### 自動化的注意事項

**可由骨架直接算出的：** 軀幹／頸／腿／上臂／前臂／腕的角度分段。

**無法由骨架算出、必須另外提供的：**
- **負重／施力分數**（< 5 kg / 5–10 kg / > 10 kg，加上突發施力）
  → 需由實驗設計的情境變項提供（如模擬病人體重）
- **握持品質**（good / fair / poor / unacceptable）
  → 需由作業類型或人工標註提供
- **活動分數**（靜態姿勢 > 1 分鐘、小幅重複 > 4 次/分、大幅快速變化）
  → 可由時序資料自動推算，但需明定判定規則

**常見錯誤：** 只算姿勢分數就宣稱是 REBA 分數。缺少負重與握持分數的
「REBA」與真正的 REBA 不可比較，論文中必須說明計分範圍。

### 驗證方式

與人工評分者比對至少 20 個姿勢，計算 ICC。目標 ≥ 0.75。
選取的姿勢應涵蓋分數全距，不要全是中等風險姿勢——
否則 ICC 會因變異範圍過窄而虛低（或因巧合而虛高）。

---

## RULA

RULA（McAtamney & Corlett, 1993）偏重上肢與靜態姿勢，
適用於精細作業、電腦工作。搬運類作業以 REBA 為主，RULA 可作為輔助指標。

實作結構與 REBA 類似（Group A/B → Table C），差異在分段閾值與加分規則。

---

## 腰椎 L5/S1 負荷估算

### 快速連桿模型（適合即時管線）

自上而下逐段計算的靜力學／準靜態逆動力學：

1. 由身高體重與 de Leva（1996）的人體肢段參數表，取得各肢段質量、
   質心位置與轉動慣量。
2. 由三維骨架取得各肢段位置與（差分得到的）加速度。
3. 自遠端（手）向近端（軀幹）逐段套用牛頓－歐拉方程，
   累積至 L5/S1 得到淨力矩。
4. 若有外部負荷（搬運物重量），加入為手部的外力。

```python
# 概念示意
def l5s1_moment(segments, external_load_n, gravity=9.81):
    """回傳 L5/S1 淨力矩（N·m）。

    準靜態近似：忽略肢段角加速度的貢獻。
    在慢速動作誤差小，快速動作會低估——需在報告中說明。
    """
```

**準靜態近似的適用界線：** 動作愈快，忽略慣性項的誤差愈大。
應以完整逆動力學（OpenSim）在若干代表性試作上比對，量化此近似的誤差
（目標相對誤差 < 15%），並在論文中報告。

### 高保真逆動力學（離線管線）

OpenSim（Delp et al., 2007; Seth et al., 2018）提供完整的肌肉骨骼模擬。
流程：骨架座標 → 標記或 IK → Inverse Dynamics → 關節力矩。

OpenSim 整合複雜度高，建議：**以連桿模型為主要路徑，OpenSim 作為驗證用**，
不要放在關鍵路徑上。若 OpenSim 整合受阻，專案不應因此停擺。

### NIOSH 抬舉指數

修訂版 NIOSH 方程式（Waters et al., 1993）提供搬運作業的風險判準，
整合生物力學、生理與心理物理三重準則。可作為 L5/S1 力矩之外的補充指標，
且其抬舉指數（LI）有明確的風險分級解釋，便於向非專業人員溝通。

注意其適用前提（雙手對稱抬舉、穩定站姿等），翻身等非標準動作
套用時需說明偏離之處。

---

## 資料結構建議

生物力學指標的資料表應包含：

```
BiomechMetric
├─ trial_id, t
├─ trunk_flexion_deg, trunk_lateral_deg, trunk_rotation_deg
├─ reba_score, reba_score_components (JSONB)   # 保留分項，便於除錯
├─ rula_score
├─ l5s1_moment_nm
├─ computed_by       # fast_linkage / opensim — 避免兩管線結果混淆
└─ definition_version # 角度定義的版本；定義變更時遞增
```

`definition_version` 是實務上的救命設計：當你不得不修改角度定義時，
能明確區分新舊資料，而非讓它們靜默混在一起。

---

## 參考文獻

- de Leva, P. (1996). Adjustments to Zatsiorsky-Seluyanov's segment inertia parameters. *Journal of Biomechanics, 29*(9), 1223–1230.
- Delp, S. L., et al. (2007). OpenSim: Open-source software to create and analyze dynamic simulations of movement. *IEEE Transactions on Biomedical Engineering, 54*(11), 1940–1950. https://doi.org/10.1109/TBME.2007.901024
- Hignett, S., & McAtamney, L. (2000). Rapid Entire Body Assessment (REBA). *Applied Ergonomics, 31*(2), 201–205. https://doi.org/10.1016/S0003-6870(99)00039-3
- McAtamney, L., & Corlett, E. N. (1993). RULA: A survey method for the investigation of work-related upper limb disorders. *Applied Ergonomics, 24*(2), 91–99. https://doi.org/10.1016/0003-6870(93)90080-S
- Seth, A., et al. (2018). OpenSim: Simulating musculoskeletal dynamics and neuromuscular control. *PLOS Computational Biology, 14*(7), e1006223. https://doi.org/10.1371/journal.pcbi.1006223
- Waters, T. R., et al. (1993). Revised NIOSH equation for the design and evaluation of manual lifting tasks. *Ergonomics, 36*(7), 749–776. https://doi.org/10.1080/00140139308967940
