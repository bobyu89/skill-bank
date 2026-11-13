## Nursing qualitative skills
大家好，我是北京中医药大学护理学院临床护理教学部的陈一萍，目前主要从事护理教育、老年护理、临床护理教学以及护理质性研究相关工作。欢迎大家持续关注 nursing-qualitative-skills。本项目希望为护理质性研究论文写作、方法学规范、COREQ/SRQR 报告对齐、IJNS 风格写作和国际期刊投稿提供可复用的 AI skills 支持。

如果你有任何需求，欢迎提交 issue；如果我们认为该需求有意义且可行，也会尽量推进实现。我们同样欢迎 PR，但请务必按照 README 后面说明的格式提交，以便我们更高效地审核与合并。

Hello everyone, I’m Chen Yiping from the Clinical Nursing Teaching Department, School of Nursing, Beijing University of Chinese Medicine. My current work focuses on nursing education, gerontological nursing, clinical nursing teaching, and qualitative nursing research. Thank you for your continued interest in nursing-qualitative-skills. This project aims to provide reusable AI skills for qualitative nursing manuscript writing, methodological reporting, COREQ/SRQR alignment, IJNS-style academic writing, and international journal submission.

If you have any requests, feel free to open an issue. If we find the request meaningful and feasible, we’ll do our best to implement it. We also welcome PRs, but please make sure to follow the submission format described later in the README so that we can review and merge them more efficiently.

# Nursing Qualitative Skills

A reusable AI skills repository for nursing qualitative research writing.

This repository currently contains one core skill:

- `nursing-qualitative-writing`: an AI writing skill for drafting, revising, structuring, and critically improving qualitative nursing research manuscripts.

The skill is designed for manuscript preparation and revision for nursing and health-care journals such as:

- International Journal of Nursing Studies
- Journal of Advanced Nursing
- Nurse Education Today
- Nurse Education in Practice
- BMC Nursing
- Journal of Clinical Nursing
- Geriatric Nursing

## Repository structure

```text
nursing-qualitative-skills/
├── README.md
├── LICENSE
├── .gitignore
├── install.sh
└── skills/
    └── nursing-qualitative-writing/
        ├── SKILL.md
        ├── README.md
        ├── examples/
        │   └── prompts.md
        └── references/
            ├── ijns-style-guide.md
            ├── qualitative-methods-guide.md
            ├── results-writing-guide.md
            ├── discussion-writing-guide.md
            └── factuality-ethics-guide.md
```

## Installation

### Option 1: Install all skills

From the repository root:

```bash
bash install.sh
```

Then restart Codex or your AI agent.

### Option 2: Manual installation

Copy the full skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/nursing-qualitative-writing ~/.codex/skills/
```

Then restart Codex.

## Example use

After installation, you can ask:

```text
Use nursing-qualitative-writing to revise the Introduction section in an IJNS-style funnel structure.
```

```text
Use nursing-qualitative-writing to rewrite the Results section using theme-level analytic paragraphs, subtheme explanations, and participant quotations.
```

```text
Use nursing-qualitative-writing to check this manuscript against COREQ/SRQR and identify missing reporting items.
```

## Important principles

This skill is designed to help with academic writing, but it must not fabricate:

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

If information is missing, the assistant should flag the missing item and use a placeholder rather than inventing details.

## License

This repository is released under the MIT License.
