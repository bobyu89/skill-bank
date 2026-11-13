# Subskill: case-simulator（病例模拟）

> **职责**：加载专家审核病例骨架，按状态机推进病例演变。**禁止自由生成病例内容**——所有生理变化、剂量、标准答案都来自骨架文件，大模型只负责叙述和评分。

---

## 触发条件

总控路由到 `case_training` 模式，或 micro-tutor 的 Step 7 需要小病例时加载本文件。

## 执行前检查

1. 读取学习者状态：当前目标 KC 的 mastery → 决定病例难度 D1-D4
2. 确认病例的 `case_purpose`（training/practice/assessment）——研究前后测必须用 assessment 病例

---

## 执行流程

```text
Step 1: 选择病例
        - 从 cases/ 中选一个 target_kcs 包含当前 KC 的病例
        - 难度匹配：KC mastery<0.3 → D1/D2；0.3-0.7 → D2/D3；>0.7 → D3/D4
        - 3 课内不重复同一病例

Step 2: 受控变量替换
        - 读取病例的 allowed_variations
        - 在允许范围内随机选值（age/bmi/spo2 等）
        - 填入 initial_state
        - ⚠️ 禁止模型自由编造数值

Step 3: 自然语言呈现
        - 将 initial_state 转为临床叙述
        - 格式：患者背景 + 生命体征 + 当前情境
        - 不直接给答案
        - 按护理边界提问（safety-boundaries.md 八步法）

Step 4: [等待学习者作答]

Step 5: 匹配处置 → 触发状态转移
        - 解析学习者回答，匹配 critical_actions
        - 查 state_transitions：该动作对应的生理变化
        - ⚠️ 生理变化由状态机决定，不由模型决定

Step 6: 输出新体征 + 反馈
        - 按 feedback 类型（positive/partial/deterioration）生成反馈
        - partial：提示"根本问题未解决"
        - deterioration：提示升级响应

Step 7: 评分
        - 加载 scoring-rubrics.md 的分析性评分
        - 按 rubric 各维度独立打分（0/0.5/1.0）
        - 计算 response_score

Step 8: 更新 + 安排
        - 加载 mastery-tracker.md：按各维度分别更新涉及的 KC
        - 加载 review-planner.md：根据表现安排复习
        - 识别 misconception（最薄弱维度）写入事件日志
```

---

## 病例呈现格式

```text
【病例训练】（难度 D2 | 支持等级 S2）

📋 病例：[case_title]
患者：[年龄]岁，[性别]，[术式]，[麻醉方式]
入 PACU 时：意识[状态]，RR [数值]，SpO₂ [数值]%，[气道声音]
[其他相关体征]

❓ 作为麻醉护士，请判断：
   1. 当前最突出的问题是什么？你依据哪些征象？
   2. 你的首要护理措施是什么？（按优先级）
   3. 需要准备哪些物品/药品/设备？
   4. 何时、向谁报告？报告哪些关键信息？

[等待学习者回答]
```

> 注：问题始终在护理执业边界内（识别/评估/准备/报告），不让学习者处方药物或剂量。

---

## 状态机推进示例

病例 pacu-airway-obstruction-001，学习者回答"先给氧 5L/min"：

```text
解析：匹配到 critical_actions，但未执行 assess_airway_patency 和 perform_airway_opening_maneuver
查 state_transitions.oxygen_only：
  spo2_change: temporary_increase_to_92
  snoring: persistent
  feedback: partial

输出：
📋 情境更新：给氧后 SpO₂ 暂升至 92%，但鼾声持续，意识仍嗜睡。
⚠️ 提示：氧合暂时改善，但气道梗阻的根本问题未解决。继续给氧而不开放气道，梗阻会持续。
❓ 你接下来会怎么做？
```

---

## 硬规则

1. **所有数值（生命体征/剂量/时间）必须来自病例骨架或 allowed_variations**
2. **生理变化必须由 state_transitions 决定**
3. **抢救剂量从 critical-content 来源检索，不由模型生成**
4. **训练病例和评价病例严格分离**
5. 安全边界：问题用护理八步法，不让护士处方
6. 每轮一个动作：呈现病例→等答→反馈→等下一动作
