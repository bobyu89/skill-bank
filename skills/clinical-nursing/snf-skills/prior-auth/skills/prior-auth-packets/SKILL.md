---
name: prior-auth-packets
license: MIT
description: >-
  Assembles Medicare Advantage / managed-care authorization work products for
  skilled nursing facility (SNF) stays: initial prior-auth packets with
  medical-necessity narratives, concurrent/continued-stay review updates,
  denial triage with peer-to-peer prep and appeal letter drafts, and an
  authorization tracking log. Use whenever the user mentions prior auth,
  authorization, auth request, concurrent review, continued stay, ongoing
  certification, denial, peer-to-peer (P2P), appeal letter, NOMNC,
  medical-necessity letter, InterQual/MCG criteria, auth tracker, or getting
  more days approved from a Medicare Advantage or managed-care plan. Also use
  when the user pastes a denial notice or asks what documents a plan needs to
  approve a SNF admission.
---

# Prior Authorization Packets for SNF Stays

Help SNF admissions and case management staff assemble authorization requests,
continued-stay reviews, and appeals for Medicare Advantage (MA) and
managed-care plans. The user is often non-technical and working against tight
payer deadlines — be concrete, produce ready-to-send drafts, and keep jargon
explained.

## Core rules (apply to every workflow)

1. **Never invent clinical facts.** Every clinical statement in a draft
   (diagnoses, dates, therapy minutes, vitals, functional levels, meds) must
   come from what the user supplied. Anything unknown becomes a
   `[BRACKETED PLACEHOLDER]` for the user to fill in. If the packet would be
   weak without a fact you don't have, ask for it or leave a labeled
   placeholder — do not fill the gap with plausible-sounding content.
2. **No PHI in your own examples.** When illustrating, use invented neutral
   names like "Sample Health Plan" and generic patients. When drafting from
   the user's real facts, use exactly what they gave you.
3. **Deadlines vary.** Plan-specific timeframes (auth turnaround, appeal
   windows, concurrent review cadence) differ by contract and change under
   CMS rules. State typical ranges only as "commonly" / "often," and always
   tell the user to verify against the plan's provider manual, the denial
   notice itself, and current Medicare rules.
4. **Clinician sign-off.** Anything with clinical content (narratives, appeal
   letters, P2P prep) must be reviewed and signed by the responsible
   clinician before submission. Say so when you hand over a draft.

First, figure out which of the four workflows fits. If the user's request is
ambiguous ("help me with this auth"), ask one clarifying question: is this a
**new admission**, a **continued-stay review**, a **denial/appeal**, or
**tracking/organization**?

---

## Workflow A: Initial authorization packet

Goal: a complete request the plan can approve on first pass. Most denials and
delays come from missing documents, so start with the checklist, then draft
the narrative.

### Step 1 — Document checklist

Walk the user through what MA plans typically require. Present as a checklist
they can mark off:

- **Demographics and insurance**: face sheet, member ID, plan name, subscriber
  info, verification of eligibility/benefits.
- **Hospital records**: History & Physical (H&P), discharge summary (or
  interim summary if not yet discharged), relevant consults, recent labs and
  imaging pertinent to the skilled need.
- **Therapy evaluations**: PT/OT/ST evals or hospital therapy notes showing
  functional deficits and tolerance for therapy.
- **Medication list**: current MAR or discharge med list — especially IV
  medications, injections, or complex regimens that themselves justify
  skilled nursing.
- **Skilled-need statement**: physician order for SNF-level care and a clear
  statement of the daily skilled service(s) required.
- **Plan-specific forms**: many plans require their own auth request form or
  portal submission — remind the user to check the plan's provider portal.

Ask which items they already have; flag gaps explicitly.

### Step 2 — Medical-necessity narrative

Gather the clinical facts from the user (hospital course, deficits, prior
level of function, planned services, discharge goal), then draft using the
template in **Output format: Medical-necessity narrative** below. The
structure matters because reviewers (often applying InterQual or MCG
criteria) look for: what skilled service, why it must be daily and
facility-based, the functional delta from baseline, measurable goals, and a
realistic discharge plan. A narrative that answers those five questions in
order is far harder to deny.

Emphasize the **prior vs. current function** contrast — "independent at home,
now max assist x2 for transfers" is the single most persuasive line in most
SNF auth requests, because it shows both the deficit and the realistic
potential to return to baseline.

---

## Workflow B: Concurrent / continued-stay review

Goal: keep an approved stay authorized. Plans approve short spans (often 3–7
days) and require updated clinicals before each extension. The reviewer's
question shifts from "is SNF needed?" to "is the patient still progressing
and still needing daily skilled care?" — so the update must be
progress-focused, not a restatement of the admission narrative.

Gather from the user:

- Progress toward each stated goal since the last review (with numbers where
  possible: assist levels, distances, therapy minutes, participation %).
- Remaining barriers to discharge (clinical and functional).
- Updated discharge plan and target date.
- Therapy attendance/tolerance — plans read missed sessions as "not
  benefiting"; if sessions were missed, capture the clinical reason so the
  narrative can explain it rather than leave it unexplained.

Draft using the **Continued-stay update** template. Then offer to set up or
update the **auth tracker table** (Workflow D template) with the new auth
span and next review due date — missed concurrent-review deadlines are a
leading cause of technical denials, so always surface the next due date
prominently.

---

## Workflow C: Denial response and appeals

### Step 1 — Triage the denial reason

Ask for (or read from a pasted notice) the stated denial reason and classify:

- **Not medically necessary / criteria not met** → strongest paths are
  peer-to-peer and clinical appeal with better-documented facts.
- **Administrative/technical** (late submission, missing documents, no auth
  on file) → correct-and-resubmit or administrative appeal; often faster
  than a clinical fight.
- **Termination of a covered stay** (last covered day / cut notice) → this is
  the NOMNC/QIO lane, which runs on very short timelines — handle same day.

Also capture: date of the notice, stated appeal deadline, whether the patient
is still in-house (drives expedited vs. standard), and whether a
peer-to-peer window is still open (P2P windows are often only 1–3 business
days — verify on the notice).

### Step 2 — Peer-to-peer prep sheet

A P2P is the attending's (or medical director's) call with the plan's medical
reviewer. Prepare a one-page prep sheet so the clinician leads with the
strongest facts instead of narrating the chart. Include:

- The 3–5 key clinical points that establish daily skilled need.
- The functional delta (prior vs. current) in one line.
- **Guideline anchors**: under CMS-4201-F, MA plans must ground SNF coverage
  decisions in **Traditional Medicare coverage criteria** and cannot use
  proprietary criteria (InterQual/MCG) to deny care that meets Medicare
  criteria. Lead with the Medicare skilled-care criteria the patient meets —
  the daily skilled service(s), frequency, and why facility-based care is
  required — then address the plan's InterQual/MCG framework as its secondary
  lens. If the denial cites a specific criterion, address it head-on.
- Anticipated objections ("could be done at a lower level of care") and the
  factual rebuttal for each.
- The specific ask: number of days requested and the review date proposed.

Format as a bulleted sheet the clinician can hold during the call.

### Step 3 — Choose the appeal path (high level)

Explain the lanes briefly, and instruct the user to verify current process
and deadlines from the denial notice and plan materials:

- **Peer-to-peer** — often available before or alongside a formal appeal;
  fastest route when the window is open.
- **Expedited appeal** — when the patient is still receiving the service or a
  delay would jeopardize health; plans must decide quickly (commonly ~72
  hours for MA expedited reconsiderations — verify).
- **Standard appeal** — post-service or non-urgent; longer window and longer
  decision time.
- **NOMNC / QIO route** — when a plan or facility issues a Notice of Medicare
  Non-Coverage ending a covered SNF stay, the beneficiary can request a fast
  review by the **QIO** (Quality Improvement Organization), generally by noon
  of the day before coverage ends. This is a beneficiary right under
  Medicare Advantage rules and is separate from the plan's own appeal
  process. Timelines are extremely short — advise the user to verify the
  current process on the NOMNC form itself and act immediately.
- Note that under MA rules, unfavorable plan-level appeal decisions are
  generally auto-forwarded to an independent review entity — the facility
  should still track the case rather than assume it's over.

### Step 4 — Draft the appeal letter

Use the **Appeal letter** template. The letter must:

- Cite the denial specifics (date, reference number, stated reason).
- Rebut the stated reason directly with the patient's specific facts —
  supplied by the user only; placeholders for anything unknown.
- Map facts to skilled-care requirements (daily skilled service, why not
  feasible at a lower level of care).
- List enclosures.
- End with the specific request (overturn denial, authorize N days) and be
  signed by the responsible clinician.

---

## Workflow D: Auth log hygiene

An accurate tracker prevents the most expensive failure mode: unbilled days
because a review date slipped. For every managed-care stay, track at minimum:

- Patient identifier (per facility policy) and payer/plan name
- Auth number and status (pending / approved / denied / appealing)
- Approved span dates (start–end) and levels/days approved
- **Next review due date** — the field that pays for the whole tracker
- Clinicals-sent date and method (portal / fax / phone)
- Plan contact (name, phone/portal, reference numbers for each call)
- NOMNC issued? (date) and appeal deadlines if in play
- Notes (P2P scheduled, docs requested, etc.)

Offer the markdown tracker in **Output format: Auth tracker table**. Suggest
sorting by next review due date and reviewing it every morning stand-up.

---

## Output format

### Medical-necessity narrative (Workflow A)

```markdown
# Skilled Nursing Facility Authorization Request — Medical Necessity

**Patient:** [NAME] | **DOB:** [DOB] | **Member ID:** [ID]
**Plan:** [PLAN NAME] | **Requesting facility:** [FACILITY]
**Admission date (requested/actual):** [DATE] | **Days requested:** [N]

## 1. Skilled services required
[Daily skilled nursing and/or therapy services, e.g., "PT/OT 5–6x/week for
gait and transfer training; skilled nursing for IV antibiotic administration
q8h" — from user-supplied facts only]

## 2. Why daily, facility-based skilled care
[Why these services require daily delivery in a SNF and cannot safely be
provided at home or a lower level of care — clinical instability, assist
levels, caregiver availability, equipment needs]

## 3. Prior level of function vs. current
- Prior: [e.g., independent with all ADLs, ambulating without device]
- Current: [e.g., max assist x2 transfers, ambulates 10 ft with RW and CGA]

## 4. Goals
[Measurable, time-bound goals, e.g., "supervision-level transfers and 150 ft
ambulation with rolling walker within 14 days"]

## 5. Discharge plan
[Anticipated discharge destination, supports available, estimated length of
stay, barriers being addressed]

Prepared by: [NAME / TITLE]  Reviewed and signed by: [RESPONSIBLE CLINICIAN]
```

### Continued-stay update (Workflow B)

```markdown
# Continued-Stay Review — [PATIENT NAME], Auth #[AUTH NUMBER]

**Review period:** [DATES] | **Current auth expires:** [DATE]
**Days requested:** [N]

## Progress toward goals
| Goal | Status at last review (omit on first review) | Current status |
|---|---|---|
| [Goal 1] | [prior] | [current] |
| [Goal 2] | [prior] | [current] |

## Nursing status
[Daily skilled nursing services still required — e.g., IV medications, wound
care, assessments — and current status]

## Therapy participation
[Disciplines, frequency delivered, minutes, tolerance; explain any missed
sessions with the clinical reason]

## Remaining barriers to discharge
[Specific clinical/functional barriers still requiring daily skilled care]

## Updated discharge plan
[Destination, target date, supports, pending items]

Enclosures: [LIST — updated therapy notes, nursing notes, MAR, orders]

Reviewed and signed by: [RESPONSIBLE CLINICIAN]
```

### Peer-to-peer prep sheet (Workflow C)

```markdown
# Peer-to-Peer Prep — [PATIENT NAME] vs. [PLAN] denial dated [DATE]
**P2P scheduled:** [DATE/TIME] | **Plan reviewer:** [NAME IF KNOWN]
**Denial reason as stated:** [QUOTE FROM NOTICE]

**Key clinical points (lead with these):**
1. [Point]
2. [Point]
3. [Point]

**Functional delta:** Prior [X] → Current [Y]

**Criteria anchors (lead with Medicare coverage criteria per CMS-4201-F;
InterQual/MCG as the plan's secondary framework):**
- [Medicare skilled-care criterion → the fact that meets it]
- [Criterion the denial cited or the reviewer will apply → the fact that meets it]

**Anticipated objections / rebuttals:**
- "[Objection]" → [Factual rebuttal]

**The ask:** [N] additional days, next review [DATE]
```

### Appeal letter (Workflow C)

```markdown
[FACILITY LETTERHEAD]
[DATE]

Sample Health Plan — Appeals Department
[ADDRESS / FAX / PORTAL PER DENIAL NOTICE]

Re: [☐ Expedited ☐ Standard] Appeal of Denial
Member: [NAME], ID [MEMBER ID], DOB [DOB]
Denial date: [DATE] | Reference #: [REF] | Dates of service: [SPAN]

Dear Appeals Reviewer:

[FACILITY] appeals the denial of skilled nursing facility coverage for the
above member. The notice dated [DATE] states the denial reason as:
"[QUOTED REASON]." We respectfully disagree for the following reasons.

**Skilled need.** [User-supplied facts establishing the daily skilled
service(s) — nursing and/or therapy — with specifics.]

**Why a lower level of care is not appropriate.** [User-supplied facts:
assist levels, clinical instability, caregiver/home limitations.]

**Response to the stated denial reason.** [Direct rebuttal of the quoted
reason using the patient's specific facts; address any cited criteria.]

**Progress and prognosis.** [Measurable progress and expected timeline.]

We request that the denial be overturned and [N] days of SNF care be
authorized from [DATE]. Enclosed: [LIST — H&P, discharge summary, therapy
evals/notes, MAR, physician orders, nursing notes].

Please contact [NAME] at [PHONE/EMAIL] with questions.

Sincerely,

[RESPONSIBLE CLINICIAN NAME, CREDENTIALS, TITLE]
```

### Auth tracker table (Workflow D)

```markdown
# Managed-Care Authorization Tracker — updated [DATE]

| Patient | Plan | Auth # | Status | Approved span | Next review due | Clinicals sent | Plan contact / ref # | NOMNC / appeal deadline | Notes |
|---|---|---|---|---|---|---|---|---|---|
| [ID] | Sample Health Plan | [A123] | Approved | [MM/DD–MM/DD] | **[MM/DD]** | [MM/DD, portal] | [Name, phone, ref] | [—] | [P2P pending] |
```

When delivering any draft, remind the user: fill every bracketed placeholder,
have the responsible clinician review and sign, and confirm the plan's
current submission method and deadline before sending.

## Disclaimer

This skill is educational and provides drafting assistance only. All clinical
content must be reviewed, corrected as needed, and signed by the responsible
clinician before submission. Authorization requirements, appeal deadlines,
and review processes vary by plan, by contract, and under current Medicare
rules — always verify against the specific plan's provider materials, the
denial or NOMNC notice itself, and current CMS guidance. Nothing here is
legal or clinical advice.
