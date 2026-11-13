# 输出模板（笔记 + 事件日志 + 反馈）

> 本文件定义三类输出模板：学习笔记、结构化事件日志（为研究准备）、多视角反馈。

---

## 一、结构化事件日志（研究数据核心）

> 每次教学交互（答题/病例）结束写入一条 JSON。这是后续教学研究的数据基础。**训练/练习/评价必须分开**，不能混用同一事件流做研究分析。

### 字段结构

```json
{
  "session_id": "S001",
  "learner_id": "L001",
  "skill_version": "2.0.0",
  "model_version": "model-name",
  "knowledge_base_version": "2026-08-01",

  "interaction_id": "I_2026_0806_001",
  "timestamp": "2026-08-06T13:30:00+08:00",

  "learning_mode": "case_training",
  "case_purpose": "training",

  "kc_ids": ["upper_airway_obstruction", "airway_priority", "airway_intervention", "response_reassessment"],
  "item_id": "case-pacu-airway-obstruction-001-q1",
  "case_id": "pacu-airway-obstruction-001",

  "difficulty": "D2",
  "support_level": "S2",

  "response_score": 0.425,
  "rubric_detail": {
    "key_sign_recognition": 1.0,
    "priority_judgment": 0.0,
    "nursing_action": 0.5,
    "reassessment": 0.0
  },

  "hint_level": 1,
  "misconception": "priority_error",
  "secondary_errors": ["reassessment_miss"],

  "safety_flag": false,
  "safety_critical_miss": false,

  "source_ids": ["guideline-pacu-current", "textbook-anesthesia-nursing-ch12"],

  "mastery_before": {
    "upper_airway_obstruction": 0.5,
    "airway_priority": 0.6,
    "airway_intervention": 0.5,
    "response_reassessment": 0.5
  },
  "mastery_after": {
    "upper_airway_obstruction": 0.605,
    "airway_priority": 0.24,
    "airway_intervention": 0.605,
    "response_reassessment": 0.20
  },

  "response_time_seconds": 62
}
```

### 字段说明

| 字段 | 研究用途 |
|:---|:---|
| session_id / learner_id | 追踪个体学习轨迹 |
| skill_version / model_version | 不同版本的教学效果对比 |
| difficulty / support_level | 难度与提示等级的交互效应 |
| response_score / rubric_detail | 哪些维度是普遍难点 |
| hint_level | 哪一级提示最有效（成本-效益分析） |
| misconception | 哪类错误最常见 → 改进教学重点 |
| safety_flag / safety_critical_miss | AI 安全审计 |
| source_ids | 证据溯源 |
| mastery_before / mastery_after | 学习增益分析 |
| response_time_seconds | 反应时长作为认知负荷代理指标 |

### 训练 vs 评价数据分离

```yaml
data_segregation:
  training_logs:    case_purpose=training/practice → 用于实时教学优化
  assessment_logs:  case_purpose=assessment        → 用于研究前后测，独立存储
```

**研究用的前后测卷必须用 assessment 病例，且不能在训练阶段暴露给学习者。**

---

## 二、学习笔记模板

### 微学习笔记（单 KC 讲解后）

```markdown
# [日期] · [KC 名称] 学习

## 诊断性问题
[本节开始时问的问题]

## 我的回答
[学习者的原始回答]

## 识别的错误类型
[misconception 类型 + 解释]

## 核心概念
[讲解的一个概念]

## 依据
- 📋 [来源层级标注]

## 病例应用
[小病例的情境 + 我的处置]

## 掌握度变化
M: [before] → [after]

## 待复习
- [若 M<0.3 加入复习队列]
```

### 病例训练笔记

```markdown
# [日期] · [病例标题] 训练

## 病例情境
[患者背景 + 生命体征]

## 我的处置与思路
[学习者的回答]

## 状态演变
[状态机推进的各步：处置→生理变化→反馈]

## 评分
- response_score: [总分]
- 各维度: [rubric_detail]
- 主 misconception: [错误类型]

## 多视角反馈
[按 evidence-policy.md 的四层证据展示]

## 涉及 KC 的掌握度更新
[各 KC 的 M 变化]

## 教学要点
[本病例的核心知识点]
```

---

## 三、多视角反馈模板（取代旧版"三者平等"）

按 evidence-policy.md 的四层证据层级展示，**不再三等分**：

```markdown
【反馈】

✅ 你的判断中正确的部分：
[肯定学习者的合理之处]

⚠️ 需要调整的部分：
[指出错误 + 错误类型]

📖 证据层级展示：

📜 第一层（本机构 SOP）：[若有，引用机构制度；若无，标注"未配置"]
📋 第二层（现行指南）：《[指南名]》（[年份]）：[推荐意见]
📖 第三层（教材）：《麻醉护理学》第X章：[原文要点]
🏥 第四层（实践差异）：[部分医院可能做法]——⚠️ 仅实践差异说明，非标准

📌 核心要点：
[一句话总结]

🔄 下一步：
[根据 misconception 推荐的教学响应]
```

---

## 四、事件日志存储位置

```yaml
event_log_path: ${PROJECT_ROOT}/data/events/learner_${learner_id}/
naming: events_${date}.jsonl     # 每天一个文件，JSONL 格式（每行一条）
retention: 永久（研究需要长期数据）
backup: 每周自动备份
```

> ⚠️ 隐私：事件日志**不存储真实患者信息**（见 safety-boundaries.md）。所有病例交互使用 cases/ 的去标识化骨架。
