---
case_id: pacu-postoperative-pain-001
title: PACU 术后疼痛评估与 PCA 管理
theme: 8_postoperative_pain
difficulty: D2
case_purpose: training
safety_critical: false
version: 1.1
reviewed_by: "AI合规审核 2026-08-06（医学逻辑/护理边界/状态机/rubric 已核）；⚠️临床专家签字待补"
review_date: 2026-08-06
---

# 病例：PACU 术后疼痛评估与 PCA 管理

## 目标知识点（target_kcs）

- `pain_assessment_nrs`：掌握成人数字疼痛评分（NRS 0-10）与疼痛的综合评估（部位/性质/加重缓解因素）
- `pca_function_check`：掌握 PCA（自控镇痛）设备与管路的功能核查（药物余量、锁定时间、泵运行、管路通畅、单次给药有效性）
- `pain_differential_somatic_vs_visceral`：区分躯体痛（切口痛）与内脏痛、导管相关痛（处置路径不同）
- `response_reassessment`：镇痛反应与阿片不良反应（镇静/呼吸抑制）的监测再评价

## 临床背景

中年患者腹部手术后入 PACU，已配置 PCA（自控镇痛）但主诉切口疼痛剧烈 NRS 7 分，自诉按压 PCA 效果不好。本病例训练术后疼痛的系统评估与 PCA 故障排查能力。镇痛不全须鉴别三类原因：① PCA 设备/管路问题（最易解决，护士可独立排查）；② 疼痛性质判断（切口躯体痛 vs 内脏痛 vs 导管相关痛，镇痛策略不同）；③ PCA 参数设置问题（需麻醉医师调整）。护士不调整 PCA 参数（药物浓度/单次剂量/锁定时间/背景输注），但必须能完成疼痛评估、设备管路排查、鉴别疼痛性质，并向麻醉医师提供清晰的评估报告以指导调整。

## initial_state（初始呈现）

```yaml
patient_template: middle_age_asa2
age: 55
gender: female
surgery: open_colectomy                       # 开腹结肠切除术（上腹部/中部切口）
anesthesia: general_anesthesia_with_epidural  # 全麻+硬膜外（硬膜外未用药，PCA 静脉镇痛）
pca: intravenous_pca_running                  # 静脉 PCA 在运行（如吗啡/舒芬太尼）
pca_drug: morphine                            # PCA 药物（示例）
pca_lockout_time: 10_min                      # 锁定时间 10 分钟
pca_attempts_vs_deliveries: pending           # 按压次数与实际给药次数比待查
pca_residual_volume: pending                  # 药物余量待查
consciousness: alert                          # 清醒，能配合评估
spo2: 97                                      # 面罩吸氧 5L/min
respiratory_rate: 16
heart_rate: 96
blood_pressure: 145_88                        # 偏高（疼痛所致）
pain_score_nrs: 7                             # NRS 7 分——中重度疼痛
pain_location: abdominal_incision             # 腹部切口
pain_quality: sharp_continuous                # 锐痛、持续
time_since_end_anesthesia: 45_min             # 术毕 45 分钟
sedation_score: mild                          # 镇静评分轻度（警惕阿片过量）
nausea: mild                                  # 轻度恶心
drain: abdominal_drain_in_situ                # 腹腔引流管在位
urinary_catheter: in_situ                     # 导尿管在位
bmi: 25
```

## allowed_variations（受控变量范围）

```yaml
age: [40, 70]
pain_score_nrs: [6, 9]                        # 均为中重度疼痛
blood_pressure_systolic: [135, 160]           # 均因疼痛偏高
pca_lockout_time: [8, 15]
heart_rate: [88, 108]
```

## critical_actions（关键处置，顺序敏感）

1. `assess_pain_systematically`：系统评估疼痛——NRS 评分（7 分为中重度）、部位（腹部切口）、性质（锐痛/钝痛/绞痛）、加重缓解因素、起病时间、与手术关系；同时评估镇静评分（警惕阿片过量致呼吸抑制）
2. `check_pca_device_and_line`：核查 PCA 设备与管路——泵是否正常运行、药物余量、按压次数 vs 实际给药次数比（反映锁定时间内的无效按压）、管路是否通畅/扭曲/堵塞、连接是否牢固、单次给药按钮是否有效
3. `assess_sedation_and_respiratory_safety`：评估镇静评分（如 RSS/Ramsay）和呼吸状态——警惕阿片过量（过度镇静、RR<10、SpO₂ 下降），镇痛不全与呼吸抑制须同时监测
4. `differentiate_pain_type`：鉴别疼痛性质——
   - **躯体痛（切口痛）**：表浅、定位明确、锐痛、随体位/咳嗽加重（本例主要）
   - **内脏痛**：深部、定位模糊、钝痛/绞痛、伴恶心呕吐（腹部手术后内脏痛常见）
   - **导管相关痛**：引流管/导尿管刺激、局部牵扯痛、与导管位置相关
5. `non_pharmacological_comfort`：非药物辅助镇痛——调整体位、切口支撑（咳嗽时按压）、环境舒适、心理安抚
6. `report_anesthesiologist_for_pca_adjustment`：报告麻醉医师——提供完整评估（NRS/性质/PCA 排查结果/镇静评分），PCA 参数调整（药物浓度/单次剂量/锁定时间/背景输注）属医师处方
7. `monitor_pca_response_and_adverse`：监测镇痛反应（NRS 变化）与不良反应（镇静过度、呼吸抑制、恶心呕吐、瘙痒、尿潴留）
8. `reassess_pain_after_intervention`：再评价 NRS、镇静评分、呼吸、PCA 运行状态（目标 NRS≤4，镇静评分适度）

## common_misconceptions（常见错误）

- `skip_pca_device_check`：未核查 PCA 设备/管路就报告"镇痛不全"，遗漏可由护士独立解决的最简单原因（管路扭曲/堵塞/泵故障）
- `nurse_adjust_pca_parameters`：护士自行调整 PCA 参数（药物浓度/单次剂量/锁定时间/背景输注）——越界处方，违反安全规范
- `treat_pain_as_single_type`：将所有疼痛视为"切口痛"，未鉴别躯体痛/内脏痛/导管相关痛（处置策略不同）
- `miss_sedation_monitoring`：只关注疼痛评分，忽视镇静评分和呼吸监测（追加镇痛后可能发生阿片过量致呼吸抑制）
- `ignore_pca_attempts_ratio`：未看按压次数 vs 给药次数比——比值高提示频繁触发锁定（参数不足或疼痛性质判断错误）
- `escalation_delay`：镇痛不全（NRS≥7）未及时报告麻醉医师调整
- `over_rely_on_pharmacology`：忽视非药物镇痛（体位、支撑、心理安抚）
- `miss_pca_adverse_effects`：未监测 PCA 阿片类不良反应（恶心呕吐、瘙痒、尿潴留、过度镇静）

## state_transitions（状态机）

```yaml
assess_then_check_pca_then_differentiate:    # 疼痛评估 + PCA 排查 + 疼痛性质鉴别（正确核心流程）
  diagnostic_clarity: improving
  pca_issue_identified: yes_or_ruled_out
  feedback: positive
  next_prompt: "你完成了疼痛评估和 PCA 排查。你判断这是什么性质的疼痛？应报告哪些信息给麻醉医师？"

correct_full_pipeline_with_report:           # 评估 + PCA 排查 + 鉴别 + 非药物 + 报告 + 监测（完整正确）
  pain_score: decrease_to_4
  blood_pressure: decrease_to_130_80
  sedation_score: appropriate
  respiratory_rate: stable
  feedback: positive
  next_prompt: "疼痛缓解到 NRS 4。你还需要监测 PCA 的哪些不良反应？目标 NRS 是多少？"

identify_pca_device_issue:                   # 识别 PCA 设备/管路问题（护士可独立解决）
  pca_issue: resolved
  pain_score: partial_decrease
  feedback: positive
  next_prompt: "你发现并解决了 PCA 管路问题。但疼痛评分仍偏高，还应报告什么？"

skip_pca_check_directly_report:              # 未排查 PCA 设备就报告（流程不全）
  potential_fixable_issue: missed
  diagnostic_completeness: poor
  feedback: partial
  next_prompt: "⚠️ 你没有核查 PCA 设备和管路就报告镇痛不全。哪些问题是你作为护士可以独立排查和解决的？"

nurse_self_adjust_pca:                       # 护士自行调整 PCA 参数（越界处方）
  scope_of_practice: violated
  patient_safety: at_risk
  feedback: partial
  next_prompt: "⚠️ PCA 参数（药物浓度/单次剂量/锁定时间/背景输注）属于麻醉医师处方。你的职责是什么？应如何报告？"

treat_as_single_pain_type:                   # 未鉴别疼痛性质，一律按切口痛处理
  pain_differential: incomplete
  treatment_mismatch_risk: present
  feedback: partial
  next_prompt: "⚠️ 你没有鉴别疼痛性质。躯体痛（切口）、内脏痛、导管相关痛的处置策略有何不同？"

miss_sedation_respiratory_monitoring:        # 只看疼痛，忽视镇静和呼吸监测
  opioid_overdose_risk: unrecognized
  respiratory_depression_risk: elevated
  feedback: partial
  next_prompt: "⚠️ 你只关注了疼痛评分。PCA 阿片类药物最大的风险是什么？还应监测什么？"

no_action_or_delayed_report:                 # 未处置或延迟报告
  pain_score: persist_7_or_increase
  blood_pressure: persist_elevated
  patient_distress: ongoing
  feedback: deterioration
  next_prompt: "⚠️ 患者持续中重度疼痛，血压偏高，PCA 效果不好。立即要做什么？"
```

## rubric（评分量表）

```yaml
pain_assessment:
  kc: pain_assessment_nrs
  weight: 0.30
  criteria:
    1.0: 用 NRS 完整评估疼痛（评分+部位+性质+加重缓解因素+时间），同时评估镇静评分
    0.5: 评估了 NRS 评分但缺少性质/部位/镇静评分等综合信息
    0.0: 仅问疼痛评分，未做系统评估或忽视镇静监测

pca_function_check:
  kc: pca_function_check
  weight: 0.30
  criteria:
    1.0: 系统核查 PCA——泵运行、药物余量、按压/给药比、管路通畅、单次给药有效性（无遗漏）
    0.5: 检查了部分项目但不完整
    0.0: 未核查 PCA 设备/管路就直接报告，遗漏护士可独立解决的问题

pain_differential:
  kc: pain_differential_somatic_vs_visceral
  weight: 0.20
  criteria:
    1.0: 鉴别躯体痛（切口）/内脏痛/导管相关痛，明确主要疼痛性质以指导策略
    0.5: 提及疼痛性质但鉴别不系统
    0.0: 将所有疼痛视为单一类型，未做鉴别

escalation_and_monitoring:
  kc: response_reassessment
  weight: 0.20
  criteria:
    1.0: 用 SBAR 报告麻醉医师调整 PCA 参数（不自行调整），监测镇痛反应与阿片不良反应（镇静/呼吸/恶心/瘙痒/尿潴留），再评价 NRS 目标
    0.5: 报告但监测不完整，或自行调整 PCA 参数（越界）
    0.0: 自行调整 PCA 参数（越界处方）、未监测不良反应或未再评价
```

## evidence_sources（依据来源）

```yaml
- textbook: 《麻醉护理学》第十二章 麻醉恢复室患者的护理（术后疼痛评估与PCA管理）
- textbook: 《疼痛学》急性术后疼痛管理章节
- guideline: 成人术后疼痛处理专家共识（PCA 管理与多模式镇痛）
- guideline: 麻醉后监测治疗专家共识（PACU 疼痛管理）
- scale: NRS 数字疼痛评分（0-10，≤4 为达标，≥7 为中重度需处理）
- scale: 镇静评分（如 Ramsay/RASS，警惕过度镇静）
- sop: [本机构 PACU 术后疼痛评估与 PCA 管理 SOP——若有]
- safety_note: |
    涉及 PCA 参数设置（药物种类与浓度、单次剂量、锁定时间、背景输注速率）、
    镇痛药种类选择与剂量调整、补救镇痛方案，
    均属于麻醉医师处方范畴。护士不调整 PCA 参数、不处方镇痛药剂量，
    必须按麻醉医师医嘱执行并参照本机构 SOP，不从模型记忆生成。
    涉及阿片类药物过量（呼吸抑制）的拮抗处理（如纳洛酮）参照本机构应急预案 SOP。
```

## 教学要点

1. **疼痛评估是系统过程**：NRS 评分只是起点，必须同时评估部位、性质（锐/钝/绞痛）、加重缓解因素、起病时间——并同步评估镇静评分（警惕阿片过量）
2. **PCA 设备/管路排查是护士独立职责**：泵运行、药物余量、按压/给药比、管路通畅、单次给药有效性——这些是镇痛不全最易解决的原因，护士必须先排查再报告
3. **疼痛性质鉴别指导策略**：躯体痛（切口，表浅、锐痛、随体位/咳嗽加重）、内脏痛（深部、钝痛/绞痛、伴恶心）、导管相关痛（局部牵扯）——不同性质镇痛策略不同，盲目追加阿片不总是有效
4. **护士不调整 PCA 参数**：药物浓度/单次剂量/锁定时间/背景输注属麻醉医师处方；护士的核心职责是准确评估、排查设备管路、鉴别疼痛性质、用 SBAR 报告、监测反应与不良反应
5. **镇痛与呼吸安全并重**：PCA 阿片类最大风险是过度镇静和呼吸抑制——疼痛评分下降时必须同步监测镇静评分和 RR/SpO₂；目标 NRS≤4，但镇静须适度不能过深
