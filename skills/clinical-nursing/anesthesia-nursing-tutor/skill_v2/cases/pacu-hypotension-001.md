---
case_id: pacu-hypotension-001
title: PACU 低血压（鉴别诊断）
theme: 11_hemodynamic_instability
difficulty: D3
case_purpose: training
safety_critical: true
version: 1.1
reviewed_by: "AI合规审核 2026-08-06（医学逻辑/护理边界/状态机/rubric 已核）；⚠️临床专家签字待补"
review_date: 2026-08-06
---

# 病例：PACU 低血压（鉴别诊断）

## 目标知识点（target_kcs）

- `hypotension_differential`：掌握 PACU 低血压的鉴别思路（麻醉残余/容量不足/术后出血/心功能不全/过敏）
- `volume_assessment`：掌握容量状态评估（皮肤温度/毛细血管充盈/尿量/HR/脉压差/CVP 如有）
- `escalation_threshold`：掌握报告升级阈值（识别失代偿征象、术后出血红旗征、何时立即报告）

## 临床背景

老年高血压患者全麻下结肠切除术后入 PACU，血压 85/50 mmHg（术前基础 140/80），HR 102 次/分。本病例是 D3 鉴别题——PACU 低血压的四大常见原因（麻醉残余、容量不足、术后出血、心功能不全）处置路径完全不同，混淆会致命。本病例训练护士的**鉴别判断 + 准备 + 报告时机**能力——护士不决定补液量或升压药种类，但必须能判断可能原因、准备相应措施、把握报告升级时机。

## initial_state（初始呈现）

```yaml
patient_template: elderly_cardiovascular_asa3
age: 72
gender: male
surgery: open_colectomy                    # 开腹结肠切除
anesthesia: general_anesthesia_with_et
baseline_bp: 140_80                        # 术前基础血压
hypertension_history: yes                  # 长期高血压病史（基础血压偏高）
antihypertensives_held: yes                # 术晨降压药未服
consciousness: drowsy_but_arousable
blood_pressure: 85_50                      # 当前 BP（较基础降幅大）
heart_rate: 102                            # 心率增快——提示代偿/容量不足
respiratory_rate: 16
spo2: 96                                   # 面罩吸氧 5L/min
skin: cool_pale                            # 皮肤湿冷苍白——外周灌注差
capillary_refill: 3_sec                    # 毛细血管充盈延长
urine_output: low_since_arrival            # 入室以来尿量少
drain_output: increased                    # 术区引流液量偏多——红旗征象
hematocrit: pending                        # 血细胞比待复查
bmi: 26
```

## allowed_variations（受控变量范围）

```yaml
age: [68, 78]
blood_pressure_systolic: [80, 92]          # 均为显著低血压
heart_rate: [98, 112]                      # 均增快
drain_output: [moderately_increased, markedly_increased]
```

## critical_actions（关键处置，顺序敏感）

1. `recognize_significant_hypotension`：识别 85/50 较基础（140/80）降幅>30% 为显著低血压，HR 代偿性增快
2. `rapid_abc_assessment`：快速 ABCDE 评估——气道、呼吸、循环（脉搏强弱、皮肤温度颜色、毛细血管充盈）
3. `differential_assessment`：系统鉴别四大原因，针对性收集证据：
   - **麻醉残余**：意识、瞳孔、麻醉深度、肌松（本例意识嗜睡可能部分相关）
   - **容量不足**：皮肤温度、毛细血管充盈、尿量、HR、脉压差
   - **术后出血**：引流液量与性质、腹围/伤口、HCT 复查、血红蛋白动态——**重点排查（红旗征象）**
   - **心功能不全**：心律、双肺啰音、颈静脉怒张、胸痛、心电图
4. `prepare_interventions_per_likely_cause`：按可能原因准备——液体加温、晶体液/血制品准备（按医嘱）、升压药泵准备、心电图/血气/HCT 送检
5. `maintain_oxygen_and_monitor`：维持吸氧，持续监测 BP/HR/SpO₂/尿量/意识，开放/确认静脉通路通畅
6. `report_anesthesiologist_with_sbfr`：用 SBAR 报告麻醉医师（现况-背景-评估-建议），重点报告红旗征象
7. `execute_orders_and_reassess`：核对执行医嘱（补液/血制品/升压药——剂量由医师决定），再评价 BP、HR、尿量、皮肤灌注、意识
8. `recognize_escalation_red_flags`：识别立即升级指征（持续低血压、HR 持续升高、引流量持续增加、意识恶化、少尿无尿）

## common_misconceptions（常见错误）

- `single_cause_tunnel_vision`：只想到单一原因（如只想到容量不足而忽略术后出血），未系统鉴别（D3 题核心错误）
- `miss_postoperative_bleeding_red_flag`：忽视术区引流量增加这一术后出血红旗征象（最危险遗漏）
- `baseline_ignored`：忽视"术前 140/80，长期高血压"——对高血压患者 85/50 是相对低血压更严重
- `self_prescribe_fluid_or_vasopressor`：护士自行决定补液种类/量或升压药种类（越界处方）
- `treat_number_not_perfusion`：只盯 BP 数字，不评估外周灌注（皮肤温度、毛细血管充盈、尿量、意识）
- `escalation_delay`：识别显著低血压/红旗征象后未立即报告
- `miss_cardiac_origin`：忽略老年+心血管病史患者的心源性低血压可能（不查肺啰音、心电图）

## state_transitions（状态机）

```yaml
systematic_differential_then_prepare_report:    # 系统鉴别 + 针对性准备 + SBAR 报告（正确）
  diagnostic_clarity: improving
  hemodynamic_safety: monitored
  feedback: positive
  next_prompt: "你系统鉴别了四大原因并准备到位。等待麻醉医师期间，重点关注哪些红旗征象？"

correct_identify_bleeding_risk_flag:            # 识别术后出血红旗征象并立即报告（关键正确决策）
  bleeding_recognition: timely
  preparation: blood_products_ready
  feedback: positive
  next_prompt: "你抓住了术后出血红旗征象（引流量增加）。这如何改变处置优先级？"

full_pipeline_with_reassessment:                # 鉴别 + 准备 + 报告 + 执行医嘱 + 再评价（完整正确）
  blood_pressure: improve_with_intervention
  heart_rate: decrease
  urine_output: improve
  skin: warm_dry
  feedback: positive
  next_prompt: "循环改善。你如何判断患者是否稳定到可以转出 PACU？"

single_cause_assumption:                        # 只想到单一原因（如只想到麻醉残余或只想到容量）
  diagnostic_completeness: poor
  treatment_mismatch_risk: present
  feedback: partial
  next_prompt: "⚠️ 你只考虑到单一原因。PACU 低血压四大原因是什么？哪些证据指向哪一个？"

miss_bleeding_red_flag:                         # 忽视术后出血红旗征象（引流液增加）
  bleeding_recognition: delayed
  hemodynamic_status: worsen
  blood_pressure: further_decrease_to_75
  heart_rate: increase_to_120
  feedback: deterioration
  next_prompt: "⚠️ 你忽略了术区引流量增加这一术后出血红旗征象。患者 BP 进一步下降、HR 升高。立即要做什么？"

self_prescribe_fluid_dose:                      # 护士自行决定补液量/种类（越界处方）
  scope_of_practice: violated
  feedback: partial
  next_prompt: "⚠️ 补液种类和量、升压药种类属于麻醉医师处方。你的职责是什么？应如何报告？"

no_action_or_delayed_report:                    # 未处置或延迟报告
  blood_pressure: decrease_to_72_45
  heart_rate: increase_to_125
  consciousness: worsen_to_confused
  urine_output: anuric
  shock_progression: present
  feedback: deterioration
  next_prompt: "⚠️ 患者进展为休克（低血压+心率快+少尿+意识改变）。这是医疗急症。立即做什么？"
```

## rubric（评分量表）

```yaml
hypotension_recognition_and_baseline:
  kc: hypotension_differential
  weight: 0.25
  criteria:
    1.0: 识别 85/50 较基础（140/80）降幅>30% 为显著低血压，结合长期高血压史判断为相对严重低血压
    0.5: 识别低血压但未联系术前基础或高血压史
    0.0: 未识别低血压的临床意义，或忽视基础血压比较

differential_systematic:
  kc: hypotension_differential
  weight: 0.30
  criteria:
    1.0: 系统鉴别四大原因（麻醉残余/容量不足/术后出血/心功能），针对性收集证据并识别红旗征象
    0.5: 鉴别不完整（如遗漏术后出血或心源性）或证据收集不系统
    0.0: 只想到单一原因或完全未做鉴别（D3 题核心失败）

volume_and_perfusion_assessment:
  kc: volume_assessment
  weight: 0.20
  criteria:
    1.0: 评估皮肤温度/毛细血管充盈/尿量/HR/脉压差等容量与灌注指标
    0.5: 评估部分指标但不完整
    0.0: 未评估容量状态，只盯 BP 数字

escalation_and_preparation:
  kc: escalation_threshold
  weight: 0.25
  criteria:
    1.0: 用 SBAR 及时报告麻醉医师，按可能原因准备液体/血制品/升压药泵，识别立即升级红旗征象
    0.5: 报告但准备不全，或升级时机把握不清
    0.0: 延迟报告、自行决定补液量或升压药种类（越界处方）、未识别红旗征象
```

## evidence_sources（依据来源）

> ⚠️ safety_critical=true：以下来源须标注版本年份/章节页码/核验人后才能用于教学输出（critical-content.md 规则3）。
> AI 合规审核已核医学逻辑与护理边界；**教材版次页码与指南年份待临床专家补核**，补核前不得从模型记忆补全具体剂量/阈值。

```yaml
- textbook: 《麻醉护理学》（刘保江、晁储璋，人民卫生出版社）第十二章 麻醉恢复室患者的护理（循环并发症：低血压）
  edition: ⚠️待补版次与年份
  page: ⚠️待补具体页码
  verified_by: ⚠️待临床专家核验
- textbook: 《麻醉学》围术期循环功能监测与评估
  edition: ⚠️待补版次与年份
  page: ⚠️待补页码
  verified_by: ⚠️待临床专家核验
- guideline: 麻醉后监测治疗专家共识（PACU 血流动力学不稳定管理）
  year: ⚠️待补发布年份与适用状态
  verified_by: ⚠️待临床专家核验
- guideline: 术后出血识别与处理专家共识（红旗征象）
  year: ⚠️待补发布年份与适用状态
  verified_by: ⚠️待临床专家核验
- sop: [本机构 PACU 血流动力学不稳定处理 SOP 与 SBAR 交接规范——若有，待补版本号]
- safety_note: |
    涉及补液种类与量、血制品输注、血管活性药（去甲肾上腺素/肾上腺素/多巴胺等）种类与剂量、
    抢救药物剂量，均属于麻醉医师处方范畴。护士不处方这些内容，
    必须按麻醉医师医嘱执行并参照本机构 SOP，不从模型记忆生成。
    涉及输血、过敏性休克、术后大出血等急救处置参照本机构相应应急预案 SOP。
```

## 教学要点

1. **PACU 低血压是 D3 鉴别题**：四大原因（麻醉残余/容量不足/术后出血/心功能不全）处置完全不同，必须系统鉴别而非单一归因——护士的核心能力是判断"最可能原因+准备什么+何时报告"
2. **基础血压是关键参照**：长期高血压患者 85/50 是相对低血压更严重；降幅>30% 基础值即显著——必须结合病史判断
3. **术后出血红旗征象绝不能漏**：术区引流量/性质变化、腹围增加、HCT 动态下降、持续心动过速——任一出现即立即报告，延误可致命
4. **评估灌注而非只看数字**：皮肤温度、毛细血管充盈、尿量、意识是循环有效性的真实指标；护士不处方补液/升压药，但须准确评估、准备到位、用 SBAR 报告并把握升级时机
