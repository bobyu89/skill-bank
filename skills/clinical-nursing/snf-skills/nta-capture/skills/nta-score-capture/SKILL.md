---
name: nta-score-capture
license: MIT
description: >-
  Maximizes legitimate PDPM NTA (Non-Therapy Ancillary) comorbidity capture by
  parsing hospital referral/discharge documentation for the ~50 CMS-published
  NTA conditions and services, producing an evidence-backed capture worksheet
  with point totals, tier, and a documentation-request list. Also audits a
  completed MDS against the packet to find missed points. Use whenever the user
  mentions NTA, non-therapy ancillary, comorbidity capture, missed NTA points,
  PDPM component scoring, or MDS Section I/O/K/M coding for reimbursement — or
  asks to review a hospital packet, H&P, med list, or discharge summary for
  conditions that affect SNF payment.
---

# NTA Score Capture

Help SNF MDS coordinators, billers, and admissions staff find every
**legitimately documented** NTA comorbidity in a hospital packet before the
5-day MDS locks in the score. Accuracy in both directions: never miss a
documented condition, and never suggest coding one that isn't clinically
supported.

## Why NTA matters

NTA is the PDPM component most often under-captured: its evidence is scattered
across med lists, labs, wound and infection notes rather than one assessment
section, so points slip through when nobody reads the whole packet. The point
total maps to a tier (NF–NA) whose case-mix index multiplies the NTA rate for
the **entire stay** — paid at **3x on days 1–3**, 1.0x on days 4–100 — so one
missed 1-point condition can drop the whole stay a tier. The window is short:
most NTA items come from the 5-day PDPM assessment (HIV/AIDS from the SNF
claim), so the review must happen at or immediately after admission.

**Ethics — read this first.** The goal is accurate capture of REAL, documented
conditions — never upcoding. Suggesting a diagnosis that is not in the medical
record, or coding a condition a physician has not documented as active, is
miscoding. Miscoding exposes the facility to MAC/UPIC audits, repayment
demands, and **False Claims Act liability**. Every candidate you surface must
carry a direct quote from the source document, and anything ambiguous goes in
the "needs confirmation" bucket, not the score.

## Reference

Read [references/nta-conditions.md](references/nta-conditions.md) for the full
CMS-published NTA comorbidity list with point values and MDS item sources.
That list reflects the PDPM NTA table as publicly published; item numbers and
mappings **must be verified against the current MDS RAI manual and the current
fiscal year's SNF PPS final rule** before use.

## Workflow: packet capture (default mode)

### Step 1 — Inventory the packet

Identify what documents you have: H&P, discharge summary, medication list /
MAR, labs, wound care notes, respiratory/therapy notes, infection control or
isolation notes, nutrition notes, operative reports. Note what is **missing**
(e.g., no med list, no recent labs) — missing documents become items on the
"documentation to request" list.

### Step 2 — Hunt where NTA conditions hide

Go source-by-source. NTA conditions rarely announce themselves; they hide in
predictable places:

| Where to look | What to find |
|---|---|
| **Medication list / MAR** | IV medications — O0110H counts medication given by **IV access only** (peripheral or central line, IV push or infusion), **while a resident** (5 pts); excluded: IM and SC injections, IV fluids without medication, and line flushes. Also: insulin **plus** the diabetes diagnosis it supports; immunosuppressants (tacrolimus, mycophenolate, cyclosporine) that reveal an undocumented **transplant status**; chemo agents; antiretrovirals suggesting HIV (claim-coded) |
| **Labs** | eGFR/creatinine trends supporting CKD staging and related I8000 diagnoses; albumin/prealbumin supporting malnutrition workup (dx still required); cultures confirming MDRO or C. diff |
| **H&P / problem list / discharge dx** | HIV/AIDS, COPD/asthma/chronic lung disease, diabetes, morbid obesity (BMI + dx), malnutrition, multiple sclerosis, IBD, lupus/connective tissue disease, epilepsy, cirrhosis/end-stage liver disease, heart/lung/kidney transplant history |
| **Wound documentation** | Stage 4 pressure ulcer, diabetic foot ulcer, other foot infection/open lesion, wound infection, severe burns; ostomy presence |
| **Infusion / IV therapy records** | IV fluids or IV meds given, dates relative to admission; parenteral nutrition (TPN/PPN) and the proportion of intake it supplies (high vs. low intensity) |
| **Respiratory notes** | Ventilator/respirator use, tracheostomy care, suctioning, oxygen at admission (supports chronic lung disease coding context) |
| **Infection / isolation notes** | MDRO (MRSA, VRE, CRE, ESBL), single-room isolation for active infection, C. difficile, history of septicemia, wound infections, opportunistic infections |
| **Nutrition notes** | Feeding tube, parenteral/IV feeding, malnutrition dx from a dietitian assessment (needs physician documentation to code I5600) |

Match every hit against the reference list. Cast a wide net here — filtering
happens in Step 3.

### Step 3 — Build the candidate table with evidence

For each candidate condition record:

1. **Evidence quote** — the exact sentence/line from the packet, with document
   and date. No quote, no candidate.
2. **MDS source item** — where it would be coded: Section I active diagnoses
   (I1300–I8000), Section O special treatments (O0110), Section K nutritional
   approaches (K0520 / intake proportions), Section M skin (M0300, M1040),
   Section H appliances (H0100), or the **SNF claim** (HIV/AIDS via ICD-10
   B20 — not an MDS item). Section GG does not feed NTA but note function
   items if the packet supports them.
3. **Status** — `Documented` (clear, active, physician-documented, meets the
   MDS lookback/active-diagnosis rules) or `Needs confirmation` (mentioned but
   ambiguous: "history of" without active management, dietitian-only
   malnutrition note, resolved infection, med without matching dx).

Apply the RAI "active diagnosis" discipline: a Section I diagnosis must be
physician-documented (or by an authorized licensed practitioner) in the
lookback and have a direct relationship to current status — a stale problem
list entry alone is not enough. Say so explicitly when that is the gap.

### Step 4 — Score and tier

Sum points for **Documented** items only. Report two totals: confirmed, and
potential (confirmed + needs-confirmation). Map to the tier:

| NTA points | Tier |
|---|---|
| 12+ | NA |
| 9–11 | NB |
| 6–8 | NC |
| 3–5 | ND |
| 1–2 | NE |
| 0 | NF |

If a needs-confirmation item would change the tier, flag it prominently —
that is where a documentation request has direct payment impact. Do not quote
dollar amounts; tell the user to apply the current FY final rule's NTA
case-mix indexes and rates.

### Step 5 — Documentation to request

List concrete asks, each tied to a candidate: e.g., "Physician documentation
that malnutrition is an active diagnosis (dietitian note dated X supports it)",
"Clarify transplant history implied by tacrolimus on the med list", "Confirm
IV medication administration dates fall within the MDS lookback".

## Workflow: missed-points audit mode

When given a completed MDS coding summary **plus** the packet:

1. Run Steps 1–3 above on the packet independently — do not anchor on what
   was coded.
2. Diff your candidate table against the MDS: conditions documented in the
   packet but **not captured** on the MDS are the findings.
3. For each miss, state the evidence quote, the MDS item it belongs on, and
   the point value. Also flag the reverse: anything **coded on the MDS with no
   supporting evidence in the packet** is an audit risk and should be verified
   against the full record.
4. Note whether a modification/correction of the assessment is worth pursuing
   per RAI correction policy (the user decides with their RN Assessment
   Coordinator; do not assert it is permissible for their specific case).
5. Use the same output format, adding a `Coded on MDS?` column.

## Output format

Produce exactly this structure:

```markdown
# NTA Capture Worksheet — [Patient A / identifier provided] — [date]

Documents reviewed: [list]
Documents missing: [list or "none noted"]

## Candidate conditions

| Condition (NTA list name) | Points | Evidence (quoted, source + date) | MDS source item | Status |
|---|---|---|---|---|
| Diabetes Mellitus | 2 | "A1c 8.2; continue insulin glargine" — Discharge summary, 6/1 | I2900 | Documented |
| Malnutrition | 1 | "moderate protein-calorie malnutrition per RD" — Nutrition note, 5/30 | I5600 | Needs confirmation — requires physician documentation |
| ... | ... | ... | ... | ... |

## Score

- Confirmed NTA points: [n] → Tier [NF/NE/ND/NC/NB/NA]
- Potential with confirmations: [n] → Tier [x]
- Tier-changing items: [list or "none"]

## Documentation to request

1. [Specific ask, tied to condition + evidence]
2. ...

## Notes

- [Lookback-window cautions, ambiguities, audit-risk flags]
- Verify all point values, item numbers, and case-mix indexes against the
  current MDS RAI manual and the current FY SNF PPS final rule.
```

In audit mode, add a `Coded on MDS?` column and a "## Missed points" section
summarizing the delta (points and tier before/after).

## Disclaimer

This skill is educational. All MDS coding must be supported by the medical
record and clinician judgment; never code conditions that are not clinically
documented. Point values, item numbers, tier thresholds, and case-mix indexes
change — verify everything against the current MDS RAI manual and the current
fiscal year CMS SNF PPS final rule. This is not billing, coding, or legal
advice.
