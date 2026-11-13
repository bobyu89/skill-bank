# Subskill: misconception-rater（错误类型识别）

> **职责**：把学习者的"答错"细分为 9 类（见 scoring-rubrics.md），每类对应不同的教学响应。**不只判断对错，而是识别错误的具体原因。**

---

## 触发条件

micro-tutor Step 3 或 case-simulator Step 7 评分时加载本文件。

## 执行前读取

- 学习者的原始回答
- 标准 critical_actions
- rubric 各维度

---

## 9 类错误识别决策树

```text
学习者回答
  ↓
是否识别出关键征象？
  ├─ 否 → key_sign_miss（关键征象遗漏）
  └─ 是 ↓
是否混淆了概念？
  ├─ 是 → concept_confusion（概念混淆）
  └─ 否 ↓
是否理解机制？
  ├─ 否 → mechanism_error（机制理解错误）
  └─ 是 ↓
风险等级判断是否正确？
  ├─ 否 → risk_level_error（风险等级判断错误）
  └─ 是 ↓
处置优先级是否正确？
  ├─ 否 → priority_error（处置优先级错误）
  └─ 是 ↓
是否遗漏护理措施？
  ├─ 是 → action_omission（护理措施遗漏）
  └─ 否 ↓
是否及时报告升级？
  ├─ 否 → escalation_delay（升级报告不及时）
  └─ 是 ↓
是否做再评价？
  ├─ 否 → reassessment_miss（未进行再评价）
  └─ 是 ↓
记录是否完整？
  ├─ 否 → documentation_gap（记录不完整）
  └─ 是 → （无错误，答对）
```

## 识别规则

一个回答可能同时存在多种错误（如既遗漏征象又优先级错）。识别时：

1. **逐项过决策树**，标记所有命中的错误类型
2. **取最严重的一项**作为主 misconception 写入事件日志
3. **其余作为次要错误**记录到 rubric_detail

### 严重度排序

```text
key_sign_miss ≈ risk_level_error > priority_error > escalation_delay >
mechanism_error > concept_confusion > action_omission > reassessment_miss > documentation_gap
```

安全关键内容的 key_sign_miss / risk_level_error 最严重（可能危及生命）。

---

## 每类错误的教学响应（联动）

| 错误类型 | 教学响应（加载） | 目标 |
|:---|:---|:---|
| key_sign_miss | micro-tutor 回概念剖析 + D1 识别训练 | 强化征象识别 |
| concept_confusion | 概念对比表（A vs B） | 鉴别诊断 |
| mechanism_error | 回机制讲解 + 生理图解 | 理解因果 |
| risk_level_error | 风险分级训练（MEWS/NEWS） | 风险判断 |
| priority_error | 优先级排序训练（ABCDE/SBAR） | 优先级 |
| action_omission | critical_actions 检查清单复述 | 完整性 |
| escalation_delay | 报告时机情景演练 | 升级意识 |
| reassessment_miss | "处置→再评价"循环强化 | 闭环思维 |
| documentation_gap | 护理记录规范练习 | 记录规范 |

---

## 输出

```yaml
primary_misconception: priority_error
secondary_errors: [reassessment_miss]
rubric_detail:
  key_sign_recognition: 1.0
  priority_judgment: 0.0
  nursing_action: 0.5
  reassessment: 0.0
recommended_response: 优先级排序训练（ABCDE 评估法）
```

写入事件日志的 misconception 字段，为研究"哪类错误最常见"提供数据。

---

## 硬规则

1. **不只说"错"，必须指明哪类错**
2. **多错并存时取最严重为主**
3. 教学响应对应错误类型，不能千篇一律
4. 安全关键内容的错误标记 `safety_critical_miss: true`
