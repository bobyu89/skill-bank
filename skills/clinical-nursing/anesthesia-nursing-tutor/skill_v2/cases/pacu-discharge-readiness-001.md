---
case_id: pacu-discharge-readiness-001
title: PACU 离室评估（Aldrete 评分与离室标准）
theme: 12_discharge_readiness
difficulty: D3
case_purpose: training
safety_critical: false
version: 1.1
reviewed_by: "AI合规审核 2026-08-06（医学逻辑/护理边界/状态机/rubric 已核）；⚠️临床专家签字待补"
review_date: 2026-08-06
---

# 病例：PACU 离室评估（Aldrete 评分与离室标准）

## 目标知识点（target_kcs）

- `aldrete_scoring`：掌握 Aldrete 评分（活动/呼吸/循环/意识/SpO₂ 五项，每项 0-2 分，满分 10 分）
- `discharge_criteria_checklist`：掌握 PACU 离室标准的系统核查清单（生命体征/呼吸/意识/疼痛/PONV/体温/肌松/出血/引流）
- `discharge_clearance_judgment`：掌握离室判定的护理职责边界（护士完成评估并记录，离室决定须麻醉医师确认）

## 临床背景

患者腹部手术后入 PACU，停留 90 分钟，生命体征平稳，准备评估是否达到离室标准。本病例是 D3 综合评估题——离室评估不是单一指标达标，而是多维度系统核查（Aldrete 评分≥9 是核心，但还须确认无活动性出血、疼痛可控、无 PONV、肌松恢复、体温正常等）。漏查任一项都可能导致返室风险（如肌松残余致离室后呼吸抑制、活动性出血未识别致休克、体温过低致寒战）。本病例训练护士完成**完整离室评估清单 + Aldrete 评分 + 判断是否符合标准**的能力——护士完成评估并记录，但**离室决定须麻醉医师确认**，护士不单独决定离室。

## initial_state（初始呈现）

```yaml
patient_template: middle_age_asa2
age: 58
gender: male
surgery: open_colectomy                       # 开腹结肠切除术
anesthesia: general_anesthesia_with_et        # 气管插管全麻
neuromuscular_blockade: rocuronium            # 术中罗库溴铵
reversal: neostigmine_administered            # 术毕已给新斯的明拮抗
pca: intravenous_pca_running                  # 静脉 PCA 在运行
pacu_duration: 90_min                         # 已停留 90 分钟
consciousness: alert_and_oriented             # 清醒，定向力正常
activity: able_to_move_all_limbs              # 能主动活动四肢或抬腿——Aldrete 活动项满分
respiratory_rate: 14                          # 正常范围
spo2: 97                                      # 吸空气下——Aldrete SpO₂ 项满分
heart_rate: 82                                # 接近术前基础
blood_pressure: 128_76                        # 接近术前基础（术前 130_80）
core_temperature: 36.2                        # 核心温度正常（≥36℃）
pain_score_nrs: 3                             # NRS 3 分（≤4 达标）
ponv: none                                    # 无恶心呕吐
head_lift_5sec: able                          # 抬头能坚持 5 秒——肌松恢复
tof_ratio: 0.92                               # TOF 0.92（≥0.9 达标）
drain_output: minimal_stable                  # 引流量少且稳定——无活动性出血
wound_dressing: dry_intact                    # 伤口敷料干燥完整
urine_output: adequate                        # 尿量充足
hematocrit: stable                            # 血细胞比容稳定（无下降趋势）
bmi: 26
```

## allowed_variations（受控变量范围）

```yaml
age: [45, 75]
pacu_duration: [75, 120]
spo2: [95, 98]                                # 吸空气下均达标
pain_score_nrs: [2, 4]                        # 均≤4 达标
core_temperature: [36.0, 36.8]                # 均≥36℃ 达标
tof_ratio: [0.90, 0.95]                       # 均≥0.9 达标
```

## critical_actions（关键处置，顺序敏感）

1. `score_aldrete_systematically`：系统计算 Aldrete 评分（五项：活动/呼吸/循环/意识/SpO₂，每项 0-2 分，满分 10 分；≥9 分为离室核心标准之一）
2. `check_respiratory_recovery`：核查呼吸恢复——RR 正常范围、SpO₂ 吸空气下≥95%、无气道梗阻、呼吸做功正常
3. `check_neuromuscular_recovery`：核查肌松恢复——抬头试验（≥5 秒）、握力、TOF 比值（≥0.9）、舌咽反射（避免离室后呼吸抑制和误吸）
4. `check_hemodynamic_stability`：核查循环稳定——BP/HR 接近术前基础（降幅<20-30%）、无心律失常、皮肤灌注良好
5. `check_temperature_normal`：核查体温——核心温度≥36℃（避免离室后寒战、心血管事件）
6. `check_no_active_bleeding`：核查无活动性出血——引流液量与性质稳定、伤口敷料干燥、HCT 无下降趋势、腹围/术区无异常（红旗征象）
7. `check_pain_and_ponv_controlled`：核查疼痛可控（NRS≤4）和无 PONV——镇痛方案可持续（PCA/口服镇痛）、无恶心呕吐
8. `complete_discharge_checklist_and_document`：完成完整离室评估清单并记录——Aldrete 评分、各项核查结果、生命体征趋势、管路情况
9. `obtain_anesthesiologist_clearance`：报告麻醉医师，由麻醉医师确认离室决定并下达医嘱（护士不单独决定离室）；同时与接收病房/ICU 进行 SBAR 交接

## common_misconceptions（常见错误）

- `aldrete_only_ignore_other_criteria`：只看 Aldrete 评分≥9 就认为可离室，忽略其他离室标准（肌松/体温/PONV/出血/疼痛）——D3 题核心错误
- `miss_neuromuscular_check_at_discharge`：离室前未查抬头试验/TOF，漏诊残余肌松（离室后可致延迟性呼吸抑制）
- `miss_active_bleeding_check`：未核查引流量/伤口/HCT 趋势，漏诊活动性出血（离室后可致休克）
- `miss_temperature_check`：未测核心温度，漏诊低体温（离室后寒战、心血管事件）
- `nurse_solo_discharge_decision`：护士未报告麻醉医师就单独决定让患者离室（违反职责边界）
- `accept_pain_not_controlled`：NRS>4 仍安排离室（违反离室标准）
- `accept_ponv_not_controlled`：有明显 PONV 仍安排离室
- `ignore_baseline_comparison`：未与术前基础 BP/HR 比较，将相对异常误判为正常
- `incomplete_documentation`：离室评估未完整记录（Aldrete 评分、各项核查、生命体征趋势）

## state_transitions（状态机）

```yaml
full_discharge_checklist_then_physician_clearance:    # 完整清单核查 + Aldrete 评分 + 麻醉医师确认（完整正确）
  discharge_readiness: confirmed
  documentation: complete
  safety: assured
  feedback: positive
  next_prompt: "你完成了系统离室评估，所有标准达标，麻醉医师已确认。与接收病房交接时用 SBAR 报告哪些关键信息？"

correct_aldrete_plus_all_criteria:                    # Aldrete≥9 + 各项标准核查无遗漏（正确）
  discharge_readiness: confirmed
  missed_criterion: none
  feedback: positive
  next_prompt: "Aldrete 评分和各项离室标准都达标。离室前还需要麻醉医师做哪一步确认？"

identify_unmet_criterion_hold_discharge:              # 识别某项未达标（如肌松/体温/疼痛）并暂缓离室（关键正确决策）
  discharge_held: yes
  reason_documented: yes
  feedback: positive
  next_prompt: "你识别了一项未达标的标准并暂缓离室。这如何处理？应报告什么？"

aldrete_only_disregard_other_criteria:                # 只看 Aldrete≥9 就认为可离室（核心错误）
  missed_criteria: present
  discharge_safety: at_risk
  feedback: partial
  next_prompt: "⚠️ Aldrete 评分只是核心标准之一。你还需要核查哪些离室标准？（肌松/体温/PONV/出血/疼痛）"

miss_neuromuscular_check:                             # 离室前未查肌松恢复
  residual_block_risk: unrecognized
  post_discharge_respiratory_depression_risk: elevated
  feedback: partial
  next_prompt: "⚠️ 你没有核查肌松恢复（抬头/TOF）。残余肌松离室后会发生什么？应查什么？"

miss_bleeding_check:                                  # 未核查活动性出血（引流/HCT/伤口）
  active_bleeding: unrecognized
  post_discharge_shock_risk: elevated
  feedback: deterioration
  next_prompt: "⚠️ 你没有核查活动性出血红旗征象（引流量/伤口/HCT 趋势）。离室后发生出血会怎样？立即要做什么？"

nurse_solo_discharge_decision:                        # 护士单独决定离室（违反职责边界）
  scope_of_practice: violated
  clearance_process: bypassed
  feedback: partial
  next_prompt: "⚠️ 离室决定必须由麻醉医师确认。你作为护士的职责是什么？应如何报告？"

discharge_with_unmet_criterion:                       # 某项未达标仍安排离室（违反标准）
  discharge_safety: violated
  post_discharge_adverse_event_risk: elevated
  feedback: deterioration
  next_prompt: "⚠️ 患者某项离室标准未达标却安排离室。这可能导致什么返室风险？立即要做什么？"
```

## rubric（评分量表）

```yaml
aldrete_scoring:
  kc: aldrete_scoring
  weight: 0.25
  criteria:
    1.0: 正确系统计算 Aldrete 五项评分（活动/呼吸/循环/意识/SpO₂），判定≥9 分为核心标准
    0.5: 计算 Aldrete 但不完整或某项判读不准
    0.0: 不会计算 Aldrete 或评分方法错误

discharge_criteria_checklist:
  kc: discharge_criteria_checklist
  weight: 0.35
  criteria:
    1.0: 系统核查所有离室标准——呼吸/肌松（抬头+TOF≥0.9）/循环（与基础比较）/体温（≥36℃）/无活动性出血（引流+HCT+伤口）/疼痛（NRS≤4）/无PONV（无遗漏）
    0.5: 核查了部分标准但漏项（如漏肌松/漏体温/漏出血）
    0.0: 仅凭 Aldrete 评分就判断可离室，忽略其他标准（D3 题核心失败）

unmet_criterion_recognition:
  kc: discharge_criteria_checklist
  weight: 0.20
  criteria:
    1.0: 识别未达标项目（如肌松残余/低体温/疼痛未控/活动性出血）并暂缓离室、记录原因、报告处理
    0.5: 识别问题但处置不完整（如未暂缓离室或未记录）
    0.0: 未识别未达标项目或识别后仍安排离室（违反标准）

discharge_clearance_boundary:
  kc: discharge_clearance_judgment
  weight: 0.20
  criteria:
    1.0: 完成评估并记录，由麻醉医师确认离室决定并下达医嘱，与接收病房 SBAR 交接（不单独决定离室）
    0.5: 完成评估但未明确报告流程或交接不完整
    0.0: 护士单独决定离室（违反职责边界）或离室评估未记录
```

## evidence_sources（依据来源）

> 本病例为非 safety_critical，来源标注可适度放宽，但仍建议补充临界值标准的指南年份以便追溯（待临床专家补核）。

```yaml
- textbook: 《麻醉护理学》（刘保江、晁储璋，人民卫生出版社）第十二章 麻醉恢复室患者的护理（离室评估与离室标准）
  edition: ⚠️待补版次与年份
  page: ⚠️待补具体页码
  verified_by: ⚠️待临床专家核验
- textbook: 《麻醉学》PACU 离室标准章节
  edition: ⚠️待补版次与年份
  page: ⚠️待补页码
  verified_by: ⚠️待临床专家核验
- guideline: 麻醉后监测治疗专家共识（PACU 离室标准与 Aldrete 评分）
  year: ⚠️待补发布年份与适用状态
  verified_by: ⚠️待临床专家核验
- guideline: 残余神经肌肉阻滞防治专家共识（离室 TOF≥0.9 标准）
  year: ⚠️待补发布年份与适用状态
  verified_by: ⚠️待临床专家核验
- scale: Aldrete 评分（活动/呼吸/循环/意识/SpO₂ 五项，每项 0-2 分，≥9 分为离室核心标准）
- scale: PADSS 术后离室评分系统（Postanesthetic Discharge Scoring System，可作为补充）
- sop: [本机构 PACU 离室标准与离室流程 SOP——若有，待补版本号]
- safety_note: |
    PACU 离室评估涉及多项临床判断（肌松恢复/活动性出血/疼痛可控/体温正常等），
    离室决定须由麻醉医师确认并下达医嘱，护士不单独决定离室。
    各项标准的临界值（如 TOF≥0.9、核心温度≥36℃、NRS≤4、Aldrete≥9）参照本机构现行 SOP，
    不从模型记忆生成。
    若离室后发现异常（如返室后再发呼吸抑制、出血、低体温），按相应专题病例处置路径处理。
```

## 教学要点

1. **离室评估是 D3 系统综合题**：Aldrete 评分≥9 只是核心标准之一，必须系统核查所有离室标准（呼吸/肌松/循环/体温/无活动性出血/疼痛可控/无PONV）——任一漏查都可能导致返室风险
2. **Aldrete 五项评分是基础工具**：活动（0-2）、呼吸（0-2）、循环（0-2）、意识（0-2）、SpO₂（0-2），满分 10 分，≥9 分为离室核心标准之一——必须正确计算
3. **肌松恢复是硬红线**：抬头≥5 秒 + TOF≥0.9 才可离室——残余肌松离室后可致延迟性呼吸抑制和误吸，离室前必须核查
4. **活动性出血绝不能漏**：引流液量/性质、伤口敷料、HCT 动态趋势——任一异常即暂缓离室并报告（红旗征象）
5. **离室决定须麻醉医师确认**：护士完成评估并记录，但离室决定须麻醉医师确认并下达医嘱；护士不单独决定离室；同时与接收病房/ICU 进行 SBAR 交接，确保信息连续性
