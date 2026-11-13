# Payer Screening Guide

Use this guide in Step 3 of the workflow. It covers payer classification,
coverage prerequisites, prior-auth likelihood, reimbursement drivers, and
high-cost/margin items. It deliberately contains **no dollar amounts or rates** —
rates change every year and vary by contract. For numbers, direct the user to the
current CMS SNF PPS final rule, their Medicare Administrative Contractor (MAC),
their state Medicaid agency, or their own payer contracts.

## Classifying the payer

Classify from the exact plan name on the face sheet / insurance card. Common traps:

- **"Medicare" alone is ambiguous.** Traditional Medicare (FFS) and Medicare
  Advantage (MA) behave completely differently for SNF coverage. An MA plan often
  carries "Medicare" in its name (e.g. "Sample Health Plan Medicare Complete").
  If in doubt, classify as **unverified** and instruct the user to run an
  eligibility check before admission — enrollment in an MA plan replaces FFS
  billing entirely.
- **Dual eligibles**: a patient can have Medicare (FFS or MA) plus Medicaid.
  Identify the primary payer for the skilled stay and note Medicaid as secondary
  (room-and-board / coinsurance implications, and the long-term-care fallback if
  the skilled stay ends but the patient cannot go home).
- **Managed Medicaid** plans also mimic commercial names. State Medicaid FFS vs a
  managed Medicaid plan changes who authorizes and who pays.
- **Special cases**: VA community care (needs VA authorization), workers' comp
  (needs adjuster approval, often negotiated rates), hospice election (SNF stay
  interacts with the hospice benefit — flag for the billing office), and
  ACO / bundled-payment / institutional special needs plan (I-SNP) arrangements,
  which may change qualifying-stay rules and care-management expectations.

## Per-payer screening

### Medicare FFS (Traditional Part A)

- **Qualifying stay**: generally requires a 3-consecutive-day *inpatient*
  hospital stay (counting midnights, not the discharge day). **Observation days
  and ED time do not count** — the packet's admission order status matters, not
  just the length of the hospital stay. Verify inpatient status explicitly.
  Waivers exist (certain ACOs, I-SNPs, and declared emergencies have modified
  this) — tell the user to verify rather than assume either way.
- **Transfer window**: SNF admission generally must occur within 30 days of
  hospital discharge to use the qualifying stay.
- **Benefit days**: up to 100 SNF days per benefit period; a daily coinsurance
  applies after day 20 (amount changes yearly — look up the current figure).
  Ask whether prior SNF days in this benefit period have been used.
- **Prior auth**: none for the stay itself. Coverage instead hinges on meeting
  the daily-skilled-need criteria and correct assessment/billing — hence the
  emphasis on documenting the skilled need in the memo.
- **Reimbursement**: PDPM per-diem built from case-mix components (PT, OT, SLP,
  nursing, non-therapy ancillary/NTA) plus a non-case-mix piece. Packet facts
  that drive PDPM: the primary diagnosis (maps to a clinical category), surgical
  history from the hospital stay, function scores, swallowing/nutrition issues,
  and NTA-scoring comorbidities (e.g. HIV, IV meds, wounds, morbid obesity,
  diabetes with complications). PT/OT and NTA components pay more early in the
  stay and decline/step down over time, which makes expected length of stay part
  of the margin picture. For component-level estimates, suggest the
  **pdpm-estimate** and **nta-score-capture** skills from this marketplace if
  installed.

### Medicare Advantage (MA)

- **Prior auth**: almost always required before admission, and continued-stay
  reviews follow. No auth number in the packet = at most "Accept pending
  authorization" in the memo.
- **Qualifying stay**: many MA plans waive the 3-day inpatient requirement — plan
  rules govern, not FFS rules. Verify per plan.
- **Reimbursement**: contract-driven — commonly a per-diem by level of care, a
  PDPM-mimicking rate, or case rates. The contract's leveling criteria (therapy
  intensity, nursing complexity) decide the rate tier, so the therapy outlook and
  special care needs from the clinical screen directly determine revenue.
- **Watch for**: short authorized lengths of stay with aggressive concurrent
  review; carve-outs vs all-inclusive per-diems (does the per-diem include
  high-cost drugs? dialysis? transport?). An all-inclusive per-diem plus an
  expensive med list is the classic money-losing admission — put every high-cost
  item in the memo.
- **Network**: confirm the facility is in-network; out-of-network admissions need
  a single-case agreement negotiated **before** transfer.

### Medicaid FFS and managed Medicaid

- **Coverage**: Medicaid is typically the payer for long-term custodial care and,
  in many states, for skilled stays when no Medicare benefit applies. State rules
  vary widely — always defer to the user's state.
- **Prior auth / screening**: managed Medicaid plans generally require prior
  auth. State-level requirements (e.g. PASRR, state level-of-care determinations)
  may also gate admission.
- **Eligibility pitfalls**: pending Medicaid applications ("Medicaid pending")
  mean the facility carries the risk if the application fails — a major financial
  risk to name in the memo. Check for share-of-cost / patient liability amounts.
- **Reimbursement**: state-set or contract per-diems, usually lower than Medicare;
  high-cost meds and services are rarely fully carved out. A heavy clinical
  packet on a Medicaid per-diem deserves explicit margin scrutiny.

### Commercial / employer plans

- **Prior auth**: required in nearly all cases; benefits for SNF care may be
  limited (day caps, rehab-only benefits) — request the benefit summary.
- **Reimbursement**: contract per-diem or case rate; same carve-out questions as
  MA. Out-of-network = single-case agreement before accepting.

## Prior-auth likelihood summary

| Payer type | Prior auth for admission | Typical concurrent review |
|---|---|---|
| Medicare FFS | No | No (coverage criteria + assessments instead) |
| Medicare Advantage | Yes (near-universal) | Yes, often frequent |
| Medicaid FFS | Varies by state | Varies |
| Managed Medicaid | Yes (near-universal) | Yes |
| Commercial | Yes | Yes |
| VA / workers' comp | Yes (authorization/adjuster) | Yes |

## High-cost items to flag (margin erosion on per-diem payment)

List each one found in the packet in the memo's "High-cost items" line; do not
attempt to price them — direct the user to their pharmacy/contract pricing:

- IV antibiotics (especially long courses, daptomycin/ertapenem-class drugs) and
  the associated lab monitoring
- Anticoagulants beyond warfarin, biologics, antiretrovirals, oncology and
  immunosuppressant drugs, specialty inhalers, newer diabetes/obesity injectables
- TPN and specialty enteral formulas
- Dialysis: transport (often several trips/week) and any non-covered treatment cost
- Wound vac rental and advanced wound dressings
- Bariatric equipment rental
- Isolation: private-room opportunity cost, PPE/supplies, cohorting constraints
- 1:1 supervision or sitter needs (pure staffing cost, almost never reimbursed)
- Frequent specialty clinic follow-ups requiring arranged transport
- Blood products / transfusion needs (usually hospital-only — confirm the plan)

## Financial-fit questions to ask the user

1. Is the facility in-network with this plan (or is a single-case agreement needed)?
2. For Medicare FFS: inpatient midnights confirmed? Benefit days remaining known?
3. Has an eligibility/benefits check been run today? (Coverage changes monthly.)
4. Does the contract per-diem include or carve out the high-cost items found?
5. What is the realistic expected length of stay, and does the payer's typical
   authorized length of stay match it?
