# PubMed 關鍵字策略 — Bob 個人化版本

> 最後更新：2025-03-15
> 適用主題：CDSS（臨床決策支援）× AI 輔助專科護理師教育

---

## 搜尋規則

**每次搜尋必加篩選：**
```
AND free full text[filter]
AND ("2020/01/01"[PDAT] : "3000"[PDAT])
```

---

## QUERY_CDSS — 臨床決策支援主題

**用於：星期一 / 四**

```
(
  "Decision Support Systems, Clinical"[MeSH] OR
  "clinical decision support"[Title/Abstract] OR
  "CDSS"[Title/Abstract] OR
  "AI-assisted decision"[Title/Abstract] OR
  "early warning system"[Title/Abstract]
)
AND
(
  "Artificial Intelligence"[MeSH] OR
  "machine learning"[Title/Abstract] OR
  "deep learning"[Title/Abstract] OR
  "large language model"[Title/Abstract]
)
AND
(
  "nursing"[Title/Abstract] OR
  "nurse"[Title/Abstract] OR
  "clinical workflow"[Title/Abstract]
)
AND free full text[filter]
```

**核心 MeSH：**
- `Decision Support Systems, Clinical`
- `Artificial Intelligence`
- `Machine Learning`
- `Natural Language Processing`

**核心自由詞：**
- `clinical decision support` / `CDSS`
- `alert fatigue` / `alarm fatigue`
- `sepsis prediction` / `deterioration prediction`
- `predictive analytics` / `risk stratification`
- `early warning system` / `NEWS score`

---

## QUERY_NURSING_EDU — 護理教育主題

**用於：星期二 / 五**

```
(
  "Nurses, Advanced Practice"[MeSH] OR
  "Education, Nursing"[MeSH] OR
  "advanced practice nurse"[Title/Abstract] OR
  "nurse practitioner"[Title/Abstract] OR
  "specialty nurse"[Title/Abstract]
)
AND
(
  "artificial intelligence"[Title/Abstract] OR
  "machine learning"[Title/Abstract] OR
  "simulation"[Title/Abstract] OR
  "large language model"[Title/Abstract]
)
AND
(
  "education"[Title/Abstract] OR
  "training"[Title/Abstract] OR
  "competency"[Title/Abstract] OR
  "clinical assessment"[Title/Abstract]
)
AND free full text[filter]
```

**核心 MeSH：**
- `Nurses, Advanced Practice`
- `Education, Nursing`
- `Simulation Training`
- `Clinical Competence`
- `Nursing Informatics`

**核心自由詞：**
- `nurse practitioner training` / `advanced practice nurse`
- `AI in nursing education` / `nursing simulation`
- `clinical competency` / `OSCE`
- `SBIRT` / `psychiatric nursing`
- `health literacy in nursing`

---

## QUERY_CROSS — CDSS × 護理教育交叉主題

**用於：星期三 / 六**

```
(
  "Decision Support Systems, Clinical"[MeSH] OR
  "clinical decision support"[Title/Abstract] OR
  "CDSS"[Title/Abstract]
)
AND
(
  "nursing workflow"[Title/Abstract] OR
  "nurse perception"[Title/Abstract] OR
  "nursing informatics"[Title/Abstract] OR
  "nursing education"[Title/Abstract]
)
AND
(
  "artificial intelligence"[Title/Abstract] OR
  "machine learning"[Title/Abstract] OR
  "LLM"[Title/Abstract] OR
  "generative AI"[Title/Abstract]
)
AND
(
  "implementation"[Title/Abstract] OR
  "acceptance"[Title/Abstract] OR
  "usability"[Title/Abstract] OR
  "perception"[Title/Abstract]
)
AND free full text[filter]
```

**適合這組的關鍵議題：**
- CDSS × 護理師使用意願 / 信任度
- LLM × 護理臨床決策
- AI 工具的 EHR 整合
- 護理師 alert fatigue 與 AI 警示設計
- digital health implementation in nursing

---

## 主題標籤對照表

| 搜尋結果文章關鍵詞 | 在筆記中標記為 |
|-----------------|-------------|
| CDSS, decision support, alert | `topic/CDSS` |
| nursing education, simulation, competency | `topic/AI-nursing-education` |
| fall risk, sepsis, deterioration | `topic/AI-clinical-prediction` |
| EHR, interoperability, workflow | `topic/Health-Informatics` |
| LLM, ChatGPT, generative AI | `topic/LLM-in-healthcare` |

---

## Obsidian MOC 反向連結對應

| 文章主題 | 接入 MOC |
|---------|---------|
| CDSS / clinical AI | `[[CDSS-MOC]]` |
| 護理教育 / 訓練 | `[[AI-in-Nursing-MOC]]` |
| 跌倒 / 敗血症預測 | `[[Clinical-Prediction-MOC]]` |
| 護理資訊學 | `[[Nursing-Informatics-MOC]]` |
| 研究方法 | `[[Research-Methods-MOC]]` |

---

## 更新指引

當你想新增研究主題時，依以下格式在此檔案新增一個 `## QUERY_XXX` 區塊，
並在 SKILL.md 的週期排程表中加入對應的星期/頻率。
