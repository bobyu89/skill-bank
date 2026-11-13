# Changelog

All notable changes to the `oncoskill` skill. Versioning is informal during v0.

## [0.1.1] — 2026-09-07

- Incorporated the prepared public-example privacy cleanup; corrected PDF/QR redaction and the
  limits of expiring links, including templates and evaluation expectations.
- Removed universal nadir-day, dietary-restriction, iron-route, and safe-delay claims. Added scoped,
  dated source notes to the installed package; model agreement and working links are not verification.
- Supported independent second opinions after an agreed plan and complaints during treatment when
  warranted; removed blanket deference and mandatory disclosure rules.
- Clarified permitted document/research tools, platform-dependent privacy, and verified persistence.
  Current State distinguishes package strength from prescribed dose and keeps superseded entries clear.
- Added one-message setup, a clean native archive and a complete chat document, reproducible builds,
  package integrity tests, and focused synthetic regression scenarios. Cross-platform model behaviour
  remains a separate check; the historical results below do not validate this version.

## [0.1.0-dev] — unreleased (v0)

### Readability & self-containment pass (Fable review)
A read-only audit for human + agent usability, then fixes. No clinical content changed.
- **Follow-up: three-reviewer verification pass** (human-lens / agent-lens / regression sweep), then
  targeted fixes: privacy intake note rewritten in plain language (the "Zero Data Retention" jargon
  could read as reassuring when it means the opposite); "Evidence reviewed through:" stiff-stamp
  contradiction resolved everywhere in favour of the woven, human phrasing (SKILL §3, POLICY, explain)
  and §3 now says plainly that v0 bundles no structured disease packs and to never invent a
  reviewed-date; documented-stage restate carve-out added to SKILL §2; routing gaps closed (money &
  insurance route to `financial-insurance.md`; tiebreakers for distress-by-speaker and
  "experimental"/second-opinion); onboarding no longer suggests naming the project "Recovery" and
  explains what to paste; EU "S2" glossed on first use; every relative cross-reference in the bundle
  now resolves (bare `POLICY.md`/`SKILL.md`/schema paths prefixed across ~35 files, verified by a
  resolver scan); an internal build token that had leaked into `source-hierarchy.md` removed;
  Medebound moved below the named cancer centres and labelled as commercial; leftover replacement
  artifacts from the ledger rewording cleaned up (incl. a mangled historical entry in this file).
- **Bundle-integrity bugs fixed.** Re-synced the in-skill `POLICY.md` **and** `INTENDED_USE.md` with
  their repo-root source-of-truth copies (both had drifted — installed users were getting a policy
  missing the advocacy section, and an intended-use file missing the medical-device-status sentence).
  Added a "duplicated-on-purpose, keep in sync" rule to `CONTRIBUTING.md`.
- **Reply in the user's language.** New explicit rule in `tone.md` and `SKILL.md` §4 (mirror the
  user's language; keep Current State in their language; only outward drafts follow the recipient's).
- **Progressive disclosure restored.** `SKILL.md` §0 no longer invites pre-loading all core files
  (~16k tokens); it now says §2/§4 are a self-contained summary and to open a core file only when the
  moment calls for it (~84% lighter start). §0 insurance/S2 line corrected to "only on a real
  trigger, not at hello" (was contradicting `onboarding.md`).
- **De-duplicated boilerplate.** The full example-caveat block (was repeated in 23 files) collapsed to
  a one-line pointer in 24 files; the canonical block stays in `adapt-to-context.md` + human-facing
  templates. Added a `tone.md` rule: the stance is a behavioural lens, **not** text to recite each turn.
- **Dangling references fixed.** In-skill files no longer link `research/source-ledger.yaml` as if
  bundled — they name it as the repo-only ledger and cite the source itself; `SKILL.md` §7 says so.
- **Simpler default memory.** Added `assets/state-templates/current-state-simple.md` — the one living
  picture as a short, no-tables list; onboarding now defaults to it, with the tabular `current-state.md`
  as the grow-into option.
- **Navigation & discoverability.** New `references/modes/README.md` index; root `README` now documents
  running Oncoskill as a dedicated agent (`AGENTS.md`, `roles/`, `docs/run-as-your-own-agent.md`) and
  a corrected repo-layout tree. `SKILL.md` frontmatter description broadened (on-treatment, meds/food,
  fertility, surgery, insurance, survivorship) for better activation; intake privacy note generalized
  beyond "Claude product" to "whatever AI product you're using."

### Review-wave: advocacy surfaced, genericization, active-treatment + access + support build-out
A large build wave shaped by a de-identified multi-chat review. No real patient data — every worked
example is a synthetic composite, and every lived medical/financial/legal specific is flagged as an
example to adapt, not a rule (`references/core/adapt-to-context.md`).

- **Advocacy stance, surfaced and kept prominent.** Added `references/core/your-role.md` (the
  "trust your team, and verify; the responsibility rests with you" stance as a calm, public-facing
  core principle — realism, not cynicism, not a fight with your doctors). Carried, softened in tone
  but not in substance, into `POLICY.md`, `README.md`, and `caregiver.md`; the caregiver advocacy
  section keeps its teeth and gains a patient-autonomy/consent line.
- **Genericization principle.** Added `references/core/adapt-to-context.md` (everything here is
  example-level; adapt to your country, health system, and language; your own team's instructions
  win). The canonical caveat block now heads every lived/medical/financial/legal module.
- **Active-treatment layer.** New modes: `on-treatment.md` (the internal loop of being on treatment —
  expected cumulative side-effects vs red flags, lab-trend reading, anemia as an operational blocker,
  treatment-readiness checks, "ask the threshold"), `medications.md` (stricter public boundary:
  explain the leaflet, verify active ingredient/dose from the package, flag interactions to the
  pharmacist/team, never compute a personal dose or green-light a combination), `perioperative.md`
  (surgery day + first 72h), `survivorship.md`, `oncofertility.md` (closing-window decisions, OTC
  explained, jurisdiction-as-law flagged), `patient-mental-health.md`, and `decision-support.md`
  (structure a hard choice; questions to the team, never decide for them).
- **Access-engineering, cross-border & finance.** Extended `next-action.md` (multi-centre
  coordination, burned-bridge playbook, sequencing before irreversible/costly steps, no media during
  active treatment, the overall-treatment-time delay framing). Raised `eu-crossborder.md` to a full
  S2/Directive/self-pay-reimbursement playbook; new `financial-insurance.md` (general payer map);
  new `authorised-representative.md`, `pathology-biomarkers.md`, `second-opinion-experimental.md`;
  extended `trials.md` (trial navigation + compassionate-use routing). First **regional country
  pack** `portugal.md`, labelled explicitly as a *regional example*.
- **Research & consultation discipline.** `research.md` gained a stop-rule, negative-search log,
  criteria-based centre comparison (no vague "best centre"), privacy-before-multi-model rule, and a
  doctor-facing evidence brief that discloses AI assistance. `evidence-check.md` became the
  founding gap-check engine (Care Plan Gap Brief + advanced-technique quality gate). `consultation.md`
  gained a live medical-interpreter protocol and a question tracker. `nutrition.md` gained a
  practical food-safety + symptom layer (no "immune-boosting" supplements during treatment;
  self-calibrate against over-restriction).
- **One place of memory.** Enriched `schemas/current-state.schema.json` (medications, allergies,
  labs, decisions, recommendations, windows, documents, red-flags-from-team, care-team contacts) so
  Current State stays the single living source of truth — modules update a *section* of it rather
  than spawn new ledgers. State templates refreshed to match. The Outreach Ledger and Doctor Share
  Pack remain the only genuinely separate artifacts.
- **Share pack, scripts, letters.** Added the **Doctor Share Pack** (`assets/share-pack/`) — a clean
  outward dossier, explicitly *not* the internal Current State. Added interpersonal **scripts**
  (`assets/scripts/`: reception/phone, WhatsApp/follow-up). Expanded `assets/letters/templates.md`
  from 6 to a fuller skeleton set (slot holds, escalation/de-escalation, S2 support, records/DICOM/
  pathology requests, reimbursement clarifications, for-the-record summaries, and more).
- **Tone & safety guards.** `tone.md` gained a trauma-safe language guard ("this weakens the
  request", not "this is fatal"), a `response_style` preference, and a "don't be the source of extra
  restrictions" rule. `safety.md`, `source-hierarchy.md`, `onboarding.md`, and `privacy.md` filled
  out (safe-prognosis pattern, diagnosis restate-vs-infer boundary, conflicting-source weighing,
  immediate-need-first onboarding, a doctor-pack redaction checklist).
- **Evidence honesty & evals.** Appended review-surfaced sources to `research/source-ledger.yaml`
  (supportive care, fertility, psycho-onc methods, Portugal, second-opinion/profiling), each marked
  medium/low confidence with a "verify before public release" caveat. New synthetic golden cases
  added under `evals/public/` (live-interpreter, food-safety, oncofertility, post-op aftercare,
  caregiver-breakdown, plan-gap, capability audit, private-fallback, consultation-tracker, redaction,
  conflicting-guidelines, unsupported-centre-claim, symptom-trend, medication-adverse-effect,
  documented-stage-restate, prognosis); the colorectal Hb-range note was corrected and the
  prompt-injection case is required to actually run.

### Letters library, logistics, CONTRIBUTING, nutrition
- Authored the letters library (`assets/letters/README.md` + `templates.md`): rules + "what to avoid"
  distilled from a real proven EU outreach campaign (de-identified), 6 letter types, and **worked
  examples filled with the synthetic chordoma case (EN + PT) — no real patient data**.
- Added the **parallel outreach campaign** play + traps to `next-action.md`.
- Added `references/modes/logistics.md` (cross-border travel/lodging/documents/money) and wired it
  into SKILL.md §1.
- Deepened `references/modes/nutrition.md` (malnutrition-first, myth-handling, claim-check).
- Added root `CONTRIBUTING.md` (rules of the house: no real patient data, verify-before-assert, safety
  boundary, source hierarchy, how to propose changes).

### Onboarding, caregiver resources, support bases, self-containment
- Added `references/core/onboarding.md` (first-run flow: role + tech level, simple setup, insurance /
  S2 flagged early, reduce-uncertainty framing) and wired it into SKILL.md §0.
- Added `references/support/caregiver-resources.md` (Ring Theory — Silk & Goldman; Caregiver's Bill of
  Rights; Distress Thermometer self-check; advocacy/communication; burnout; helplines; books; official
  videos) + a `caregiver_support` section in the source ledger. Enriched `caregiver.md` with the
  circles/"comfort in, dump out", the right to struggle, and the advocacy lessons.
- Filled support stubs: `psycho-onc.md`, `ru-resources.md`, `trials.md`.
- **Self-containment fix:** copied `POLICY.md`, `DISCLAIMER.md`, `INTENDED_USE.md` into the skill so
  the binding rules travel with the uploaded bundle (they previously lived only at the repo root).
- Tone: added a "no superiority / no gotcha — offer alternatives collaboratively" rule and a "match
  the depth to what they actually asked" rule to `tone.md`.

### Research & consultation modules
- Added `references/modes/research.md` — deep-research & fact-check engine: staging-gate first, then
  all current protocols for the exact cancer + stage, expert centres/clinicians + contacts, the
  multi-LLM cross-check + source-grounded (NotebookLM-style) verification method, and a prioritized,
  source-status-tagged, multilingual deliverable with diplomatic doctor questions. Posture: offer it,
  don't dump it, never trash the clinic.
- Added `references/modes/consultation.md` — prepare a brief, translate/capture the visit, debrief,
  and keep transcripts (with privacy caveats). Wired both into SKILL.md §1; cross-linked from
  `evidence-check.md`.

### Voice retune + caregiver mode
- Added `references/core/tone.md` (warm, human, conversational voice — no labelled report sections)
  and `references/core/conversation.md` (lead the dialogue across the whole journey). Rewrote
  SKILL.md §4 and the output guidance in `explain.md` / `next-action.md` accordingly.
- Authored the **caregiver** mode (`references/modes/caregiver.md`): 3-a.m. support, urgency-vs-
  anxiety, a human "stop rule", between-visit support, burnout, and routing to human/professional
  help — all in the new voice.
- Golden tests note that replies must read human (not labelled sections); a conversational re-run of
  the colorectal case + a caregiver demo are in `evals/results/2026-06-22.md`.

### Step ② — core workflows
- Authored the two core modes: `references/modes/explain.md` (document explainer) and
  `references/modes/next-action.md` (incl. Institution Channel Map, escalation/de-escalation
  playbook, power-of-attorney, owner/follow-up/escalation).
- State templates added (`assets/state-templates/`); `provenance` audit field added to the three
  state schemas.
- Cross-border reframed as a general competency with EU/S2 as the first jurisdiction module.
- Two public golden tests with attached source packets: `colorectal-explain-nextstep.md` (primary,
  common scenario) and `chordoma-crossborder-core.md` (edge, cross-border). Both run and PASS the
  rubric; an independent adversarial grading pass is recorded in `evals/results/`.
- Colorectal grounding facts verified against NICE/ESMO/NCCN and added to the source ledger.

### Step ① — skeleton
- Self-contained skill scaffold: thin `SKILL.md` router, schemas, bundled licenses.
- Reference/assets structure stubbed; dual-mode, safety/evidence/privacy rules, intake privacy
  note established. No executable scripts; no outbound network.
