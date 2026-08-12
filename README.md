# Case Study — AI-Native Operations at an E-Commerce Media Agency

**Internship · May–Aug 2026 · AI-native data operations** (details anonymized;
figures are real).

> This is a **case study**, not the source code. The production codebase
> belongs to the employer and is covered by a confidentiality agreement;
> per the agreement I publish only anonymized descriptions of what was
> built and the measured outcomes.

## What the role was

An "AI-native data operations" internship at a Chinese e-commerce media
agency (KOL/vendor campaign operations on Douyin ecosystem). The job was
not data entry with AI help — it was **putting AI into the business
workflow and running it**: designing automations, reviewing their output,
and reporting numbers the team could act on.

## What I built

### 1. Vendor database on Feishu Base (core asset)

Designed and built a Feishu Base tracking **1,436 vendor submissions**
across **8 campaigns**, used daily by **13 team members**:

- 8 tables (submission ledger, task assignment with parent/child tasks,
  campaigns, employees, per-campaign tables) + 1 dashboard + 8 workflows
- **8 automated workflows**: weekly progress cards pushed to group chat,
  task distribution, weekly report generation — replacing manual
  spreadsheet aggregation
- Weekly progress visualization (6-column campaign overview + employee
  detail + progress table)

**Outcome**: reporting that took half a day of copying between spreadsheets
became push-button; the team stopped maintaining parallel sheets.

### 2. AI video review pipeline (YOLOv8)

For an AI video-audit project, trained YOLOv8 on **10,000+ labeled frames**
to detect non-compliant video elements:

- **93% accuracy** on the validation set
- Cut defect-identification time by **~60%**
- Reviewers went from frame-by-frame eyeballing to reviewing flagged
  candidates

### 3. Automation infrastructure (Feishu API + Python)

Built Python automation on top of Feishu APIs:

- Ingest → review → write-back pipeline with a **106-row manual review
  workflow** for edge cases the model couldn't decide
- Multi-round review fix cycles (rules versions updated across review
  rounds)
- OCR + parsing utilities for screenshot-based vendor submissions

### 4. Agent setup for the team

Maintained an OpenClaw-based AI assistant the team queries for daily
operations (submission status, task lookups) — turning the Base into a
question-answering layer, not just a spreadsheet.

## Numbers summary

| Metric | Value |
|---|---|
| Vendor submissions tracked | 1,436 |
| Campaigns | 8 |
| Team members using the Base | 13 |
| Automated workflows | 8 |
| YOLOv8 validation accuracy | 93% |
| Defect-identification time saved | ~60% |
| Manual-review edge-case rows | 106 |

## What I learned

- **AI-native ≠ adding AI**: the leverage came from making the *default
  path* of the business flow go through the automation, with humans as
  exception handlers — not from AI bolted onto manual work
- **Numbers you can defend**: every workflow had a baseline and a measured
  outcome; a story without numbers is a hobby
- **Systems outlive tools**: the Feishu Base structure survived tooling
  changes; the workflows were designed as data contracts, not UI clicks

*Sibling tooling I built alongside this work is public in my other repos
([stock-loop-lab](https://github.com/HY2MHY/stock-loop-lab),
[henry-v2](https://github.com/HY2MHY/henry-v2),
[vault-qa](https://github.com/HY2MHY/vault-qa),
[agent-compound](https://github.com/HY2MHY/agent-compound)).*
