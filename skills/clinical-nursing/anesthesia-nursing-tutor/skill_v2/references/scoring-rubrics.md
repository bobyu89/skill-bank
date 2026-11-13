# 评分量表与错误类型分类

> **本文件取代旧版"答对/答错"二元判断。** 将学习者错误细分为 9 类，每类对应不同的教学响应策略。配合 case-schema.md 的 rubric 字段实现分析性评分。

---

## 一、9 类错误类型细分

旧版只判断对错。本版把"答错"进一步细分为以下 9 类，每类有明确的教学响应：

| 错误代码 | 错误类型 | 典型表现 | 教学响应策略 |
|:---|:---|:---|:---|
| `key_sign_miss` | 关键征象遗漏 | 未注意到鼾声、SpO₂ 下降、呼吸频率减慢 | 强化征象识别训练，回到概念剖析 |
| `concept_confusion` | 概念混淆 | 混淆低氧血症与低通气、混淆 CRBD 与切口疼痛 | 概念对比表，鉴别诊断训练 |
| `mechanism_error` | 机制理解错误 | 不理解为什么梗阻先于缺氧、不理解残余肌松机制 | 回到机制讲解，配生理机制图解 |
| `risk_level_error` | 风险等级判断错误 | 把危急情况判断为轻症，或反之 | 风险分级训练，早期预警评分 |
| `priority_error` | 处置优先级错误 | 先给氧再开放气道（应反过来） | 优先级排序训练，ABCDE 评估法 |
| `action_omission` | 护理措施遗漏 | 漏做开放气道、漏做再评价 | 检查清单训练，critical_actions 复述 |
| `escalation_delay` | 升级报告不及时 | 未及时报告麻醉医师、未启动应急 | 报告时机训练，SBAR 沟通框架 |
| `reassessment_miss` | 未进行再评价 | 处置后不复查效果 | "处置→再评价"循环强化 |
| `documentation_gap` | 记录不完整 | 漏记时间、漏记生命体征变化 | 护理记录规范训练 |

### 错误类型 → 教学响应映射

```text
key_sign_miss      → 征象识别专项（回 D1 难度病例）
concept_confusion  → 概念对比表（A vs B 鉴别）
mechanism_error    → 机制重讲（回到概念剖析）
risk_level_error   → 风险分级训练（MEWS/NEWS 评分）
priority_error     → 优先级排序（ABCDE、SBAR）
action_omission    → 检查清单复述
escalation_delay   → 报告时机情景演练
reassessment_miss  → "处置→再评价"循环
documentation_gap  → 记录规范练习
```

---

## 二、分析性评分量表（rubric）

每个病例在 case-schema 中声明 rubric。评分时按维度独立打分。

### 维度评分标准（每维 0/0.5/1.0 三档）

| 得分 | 含义 |
|:---:|:---|
| 0 | 完全未达成本维度（遗漏/错误） |
| 0.5 | 部分达成（方向对但不完整/不规范） |
| 1.0 | 完全达成（正确且完整） |

### 综合 response_score 计算

```text
response_score = Σ(维度得分 × 维度权重)
```

范围 0-1.0。例如四个维度各 0.30/0.25/0.25/0.20 权重，若得分 1.0/0.0/0.5/0.0：

```
response_score = 1.0×0.30 + 0.0×0.25 + 0.5×0.25 + 0.0×0.20 = 0.425
```

### response_score → 掌握度更新的映射

| response_score | 含义 | KC 更新策略 |
|:---:|:---|:---|
| ≥ 0.85 | 优秀 | 涉及的 KC 按"答对"更新（题型权重取 apply/transfer） |
| 0.5-0.84 | 合格 | 得分≥0.5 的维度对应 KC"答对"，<0.5 的"答错" |
| < 0.5 | 不合格 | 涉及的 KC 全部按"答错"更新，进入补救 |

---

## 三、提示后答对的处理

学习者使用提示后答对，**不能等同于独立答对**。

| 情况 | 掌握度权重 | 说明 |
|:---|:---:|:---|
| 无提示独立答对 | 题型原权重（如 apply=0.35） | 满分权重 |
| 一级提示（hint）后答对 | 原权重 × 0.6 | 部分掌握 |
| 二级提示（scaffold）后答对 | 原权重 × 0.3 | 依赖脚手架 |
| 三级提示（bottom-out）后"答对" | 0 | 兜底不算掌握 |

> 详见 subskills/hint-ladder.md 的三级提示定义。

---

## 四、安全关键内容的特殊评分

涉及 `critical-content.md` 清单的内容：

- 答错 → M × 0.3（比普通 ×0.4 更严格）
- 事件日志标记 `safety_critical_miss: true`
- **强制进入补救训练**，不能跳过
- 补救训练通过前，该 KC 不能标记为 mastered

---

## 五、事件日志字段（与 scoring 联动）

每次评分后写入的事件日志（见 output-templates.md）包含以下与评分相关的字段：

```json
{
  "response_score": 0.425,
  "rubric_detail": {
    "key_sign_recognition": 1.0,
    "priority_judgment": 0.0,
    "nursing_action": 0.5,
    "reassessment": 0.0
  },
  "misconception": "priority_error",       // 最薄弱维度对应的错误类型
  "hint_level": 1,                         // 使用了几级提示（0=无提示）
  "safety_critical_miss": false
}
```

这些字段为后续教学研究（如"哪类错误最常见""哪级提示最有效"）提供结构化数据。

---

## 六、与其它文件的联动

| 联动文件 | 关系 |
|:---|:---|
| `case-schema.md` | 病例的 rubric 字段定义维度和权重 |
| `learner-state.md` | response_score 映射到 KC 掌握度更新 |
| subskills/misconception-rater.md | 执行本文件的 9 类错误识别 |
| subskills/mastery-tracker.md | 按本文件的映射更新 M 值 |
| subskills/hint-ladder.md | 提示级别影响评分权重 |
