# How the reporting workflow is organized

This is a public-safe sketch based on private project notes. It omits the employer's table names, field IDs, credentials, schedules, message text, and operational data. The example below is fictional; it is not an exported record.

```text
Feishu Base records
    → normalize project, task, owner, status, and period
    → check data quality
    → build a report draft and exception list
    → human review
    → send or hold
    → record the result of the run
```

The Base is the place for people to update work and review results. The processing script handles joins, calculations, validation, and rendering. Keeping those jobs separate avoids burying business logic inside a long chain of UI automations. The [local demo](../demo/report.py) illustrates just the validation and draft-generation steps with invented records.

## Checks before a draft is ready

The checks look for absent owners or targets, tasks whose parent cannot be found, duplicate reporting periods, stale input, and progress values that do not match the agreed field definition. A flagged row goes to an exception list. It is not quietly dropped from the denominator.

For example, these two fictional records should not automatically count as two independent completed tasks:

| Task | Parent | Status |
| --- | --- | --- |
| Prepare campaign summary | — | In progress |
| Check submission totals | Prepare campaign summary | Done |

The report has to declare whether it counts leaf tasks, parent tasks, or both. Otherwise the same work can inflate progress.

## Sending and reruns

A successful draft is still only a draft. A reviewer checks it before any group message is sent. The run log distinguishes `generated`, `approved`, `sent`, and `failed`; a send failure cannot be shown as success. If the job is retried, the reporting period and destination are checked so a retry does not create a duplicate message.

For model-assisted review work, the same boundary applies: uncertain or high-risk output is a candidate for human review, not an automatic final decision. That part is a design principle from the related Obsidian notes, not a claim that every proposed model workflow was deployed.

## What is deliberately absent

No real people, customers, Base identifiers, links, videos, screenshots, or production scripts are included. The private Vault remains local; this repository contains only a rewritten, generic explanation of the workflow.
