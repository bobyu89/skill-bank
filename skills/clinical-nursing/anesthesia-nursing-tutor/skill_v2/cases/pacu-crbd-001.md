---
case_id: pacu-crbd-001
title: PACU 苏醒期躁动（小儿扁桃体切除术后）
theme: 7_crbd
difficulty: D2
case_purpose: training
safety_critical: false
version: 1.1
reviewed_by: "AI合规审核 2026-08-06（医学逻辑/护理边界/状态机/rubric 已核）；⚠️临床专家签字待补"
review_date: 2026-08-06
---

# 病例：PACU 苏醒期躁动（小儿扁桃体切除术后）

## 目标知识点（target_kcs）

- `crbd_recognition`：识别苏醒期躁动（CRBD），掌握 PAED 评分（小儿麻醉苏醒期谵妄评估量表）
- `pediatric_safety_protection`：实施儿科患者防坠床、防意外拔管、防外伤的护理保护措施
- `pain_vs_delirium_differentiation`：区分疼痛与 CRBD（对镇痛药反应不同，处置路径不同）
- `response_reassessment`：用药后再评价 PAED 评分、监测呼吸抑制/喉痉挛的闭环

## 临床背景

3 岁患儿在全麻下扁桃体切除术后入 PACU。苏醒期出现剧烈哭闹、躁动、不能安抚、试图拔除静脉导管，对父母呼唤无反应。本病例训练儿科 PACU 的两大核心能力：**CRBD 的识别与评分**（PAED 量表），以及**疼痛 vs CRBD 的鉴别**。CRBD 在儿科高发（尤其吸入麻醉药、五官科手术、学龄前儿童），与术后疼痛不同——CRBD 患儿对镇痛药反应差，盲目追加阿片类镇痛药不仅无效，反而增加呼吸抑制、呕吐、喉痉挛风险。安全重点是防坠床、防意外拔管（气道/静脉）、防外伤。

## initial_state（初始呈现）

```yaml
patient_template: pediatric_asa2
age: 3
gender: male
surgery: tonsillectomy_adenoidectomy         # 扁桃体+腺样体切除
anesthesia: general_anesthesia_with_sevoflurane  # 七氟烷吸入麻醉（CRBD 高危）
time_since_end_anesthesia: 12_min            # 术毕 12 分钟
consciousness: agitated inconsolable         # 躁动，不能安抚
behavior: crying_thrashing                   # 剧烈哭闹、扭动、翻滚
trying_to_pull_iv: yes                       # 试图拔除静脉导管——安全风险
eye_contact: none                            # 无眼神接触，对父母呼唤无反应
paed_score: 15                               # PAED 15 分（≥10 分提示苏醒期谵妄/CRBD）
spo2: 96                                     # 面罩吸氧下可接受（排除低氧致躁动）
respiratory_rate: 28                         # 哭闹致偏快
heart_rate: 138                              # 偏快（躁动/疼痛/哭闹）
blood_pressure: 108_65
airway: patent_with_oxygen_mask              # 气道通畅，面罩吸氧
pain_scale: pending                          # 小儿疼痛评分待评（FLACC）
iv_access: in_situ_at_risk                   # 静脉通路在位但有自拔风险
parent_present: yes                          # 家长在场（可参与安抚）
bmi: 16
```

## allowed_variations（受控变量范围）

```yaml
age: [2, 5]                                  # 学龄前儿童，CRBD 高发年龄段
paed_score: [12, 18]                         # 均≥10 分，确保 CRBD 成立
time_since_end_anesthesia: [8, 20]
spo2: [94, 98]                               # 氧合可接受，强调非低氧性躁动
heart_rate: [125, 150]
```

## critical_actions（关键处置，顺序敏感）

1. `ensure_safety_first`：首先保证安全——升床栏、专人看护/抱持、必要时软性约束、防坠床防拔管防外伤（最优先，躁动小儿坠床/自拔静脉/损伤风险高）
2. `exclude_reversible_causes`：逐一排查可逆原因（ABCDE）：
   - 气道/呼吸：SpO₂ 是否正常（已排除低氧）、有无气道梗阻/喉痉挛
   - 疼痛：用 FLACC 评分评估术区疼痛（扁桃体切除术后疼痛明确存在）
   - 低血糖/低体温/膀胱胀：核查（小儿尤须注意禁食后低血糖）
3. `assess_paed_score`：用 PAED 评分（小儿麻醉苏醒期谵妄评估量表）量化 CRBD 程度（≥10 分提示 CRBD）
4. `differentiate_crbd_vs_pain`：鉴别 CRBD 与疼痛——CRBD 特征：无目的性躁动、无视父母、对安抚无反应、对镇痛药反应差；疼痛特征：定向性哭闹、寻求安抚、术区明确、对镇痛药有反应
5. `non_pharmacological_comfort`：非药物干预优先——家长陪伴安抚、环境安静调暗、避免过度刺激、包裹保暖、轻柔约束（小儿尤其有效）
6. `report_anesthesiologist_for_pharmacologic_decision`：非药物干预无效且持续严重 CRBD → 报告麻醉医师评估用药（药物选择与剂量属医师处方，如丙泊酚/右美托咪定/阿片类——须先鉴别是 CRBD 还是疼痛再决定方向）
7. `continuous_monitoring`：持续监测 SpO₂、意识状态、呼吸（警惕用药后呼吸抑制、喉痉挛——扁桃体术后高危）
8. `reassess_after_intervention`：再评价 PAED 评分、安全状态、意识变化、SpO₂

## common_misconceptions（常见错误）

- `confuse_crbd_with_pain`：将 CRBD 误认为疼痛，盲目追加阿片类镇痛药（CRBD 对镇痛药反应差，反增呼吸抑制/呕吐/喉痉挛风险——最核心错误）
- `miss_safety_protection`：未升床栏/未专人看护/未约束，导致坠床或自拔静脉导管/气道（最严重后果）
- `use_paed_score_unknown`：不会用 PAED 评分量化 CRBD，仅凭主观判断
- `sedate_before_assessment`：未排查可逆原因（低氧/低血糖/气道梗阻）就直接用药
- `miss_reversible_causes`：忽视低氧、低血糖、喉痉挛、膀胱胀等可逆因素——扁桃体术后尤须警惕喉痉挛
- `exclude_parent`：将家长拒之门外，未利用家长安抚这一儿科最有效的非药物干预
- `overuse_restraints`：过度依赖物理约束而忽略环境调整和安抚
- `ignore_airway_risk_post_tonsillectomy`：扁桃体切除术后忽视气道出血和喉痉挛风险

## state_transitions（状态机）

```yaml
safety_first_then_assess_differentiate:     # 先安全保护 + 排查可逆原因 + PAED 评分（正确优先级）
  safety_event: none
  agitation_level: partial_reduce           # 安抚+安全后部分缓解
  feedback: positive
  next_prompt: "患儿安全得到保障。你下一步如何鉴别这是 CRBD 还是疼痛？用哪个评分工具？"

correct_differentiation_then_comfort:       # 鉴别 CRBD vs 疼痛 + 非药物安抚 + 必要时报告（完整正确）
  agitation_level: significantly_reduce
  behavior: consolable
  eye_contact: restored
  blood_pressure: decrease_to_normal
  feedback: positive
  next_prompt: "患儿逐渐可安抚，恢复眼神交流。还需要监测什么以警惕用药后的呼吸抑制和喉痉挛？"

correct_identify_crbd_not_pain:             # 正确识别为 CRBD（非疼痛），避免盲目加阿片
  diagnostic_accuracy: correct
  inappropriate_opioid_use_avoided: yes
  feedback: positive
  next_prompt: "你正确判断这是 CRBD 而非疼痛。这如何改变处置方向？应优先用什么干预？"

treat_as_pain_blindly_add_opioid:           # 将 CRBD 误认为疼痛，盲目追加阿片类（核心错误）
  agitation_level: persistent_or_worsen      # CRBD 对镇痛药反应差
  respiratory_depression_risk: elevated
  vomiting_laryngospasm_risk: elevated
  feedback: partial
  next_prompt: "⚠️ 你按疼痛处理追加了阿片药，但患儿躁动未缓解。CRBD 与疼痛对镇痛药反应有何不同？这增加了什么风险？"

miss_safety_protection:                     # 未做防坠床防拔管保护
  safety_event: fall_or_iv_pullout_risk
  agitation_level: unchanged_severe
  feedback: deterioration
  next_prompt: "⚠️ 患儿试图拔静脉导管，剧烈扭动，但床栏未升、未专人看护。立即要做什么？"

sedate_without_assessment:                  # 未排查可逆原因就直接用药
  spo2_change: risk_decrease                 # 可能掩盖低氧
  underlying_cause: masked
  feedback: partial
  next_prompt: "⚠️ 你在未排查低氧/低血糖/喉痉挛前就用了药。这可能掩盖什么危险？"

no_action:                                  # 未处置
  safety_event: high_risk_self_harm
  agitation_level: worsen
  feedback: deterioration
  next_prompt: "患儿躁动加剧，存在坠床和拔管风险。立即要做什么？"
```

## rubric（评分量表）

```yaml
safety_protection:
  kc: pediatric_safety_protection
  weight: 0.35
  criteria:
    1.0: 首先升床栏+专人看护/抱持+防拔管（静脉/气道），明确把儿科安全放第一位
    0.5: 提及安全但未作为首要措施，或措施不完整
    0.0: 未做安全保护（严重安全隐患，可直接导致坠床/拔管/外伤）

crbd_recognition_and_paed:
  kc: crbd_recognition
  weight: 0.25
  criteria:
    1.0: 用 PAED 评分（≥10 分）识别为 CRBD（苏醒期谵妄），并认识儿科吸入麻醉/五官科手术的高发性
    0.5: 识别躁动但未用 PAED 评分量化或未联系 CRBD 的高危因素
    0.0: 未识别 CRBD 性质或不会用 PAED 评分

pain_vs_crbd_differentiation:
  kc: pain_vs_delirium_differentiation
  weight: 0.25
  criteria:
    1.0: 系统鉴别 CRBD（无目的躁动、无视父母、对镇痛药反应差）vs 疼痛（定向哭闹、寻求安抚、术区明确），避免盲目加阿片
    0.5: 提及鉴别但依据不完整或方向模糊
    0.0: 将 CRBD 误认为疼痛盲目追加阿片类，或完全未做鉴别（核心错误）

nursing_intervention_and_escalation:
  kc: response_reassessment
  weight: 0.15
  criteria:
    1.0: 先用非药物安抚（家长陪伴、环境调整），无效时报告麻醉医师评估用药，并持续监测用药后呼吸抑制/喉痉挛
    0.5: 处置方向对但不完整（如缺再评价或报告时机不清）
    0.0: 直接自行决定用药（越界处方）或未监测用药后反应
```

## evidence_sources（依据来源）

```yaml
- textbook: 《麻醉护理学》第十二章 麻醉恢复室患者的护理（苏醒期躁动）
- textbook: 《小儿麻醉学》苏醒期谵妄与术后躁动章节
- guideline: 麻醉后监测治疗专家共识（PACU 苏醒期躁动管理）
- guideline: 小儿麻醉苏醒期谵妄防治专家共识（PAED 评分与干预策略）
- scale: PAED 评分（Pediatric Anesthesia Emergence Delirium Scale，≥10 分提示 CRBD）
- scale: FLACC 评分（小儿疼痛评估，Face/Legs/Activity/Cry/Consolability）
- sop: [本机构 PACU 儿科苏醒期躁动护理 SOP 与物理约束使用规范——若有]
- safety_note: |
    涉及镇静药/镇痛药（如丙泊酚、右美托咪定、芬太尼、舒芬太尼等）的种类与剂量选择，
    属于麻醉医师处方范畴。护士不处方这些药物剂量，
    必须按麻醉医师医嘱执行并参照本机构 SOP，不从模型记忆生成。
    小儿用药尤须按体重精确计算，参照本机构儿科用药 SOP。
    扁桃体切除术后须警惕气道出血和喉痉挛，相关急救参照本机构应急预案。
```

## 教学要点

1. **安全永远是第一位**：躁动小儿先升床栏、专人看护/抱持、防拔管（静脉/气道）、防外伤——ABC 之外，物理安全是儿科 PACU 躁动患者的第一要务
2. **CRBD 在儿科高发**：吸入麻醉药（七氟烷）、五官科手术（扁桃体/腺样体）、学龄前儿童（2-5 岁）是三大高危因素；PAED 评分≥10 分可量化诊断
3. **CRBD 与疼痛的鉴别是核心**：CRBD 特征是无目的性躁动、无视父母、对安抚和镇痛药反应差；疼痛是定向性哭闹、寻求安抚、术区明确、对镇痛药有反应——盲目追加阿片类不仅无效，反增呼吸抑制、呕吐、喉痉挛风险
4. **非药物干预优先**：家长陪伴安抚（儿科最有效）、环境安静调暗、避免过度刺激、保暖——这些在 CRBD 往往比药物更安全有效；用药决策属麻醉医师，护士须先鉴别 CRBD vs 疼痛再报告方向
5. **扁桃体术后特殊警示**：警惕气道出血（血液咽下或呛咳）、喉痉挛（高发）——躁动评估时必须排除这些气道原因，不可仅归为 CRBD
