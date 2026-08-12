# Procedures

One note per recurring process — **how you actually do a thing**, step by step. The layer that holds working knowledge, as distinct from `projects/` (what is being worked on) and the thematic wikis (what is known).

Each note (`note_type: procedure`, template `procedure_template.md`) holds a trigger, numbered steps tagged by who executes them (`[ai]` / `[human]` / `[external]` / `[veto]`), the decision points that are still judgment calls, known failure modes, a machine-specific `Config` block, and an automatically-appended run log.

## Procedure or skill?

> A **procedure** describes how *you* do something, judgment calls included. It may be half-formed, role-specific, employer-specific. It is a note.
>
> A **skill** is machinery any researcher could run: fixed input/output contract, no unresolved judgment forks, proven stable across repeated execution.

Everything starts as a procedure. Promotion to a skill is **mechanical, not remembered** — `scripts/procedure_promotion_check.py` evaluates five gates (≥3 recorded runs, steps unchanged across the last two, a complete contract, every decision fork resolved, nothing person-specific outside `Config`). When all five pass, `promotion:` flips to `ready`, the weekly routine surfaces it, and `/procedure promote` drafts the SKILL.md. Shipping it still takes one confirm.

## Who writes these

`/workflow-audit` identifies and scores them; `/procedure new` authors them **in dialogue** — Claude proposes a draft from observed evidence, you correct it, then it is written. Nothing here is scraped from a transcript.

The run log is machine-owned: the nightly routine matches the day's observed work against each trigger and appends a stamp plus any deviation. **Do not hand-maintain it.** A procedure whose log keeps recording the same deviation is a procedure whose steps are wrong — that signal is the whole point of the layer.

## Vetoes are permanent

A step tagged `[veto]` must never be automated, whatever its clone score says. The reference case is AD-5: Claude must never read, process, log, or cache real SOEP microdata in any form. A veto carries a `veto_reason` and survives every re-scoring.
