---
name: medicare-snf-eligibility
license: MIT
description: >-
  Reason through skilled nursing facility (SNF) coverage before or at admission:
  Medicare Part A benefit-period math, the 3-day qualifying stay, Medicare
  Advantage authorization, Medicaid and Medicaid-pending risk, and payer
  coordination. Use whenever the user mentions eligibility, benefit days,
  qualifying stay, 3-day stay, observation vs inpatient, 30-day transfer rule,
  benefit period, coinsurance days, 100 days, Medicaid pending, share of cost,
  patient liability, prior authorization for a SNF admission, or coverage
  verification for a referral or admission. Produces a structured eligibility
  worksheet with a coverage determination, benefit-days math, risks, and open
  items to verify.
---

# Medicare SNF Eligibility Reasoning

Help SNF admissions and billing staff reason through whether a prospective
admission is covered, by which payer, for how many days, and at what financial
risk — BEFORE the resident is in the building. A wrong call here becomes an
uncollectible stay, so the goal is a defensible, documented determination with
every unverified assumption flagged.

Never guess facts you don't have (dates, plan names, days used). Ask for them
or list them as open items. Never state current-year dollar amounts — they
change annually; always instruct the user to look up the current figure.

## Step 1: Identify the payer situation

Ask (or extract from what the user provided):

1. What coverage does the patient have? Traditional Medicare (FFS) Part A,
   a Medicare Advantage (MA) plan, Medicaid, dual-eligible, commercial,
   or nothing confirmed yet?
2. Where is the patient coming from — hospital inpatient, observation,
   emergency department, home, another SNF?
3. Key dates: hospital admission and discharge dates, planned SNF admission
   date, any prior SNF stays and their dates.

Route the analysis: FFS → Step 2. MA → Step 3. Medicaid or Medicaid-pending →
Step 4. Multiple payers → also do Step 5. Always finish with Steps 6–7.

## Step 2: Medicare FFS Part A analysis

Work through these gates IN ORDER — each one can independently kill coverage.

### Gate 1: 3-day qualifying inpatient hospital stay

Medicare Part A SNF coverage requires a medically necessary INPATIENT hospital
stay of at least 3 consecutive days, counting the admission day but NOT the
discharge day.

**The classic trap: observation days do not count.** A patient can spend four
nights in a hospital bed and have zero qualifying days if they were under
observation (outpatient) status. Always ask: was the patient formally admitted
as an inpatient, and on what date did inpatient status begin? The hospital's
Medicare Outpatient Observation Notice (MOON) and the discharge paperwork show
status. If any of the days were observation, count only the inpatient days.
Beneficiaries reclassified from inpatient to observation may appeal the
reclassification (post-*Barrows v. Becerra* process); a successful appeal can
retroactively create a qualifying stay — verify the current process.

**Waivers exist — check for them.** Some ACO / shared-savings programs, other
CMS waiver models, and many MA plans waive the 3-day requirement. If the
hospital or attending group participates in a SNF 3-day-rule waiver, the stay
may qualify anyway — but the waiver applies only to specific providers and
beneficiaries, so verify participation for THIS patient; never assume it.

### Gate 2: 30-day transfer rule

The SNF admission generally must begin within 30 days of the qualifying
hospital discharge (limited medical-appropriateness exceptions exist). Compute
the gap between hospital discharge and SNF admission. More than 30 days out,
the qualifying stay no longer supports coverage — flag it as a hard risk.

**30-day SNF readmission rule.** A readmission to a SNF within 30 days of
discharge from a prior covered SNF stay needs NO new 3-day qualifying stay —
the stay continues under the same benefit period, using the remaining days.

### Gate 3: Benefit days remaining

Medicare covers up to 100 days of SNF care PER BENEFIT PERIOD, not per year
and not per lifetime:

- **Days 1–20:** Medicare pays in full.
- **Days 21–100:** the beneficiary owes a daily coinsurance. Do NOT quote a
  dollar amount — it changes every year. Instruct the user to look up the
  current-year SNF coinsurance on medicare.gov or from their MAC, and to check
  whether a Medigap/supplement or Medicaid picks it up.
- **After day 100:** no Part A SNF coverage until a new benefit period begins.

**Benefit-period mechanics.** A benefit period starts with inpatient hospital
care **or** covered SNF care (not only an inpatient hospital admission) and
ends only after the beneficiary has gone **60 consecutive days**
without inpatient hospital care or skilled care in a SNF. Only then does the
100-day counter reset (a new qualifying hospital stay is also needed for the
new period). Custodial residence in a nursing facility does not break the
60-day clock by itself, but receiving skilled-level care does.

So you must know: prior hospital and SNF stays, dates, and whether there was a
60-day skilled-care-free gap. Days already used in the current benefit period
come off the 100. Verify actual days used through the eligibility systems
(HETS via your eligibility vendor/clearinghouse, or the MAC portal) — hospital
report and family recollection are not reliable.

### Gate 4: Skilled-need requirement

Coverage requires that the patient needs — and receives — **daily** skilled
nursing or skilled rehabilitation services (skilled **nursing** on a daily
basis means 7 days/week; daily skilled **rehabilitation** alone satisfies the
requirement at 5+ days/week — nursing needed only 5 days/week does not
qualify) that as a practical matter can only be provided in a SNF,
for a condition related to the qualifying stay. Custodial care alone
(bathing, dressing, supervision) is never covered, even with days remaining.
Note: under the Jimmo settlement, skilled care to MAINTAIN function or prevent
decline can qualify — improvement is not required. Flag admissions where the
skilled need looks thin (e.g., stable patient, no therapy orders).

## Step 3: Medicare Advantage analysis

**Eligibility is not authorization.** An MA member can have benefit days
available and the claim still denies because the plan never authorized the
stay. For every MA referral, verify:

1. **Active enrollment and the exact plan** — plans change every January and
   mid-year for some enrollees; confirm the current plan ID, not last year's
   card.
2. **Network status** — is your facility in-network for this specific plan and
   product (HMO vs PPO vs I-SNP)? Out-of-network changes everything.
3. **Prior authorization** — is auth required (usually yes), has it been
   issued, for how many days, and with what concurrent-review cadence? Record
   the auth number, dates approved, and reviewer contact.
4. **Qualifying-stay rules** — most MA plans waive the 3-day inpatient
   requirement, but it is plan-specific. Never assume; confirm with the plan.
5. **Cost sharing** — MA SNF copay structures differ from FFS; get the plan's
   day-band copays from the plan or portal, not from memory.

Treat an MA admission without an auth number as at-risk regardless of what a
discharge planner said verbally.

## Step 4: Medicaid and Medicaid-pending analysis

Medicaid rules vary substantially BY STATE — everything below must be verified
with the specific state's Medicaid agency; do not present it as settled.

For an established Medicaid recipient, verify:

1. **Active eligibility** in the state's verification system, on the admission
   date, in a category that covers nursing facility services.
2. **Level-of-care (LOC) determination** — nursing facility coverage requires
   the state's LOC/medical-necessity determination (often via a state
   assessment process); confirm it is done or initiated, and note PASRR
   screening is a federal precondition to NF admission.
3. **Patient liability / share of cost** — most states apply the resident's
   income (minus a personal needs allowance and other deductions) to the cost
   of care. Compute the expected monthly liability with the state's rules and
   set up collection from day one.
4. **Managed-care enrollment** — if the state runs Medicaid managed care /
   MLTSS, the plan (not the state) may control auth and payment. See Step 5.

**Medicaid-pending admissions** are a business decision to extend credit.
Before accepting one, run this risk checklist:

- **Application status:** Filed or not? With what agency, on what date, and
  who is tracking it? An unfiled application is the highest-risk state.
- **Retroactive eligibility window:** Many states can grant eligibility
  retroactive to some period before the application month, but several states
  have waived or narrowed retroactive coverage — verify the window in YOUR
  state before counting on it to cover admission-date-forward days.
- **Asset picture:** Countable assets near the state limit? Any transfers
  within the lookback period that could trigger a penalty period? A penalty
  period means Medicaid will not pay even after approval.
- **Responsible-party engagement:** Is there a cooperative family member,
  agent under POA, or guardian who will produce documents (bank statements,
  deeds, insurance) promptly? Uncooperative or absent responsible parties are
  the most common reason pending cases die.
- **Income and liability:** Even when approved, the patient liability portion
  must be collectible.

Document the risk decision and who approved it.

## Step 5: Coordination of benefits

- **Medicare primary vs secondary:** Medicare is usually primary for a SNF
  stay, but check for situations where another payer is primary (e.g.,
  liability/no-fault or workers' comp for the admitting condition, or certain
  employer group coverage situations). Query the eligibility response for
  MSP (Medicare Secondary Payer) flags.
- **Dual-eligibles:** Medicare (or the MA plan) pays first; Medicaid may pick
  up coinsurance days 21–100 subject to state rules — verify with the state.
- **Hospice:** If the patient has elected hospice, the hospice benefit covers
  care related to the terminal condition, and SNF **room and board is not a
  Medicare benefit** — it's billed to the hospice (per their contract with
  you), to Medicaid where applicable, or privately. A Part A skilled SNF stay
  for the terminal condition generally cannot run alongside hospice; a
  Part A stay for an unrelated condition is possible but scrutinized.
  Always ask about hospice election before quoting Part A coverage.
- **Managed-care carve-ins:** Some states have moved (carved in) nursing
  facility benefits into Medicaid managed care, and some MA/D-SNP products
  bundle both sides. Identify every plan the patient is enrolled in and which
  one actually pays for NF services.

## Step 6: Verification workflow (every admission)

Check, and save evidence for, each item:

1. **Identity and MBI** — name, DOB, and Medicare Beneficiary Identifier
   exactly as on the card/eligibility response; mismatches cause rejections.
2. **Eligibility response** — run the payer eligibility check (HETS via your
   clearinghouse or MAC portal for FFS; plan portal or 270/271 for MA and
   Medicaid). Save a dated copy/screenshot.
3. **Benefit days remaining and benefit-period status** — from the
   eligibility response, not from the hospital.
4. **Prior stay history** — hospital and SNF stays that drive the qualifying
   stay, the 30-day transfer window, and the 60-day reset math.
5. **Inpatient status proof** — discharge summary or hospital face sheet
   showing inpatient admission date (not observation).
6. **MA plan and authorization** — plan ID, network status, auth number,
   approved dates.
7. **Secondary coverage** — Medigap, Medicaid, or other; who takes the
   coinsurance days.
8. **Hospice election status.**

Save: eligibility screenshots/printouts with dates, auth numbers and names of
plan representatives with date/time of calls, hospital status documentation,
and the completed worksheet (Step 7). If it isn't documented, it didn't
happen when the denial arrives.

### Worked example (fictional dates)

Patient discharged from an inpatient hospital stay 2026-03-10 after being
admitted as inpatient 2026-03-06 (4 inpatient days — qualifying stay met,
even though the first night, 2026-03-05, was observation and does not count).
SNF admission planned 2026-03-12 — 2 days after discharge, inside the 30-day
window. Eligibility response shows 35 SNF days already used in the current
benefit period (a prior SNF stay ended 2026-01-20, and fewer than 60
skilled-care-free days elapsed before the 2026-03-06 hospital admission, so
NO reset occurred).

- Days remaining: 100 − 35 = **65 days**.
- Full-coverage days at this SNF: days 36–? … none — day 20 was passed during
  the prior stay, so **every covered day this stay is a coinsurance day**
  (the patient enters at benefit day 36).
- Coinsurance days available: days 36 through 100 = 65 days at the
  current-year daily coinsurance (look up the current amount; check Medigap/
  Medicaid for pickup).
- Coverage still contingent on daily skilled need being met and documented.

## Output format

Produce the worksheet exactly in this structure, filling what is known and
marking everything unverified:

```markdown
# SNF Eligibility Worksheet — [Patient initials only, no full PHI]
Prepared: [date] | Prepared by: [name/role] | Planned admission: [date]

## 1. Coverage determination
- Primary payer: [FFS Part A / MA plan name / Medicaid / other]
- Determination: [COVERED / COVERED WITH CONDITIONS / NOT COVERED / PENDING]
- Basis: [one or two sentences citing the gates above]

## 2. Qualifying stay & timing (FFS)
- Inpatient admission date: [date] | Discharge: [date] | Inpatient days: [n]
- Observation days excluded: [n / none / UNVERIFIED]
- 3-day stay met: [YES / NO / WAIVED (program: ___) / UNVERIFIED]
- Days from discharge to SNF admission: [n] (30-day rule: [MET / NOT MET])

## 3. Benefit days math
- Days used this benefit period: [n] (source: [eligibility response / UNVERIFIED])
- 60-day reset since last skilled care: [YES / NO / UNVERIFIED]
- Days remaining: 100 − [used] = [n]
- Entering at benefit day: [n] → full-coverage days: [n]; coinsurance days: [n]
- Daily coinsurance: LOOK UP current-year amount | Picked up by: [Medigap /
  Medicaid / patient / UNVERIFIED]

## 4. Authorization & plan checks (MA / managed Medicaid)
- Plan & ID: [ ] | In network: [YES/NO/UNVERIFIED]
- Auth required: [Y/N] | Auth #: [ ] | Approved dates: [ ] | Review cadence: [ ]

## 5. Medicaid / Medicaid-pending risk
- Status: [active / pending / n/a] | Application filed: [date/NO]
- LOC determination & PASRR: [status] | Patient liability est.: [amount/UNVERIFIED]
- Retro window in [state]: [VERIFY with state] | Asset/transfer concerns: [notes]
- Responsible party engaged: [YES/NO] | Risk decision & approver: [ ]

## 6. Coordination
- Secondary coverage: [ ] | MSP flags: [ ] | Hospice election: [YES/NO/UNVERIFIED]

## 7. Risks
- [Bulleted list — each risk with impact, e.g. "Observation status unconfirmed —
  if days 1–2 were observation, qualifying stay fails and stay is not covered."]

## 8. Open items to verify (with source)
- [Item] — [source: plan phone # / plan portal / MAC portal / HETS via
  clearinghouse / state Medicaid agency / hospital HIM]

## Evidence saved
- [List of screenshots, auth numbers, call logs with dates]
```

Fill every section; write "n/a" rather than deleting sections so gaps are
visible. Anything not confirmed against an eligibility system or the payer
must appear in section 8.

## Disclaimer

This skill is educational and summarizes generally applicable, publicly known
Medicare and Medicaid rules. It is not billing, coding, reimbursement, or
legal advice, and rules, amounts, and state policies change. Always verify
coverage and requirements directly with the payer, your Medicare
Administrative Contractor (MAC), the specific health plan, and the state
Medicaid agency before relying on any determination.
