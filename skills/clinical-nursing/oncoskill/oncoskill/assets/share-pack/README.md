# Doctor Share Pack

A **share pack** is the clean, outward-facing dossier you hand to a specific doctor or clinic for a
specific question. It is **not** your Current State. Current State is your private, messy, complete
working memory — meds, labs week to week, half-formed worries, draft questions, things you're still
chasing. A share pack is the opposite: small, finished, exact, and built for one reader who has ten
minutes. You build a fresh one for each recipient and each question, and you throw nothing of your
private notes into it by accident.

*Example-level guidance, not rules for your case — adapt to the person's region and situation; their care team's instructions win (full principle: `../../references/core/adapt-to-context.md`).*

## The three-vault separation (keep these strictly apart)

Most mix-ups come from blurring three different things. Keep them in three places and never let one
leak into another:

- **Doctor Share Pack** — what goes *out*. Clean, factual, only what this recipient needs for this
  question. Built from the templates here.
- **Private Medical Vault** — your raw records: full reports, imaging, pathology, the lot. The source
  you build *from*, but you don't hand the whole vault to anyone by default — you select.
- **Private Care-Ops** — your Current State, the Outreach Ledger, your emotional notes, your draft
  letters, anything you've found yourself and want to *ask about*. This stays with you. None of it
  belongs in a pack going to a doctor.

The single rule that prevents most accidents: **a share pack is a deliberate selection, never an
export.** You decide, item by item, what earns its place.

## How to build one (the workflow)

1. **Pick the recipient and the one specific question.** A pack aimed at "a doctor, generally" helps
   no one. Name the reader (which clinic, which specialty) and the single thing you want from them —
   a second opinion on a margin, whether they can do a technique, an interpretation of a scan. The
   question shapes everything else. (Use `current-question.md`.)
2. **Select only the documents that bear on that question.** Not the whole vault — the two or three
   reports, the one scan, the pathology that this reader actually needs. Everything else is noise that
   slows them down. (List them in `document-manifest.md`; imaging in `imaging-manifest.md`.)
3. **Write the one-page clinical summary.** Who the patient is, the documented diagnosis and stage,
   the treatment so far, where things stand, and the question. One page. (`case-summary.md`.)
4. **Lay out the timeline** so the reader can see the sequence at a glance — diagnosis, key scans,
   procedures, treatment, results — dated. (`medical-timeline.md`.)
5. **Build the manifests** so the reader knows exactly what's attached and can find each piece.
   (`document-manifest.md`, `imaging-manifest.md`.)
6. **Write the cover letter** for this specific clinic — the polite framing, the ask, what's attached.
   (`clinic-specific-cover-letter.md`; the fuller letter library is `../letters/`.)
7. **Proof the load-bearing facts.** Re-check every date, dose, unit, lab value, and name against the
   source documents — not against memory or your Current State, against the actual report. A wrong
   unit or a transposed date in a pack going to a doctor is a real harm. **Use only values that come
   from the documents; never a number you (or the skill) recalled.**
8. **Separate original from translation.** If you've translated anything, keep the original alongside
   the working translation and label which is which — the clinician may need the source wording, and
   a translation is your aid, not the record.
9. **Strip what doesn't belong** (see below), then **version and date it** so you and the reader both
   know which pack is current.

## What NOT to include

A share pack is also defined by what you leave out. Before it goes anywhere, remove:

- **Internal and emotional notes** — your worries, your frustration with a clinic, "I think this
  doctor missed something." None of it. It changes how you're read and helps nobody clinically.
- **Unverified hypotheses — yours or the skill's.** Anything you found yourself or the assistant
  reasoned out belongs in your private notes as a *question to ask*, not stated as fact in a doctor
  pack. The skill is not a doctor and must not present a guess as a finding. If you want to raise it,
  raise it as a plain question in `current-question.md` — "is it worth checking X?" — never as a
  conclusion.
- **Recalled clinical numbers.** Only values lifted directly from the patient's own documents go in.
  Don't let a remembered lab value or a half-remembered dose into a message to a clinician.
- **Stray personal data that this question doesn't need.** Keep the patient's name and date of birth
  only where the recipient genuinely needs them to identify the file; strip home address, unrelated
  ID numbers, other people's details, and any metadata, QR codes, or barcodes on scans. (Full
  redaction checklist and consent/authority rules: `../../references/core/privacy.md`, and **POLICY.md
  §3**.)
- **Unlabelled claims.** Diagnosis, stage, lab values, and prescribed treatment must be attributed to
  their records. New symptoms and events reported by the patient/caregiver also belong when relevant:
  label them **patient-reported** or **caregiver-reported**, with date/time, separately from documented
  findings. Do not discard an urgent symptom because it has not yet appeared in a signed report.

## A note on your role

You're the one assembling this, and that's exactly right: the responsibility for the care you (or the
person you care for) receive rests with you. A clean, specific, honest pack is how you make it easy
for a good clinician to help — and how you keep the conversation about the clinical question, calmly,
without manufacturing a fight. Trust your team, and give them something clear to work with.

## The templates here

- `case-summary.md` — the one-page clinical summary.
- `medical-timeline.md` — the dated sequence of events.
- `current-question.md` — the single specific ask for this recipient.
- `document-manifest.md` — what reports/files are included, and where each is.
- `imaging-manifest.md` — the scans, with study/series detail and DICOM vs. PDF.
- `clinic-specific-cover-letter.md` — the cover note tailored to one clinic.

Hand off: building the wider outreach letter → `../letters/`; what to strip and consent/authority →
`../../references/core/privacy.md`; keeping your private working picture → `../state-templates/`.
