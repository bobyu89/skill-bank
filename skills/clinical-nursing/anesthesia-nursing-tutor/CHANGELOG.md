# Changelog

本仓库版本记录。格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/)。

## [Unreleased] - 2026-08-06

### 🔬 v2 PACU 病例库专家审核修订（12 例全量）

按"逐个审核 + 修改"流程，对 12 个 PACU 病例骨架完成四维度合规审核（医学准确性 / 护理执业边界 / 状态机逻辑 / rubric 评分 / P0 来源标注）。

#### 审核结论
- ✅ **核心医学逻辑全部通过**：12 例无医学知识错误、无护理越界硬伤（涉药全部声明"属医师处方、不从模型记忆生成"），八步法完整，safety_critical 病例错误路径足够严格
- ✅ **rubric 权重和**：12/12 精确 = 1.0

#### 修订内容
- **KC 一致性修复（8 例）**：airway-obstruction / hypoxemia / residual-neuromuscular / emergence-delirium / crbd / postoperative-pain / ponv / hypothermia —— 在 `target_kcs` 补充声明 `response_reassessment`（及 `airway_intervention`），使 rubric 评分维度可回写到已注册 KC
- **P0 来源标注（5 例 safety_critical）**：hypoxemia / residual-neuromuscular / emergence-delay / ponv / hypotension —— `evidence_sources` 补全 `edition/year/page/verified_by` 字段（按 critical-content.md 规则3，版本页码标为"待临床专家核验"占位，禁用模型记忆伪造）
- **reviewed_by 更新（12 例）**：从 `[待专家审核]` 改为 `"AI合规审核 2026-08-06（医学逻辑/护理边界/状态机/rubric 已核）；⚠️临床专家签字待补"`——诚实区分 AI 合规审核与人类临床专家签字
- **零星修订**：
  - airway-obstruction：补 `oxygen_delivery: room_air` 字段；状态机 `improve_to_alert` → `improve_but_still_drowsy`（更符合"麻醉未完全清醒"的生理）
  - hypoxemia：critical_action 5 "体位引流" → "深呼吸/激励性肺量计/变换体位"（更符合 PACU 实践）；`incorrect_treat_as_hypoventilation` 的 feedback 从 partial 升级为 deterioration（safety_critical 病例鉴别错误应更严格）
  - residual-neuromuscular：critical_action 6 显式加入"核对执行拮抗药医嘱→监测再箭毒化"
  - hypotension：修正 safety_note 笔误"去甲肾上腺素/去甲肾上腺素"→"去甲肾上腺素/肾上腺素"

#### 新增工具
- `skill_v2/verify_cases.py`：病例合规自动验证脚本（检查 KC 一致性 / 权重和 / reviewed_by / P0 来源标注），全 12 例通过

---

## [1.0.0] - 2026-08-06

### 🎉 首次发布

#### 新增
- **Skill 核心**：5 个文件（SKILL.md / agent_prompt.md / 水平评估测试.md / 学习进度追踪_模板.md / SKILL_README.md）
- **综合教学模式**：理论逐章 + 临床情景双轨
- **L1-L4 分层教学系统**：四层级，不同教学策略
- **四步提问法**：定义题 → 应用题 → 反向提问 → 自由发散
- **BKT 知识追踪**：每个知识点量化掌握概率（M 值）
- **三级脚手架**：提示 → 子题 → 兜底
- **三层可审计记忆**：L1 原始事件 / L2 提炼事实 / L3 学习者画像
- **间隔重复系统**：1-3-7-14-30-60 课次
- **多视角解读**：教材 vs 指南 vs 临床三者平等对照
- **高危警示与硬掌握闸门**：恶性高热、局麻药中毒、过敏休克、CPR

#### 知识库
- 核心教材：《麻醉护理学》全文 md（1.7MB）
- 13 份围术期指南/专家共识 PDF（24MB）

#### 设计灵感
- 中医学习导师 Skill 系列（成熟骨架）
- learn-claude-code（渐进课程锚点）
- DeepTutor（可审计三层记忆）
- OATutor（BKT 知识追踪 + 三级脚手架）
- Anthropic Skills（Skill 编写规范）

---

## 版本号规则

- **主版本号.次版本号.修订号**（SemVer）
- 主版本号：教学体系重大重构
- 次版本号：新增章节支持、新增功能
- 修订号：bug 修复、内容勘误
