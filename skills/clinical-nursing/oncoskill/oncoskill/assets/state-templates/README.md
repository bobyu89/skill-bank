# State templates

Blank, copy-paste templates so a non-technical user can keep their own state files (in a Project, a
Google Doc, or Notion) — no tooling needed. They hold no real data; you fill them in locally.

- `current-state-simple.md` — **start here.** The single living picture as a short, plain list — no
  tables, fill only what matters. This is the right default for almost everyone.
- `current-state.md` — the **full** version of that same single picture, with proper tables (meds,
  labs, decisions, recommendations, windows, documents as **sections inside this one file**, not
  separate trackers). Grow into it only if the simple list stops being enough. Matches
  `../../schemas/current-state.schema.json`.
- `outreach-ledger.md` — the one separate tracker: a simple contact-tracker for chasing clinics, doctors, and
  second opinions, because that's a different shape of list. Matches
  `../../schemas/outreach-ledger.schema.json`.
- `action-board.md` — an optional short list of owned next actions, if you'd rather pull them out of
  Current State. Matches `../../schemas/action-board.schema.json`.

Start with the **simple** Current State; add the Outreach Ledger only when you're contacting
clinics, and reach for the full Current State only if the simple one stops holding enough. These are
CC BY 4.0 content.
