---
case_id: pacu-residual-neuromuscular-001
title: PACU 残余神经肌肉阻滞（残余肌松）
theme: 4_residual_neuromuscular_block
difficulty: D2
case_purpose: training
safety_critical: true
version: 1.1
reviewed_by: "AI合规审核 2026-08-06（医学逻辑/护理边界/状态机/rubric 已核）；⚠️临床专家签字待补"
review_date: 2026-08-06
---

# 病例：PACU 残余神经肌肉阻滞（残余肌松）

## 目标知识点（target_kcs）

- `residual_block_recognition`：识别残余肌松的临床征象（抬头<5 秒、握力弱、舌咽反射弱）
- `train_of_four_assessment`：掌握 TOF（四个成串刺激）评估方法及判读（TOF<0.9 提示残余阻滞）
- `airway_protection`：理解残余肌松对气道保护反射的威胁及护理对策
- `response_reassessment`：报告后核对执行医嘱（含拮抗药）→ 再评价 TOF/抬头/舌咽反射、监测再箭毒化风险的闭环

## 临床背景

患者全麻下腹部手术后入 PACU，已拔除气管导管。麻醉护士交接时发现患者清醒但**不能坚持抬头 5 秒**、握力明显减弱，SpO₂ 有波动趋势。本病例训练识别**残余神经肌肉阻滞**——这是 PACU 致呼吸抑制、误吸、再插管的重要原因，TOF 监测是客观评估手段。

## initial_state（初始呈现）

```yaml
patient_template: middle_age_asa2
age: 62
gender: female
surgery: total_abdominal_hysterectomy       # 经腹全子宫切除
anesthesia: general_anesthesia_with_et
neuromuscular_blockade: rocuronium           # 术中使用罗库溴铵
reversal: neostigmine_administered           # 术毕已给新斯的明拮抗（但可能不完全）
consciousness: alert                         # 清醒，能应答
spo2: 94                                     # 面罩吸氧 5L/min 下边缘值，有波动
respiratory_rate: 14
head_lift_5sec: unable                       # 抬头不能坚持 5 秒——关键征象
hand_grip: weak                              # 握力弱
gag_reflex: weak                             # 舌咽/吞咽反射减弱——气道保护受损
tof_ratio: 0.65                              # TOF 比值 0.65（<0.9 提示残余阻滞）
vital_capacity: reduced                      # 用力肺活量下降
bmi: 28
```

## allowed_variations（受控变量范围）

```yaml
age: [55, 70]
spo2: [92, 96]
tof_ratio: [0.55, 0.75]                      # 均 <0.9，确保残余阻滞存在
head_lift_5sec: [unable, barely]             # 抬头均不达标
```

## critical_actions（关键处置，顺序敏感）

1. `recognize_residual_block_signs`：识别抬头<5 秒+握力弱+舌咽反射弱为残余肌松征象
2. `confirm_with_tof`：用 TOF 监测客观确认（TOF<0.9），不要仅凭临床征象
3. `protect_airway`：气道保护——侧卧位、备好口咽通气道、床旁备吸引器（防误吸）
4. `maintain_oxygen_and_monitor`：维持吸氧，持续监测 SpO₂、RR、意识、呼吸做功
5. `avoid_premature_discharge`：禁止在肌松未恢复前离室（PADSS 离室标准不达标）
6. `report_anesthesiologist_and_prepare_antagonist_order`：报告麻醉医师（残余肌松需评估是否需要追加拮抗/补救）；按医嘱**核对**准备并执行拮抗药（新斯的明/舒更葡糖钠——种类与剂量由医师决定），给药后监测起效与不良反应
7. `reassess_neuromuscular_recovery`：再评价 TOF、抬头试验、舌咽反射；警惕"再箭毒化"（舒更葡糖钠/新斯的明作用消退后肌松再现），延长监测时间

## common_misconceptions（常见错误）

- `dismiss_head_lift_finding`：忽视"抬头不能坚持 5 秒"这一关键临床征象，仅凭清醒就认为恢复良好
- `clinical_signs_without_tof`：只凭临床征象判断，不做 TOF 客观评估（临床征象不敏感）
- `allow_early_oral_intake`：在舌咽反射未恢复时允许饮水/进食（误吸风险）
- `premature_discharge`：在 TOF<0.9 时安排离室（违反离室标准）
- `delay_recognition_of_respiratory_risk`：未认识到残余肌松可致延迟性呼吸抑制
- `escalation_delay`：识别后未及时报告麻醉医师

## state_transitions（状态机）

```yaml
recognize_then_tof_then_protect:        # 识别 + TOF 确认 + 气道保护 + 报告（完整正确）
  respiratory_safety: maintained
  spo2_change: stable_at_96             # 气道保护+吸氧下氧合稳定
  airway_protection: side_position_with_suction_ready
  feedback: positive
  next_prompt: "你正确识别并保护了患者。等待麻醉医师评估期间，还需监测什么？"

recognize_signs_only:                   # 识别征象但未做 TOF 确认
  spo2_change: stable_at_94
  diagnostic_certainty: incomplete
  feedback: partial
  next_prompt: "你识别了抬头困难，但仅凭临床征象不敏感。还需要哪项客观评估？"

tof_but_miss_airway_protection:         # 做了 TOF 但忽视气道保护（侧卧位/吸引准备）
  spo2_change: fluctuate_92_95
  aspiration_risk: elevated
  feedback: partial
  next_prompt: "⚠️ TOF 0.65 提示舌咽反射受损，误吸风险升高。你忽略了哪项关键护理？"

premature_discharge_attempt:            # 在 TOF<0.9 时尝试离室
  spo2_change: decrease_to_90           # 转运/离室后呼吸抑制
  respiratory_event: respiratory_depression
  feedback: deterioration
  next_prompt: "⚠️ 违反离室标准。残余肌松患者离室后可发生呼吸抑制。重新评估离室条件。"

no_action:                              # 未识别残余肌松征象
  spo2_change: decrease_to_88
  respiratory_rate: decrease_to_10
  consciousness: worsen_to_drowsy       # 呼吸抑制进展
  aspiration_risk: high
  feedback: deterioration
  next_prompt: "病情恶化，出现呼吸抑制征象。立即要做什么？"
```

## rubric（评分量表）

```yaml
key_sign_recognition:
  kc: residual_block_recognition
  weight: 0.30
  criteria:
    1.0: 识别抬头<5 秒+握力弱+舌咽反射弱，判断为残余神经肌肉阻滞
    0.5: 识别部分征象但未归结到残余肌松
    0.0: 未识别关键征象或忽视气道保护反射受损

tof_assessment:
  kc: train_of_four_assessment
  weight: 0.30
  criteria:
    1.0: 主动提出做 TOF 监测，正确判读 TOF<0.9 为残余阻滞
    0.5: 提及 TOF 但判读标准不清（如未提 0.9 阈值）
    0.0: 未做 TOF 或不会判读（仅凭临床征象）

airway_protection:
  kc: airway_protection
  weight: 0.25
  criteria:
    1.0: 实施侧卧位+备吸引器+避免过早经口进食，明确保护气道反射
    0.5: 提及气道保护但措施不完整
    0.0: 未做气道保护或允许过早进食饮水

escalation_and_discharge_safety:
  kc: response_reassessment
  weight: 0.15
  criteria:
    1.0: 报告麻醉医师评估是否追加拮抗，并坚持 TOF≥0.9 才离室
    0.5: 提及报告但离室标准把握不严
    0.0: 未报告或允许残余肌松患者离室（违反安全标准）
```

## evidence_sources（依据来源）

> ⚠️ safety_critical=true：以下来源须标注版本年份/章节页码/核验人后才能用于教学输出（critical-content.md 规则3）。
> AI 合规审核已核医学逻辑与护理边界；**教材版次页码与指南年份待临床专家补核**，补核前不得从模型记忆补全具体剂量/阈值。

```yaml
- textbook: 《麻醉护理学》（刘保江、晁储璋，人民卫生出版社）第十二章 麻醉恢复室患者的护理（神经肌肉阻滞恢复评估）
  edition: ⚠️待补版次与年份
  page: ⚠️待补具体页码
  verified_by: ⚠️待临床专家核验
- guideline: 麻醉后监测治疗专家共识（残余肌松监测与离室标准）
  year: ⚠️待补发布年份与适用状态
  verified_by: ⚠️待临床专家核验
- guideline: 残余神经肌肉阻滞防治专家共识（TOF 监测与拮抗指征）
  year: ⚠️待补发布年份与适用状态
  verified_by: ⚠️待临床专家核验
- sop: [本机构 PACU 离室标准与 TOF 监测 SOP——若有，待补版本号]
- safety_note: |
    涉及肌松拮抗药（如新斯的明、舒更葡糖钠 Sugammadex）的种类选择与剂量，
    属于麻醉医师处方范畴。护士不处方拮抗药剂量，
    必须按麻醉医师医嘱执行并参照本机构 SOP，不从模型记忆生成。
    舒更葡糖钠/新斯的明作用消退后存在"再箭毒化"风险，须延长监测时间。
```

## 教学要点

1. **抬头试验是最实用的床旁评估**：能坚持抬头 5 秒是肌松恢复的经典临床指标；不能坚持即提示残余阻滞
2. **TOF 是客观金标准**：TOF 比值≥0.9 才视为恢复充分；仅凭临床征象不敏感，会漏诊残余肌松
3. **残余肌松的核心危害是气道保护反射丧失**：舌咽反射弱→误吸风险；呼吸肌力弱→延迟性呼吸抑制
4. **离室标准是硬红线**：TOF<0.9 不应离室；护士的职责是识别、保护气道、报告，拮抗药决策由麻醉医师作出
