---
case_id: pacu-ponv-001
title: PACU 术后恶心呕吐（PONV）
theme: 9_ponv
difficulty: D2
case_purpose: training
safety_critical: true
version: 1.1
reviewed_by: "AI合规审核 2026-08-06（医学逻辑/护理边界/状态机/rubric 已核）；⚠️临床专家签字待补"
review_date: 2026-08-06
---

# 病例：PACU 术后恶心呕吐（PONV）

## 目标知识点（target_kcs）

- `ponv_risk_assessment`：掌握 PONV 风险因素评估（Apfel 简化评分：女性/非吸烟/PONV 史/术后阿片）
- `aspiration_prevention`：预防误吸的护理措施（体位、吸引准备、评估意识与反射）
- `antiemetic_nursing`：止吐药护理（执行医嘱、监测反应、识别疗效与不良反应）
- `response_reassessment`：恶心呕吐/误吸征象/脱水电解质的再评价监测

## 临床背景

女性非吸烟患者全麻下妇科手术后入 PACU，30 分钟内呕吐 2 次，主诉恶心。本病例训练 PONV 的风险评估、误吸预防（尤其未完全清醒时误吸风险高）和止吐药护理。PONV 是 PACU 最常见并发症之一，严重时可致误吸、脱水、伤口张力增加、电解质紊乱、延长住院。

## initial_state（初始呈现）

```yaml
patient_template: middle_age_asa2
age: 42
gender: female                            # Apfel 风险因素之一
smoking_status: non_smoker                # Apfel 风险因素之二
surgery: gynecological_laparotomy         # 妇科开腹手术（高 PONV 风险手术）
anesthesia: general_anesthesia_with_et
consciousness: drowsy_but_arousable        # 嗜睡但可唤醒——误吸风险升高
ponv_history: yes                         # Apfel 风险因素之三（既往 PONV 史）
postoperative_opioid: yes                 # Apfel 风险因素之四（术后阿片镇痛）
apfel_score: 4                            # 4 个风险因素全中——高危
spo2: 95                                  # 面罩吸氧 5L/min
vomiting_episodes: 2                      # 已呕吐 2 次
nausea_score: 7                           # 中重度恶心（0-10）
gag_reflex: present_but_weak              # 舌咽反射存在但偏弱
bmi: 24
```

## allowed_variations（受控变量范围）

```yaml
age: [35, 50]
apfel_score: [3, 4]                        # 均为高危
vomiting_episodes: [1, 3]
nausea_score: [6, 9]
```

## critical_actions（关键处置，顺序敏感）

1. `assess_consciousness_and_airway_reflex`：首先评估意识与气道保护反射（未清醒+反射弱=误吸高危）
2. `position_for_aspiration_prevention`：安置体位——侧卧位/头偏向一侧（清醒患者可半坐卧位），防误吸
3. `prepare_suction_equipment`：床旁备好吸引装置并处于工作状态（关键防误吸准备）
4. `assess_purv_risk_factors`：评估 Apfel 风险因素（女性/非吸烟/PONV 史/术后阿片）确认高危
5. `maintain_oxygen_and_hydration`：维持吸氧，评估脱水/电解质（反复呕吐）
6. `report_anesthesiologist_for_antiemetic`：报告麻醉医师，按医嘱执行止吐药（药物种类与剂量属医师处方）
7. `monitor_antiemetic_response_and_adverse`：监测止吐药疗效与不良反应（如 QT 间期、锥体外系反应）
8. `reassess_nausea_vomiting`：再评价恶心呕吐程度、误吸征象（听诊肺部）、意识状态

## common_misconceptions（常见错误）

- `miss_aspiration_risk_in_drowsy_patient`：忽视嗜睡+反射弱患者的误吸风险，未做体位/吸引准备（最危险）
- `treat_purv_as_minor`：把 PONV 当小事，未评估反复呕吐的脱水/电解质后果
- `antiemetic_without_assessment`：未评估风险因素和意识状态就急于用药
- `miss_apfel_assessment`：不会用 Apfel 评分系统量化风险
- `supine_during_vomiting`：呕吐时让患者平卧（增加误吸）
- `escalation_delay`：反复呕吐未及时报告麻醉医师评估
- `self_prescribe_antiemetic_dose`：护士自行决定止吐药种类和剂量（越界处方）

## state_transitions（状态机）

```yaml
assess_then_position_then_suction_ready:    # 评估+侧卧位+吸引准备（正确防误吸）
  aspiration_safety: protected
  spo2_change: stable
  feedback: positive
  next_prompt: "误吸风险已控制。你如何评估她的 PONV 风险因素？"

correct_full_pipeline:                       # 评估+体位+吸引+Apfel 评估+报告+止吐药护理
  aspiration_safety: protected
  nausea_score: decrease_to_3
  vomiting_episodes: no_further
  consciousness: improve
  feedback: positive
  next_prompt: "恶心呕吐缓解。还需监测止吐药的哪些不良反应？"

position_but_miss_apfel_assessment:          # 体位正确但未做 Apfel 风险评估
  aspiration_safety: protected
  risk_stratification: incomplete
  feedback: partial
  next_prompt: "你做了防误吸体位，但还没有量化 PONV 风险。用哪个评分工具？她有几个风险因素？"

miss_aspiration_prevention:                  # 未做防误吸（最危险）
  aspiration_risk: high
  spo2_change: risk_decrease
  potential_complication: aspiration_pneumonitis
  feedback: deterioration
  next_prompt: "⚠️ 患者嗜睡、反射弱、反复呕吐，但你未安置侧卧位、未备吸引器。误吸风险极高。立即要做什么？"

antiemetic_without_position:                 # 急于用药但未先防误吸（顺序错误）
  aspiration_risk: elevated
  feedback: partial
  next_prompt: "⚠️ 在止吐药起效前，患者仍在呕吐。你忽略了哪项比用药更优先的处置？"

supine_during_vomiting:                      # 呕吐时平卧（错误体位）
  aspiration_event: high_risk
  feedback: deterioration
  next_prompt: "⚠️ 平卧位呕吐极易误吸。应立即采取什么体位？"

no_action:                                   # 未处置
  vomiting_episodes: increase
  aspiration_risk: critical
  dehydration_risk: elevated
  feedback: deterioration
  next_prompt: "患者持续呕吐，意识嗜睡，误吸和脱水风险进行性升高。立即要做什么？"
```

## rubric（评分量表）

```yaml
aspiration_prevention:
  kc: aspiration_prevention
  weight: 0.35
  criteria:
    1.0: 首先评估意识/反射，立即侧卧位或头偏一侧，床旁备吸引器（清醒者可半坐卧）
    0.5: 提及防误吸但措施不完整（如只侧卧未备吸引，或顺序不当）
    0.0: 未做防误吸或呕吐时仍平卧（高危误吸，可致吸入性肺炎）

risk_assessment:
  kc: ponv_risk_assessment
  weight: 0.25
  criteria:
    1.0: 用 Apfel 评分识别 4 个风险因素（女性/非吸烟/PONV 史/术后阿片），判定为高危
    0.5: 识别部分风险因素但未系统量化
    0.0: 未做风险因素评估

antiemetic_nursing:
  kc: antiemetic_nursing
  weight: 0.25
  criteria:
    1.0: 报告麻醉医师并按医嘱执行止吐药，监测疗效与不良反应（QT 间期/锥体外系）
    0.5: 提及止吐药但报告时机或监测不完整
    0.0: 自行决定止吐药种类剂量（越界处方）或未监测反应

reassessment_and_complication_monitoring:
  kc: response_reassessment
  weight: 0.15
  criteria:
    1.0: 再评价恶心呕吐程度、肺部听诊（误吸征象）、脱水/电解质、意识变化
    0.5: 提及复查但不完整
    0.0: 未做再评价，未监测反复呕吐的全身后果
```

## evidence_sources（依据来源）

> ⚠️ safety_critical=true：以下来源须标注版本年份/章节页码/核验人后才能用于教学输出（critical-content.md 规则3）。
> AI 合规审核已核医学逻辑与护理边界；**教材版次页码与指南年份待临床专家补核**，补核前不得从模型记忆补全具体剂量/阈值。

```yaml
- textbook: 《麻醉护理学》（刘保江、晁储璋，人民卫生出版社）第十二章 麻醉恢复室患者的护理（术后恶心呕吐）
  edition: ⚠️待补版次与年份
  page: ⚠️待补具体页码
  verified_by: ⚠️待临床专家核验
- guideline: 术后恶心呕吐防治专家共识（Apfel 风险评分与止吐药策略）
  year: ⚠️待补发布年份与适用状态
  verified_by: ⚠️待临床专家核验
- guideline: 麻醉后监测治疗专家共识（PACU PONV 管理）
  year: ⚠️待补发布年份与适用状态
  verified_by: ⚠️待临床专家核验
- sop: [本机构 PACU 术后恶心呕吐护理 SOP——若有，待补版本号]
- safety_note: |
    涉及止吐药（如昂丹司琼、甲氧氯普胺、氟哌利多、地塞米松等）的种类选择与剂量，
    属于麻醉医师处方范畴。护士不处方止吐药剂量，
    必须按麻醉医师医嘱执行并参照本机构 SOP，不从模型记忆生成。
    涉及误吸等急救处置参照本机构误吸应急预案 SOP。
```

## 教学要点

1. **Apfel 评分是 PONV 风险评估的核心工具**：4 个因素（女性、非吸烟、PONV/晕动史、术后阿片），≥3 个为高危——本病例 4 项全中
2. **误吸预防是 PONV 护理的第一要务**：尤其未完全清醒/反射弱者，必须侧卧位+头偏一侧+床旁备吸引器；清醒患者可半坐卧位
3. **PONV 非小事**：反复呕吐可致误吸、脱水、电解质紊乱、伤口裂开（尤腹部/颅脑手术）、延长住院——须系统监测并发症
4. **护士不处方止吐药剂量**：核心职责是评估风险、防误吸、按医嘱执行、监测疗效与不良反应（QT 间期、锥体外系反应）；高危患者应建议预防性多模式止吐策略
