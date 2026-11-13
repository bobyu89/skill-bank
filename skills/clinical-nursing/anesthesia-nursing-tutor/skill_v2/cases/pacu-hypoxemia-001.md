---
case_id: pacu-hypoxemia-001
title: PACU 低氧血症（鉴别低氧血症 vs 低通气）
theme: 3_hypoxemia_hypoventilation
difficulty: D2
case_purpose: training
safety_critical: true
version: 1.1
reviewed_by: "AI合规审核 2026-08-06（医学逻辑/护理边界/状态机/rubric 已核）；⚠️临床专家签字待补"
review_date: 2026-08-06
---

# 病例：PACU 低氧血症（鉴别低氧血症 vs 低通气）

## 目标知识点（target_kcs）

- `oxygenation_assessment`：评估氧合状态（SpO₂、PaO₂、吸氧浓度）
- `hypoventilation_recognition`：识别低通气（RR 慢、ETCO₂ 升高、胸廓起伏浅）
- `oxygen_therapy_principle`：理解给氧原理（低氧血症补氧，低通气需改善通气）
- `response_reassessment`：处置后复查 SpO₂/RR/ETCO₂/肺部体征、设定报告升级阈值的闭环再评价

## 临床背景

患者全麻下腹部手术后入 PACU。麻醉尚未完全清醒，发现 SpO₂ 偏低。本病例的核心训练目标是**鉴别低氧血症与低通气**——二者处置路径完全不同，混淆可延误病情。

- **低氧血症型**：SpO₂ 低 + RR 正常或偏快（呼吸代偿）+ ETCO₂ 正常或偏低 → 问题在氧合（V/Q 失调、肺不张、分流）
- **低通气型**：SpO₂ 低 + RR 慢 + ETCO₂ 升高 → 问题在通气（阿片抑制、肌松残余、气道梗阻），单纯补氧不能纠正根本问题

## initial_state（初始呈现）

```yaml
patient_template: middle_age_asa2
age: 58
gender: male
surgery: open_colectomy                 # 开腹结肠切除
anesthesia: general_anesthesia_with_et  # 气管插管全麻
consciousness: drowsy                   # 嗜睡，呼之能应
respiratory_rate: 20                    # 偏快（代偿性）
spo2: 90                                # 下降（面罩吸氧 5L/min）
etco2: 38                               # 正常上限（提示通气尚可）
fiO2: 0.40                              # 面罩 5L/min
lung_auscultation: bibasal_crackles     # 双肺底湿啰音——提示肺不张/肺泡液
bmi: 27
```

## allowed_variations（受控变量范围）

```yaml
age: [50, 68]
spo2: [88, 92]
respiratory_rate: [18, 24]              # 注意：本病例为低氧血症型，RR 偏快
etco2: [35, 42]                         # ETCO₂ 不高，区别于低通气型
```

## critical_actions（关键处置，顺序敏感）

1. `recognize_hypoxemia`：识别 SpO₂ 90% 为低氧血症（吸氧状态下仍偏低）
2. `differentiate_from_hypoventilation`：通过 RR 偏快、ETCO₂ 不高，鉴别为低氧血症而非低通气（关键决策点）
3. `increase_fio2`：在麻醉医师授权范围内提高吸氧浓度（如调整面罩流量、改用储氧面罩）
4. `assess_oxygenation_cause`：评估可能原因（听诊肺底湿啰音→提示肺不张/分泌物）
5. `encourage_early_mobility_and_breathing`：鼓励深呼吸、有效咳嗽、激励性肺量计训练、变换体位（清醒后）——改善肺不张
6. `report_anesthesiologist_if_persistent`：持续 SpO₂<92%（吸氧下）报告麻醉医师
7. `reassess_oxygenation`：再评价 SpO₂、RR、ETCO₂、肺部听诊

## common_misconceptions（常见错误）

- `confuse_hypoxemia_with_hypoventilation`：混淆二者，对 RR 慢+ETCO₂ 高者只补氧不改善通气（最常见、最危险错误）
- `treat_number_not_patient`：只看 SpO₂ 数字，不看 RR 和 ETCO₂ 整体判断
- `miss_etco2_check`：未测/未看 ETCO₂，丢失鉴别关键信息
- `oxygen_dose_without_assessment`：未评估呼吸做功和肺部体征就盲目调氧
- `delay_escalation`：吸氧下 SpO₂ 持续偏低却未及时报告

## state_transitions（状态机）

```yaml
correct_differentiation_then_oxygen:    # 正确鉴别为低氧血症 + 提高吸氧浓度
  spo2_change: increase_to_95
  respiratory_rate: decrease_to_16       # 代偿性 RR 回落
  consciousness: improve_to_alert
  feedback: positive
  next_prompt: "SpO₂ 改善到 95%。你接下来还要做什么评估和处置？"

correct_full_pipeline:                  # 鉴别 + 给氧 + 评估原因 + 鼓励呼吸训练
  spo2_change: increase_to_96
  respiratory_rate: decrease_to_15
  lung_auscultation: crackles_reduce
  consciousness: improve_to_alert
  feedback: positive
  next_prompt: "患者情况改善。离室前还需要确认哪些指标？"

oxygen_without_differentiation:         # 只调氧，未做低氧 vs 低通气的鉴别
  spo2_change: increase_to_93
  respiratory_rate: unchanged_20
  etco2: unchanged_38
  feedback: partial
  next_prompt: "SpO₂ 暂升到 93%，但你的处置是否基于正确的鉴别？请说明这是低氧血症还是低通气，依据是什么。"

incorrect_treat_as_hypoventilation:      # 误判为低通气（实际为低氧血症），错误处置
  spo2_change: fluctuate_90_93
  respiratory_rate: fluctuate
  feedback: deterioration               # safety_critical 病例：鉴别错误导致处置方向错误，延迟纠正肺不张/分流，标记恶化
  next_prompt: "⚠️ 你按低通气处理了（如开放气道/辅助通气/拮抗），但患者 RR 偏快、ETCO₂ 正常、肺底湿啰音，提示问题在氧合（V/Q 失调、肺不张、分流）而非通气。错误鉴别延误了什么？SpO₂ 为什么未根本改善？"

no_action:                              # 未处置
  spo2_change: decrease_to_85
  respiratory_rate: increase_to_24       # 代偿性进一步加快
  consciousness: worsen_to_restless      # 缺氧致烦躁
  feedback: deterioration
  next_prompt: "病情恶化，患者出现缺氧性烦躁。立即要做什么？"
```

## rubric（评分量表）

```yaml
key_sign_recognition:
  kc: oxygenation_assessment
  weight: 0.25
  criteria:
    1.0: 识别 SpO₂ 90%（吸氧下）为低氧血症，并结合肺部听诊判断可能原因
    0.5: 识别 SpO₂ 偏低但未结合其他体征综合分析
    0.0: 未识别低氧血症或忽视 SpO₂ 异常

differential_diagnosis:
  kc: hypoventilation_recognition
  weight: 0.35
  criteria:
    1.0: 明确鉴别为低氧血症（依据 RR 偏快+ETCO₂ 正常+肺底湿啰音），排除低通气
    0.5: 鉴别方向正确但依据不完整（如只提 RR 未提 ETCO₂）
    0.0: 误判为低通气或完全未做鉴别（混淆低氧血症与低通气）

nursing_action:
  kc: oxygen_therapy_principle
  weight: 0.25
  criteria:
    1.0: 基于正确鉴别，提高吸氧浓度 + 评估病因 + 鼓励呼吸训练
    0.5: 调氧正确但缺少病因评估或呼吸训练
    0.0: 处置与鉴别不符（如对低氧血症只改善通气不补氧）或无护理措施

reassessment_and_escalation:
  kc: response_reassessment
  weight: 0.15
  criteria:
    1.0: 复查 SpO₂/RR/ETCO₂/肺部听诊，持续偏低时报告麻醉医师
    0.5: 提及复查但不完整，或未明确报告时机
    0.0: 未做再评价，未设定报告升级阈值
```

## evidence_sources（依据来源）

> ⚠️ safety_critical=true：以下来源须标注版本年份/章节页码/核验人后才能用于教学输出（critical-content.md 规则3）。
> AI 合规审核已核医学逻辑与护理边界；**教材版次页码与指南年份待临床专家补核**，补核前不得从模型记忆补全具体剂量/阈值。

```yaml
- textbook: 《麻醉护理学》（刘保江、晁储璋，人民卫生出版社）第十二章 麻醉恢复室患者的护理（低氧血症章节）
  edition: ⚠️待补版次与年份
  page: ⚠️待补具体页码
  verified_by: ⚠️待临床专家核验
- textbook: 《麻醉学》围术期呼吸功能监测
  edition: ⚠️待补版次与年份
  page: ⚠️待补页码
  verified_by: ⚠️待临床专家核验
- guideline: 麻醉后监测治疗专家共识（PACU 低氧血症识别与处理）
  year: ⚠️待补发布年份与适用状态
  verified_by: ⚠️待临床专家核验
- sop: [本机构 PACU 呼吸监测与氧疗 SOP——若有，待补版本号]
- safety_note: |
    涉及紧急氧合处置（如储氧面罩、无创通气）的剂量与设备设置，
    必须参照本机构现行 SOP 与麻醉医师医嘱执行，不从模型记忆生成。
```

## 教学要点

1. **SpO₂ 低不是诊断，是征象**：必须结合 RR 和 ETCO₂ 鉴别是低氧血症还是低通气——这是 PACU 最常见的概念混淆
2. **鉴别口诀**：SpO₂ 低 + RR 高 + ETCO₂ 正常/低 = 低氧血症（问题在氧合）；SpO₂ 低 + RR 低 + ETCO₂ 高 = 低通气（问题在通气）
3. **处置路径不同**：低氧血症重在补氧+处理肺部原因；低通气重在改善通气（开放气道、拮抗、辅助通气）——对低通气只补氧会掩盖病情
4. **护士不处方、但须识别和报告**：护士的核心职责是准确鉴别、做好给氧准备、按医嘱执行并监测反应；持续不改善即报告麻醉医师
