# nursing-qualitative-writing

A reusable AI writing skill for nursing qualitative research manuscripts.

This skill helps draft, revise, structure, and evaluate qualitative nursing research manuscripts, especially for journal submission to nursing and health-care journals such as:

- International Journal of Nursing Studies
- Journal of Advanced Nursing
- Nurse Education Today
- Nurse Education in Practice
- BMC Nursing
- Journal of Clinical Nursing
- Geriatric Nursing

## What this skill is for

Use this skill for:

- qualitative nursing manuscript writing;
- title, abstract, introduction, methods, results, discussion, conclusion, and keywords;
- COREQ/SRQR alignment;
- journal adaptation;
- persona-based qualitative studies;
- life-course qualitative studies;
- reflexive thematic analysis;
- qualitative content analysis;
- phenomenological studies;
- grounded theory;
- nursing education, gerontological nursing, clinical nursing, nursing management, and patient experience studies.

## Core writing logic

This skill follows an IJNS-style approach:

1. Frame a clinically, educationally, or systemically important nursing problem.
2. Narrow to a specific population, setting, culture, policy context, or care situation.
3. Summarise existing evidence as an argument, not a literature list.
4. Identify a precise qualitative knowledge gap.
5. Explain why qualitative inquiry is appropriate.
6. Present findings as analytic interpretations grounded in participant accounts.
7. Develop discussion as an interpretive argument, not a repetition of results.
8. Maintain strict factuality and ethical protection.

## Main modules

- Introduction writing
- Methods writing
- Results writing
- Discussion writing
- Abstract writing
- Title writing
- Keywords
- Journal adaptation
- COREQ/SRQR alignment
- Factuality and ethics rules
- Output formats

## Example prompts

### Introduction

> Use nursing-qualitative-writing to draft an IJNS-style Introduction for a qualitative study on professional identity formation among male undergraduate nursing students from a life-course perspective.

### Methods

> Use nursing-qualitative-writing to revise the Methods section. Please check whether the study design, sampling, data collection, data analysis, rigour, ethics, and reflexivity are methodologically coherent.

### Results

> Use nursing-qualitative-writing to rewrite the Results section using theme-level analytic paragraphs, subtheme explanations, and participant quotations.

### Discussion

> Use nursing-qualitative-writing to strengthen the Discussion for Nurse Education Today. Please move beyond theme repetition and identify the conceptual contribution.

### Abstract

> Use nursing-qualitative-writing to write a structured abstract with Background, Aim, Design, Participants, Methods, Results, Conclusion, and Keywords.

### COREQ/SRQR

> Use nursing-qualitative-writing to check this manuscript against COREQ/SRQR and identify missing reporting items.

### Persona-based qualitative study

> Use nursing-qualitative-writing to present persona-based qualitative findings. Please include persona name, included participants, description, characteristics, needs, quotations, and implications.

## Installation

Copy the entire `nursing-qualitative-writing` folder into your Codex skills directory.

Typical location:

```bash
~/.codex/skills/
```

Example:

```bash
mkdir -p ~/.codex/skills
cp -R nursing-qualitative-writing ~/.codex/skills/
```

Then restart Codex.

## Important rules

This skill must not invent:

- participant numbers;
- participant characteristics;
- recruitment sites;
- interview dates or duration;
- themes or subthemes;
- participant quotations;
- ethics approval numbers;
- analytic procedures;
- software use;
- saturation or information power;
- member checking;
- references;
- journal requirements.

If information is missing, the assistant should flag the missing item and use a placeholder rather than fabricate details.
