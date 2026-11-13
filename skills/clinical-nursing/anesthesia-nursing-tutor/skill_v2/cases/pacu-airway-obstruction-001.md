---
case_id: pacu-airway-obstruction-001
title: PACU 上呼吸道梗阻（舌后坠）
theme: 2_upper_airway_obstruction
difficulty: D2
case_purpose: training
safety_critical: false
version: 1.1
reviewed_by: "AI合规审核 2026-08-06（医学逻辑/护理边界/状态机/rubric 已核）；⚠️临床专家签字待补"
review_date: 2026-08-06
---

# 病例：PACU 上呼吸道梗阻（舌后坠）

## 目标知识点（target_kcs）

- `upper_airway_obstruction`：识别上呼吸道梗阻的征象
- `oxygenation_assessment`：评估氧合状态
- `airway_priority`：判断气道处理的优先级
- `airway_intervention`：掌握开放气道的护理手法（抬颏/托颌/侧卧位）及通气管的使用
- `response_reassessment`：处置后复查 SpO₂/RR/意识的闭环再评价

## 临床背景

患者全麻腹腔镜胆囊切除术后入 PACU。麻醉尚未完全清醒，出现典型的舌后坠致上呼吸道梗阻。

## initial_state（初始呈现）

```yaml
patient_template: middle_age_asa2
age: 52
gender: male
surgery: laparoscopic_cholecystectomy
anesthesia: general_anesthesia_with_lma
consciousness: drowsy              # 嗜睡，呼之能应但很快又睡
respiratory_rate: 12               # 偏慢
spo2: 88                           # 下降（未吸氧）
airway_sound: snoring              # 鼾声——关键征象
etco2: 48                          # 升高
oxygen_delivery: room_air          # 入室时未吸氧（尚未给氧）
bmi: 30
```

## allowed_variations（受控变量范围）

```yaml
age: [45, 60]
bmi: [28, 34]
spo2: [84, 91]
respiratory_rate: [10, 14]
```

## critical_actions（关键处置，顺序敏感）

1. `assess_airway_patency`：评估气道通畅性（看胸廓起伏、听鼾声、感受口气）
2. `perform_airway_opening_maneuver`：开放气道的护理手法（抬颏/托颌/侧卧位）
3. `administer_oxygen`：给氧（气道开放后）
4. `reassess_oxygenation_and_ventilation`：再评价 SpO₂、RR、意识
5. `consider_airway_adjuvant`：考虑口咽/鼻咽通气管（若手法无效）
6. `call_anesthesiologist_if_persistent`：持续不缓解时报告麻醉医师

## common_misconceptions（常见错误）

- `oxygen_before_airway`：先给氧而非先开放气道（最常见错误）
- `miss_reassessment`：开放气道后漏做再评价
- `delay_escalation`：手法无效且持续梗阻时未及时报告

## state_transitions（状态机）

```yaml
airway_opened:                    # 学习者执行了开放气道（正确）
  spo2_change: increase_to_95
  snoring: resolve
  consciousness: improve_but_still_drowsy   # 气道通畅后缺氧改善，但麻醉未完全清醒，仍嗜睡
  feedback: positive
  next_prompt: "再评价后，你还会做什么？"

airway_opened_then_oxygen:        # 开放气道 + 给氧（完整正确）
  spo2_change: increase_to_97
  snoring: resolve
  consciousness: improve_but_still_drowsy   # 氧合改善，意识部分恢复但未完全清醒
  feedback: positive
  next_prompt: "患者情况改善。离室评估还需要关注什么？"

oxygen_only:                      # 只给氧未开放气道（常见错误）
  spo2_change: temporary_increase_to_92
  snoring: persistent
  consciousness: unchanged_drowsy
  feedback: partial
  next_prompt: "SpO₂ 暂升到 92%，但鼾声持续、意识仍嗜睡。说明什么问题？"

no_action:                        # 未处置
  spo2_change: decrease_to_82
  etco2: increase_to_55
  consciousness: worsen_to_unresponsive
  feedback: deterioration
  next_prompt: "病情恶化。你立即要做什么？"

incorrect_priority_repeated:      # 反复只给氧不开放气道
  spo2_change: fluctuate_88_92
  snoring: persistent
  feedback: deterioration
  next_prompt: "⚠️ 根本问题（气道梗阻）未解决。ABC 中 A 永远优先。"
```

## rubric（评分量表）

```yaml
key_sign_recognition:
  kc: upper_airway_obstruction
  weight: 0.30
  criteria:
    1.0: 识别鼾声 + SpO₂下降 + 意识嗜睡，判断为气道梗阻
    0.5: 识别部分征象但未归结到气道梗阻
    0.0: 未识别关键征象

priority_judgment:
  kc: airway_priority
  weight: 0.25
  criteria:
    1.0: 先开放气道再给氧（正确优先级）
    0.5: 同时进行或顺序模糊
    0.0: 先给氧再考虑气道（错误优先级）

nursing_action:
  kc: airway_intervention
  weight: 0.25
  criteria:
    1.0: 正确实施抬颏/托颌/侧卧位
    0.5: 提及开放气道但手法描述不清
    0.0: 未提及任何气道开放手法

reassessment:
  kc: response_reassessment
  weight: 0.20
  criteria:
    1.0: 处置后复查 SpO₂/RR/意识
    0.5: 提及复查但不完整
    0.0: 未做再评价
```

## evidence_sources（依据来源）

```yaml
- textbook: 《麻醉护理学》第十二章 麻醉恢复室患者的护理
- guideline: 麻醉后监测治疗专家共识
- sop: [本机构 PACU 管理制度——若有]
```

## 教学要点

1. **舌后坠是 PACU 最常见的上呼吸道梗阻原因**，鼾声是关键征象
2. **ABCDE 评估法**：A(气道) 永远优先于 B(呼吸)——先开放气道再给氧
3. **再评价是闭环**：处置后必须复查效果
4. **升级时机**：手法+通气管无效且持续梗阻 → 立即报告麻醉医师
