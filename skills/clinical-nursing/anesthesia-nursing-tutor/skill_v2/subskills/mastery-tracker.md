# Subskill: mastery-tracker（掌握度更新）

> **职责**：轮末更新各 KC 的掌握度。按题型权重 + 分析性评分，**分别**更新涉及的每个 KC，不再一刀切。

---

## 触发条件

每轮教学动作（答题/病例）结束时，总控第 6 步加载本文件。

## 执行前读取

1. 当前 KC 列表（单 KC 讲解 或 病例的 target_kcs）
2. 题型（recall/explain/apply/transfer/delayed/hinted）
3. 若是病例：读取该病例的 rubric 各维度得分
4. 提示级别（hint_level 0-4）

---

## 更新算法

### 单 KC 场景（micro-tutor 讲解）

```text
查题型权重 w（learner-state.md 的赋权表）：
  recall     → 0.15
  explain    → 0.25
  apply      → 0.35
  transfer   → 0.45
  delayed    → 0.50

查提示级别折扣 f（hint-ladder.md）：
  hint_level 0 → f = 1.0
  hint_level 1 → f = 0.6
  hint_level 2 → f = 0.3
  hint_level 3 → f = 0.1
  hint_level 4 → f = 0.0

if 答对:
  M_new = M + (1 - M) × w × f
elif 答错:
  if safety_critical: M_new = M × 0.3
  else: M_new = M × 0.4

更新 mastery_status:
  M < 0.3       → weak
  0.3 ≤ M < 0.85 → emerging
  M ≥ 0.85      → mastered
```

### 多 KC 场景（病例训练）

按 rubric 各维度分别处理：

```text
for each 维度 in rubric:
  维度得分 = 学习者在该维度的表现（0/0.5/1.0）
  对应的 KC = rubric[维度].kc
  
  if 维度得分 ≥ 0.5:
    该 KC 按答对处理（题型=apply，权重 0.35，乘以提示折扣）
  else:
    该 KC 按答错处理
  
  独立更新该 KC 的 M 值

识别最薄弱维度（得分最低）→ 其错误类型作为 misconception 写入日志
```

---

## 示例

### 示例 1：单 KC 讲解（recall 答对，无提示）

```
KC: upper_airway_obstruction, M_old = 0.5
题型: recall → w = 0.15
提示: 0 → f = 1.0
答对
M_new = 0.5 + (1 - 0.5) × 0.15 × 1.0 = 0.575
状态: emerging
```

### 示例 2：病例多 KC（分析性评分）

```
病例: pacu-airway-obstruction-001, hint_level = 1
rubric 得分:
  key_sign_recognition (kc: upper_airway_obstruction): 1.0 → 答对
  priority_judgment (kc: airway_priority): 0.0 → 答错
  nursing_action (kc: airway_intervention): 0.5 → 答对
  reassessment (kc: response_reassessment): 0.0 → 答错

各 KC 独立更新:
  upper_airway_obstruction: apply 答对，提示折扣 0.6
    M = M + (1-M)×0.35×0.6
  airway_priority: apply 答错
    M = M × 0.4
  airway_intervention: apply 答对（0.5 算对），提示折扣 0.6
    M = M + (1-M)×0.35×0.6
  response_reassessment: apply 答错
    M = M × 0.4

misconception: priority_error（priority_judgment 维度最薄弱）
```

---

## 安全关键内容的额外处理

若 KC 属于 critical-content.md 清单：

```text
答错时:
  M_new = M × 0.3（更严格）
  事件日志 safety_critical_miss = true
  强制安排补救训练（加入近期复习队列，不能跳过）
  该 KC 在补救通过前不能标记 mastered
```

---

## 输出

更新进度文件的 BKT 知识追踪表（改名为"掌握度追踪表"）：

```markdown
| 知识点（KC） | 掌握度 M | 状态 | 常见错误 | 上次更新 | 安全关键 |
|:---|:---:|:---|:---|:---:|:---:|
| upper_airway_obstruction | 0.65 | emerging | - | 课7 | 否 |
| airway_priority | 0.20 | weak | priority_error | 课7 | 否 |
```

同时写事件日志（见 output-templates.md），含 response_score、rubric_detail、misconception、hint_level、safety_critical_miss。

---

## 硬规则

1. **每个 KC 独立更新**，病例场景不统一乘系数
2. **提示后答对要打折**（hint_level 影响权重）
3. **安全关键内容答错更严格**（×0.3 + 强制补救）
4. 更新后立即同步到进度文件和事件日志
