# Feishu operations automation — anonymized case study

This repository describes an operations workflow I worked on during an internship. The employer's code, Feishu Base, customer records, and internal documents are private. What is here is a simplified account of the design and the problems it had to handle, not a copy of the production system.

## The problem

Project updates lived across several tables and chat threads. Preparing a weekly summary meant checking task ownership, resolving inconsistent status fields, and copying figures into a message. That was slow, and a plausible-looking summary could still be wrong if a parent task and its children were counted twice.

## What I worked on

- Organized project, task, owner, status, and progress fields so reports could use one consistent definition.
- Used Python and the Feishu API to turn table records into report drafts and exception lists.
- Added checks for missing owners, stale records, broken parent-child links, duplicate reporting periods, and values outside their expected range.
- Kept a human review step before messages went to a group. A generated draft is not treated as a sent report.
- Logged each run and made failed reads or writes visible rather than silently producing an incomplete report.

The [workflow note](docs/workflow.md) shows the boundaries between the Base, the processing script, and human review. A [small local demo](demo/report.py) checks fictional task data and generates a report draft; it does not connect to Feishu or send messages.

```bash
python3 -m demo.report demo/tasks.csv
python3 -m unittest discover -s tests -v
```

## What this case does and does not show

This is a design and operations case study with a runnable local example, not a production integration. There are no credentials, live Base links, employee details, customer names, or source records here. The example data is invented.

I have left performance and scale figures out of the public version because the source notes use different definitions for some counts, and several outcome metrics still need a reproducible baseline. I would rather explain the decisions and failure modes clearly than publish numbers I cannot yet defend.

## What changed in my approach

The useful lesson was to separate producing a report from sending it. Data checks, draft generation, approval, delivery, and logging each need their own state. That made it easier to spot errors and safer to rerun a job without sending the same message twice.
