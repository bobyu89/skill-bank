---
case_id: pacu-emergence-delay-001
title: PACU 苏醒延迟（老年患者全麻髋关节置换术后）
theme: 5_emergence_delay
difficulty: D3
case_purpose: training
safety_critical: true
version: 1.1
reviewed_by: "AI合规审核 2026-08-06（医学逻辑/护理边界/状态机/rubric 已核）；⚠️临床专家签字待补"
review_date: 2026-08-06
---

# 病例：PACU 苏醒延迟（老年患者全麻髋关节置换术后）

## 目标知识点（target_kcs）

- `emergence_delay_recognition`：掌握苏醒延迟的定义与识别（停麻醉药后 20-30 分钟仍未清醒或意识未恢复）
- `differential_diagnosis_delay`：掌握苏醒延迟的鉴别思路（麻醉药残余/低体温/低血糖/脑血管意外/CO₂蓄积/电解质紊乱）
- `reversible_cause_search`：掌握可逆原因的系统排查（测血糖/体温/血气/瞳孔/肌松/神经系统查体）

## 临床背景

75 岁老年患者全麻下髋关节置换术后入 PACU，停麻醉药后 40 分钟仍未清醒，对呼唤仅有轻微肢体反应。本病例是 D3 鉴别题——苏醒延迟是症状不是诊断，必须系统鉴别五大类原因（麻醉药残余、低体温、代谢紊乱如低血糖/电解质、呼吸衰竭致 CO₂蓄积、神经系统事件如脑血管意外）。各原因处置路径完全不同：盲目给拮抗药（如纳洛酮）会掩盖低血糖或脑事件等可治原因，甚至诱发躁动、呕吐、心血管意外。本病例训练护士的**识别 + 系统排查可逆原因 + 准备 + 报告**能力——护士不处方拮抗药，但必须能判断可能原因、针对性收集证据、把握报告时机。

## initial_state（初始呈现）

```yaml
patient_template: elderly_asa3
age: 75
gender: male
surgery: total_hip_replacement               # 全髋关节置换
anesthesia: general_anesthesia_with_et       # 气管插管全麻（已拔管）
anesthesia_agents: sevoflurane_remitentanil  # 七氟烷+瑞芬太尼
neuromuscular_blockade: rocuronium           # 术中罗库溴铵
reversal: neostigmine_administered           # 术毕已给新斯的明拮抗
time_since_end_anesthesia: 40_min            # 停药 40 分钟仍未清醒——苏醒延迟
consciousness: unresponsive_to_verbal        # 对呼唤无睁眼，疼痛有轻微肢体回缩
pupil: equal_and_reactive                    # 双侧等大等圆有反应（暂排除明显脑疝）
spo2: 95                                     # 面罩吸氧 5L/min
respiratory_rate: 10                         # 偏慢——警惕通气不足/CO₂蓄积
etco2: 55                                    # 升高——关键征象，提示 CO₂蓄积
heart_rate: 78
blood_pressure: 138_82
temperature: 35.4                            # 轻度低体温（待确认是否为核心温度）
blood_glucose: pending                       # 血糖待测——必须排查
abg: pending                                 # 动脉血气待测
tof_ratio: pending                           # TOF 待测（排除残余肌松）
pmh: hypertension_diabetes                   # 高血压、糖尿病史
bmi: 27
```

## allowed_variations（受控变量范围）

```yaml
age: [70, 82]
time_since_end_anesthesia: [30, 50]          # 均>20-30 分钟阈值，确保苏醒延迟成立
temperature: [34.8, 35.8]                    # 均提示低体温可能
etco2: [48, 58]                              # 均升高，提示 CO₂蓄积可能
respiratory_rate: [8, 12]
```

## critical_actions（关键处置，顺序敏感）

1. `recognize_emergence_delay`：识别停麻醉药后 40 分钟未清醒为苏醒延迟（>20-30 分钟阈值），判断为异常需排查
2. `secure_airway_and_ventilation`：保障气道与通气——确认气道通畅、面罩吸氧、监测 SpO₂/RR/ETCO₂，ETCO₂ 55 升高提示 CO₂蓄积，必要时准备辅助通气
3. `systematic_reversible_cause_search`：系统排查可逆原因，针对性收集证据：
   - **麻醉药残余**：核对麻醉记录（七氟烷/瑞芬太尼/罗库溴铵用量与时间、新斯的明拮抗情况）、查 TOF（排除残余肌松）
   - **低体温**：测核心温度（鼻咽/膀胱），<36℃ 可致苏醒延迟
   - **代谢紊乱**：**立即测指尖血糖**（排除低血糖——最易漏诊可逆原因）、查电解质（血钠/钙）
   - **CO₂蓄积/呼吸衰竭**：看 ETCO₂（已 55 升高）、送动脉血气（PaCO₂、pH、电解质）
   - **神经系统事件**：查瞳孔（大小/对称/反应）、肢体活动对称性、格拉斯哥昏迷评分（GCS）
4. `prepare_diagnostics_and_interventions`：准备进一步检查与处置——血气分析仪、血糖仪、TOF 监测、保暖设备、必要时影像/神经科会诊准备
5. `maintain_monitoring_and_safety`：持续监测 BP/HR/SpO₂/RR/ETCO₂/意识/瞳孔，侧卧位防误吸，床旁备吸引器
6. `report_anesthesiologist_with_findings`：用 SBAR 报告麻醉医师——苏醒延迟 + 已排查的发现（血糖/体温/血气/TOF/瞳孔），重点报告红旗征象
7. `execute_orders_and_reassess`：核对执行医嘱（如复温、纠正低血糖、调整通气——剂量与方案由医师决定），再评价意识、ETCO₂、血糖、体温
8. `recognize_escalation_red_flags`：识别立即升级指征（瞳孔不等大/不对称、肢体偏瘫、GCS 进行性下降、严重低血糖无法纠正、ETCO₂ 持续升高伴意识恶化——警惕脑血管意外）

## common_misconceptions（常见错误）

- `single_cause_assumption`：只想到单一原因（如只想到麻醉药残余），未系统鉴别五大类（D3 题核心错误）
- `give_reversal_before_workup`：未排查可逆原因就盲目给拮抗药（纳洛酮/氟马西尼）——掩盖低血糖/脑事件，且可诱发躁动、呕吐、心血管意外（最危险错误）
- `miss_blood_glucose`：未立即测血糖，漏诊低血糖这一最易纠正可逆原因
- `miss_hypothermia`：未测核心温度，漏诊低体温致苏醒延迟
- `ignore_etco2_elevation`：忽视 ETCO₂ 55 升高，漏诊 CO₂蓄积致意识抑制
- `miss_neurological_event`：未查瞳孔和肢体活动，漏诊脑血管意外（老年+大手术+可能的低血压时段为高危）
- `nurse_self_prescribe_reversal_dose`：护士自行决定拮抗药种类和剂量（越界处方）
- `delay_escalation_for_neuro_event`：发现瞳孔异常或肢体偏瘫未立即报告升级（延误脑事件诊断）
- `fail_to_check_anesthesia_record`：未核对麻醉记录，遗漏用药种类/总量/拮抗情况等关键信息

## state_transitions（状态机）

```yaml
systematic_workup_then_prepare_report:       # 系统排查五大原因 + 针对性准备 + SBAR 报告（正确）
  diagnostic_clarity: improving
  airway_ventilation_safety: secured
  feedback: positive
  next_prompt: "你系统排查了可逆原因（血糖/体温/血气/TOF/瞳孔）。等待麻醉医师期间，重点关注哪些红旗征象？"

correct_full_pipeline_with_reassessment:     # 排查 + 准备 + 报告 + 执行医嘱 + 再评价（完整正确）
  consciousness: gradual_improve
  etco2: decrease_with_ventilation_management
  blood_glucose: corrected_if_low
  temperature: increase_with_rewarming
  feedback: positive
  next_prompt: "意识逐渐恢复，ETCO₂ 回落。你如何判断患者是否真正脱离苏醒延迟风险？"

identify_reversible_cause_timely:            # 识别可逆原因（如低血糖/低体温/CO₂蓄积）并报告
  cause_identified: yes
  preparation: appropriate
  feedback: positive
  next_prompt: "你发现了一个可逆原因。这如何指导后续处置优先级？"

single_cause_assumption:                     # 只想到单一原因（如只想到麻醉药残余）
  diagnostic_completeness: poor
  missed_cause_risk: present
  feedback: partial
  next_prompt: "⚠️ 你只考虑到单一原因。苏醒延迟五大类原因是什么？哪些证据指向哪一个？你漏查了哪项？"

give_reversal_blindly:                       # 未排查可逆原因就盲目给拮抗药（最危险）
  underlying_cause: masked
  adverse_event_risk: elevated               # 可能诱发躁动、呕吐、心血管意外
  safety_event: potential_respiratory_depression_after_reversal_wears_off
  feedback: partial
  next_prompt: "⚠️ 你在未测血糖/体温/血气/瞳孔前就给了拮抗药。这可能掩盖什么危险？拮抗药失效后会发生什么？"

miss_blood_glucose:                          # 未测血糖（漏诊低血糖）
  hypoglycemia: undiagnosed
  neurological_injury_risk: elevated
  feedback: partial
  next_prompt: "⚠️ 你没有测血糖。低血糖是苏醒延迟最易漏诊且最易纠正的可逆原因。立即做什么？"

miss_neurological_red_flag:                  # 未查瞳孔/肢体，漏诊脑血管意外
  neuro_event: unrecognized
  consciousness: worsen
  pupil: asymmetric_change
  feedback: deterioration
  next_prompt: "⚠️ 你忽略了神经系统查体。患者瞳孔变化、肢体不对称——警惕脑血管意外。立即要做什么？"

no_action_or_delayed_report:                 # 未处置或延迟报告
  consciousness: worsen_to_coma
  etco2: increase_to_65
  respiratory_rate: decrease_to_7
  neurologic_or_metabolic_injury: progressing
  feedback: deterioration
  next_prompt: "⚠️ 患者意识进一步恶化，ETCO₂ 持续升高，呼吸抑制加重。这是医疗急症。立即做什么？"
```

## rubric（评分量表）

```yaml
emergence_delay_recognition:
  kc: emergence_delay_recognition
  weight: 0.20
  criteria:
    1.0: 识别停麻醉药后 40 分钟未清醒为苏醒延迟（>20-30 分钟阈值），判断需系统排查
    0.5: 识别意识未恢复但未明确苏醒延迟定义或阈值
    0.0: 未识别苏醒延迟或忽视意识异常

airway_and_ventilation_security:
  kc: emergence_delay_recognition
  weight: 0.20
  criteria:
    1.0: 保障气道通畅、维持吸氧、监测 SpO₂/RR/ETCO₂ 并识别 ETCO₂ 55 升高提示 CO₂蓄积，必要时准备辅助通气
    0.5: 维持吸氧但未识别 ETCO₂ 升高的意义或未准备通气支持
    0.0: 忽视通气安全或未监测 ETCO₂

systematic_differential_and_workup:
  kc: differential_diagnosis_delay
  weight: 0.35
  criteria:
    1.0: 系统鉴别五大类原因，针对性收集证据——测血糖、测核心温度、送血气、查 TOF、查瞳孔/肢体/GCS、核对麻醉记录（无遗漏）
    0.5: 鉴别不完整（如漏血糖/漏体温/漏神经系统查体）或证据收集不系统
    0.0: 只想到单一原因或完全未做系统排查（D3 题核心失败），或盲目给拮抗药未先排查

reversible_cause_search_and_escalation:
  kc: reversible_cause_search
  weight: 0.25
  criteria:
    1.0: 识别并优先纠正可逆原因（低血糖/低体温/CO₂蓄积/残余肌松），用 SBAR 及时报告，识别脑血管意外红旗征象并立即升级
    0.5: 报告但准备不全，或升级时机把握不清，或未明确红旗征象
    0.0: 自行决定拮抗药种类剂量（越界处方）、盲目给拮抗药、未识别神经系统红旗征象、延迟报告
```

## evidence_sources（依据来源）

> ⚠️ safety_critical=true：以下来源须标注版本年份/章节页码/核验人后才能用于教学输出（critical-content.md 规则3）。
> AI 合规审核已核医学逻辑与护理边界；**教材版次页码与指南年份待临床专家补核**，补核前不得从模型记忆补全具体剂量/阈值。

```yaml
- textbook: 《麻醉护理学》（刘保江、晁储璋，人民卫生出版社）第十二章 麻醉恢复室患者的护理（苏醒延迟）
  edition: ⚠️待补版次与年份
  page: ⚠️待补具体页码
  verified_by: ⚠️待临床专家核验
- textbook: 《麻醉学》苏醒延迟的鉴别诊断章节
  edition: ⚠️待补版次与年份
  page: ⚠️待补页码
  verified_by: ⚠️待临床专家核验
- textbook: 《老年麻醉学》老年患者术后苏醒延迟与神经系统并发症
  edition: ⚠️待补版次与年份
  page: ⚠️待补页码
  verified_by: ⚠️待临床专家核验
- guideline: 麻醉后监测治疗专家共识（PACU 苏醒延迟评估与管理）
  year: ⚠️待补发布年份与适用状态
  verified_by: ⚠️待临床专家核验
- guideline: 术后苏醒延迟鉴别诊断专家共识
  year: ⚠️待补发布年份与适用状态
  verified_by: ⚠️待临床专家核验
- sop: [本机构 PACU 苏醒延迟评估与处理 SOP——若有，待补版本号]
- safety_note: |
    涉及拮抗药（如纳洛酮拮抗阿片、氟马西尼拮抗苯二氮卓、新斯的明/舒更葡糖钠拮抗肌松）的种类选择与剂量，
    涉及纠正低血糖的葡萄糖剂量、复温方案、辅助通气参数设置，
    均属于麻醉医师处方范畴。护士不处方这些药物剂量与方案，
    必须按麻醉医师医嘱执行并参照本机构 SOP，不从模型记忆生成。
    涉及脑血管意外等急救处置参照本机构相应应急预案 SOP。
    拮抗药起效快但半衰期短于被拮抗药时，存在"再麻醉/再呼吸抑制"风险，须延长监测时间。
```

## 教学要点

1. **苏醒延迟是 D3 鉴别题**：停麻醉药后>20-30 分钟未清醒即属异常，必须系统鉴别五大类原因（麻醉药残余/低体温/代谢紊乱/CO₂蓄积/神经系统事件）——护士的核心能力是判断"最可能原因+排查什么+准备什么+何时报告"
2. **五大类原因排查口诀**：**A**nesthetic（麻醉药残余，查麻醉记录+TOF）、**T**emperature（低体温，测核心温度）、**M**etabolic（代谢，**立即测血糖**+电解质+血气）、**R**espiratory（CO₂蓄积，看 ETCO₂+血气）、**N**eurologic（神经系统，查瞳孔+肢体+GCS）——ATMRN
3. **低血糖是最易漏诊且最易纠正的可逆原因**：指尖血糖必须作为苏醒延迟排查的首项之一，糖尿病史/老年/长时间禁食患者尤须警惕
4. **盲目给拮抗药是危险错误**：未排查可逆原因就给纳洛酮/氟马西尼，会掩盖低血糖、脑事件；且拮抗药半衰期短于被拮抗药时可发生"再呼吸抑制"，须延长监测——护士不处方拮抗药剂量
5. **神经系统红旗征象绝不能漏**：瞳孔不等大/不对称、肢体偏瘫、GCS 进行性下降——任一出现立即报告升级，警惕脑血管意外（老年+大手术+可能的术中低血压时段为高危）
