---
name: census-analysis
license: MIT
description: >-
  Turns raw SNF census data (daily/midnight census exports or hand-typed
  numbers) into an operational census brief: occupancy, ADC and payer mix,
  skilled mix, admission/discharge flow, length of stay, trends, red flags,
  and recommended actions. Use whenever the user mentions census, occupancy,
  payer mix, average daily census (ADC), skilled mix, bed management, midnight
  census, admissions/discharges pipeline, backfill, bed holds, or pastes or
  uploads a census spreadsheet. Also use for "how full are we," "are we
  losing Medicare days," or any request to analyze building occupancy trends.
---

# Census Analysis

Turn a facility's census data into a decision-ready brief. The audience is SNF
administrators, admissions directors, and regional ops — often non-technical.
Do the math for them, explain what the numbers mean, and always end with
concrete actions, not just statistics.

## Privacy first

Census data can contain PHI (resident names, MRNs, room-level detail tied to
identity). Before analyzing:

- If a file appears to contain resident names or identifiers, remind the user
  they can strip names/IDs before sharing — aggregate counts are all this
  analysis needs.
- Treat any data provided as confidential. Never echo resident names or
  identifiers back in output. Report only aggregates (counts, percentages,
  averages).

## Step 1 — Gather inputs

Accept either:

1. **A census export** (CSV/Excel — a daily or midnight census report from the
   EHR, e.g. PointClickCare, MatrixCare, Netsmart). Read it with available
   file/spreadsheet tools. Typical columns: date, unit/room/bed, payer,
   admission date, and sometimes anticipated discharge date. Identify the
   date range and whether rows are resident-days or one row per resident.
   Aggregate exports also work: one row per day with payer-count columns
   (date, Medicare, MA, Medicaid, … , total) — no resident-level detail needed.
2. **Typed numbers** — current census, licensed beds, counts by payer,
   admissions/discharges for the period.

Always establish, asking if missing:

- **Licensed beds** — the state-licensed capacity. Distinguish from
  **certified beds** (the Medicare/Medicaid-certified count), which can be
  fewer than licensed.
- **Operational (available) beds** — beds actually in service. These often
  differ: closed wings, rooms converted to private, staffing-limited beds,
  isolation rooms held offline. Occupancy on operational beds is the number
  the team can actually manage to — lenders often use it; surveyors and CMS
  reference certified beds; market reports usually cite licensed. Compute
  licensed and operational at minimum.
- **Target occupancy** (if the user has one) — needed for backfill math.

If only a single day's snapshot is provided, compute point-in-time metrics and
say plainly that trends need at least 2–4 weeks of daily data; offer to analyze
more history if they can export it.

## Step 2 — Core metrics

Compute and show the work (formulas make the brief trustworthy and reusable):

**Occupancy**

- Occupancy % (licensed) = census ÷ licensed beds × 100
- Occupancy % (operational) = census ÷ operational beds × 100
- Over a period, use ADC in the numerator instead of a single day's census.

**Average daily census (ADC)**

- ADC = total resident-days in period ÷ days in period
- Compute overall ADC and ADC by payer.

**Payer mix %** — each payer's ADC ÷ total ADC × 100. Standard buckets:

- Medicare FFS (Part A)
- Medicare Advantage (MA)
- Medicaid (traditional/FFS)
- Managed Medicaid
- Commercial / other insurance
- Private pay
- (Other as present: hospice, VA, respite — keep whatever the data shows.)

Map the facility's payer labels into these buckets; show the mapping if it
required judgment so the user can correct it.

**Skilled mix %** = skilled-level ADC ÷ total ADC × 100, where skilled
typically means Medicare FFS + MA + other insurance paying for skilled care
(commercial skilled, managed care skilled). Skilled mix drives revenue per
patient day in most SNFs, so it gets its own headline number — a building can
hold total occupancy flat while quietly trading skilled days for long-term
custodial days, which is a revenue decline hidden inside a stable census.
Also report **FFS vs MA composition within skilled** — skilled mix alone
scores FFS→MA substitution as flat, and it isn't. Note too that census cannot
see PDPM/case-mix acuity, the adjacent revenue metric — flag it as a separate
analysis, not something this brief measures.

**Flow**

- Admissions per week, discharges per week (include deaths and hospital
  transfers that end the stay), and **net = admits − discharges**. Net tells
  you which way census is drifting even before the ADC line moves.

**Average length of stay (ALOS), by payer**

- Discharge-based (preferred when discharge data exists):
  ALOS = total days of stays that ended in period ÷ number of discharges
- If only census and discharge counts exist, approximate:
  ALOS ≈ ADC ÷ (discharges per day)
- Report by payer. Short and shrinking skilled ALOS with flat admissions means
  fewer skilled days; note it when it appears. Label the method used —
  the two formulas can differ materially. Never quote a blended (all-payer)
  ALOS as skilled ALOS in a mixed building — long-stay custodial residents
  swamp the average; per-payer discharge data is required.

## Step 3 — Trends

With multi-week data:

- **Week-over-week and month-over-month movement** for occupancy, ADC by
  payer, skilled mix, and net admissions. Show direction and size
  (points/percent), not just current values.
- **Payer-mix shift flags.** A skilled mix decline of roughly 2+ points over
  a few weeks is a revenue red flag — flag it and point at the usual causes
  to investigate: referral acceptance rate, hospital referral volume, MA
  authorization denials/short auths, competitors, and discharge timing.
- **Rising long-term/custodial share** while skilled falls: occupancy may look
  healthy while revenue quality erodes — say so explicitly.
- **Volatility**: if daily census swings widely, note it (staffing and
  scheduling implication), and prefer weekly averages for trend claims.

**Discharge pipeline.** If the data includes anticipated/planned discharge
dates, build a 7-day and 14-day forward view: how many residents are expected
to leave, by payer. This converts census from a rear-view metric into a
forecast — the admissions team needs to know today how many beds open next
week.

**Backfill need** — admits per week required to hold a target census. Show
the formula in the brief:

```
Required admits/week = expected discharges/week
                     + (target ADC − current ADC) ÷ weeks to reach target
```

To simply hold current census, the second term is zero: admits must match
discharges. If no anticipated-discharge data exists, use the trailing average
discharges/week as the expected value and say that's the assumption. Compare
required admits/week to the actual recent admit rate — the gap is the
headline for the admissions team.

## Step 4 — Bed management considerations

Raw "beds available" overstates true availability. When the data supports it
(room/unit columns), or as a checklist otherwise, remind the user:

- **Gender/room compatibility** — a semi-private bed is only available to a
  resident compatible with the current occupant; a building can be 90%
  occupied yet unable to place the next male referral.
- **Isolation needs** — beds held for infection precautions or residents
  requiring private rooms reduce effective capacity.
- **Bed holds** — beds reserved during hospital or therapeutic leave. Whether
  and how bed holds are paid **varies by state Medicaid policy and by managed
  care/MA contract** — do not assume; instruct the user to check their state
  rules and specific contracts before counting held beds as revenue or as
  available.
- Distinguish **physically vacant** vs **truly sellable** beds in the brief
  when possible.

## Step 5 — Charting (optional)

If the environment can render and share files, offer a simple trend chart —
occupancy % over time and a stacked payer-mix view are the two that earn
their place. Save as an image or a small self-contained HTML file. Keep it
plain: dates on the x-axis, one or two series, labeled directly.

If charts aren't possible, use a markdown table or a compact ASCII sparkline
(e.g. `Occ%: 88 87 89 91 90 ▁▁▂▃▂`) — never skip the trend view entirely.

## Output format

Produce the brief in exactly this structure:

```markdown
# Census Brief — [Facility name] — [date or period]

## Headline metrics
| Metric | Value | vs prior period |
|---|---|---|
| Census (latest) | 92 | +3 |
| Occupancy % (licensed, 120 beds) | 76.7% | +2.5 pts |
| Occupancy % (operational, 110 beds) | 83.6% | +2.7 pts |
| ADC (period) | 90.4 | +1.8 |
| Skilled mix % | 22.1% | −2.4 pts |
| Admits / Discharges / Net (per wk) | 8 / 9 / −1 | net down 2 |

## Payer mix
| Payer | ADC | Mix % | Trend | ALOS |
|---|---|---|---|---|
| Medicare FFS | ... | ... | ▲/▼/— | ... |
| Medicare Advantage | ... | ... | ... | ... |
| Medicaid | ... | ... | ... | ... |
| Managed Medicaid | ... | ... | ... | ... |
| Commercial | ... | ... | ... | ... |
| Private | ... | ... | ... | ... |

## Trends
- [2–4 bullets: WoW / MoM movement in occupancy, skilled mix, net flow]

## Discharge pipeline & backfill
- Anticipated discharges next 7 days: N (X skilled) · next 14 days: N
- Required admits/week to hold [target]% occupancy: N (formula shown above);
  current admit rate: N/week → gap: ±N

## Red flags
- [Only real ones. e.g. "Skilled mix down 2.4 pts in 3 weeks — revenue risk."]

## Recommended actions
- [Specific and assignable, e.g. "Skilled mix down X pts: review referral
  acceptance rate and denial reasons this week; increase hospital liaison
  touches at top 2 referral sources."]
- [e.g. "Net flow −1/wk: admissions needs 9 admits/wk to hold 88% occupancy."]
```

Rules for the brief:

- Fill every section; if data is missing for one, state what export or number
  would unlock it rather than leaving it blank.
- Round to one decimal for percentages, whole numbers for census counts.
- Red flags must be earned by the data — no boilerplate warnings.
- Recommended actions must tie to a specific metric movement.
- Do not state benchmark dollar figures or "industry average" rates as fact;
  if the user wants comparisons, direct them to their own historical data,
  state cost reports, or market data they have access to.

## Disclaimer

This skill provides educational and operational analysis only. It is not
financial, legal, reimbursement, or clinical advice. Payment rules — including
bed-hold policies, Medicaid rates, and managed care terms — vary by state and
contract; verify against current policies and your own agreements before
acting on any figure produced here.
