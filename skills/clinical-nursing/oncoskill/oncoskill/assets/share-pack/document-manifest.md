# Document manifest

> The contents page of the pack: exactly what's attached, in order, so the reader knows what they have
> and can find each piece. List **only** the documents that bear on this question — not the whole vault.
> Each row is **selected on purpose**, never an export. Keep originals and translations as separate rows
> and label which is which. Every date and detail comes from the document itself, **not from memory**.
> Replace every `[placeholder]`. The example below is a **synthetic illustrative case (skull-base
> chordoma) — not a real patient.**

> *This list accompanies a patient's records sent for a clinician's review. The documents are the source
> of truth; this manifest only points to them.*

---

**Pack for:** [recipient] · **Question:** see `current-question.md` · **Version:** [v1] · **Prepared:** [date]

| # | Document | Type | Date | Language (orig / translation) | Pages | Share-safe? |
|---|---|---|---|---|---|---|
| 1 | [report name] | [pathology / radiology / discharge / MDT note / labs] | [YYYY-MM-DD] | [e.g. PT original] | [n] | [redacted ✓ / check] |
| 2 | [report name] | [type] | [YYYY-MM-DD] | [e.g. EN working translation of #1] | [n] | [✓] |
| 3 | [labs] | [labs] | [YYYY-MM-DD] | [orig] | [n] | [✓] |

**Imaging** is listed separately in `imaging-manifest.md` (studies, series, DICOM vs PDF).

**Before this leaves your hands — the per-item check (full version: `../../references/core/privacy.md`):**
- Unneeded identifiers and QR/barcodes are **actually removed**, hidden text and metadata cleaned,
  and the saved copy reopened and checked. Flattening alone is not redaction. Mark unchecked files
  as **check**, not as redacted.
- Stray personal data this question doesn't need is removed (home address, unrelated ID numbers, other
  people's details); name + DOB kept **only** where the recipient needs them to match the file.
- No internal or emotional notes, and **no unverified hypotheses** (yours or the skill's), rode along
  inside any document — those are questions for `current-question.md`, not facts in a pack.
- Where a document is translated, the **original is included alongside** the working translation and each
  is labelled — a translation is an aid, not the record.
- Every value the reader will rely on was **checked against the document, not recalled.**

**Notes:** keep the order logical (diagnosis → staging → treatment → latest result). If a document is
referenced but deliberately *not* attached (too much, or not relevant), say so in a line rather than
leave the reader guessing.

---

### Worked example (synthetic — skull-base chordoma)

**Pack for:** [external particle-therapy centre] · **Question:** see `current-question.md` · **Version:** v2 · **Prepared:** 12 Mar 2026

| # | Document | Type | Date | Language (orig / translation) | Pages | Share-safe? |
|---|---|---|---|---|---|---|
| 1 | Histopathology report | Pathology | 2026-02-18 | EN original | 3 | redacted ✓ |
| 2 | MRI head report | Radiology | 2026-02-10 | EN original | 2 | redacted ✓ |
| 3 | Staging CT report | Radiology | 2026-02-14 | EN original | 2 | redacted ✓ |
| 4 | Skull-base MDT note | MDT note | 2026-02-24 | EN original | 1 | redacted ✓ — QR removed; saved copy checked |
| 5 | Discharge note (biopsy) | Discharge | 2026-02-17 | EN original | 1 | redacted ✓ — meds list kept, address removed |

_Imaging files themselves listed in `imaging-manifest.md`. Outreach notes and Current State are private
and deliberately not attached._
