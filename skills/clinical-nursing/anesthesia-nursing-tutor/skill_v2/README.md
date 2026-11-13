# 麻醉护理学习导师 v2.0（PACU-Tutor 智能体）

> **v2 是按审稿意见全量重构的版本。** 从单文件 1071 行超长提示词，重构为"总控 SKILL + references/ + subskills/ + cases/"的多文件智能体；范围从全教材 22 章收窄为 **PACU 全麻苏醒期护理**专项。

## 与 v1 的对比

| 维度 | v1（skill/） | v2（skill_v2/） |
|:---|:---|:---|
| 架构 | 单文件 1071 行 | 总控 183 行 + 8 references + 8 subskills + 12 cases |
| 范围 | 全教材 22 章 | PACU 苏醒期 12 主题（22 章保留为课程库） |
| 病例生成 | 自由生成（动态情景题引擎） | 专家骨架 + 受控变量 + 状态机 |
| 掌握度 | "BKT 四参数"（名不副实） | 启发式掌握度 + 分析性评分（诚实命名） |
| 证据层级 | 教材/指南/临床三者平等 | 四层层级（法规/SOP > 指南 > 教材 > 实践差异） |
| 护理边界 | 让护士处方（剂量/药物） | 护理八步法（识别→评估→准备→报告→执行医嘱→监测→再评价） |
| 真实临床请求 | 无识别 | 请求分类器 + 6 条处理规则 |
| 高危内容 | 允许模型记忆补全 | 安全关键清单 + 禁用模型记忆 |
| 学习者分层 | L1-L4 混合多义 | 四维度独立（role/level/support/difficulty） |
| 教学流程 | 固定 5 步 | 微学习循环，每轮单动作，等答后再进 |
| 路径 | 绝对 Windows 路径 | config.yaml + ${PROJECT_ROOT} |
| 研究支持 | 无 | 结构化事件日志 JSON（训练/评价分离） |

## 目录结构

```
skill_v2/
├── SKILL.md                    总控路由（183行）
├── SKILL_v1_backup.md          v1 旧版备份（1071行，作历史对比）
├── config.example.yaml         配置模板（用户复制为 config.local.yaml）
│
├── references/                 静态规范（8个）
│   ├── safety-boundaries.md    【P0】请求分类 + 护理边界 + 隐私
│   ├── evidence-policy.md      【P0】四层证据 + 来源注册表
│   ├── critical-content.md     【P0】安全关键内容清单
│   ├── learner-state.md        启发式掌握度 + 四维度分层
│   ├── case-schema.md          病例骨架 YAML + 状态机
│   ├── scoring-rubrics.md      9 类错误 + 分析性评分
│   ├── curriculum-map.md       PACU 12 主题 + 全教材课程库
│   └── output-templates.md     笔记 + 事件日志 + 反馈模板
│
├── subskills/                  执行单元（8个）
│   ├── micro-tutor.md          微学习循环
│   ├── case-simulator.md       病例模拟（骨架+状态机）
│   ├── socratic-questioning.md 四步提问（回忆/解释/应用/迁移）
│   ├── hint-ladder.md          四级提示（最低必要原则）
│   ├── misconception-rater.md  9 类错误识别
│   ├── mastery-tracker.md      掌握度更新（分析性评分）
│   ├── review-planner.md       间隔复习（自然时间+课次双触发）
│   └── evidence-checker.md     证据 5 步核验
│
└── cases/                      PACU 病例骨架库（12个，覆盖12主题）
    ├── pacu-initial-assessment-001.md       D1 PACU 初始评估
    ├── pacu-airway-obstruction-001.md       D2 上呼吸道梗阻
    ├── pacu-hypoxemia-001.md                D2 低氧血症与低通气 ⚠️
    ├── pacu-residual-neuromuscular-001.md   D2 残余肌松 ⚠️
    ├── pacu-emergence-delay-001.md          D3 苏醒延迟鉴别 ⚠️
    ├── pacu-emergence-delirium-001.md       D2 苏醒期躁动（成人）
    ├── pacu-crbd-001.md                     D2 小儿苏醒期谵妄
    ├── pacu-postoperative-pain-001.md       D2 术后疼痛与 PCA
    ├── pacu-ponv-001.md                     D2 PONV 与误吸预防 ⚠️
    ├── pacu-hypothermia-001.md              D2 低体温与寒战
    ├── pacu-hypotension-001.md              D3 血流动力学异常 ⚠️
    └── pacu-discharge-readiness-001.md      D3 PACU 离室评估
```

⚠️ = safety_critical: true（涉及紧急情况，按 critical-content.md 严格处理）

## 使用方法

1. 把 `skill_v2/` 整个目录复制到你的 `.zcode/skills/` 下（重命名为 `麻醉护理学学习导师`）
2. 复制 `config.example.yaml` 为 `config.local.yaml`，按本地路径修改 `${PROJECT_ROOT}`
3. 确保知识库（教材 + 指南）放在 config 配置的路径下
4. 触发：对 ZCode 说"开始麻醉护理学习"

## 三项核心能力

1. **不直接给答案，而是通过分级提示逐步引导**
2. **不只判断对错，而是识别学习者错误的具体原因（9 类）**
3. **不按固定章节机械教学，而是根据知识点掌握情况决定下一步内容**

## ⚠️ 待办（专家审核）

所有病例标注 `reviewed_by: [待专家审核]`。正式用于教学/研究前，需由麻醉护理专家审核：
- 病例医学准确性
- critical_actions 的护理边界合规性
- state_transitions 的生理合理性
- rubric 评分标准的临床合理性

## 研究支持

v2 内置结构化事件日志（见 output-templates.md），支持教学研究：
- 记录每次交互的 KC / 难度 / 评分 / 错误类型 / 提示级别 / 掌握度变化
- 训练数据与评价数据严格分离
- 可用于"AI 动态病例 vs 传统题库"的对照研究
