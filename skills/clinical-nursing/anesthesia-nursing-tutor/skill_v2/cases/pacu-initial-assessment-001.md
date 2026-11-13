---
case_id: pacu-initial-assessment-001
title: PACU 初始评估与标准化接收
theme: 1_pacu_initial_assessment
difficulty: D1
case_purpose: training
safety_critical: false
version: 1.1
reviewed_by: "AI合规审核 2026-08-06（医学逻辑/护理边界/状态机/rubric 已核）；⚠️临床专家签字待补"
review_date: 2026-08-06
---

# 病例：PACU 初始评估与标准化接收

## 目标知识点（target_kcs）

- `pacu_handoff_reception`：掌握 PACU 标准化交接流程（SBAR 交接、麻醉记录核对、术中事件回顾）
- `immediate_assessment_abc`：掌握入室即刻 ABCDE 评估（气道/呼吸/循环/意识/暴露）
- `baseline_vitals_recording`：掌握基线生命体征建立与系统检查（生命体征、意识、体温、疼痛、引流管、静脉通路）

## 临床背景

患者全麻下腹部手术后由手术间转运入 PACU。这是 PACU 护理的**第一环节**——标准化接收与初始评估。本病例是 D1 识别题，训练麻醉护士在患者到达 PACU 时按规范完成：交接核对 → 即刻 ABCDE → 建立基线 → 系统全面检查。规范的初始评估是后续所有决策的基线参照，遗漏任一环节（如未测体温漏诊低体温、未核对引流管漏接、未建立基线生命体征无法判断后续变化）都会埋下隐患。

## initial_state（初始呈现）

```yaml
patient_template: middle_age_asa2
age: 58
gender: male
surgery: open_colectomy                      # 开腹结肠切除术
anesthesia: general_anesthesia_with_et       # 气管插管全麻
arrival_status: just_arrived                 # 刚转入 PACU
anesthesia_team_present: yes                 # 麻醉医师/巡回护士正在床旁交接
time_since_end_anesthesia: 10_min            # 术毕 10 分钟
consciousness: drowsy_arousable              # 嗜睡，呼之能应
airway: oral_endotracheal_tube_removed       # 已拔除气管导管
oxygen_delivery: face_mask_5L                # 面罩吸氧 5L/min（转运中持续）
respiratory_rate: 14
spo2: 96                                     # 面罩吸氧下
heart_rate: 88
blood_pressure: 125_78
temperature: pending                         # 体温待测——易遗漏环节
pain_score: pending                          # 疼痛待评
drain: abdominal_drain_in_situ               # 腹腔引流管在位
urinary_catheter: in_situ                    # 导尿管在位
iv_access: peripheral_iv_running             # 外周静脉通路在位，液体输注中
anesthesia_record: available                 # 麻醉记录单待核对
bmi: 26
```

## allowed_variations（受控变量范围）

```yaml
age: [45, 70]
surgery: [open_colectomy, open_appendectomy, laparoscopic_cholecystectomy]
spo2: [94, 98]                               # 吸氧下均氧合可接受
heart_rate: [75, 100]
blood_pressure_systolic: [110, 140]
consciousness: [drowsy_arousable, alert]
```

## critical_actions（关键处置，顺序敏感）

1. `receive_handoff_with_sbar`：用 SBAR 框架接收手术间交接（现况-背景-评估-建议），核对患者身份、手术、麻醉方式、过敏史
2. `immediate_abc_assessment`：入室即刻完成 ABCDE 评估——A 气道（通畅性/有无鼾声）、B 呼吸（RR/胸廓起伏/SpO₂）、C 循环（HR/BP/脉搏/皮肤灌注）、D 意识（镇静深度/瞳孔）、E 暴露（体温/皮肤/伤口）
3. `connect_monitors_and_baselines`：连接监护仪，建立基线生命体征（BP/HR/RR/SpO₂/ECG/体温），首次记录
4. `verify_airway_and_oxygen`：确认气道通畅与吸氧装置在位有效（面罩流量、管路无扭曲）
5. `check_anesthesia_record`：核对麻醉记录单——术中用药（肌松药/阿片/抗菌素/拮抗药）、出入量、失血量、输液输血、特殊事件（低血压/过敏/困难气道）
6. `systematic_check_lines_drains`：系统检查所有管路与引流——气管导管（已拔？）、静脉通路（通畅？液体？）、导尿管（尿量/颜色？）、引流管（量/色/通畅？）、伤口敷料（渗血？）
7. `assess_pain_and_temperature`：完成疼痛评分（NRS/FLACC）和体温测量（核心或体表），不可遗漏
8. `document_baseline_and_report_abnormalities`：完整记录初始评估结果；发现任何异常（SpO₂<94%、BP 异常、体温<36℃、引流量异常）立即报告麻醉医师并升级处置

## common_misconceptions（常见错误）

- `skip_handoff_verification`：跳过交接核对直接接手患者，未确认身份/手术/过敏/术中特殊事件
- `incomplete_abc`：ABC 评估不完整（如只看监护仪数字不看气道和胸廓起伏，漏诊气道梗阻）
- `miss_temperature`：初始评估未测体温，漏诊术后低体温（最常见遗漏环节之一）
- `miss_baseline_establishment`：未建立首次基线生命体征记录，后续无法判断变化趋势
- `ignore_drain_iv_check`：未系统检查引流管和静脉通路（漏接、扭曲、堵塞、液体走空）
- `no_pain_assessment`：未完成疼痛评分，漏诊镇痛不全
- `fail_to_review_anesthesia_record`：未核对麻醉记录单，遗漏术中肌松药/阿片/失血量等关键信息
- `miss_documentation`：评估了但不记录，缺乏基线参照

## state_transitions（状态机）

```yaml
standard_reception_with_full_systematic_check:    # SBAR 交接 + ABCDE + 基线 + 记录核对 + 系统检查（完整正确）
  baseline_established: yes
  handoff_verified: complete
  abnormality_detection: ready
  feedback: positive
  next_prompt: "你完成了标准化接收与系统评估。基线生命体征已建立。下一步你重点关注哪些指标的变化趋势？"

correct_abc_then_baselines_then_record_check:      # ABC + 基线 + 麻醉记录核对（正确核心流程）
  airway_respiratory_safety: confirmed
  baseline_vitals: recorded
  intraoperative_context: understood
  feedback: positive
  next_prompt: "即刻安全已确认，术中情况已掌握。你还需要完成哪些系统检查？（提示：管路/引流/体温/疼痛）"

incomplete_systematic_check:                      # 完成部分评估但漏了系统检查（如未测体温/未查引流）
  baseline_partial: yes
  risk: missed_abnormality
  feedback: partial
  next_prompt: "⚠️ 你做了 ABC 和生命体征，但体温/疼痛/引流管/静脉通路的系统检查完成了吗？哪一项最容易被遗漏？"

skip_handoff_directly_monitor:                    # 跳过交接核对，直接连监护仪
  identity_and_context: unverified
  intraoperative_events: unknown
  feedback: partial
  next_prompt: "⚠️ 你没有完成 SBAR 交接核对就开始监测。术中有哪些信息是你必须知道的？（过敏史/失血量/特殊事件）"

monitor_only_no_abc_examination:                  # 只看监护仪数字，不做床旁 ABC 评估
  airway_patency: unverified
  respiratory_effort: unassessed
  feedback: partial
  next_prompt: "⚠️ 监护仪显示生命体征，但你是否亲自评估了气道通畅性、胸廓起伏、皮肤灌注？为什么必须床旁看患者？"

no_baseline_documentation:                        # 评估了但未完整记录
  trend_monitoring: impossible
  feedback: partial
  next_prompt: "⚠️ 没有基线记录就无法判断后续变化。你现在需要记录哪些首次数据？"

no_action_or_rushed:                              # 未做系统评估或仓促应付
  baseline: absent
  abnormality_risk: high
  escalation_readiness: poor
  feedback: deterioration
  next_prompt: "⚠️ 患者刚入 PACU，你尚未完成标准化接收。漏评估意味着可能漏诊低氧/低血压/低体温/镇痛不全。立即按什么顺序做？"
```

## rubric（评分量表）

```yaml
handoff_and_abc:
  kc: immediate_assessment_abc
  weight: 0.35
  criteria:
    1.0: 完成 SBAR 交接核对，并立即做床旁 ABCDE 评估（气道/呼吸/循环/意识/暴露）
    0.5: 做了部分交接或部分 ABC 评估，但不完整或仅依赖监护仪数字
    0.0: 跳过交接核对或未做床旁 ABC 评估

baseline_vitals_and_monitoring:
  kc: baseline_vitals_recording
  weight: 0.30
  criteria:
    1.0: 连接监护仪建立完整基线（BP/HR/RR/SpO₂/ECG/体温）并首次记录
    0.5: 建立部分基线或未完整记录
    0.0: 未建立基线生命体征或未记录

systematic_check:
  kc: pacu_handoff_reception
  weight: 0.20
  criteria:
    1.0: 系统检查麻醉记录、所有管路（IV/导尿/引流）、伤口敷料、疼痛评分、体温——无遗漏
    0.5: 检查了部分项目但漏项（如漏体温/漏引流/漏疼痛评分）
    0.0: 未做系统检查，遗漏多项关键环节

documentation_and_abnormality_response:
  kc: baseline_vitals_recording
  weight: 0.15
  criteria:
    1.0: 完整记录初始评估，发现异常（SpO₂/BP/体温/引流异常）立即报告麻醉医师并升级
    0.5: 记录但不完整，或未明确异常的报告升级路径
    0.0: 未记录或发现异常未报告
```

## evidence_sources（依据来源）

```yaml
- textbook: 《麻醉护理学》第十二章 麻醉恢复室患者的护理（入室接收与初始评估）
- guideline: 麻醉后监测治疗专家共识（PACU 入室评估流程与监测项目）
- guideline: 围术期患者转运与交接专家共识（SBAR 交接框架）
- sop: [本机构 PACU 患者入室接收与初始评估 SOP——若有]
- safety_note: |
    初始评估中若发现异常（低氧血症/低血压/低体温/镇痛不全/引流量异常等），
    须按相应病例的处置路径升级（参照各专题病例）。
    本病例为 D1 识别题，safety_critical=false，
    但发现异常时须立即升级处置并报告麻醉医师，相应抢救用药参照本机构 SOP，不从模型记忆生成。
```

## 教学要点

1. **标准化接收是 PACU 护理的第一步**：SBAR 交接核对（身份/手术/麻醉/过敏/术中事件）必须在接收时完成，跳过交接会丢失关键背景信息
2. **ABCDE 评估永远是即刻动作**：患者一到，先做床旁 ABCDE——气道通畅？呼吸如何？循环灌注？意识水平？体温/皮肤/伤口——不能只盯监护仪数字
3. **基线生命体征必须完整且记录**：BP/HR/RR/SpO₂/ECG/体温六项缺一不可，体温是最常被遗漏的项目；没有基线就无法判断后续变化趋势
4. **系统检查不漏项**：麻醉记录核对、所有管路（IV/导尿/引流）通畅性、伤口敷料、疼痛评分——遗漏任一环节都可能埋下隐患（漏诊低体温、漏接引流、漏诊镇痛不全）
5. **发现异常立即升级**：D1 识别题的本质——识别 + 报告 + 升级处置路径；护士不处方，但必须敏锐识别、准确报告
