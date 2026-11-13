# 课程图（PACU 主线 + 全教材课程库）

> **第一阶段产品定位**：PACU 苏醒期护理自适应学习。PACU 12 主题是默认主线，全教材 22 章作为可选课程库保留。

---

## 第一阶段主线：PACU 全麻苏醒期护理 12 主题

| 序号 | 主题 | 对应病例 | 难度 | 安全关键 |
|:---:|:---|:---|:---:|:---:|
| 1 | PACU 初始评估与交接 | pacu-initial-assessment-001 | D1 | 否 |
| 2 | 上呼吸道梗阻（舌后坠） | pacu-airway-obstruction-001 | D2 | 否 |
| 3 | 低氧血症与低通气鉴别 | pacu-hypoxemia-001 | D2 | 是 |
| 4 | 残余肌松识别 | pacu-residual-neuromuscular-001 | D2 | 是 |
| 5 | 苏醒延迟鉴别 | pacu-emergence-delay-001 | D3 | 是 |
| 6 | 苏醒期躁动（成人） | pacu-emergence-delirium-001 | D2 | 否 |
| 7 | CRBD（小儿苏醒期谵妄） | pacu-crbd-001 | D2 | 否 |
| 8 | 术后疼痛与 PCA 管理 | pacu-postoperative-pain-001 | D2 | 否 |
| 9 | PONV 评估与误吸预防 | pacu-ponv-001 | D2 | 是 |
| 10 | 低体温与寒战 | pacu-hypothermia-001 | D2 | 否 |
| 11 | 血流动力学异常（低血压） | pacu-hypotension-001 | D3 | 是 |
| 12 | PACU 离室评估 | pacu-discharge-readiness-001 | D3 | 否 |

### PACU 主线的学习顺序建议

```text
入门：1 初始评估（D1，建立接收流程认知）
  ↓
识别：2 气道梗阻 / 3 低氧 / 4 残余肌松（D2，单问题识别）
  ↓
应用：6 躁动 / 7 CRBD / 8 疼痛 / 9 PONV / 10 低体温（D2，简单应用）
  ↓
鉴别：5 苏醒延迟 / 11 低血压（D3，多原因鉴别）
  ↓
综合：12 离室评估（D3，系统整合）
```

### PACU 核心知识点（KC）清单（30-50 个）

每个主题对应 2-4 个 KC，总计约 35 个：

```yaml
pacu_kcs:
  # 主题1
  - pacu_handoff_reception
  - immediate_assessment_abc
  - baseline_vitals_recording
  # 主题2
  - upper_airway_obstruction
  - oxygenation_assessment
  - airway_priority
  - airway_intervention
  - response_reassessment
  # 主题3
  - hypoventilation_recognition
  - oxygen_therapy_principle
  # 主题4
  - residual_block_recognition
  - train_of_four_assessment
  - airway_protection
  # 主题5
  - emergence_delay_recognition
  - differential_diagnosis_delay
  - reversible_cause_search
  # 主题6/7
  - emergence_delirium_recognition
  - crbd_recognition
  - pediatric_safety_protection
  - pain_vs_delirium_differentiation
  - safety_protection
  - differentiation_from_pain
  # 主题8
  - pain_assessment_nrs
  - pca_function_check
  - pain_differential_somatic_vs_visceral
  # 主题9
  - ponv_risk_assessment
  - aspiration_prevention
  - antiemetic_nursing
  # 主题10
  - hypothermia_assessment
  - rewarming_technique
  - shivering_management
  # 主题11
  - hypotension_differential
  - volume_assessment
  - escalation_threshold
  # 主题12
  - aldrete_scoring
  - discharge_criteria_checklist
  - discharge_clearance_judgment
```

---

## 附录：全教材课程库（可选模式 `guided_course`）

完整 22 章保留为课程库，供 `guided_course` 模式或 `topic_learning` 按需调用。**不作为默认入口**。

### 第一篇 绪论
- 第一章 麻醉护理学发展史
- 第二章 麻醉科建设与工作范畴
- 第三章 麻醉专科护士培养

### 第二篇 基础知识与技能
- 第四章 围术期常用药物
- 第五章 围术期液体管理
- 第六章 监测技术与护理

### 第三篇 临床麻醉护理学
- 第七章 麻醉前访视与护理
- 第八章 麻醉前护理准备
- 第九章 气道管理及护理
- 第十章 各种麻醉的护理
- 第十一章 围术期并发症及意外

### 第四篇 重症医学护理学
- 第十二章 麻醉恢复室患者的护理 ⭐（PACU 主线核心来源）
- 第十三章 重症医学常见护理技术
- 第十四章 心肺脑复苏
- 第十五章 各脏器功能不全的护理

### 第五篇 疼痛诊疗护理学
- 第十六章 疼痛概述
- 第十七章 疼痛分类与评估
- 第十八章 疼痛治疗与护理

### 第六篇 麻醉护理管理
- 第十九章 麻醉科药品管理
- 第二十章 麻醉科医院感染管理
- 第二十一章 麻醉科仪器设备使用与维护
- 第二十二章 麻醉科信息管理

> 第一阶段聚焦 PACU（主来自第十二章）。其它章节的病例骨架库在后续阶段逐步建设。

---

## 围术期主循环（认知锚点，保留）

```text
术前评估 → 麻醉前准备 → 麻醉诱导 → 麻醉维持 → 术毕苏醒 → 术后恢复/随访
     ↑                                                          │
     └──────────────── 反馈与改进 ←──────────────────────────────┘
```

PACU 主线对应主循环的**术毕苏醒 + 术后恢复**两个环节。
