---
name: markerless-mocap-ergonomics
description: Build multi-camera markerless motion capture systems for occupational ergonomics and biomechanical workload assessment using consumer webcams — covers camera capture and LED synchronization, ChArUco calibration, 2D pose to 3D triangulation, REBA/RULA scoring, L5/S1 spinal load estimation, multi-person association, IMU validation, and real-time risk warning. Use this skill whenever the user mentions FreeMoCap, OpenCap, markerless motion capture, 動作捕捉, 姿態估計, multi-camera 3D reconstruction, REBA, RULA, 人因工程, 工作負荷, ergonomic risk assessment, musculoskeletal load, nurse patient handling or 翻身 biomechanics, or wants to build/scaffold a webcam-based motion analysis or posture monitoring system — even if they only describe the goal (e.g. "I want to measure how much strain nurses are under when they turn patients") without naming any of these terms.
allowed-tools: Read Write Edit Bash Glob Grep
metadata:
    domain: biomechanics / occupational ergonomics / computer vision
---

# 無標記動作捕捉：職業人因負荷量測系統

以一般網路攝影機建構多視角三維動作捕捉，量化工作姿勢的生物力學負荷。
適用於護理搬運、產線作業、復健評估等需要在真實場域量測身體負荷的情境。

## 這個 skill 解決什麼問題

實驗室光學動作捕捉（Vicon 等）精度高但昂貴、需貼標記、無法佈署到工作現場。
本 skill 提供以消費級網路攝影機達成可發表精度的完整路徑——
文獻已證實這條路走得通（OpenCap 用兩支 iPhone 達成平均絕對誤差 3.85°），
但**成敗取決於幾個不明顯的技術細節**，踩到任何一個都會產出「看起來正常但實際上錯誤」的資料。

那些細節就是本 skill 的核心價值。

---

## 先讀這個：五個會毀掉資料的陷阱

這些不是效能優化建議，是**資料有效性的底線**。每一項都會產生看似正常、
實際錯誤的資料——這比直接報錯危險得多，因為錯誤可能到論文審查階段才被發現。

### 1. 自動對焦會讓校正失效，而且不會報錯

對焦改變即焦距改變，等同相機內參改變。錄製中途自動對焦跑掉，
先前的校正結果就全部失效，但影像看起來完全正常。

**做法：** 開啟相機後必須關閉自動對焦、自動曝光、自動白平衡，
且**回讀確認生效**——部分 UVC 驅動會靜默忽略設定請求，`cap.set()` 仍回傳 True。
若無法關閉自動對焦，應視為致命錯誤並中止錄製，而非警告後繼續。

同理，**絕對不可使用具 AI 自動追蹤／自動取景的機型**（如 OBSBOT Tiny 系列）——
相機會自行轉動或數位裁切，等同持續改變內外參。優先選固定對焦機型。

### 2. 捲簾快門造成系統性（非隨機）誤差

消費級相機逐行讀出影像，上下緣取樣時刻相差 8–15 ms。物體在讀出期間移動時
影像被剪切變形。以軀幹角速度 100–200°/s 估算，誤差約 0.5–1.5°。

關鍵在於：**這是系統性誤差，方向固定，不會隨樣本數增加而抵消。**
若作業動作方向一致（如翻身），會造成偏誤而非雜訊。

**做法：** 不要隱瞞，也不要因此放棄方案。分速度區間報告效度，
以參照系統量化這項誤差。加強照明可減少動態模糊（影響姿態估計信心），
但無法消除讀出造成的傾斜。

### 3. 場景通常不只一個人

職業場域幾乎都是多人互動（護理師與病人、作業員與同事）。
MediaPipe Pose 是**單人**偵測，直接套用會隨機跳換追蹤對象，產出完全無效的資料。

**做法：** 感知層必須是四段式——多人 2D 姿態估計 → 跨視角關聯 →
時序身分維持 → 角色判定。這通常是整個專案技術風險最高的部分，
應提早開發而非留到後期。詳見 `references/multi-person.md`。

### 4. 警示系統本身會製造工作負荷

若系統的目的是降低負荷，卻因誤報頻繁而造成警示疲勞（alarm fatigue），
就形成自我否定。既有文獻已證實警報負擔會顯著推升主觀工作負荷。

**做法：** 採「強度 × 持續時間」的劑量準則而非瞬時閾值；
**特異度優先於敏感度**；把誤報率上限（如每 8 小時班 ≤ 2 次）
當作驗收條件而非事後調參。被抑制的事件仍應完整記錄，供閾值調校分析。

### 5. 研究管線與即時管線需求本質不同

離線研究要最高精度、可跑數小時；即時預警要低延遲、可佈署。
強行以單一管線滿足兩者，結果是兩邊都不合格。

**做法：** 雙管線架構，共用資料模型與生物力學核心，但擷取與推論路徑分離。
即時管線的精度不自行宣稱，而是**以離線管線為內部黃金標準逐項量化**。

完整討論見 `references/critical-constraints.md`。

---

## 快速開始：建立專案骨架

```bash
python scripts/scaffold.py <目標目錄> --package <套件名> --project "<專案名稱>"
```

範例：

```bash
python scripts/scaffold.py ./myproject --package myload --project "產線作業負荷量測"
```

會產生完整的可執行專案，包含：

- **已測試的擷取層** — 相機探索、多執行緒錄製（自動功能回讀驗證）、LED 同步次幀內插
- **CLAUDE.md** — 開發鐵則，讓後續開發不會踩到上述陷阱
- **ROADMAP.md** — P0–P7 分階段，每階段有明確驗收準則
- **合成資料測試** — 不需相機即可執行，驗證核心運算邏輯

建立後立即執行 `pytest` 確認環境正常（應全數通過），再開始開發。

---

## 開發順序：先打通端到端，再擴充

最容易失敗的做法是分別開發擷取、校正、姿態、生物力學四個模組，最後才整合——
因為**同步與座標系的問題只在整合時暴露**，屆時各模組都已寫死假設。

正確做法：先用 **2 台相機 + 一個人做簡單彎腰**，把
「錄影 → 同步 → 校正 → 2D 姿態 → 3D 重建 → 算出一個關節角度」整條路走通。

| 階段 | 內容 | 驗收準則 | 參考 |
|---|---|---|---|
| P0 | 擷取與 LED 同步 | 同步誤差 < 10 ms；掉幀率 < 0.5% | scaffold 已含 |
| P1 | ChArUco 校正 | 重投影誤差 < 1 px **且**已知長度物件重建誤差 < 1% | `references/calibration.md` |
| P2 | 單人 3D 重建 | 合成資料往返測試通過；3D 回放動作合理 | `references/reconstruction.md` |
| P3 | 關節角度與 REBA | 靜態已知角度比對；REBA 與人工評分 ICC ≥ 0.75 | `references/biomechanics.md` |
| P4 | 多人關聯與角色判定 | 跨視角關聯 ≥ 95%；角色判定 ≥ 98% | `references/multi-person.md` |
| P5 | 參照系統效度驗證 | 主要關節角度 ICC ≥ 0.75 | `references/validation.md` |
| P6 | 多模態負荷指數 | 複合指數收斂效度達標 | `references/validation.md` |
| P7 | 即時預警與介面 | AUROC ≥ 0.85；誤報 ≤ 2 次/班 | `references/warning-system.md` |

每階段沒通過驗收就不要進下一階段。P1 的「已知長度物件」測試特別重要——
重投影誤差低但**尺度錯誤**的情況並不罕見，只看重投影誤差會漏掉。

---

## 驗證紀律：幾何運算一定要有合成資料測試

三維重建的錯誤（座標系定義錯、旋轉順序錯、外參張冠李戴）
靠肉眼看 3D 骨架回放**很難發現**——動作看起來會「大致合理」但數值是錯的。

因此每個幾何模組都必須有往返測試（round-trip test）：

```
已知 3D 點 → 用已知相機參數投影成 2D → 餵入你的重建演算法 → 驗證還原誤差在數值精度內
```

這類測試不需要相機、跑得快、且能立刻定位問題。scaffold 產生的專案已含
LED 同步偵測的合成測試作為範例，請比照辦理。

另一個原則：**硬體相關邏輯與純運算邏輯必須分離**，
使純運算部分能在未安裝 OpenCV 或無相機的環境測試。

---

## 硬體選型速查

詳見 `references/hardware.md`。要點：

- **相機數量比相機等級重要。** 網路攝影機便宜，應該多買。增加視角是對抗遮蔽最有效的手段，
  而職業作業的遮蔽問題遠比步態研究嚴重。建議直接配 6 台。
- **幀率優先於解析度。** 720p60 優於 1080p30——快速動作的角速度估計需要時間解析度。
- **必須 MJPEG。** 未設定 fourcc 時 OpenCV 常取得未壓縮格式，USB 頻寬會把幀率壓到個位數。
- **照明不能省。** 必須無頻閃 LED 面板燈；一般燈具的頻閃在 60 fps 下會產生明暗帶。
- **參照系統不能省。** 用消費級相機時，IMU 或光學系統是效度驗證的**唯一**黃金標準。
  建議向機構商借而非採購。

頻寬速算：網路攝影機（機內 MJPEG）約 1.5–2.5 MB/s 一台，六台 9–15 MB/s，無壓力。
工業相機未壓縮約 93 MB/s 一台，六台 559 MB/s，會超出單一 USB3 控制器上限。

---

## LED 同步：取代硬體觸發的低成本方案

網路攝影機沒有觸發腳位。以一顆 LED（成本不到一百元）作為所有相機都能看見的共同事件，
事後對齊時間軸。

關鍵是**次幀內插**：閃光發生在兩幀之間時，過渡幀的亮度會落在明暗平台中間，
用這個中間值線性內插，可將精度從一個幀間隔（60 fps 下為 16.7 ms）推進到 2–5 ms。

| 方式 | 精度 |
|---|---|
| 硬體觸發 | < 1 ms（但相機貴五倍以上） |
| LED 閃光 + 次幀內插 | 2–5 ms |
| 只找第一個變亮的幀 | 16.7 ms |
| 純軟體時戳 | 10–30 ms，抖動大 |

實作已含於 scaffold 的 `capture/sync_led.py`。錄製流程必須要求
**開始後兩秒內觸發一次閃光**，漏做則該次試作無法使用。

---

## 參考文件索引

依需要載入，不需一次全讀：

| 檔案 | 何時讀 |
|---|---|
| `references/critical-constraints.md` | 開始任何開發前；設計決策有疑慮時 |
| `references/hardware.md` | 選購設備、規劃經費、排查頻寬或畫質問題 |
| `references/architecture.md` | 設計系統分層、資料模型、雙管線切分 |
| `references/calibration.md` | P1 相機校正 |
| `references/reconstruction.md` | P2 姿態估計與三角測量 |
| `references/biomechanics.md` | P3 關節角度、REBA/RULA、L5/S1 力矩 |
| `references/multi-person.md` | P4 多人關聯與角色判定（最高風險） |
| `references/validation.md` | P5–P6 效度驗證統計、複合負荷指數 |
| `references/warning-system.md` | P7 即時預警與警示疲勞防範 |

`assets/project_template/` 為 scaffold 使用的完整專案樣板，
需要參考某個模組的寫法時可直接讀取。

---

## 學術寫作時的注意事項

若這套系統用於研究計畫或論文：

- **效度不可由步態研究外推。** 現有免標記系統的驗證多集中在步態、蹲跳等
  單人、無遮蔽、矢狀面為主的動作。職業作業通常包含扭轉（非矢狀面）、
  近距離互動（高遮蔽）、快速施力三項挑戰，必須獨立驗證。
- **分平面、分速度區間報告效度。** 免標記系統的準確度有明確的平面依賴性——
  矢狀面佳、額狀面與橫斷面差。籠統報告單一 ICC 會掩蓋這個結構。
- **界定清楚的有限結論優於含糊的全面宣稱。** 若某些條件下效度不足，
  明確說明適用範圍，學術價值高於勉強宣稱全面可用。
- **報告 ICC 時須註明模型、型式與 95% 信賴區間**（依 Koo & Li, 2016 的準則）。

主要文獻見 `references/validation.md` 末段。
