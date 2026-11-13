---
name: referral-packet-review
license: MIT
description: Screen an inbound hospital referral packet for a skilled nursing facility (SNF) and produce a structured accept/decline decision memo covering clinical fit, financial fit, red flags, and missing documents. Use whenever the user mentions a referral, hospital packet, discharge packet, admission decision, "should we take this patient", clinical or financial screening of a prospective admission, or asks to review documents sent by a hospital discharge planner or case manager. Also use when the user pastes clinical text (H&P, discharge summary, med list) and wants an admission recommendation or a list of what to request back from the hospital.
---

# Referral Packet Review

Help SNF admissions staff (admissions coordinators, admissions directors, clinical
liaisons) screen an inbound hospital referral and decide whether to accept, decline,
or hold pending more information. The end product is always a **decision memo** in
the exact format under "Output format" below — consistent structure lets teams
compare referrals side by side and hand the memo to a DON or administrator without
rework.

Work in this order: intake → clinical screen → financial screen → red flags &
missing info → decision memo. Do not skip ahead to a recommendation before both
screens are done — a patient can be a perfect clinical fit and still be a decline
on payer terms, or vice versa.

## Step 1 — Intake: get the packet

Ask the user for the referral content in whatever form they have:

- **Pasted text** — face sheet, H&P, discharge summary, med list, therapy notes,
  case-manager message. Any fragment is usable; note what is missing.
- **PDF file paths** — if the user gives file paths, read the PDFs directly.
  Referral packets are often scans; if a PDF has no extractable text, tell the
  user and ask them to paste the key pages instead.
- **A verbal summary** — sometimes the liaison only has a phone report. Proceed,
  but mark every unverified fact as "per verbal report" in the memo.

Also ask up front (these change the whole analysis, so get them early):

1. **Which payer is listed?** (exact plan name as written on the face sheet)
2. **Referring hospital and target discharge date** — urgency drives how hard to
   push on missing documents versus deciding on what is in hand.
3. **Anything the facility already knows it cannot support?** (e.g. no vent
   capability, no bariatric beds) — saves screening time.

If the user has multiple documents, review all of them before analyzing. Newer
documents supersede older ones (a discharge med list beats an admission med list).

## Step 2 — Clinical screen

Extract and assess, in this order:

1. **Diagnoses** — primary reason for the SNF stay, plus active comorbidities.
   Distinguish the *skilled need* (why SNF-level care is required) from background
   history. Medicare-covered SNF care requires a daily skilled nursing or therapy
   need — if you cannot articulate one from the packet, flag it.
2. **Acuity and stability** — recent ICU stay, unresolved infections, pending
   procedures, recent falls, unstable vitals mentioned in notes. A patient who is
   not medically stable for SNF transfer is a hold, not an accept. For very high
   acuity (active vent weaning, ongoing instability), first ask whether the
   patient is SNF-appropriate at all versus LTACH-level care — settle level of
   care before capability screening.
3. **Special care needs** — scan explicitly for each high-impact need:
   IV therapy/central lines, wound care and wound vac, dialysis, ventilator or
   tracheostomy, behavioral/psychiatric needs, bariatric accommodation, isolation
   precautions (MDRO, C. diff, respiratory), tube feeding, oxygen/respiratory
   therapy, and complex medication regimens. Read
   [references/clinical-capability-screen.md](references/clinical-capability-screen.md)
   for the full checklist: what to look for in the packet for each need, and the
   capability question to ask the facility. That file is the authoritative list —
   consult it on every review rather than screening from memory.
4. **Therapy needs and functional status** — prior level of function, current
   mobility/ADL status, anticipated PT/OT/SLP needs, weight-bearing restrictions.
   This matters both clinically (can the patient participate?) and financially
   (therapy drives payment and level-of-care under many contracts).
5. **Cognition and behavior** — dementia, delirium, elopement risk, aggression,
   substance use. These determine unit placement and staffing, and are the most
   commonly under-disclosed items in referral packets.

For every need identified, ask the user whether the facility supports it **before**
finalizing the memo — never assume capability. Phrase it concretely ("Do you have
staff competent to manage a wound vac on all shifts?"), because "we do wound care"
and "we can manage a wound vac 24/7" are different answers. Any need the facility
cannot support is grounds for decline or for negotiating with the hospital (e.g.
"accept after the picc line is removed"). If the user cannot confirm a
capability in time, mark the memo "Capability: UNCONFIRMED" for that need — the
recommendation then cannot exceed "Hold — need more information" or "Accept
pending authorization."

## Step 3 — Financial screen

1. **Classify the payer** from the exact plan name: Medicare FFS (traditional
   Part A), Medicare Advantage, Medicaid FFS, managed Medicaid, commercial,
   VA/other. If the plan name is ambiguous (many MA plans and managed Medicaid
   plans have similar names), say so and tell the user to verify with an
   eligibility check before admission. Read
   [references/payer-screening-guide.md](references/payer-screening-guide.md) for
   the per-payer screening questions, qualifying-stay rules, and prior-auth
   likelihood — use it on every review.
2. **Qualifying stay** — for Medicare FFS, confirm the 3-day inpatient hospital
   stay requirement (observation days do not count) and remaining benefit days.
   Note that CMS waivers and certain ACO/alternative-payment arrangements can
   modify this — tell the user to verify current rules rather than assuming.
3. **Prior authorization** — Medicare FFS generally requires none; MA, managed
   Medicaid, and commercial almost always do. If auth is required and not in the
   packet, the memo's recommendation cannot be "Accept" — at most "Accept pending
   authorization."
4. **High-cost items** — flag anything that erodes margin on a per-diem payment:
   specialty/brand medications (IV antibiotics, anticoagulants, biologics,
   antiretrovirals, oncology drugs), dialysis transport and treatment, wound vac
   rentals, isolation supplies and cohorting costs, bariatric equipment rental,
   1:1 supervision needs. Do not quote drug prices or reimbursement rates —
   they change constantly; instead list the items and tell the user to price them
   against the current contract or PDPM estimate.
5. **Reimbursement drivers** — for Medicare FFS, payment follows PDPM: the
   clinical picture (primary diagnosis mapping, nursing needs, NTA comorbidities,
   function scores) determines the per-diem. Note in the memo which packet facts
   are likely PDPM-relevant. For a deeper analysis, the companion
   **pdpm-estimate** and **nta-score-capture** skills (if installed) can build a
   component-level estimate — suggest them rather than estimating rates yourself.
   Never state dollar figures for rates; refer the user to the current CMS SNF
   PPS final rule, their MAC, or their contracts for numbers.

## Step 4 — Red flags and missing information

Check the packet against this list of commonly missing items. Anything absent goes
in the memo's "Request from hospital" list, worded so the user can paste it
directly into a message to the discharge planner:

- Current medication list (with last-administered times for time-critical meds)
- History & Physical (H&P)
- Discharge summary (or interim summary if not yet discharged)
- Recent physician progress notes
- PT/OT/SLP evaluations and most recent therapy notes
- Insurance card copy (front and back) and any authorization number already obtained
- Code status / POLST / advance directive
- Recent labs (especially if on anticoagulants, antibiotics, or dialysis)
- Wound documentation with measurements and photos if available
- Behavioral health notes if any psychiatric history is mentioned
- Culture results / infection status for any isolation-relevant organism
- Demographics and emergency contact / responsible party
- Court documents if guardianship or conservatorship is referenced

Red flags to call out explicitly (these are the items that most often turn into
post-admission surprises): vague or missing skilled need, a med list that mentions
"see MAR" without the MAR, behavioral history described only in passing, pending
test results, "family issues" noted without detail, a prior SNF stay that ended in
discharge against medical advice or facility-initiated discharge, and any mismatch
between the verbal report and the written record.

## Step 5 — Write the decision memo

Fill in the template below completely. Rules:

- **Recommendation is one of:** Accept / Accept with conditions / Accept
  pending authorization / Hold — need more information / Decline. "Accept with
  conditions" must state the conditions (e.g. "pending auth approval," "after
  picc removal").
- Every risk and every missing item identified in Steps 2–4 must appear in the
  memo — the memo is the paper trail if the decision is questioned later.
- Keep the rationale to a few sentences a busy administrator can read in under a
  minute; put detail in the sections above it.
- Use only information from the packet and the user's answers. Never invent
  clinical facts; write "not documented" where the packet is silent.

## Output format

```markdown
# Referral Decision Memo

**Patient:** [initials or first name + last initial only] | **Referring hospital:** [name]
**Target discharge date:** [date or "not stated"] | **Reviewed:** [today's date]
**Reviewed by:** [user's name/role] with AI assistance

## Patient summary
[2-4 sentences: age/sex if given, primary reason for SNF stay, key comorbidities,
functional status, disposition goal (short-term rehab vs long-term care).]

## Clinical fit
| Need identified | Source in packet | Facility can support? |
|---|---|---|
| [e.g. IV antibiotics via PICC, 10 more days] | [H&P p.2] | [Yes / No / Unconfirmed] |

**Skilled need:** [one sentence stating the daily skilled nursing/therapy need, or "unclear — see risks"]
**Therapy outlook:** [anticipated PT/OT/SLP involvement and functional goals]

## Financial fit
- **Payer:** [plan name as written] — classified as [Medicare FFS / MA / Medicaid / managed Medicaid / commercial / unverified]
- **Qualifying stay (if Medicare FFS):** [met / not met / unverified — details]
- **Prior authorization:** [not required / required — status]
- **High-cost items:** [list, or "none identified"]
- **Reimbursement notes:** [PDPM-relevant facts for FFS; contract/leveling notes otherwise; suggest pdpm-estimate / nta-score-capture skills if a deeper estimate is wanted]

## Risks
1. [Each clinical, financial, or documentation risk, one line each, worst first]

## Missing information — request from hospital
- [ ] [Item 1]
- [ ] [Item 2]

## Recommendation: [Accept / Accept with conditions / Accept pending authorization / Hold — need more information / Decline]
**Conditions (if any):** [list]
**Rationale:** [2-4 sentences tying clinical fit + financial fit + risks to the recommendation]

## Follow-ups
- [ ] [Who does what by when — e.g. "Verify eligibility before transport", "Confirm wound-vac staffing with DON"]
```

After presenting the memo, offer to draft the "request from hospital" message to
the discharge planner as ready-to-send text.

## Disclaimer

This skill is an educational and workflow aid. Verify all coverage, payment, and
regulatory conclusions against current CMS rules (including the current SNF PPS
final rule), your state regulations, and your facility's payer contracts before
acting. Nothing here is clinical, billing, or legal advice; admission decisions
remain the responsibility of the facility's licensed and authorized staff.
