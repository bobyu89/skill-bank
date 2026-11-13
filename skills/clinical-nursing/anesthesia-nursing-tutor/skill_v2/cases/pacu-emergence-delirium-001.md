---
case_id: pacu-emergence-delirium-001
title: PACU 苏醒期躁动/谵妄（老年患者）
theme: 6_emergence_delirium
difficulty: D2
case_purpose: training
safety_critical: false
version: 1.1
reviewed_by: "AI合规审核 2026-08-06（医学逻辑/护理边界/状态机/rubric 已核）；⚠️临床专家签字待补"
review_date: 2026-08-06
---

# 病例：PACU 苏醒期躁动/谵妄（老年患者）

## 目标知识点（target_kcs）

- `emergence_delirium_recognition`：识别苏醒期躁动/谵妄，掌握与疼痛、低氧、膀胱胀等的鉴别
- `safety_protection`：实施防坠床、防拔管、防外伤的护理保护措施
- `differentiation_from_pain`：区分躁动原因（疼痛 vs 真正谵妄 vs 低氧 vs 膀胱胀）
- `response_reassessment`：处置后复查躁动程度、安全状态、镇静后呼吸抑制的闭环再评价

## 临床背景

老年男性患者全麻下髋关节置换术后入 PACU。拔管后患者出现躁动、不配合指令、试图翻身拔除引流管。本病例核心训练目标是**苏醒期躁动原因的鉴别**——躁动是症状不是诊断，盲目使用镇静药会掩盖低氧等可治原因。老年患者尤须警惕术后谵妄。

## initial_state（初始呈现）

```yaml
patient_template: elderly_asa3
age: 76
gender: male
surgery: total_hip_replacement              # 全髋关节置换
anesthesia: general_anesthesia_with_et
consciousness: agitated_uncooperative       # 躁动、不配合指令
behavior: trying_to_turn_over               # 试图翻身、试图拔引流管
spo2: 95                                    # 面罩吸氧下可接受（排除低氧致躁动）
respiratory_rate: 18
heart_rate: 98
blood_pressure: 158/92                      # 偏高（躁动/疼痛所致）
pain_score: unable_to_assess                # 无法配合疼痛评分
drain: hip_surgical_drain_in_situ           # 髋部术区引流管在位
urinary_catheter: in_situ                   # 导尿管在位（排除膀胱胀）
time_since_end_anesthesia: 15_min           # 术毕 15 分钟
```

## allowed_variations（受控变量范围）

```yaml
age: [70, 82]
spo2: [93, 97]                              # 氧合可接受，强调非低氧性躁动
heart_rate: [92, 108]
blood_pressure_systolic: [150, 170]
```

## critical_actions（关键处置，顺序敏感）

1. `ensure_safety_first`：首先保证安全——升床栏、约束带（按需）、专人看护，防坠床防拔管（最优先）
2. `exclude_reversible_causes`：逐一排查可逆原因（ABCDE）：
   - 气道/呼吸：SpO₂ 是否正常（已排除低氧）
   - 膀胱胀：导尿管是否通畅（已排除）
   - 疼痛：术区疼痛评估（推论可能）
   - 低血压/低血糖：核查生命体征与血糖
3. `differentiate_delirium_vs_pain`：鉴别真正谵妄 vs 疼痛所致躁动（老年人术后谵妄 vs 切口痛）
4. `use_reorientation_and_comfort`：非药物干预优先——呼唤姓名、解释身处 PACU、家属陪伴、调整体位、保暖
5. `report_anesthesiologist_for_pharmacologic_decision`：非药物干预无效且持续躁动 → 报告麻醉医师评估用药（药物选择与剂量属医师处方）
6. `continuous_monitoring`：持续监测 SpO₂、意识状态、生命体征，警惕镇静后呼吸抑制
7. `reassess_after_intervention`：再评价躁动程度、安全状态、意识变化

## common_misconceptions（常见错误）

- `sedate_before_assessment`：未排查可逆原因就直接用镇静药（掩盖低氧、低血糖等可治原因）
- `confuse_pain_with_delirium`：将疼痛性躁动误认为谵妄，或反之（处置完全不同）
- `miss_safety_protection`：未升床栏/未约束，导致坠床或自拔管（最严重后果）
- `ignore_reversible_causes`：忽视膀胱胀、低氧、低血糖、疼痛等可逆因素
- `overuse_restraints`：过度依赖物理约束而忽略非药物安抚和环境调整
- `elderly_delirium_under_recognition`：未认识到老年患者术后谵妄的高发性与不良预后

## state_transitions（状态机）

```yaml
safety_first_then_assess_causes:        # 先安全保护 + 排查可逆原因（正确优先级）
  safety_event: none
  agitation_level: partial_reduce       # 安抚+安全后部分缓解
  feedback: positive
  next_prompt: "患者安全得到保障。你下一步如何鉴别这是疼痛还是谵妄？"

correct_differentiation_then_comfort:   # 鉴别 + 非药物安抚 + 必要时报告（完整正确）
  agitation_level: significantly_reduce
  behavior: cooperative
  blood_pressure: decrease_to_140_85
  feedback: positive
  next_prompt: "患者逐渐配合。还需要监测什么以警惕镇静后的呼吸抑制？"

sedate_without_excluding_causes:        # 未排查原因直接上镇静药（最危险错误）
  spo2_change: risk_decrease            # 镇静掩盖低氧
  underlying_cause: masked
  feedback: partial
  next_prompt: "⚠️ 你在未排查可逆原因（低氧/低血糖/膀胱胀）前就用了镇静药。这可能掩盖什么危险？"

miss_safety_protection:                 # 未做防坠床防拔管保护
  safety_event: fall_or_extubation_risk
  agitation_level: unchanged_severe
  feedback: deterioration
  next_prompt: "⚠️ 患者试图翻身拔管，但床栏未升、未约束。立即要做什么？"

confuse_pain_as_delirium:               # 把疼痛性躁动误判为谵妄，未给镇痛
  agitation_level: persistent
  blood_pressure: persist_elevated
  feedback: partial
  next_prompt: "你判断为谵妄，但患者 HR、BP 偏高、刚做髋部大手术。还可能是哪类原因？"

no_action:                              # 未处置
  safety_event: high_risk_self_harm
  agitation_level: worsen
  feedback: deterioration
  next_prompt: "患者躁动加剧，存在坠床和拔管风险。立即要做什么？"
```

## rubric（评分量表）

```yaml
safety_protection:
  kc: safety_protection
  weight: 0.35
  criteria:
    1.0: 首先升床栏+专人看护/约束+防拔管，明确把安全放第一位
    0.5: 提及安全但未作为首要措施，或措施不完整
    0.0: 未做安全保护（严重安全隐患，可直接导致坠床/拔管）

cause_differentiation:
  kc: differentiation_from_pain
  weight: 0.30
  criteria:
    1.0: 系统排查可逆原因（低氧/膀胱胀/低血糖/疼痛）并鉴别谵妄 vs 疼痛
    0.5: 提及部分原因但鉴别不系统
    0.0: 未排查可逆原因，直接归为单一原因（如直接判断为谵妄或直接判断为疼痛）

delirium_recognition:
  kc: emergence_delirium_recognition
  weight: 0.20
  criteria:
    1.0: 识别为苏醒期躁动，并认识到老年患者术后谵妄的可能性
    0.5: 识别躁动但未联系到老年术后谵妄的高危性
    0.0: 未识别躁动性质或误判意识状态

nursing_intervention_and_escalation:
  kc: response_reassessment
  weight: 0.15
  criteria:
    1.0: 先用非药物安抚，无效时报告麻醉医师评估用药，并持续监测镇静后呼吸
    0.5: 处置方向对但不完整（如缺再评价或报告时机不清）
    0.0: 直接自行决定用镇静药（越界处方）或未监测镇静后反应
```

## evidence_sources（依据来源）

```yaml
- textbook: 《麻醉护理学》第十二章 麻醉恢复室患者的护理（苏醒期躁动与谵妄）
- textbook: 《老年麻醉学》术后谵妄章节
- guideline: 麻醉后监测治疗专家共识（苏醒期躁动管理）
- guideline: 术后谵妄防治专家共识（老年患者）
- sop: [本机构 PACU 苏醒期躁动护理 SOP 与物理约束使用规范——若有]
- safety_note: |
    涉及镇静药/镇痛药（如丙泊酚、右美托咪定、芬太尼等）的种类与剂量选择，
    属于麻醉医师处方范畴。护士不处方这些药物剂量，
    必须按麻醉医师医嘱执行并参照本机构 SOP，不从模型记忆生成。
```

## 教学要点

1. **安全永远是第一位**：躁动患者先升床栏、防拔管、专人看护——ABC 之外，物理安全是 PACU 躁动患者的第一要务
2. **躁动是症状不是诊断**：必须系统排查可逆原因（低氧、低血糖、膀胱胀、疼痛、血管栓塞），不可盲目使用镇静药掩盖
3. **谵妄 vs 疼痛的鉴别**：疼痛性躁动常伴 HR/BP 升高、术区明确；谵妄多见老年人、意识波动、注意力障碍、感知异常
4. **老年患者特殊警示**：术后谵妄高发且与不良预后相关；非药物干预（再定向、环境、家属）优先于药物；护士不处方镇静/镇痛药剂量
