# Nursing & Biomedical Research Skills for Claude

A library of [Claude Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) that package the research workflows clinical nursing and biomedical students actually need — APA-7 citation auditing, PRISMA-2020 systematic reviews, mixed-methods design, manuscript peer review, licensing-exam reasoning, and markerless motion-capture ergonomics.

Built by a nurse practitioner–track graduate student, for the people sitting next to me. Most of them write no code. The point of a Skill, for that audience, is that it turns a workflow into something reproducible — not a one-off chat that has to be re-explained every session.

> **Note on language.** The `SKILL.md` files are written in Traditional Chinese, because the intended users are nursing and medical researchers in Taiwan and the skills encode Taiwanese academic conventions (TWNA EBHC reporting, local IRB structures, national licensing exam formats). The workflows themselves are field-standard and portable; contributions adding English variants are welcome.

---

## The skills

| Skill | What it does | Files |
|---|---|---|
| **`apa7-master`** | APA 7th edition reference and in-text citation auditing, with a four-step audit chain: reference correction → missing-source search → citation correction → double check. Handles Chinese and English sources, plus the awkward cases (UpToDate, textbook chapters, government reports, unpublished theses). | 1 |
| **`prisma-2020-master`** | Systematic review reporting against the full PRISMA 2020 checklist, including flow-diagram construction and item-by-item compliance verification. | 2 |
| **`academic-writing`** | Section-by-section manuscript drafting for medical and nursing papers — Introduction through Conclusion — under APA 7th, with a built-in pass for removing AI writing tells. | 1 |
| **`academic-peer-reviewer-v2`** | Simulates senior peer review at a high-impact journal: novelty, methodology, clarity and significance, output as a structured report (Summary / Strengths / Major & Minor Weaknesses / Recommendation) in `.docx`. | 6 |
| **`mixed-methods-research`** | End-to-end consultation for qualitative, quantitative and mixed-methods designs: interview coding, instrument design, statistical test selection, SEM/path analysis, integration strategy, and Taiwanese academic context. | 7 |
| **`paper-analysis`** | Structured reading and appraisal of a single paper — what it claims, how well the design supports the claim, and what it does not establish. | 1 |
| **`citation-verifier`** | Checks that cited sources exist, say what they are claimed to say, and are correctly attributed. | 1 |
| **`pubmed-daily-bundle`** | Scheduled PubMed search, open-access full-text retrieval, analysis and packaging — built around clinical decision support and AI-assisted nursing education, restricted to PMC open full text. | 3 |
| **`med-licensing-exam`** | Chain-of-thought problem solving for the Taiwanese medical licensing exam: option-by-option elimination, mechanism-level explanation, and links to high-yield concepts. Includes reference sheets on biostatistics formulas, imaging clues, classification criteria and high-yield pharmacology. | 5 |
| **`markerless-mocap-ergonomics`** | Design and build multi-camera markerless motion capture systems for occupational ergonomics: the five constraints that decide the architecture, calibration, 3D reconstruction, biomechanical scoring (REBA/RULA), multi-person association, validation strategy, and a project scaffold script. | 28 |

---

## Install

Copy any skill folder into your Claude Skills directory:

```bash
cp -r skills/apa7-master ~/.claude/skills/
```

Then start a Claude Code session and ask for the thing the skill does — each `SKILL.md` declares the trigger phrases that should invoke it. Skills also work in Claude Desktop and on claude.ai; see the [Agent Skills documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) for the current install path on each surface.

---

## How these are built

Every skill follows the same shape, because the shape is what makes them usable by non-programmers:

- **Explicit trigger phrases.** The `description` field lists the things a user actually says (`「幫我寫參考文獻」`, `「這篇能不能投」`), not an abstract capability statement. If a user has to know the skill exists to use it, it has failed.
- **References over instructions.** Long-lived domain knowledge — the PRISMA checklist, APA edge cases, pharmacology high-yield tables — lives in `references/`, loaded only when needed, rather than bloating the main prompt.
- **Templates and validation scripts where output format matters.** `academic-peer-reviewer-v2` ships a Node script that generates the review as a Word document, because that is the artefact a reviewer actually submits.
- **Honest scope.** Each skill states what it does not do. `citation-verifier` will not invent a DOI; `paper-analysis` appraises, it does not adjudicate.

---

## Not included

This repository contains only skills written by the author. Third-party and official Anthropic skills installed alongside them locally (Cloudflare, data-science tooling, document format skills, and the academic-research-skills suite by Cheng-I Wu, CC BY-NC 4.0) are **not** redistributed here.

Two further personal skills are deliberately withheld: one built on a copyrighted internal medicine textbook, and one encoding a specific institution's internal handbook. Neither is mine to publish.

---

## License

MIT — see [LICENSE](LICENSE). Use them, fork them, adapt them for your own department. If they save you an afternoon, that is the entire point.

## Author

**Ming-Xun Yu (游明勳)** — M.S.N. candidate, Nurse Practitioner track, National Defense Medical University, Taipei. Registered nurse, three and a half years in gastroenterology before returning to research.

Currently building GenAI clinical decision support for nurse practitioner education.
