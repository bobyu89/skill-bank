---
name: mds-compliance-calendar
license: MIT
description: >-
  Builds and audits a skilled nursing facility's MDS assessment and regulatory
  reporting calendar: PPS 5-day and IPA windows, the OBRA schedule (admission,
  quarterly, annual, significant change), discharge assessments, PBJ quarterly
  submission deadlines, and how staffing data feeds Five-Star. Use whenever a
  user mentions MDS scheduling, ARDs, assessment windows, late or missed
  assessments, default rate risk, PBJ deadlines, or asks "what assessments are
  due" for a resident, a census list, or a date range. Also use proactively when
  a user shares a resident census with admission dates or a list of completed
  assessments and wants to know whether the facility is compliant.
---

# MDS Compliance Calendar

Build a dated, per-resident assessment schedule from a facility census, and
audit past assessments for missed or late items. The goal is simple: no
assessment should ever surprise the MDS coordinator, because every deadline is
on a calendar with lead time before it hits.

**Why this matters.** MDS timing errors are expensive in three distinct ways:
a late PPS assessment forces billing at the **default rate** (the lowest
payment) for non-covered days; late OBRA assessments are survey citations
(assessment F-tags); and late or failed PBJ submissions can suppress the
facility's Five-Star staffing rating. All three are preventable with a
calendar built from admission dates.

**Currency rule.** Assessment windows, item sets, and PBJ deadlines drift
across RAI manual versions and CMS memos. Treat every rule below as the
publicly known baseline and always tell the user to **verify against the
current MDS 3.0 RAI Manual (Chapter 2 for scheduling) and current CMS PBJ
policy memos** before acting. State-specific assessment requirements (e.g.,
state Medicaid case-mix OBRA rules) are out of scope here — flag them as a
verification item, do not guess. Post-2023, PDPM Medicaid case-mix states use
the **Optional State Assessment (OSA)** — name it in that verification flag.

## Core scheduling rules (public baseline — verify current RAI manual)

### PPS assessments (Medicare Part A stays, PDPM)

- **5-Day assessment**: required for every Medicare Part A stay. ARD
  (Assessment Reference Date) must be set on **days 1–8** of the Part A stay.
  Under PDPM it establishes the payment classification for the entire stay
  unless an IPA is completed.
- **Interim Payment Assessment (IPA)**: **optional**. Complete when the
  facility determines a resident's clinical condition has changed enough that
  the PDPM classification should change. The ARD is any day the facility
  chooses; payment changes from the ARD forward. Because it is optional, put
  it on the calendar as a *clinical trigger review*, not a fixed date.
- **Late 5-Day consequence**: if the ARD is set after day 8, the facility
  bills the **default rate** for the days of the stay not covered by a timely
  assessment. Never present a late 5-Day as merely a paperwork problem — it
  is a direct revenue loss.
- **Medicare Advantage routing**: there is no federal PPS 5-Day for MA
  residents; the OBRA schedule fully applies — check the plan contract for
  its own assessment/level requirements.

### OBRA assessments (all residents regardless of payer)

- **Admission (comprehensive)**: must be **completed by day 14** of the stay
  (admission date = day 1). CAAs (V0200B2) complete by day 14; the
  **comprehensive care plan (V0200C2) is due within 7 days after CAA
  completion** — a separate, later deadline, not the same date.
- **Quarterly**: ARD no later than **92 days after the ARD of the previous
  OBRA assessment**.
- **Annual (comprehensive)**: ARD no later than **366 days after the ARD of
  the most recent comprehensive assessment** (and still within 92 days of the
  last OBRA assessment of any type).
- **Significant Change in Status Assessment (SCSA)**: comprehensive
  assessment completed within **14 days of determining** a significant change
  (improvement or decline) has occurred. An SCSA resets the annual/quarterly
  clock like any comprehensive.
- **Significant correction assessments** (SCPA/SCQA) exist for correcting a
  prior comprehensive/quarterly; mention them in audits when a correction
  pattern appears.

### Discharge and tracking

- **Discharge assessments** (return anticipated / return not anticipated):
  ARD = date of discharge; complete within **14 days after the ARD**
  (Z0500B ≤ ARD + 14).
- **Death in facility** tracking record when a resident dies in the facility.
- **Part A PPS Discharge assessment** when a Medicare Part A stay ends but the
  resident remains in the facility (may be combined with an OBRA discharge
  when the resident physically leaves).

### PPS/OBRA interaction for Medicare stays

For a new Medicare admission, the 5-Day window (days 1–8) sits inside the
OBRA admission window (by day 14). Facilities may **combine** assessments
when the windows overlap and the item set supports it — the combined ARD must
satisfy **both** schedules' rules (use the more restrictive window). When
building a calendar, propose combined assessments where legal because they
reduce workload, but show both underlying deadlines so a slipped ARD is
caught against the tighter one.

### Submission timing

Completed MDS records must be encoded and submitted to CMS (iQIES) on the
RAI-manual timelines (baseline: encode within 7 days of completion, submit
within 14 days of completion). Include submission due dates on the calendar,
not just ARDs — a perfect ARD with a late submission is still non-compliant.

## PBJ (Payroll-Based Journal)

Staffing data is submitted quarterly for **federal fiscal quarters**, due
**45 days after quarter end**. Baseline deadlines (**verify current CMS
dates** — they shift when the 45th day lands on a weekend/holiday and CMS
occasionally grants extensions):

| Fiscal quarter | Period covered | Baseline due date |
|---|---|---|
| Q1 | Oct 1 – Dec 31 | **Feb 14** |
| Q2 | Jan 1 – Mar 31 | **May 15** |
| Q3 | Apr 1 – Jun 30 | **Aug 14** |
| Q4 | Jul 1 – Sep 30 | **Nov 14** |

Put an internal deadline **2+ weeks before** each CMS date on the calendar so
payroll reconciliation and census-day verification happen before submission,
not after a rejection.

## Five-Star connection (why the calendar includes PBJ)

Care Compare's Five-Star rating has three domains: **health inspections**
(survey results), **staffing** (computed from PBJ hours vs. MDS/census-based
resident acuity), and **quality measures** (largely MDS-derived). A missed or
failed PBJ submission, or an audit failure, results in a suppressed or
one-star staffing rating for the quarter. MDS accuracy also flows directly
into QMs. This is why an "assessment calendar" must carry PBJ dates too: the
same rating is damaged by either miss.

## Workflow

### Mode A — Build a forward calendar

1. **Collect inputs**: for each resident — name/identifier, admission date,
   payer (Medicare Part A vs. other), most recent OBRA ARD and type, most
   recent comprehensive ARD, any pending significant-change determinations,
   expected discharge if known. Also today's date and the calendar horizon
   (default: 90 days). Never ask for or retain more resident detail than
   scheduling needs; identifiers/initials are enough — this tool must not
   become a PHI store.
2. **Compute deadlines** per resident using the rules above: 5-Day window end
   (day 8), OBRA admission completion (day 14), next quarterly (prior OBRA
   ARD + 92), next annual (last comprehensive ARD + 366), plus submission due
   dates. Show the arithmetic (e.g., "admitted 3/2 → day 8 = 3/9") so the
   coordinator can verify day-counting; day 1 = admission date.
3. **Propose combinations** where PPS and OBRA windows overlap, using the
   most restrictive window.
4. **Add facility-level items**: the next PBJ due date and a recommended
   internal PBJ deadline.
5. **Flag risk**: mark any deadline within 7 calendar days as AT RISK
   (due-today counts as AT RISK until end of day), any already passed with a
   confirmed missing assessment as OVERDUE, and any already passed where
   completion is unknown as VERIFY-NOW, and state the concrete consequence
   (default rate / citation exposure / staffing-star impact).
6. **Output** using the format below, sorted by due date.

### Mode B — Audit past assessments

1. **Collect inputs**: per resident, the list of completed assessments (type,
   ARD, completion date, submission date if known) plus admission date and
   payer for the period audited.
2. **Check each interval**: 5-Day ARD within days 1–8; admission completed by
   day 14; each OBRA ARD ≤ 92 days after the prior; comprehensive ≤ 366 days;
   discharge assessments present for each discharge; submissions within
   timelines where dates are available.
3. **Classify findings**: `Late` (done outside window), `Missed` (never
   done), `Gap` (interval exceeded between assessments), `Unverifiable`
   (missing data — say exactly what is missing rather than assuming
   compliance).
4. **Quantify impact** where possible: for late/missed 5-Days, list the days
   exposed to default-rate billing; for OBRA misses, note citation exposure.
5. **Output** the same calendar table for the audited period plus a findings
   list, and recommend the fix (e.g., complete now and submit; consult the
   current RAI manual's late-assessment instructions for whether/how to
   complete an out-of-window assessment).

## Output format

Produce exactly this structure:

```markdown
# MDS Compliance Calendar — [Facility] — generated [date]
Horizon: [start] to [end] | Residents reviewed: [n]
Rules baseline: MDS 3.0 RAI Manual (VERIFY current version) + CMS PBJ memos

## Assessment schedule
| Due date | Resident | Assessment | Window / rule | Status | Notes |
|---|---|---|---|---|---|
| 2026-03-09 | R. Smith | PPS 5-Day (ARD by day 8) | Days 1–8; admitted 2026-03-02 | AT RISK | Combine with OBRA Admission if ARD set by 3/9 |
| 2026-03-15 | R. Smith | OBRA Admission (complete) | By day 14 | ON TRACK | CAAs by day 14; care plan within 7 days after CAA completion |
| 2026-05-15 | FACILITY | PBJ Q2 submission | FY quarter + 45 days | ON TRACK | Internal deadline 2026-05-01 |

Status values: ON TRACK / AT RISK (≤7 calendar days; due-today counts as AT
RISK until end of day) / OVERDUE (deadline passed, assessment confirmed not
done) / VERIFY-NOW (deadline passed, completion unknown) / DONE / UNVERIFIABLE

## Risk flags
1. [OVERDUE] [Resident] — [assessment] due [date]: [consequence — e.g.,
   default rate applies to days X–Y; estimated exposure; action to take now]
2. [AT RISK] ...

## Audit findings (Mode B only)
| Resident | Assessment | Required by | Actual | Finding | Impact |
|---|---|---|---|---|---|

## Verify before acting
- Current RAI manual version and any scheduling changes: [items to check]
- Current PBJ deadline for [quarter]: [baseline date] — confirm on CMS PBJ page
- State-specific OBRA/case-mix requirements for [state]: not evaluated here
```

Keep the table sorted by due date, facility-level rows (PBJ) interleaved by
date, and every OVERDUE/AT RISK row echoed in the Risk flags section with its
consequence spelled out — the flags section is what an administrator will
actually read.

For extended window tables and day-counting examples, see
[references/scheduling-reference.md](references/scheduling-reference.md).

## Disclaimer

This skill is educational and reflects publicly available CMS material
(MDS 3.0 RAI Manual structure, PBJ policy, Five-Star methodology) as generally
known; deadlines and rules change. Verify every date and requirement against
the current RAI manual, CMS memoranda, and your state's requirements before
relying on it. This is not legal, regulatory, billing, or clinical advice.
