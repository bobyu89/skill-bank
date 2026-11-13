# PDPM Component Classification Reference

Read this file when actually classifying a patient into PDPM case-mix groups.
Structures below follow the publicly documented CMS PDPM methodology (see the
CMS PDPM web page: fact sheets, the PDPM classification walkthrough, and the
annual SNF PPS final rule). Group *structures* are stable since PDPM's 2019
start, but **CMIs, ICD-10 mappings, and any boundary CMS revises are FY-
specific — where noted, verify against the current CMS PDPM classification
walkthrough and final rule.**

## 1. PDPM clinical categories (from primary diagnosis)

The primary SNF diagnosis (MDS I0020B) maps via the CMS ICD-10-to-clinical-
category mapping file (published and updated each FY on the CMS PDPM page) to
one of ten categories:

1. Major Joint Replacement or Spinal Surgery
2. Cancer
3. Non-Surgical Orthopedic/Musculoskeletal
4. Orthopedic Surgery (Except Major Joint Replacement or Spinal Surgery)
5. Acute Infections
6. Cardiovascular and Coagulations
7. Pulmonary
8. Non-Orthopedic Surgery
9. Acute Neurologic
10. Medical Management

Notes:
- Some codes map to **"Return to Provider"** — not payable as primary; a more
  specific code is needed.
- Some codes are **surgery-conditional**: the final category depends on
  whether a qualifying surgical procedure occurred during the preceding
  hospital stay (MDS items J2100–J5000). E.g., a fracture treated surgically
  classifies as Orthopedic Surgery rather than Non-Surgical Orthopedic; hip or
  knee replacement and spinal fusion land in Major Joint Replacement or
  Spinal Surgery.

**Collapse for PT/OT** (10 → 4):

| PT/OT collapsed category | Includes clinical categories |
|---|---|
| Major Joint Replacement or Spinal Surgery | Major Joint Replacement or Spinal Surgery |
| Other Orthopedic | Orthopedic Surgery (Except Major Joint); Non-Surgical Orthopedic/Musculoskeletal |
| Medical Management | Medical Management; Acute Infections; Cancer; Pulmonary; Cardiovascular and Coagulations |
| Non-Orthopedic Surgery and Acute Neurologic | Non-Orthopedic Surgery; Acute Neurologic |

**Collapse for SLP** (10 → 2): Acute Neurologic vs. Non-Neurologic (all
others).

## 2. Section GG function scores

### Item-to-points mapping (each GG item → 0–4)

| GG response code | Points |
|---|---|
| 05 Setup/clean-up assistance, or 06 Independent | 4 |
| 04 Supervision or touching assistance | 3 |
| 03 Partial/moderate assistance | 2 |
| 02 Substantial/maximal assistance | 1 |
| 01 Dependent; 07 refused; 09 not applicable; 10 not attempted (environmental limitation); 88 not attempted (medical/safety) | 0 |

For walking items only, an "activity not attempted" coding pathway can also
yield 0 via the walking gateway questions.

### PT/OT function score (0–24)

Sum of:

| Score element | GG items | How counted |
|---|---|---|
| Eating | GG0130A | single item |
| Oral hygiene | GG0130B | single item |
| Toileting hygiene | GG0130C | single item |
| Bed mobility | GG0170B (sit to lying), GG0170C (lying to sitting on side of bed) | average of the 2 |
| Transfer | GG0170D (sit to stand), GG0170E (chair/bed-to-chair), GG0170F (toilet transfer) | average of the 3 |
| Walking | GG0170J (walk 50 ft, 2 turns), GG0170K (walk 150 ft) | average of the 2 |

Six elements × up to 4 points = 0–24. Use the admission-performance codes
from the 5-day MDS (pre-admission: your translated estimate).

### Nursing function score (0–16)

Same elements **excluding walking and oral hygiene**: eating + toileting
hygiene + bed-mobility average + transfer average (4 elements × 4 = 0–16).
**Verify the exact nursing-score item list against the current CMS PDPM
classification walkthrough** before relying on a boundary case.

## 3. PT and OT case-mix groups (TA–TP)

Grid: collapsed clinical category × PT/OT function score.

| Collapsed category | GG 0–5 | GG 6–9 | GG 10–23 | GG 24 |
|---|---|---|---|---|
| Major Joint Replacement or Spinal Surgery | TA | TB | TC | TD |
| Other Orthopedic | TE | TF | TG | TH |
| Medical Management | TI | TJ | TK | TL |
| Non-Orthopedic Surgery and Acute Neurologic | TM | TN | TO | TP |

PT and OT use the same grid and land in the same-letter group; their CMIs
differ. Within each category, note the general (not universally monotonic)
pattern: mid-range function scores often carry the highest therapy CMIs.
**Verify score-band boundaries against the current CMS PDPM classification
walkthrough.**

## 4. SLP case-mix groups (SA–SL)

Two axes:

**Axis 1 — count of SLP-related clinical factors present (0–3):**
1. Primary clinical category is **Acute Neurologic**
2. An **SLP-related comorbidity** is present (CMS list — e.g., aphasia,
   dysphagia-related neurologic conditions, CVA/TIA, hemiplegia, TBI,
   tracheostomy or ventilator while a resident, laryngeal/oral cancers,
   apraxia, ALS; see the current CMS list for the full set)
3. **Cognitive impairment** (mild or worse, per the PDPM cognitive level from
   BIMS/staff assessment)

**Axis 2 — mechanically altered diet (K0510C2) and/or swallowing disorder
(K0100):** Neither / Either one / Both.

| Factors present | Neither | Either | Both |
|---|---|---|---|
| None | SA | SB | SC |
| Any one | SD | SE | SF |
| Any two | SG | SH | SI |
| All three | SJ | SK | SL |

CMI rises down and to the right; SL is the highest SLP group.

## 5. Nursing case-mix groups (25 groups, ES3…PA1)

Walk the hierarchy **top-down; first qualifying tier wins**. Uses the nursing
function score (0–16), depression (PHQ-9 based, per the MDS), and count of
restorative nursing programs (2+ = "with restorative").

| Tier (top → bottom) | Qualifiers (summary) | Groups |
|---|---|---|
| Extensive Services | Tracheostomy care, ventilator/respirator, or infection isolation while a resident (function score ≤ 14) | ES3 (trach **and** vent), ES2 (trach or vent), ES1 (isolation) |
| Special Care High | E.g., comatose; septicemia; diabetes with daily injections + insulin order changes; quadriplegia (with low function); COPD with shortness of breath lying flat; parenteral/IV feedings; respiratory therapy 7 days; fever with pneumonia/vomiting/weight loss/feeding tube | HDE2/HDE1 (function 0–5, with/without depression), HBC2/HBC1 (function 6–14) |
| Special Care Low | E.g., cerebral palsy/MS/Parkinson's with low function; respiratory failure with oxygen; feeding tube meeting intake criteria; stage 2+ pressure ulcers (2 or more) or stage 3–4 with skin treatments; foot infection/wound with treatment; radiation or dialysis while a resident | LDE2/LDE1 (0–5), LBC2/LBC1 (6–14) |
| Clinically Complex | E.g., pneumonia; hemiplegia with low function; surgical wounds or open lesions with treatment; burns; chemotherapy, oxygen, IV medications, or transfusions while a resident | CDE2/CDE1 (0–5), CBC2/CBC1 (6–14), CA2/CA1 (15–16) — 2 = with depression |
| Behavioral Symptoms & Cognitive Performance | Severe cognitive impairment or behavioral symptoms (hallucinations, delusions, physical/verbal behaviors, rejection of care, wandering), function 11–16 | BAB2/BAB1 (2 = with 2+ restorative programs) |
| Reduced Physical Function | None of the above | PDE2/PDE1 (0–5), PBC2/PBC1 (6–10), PA2/PA1 (11–16) — 2 = with 2+ restorative programs |

Endings: in the D/B/A letter pairs the middle letters encode the function
band; the trailing digit encodes depression (Special Care/Clinically Complex)
or restorative count (Behavioral/Reduced Physical Function). Tier qualifier
details and exact function cutoffs are FY-rule material — **verify against
the current CMS PDPM classification walkthrough**. An AIDS diagnosis adds a
statutory add-on to the nursing component rate (see the final rule).

## 6. NTA component (NA–NF)

Sum points for each qualifying comorbidity/service (from MDS items and coded
diagnoses), then map:

| NTA points | Group |
|---|---|
| 12+ | NA |
| 9–11 | NB |
| 6–8 | NC |
| 3–5 | ND |
| 1–2 | NE |
| 0 | NF |

Point values (summary of the CMS list of ~50 conditions/extensive services,
as originally published — **verify current FY**):

| Points | Conditions / services |
|---|---|
| 8 | HIV/AIDS (coded on the SNF claim, not the MDS) |
| 7 | Parenteral/IV feeding — high intensity |
| 5 | IV medications while a resident (O0110H) |
| 4 | Ventilator/respirator while a resident (O0110F) |
| 3 | Parenteral/IV feeding — low intensity; lung transplant status |
| 2 | Transfusions while a resident (O0110I); major organ transplant status except lung; multiple sclerosis; opportunistic infections; asthma/COPD/chronic lung disease; bone/joint/muscle infections or necrosis (e.g., osteomyelitis); chronic myeloid leukemia; wound infection; diabetes mellitus |
| 1 | The long tail — e.g., endocarditis, morbid obesity, stage 4 pressure ulcer, diabetic foot ulcer, tracheostomy care while a resident, isolation while a resident, radiation while a resident, multi-drug-resistant organism, immune disorders, end-stage liver disease, cystic fibrosis, and others |

Two frequent scoring mistakes to avoid: diabetes, COPD/asthma, and wound
infection are worth **2 points each** (not 1), and transfusions count **2
points and only while a resident** — a transfusion given in the hospital
before SNF admission earns nothing.

The full CMS list, its MDS item sources, and per-condition capture guidance
are beyond this summary — **see the companion `nta-score-capture` skill (if
installed) for the complete table and capture workflow**, and verify point
values against the current CMS PDPM classification walkthrough / RAI manual.

## 7. Where the numbers come from each year

- **Base rates (urban/rural), labor-related share, wage indexes, CMIs:** the
  annual CMS SNF PPS final rule (effective each October 1). Never reuse a
  prior year's figures.
- **ICD-10 → clinical category mapping and SLP/NTA comorbidity code lists:**
  the FY mapping files on the CMS PDPM web page.
- **Classification logic details:** the CMS PDPM classification walkthrough
  and MDS 3.0 RAI manual.
