---
name: pdpm-estimate
license: MIT
description: >-
  Estimate the Medicare Fee-for-Service PDPM per-diem rate and total stay
  revenue for a SNF admission from referral documentation (hospital packet,
  discharge summary, therapy notes, med list). Classifies all six PDPM
  components (PT, OT, SLP, Nursing, NTA, non-case-mix), applies the variable
  per-diem schedule, and produces a worksheet plus a length-of-stay revenue
  curve. Use whenever the user mentions PDPM, per-diem, case-mix groups (CMGs),
  HIPPS codes, Section GG function scores, NTA points, or asks anything like
  "what will Medicare pay for this admission," "estimate reimbursement for this
  referral," "is this referral worth taking financially," or "what PDPM rate
  would this patient generate."
---

# PDPM Revenue Estimate from Referral Documentation

Estimate what a Medicare Part A (Fee-for-Service) SNF stay will reimburse under
the Patient-Driven Payment Model (PDPM) **before** the patient is admitted,
using only the referral packet. This helps admissions and billing staff make
informed acceptance decisions and spot documentation gaps early.

**Why this is always an estimate:** actual PDPM classification is set by the
MDS 3.0 assessment (the 5-day PPS assessment) completed *after* admission —
coded diagnoses (I0020B), Section GG function scores, Section K
swallowing/diet items, Section O treatments, and the rest. A pre-admission
estimate built from hospital paperwork can and will differ from the final
HIPPS code. Always label the output as an estimate and flag every assumption.

**Scope guard:** this is Medicare FFS PDPM only. Medicare Advantage plans may
pay levels, contracted rates, or their own PDPM variant — if the payer is an MA
plan, say so and ask for the contract terms instead of assuming FFS rates.

## The six PDPM components

Every Medicare Part A day is paid as the sum of six component rates. Five are
case-mix adjusted (component base rate × case-mix index (CMI) for the
patient's group, × a variable per-diem factor for PT/OT/NTA); one is flat.

| Component | What drives the group | Groups |
|---|---|---|
| PT | PDPM clinical category (collapsed to 4) × GG function score (0–24) | TA–TP (16) |
| OT | Same drivers as PT (groups can differ only via CMI) | TA–TP (16) |
| SLP | Acute neurologic condition, SLP comorbidity, cognitive impairment, swallowing disorder, mechanically altered diet | SA–SL (12) |
| Nursing | RUG-derived clinical hierarchy (extensive services / special care / clinically complex / behavioral / reduced physical function) + function score + depression + restorative nursing | ES3…PA1 (25) |
| NTA | Comorbidity/service point score | NA–NF (6) |
| Non-case-mix | Flat per-diem (room & board overhead) | 1 |

The full classification logic and CMG tables live in
[references/pdpm-components.md](references/pdpm-components.md). **Read that
file whenever you actually classify a patient** — do not classify from memory.

## Workflow

### Step 1 — Gather inputs from the referral packet

Extract (or ask the user for) the following. Note explicitly which items are
documented vs. assumed:

1. **Primary reason for the SNF stay** — the ICD-10 diagnosis that will go in
   MDS item I0020B. Often differs from the hospital's principal diagnosis;
   pick the condition the SNF will primarily manage.
2. **Recent surgical procedures** during the qualifying hospital stay (e.g.,
   hip/knee replacement, spinal fusion, other orthopedic or major surgery) —
   these can shift the clinical category.
3. **Functional status** — anything mapping to Section GG self-care and
   mobility items (therapy evals, nursing notes, PT/OT hospital notes).
4. **Comorbidities and treatments** — full diagnosis list, IV medications,
   parenteral/IV feeding, ventilator/tracheostomy, wounds/ulcers, dialysis,
   isolation, oxygen, chemotherapy, transfusions, etc. (drives Nursing and NTA).
5. **SLP-related factors** — neurologic diagnoses (stroke, TBI), cognitive
   status, swallowing problems, diet texture modifications (thickened liquids,
   mechanical soft, puree).
6. **Depression indicators and restorative nursing** candidacy (affects the
   Nursing group ending; usually unknown pre-admission — assume the more
   conservative option and note it).
7. **Expected length of stay** (from discharge planning or your own typical
   LOS for this diagnosis).

### Step 2 — Ask the user for their facility's current rates

**Never hardcode or recall dollar amounts, CMIs' underlying base rates, or
wage indexes — CMS updates them every fiscal year.** Ask the user for:

- Their facility's **current FY federal urban or rural per-diem base rates**
  for each of the six components (from the current CMS SNF PPS final rule,
  published each summer, effective October 1).
- Their **CBSA wage index** and how their business office applies it (the
  labor-related share of each rate is wage-adjusted; the current labor share
  percentage is also in the final rule).

If the user cannot supply rates, produce the worksheet with the groups and
CMIs filled in and leave rate columns as placeholders labeled
"[insert FY 20XX base rate from CMS SNF PPS final rule]." CMI values also
change by rule year — use the CMIs from the user's current final rule; the
reference file explains where they live.

### Step 3 — Map the primary diagnosis to a PDPM clinical category

Map the ICD-10 code to one of the ten PDPM clinical categories using the
**CMS PDPM ICD-10 mapping file** — CMS publishes it (a spreadsheet on the CMS
PDPM web page) and updates it every fiscal year with the ICD-10 code update.
Do not guess the category for ambiguous codes; look the code up or ask the
user to. Watch for:

- **"Return to Provider" codes** — the mapping flags codes too vague to
  support payment (e.g., unspecified codes). If the referral's primary
  diagnosis maps to Return to Provider, flag it: the MDS coordinator must
  identify a more specific/appropriate code before the 5-day MDS.
- **Surgical-procedure adjustment** — some codes map to "May be Eligible for
  One of the Two Orthopedic Surgery Categories" or similar: if a qualifying
  surgical procedure occurred during the preceding hospital stay (coded on the
  MDS in J2100–J5000), the category shifts (e.g., a fracture managed
  surgically moves from Non-Surgical Orthopedic to Orthopedic Surgery; hip
  replacement → Major Joint Replacement or Spinal Surgery). Check the
  operative reports.

Then collapse the category per component: PT/OT use 4 collapsed categories;
SLP only cares whether the category is Acute Neurologic. The collapse tables
are in the reference file.

### Step 4 — Build the Section GG function scores

Construct the PDPM function score from Section GG items (details and the
0–4 point mapping are in the reference file):

- **PT/OT score (0–24):** 2 eating/oral hygiene/toileting-hygiene self-care
  items scored individually, plus averaged bed-mobility, transfer, and walking
  item groups.
- **Nursing score (0–16):** same idea but **excludes walking and oral
  hygiene**.

Pre-admission you rarely have true GG codes, so translate hospital therapy
notes ("min assist x1," "supervision," "dependent," "CGA") into the 0–4 scale,
state the translation you made, and mark the score as estimated. Function
score is the single most common source of estimate error — show a sensitivity
line for the adjacent score band.

### Step 5 — Classify each component

Using [references/pdpm-components.md](references/pdpm-components.md):

1. **PT and OT:** collapsed clinical category × function score band → TA–TP.
2. **SLP:** count the presence of (a) acute neurologic category, (b) an
   SLP-related comorbidity, (c) mild-or-worse cognitive impairment; cross with
   swallowing disorder / mechanically altered diet → SA–SL.
3. **Nursing:** walk the hierarchy top-down (Extensive Services → Special Care
   High → Special Care Low → Clinically Complex → Behavioral/Cognitive →
   Reduced Physical Function); the first qualifying tier wins. Apply the
   nursing function score, depression, and restorative splits.
4. **NTA:** sum comorbidity/service points, map to tier NA–NF. (For a
   documentation-capture workflow that maximizes *legitimately supported* NTA
   points, see the companion `nta-score-capture` skill if installed.)
5. Record the CMI for each group from the user's current-FY final rule tables.

### Step 6 — Apply variable per-diem adjustments and compute the curve

Three components have constant factors (SLP, Nursing, non-case-mix = 1.00 all
days). Two decline or spike:

- **NTA:** factor **3.0 on days 1–3**, then 1.0 from day 4 on. (This front-
  loads payment for medication/supply costs concentrated at admission.)
- **PT and OT:** factor 1.00 for days 1–20, then **declines 2 percentage
  points every 7 days** (days 21–27 = 0.98, 28–34 = 0.96, … days 98–100 =
  0.76).

Compute, for each day 1…expected LOS:

```
day rate = PT_base×PT_CMI×ptot_factor(day)
         + OT_base×OT_CMI×ptot_factor(day)
         + SLP_base×SLP_CMI
         + Nursing_base×Nursing_CMI
         + NTA_base×NTA_CMI×nta_factor(day)
         + NonCaseMix_base
```

using wage-adjusted base rates. Sum for total expected stay revenue; also
report the day-1–3 rate, the day-4–20 rate, and the average per-diem over the
expected LOS (the number most useful for comparing referrals).

Footnote every estimate: these figures are **gross allowable**. Collected cash
≈ allowable minus the **2% Medicare sequestration**, further adjusted by the
facility's **SNF VBP incentive multiplier** — say so when the user compares
the estimate to remittances.

### Step 7 — Present the worksheet, assumptions, and sensitivities

Use the output format below. Every input not directly documented in the packet
must appear in the assumptions list. For sensitivity notes, identify the 2–4
classification decisions closest to a boundary (function score near a band
edge, NTA points near a tier cutoff, an undocumented swallowing disorder,
surgical vs. non-surgical category) and state what documentation would move
them and roughly how it changes the group.

## Output format

Produce exactly this structure:

```markdown
# PDPM Revenue Estimate — [patient initials or referral ID, no full names]
**Estimate only — final classification is determined by the 5-day MDS assessment.**
Payer assumed: Medicare Part A FFS. Expected LOS: [N] days.

## Component worksheet
| Component | Inputs used | Case-mix group | CMI | Wage-adj. base rate | Per-diem $ |
|---|---|---|---|---|---|
| PT | [category] + GG [score] | T_ | [CMI] | [$ or placeholder] | [$] |
| OT | [category] + GG [score] | T_ | [CMI] | [$ or placeholder] | [$] |
| SLP | [factors present] | S_ | [CMI] | [$ or placeholder] | [$] |
| Nursing | [tier + function/depression/restorative] | ___ | [CMI] | [$ or placeholder] | [$] |
| NTA | [points] pts | N_ | [CMI] | [$ or placeholder] | [$] |
| Non-case-mix | — | — | — | [$ or placeholder] | [$] |
| **Total (days 4–20)** | | | | | **[$]** |

Estimated HIPPS pattern: [PT/OT char][SLP char][Nursing char][NTA char][assessment indicator]

## Revenue curve
| Days | PT/OT factor | NTA factor | Per-diem | Segment total |
|---|---|---|---|---|
| 1–3 | 1.00 | 3.00 | [$] | [$] |
| 4–20 | 1.00 | 1.00 | [$] | [$] |
| 21–27 | 0.98 | 1.00 | [$] | [$] |
| [continue through expected LOS] | | | | |
**Estimated total stay revenue: [$] — average per-diem: [$]**

## Assumptions
- [Every value not directly documented in the packet, with the source of the guess]

## Sensitivity notes
- [Boundary-adjacent classifications: what documentation could move them, direction and rough size of the impact]

## Documentation gaps to resolve before the 5-day MDS
- [Missing items that would confirm or improve classification]
```

Never include patient names, dates of birth, or other identifiers in the
output — use initials or the referral ID only.

## Disclaimer

This skill is educational and produces estimates only. PDPM classification is
ultimately determined by the completed MDS assessment, and payment rates,
case-mix indexes, wage indexes, and the ICD-10 mapping change every fiscal
year — verify everything against the current CMS SNF PPS final rule and the
current CMS PDPM classification materials before relying on any figure. This
is not billing, coding, legal, or reimbursement advice.
