# 病例骨架 Schema 与状态机规范（替代自由生成）

> **本文件取代旧版"动态情景题生成引擎"的自由生成模式。** 完全依靠大模型现场生成病例会出现：生命体征不符合生理逻辑、药物与病情不一致、一次塞入过多问题、标准答案漂移、难度不可比较、无法用于规范研究。本版改为**专家审核病例骨架 + 受控变量替换 + 状态机演变**。

---

## 一、大模型职责边界（严格划分）

### ✅ 大模型负责

- 将结构化病例骨架转化为自然语言叙述
- 理解学习者回答（自然语言→评分维度匹配）
- 匹配病例动作（学习者处置→状态转移触发）
- 生成个性化提示（按 hint-ladder 分级）
- 提供基于证据的解释（从 knowledge_sources 检索）

### ❌ 大模型不负责

- 自由决定患者生理变化（由状态机 state_transitions 决定）
- 自由生成抢救剂量（必须从 critical-content 来源检索）
- 自由设计关键处置流程（必须对照 critical_actions）
- 自行修改专家审核的标准答案

---

## 二、病例骨架 YAML Schema

每个 `cases/*.md` 文件包含一个病例，结构如下：

```yaml
case_id: pacu-airway-obstruction-001
title: PACU 上呼吸道梗阻
theme: 2_upper_airway_obstruction          # 对应 curriculum-map 主题编号
difficulty: D2                             # D1/D2/D3/D4
target_kcs:                                # 本病例训练的知识点
  - upper_airway_obstruction
  - oxygenation_assessment
  - airway_priority
safety_critical: false                     # 是否涉及 critical-content 清单

initial_state:                             # 患者初始呈现
  patient_template: elderly_cardiopulmonary  # 引用患者池骨架
  consciousness: drowsy
  respiratory_rate: 12
  spo2: 88
  airway_sound: snoring
  etco2: 48
  surgery: laparoscopic_cholecystectomy
  anesthesia: general_anesthesia

allowed_variations:                        # 受控变量替换范围（保证难度可比）
  age: [65, 78]
  bmi: [26, 34]
  spo2: [84, 91]
  rr: [10, 14]

critical_actions:                          # 关键处置（顺序敏感）
  - assess_airway_patency                  # 1. 评估气道通畅性
  - perform_airway_opening_maneuver         # 2. 开放气道的护理手法
  - call_for_support                       # 3. 呼叫支持（报告升级）
  - reassess_oxygenation_and_ventilation   # 4. 再评价氧合与通气

common_misconceptions:                     # 本病例常见的错误类型
  - oxygen_before_airway                   # 先给氧而非先开放气道
  - miss_reassessment                      # 漏做再评价

state_transitions:                         # 状态机：处置→生理变化
  airway_opened:                           # 学习者执行了开放气道
    spo2_change: increase_to_95
    snoring: resolve
    consciousness: improve_to_alert
    feedback: positive

  oxygen_only:                             # 学习者只给氧未开放气道
    spo2_change: temporary_increase_to_92
    snoring: persistent
    consciousness: unchanged
    feedback: partial                      # 提示：暂时改善但未解决根本问题

  no_action:                               # 学习者未处置
    spo2_change: decrease_to_82
    consciousness: worsen_to_unresponsive
    feedback: deterioration                # 病情恶化提示

rubric:                                    # 评分量表（详见 scoring-rubrics.md）
  key_sign_recognition:
    kc: upper_airway_obstruction
    weight: 0.30
  priority_judgment:
    kc: airway_priority
    weight: 0.25
  nursing_action:
    kc: airway_intervention
    weight: 0.25
  reassessment:
    kc: response_reassessment
    weight: 0.20

evidence_sources:                          # 本病例依据的来源
  - textbook: 第十二章 麻醉恢复室患者的护理
  - guideline: 麻醉后监测治疗专家共识

reviewed_by: [专家姓名]
review_date: 2026-08-06
version: 1.0
```

---

## 三、病例难度分级（D1-D4）

**只有 D3 和 D4 要求跨围术期环节。** D1/D2 可以是单一阶段。

| 难度 | 知识点数 | 跨阶段 | 训练目标 | 示例主题 |
|:---:|:---:|:---:|:---|:---|
| D1 | 1 | 否 | 识别 | 识别上呼吸道梗阻、识别残余肌松 |
| D2 | 2 | 否 | 简单应用 | 区分低氧血症与低通气、判断 CRBD 与切口疼痛 |
| D3 | 2-3 | 相邻阶段 | 鉴别和优先级 | PACU 低血压的鉴别（容量/麻醉残余/出血） |
| D4 | 多 | 跨阶段 | 复杂综合决策 | 苏醒延迟 + 循环不稳 + 寒战的联合处理 |

### 难度匹配规则

病例难度根据学习者状态动态选择：
- KC mastery < 0.3 → D1/D2（先练识别和简单应用）
- KC mastery 0.3-0.7 → D2/D3
- KC mastery > 0.7 → D3/D4（挑战迁移）
- **不因整体 level 高就给 D4**——看具体 KC 的 M 值

---

## 四、受控变量替换规则

为使不同学习者遇到的病例难度可比（研究需要），变量替换必须在 `allowed_variations` 范围内：

```text
生成病例时：
  for each variable in allowed_variations:
    value = random_choice(allowed_variations[variable])   # 在允许范围内随机
  将 value 填入 initial_state
```

**禁止**：让模型自由编造年龄/BMI/SpO₂ 等数值。所有数值必须在骨架声明的范围内。

---

## 五、状态机推进规则

病例不是静态的——学习者的每个处置会触发状态转移：

```text
学习者输入处置
  ↓
匹配 critical_actions 中的动作
  ↓
查 state_transitions：该动作对应的状态变化
  ↓
输出新的生命体征 + 反馈类型（positive/partial/deterioration）
  ↓
按 feedback 类型生成自然语言反馈
```

### 反馈类型

| feedback | 含义 | 输出 |
|:---|:---|:---|
| positive | 处置正确，病情改善 | 新体征 + 正向反馈 + 进入下一阶段 |
| partial | 部分正确，暂改善但未根治 | 新体征 + 提示"根本问题未解决" |
| deterioration | 未处置或处置错误，病情恶化 | 恶化体征 + 提示升级响应 |

---

## 六、训练病例 vs 评价病例（严格分离）

> **训练题、练习病例和正式评价病例必须分开。不能由智能体使用同一病例进行训练和效果评价。**

```yaml
case_purpose:
  training:        训练用（可给提示、可重复、反馈详细）
  practice:        练习用（不给提示、可重复、只给对错）
  assessment:      正式评价（不给提示、不重复、用于研究前后测）
```

每个病例文件必须声明 `case_purpose`。研究用的前后测卷必须用 `assessment` 类病例，且不能在训练阶段暴露。

---

## 七、与其它文件的联动

| 联动文件 | 关系 |
|:---|:---|
| `scoring-rubrics.md` | 病例的 rubric 字段引用此处的错误类型 |
| `learner-state.md` | 难度 D1-D4 匹配 support_level S1-S4 |
| `safety-boundaries.md` | critical_actions 不让护士处方 |
| `critical-content.md` | safety_critical=true 的病例按 P0 规则处理 |
| subskills/case-simulator.md | 执行本文件的状态机推进逻辑 |
| cases/*.md | 每个文件是一个本 schema 的实例 |
