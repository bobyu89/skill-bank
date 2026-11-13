---
name: contract-analysis
license: MIT
description: >-
  Analyze skilled nursing facility (SNF) managed-care contracts: extract terms
  into a structured contract summary sheet, level patients against a contract's
  level grid with evidence per criterion, and prepare negotiation-points memos
  that flag SNF-unfavorable terms. Use whenever the user mentions a payer
  contract, managed care agreement, rate sheet, per-diem levels, carve-outs,
  exclusions, leveling a patient, authorization or concurrent review terms,
  timely filing, lesser-of language, a single case agreement, or contract
  negotiation or renewal — even if they only paste contract text or ask "what
  level is this patient?" without naming the contract. Also use when reviewing
  a proposed amendment or comparing a draft contract against current terms.
---

# SNF Managed-Care Contract Analysis

Help SNF administrators, regional directors of managed care, and billers
understand what a managed-care contract actually says, place patients at the
correct level under it, and prepare for negotiations. Many users are
non-technical and non-legal: write plainly, define jargon on first use, and
point them to `references/contract-terms-glossary.md` when a term needs more
depth than the output allows.

Three workflows live in this skill. Pick the one that matches the request:

| User asks... | Workflow |
|---|---|
| "Summarize this contract" / "What are the terms?" / pastes a contract | **A — Term extraction** |
| "What level does this patient qualify for?" / "Level this admission" | **B — Patient leveling** |
| "What should we push back on?" / "Prep me for the renewal meeting" | **C — Negotiation prep** |

Workflows B and C both depend on the terms extracted in Workflow A. If the
user jumps straight to B or C without a contract summary, run the relevant
parts of Workflow A first (quietly — don't produce the full summary sheet
unless asked, but do show the level grid or the terms you relied on, so the
user can verify you read the contract correctly).

## Ground rules (apply to every workflow)

- **Quote, don't paraphrase, for anything load-bearing.** Rate methodology,
  level criteria, deadlines, and termination language should be quoted verbatim
  with a section/page reference. Paraphrase drifts; a biller acting on a
  paraphrase can miss a filing deadline or bill the wrong level. When a page or
  section number is available, cite it.
- **Flag silence explicitly.** What a contract *doesn't* say is often the most
  important finding (no escalator, no high-cost drug carve-out, no retro-auth
  provision). Every output template below has a place for "not addressed in
  contract" — use it. Never fill a gap with an industry-typical assumption
  presented as if it were in the contract.
- **Never invent numbers.** Rates, thresholds, and deadlines come only from
  the document in front of you. If asked what a "typical" or "market" rate is,
  explain that rates vary widely by market, payer, and acuity mix and that
  benchmark figures should come from the facility's own comparable contracts
  or market data — do not supply a figure.
- **No PHI in outputs beyond what the task needs.** For leveling, work from
  the clinical facts given; don't ask for or restate identifiers (name, DOB,
  SSN, member ID) — refer to "the patient."
- **Ambiguity is a finding, not an obstacle.** Vague contract language
  ("skilled nursing services as appropriate") is exactly what causes level
  disputes and denials. Call it out, show both plausible readings, and say
  which party the ambiguity favors.

---

## Workflow A — Contract term extraction

**Goal:** turn a contract PDF or pasted text into a summary sheet a busy
administrator can act on, and a biller can pin above their desk.

### Steps

1. **Read the whole document before extracting anything.** Contracts scatter
   related terms: the rate exhibit may be Amendment 3, the level definitions
   in Attachment B, and the lesser-of clause buried in the payment section.
   Amendments and exhibits override the body — note the controlling version
   of any term that appears more than once, and flag conflicts between body
   and exhibit.
2. **Extract into the categories below.** For each: the substance, a verbatim
   quote of the operative language, and the location. Mark anything absent as
   "Not addressed in contract."
   - **Parties & dates** — legal entities, effective date, initial term,
     renewal mechanics (evergreen/auto-renew? notice window to non-renew?),
     termination (with cause / without cause, notice periods, and whether
     termination rights are mutual or one-sided).
   - **Rate methodology** — identify which model applies: per-diem level grid,
     RUG-based, PDPM-based, percent-of-Medicare (state the percentage and
     which Medicare fee schedule year it references — a fixed year silently
     erodes value), case rates, or a hybrid. Reproduce the full rate grid.
   - **Level definitions & qualifying criteria** — for each level, the exact
     qualifying criteria as written. This is the raw material for Workflow B,
     so completeness matters more here than anywhere else. Note whether
     criteria are objective (e.g., "receiving IV antibiotics") or judgment
     terms (e.g., "complex wound care"), and who decides when they're met.
   - **Carve-outs & pass-throughs** — high-cost drugs (threshold amount, per
     dose or per day, what documentation triggers it), dialysis, ventilator,
     bariatric, behavioral, transportation, DME. For each: paid in addition to
     the per diem, or in lieu of it? At cost, cost-plus, or a stated rate?
   - **Exclusions** — services the SNF must not bill the payer for, and
     whether the contract says who *is* responsible (patient? unaddressed?).
   - **Authorization & concurrent review** — initial auth requirement and
     turnaround, recertification/concurrent review cadence, how continued-stay
     denials are communicated, retro-auth rules (allowed at all? window?),
     and what happens to days between auth expiry and re-auth.
   - **Claims & timely filing** — filing deadline (from date of service or
     discharge?), clean-claim definition, required claim format/codes,
     prompt-pay commitment, and the resubmission/corrected-claim window.
   - **Denials & appeals** — levels of appeal, deadline for each, where
     appeals go, whether the contract allows external review or arbitration,
     and any "failure to appeal within X days waives" language.
   - **Rate escalators** — annual increase (fixed %, CPI-linked, or
     renegotiation-only), and what happens on auto-renewal (rates frozen?).
   - **Lesser-of language** — any clause paying the lesser of contract rate
     vs. billed charges (see glossary: this makes the chargemaster a rate
     ceiling), and any most-favored-nation or rental-network/silent-PPO
     language letting other entities access these rates.
   - **Patient responsibility** — copay/coinsurance/patient-days handling,
     who collects, and whether the payer's payment is net or gross of it.
3. **Produce the summary sheet** using the Output format template. Lead with
   the three to five terms most likely to cost the facility money if missed.

### Output format — Workflow A

ALWAYS use this exact template:

```markdown
# Contract Summary Sheet
**Payer:** [name] | **Facility:** [name] | **Effective:** [date] | **Prepared:** [date]
**Documents reviewed:** [base contract + amendments/exhibits, with dates]

## Top findings (read these first)
1. [Highest-impact term or gap, one sentence + why it matters]
2. ...

## Term & termination
| Item | Provision | Source |
|---|---|---|
| Effective date / initial term | ... | §/p. |
| Renewal | ... | §/p. |
| Termination without cause | ... | §/p. |
| Termination with cause | ... | §/p. |

## Rates
**Methodology:** [per-diem levels / RUG / PDPM / % of Medicare / case rate / hybrid]
[Rate grid reproduced verbatim]
**Escalator:** [provision or "Not addressed in contract"]
**Lesser-of / rate-access language:** [quote or "None found"]

## Level definitions
| Level | Qualifying criteria (verbatim) | Objective or judgment-based? | Source |
|---|---|---|---|

## Carve-outs & pass-throughs
| Item | Trigger/threshold | Payment basis | In addition to per diem? | Source |
|---|---|---|---|---|
[Include rows marked "Not addressed" for: high-cost drugs, dialysis,
ventilator, bariatric, transportation]

## Exclusions
[List, with who bears the cost if stated]

## Authorization & review
| Item | Provision | Source |
|---|---|---|
| Initial authorization | | |
| Concurrent review cadence | | |
| Retro authorization | | |

## Claims, denials & appeals
| Item | Deadline/Provision | Source |
|---|---|---|
| Timely filing | | |
| Clean claim definition | | |
| Appeal level 1 / 2 | | |

## Patient responsibility
[Provision]

## Gaps & ambiguities
[Everything marked "Not addressed" or vague, one line each on the risk]
```

---

## Workflow B — Patient leveling

**Goal:** given the contract's level grid and a patient's clinical picture,
determine the level the patient qualifies for — with evidence the facility
could hand to the payer's reviewer.

The integrity constraint comes first: **never inflate.** The job is to make
sure the facility is paid for the acuity it is actually delivering — patients
are frequently *under*-leveled because staff default to the safe low level —
but a level must be earned by documented clinical fact. If the evidence
supports Level 2, say Level 2, even if the user hoped for Level 3. An
unsupported higher level is a takeback and a payer-relations problem waiting
for the next audit.

### Steps

1. **Get the level grid.** From a prior Workflow A summary, or extract it now
   from the contract. If the user provides neither, stop and ask — leveling
   against a generic notion of "levels" is meaningless because criteria are
   contract-specific.
2. **Map every criterion of every plausible level against the clinical
   picture.** Work top-down from the highest plausible level. For each
   criterion record: met / not met / unknown, and the specific clinical
   evidence (order, medication, treatment, therapy minutes, nursing task).
   "Unknown" is common and important — it usually means the chart supports
   the level but nobody wrote it down.
3. **Handle judgment-based criteria explicitly.** Where the contract says
   something vague ("complex care," "extensive services"), state the
   reasonable interpretation you applied and note that the payer may read it
   differently. This is where concurrent-review disputes are born.
4. **Determine the qualifying level** per the contract's own combination rule
   (some grids require ALL criteria at a level; others ANY one; others a
   count — quote the rule). If the contract is silent on the combination
   rule, flag that as an ambiguity and show the result under both readings.
5. **Build the documentation checklist for the defensible level.** For each
   supporting criterion, name the exact chart element that proves it
   (physician order dated..., MAR entry showing..., wound-care flow sheet,
   therapy minutes log). For each "unknown," name what would need to be
   documented — *if clinically true* — to support it. Frame these as
   documentation of existing care, never as care to add for billing's sake.

### Output format — Workflow B

ALWAYS use this exact template:

```markdown
# Level Determination
**Contract:** [payer/contract id] | **Determination:** **Level [X]** | **Confidence:** [High/Medium/Low + one-line reason]

## Criteria analysis
### Level [highest plausible] — [qualifies / does not qualify / cannot determine]
| Criterion (verbatim from contract) | Met? | Evidence |
|---|---|---|
| ... | Met / Not met / Unknown | ... |
[Repeat per level evaluated, highest first]

**Combination rule applied:** [quote, or "Contract silent — see ambiguities"]

## Ambiguities affecting this determination
[Each vague criterion: your reading, the payer's likely reading, which level
each reading yields]

## Documentation checklist to support Level [X]
- [ ] [Chart element] — supports "[criterion]"
- [ ] ...

## If clinically justified, to support Level [X+1] the chart would need
[Only include this section when "unknown" criteria plausibly reflect care
actually being delivered. Each item: what to document, which criterion it
satisfies. Note: document care that is happening — never add services or
wording solely to reach a level.]
```

---

## Workflow C — Negotiation prep

**Goal:** compare extracted terms against the checklist of SNF-unfavorable
provisions and produce a memo the administrator can take into the meeting.

### The unfavorable-terms checklist

Screen the contract for each of these. For every hit, the memo needs three
things: the quoted language, *why it hurts the facility* (in operational or
financial terms a non-lawyer can repeat in a meeting), and a concrete ask.

1. **Silent PPO / rental network language** — clauses letting the payer lease
   its rates to affiliates, rental networks, or "other payers." The facility
   ends up giving its discount to payers it never negotiated with. Ask: strike
   it, or limit rate access to named entities.
2. **Lesser-of billed charges** — payment at the lesser of the contract rate
   or billed charges. A chargemaster set low (or not updated) silently caps
   revenue below the negotiated rate. Ask: strike, or at minimum audit the
   chargemaster before signing.
3. **No escalator** — flat rates with evergreen auto-renewal means a real-rate
   cut every year of the contract's life. Ask: annual CPI-or-fixed-% increase,
   or a rate reopener on each renewal.
4. **Short timely filing** — a short window (measured against the facility's
   actual billing cycle) plus SNF realities (payer of last resort
   determinations, Medicare exhaust, retro-eligibility) produces write-offs of
   clean, payable claims. Ask: a longer window, and an exception for
   retro-eligibility and coordination-of-benefits situations running from the
   date eligibility became known.
5. **Unilateral amendment** — the payer may amend by notice, with silence as
   acceptance ("material change" clauses). The contract you signed is not the
   contract you'll have. Ask: mutual written consent for amendments, or at
   minimum the right to terminate without cause within the notice window.
6. **Missing high-cost carve-outs** — no drug/dialysis/vent/bariatric
   pass-throughs means one admission with a high-cost specialty drug can wipe
   out the margin on a month of census. Ask: cost-based or threshold-triggered
   carve-outs for the categories in Workflow A.
7. **Level criteria vagueness** — judgment terms in the level grid give the
   payer's reviewer, not the contract, control of the effective rate. Ask:
   objective criteria (named services, measurable thresholds) and a stated
   combination rule.

Also screen beyond the checklist — anything from the Workflow A "Gaps &
ambiguities" section that shifts risk to the facility belongs in the memo
(one-sided termination, weak prompt-pay terms, appeal deadlines shorter than
the payer's own decision timelines, offset/recoupment without notice).

### Steps

1. Start from a Workflow A summary (produce the needed parts if absent).
2. Run the checklist; collect quotes.
3. Prioritize: rank findings by financial exposure and operational pain, not
   by checklist order. Three well-argued asks beat twelve.
4. Draft the memo. For each point, write the "ask" as specific contract
   language direction, not a vibe ("add a mutual-amendment clause requiring
   signed consent" — not "make amendments fairer").

### Output format — Workflow C

ALWAYS use this exact template:

```markdown
# Negotiation Points Memo
**Contract:** [payer] | **Renewal/negotiation date:** [date] | **Prepared:** [date]

## Executive summary
[3-5 sentences: overall posture of this contract, the two or three points
that matter most, and the single most important ask.]

## Priority negotiation points
### 1. [Issue name] — [High/Medium/Low priority]
- **Current language:** "[verbatim quote]" (§/p.)
- **Why it hurts:** [operational/financial impact, plain language]
- **The ask:** [specific change]
- **Fallback position:** [acceptable compromise, if any]
[Repeat, in priority order]

## Checklist results
| Unfavorable term | Present? | Location |
|---|---|---|
| Silent PPO / rental network | Yes / No / Unclear | |
| Lesser-of billed charges | | |
| No escalator | | |
| Short timely filing | | |
| Unilateral amendment | | |
| Missing high-cost carve-outs | | |
| Vague level criteria | | |

## Points in the facility's favor
[Terms worth protecting in the negotiation — don't trade these away blind.]

## Before the meeting
[Data to pull: utilization by level, carve-out-eligible admissions history,
denial/appeal outcomes under this payer, chargemaster review if lesser-of
language exists. Compare the proposed per-diem levels against the facility's
own cost per patient day and its Medicare FFS PDPM yield — this skill carries
no benchmarks, so run that comparison from the facility's numbers; do not
skip it. Facility's own data only — no external benchmarks needed.]
```

---

## Reference

Read `references/contract-terms-glossary.md` when the user asks what a term
means, when writing for an audience new to managed care, or when unsure of
the SNF-specific significance of a term you've encountered in a contract.
Definitions there include *why the term matters to an SNF*, which is the part
worth echoing into your outputs.

## Worked micro-example (leveling)

Input: "Sample Health Plan contract, Level 3 requires: IV medication
administration, OR complex respiratory care, OR wound vac. Patient is
post-op, on oral antibiotics, has a wound vac in place per the treatment
sheet."

Output core: Level 3 — criterion "wound vac" **Met** (evidence: active wound
vac order + treatment sheet entries). IV meds Not met (orals only).
Combination rule is ANY (contract uses "OR"). Documentation checklist:
current physician order for NPWT, treatment/flow sheet entries each shift,
weekly wound measurements. Confidence: High — objective criterion, directly
documented.

## Disclaimer

This skill is educational. Managed-care contracts are legal documents; have
counsel review any contract, amendment, or negotiation position before
signing or relying on it. Level determinations and claims decisions must be
made by qualified facility staff based on the actual contract and the actual
medical record. Nothing produced by this skill is legal, billing, coding, or
reimbursement advice.
