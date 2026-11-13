# Imaging manifest

> Imaging needs more detail than a document list — a clinician planning treatment usually needs the
> **actual study (DICOM), not just the PDF report.** This is where you spell out each scan: what it is,
> when, what's attached (the images themselves vs only the written report), and how the reader gets it.
> A radiology reviewer can rarely work from a report alone. Every study/series/date comes from the scan
> or its report, **not from memory.** Replace every `[placeholder]`. The example below is a **synthetic
> illustrative case (skull-base chordoma) — not a real patient.**

> *This lists a patient's imaging assembled for a clinician's review. The images and reports are the
> source; restate what they say, don't infer.*

---

**Pack for:** [recipient] · **Question:** see `current-question.md` · **Version:** [v1] · **Prepared:** [date]

| # | Study | Modality | Date | Body region | What's attached | Format | How to access |
|---|---|---|---|---|---|---|---|
| 1 | [study name] | [MRI / CT / PET-CT / X-ray / US] | [YYYY-MM-DD] | [region] | [images + report / report only] | [DICOM disc / DICOM link / PDF] | [disc enclosed / view-only link / portal] |
| 2 | [study name] | [modality] | [YYYY-MM-DD] | [region] | [images + report] | [DICOM] | [link / disc] |

**Reading this for the reader:**
- **DICOM vs PDF matters.** A PDF is the radiologist's *words*; DICOM is the *images* a planning team can
  re-read and measure. If the reader is being asked to re-interpret or plan, they almost certainly need
  DICOM — note clearly which studies you can supply as images and which are report-only so they can ask.
- **Say how each study is delivered** — a physical disc enclosed, a view-only/expiring link, or via a
  portal — and that a view-only link can be blocked by a hospital's security, so a disc or file copy is
  often the reliable fallback. (Link mechanics and expiry: `../../references/core/privacy.md`.)
- **Strip the invisible layer.** DICOM headers carry patient identifiers and sometimes institution data;
  PDF reports can carry QR codes/barcodes that resolve to the live chart. Note what's been cleaned, and
  keep name/DOB only where the reader needs it to match the file.
- **If a study is referenced but not supplied**, say so plainly (e.g. "prior MRI held at [centre], not
  yet retrieved") rather than leave a gap the reader has to chase.

**Requesting the images:** if you still need to obtain DICOM from the holding hospital, the records/DICOM
request is in `../letters/` (and the multi-centre handoff logic — "assume centres don't talk to each
other" — is in `../../references/modes/next-action.md`).

---

### Worked example (synthetic — skull-base chordoma)

**Pack for:** [external particle-therapy centre] · **Question:** see `current-question.md` · **Version:** v2 · **Prepared:** 12 Mar 2026

| # | Study | Modality | Date | Body region | What's attached | Format | How to access |
|---|---|---|---|---|---|---|---|
| 1 | MRI head, with contrast | MRI | 2026-02-10 | Skull base / clivus | Images + report | DICOM | Disc enclosed + view-only link (expires 30 days) |
| 2 | Staging CT chest/abdo/pelvis | CT | 2026-02-14 | Chest/abdomen/pelvis | Images + report | DICOM | Disc enclosed |
| 3 | Prior MRI head | MRI | 2025-11-?? | Head | Report only — images held at [home centre] | PDF report | Images being requested; see `../letters/` |

_DICOM headers de-identified to name + DOB only (needed to match the file); MDT-note QR removed and saved copy checked.
Outreach and private notes are not part of this pack._
