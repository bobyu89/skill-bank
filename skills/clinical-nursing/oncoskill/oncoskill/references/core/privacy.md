# Core: privacy & safe sharing — strip, consent, link, then send

How to help someone share medical material safely: what to take out before it leaves their hands, who
is allowed to share what, and how to limit further access after sharing. Draft-only — the agent prepares
and checks; the person sends. (Binding rules: `../../POLICY.md` §3. Intake-note text: `../../SKILL.md` §6.)

*Example-level guidance, not rules for your case — adapt to the person's region and situation; their care team's instructions win (full principle: `adapt-to-context.md`).*

The quiet truth worth saying once: **the responsibility for what gets shared, and with whom, rests
with the person whose data it is.** No portal, no "secure link", and no helper removes that. So the
move is calm and deliberate — share exactly what answers the question, to exactly the person who needs
it, with access controls where available and an honest account of their limits. Not paranoia; just keeping control of your own file.

## A few ground rules first

- **Storage depends on the host and its settings.** The skill provides no special protection.
  Show the intake note (`../../SKILL.md` §6) before document sharing; do not make unverified promises
  about retention, training use, or who has access.
- **No real patient data lives in this repo or in examples** — only de-identified, synthetic composites.
- **Draft-only.** The agent never sends, uploads, or posts anything externally. It prepares a clean
  copy and a checklist; the person reviews and shares.
- **Share the minimum that answers the question.** A specialist answering one question rarely needs the
  whole file. Less shared is less to leak.

## Redaction checklist — before a doctor pack leaves your hands

Walk this every time a packet is about to go to a clinician, second-opinion service, or insurer. The
goal isn't to scrub everything — a doctor often *needs* the name and date of birth to match the record
— it's to strip what doesn't earn its place.

- **Keep name + date of birth only if the recipient needs them to match the record.** For a question
  to a service that doesn't hold the file, initials + year of birth are often enough. When in doubt,
  ask what the recipient actually needs to identify the case.
- **Remove what doesn't belong to the clinical question:** home address, phone, email, national health
  / insurance / tax / passport numbers, employer, next-of-kin details — unless that specific recipient
  genuinely needs one of them (e.g. an insurer needs the policy number; a clinician usually doesn't).
- **Actually redact identifiers and QR/barcodes where they are not needed.** A visible code can
  remain readable after flattening or re-exporting a PDF. Use true redaction that removes the content,
  not a black rectangle layered over it; remove hidden text/OCR under the redacted area, metadata,
  embedded files, and comments that contain identifiers. Preserve clinical content and the original
  privately. Reopen the output: visually inspect each redaction and check search/copy/text extraction
  and metadata. Do not claim it is redacted if you only supplied instructions or cannot inspect it.
  For DICOM, use the recipient's accepted de-identification process; PDF redaction is not sufficient.

- **Clean the document body itself:** other people's data that rode along (a shared lab batch, a ward
  list, a family member named in a note), a clinic's internal routing stamps, and account/portal IDs in
  headers and footers.
- **Pull anything that's yours-and-private, not doctor-facing:** your own working notes, emotional
  notes, *unverified AI hypotheses or "could this be X?" guesses*, draft questions, and strategy notes.
  A clinician should receive documented facts and a clear question — not a transcript of your worry or a
  machine's speculation presented as if it were a finding.
- **From chat or transcript exports specifically:** remove the back-and-forth, the reassurance, the
  half-formed theories, and any third party who appears. What's left should read like a clean clinical
  summary, not a conversation.

Account names and ID formats above are **flagged examples** — the exact identifiers that matter vary by
country. The principle is constant: keep what identifies the case to *this* recipient, remove the rest.

A natural way to offer this:
> "Before this goes to the second-opinion clinic, let's tidy it so it only carries what they need. I'd
> keep your name and date of birth since they'll match it to your records, but take out your home
> address and any insurance number this clinic doesn't need. There's also a QR code on page 2;
> I'd remove the code itself and verify the saved copy, because flattening won't make it unreadable. And your
> note at the bottom — 'maybe it spread?' — I'd remove that; it's a worry, not a finding, and it can
> muddy how they read the rest. Want me to mark up exactly what to strip?"

## Limit future access — links, expiry, revocation

How a packet is *delivered* matters as much as what's in it.

- **Prefer a read-only, expiring, revocable link over an open attachment** when the platform allows it:
  restricted to the intended recipient, with an expiry date and revocable access. These controls
  cannot prevent screenshots, copying, or forwarding a copy already obtained. Revocation stops future
  access through that link; it does not retrieve copies.
- **One known recipient per link** beats a single link passed around. If two clinics need it, that's
  two links you can expire independently.
- **A view-only link can be blocked** by a hospital's security or simply ignored — so when a clinician
  actually needs the document, also attach the clean 1-pager (see `../modes/next-action.md` for the
  outreach mechanics). Convenience for them, control for you: share the link, keep the attachment minimal.
- **Set an expiry and actually let it lapse**; revoke access once the consult is done. Keep a light note
  of *what you shared, with whom, and when* — that belongs in the **documents** section of Current State,
  not a new tracker (see "one place of memory" below).

## Consent & authority — who may share what

Sharing someone's medical data is an act of consent, and consent belongs to the patient.

- **The patient decides** what is shared and with whom, as long as they can. Patient autonomy comes
  before a caregiver's convenience: a faster workflow never overrides the patient's choice about their
  own information.
- **A caregiver sharing on the patient's behalf needs authority to do it** — informal agreement for
  light coordination, and a **formal authorisation** when a clinic will only release records to an
  authorised person. That's a documents-and-rights workflow, not a fight; the patient stays the
  decision-maker. Hand off to `../support/authorised-representative.md` for how to set that up and which
  instrument fits (it's law, and varies by country).
- **Other people's data is not yours to share.** If a family member, a shared report, or a third party
  appears in a document, that's a redaction item, not something to pass along.
- **Get consent for genomic / biomarker testing and for onward sharing of those results** as its own
  step — it carries family implications. Detail lives in `../support/pathology-biomarkers.md`.

## What stays private vs what is doctor-facing

Two different audiences, two different contents — keep them apart on purpose:

- **Private (yours, internal):** the full picture — your worries, emotional notes, half-formed theories,
  unverified AI hypotheses, strategy and outreach notes, the messy working detail. This is your Current
  State and your private vault. It is *for you*, and it does not go out.
- **Doctor-facing (outward):** documented facts, the specific question, the relevant reports — clean,
  matched to the recipient, nothing extra. This is the Doctor Share Pack
  (`../../assets/share-pack/`): a separate, deliberately-built outward dossier, not your internal file
  with the worry left in.

Keeping these separate is what lets you be completely honest in your private notes *and* completely
clean in what a clinician receives. One feeds the other; they are never the same document.

## One place of memory

Tracking what's been shared, redacted, or consented to does **not** need a new ledger. It's the
**documents** section of **Current State** (the single living doc; see `../../schemas/`). When you
help someone share something, offer to *update the relevant section of Current State* — what was
shared, with whom, the link's expiry — rather than spinning up a separate sharing log.

## A note on evals-private

Anything kept for evaluation or quality work uses **de-identified, synthetic derivatives** — never raw
records. An eval case is a fictional composite built to test behaviour, not a real person's file with
the name taken off. Raw documents stay with the person they belong to.

---

When the immediate sharing question is handled, hand off where it goes next: building the clean outward
dossier (`../../assets/share-pack/`), the outreach and link mechanics (`../modes/next-action.md`),
formal authorisation to act for the patient (`../support/authorised-representative.md`), and
biomarker/genomic consent specifics (`../support/pathology-biomarkers.md`). Binding rules throughout:
`../../POLICY.md` §3.
