# 学习者状态模型（替代旧版 BKT）

> **命名更正**：旧版称"BKT 四参数知识追踪"，但实际只用了 2 个参数（M、常错类型）和启发式更新公式，**不是严格意义上的四参数贝叶斯知识追踪**（4P-BKT 需要 P(L0)/P(T)/P(G)/P(S) 且需参数校准）。本版诚实命名为"**启发式知识点掌握度模型**"。

---

## 一、四维度分层（替代旧版 L1-L4 混合分级）

旧版 L1-L4 同时表示身份/经验/水平/难度/提示密度，混淆了多个维度。本版拆为四个独立维度：

```yaml
learner_role:                        # 学习者身份（静态，自报或评估）
  - nursing_student                  # 护生
  - new_pacu_nurse                   # PACU 新护士
  - anesthesia_specialty_nurse       # 麻醉专科护士
  - educator                         # 带教老师

baseline_level:                      # 总体知识水平（粗粒度）
  - novice                           # 新手
  - intermediate                     # 进阶
  - advanced                         # 高级

support_level:                       # 当前给予的提示密度（动态，随表现调整）
  - S1_high_scaffolding              # 高密度脚手架（选项引导、术语自释）
  - S2_moderate_scaffolding          # 中等（开放提问，关键术语解释）
  - S3_low_scaffolding               # 低（讨论式，追问决策理由）
  - S4_independent_reasoning         # 独立推理（平等对话，反向提问）

case_difficulty:                     # 当前病例难度（按 KC 动态匹配）
  - D1_recognition                   # 单一知识点，单一阶段，训练识别
  - D2_application                   # 2 个知识点，同一阶段，简单应用
  - D3_differential_reasoning        # 2-3 个知识点，相邻阶段，鉴别和优先级
  - D4_complex_decision              # 多知识点，跨阶段，复杂综合决策
```

### 四维度的关键意义

> **一个 advanced 麻醉专科护士，也可能对某个具体 KC 不熟悉（M 值低）。**

例如：工作 6 年的专科护士（role=specialty, level=advanced），但对"CRBD 评估"这个具体 KC 是新手（M=0.3）。此时该 KC 的 support_level 应降到 S2，case_difficulty 用 D2，而非因其整体 advanced 就给 D4。

### 示例状态记录

```yaml
learner_role: anesthesia_specialty_nurse
baseline_level: advanced
current_kc: crbd_assessment
current_kc_mastery: 0.45
current_support_level: S2
current_case_difficulty: D2
```

---

## 二、启发式知识点掌握度模型

### 每个 KC 维护的字段

```yaml
kc_id: upper_airway_obstruction
mastery: 0.45                          # 掌握度 M，0-1，初始 0.5
mastery_status: weak                   # weak(<0.3) / emerging(0.3-0.7) / mastered(>0.85)
common_errors:                         # 常见错误类型（见 scoring-rubrics.md）
  - priority_judgment_error
last_updated_lesson: 7
last_updated_at: 2026-08-06T13:30:00
```

### 按题型赋权的更新规则（核心改进）

旧版对所有答题统一用 `M = M + (1-M)×0.3`（对）/ `M×0.4`（错），过于粗糙。本版按题型差异化赋权：

| 题型 | 答对的增益权重 w | 说明 |
|:---|:---:|:---|
| 概念回忆（recall） | 0.15 | 低权重——记住定义不等于掌握 |
| 机制解释（explain） | 0.25 | 中权重——理解因果 |
| 典型病例应用（apply） | 0.35 | 中高权重——能用在标准情境 |
| 变式病例迁移（transfer） | 0.45 | 高权重——能迁移到新情境 |
| 延迟复习答对（delayed） | 0.50 | 最高权重——长期保持的证据 |
| 使用提示后答对（hinted） | 0.10 | 仅计部分掌握——依赖提示不算真懂 |

**更新公式**：

```text
答对：M_new = M + (1 - M) × w          # w 取上表对应值
答错：M_new = M × 0.4                   # 普通题
      M_new = M × 0.3                   # 安全关键内容答错（更严格）
```

**状态阈值**：
- M < 0.3 → `weak`（薄弱，优先纳入复习和病例训练）
- 0.3 ≤ M < 0.85 → `emerging`（发展中）
- M ≥ 0.85 → `mastered`（掌握）

---

## 三、分析性评分（病例含多 KC 时分别更新）

### 旧版问题

旧版一个病例答错就把所有 KC 统一 ×0.4，但学习者可能只是：
- 未识别鼾声（key_sign_miss）
- 不理解氧合与通气区别（concept_confusion）
- 处置顺序错误（priority_error）
- 遗漏再评价（reassessment_miss）

这些是**不同 KC 的不同错误**，不能一刀切。

### 新版规则：按 rubric 分别评分

每个病例在 `cases/*.md` 中定义评分量表（详见 `scoring-rubrics.md`），例如：

```yaml
rubric:
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
```

**评分流程**：
1. 学习者作答后，按 rubric 每个维度独立打分（0/0.5/1）
2. 计算 response_score = Σ(维度得分 × weight)
3. **每个涉及的 KC 分别按其维度得分更新 M 值**
4. 识别最薄弱的维度 → 标记为 misconception 写入事件日志

### 示例

学习者对 PACU 上呼吸道梗阻病例的作答：
- key_sign_recognition: 1.0（正确识别鼾声+SpO₂下降）→ KC `upper_airway_obstruction` 答对
- priority_judgment: 0.0（先给氧而非先开放气道）→ KC `airway_priority` 答错
- nursing_action: 0.5（开放气道但手法不规范）→ KC `airway_intervention` 部分掌握
- reassessment: 0.0（漏做再评价）→ KC `response_reassessment` 答错

更新结果：4 个 KC 各自独立更新，misconception 标记为 `priority_judgment_error`。

---

## 四、关于"未来真正实施 BKT"的要求

如后期需在论文中正式使用四参数 BKT，至少应维护：

```yaml
P_L0: 初始掌握概率
P_T:  学习转移概率（一次教学后从不会到会的概率）
P_G:  猜对概率（不会但蒙对的概率）
P_S:  已掌握但答错的概率（失误）
```

且每道题需配置知识点映射：

```yaml
item_id: case-pacu-001-q1
kc_weights:
  upper_airway_obstruction: 0.5
  oxygenation_assessment: 0.3
  escalation_priority: 0.2
```

**在没有足够学习数据进行参数校准前，优先使用本文件的启发式掌握度 + 分析性评分。**

---

## 五、与其它文件的联动

| 联动文件 | 关系 |
|:---|:---|
| `scoring-rubrics.md` | 定义 rubric 结构和 9 类错误 |
| `case-schema.md` | 每个病例声明其 rubric |
| subskills/mastery-tracker.md | 执行本文件的更新公式 |
| subskills/review-planner.md | 读 M 值决定复习优先级 |
| subskills/case-simulator.md | 读 M 值决定病例难度 |
