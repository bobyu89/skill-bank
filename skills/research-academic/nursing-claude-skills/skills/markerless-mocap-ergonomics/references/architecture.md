# 系統架構與資料模型

---

## 七層架構

| 層級 | 名稱 | 主要組成 |
|---|---|---|
| L6 | 應用層 | Web UI、即時警示介面、研究者分析後台 |
| L5 | 分析層 | 複合負荷指數、風險偵測、疲勞預測 |
| L4 | 生物力學層 | 關節角度、REBA/RULA、L5/S1 逆動力學 |
| L3 | 感知層 | 2D 多人姿態 → 跨視角關聯 → 3D 三角測量 → 濾波 |
| L2 | 同步層 | 統一時基、LED 閃光對齊、時鐘漂移補償 |
| L1 | 採集層 | 多相機、生理感測器、電子量表 |
| L7 | 資料層 | 時序資料庫、詮釋資料、物件儲存 |

L1–L5 為資料處理主幹，由下而上逐層提升抽象；L6 為介面；L7 橫跨各層。

---

## 雙管線切分

見 `critical-constraints.md` 第五節。兩條管線共用 L4、L5 與資料模型，
僅 L1–L3 的實作路徑分離。

---

## 多模態時間同步

**使用 Lab Streaming Layer（LSL）**，不要自行實作。

LSL 是研究級多模態時間同步的事實標準，專為此需求設計：
統一時基、自動時鐘漂移補償、標準化的 XDF 記錄格式。
自行實作幾乎必然會在時鐘漂移或緩衝延遲上出錯。

各模態接入方式：
- 相機：每幀時戳寫入 CSV，事後以 LED 閃光對齊到 LSL 時基
- HRV：多數胸帶（如 Polar H10）有現成的 LSL 串流器
- EMG：商用系統多支援 LSL
- 量表事件：以 LSL marker stream 記錄填答時刻

---

## 資料模型

```
Participant（受試者）
├─ participant_id（去識別化代碼）
├─ role, years_experience
├─ height_cm, weight_kg          ← 肢段慣性參數計算所需
└─ consent_version

Session（場次）
├─ session_id, participant_id
├─ datetime, venue
└─ calibration_id                ← 綁定當時的校正

Trial（試作）— 實驗設計核心
├─ trial_id, session_id
├─ <自變項欄位>                   ← 每個實驗因子一欄，便於統計分析
├─ repetition_index
└─ task_phase_annotations (JSONB)

Calibration
├─ intrinsics, extrinsics
├─ reprojection_error_px
├─ scale_check_error_pct         ← 第二道驗證，見 calibration.md
├─ camera_settings_hash          ← 載入時驗證設定未變
└─ valid_from, valid_until

PoseFrame（時序）→ 時序資料庫 hypertable
├─ trial_id, t, subject_role     ← subject_role 支援多人
├─ joint_positions (J, 3)
├─ confidence (J,)
├─ n_visible_cameras (J,)        ← 遮蔽程度，供分層分析
└─ is_interpolated (J,)          ← 插補標記，不可省

BiomechMetric（時序）
├─ trunk_flexion/lateral/rotation_deg
├─ reba_score, reba_score_components (JSONB)
├─ l5s1_moment_nm
├─ computed_by                   ← fast_linkage / opensim
└─ definition_version            ← 角度定義版本

BioSignal（時序）
├─ trial_id, t, signal_type, channel, value

SurveyResponse
├─ trial_id, instrument, scores (JSONB)

RiskEvent
├─ t_start, t_end, event_type, severity
├─ triggered_alert (bool)
└─ suppressed_reason             ← 被抑制的事件也要記錄

ValidationPair（效度驗證）
├─ metric_name
├─ system_value, reference_value, reference_system
├─ occlusion_level               ← 分層分析用
└─ angular_velocity              ← 分速度區間分析用
```

### 幾個容易被省略但很重要的欄位

| 欄位 | 為什麼不能省 |
|---|---|
| `n_visible_cameras` | 遮蔽程度的量化指標，是分層效度分析的基礎 |
| `is_interpolated` | 不標記則插補值會被當實測值，虛高效度 |
| `computed_by` | 雙管線結果混在一起會使分析失效 |
| `definition_version` | 角度定義若中途修改，能區分新舊資料 |
| `suppressed_reason` | 閾值調校的資料基礎 |
| `camera_settings_hash` | 防止用過期校正處理新資料 |

---

## 技術選型建議

| 用途 | 選型 | 理由 |
|---|---|---|
| 語言 | Python 3.11+ | 生態完整 |
| 影像擷取 | OpenCV（Windows 用 `CAP_DSHOW`）| `CAP_MSMF` 多相機同開不穩定 |
| 多模態同步 | Lab Streaming Layer | 研究級標準，勿自行造輪 |
| 2D 姿態 | MMPose (RTMPose) | 原生多人；多規模對應雙管線 |
| 校正 | OpenCV + ChArUco | 需 `opencv-contrib-python` |
| 三角測量 | Anipose 或自建（參考其時空正則化）| 對遮蔽穩健 |
| 肌肉骨骼模擬 | OpenSim（離線選配）| 非關鍵路徑 |
| 時序資料 | PostgreSQL + TimescaleDB | 時序壓縮與連續聚合；相容標準 SQL |
| 資料版本 | DVC | 研究可重現性的基礎 |
| 實驗追蹤 | MLflow | 模型訓練歷程 |
| 後端 | FastAPI | 原生非同步與 WebSocket |
| 容器化 | Docker Compose | 跨機構部署 |

**注意：** 這類專案的資料存取模式是「時間區間查詢 + 聚合」，
應使用時序資料庫，不是向量資料庫。

---

## 程式碼組織

```
<package>/
├── capture/       # L1–L2：相機探索、錄製、LED 同步
├── calib/         # P1：ChArUco 校正、內外參管理
├── pose/          # L3：2D 姿態、跨視角關聯、三角測量、濾波
├── biomech/       # L4：關節角度、REBA/RULA、逆動力學
├── analytics/     # L5：負荷指數、風險偵測、疲勞預測
├── viz/           # 3D 回放、圖表
├── io/            # 資料格式、時序儲存
└── api/           # L6：FastAPI、WebSocket
```

**原則：硬體相關邏輯與純運算邏輯必須分離。** 例如相機設定的資料結構
應放在獨立模組，不要與 OpenCV 呼叫混在同一檔案——
否則只是要讀一份設定檔也得安裝 OpenCV，純運算部分就無法在無相機環境測試。
