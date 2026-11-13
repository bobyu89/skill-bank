# 審稿範例集

## 目錄
1. [範例一：Minor Revision — RCT 研究](#範例一)
2. [範例二：Major Revision — AI/ML 研究](#範例二)
3. [範例三：Reject — 觀察性研究](#範例三)

---

## 範例一：Minor Revision — RCT 研究 {#範例一}

**論文：** "Effect of a Nurse-Led Telehealth Intervention on HbA1c in Type 2 Diabetes: A Randomized Controlled Trial"

### 1. Summary
This RCT examines the effect of a 12-week nurse-led telehealth intervention on glycemic control (HbA1c) in 186 adults with type 2 diabetes. The study demonstrates a statistically significant reduction in HbA1c (-0.6%, p=0.003) in the intervention group compared to usual care. The study is well-designed with adequate randomization and blinding of outcome assessors. The main concern is the relatively short follow-up period and potential contamination between groups.

### 2. Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Novelty | 3 | Telehealth diabetes management is well-studied; the nursing-specific angle adds limited novelty |
| Methodology | 4 | Sound RCT design with proper randomization; minor concerns about contamination control |
| Significance | 4 | Clinically meaningful HbA1c reduction with practical implications for nursing telehealth |
| Clarity | 4 | Well-written with clear CONSORT flow diagram; minor issues in Table 2 labeling |
| **Weighted Total** | **3.75** | |

### 3. Strengths
**S1. Rigorous randomization and allocation concealment**
The use of computer-generated randomization with sealed envelopes and blinding of outcome assessors demonstrates methodological rigor appropriate for an RCT of this nature.

**S2. Clinically meaningful primary outcome**
The 0.6% reduction in HbA1c exceeds the commonly accepted threshold of 0.5% for clinical significance, and the authors appropriately distinguish clinical from statistical significance in the Discussion.

**S3. Comprehensive intervention description**
The intervention protocol is described in sufficient detail (frequency, duration, content of each session) to enable replication, addressing a common gap in nursing intervention studies.

### 4. Major Issues
**M1. Insufficient follow-up duration**
**Location:** Methods, Section 2.4; Discussion, paragraph 3
**Problem:** A 12-week follow-up cannot demonstrate sustained behavior change. HbA1c improvement may represent initial novelty effect rather than lasting glycemic control. Most diabetes RCTs report 6-12 month outcomes.
**Suggestion:** Authors should either (a) report longer-term follow-up data if available, or (b) clearly frame results as short-term effects and discuss plans for a follow-up study.

### 5. Minor Issues
**m1. Table 2 missing units**
**Location:** Table 2, column headers
**Problem:** Blood pressure values lack units (mmHg) in the column header.
**Suggestion:** Add units to all measurement columns.

**m2. Incomplete CONSORT checklist**
**Location:** Supplementary materials
**Problem:** Item 6b (changes to trial outcomes after trial commenced) is not addressed.
**Suggestion:** Include explicit statement even if no changes occurred.

### 6. Recommendation
**Minor Revision** — The core RCT is sound with clinically meaningful results. M1 requires additional discussion but does not invalidate the findings. Minor corrections to tables and CONSORT compliance should be addressed.

---

## 範例二：Major Revision — AI/ML 研究 {#範例二}

**論文：** "DeepTriageNP: A Deep Learning Model for Emergency Department Triage Decision Support"

### 1. Summary
This study develops a deep learning model (DeepTriageNP) for predicting emergency department triage acuity levels using structured EHR data from 45,000 ED visits. The model achieves 82.3% accuracy and AUC-ROC of 0.91. While the clinical problem is important and the dataset is substantial, the study suffers from significant methodological gaps including lack of external validation, insufficient ablation studies, and incomplete fairness analysis that undermine confidence in the reported results.

### 2. Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Novelty | 3 | ED triage ML models exist; the NP-specific framing and feature set add incremental value |
| Methodology | 2 | No external validation, no ablation study, single random split instead of cross-validation |
| Significance | 4 | High practical importance if validated; addresses real NP workflow pain point |
| Clarity | 3 | Generally readable but model architecture description lacks critical details |
| **Weighted Total** | **2.85** | |

### 3. Strengths
**S1. Large, real-world dataset**
Using 45,000 actual ED visit records provides a realistic foundation for model development, avoiding the artificial simplicity common in smaller proof-of-concept studies.

**S2. Clinically grounded feature engineering**
The feature selection process involved practicing NPs and reflects actual triage assessment variables, increasing face validity and potential for clinical adoption.

**S3. Important clinical problem**
ED triage is a high-stakes, time-sensitive task where NPs could genuinely benefit from decision support, making this a worthwhile research direction.

### 4. Major Issues
**M1. No external validation**
**Location:** Methods, Section 3.3
**Problem:** The model is trained and tested on data from a single institution (70/15/15 split). Without external validation, generalizability to other ED populations, practice patterns, and EHR systems is unknown. This is critical for any clinical deployment claim.
**Suggestion:** Validate on at least one external dataset from a different institution or health system. If not available, explicitly state this as a major limitation and remove claims about deployment readiness.

**M2. Missing ablation study**
**Location:** Results, Section 4
**Problem:** The contribution of individual feature groups and model components is unclear. Readers cannot determine whether the deep learning architecture provides genuine improvement over simpler models or whether specific clinical features drive performance.
**Suggestion:** Add ablation experiments: (a) remove feature groups one at a time, (b) compare against logistic regression and random forest baselines, (c) show learning curves.

**M3. Incomplete fairness analysis**
**Location:** Discussion, Section 5.2
**Problem:** The authors mention fairness briefly but provide no disaggregated performance metrics by race, age, or gender. In ED triage, algorithmic bias could have life-threatening consequences.
**Suggestion:** Report accuracy, sensitivity, and specificity broken down by demographic groups. Apply at least one fairness metric (e.g., equalized odds).

### 5. Minor Issues
**m1. Only accuracy and AUC-ROC reported**
**Location:** Table 3
**Problem:** For multi-class triage prediction, per-class precision, recall, and F1 scores are essential. Under-triage (predicting lower acuity than actual) is clinically more dangerous than over-triage.
**Suggestion:** Add confusion matrix and per-class metrics, highlighting under-triage rate specifically.

**m2. No confidence intervals**
**Location:** Results, all reported metrics
**Problem:** Single-point performance estimates without CI or standard deviation make it impossible to assess reliability.
**Suggestion:** Report 95% CI using bootstrap resampling.

### 6. Recommendation
**Major Revision** — The research addresses an important problem with a substantial dataset, but the three major methodological gaps (no external validation, no ablation, no fairness analysis) must be addressed before the paper can be considered for publication. These are addressable issues that do not require fundamental redesign.

---

## 範例三：Reject — 觀察性研究 {#範例三}

**論文：** "Association Between Night Shift Work and Burnout Among ICU Nurses: A Cross-Sectional Study"

### 1. Summary
This cross-sectional study surveys 89 ICU nurses to examine the association between night shift frequency and burnout (measured by MBI). The study reports a significant positive correlation (r=0.42, p<0.01). However, the study has fundamental design limitations: an inadequate sample size for the number of variables analyzed, failure to control for major confounders, an inappropriate causal framing for cross-sectional data, and significant sampling bias. These issues collectively undermine the validity of the conclusions.

### 2. Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Novelty | 1 | Night shift and nurse burnout association is extensively documented in the literature |
| Methodology | 2 | Underpowered, uncontrolled confounders, convenience sample with 38% response rate |
| Significance | 2 | Findings replicate known associations without new insight or actionable recommendations |
| Clarity | 3 | Reasonably well-written but Discussion overstates findings |
| **Weighted Total** | **1.85** | |

### 3. Strengths
**S1. Validated instrument**
Using the Maslach Burnout Inventory is appropriate and ensures measurement validity for the burnout construct.

**S2. Relevant clinical context**
ICU nursing burnout is a genuine and pressing issue, and the research question has practical importance.

**S3. Detailed demographic description**
The participant characteristics table provides comprehensive information about the sample.

### 4. Major Issues
**M1. Insufficient sample size**
**Location:** Methods, Section 2.2
**Problem:** With 89 participants and 12 predictor variables in the regression model, the study violates minimum sample size guidelines (commonly 10-15 per predictor). No a priori power analysis is provided. The study is likely underpowered to detect meaningful effects or produce stable regression coefficients.
**Suggestion:** A properly powered study would require approximately 120-180 participants minimum. Consider expanding recruitment or reducing the number of predictors.

**M2. Uncontrolled confounders**
**Location:** Methods, Section 2.4; Table 4
**Problem:** The regression model does not control for known major confounders of nurse burnout: nurse-patient ratio, organizational support, personal coping strategies, and years of ICU experience. The observed night shift-burnout correlation may be entirely explained by these unmeasured variables.
**Suggestion:** This is a fundamental design issue. Include established confounders in the regression model, or use propensity score matching.

**M3. Causal language inappropriate for cross-sectional design**
**Location:** Discussion, paragraphs 1, 3, 5; Conclusion
**Problem:** Phrases like "night shift work leads to burnout" and "reducing night shifts would decrease burnout" imply causation, which a cross-sectional design cannot establish. The association could be bidirectional (burned-out nurses may self-select into night shifts).
**Suggestion:** Thoroughly revise all causal language. However, even with corrected language, the correlation finding itself adds minimal new knowledge.

**M4. Severe sampling bias**
**Location:** Methods, Section 2.2
**Problem:** Convenience sampling from a single hospital with 38% response rate raises major concerns about selection bias. Non-respondents may differ systematically in burnout levels. No non-response analysis is provided.
**Suggestion:** Report non-response analysis comparing demographics of respondents vs. non-respondents.

### 5. Minor Issues
**m1. No IRB statement**
**Location:** Methods section
**Problem:** No mention of ethics committee approval or informed consent procedures.
**Suggestion:** Add IRB approval number and consent procedures.

### 6. Recommendation
**Reject** — While the topic is important, the study replicates well-established findings without novel contribution (Novelty=1) and has multiple fundamental methodological flaws that cannot be addressed through revision alone (sample size, uncontrolled confounders, sampling bias). I encourage the authors to redesign the study with adequate power, confounders control, and ideally a longitudinal or mixed-methods design to advance beyond what is already known about shift work and burnout.
