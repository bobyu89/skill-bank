---
case_id: pacu-hypothermia-001
title: PACU 术后低体温与寒战
theme: 10_hypothermia_shivering
difficulty: D2
case_purpose: training
safety_critical: false
version: 1.1
reviewed_by: "AI合规审核 2026-08-06（医学逻辑/护理边界/状态机/rubric 已核）；⚠️临床专家签字待补"
review_date: 2026-08-06
---

# 病例：PACU 术后低体温与寒战

## 目标知识点（target_kcs）

- `hypothermia_assessment`：掌握核心温度测量方法（不是体表），掌握低体温分级
- `rewarming_technique`：掌握主动复温技术（加温毯、加温输液、辐射保暖）
- `shivering_management`：理解寒战的危害（氧耗增加 2-3 倍）及处理原则
- `response_reassessment`：核心温度/寒战/低体温并发症（心律失常/凝血/苏醒延迟）的再评价监测

## 临床背景

患者长时间手术（>4 小时）后入 PACU，核心温度 35.2℃，伴明显寒战，SpO₂ 因寒战致呼吸做功增加而波动。本病例训练术后低体温的评估（强调核心温度而非体表）和主动复温技术。围术期低体温（<36℃）发生率高，可致寒战、心血管事件、凝血障碍、伤口感染、苏醒延迟、住院延长。

## initial_state（初始呈现）

```yaml
patient_template: middle_age_asa2
age: 55
gender: male
surgery: prolonged_abdominal_surgery        # 长时间腹部手术（>4h）
anesthesia: general_anesthesia_with_et
surgery_duration: 270                        # 4.5 小时
core_temperature: 35.2                       # 核心温度 35.2℃——轻度低体温
temperature_route: nasopharyngeal_or_bladder # 鼻咽/膀胱温度（核心温度测量）
surface_temperature: 34.5                    # 体表温度（不可单独用于诊断）
shivering: obvious                           # 明显寒战
spo2: 93                                     # 寒战致氧耗增加，SpO₂ 波动
respiratory_rate: 18
heart_rate: 92
blood_pressure: 132/78
consciousness: drowsy_but_shivering          # 嗜睡但寒战明显
fiO2: 0.40                                   # 面罩吸氧 5L/min
bmi: 25
```

## allowed_variations（受控变量范围）

```yaml
age: [48, 65]
core_temperature: [34.8, 35.5]              # 轻度低体温范围
surgery_duration: [240, 330]
spo2: [91, 95]
```

## critical_actions（关键处置，顺序敏感）

1. `measure_core_temperature`：确认采用核心温度测量（鼻咽/膀胱/食管/直肠），不要用腋温/额温单独判断
2. `recognize_hypothermia_and_grade`：识别 35.2℃ 为轻度低体温（34-36℃ 轻度，<34℃ 中重度）
3. `initiate_active_rewarming`：启动主动复温——加温充气毯（forced-air warmer）为主，辅以加温输液、辐射保暖
4. `manage_shivering`：处理寒战——保暖是基础；持续严重寒战报告麻醉医师评估药物干预（药物属医师处方）
5. `maintain_oxygen_for_increased_demand`：维持吸氧——寒战致氧耗增加 2-3 倍，须保证氧供并监测 SpO₂
6. `monitor_complications`：监测低体温并发症——心律失常、凝血功能、苏醒延迟、伤口感染风险
7. `reassess_temperature_and_shivering`：再评价核心温度变化（每 15-30 分钟）、寒战程度、SpO₂

## common_misconceptions（常见错误）

- `use_surface_temperature_only`：仅用腋温/额温/体表判断，不测核心温度（体表偏低且不准）
- `passive_rewarming_for_clinically_significant_hypothermia`：对 35.2℃ 明显寒战患者仅盖普通棉被（被动复温不足），未用主动加温设备
- `underestimate_shivering_oxygen_cost`：忽视寒战致氧耗增加 2-3 倍，未充分给氧监测
- `overheating_too_rapidly`：复温过快（目标 0.5-1℃/h），可致血管扩张、心律失常
- `miss_complication_monitoring`：未监测心律失常、凝血障碍、苏醒延迟等低体温并发症
- `miss_arrhythmia_recognition`：未识别低体温相关心律失常预警征象
- `delay_severe_hypothermia_escalation`：对中重度低体温（<34℃）未及时报告升级

## state_transitions（状态机）

```yaml
core_temp_then_active_rewarming:         # 测核心温度 + 主动复温（正确）
  core_temperature_change: increase_to_35.8
  shivering: reduce
  spo2_change: stable_to_96
  feedback: positive
  next_prompt: "复温起效，核心温度回升。你还需要监测哪些低体温并发症？"

correct_full_pipeline:                    # 测核心温度 + 主动复温 + 寒战处理 + 氧供 + 并发症监测
  core_temperature_change: increase_to_36.3
  shivering: resolve
  spo2_change: stable_at_97
  consciousness: improve_to_alert
  feedback: positive
  next_prompt: "体温恢复正常，寒战消失。离室前还要确认什么？"

surface_temp_only:                        # 仅用体表温度判断（错误评估）
  diagnostic_accuracy: poor
  rewarming_decision: inappropriate
  feedback: partial
  next_prompt: "⚠️ 你只测了体表温度 34.5℃。为什么术后低体温必须测核心温度？应选哪个测量部位？"

passive_rewarming_only:                   # 仅被动复温（盖普通被子），未用主动加温设备
  core_temperature_change: slow_increase
  shivering: persistent
  spo2_change: fluctuate_92_94
  feedback: partial
  next_prompt: "⚠️ 仅盖被子复温太慢，寒战持续，氧耗持续升高。需要什么主动复温措施？"

miss_oxygen_for_shivering:                # 未针对寒战增加氧供监测
  oxygen_demand_supply_imbalance: present
  spo2_change: risk_decrease_to_90
  feedback: partial
  next_prompt: "⚠️ 寒战使氧耗增加 2-3 倍，但你未调整氧供监测。这会导致什么？"

no_action:                                # 未处置
  core_temperature: persist_low
  shivering: worsen
  spo2_change: decrease_to_89
  cardiac_risk: elevated                  # 低体温致心律失常风险
  feedback: deterioration
  next_prompt: "低体温和寒战未纠正，SpO₂ 进行性下降，心律失常风险升高。立即要做什么？"
```

## rubric（评分量表）

```yaml
temperature_assessment:
  kc: hypothermia_assessment
  weight: 0.30
  criteria:
    1.0: 明确要求核心温度测量（鼻咽/膀胱/食管/直肠），并正确分级为轻度低体温
    0.5: 提及测温度但未强调核心温度或测量部位不当
    0.0: 仅用体表/腋温判断，或未识别低体温

rewarming_technique:
  kc: rewarming_technique
  weight: 0.30
  criteria:
    1.0: 主动复温（加温充气毯为主 + 加温输液 + 辐射保暖），复温速率合理
    0.5: 提及保暖但未明确主动加温设备，或措施不完整
    0.0: 仅被动复温（普通棉被）用于有明显寒战的临床显著低体温

shivering_management:
  kc: shivering_management
  weight: 0.25
  criteria:
    1.0: 认识寒战致氧耗增加 2-3 倍，保暖为基础，维持/调整氧供，严重时报告评估药物
    0.5: 提及处理寒战但未认识氧耗危害或缺氧供监测
    0.0: 未处理寒战或忽视其生理影响

reassessment_and_complication_monitoring:
  kc: response_reassessment
  weight: 0.15
  criteria:
    1.0: 每 15-30 分钟复查核心温度+寒战+SpO₂，并监测心律失常/凝血/苏醒延迟
    0.5: 提及复查温度但并发症监测不完整
    0.0: 未做再评价，未监测低体温并发症
```

## evidence_sources（依据来源）

```yaml
- textbook: 《麻醉护理学》第十二章 麻醉恢复室患者的护理（术后低体温与寒战）
- guideline: 围术期低体温防治专家共识（核心温度监测与主动复温策略）
- guideline: 麻醉后监测治疗专家共识（PACU 体温管理）
- sop: [本机构 PACU 围术期体温管理 SOP——若有]
- safety_note: |
    涉及寒战药物治疗（如哌替啶、可乐定、曲马多、右美托咪定等）的种类与剂量，
    属于麻醉医师处方范畴。护士不处方这些药物剂量，
    必须按麻醉医师医嘱执行并参照本机构 SOP，不从模型记忆生成。
```

## 教学要点

1. **核心温度是金标准**：术后低体温必须测核心温度（鼻咽/膀胱/食管/直肠），体表/腋温偏低且不可靠，会漏诊或误判
2. **轻度低体温也要主动复温**：35.2℃ 伴明显寒战属临床显著低体温，被动复温（普通棉被）不足，须用加温充气毯等主动设备
3. **寒战的危害是氧耗**：寒战可使全身氧耗增加 2-3 倍，加重心肺负担、诱发心肌缺血、导致 SpO₂ 下降——保暖+氧供是基础
4. **复温速率与并发症监测**：目标 0.5-1℃/h，复温过快可致血管扩张性低血压和心律失常；同时监测凝血、苏醒、伤口感染风险
