---
title: "{{title}}"
note_type: procedure
summary: ""
role: ""                # phd | dz-modelling | dz-outreach | admin
trigger: ""             # the observable event that means "run this now"
frequency: ""           # daily | weekly | monthly | per-project | ad-hoc
clone_score: null       # 0-100, from /workflow-audit — null until scored
automation: manual      # manual | assisted | scheduled | vetoed
veto_reason: ""         # REQUIRED and permanent when automation: vetoed
inputs: []
outputs: []
done_when: ""
projects: []
runs: 0
last_run: ""
steps_hash: ""          # engine-owned — set by /procedure, never by hand
promotion: draft        # draft | maturing | ready | promoted
promoted_to: ""         # skill name, once promoted
tags:
  - procedure
updated: "{{date:YYYY-MM-DD}}"
---

# {{title}}

## What this is, in one breath

<!-- One sentence. If it takes two, this is probably two procedures. -->

## Trigger

<!-- The observable event that means "run this now". Written so a routine could
     match it against a day's git activity, calendar, or file changes — not just
     so a human recognises it. Good: "a referee report arrives for a submitted
     paper". Weak: "when I need to review something". -->

## Steps

<!-- Numbered, imperative, one action each. Tag every step with who runs it:
       [ai]       Claude can execute this unsupervised
       [human]    requires your judgment, hands, or credentials
       [external] an outside tool or system does it (EUROMOD, Outlook, a co-author)
       [veto]     must NEVER be automated — see veto_reason, permanent
     A step nobody has tagged is not finished being written. -->

1.
2.
3.

## Decision points

<!-- Every fork in the steps above. Each one is either resolved into a stated
     rule, or explicitly marked `ask-user`. An unresolved fork is what keeps a
     procedure from being promotable — that is the point, not a defect. -->

| At step | The question | Rule |
|---|---|---|
|  |  | `ask-user` |

## Failure modes

<!-- What goes wrong when this is run badly, and the tell that it happened.
     Written from real failures, not imagined ones. -->

## Config

<!-- Everything specific to this machine, employer, or person: paths, account
     names, institution-specific conventions. Isolating it here is what makes
     the `generic` promotion gate passable — the steps stay portable, the
     specifics live in one block that a second user would rewrite. -->

```yaml
```

## Run log

<!-- Appended automatically by the nightly routine when it matches observed work
     against this procedure's trigger. Deviations are the valuable part: a
     procedure whose log keeps recording the same deviation is a procedure whose
     steps are wrong. Do not hand-maintain this section. -->

<!-- @generated:start procedure-runs -->
<!-- @generated:end -->
