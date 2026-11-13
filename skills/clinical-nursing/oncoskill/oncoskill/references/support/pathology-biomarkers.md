# Support: pathology & biomarker logistics

Help a patient/caregiver move the *physical specimen* and its tests through the system — the part that
quietly stalls cases — and prepare the right questions, never to interpret the slides or call a test
result yourself. Draft-only; the team decides. (Binding rules: `../../POLICY.md`.)

*Example-level guidance, not rules for your case — adapt to the person's region and situation; their care team's instructions win (full principle: `../core/adapt-to-context.md`).*

## The thing almost everyone misses: the bottleneck is usually the specimen, not the test

When a biomarker or genomic test is needed, it's easy to picture the hold-up as "the lab is slow." Far
more often the real blocker is the **tissue itself** — where the block physically sits, who has to cut
slides from it, whether anyone has actually requested it move, and whether enough material is left.
A test ordered against a specimen that nobody has shipped just waits. This is a classic seam where two
centres each assume the other is handling it, so it's worth treating the specimen as something *you*
track until it's confirmed where it is and where it's going. (The "centres don't talk to each other"
assumption from `../modes/next-action.md` applies in full here.)

This is also exactly where the advocate role bites gently. A good lab and a good team can still let a
block sit for weeks because no single person owns moving it. You don't need to fight anyone — just ask,
in writing, *where is the block, who is sending what to whom, and by when*, and keep asking until it's
confirmed. Trust the team; verify the specimen actually moved.

## What to track for the specimen

Hold these in the **relevant section of Current State** (documents / windows / open questions) — not a
new tracker. Offer to update Current State as answers come in.

- **Where the FFPE block is held** — which hospital, which pathology department, an archive/reference
  number if there is one. The original diagnostic block is often at the *first* centre that biopsied,
  not the one now treating.
- **Whether the treating centre re-reviews outside pathology.** Many expert centres re-read slides from
  elsewhere before acting; that re-review can itself change staging or the plan. Worth asking whether
  they want the **block**, **unstained slides**, or just the report.
- **Whether unstained slides can be cut** from the block instead of sending the block — and **how many
  slides** the receiving lab needs for the specific test. Tests differ; an NGS panel may need several
  sections, a single IHC stain far fewer.
- **Whether the original block must be returned**, and to whom. Blocks are sometimes the only archived
  tissue; losing one closes the door on future testing. If the block leaves, ask how its return is
  guaranteed.
- **Chain of custody** — who is shipping, how, tracking, who confirms receipt at the other end. "We'll
  send it over" is not confirmation; a logged hand-off is. (Records/specimen-request mechanics:
  `authorised-representative.md`.)
- **What the report actually states** — whether it names the **clone/antibody, the platform/assay, and
  the scoring system** used, not just a positive/negative. A result without its method is hard to
  compare or act on (see PD-L1 note below).
- **Turnaround, cost and coverage** — how long the test takes, what it costs, and whether it's covered
  or self-pay. If it's self-pay or sent to a private/overseas lab, the funding route belongs in
  `financial-insurance.md` and `eu-crossborder.md`.
- **Consent for genomic testing.** Broader tumour-genomic / germline sequencing usually needs explicit
  consent, and germline findings can carry family implications — flag it as a consent conversation with
  the team and, where relevant, a genetic counsellor, not a box to tick blindly.
- **How results return to the team.** A result that lands in a portal nobody on the treating team reads
  is the same as no result. Confirm who receives it and who acts on it.

## "PD-L1" — and most biomarkers — are not one single thing

A frequent, costly confusion: assuming any "PD-L1 test" answers the question. The same marker can be
run with different **antibody clones**, on different **platforms**, and reported with different
**scoring systems** (for example, a Combined Positive Score, CPS, versus a tumour-proportion score) —
and which one is the *right* one depends on the specific cancer and the decision it's feeding. A result
scored one way may not answer the question your team is actually asking. *(This is a general illustration
of how assay and scoring vary — not a claim about any specific cancer; confirm the correct assay and
scoring with your pathology team.)*

So the useful question isn't "was PD-L1 done?" but, in plain terms: *was it run with the assay and
scoring my team needs for this cancer, for this decision?* The same logic applies to other biomarkers
where method and scoring vary. Frame it calmly as a question for the pathologist or oncologist, not a
challenge.

## Preserve material for the future

Tissue is finite, and decisions can change — a later line of treatment may call for a broader
next-generation-sequencing / comprehensive genomic-profiling panel that wasn't needed at first. Worth
asking the team: *is enough tissue being preserved, and is the block being kept, so future testing
stays possible without another biopsy?* Re-biopsy isn't always feasible, so not burning the last of the
specimen on a narrow test is a real consideration — as a question to raise, not a rule you impose.

## Choosing or vetting a lab

If testing is being sent out — to a reference, private, or overseas lab — the question isn't "is this a
good lab" in the abstract but whether it actually runs the *specific* assay you need, validated and
reportable for clinical use (not research-only or a marketing line). That's the **technical-capability
audit** in `../modes/research.md` — ask for the exact assay, clone/platform, scoring, accreditation,
turnaround and how the report comes back, and route the question to the right department (pathology /
molecular pathology / the lab's clinical-liaison). Don't accept "yes we do genomic testing" as the
answer to "do you run *this* panel, reported this way."

## What this stays clear of

This module helps you *move and document* tissue and *prepare questions* about tests. It does not
interpret a pathology report, score a stain, call a biomarker positive or negative, or decide which
test you need — those are the pathologist's and oncologist's calls. If you want help understanding the
plain-language meaning of a report you already have, that's `../modes/explain.md` (which keeps the rule:
faithfully restate what a signed report documents, never independently infer a diagnosis or stage).

## Hand-offs

- **Letters** (`../../assets/letters/`) — skeletons for a pathology block/slides request, a DICOM/
  imaging request, and a medical-summary request, so the specimen and reports actually move.
- **`../modes/research.md`** — the technical-capability audit for vetting a lab's exact assay.
- **`authorised-representative.md`** — records- and specimen-request workflow when a centre will only
  release to the patient or won't release at all; a non-response is itself an event to log.
- **`financial-insurance.md`** / **`eu-crossborder.md`** — funding and coverage when a test is self-pay
  or sent abroad.
- **`../modes/next-action.md`** — to put "confirm where the block is and who's moving it" on the action
  list with an owner and a date.

**Guardrails:** no interpretation of slides or results; genomic testing needs proper consent (and
sometimes genetic counselling); state turnaround/cost/coverage as examples to confirm locally; record
findings in the relevant section of Current State, not a new ledger (`../../POLICY.md`).
