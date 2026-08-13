---
title: "{{title}}"
name: "{{slug}}"        # invocation key for /automate run <name> — MUST match the filename
note_type: procedure
summary: ""
role: ""                # phd | dz-modelling | dz-outreach | admin | cross-cutting | life
trigger: ""             # the observable event that means "run this now"
schedule: null          # null | "daily HH:MM" | "weekly <day> HH:MM" | "monthly <day> HH:MM"
                         # declaring this is the whole deploy step — /automate schedule reads it
automation: assisted     # assisted | scheduled | vetoed
veto_reason: ""          # REQUIRED and permanent when automation: vetoed
calls: []                # research-os skills or BMAD workflows this composes, e.g.
                          #   ["/diagnose", "mmm-qa-verify"] — procedures may call skills;
                          #   skills never call procedures (see docs/13-the-automation-layer.md)
inputs: []
outputs: []
done_when: ""
clone_score: null        # 0-100, from /workflow-audit — null until scored
draft: true              # true until a real /automate run has corrected this note
projects: []
tags:
  - procedure
updated: "{{date:YYYY-MM-DD}}"
---

# {{title}}

**Note:** this is an executable spec, not documentation. `/automate run {{slug}}`
walks the Steps below — `[ai]` steps execute, `[human]` steps stop and ask,
`[veto]` steps refuse, always, on a schedule or not. There is no promotion gate:
this note is runnable the moment it validates.

## What this is, in one breath

<!-- One sentence. If it takes two, this is probably two procedures. -->

## Trigger

<!-- The observable event that means "run this now" — matched by /automate
     against git activity, the calendar, or a file appearing, and by
     automate_schedule.py if `schedule:` above is set. Good: "a referee report
     arrives for a submitted paper". Weak: "when I need to review something". -->

## Steps

<!-- Numbered, imperative, one action each. Tag every step with who runs it —
     the runner classifies by this tag, so an untagged step cannot be executed:
       [ai]       /automate executes this itself
       [human]    stops and asks — your judgment, hands, or credentials
       [external] an outside tool or system does it (EUROMOD, Outlook, a co-author)
       [veto]     refused, always — see veto_reason, permanent
     If a step composes a research-os skill or a BMAD workflow, name it and add
     it to `calls:` above — e.g. "3. [ai] Run `mmm-qa-verify`; require [OK]." -->

1.
2.
3.

## Decision points

<!-- Every fork in the steps above. Each becomes a stated rule or an explicit
     `ask-user` — a rule the runner can act on unattended; `ask-user` is a
     [human] stop, not a defect. An EMPTY rule cell means nobody has decided yet
     and the runner cannot proceed past that step. -->

| At step | The question | Rule |
|---|---|---|
|  |  | `ask-user` |

## Failure modes

<!-- What goes wrong when this is run badly, and the tell that it happened.
     Written from real failures, not imagined ones. -->

## Config

<!-- Everything specific to this machine, employer, or person: paths, account
     names, institution-specific conventions. Isolating it here keeps Steps
     portable — a future run in a different project or on a different machine
     changes only this block. -->

```yaml
```

## Run log

<!-- Appended by /automate run on every execution — timestamp, actor mix,
     [human] stop-points hit, deviations from what the note describes. A
     procedure whose log keeps recording the same deviation has steps that are
     wrong; fix the note, don't just re-run it. Never hand-edit inside the
     markers. -->

<!-- @generated:start run-log -->
<!-- @generated:end -->
