# 证据层级与来源注册表（P0）

> **本文件取代旧版"教材/指南/临床三者平等"的多视角规则。** 临床实际操作不能与指南和标准视为同等证据——它可能只是某医院或个人的习惯，不一定符合现行指南。

---

## 一、四层证据层级（从高到低）

```text
第一层：法律法规、护理执业范围、本机构现行制度/SOP
        ↓
第二层：现行指南、专家共识、专业标准
        ↓
第三层：指定教材（《麻醉护理学》）和经过专家审核的教学资料
        ↓
第四层：常见临床做法 / 本地工作流程
        （仅作为"实践差异说明"，不作为独立规范依据）
```

### 各层用途定位

| 层级 | 用途 | 禁止 |
|:---|:---|:---|
| 第一层（法规/SOP） | 判定执业边界、本地流程合规性 | — |
| 第二层（指南/共识） | 规范临床实践的通用原则 | — |
| 第三层（教材） | 建立基础知识框架、课程考试依据 | 不能作为最新临床决策唯一依据 |
| 第四层（临床做法） | 帮助学习者理解实际工作情境的差异 | 不得表述为"临床标准"；不得替代正式指南 |

### 第四层的硬限制

1. 只有知识库中存在正式医院制度或 SOP 时，才可以作为本地实践依据
2. 未经审核的习惯性操作**不能**表述为"临床标准"
3. 本地实践与指南或制度不一致时，**必须明确标记差异**
4. 不得以"临床上一般这样做"为依据，替代正式指南和操作规范

---

## 二、多视角解读的新规则

**旧版（已废止）**：
> 教材、指南、临床三者平等呈现

**新版**：

```text
教材用于建立基础知识框架；
现行指南和本机构制度用于规范临床实践；
本地实践差异仅用于帮助学习者理解实际工作情境，不作为独立规范依据。
```

### 展示格式（取代旧版"三者平等"）

当涉及临床决策时，按以下层级展示，**不再三等分**：

```
【证据层级展示】

📜 第一层（本机构 SOP）：[若有，引用机构制度]
📋 第二层（现行指南）：《[指南名]》（[年份]）：[推荐意见]
📖 第三层（教材）：《麻醉护理学》第X章：[原文要点]
🏥 第四层（实践差异）：部分医院可能[做法]——注意：这是实践差异说明，非标准

⚠️ 若第四层与上层冲突：以第一/二层为准，第四层仅供理解实际工作情境
```

### 冲突处理原则

```text
本机构正式制度 → 优先用于本地流程判断
现行指南       → 优先用于通用临床原则
教材           → 用于基础理论和课程考试
临床经验       → 只用于解释实践差异
所有冲突       → 必须明确展示，不得自动混合、不得隐瞒
```

---

## 三、指南版本注册表

**不再在 SKILL.md 中写死固定的指南清单**。改用结构化注册表，每个来源独立记录。

### 单个来源的字段结构

```yaml
source_id: guideline-airway-2023          # 唯一ID
title: 困难气道管理指南
source_type: guideline                     # law/sop/guideline/consensus/textbook/reference
organization: 中华医学会麻醉学分会
publication_year: 2023
effective_date: 2023-09-01
status: current                            # current / superseded / archived
scope: 困难气道评估与处理
applicable_population: adult               # adult / pediatric / obstetric / all
applicable_setting: or / pacu / icu / all
applicable_role: anesthesia_provider       # physician / nurse / all
supersedes: guideline-airway-2017          # 取代的旧版 source_id
file_path: ${PROJECT_ROOT}/knowledge/guidelines/困难气道管理指南2023.pdf
reviewed_by: [专家姓名列表]
review_date: 2026-08-01
```

### 来源状态规则

- `current`：当前有效版本，可作为决策依据
- `superseded`：已被新版取代，仅作历史参考，禁止作为现行依据
- `archived`：归档，不再使用

### 回答问题前的来源检查（5 步）

每次引用来源前，必须检查：

1. **是否为当前版本**（status: current）？引用 superseded 必须显式说明
2. **是否适用人群**（成人/小儿/产妇）？不匹配则不引用
3. **是否适用于护理决策**（applicable_role）？纯医师指南需注明
4. **是否存在本机构 SOP**？若有，本地流程以 SOP 为准
5. **是否与其他来源冲突**？冲突必须按上述原则处理，明示差异

---

## 四、知识来源 vs 测评来源（严格分离）

### 知识来源（用于生成医学解释和反馈）

```yaml
knowledge_sources:
  - law_and_regulation          # 法律法规
  - institutional_sop           # 本机构 SOP
  - guideline                   # 现行指南
  - consensus                   # 专家共识
  - textbook                    # 指定教材
  - reviewed_reference          # 经专家审核的参考资料
```

**规则**：生成医学解释、护理建议、反馈时，**只能引用 knowledge_sources**。

### 测评来源（用于出题、难度校准、知识点覆盖分析）

```yaml
assessment_sources:
  - expert_case                 # 专家审核病例
  - reviewed_question_bank      # 经审核的题库
  - past_exam                   # 历年真题
  - practice_question           # 练习题
```

**规则**：
- 试卷只能用于题型分析、难度校准、知识点覆盖
- **试卷答案必须经过教材或指南核验**才能用作标准答案
- **不得将试卷作为临床处置建议的证据**

---

## 五、与其它文件的联动

| 联动文件 | 关系 |
|:---|:---|
| `critical-content.md` | 安全关键内容必须来自 knowledge_sources 的前两层 |
| `safety-boundaries.md` | 护理执业边界依据第一层（法规/SOP） |
| subskills/evidence-checker.md | 执行本文件的 5 步来源检查 |
| 总控 SKILL.md | 检索流程按本文件的层级排序 |
