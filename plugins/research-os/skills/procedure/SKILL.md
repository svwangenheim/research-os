---
name: procedure
description: Author, inspect, and promote the step-by-step processes in _brain/procedures/. Socratic authoring; promotion to a skill is computed, not remembered. Use on "write a procedure", "how do I do X", "promote this procedure", or "procedure status".
argument-hint: "new <name> | status [name] | promote <name> | map"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Procedure

The workflow layer's working surface. Procedures live in `_brain/procedures/`
(template: `${CLAUDE_PLUGIN_ROOT}/templates/brain-notes/procedure_template.md`).

**Input:** `$ARGUMENTS` — a subcommand. With none, run `status`.

| Subcommand | Does |
|---|---|
| `new <name>` | Author a procedure **in dialogue**, pre-seeded from evidence |
| `status [name]` | Run the promotion gates; show what each is blocked on |
| `promote <name>` | Draft a SKILL.md from a gate-passing procedure |
| `map` | Regenerate the interactive procedure map |

---

## Procedure or skill? (the rule this skill enforces)

> A **procedure** describes how *this researcher* does something, judgment calls
> included. It may be half-formed, role-specific, employer-specific. It is a note.
>
> A **skill** is machinery any researcher could run: fixed input/output contract,
> no unresolved judgment forks, proven stable across repeated execution.

Everything starts as a procedure. Nothing is promoted by opinion.

---

## `new <name>` — Socratic authoring

**Never scrape a transcript into steps.** The steps must be what the researcher
*means* to do, not a replay of what happened to occur in one session — which
would encode that session's mistakes and detours as canon.

### 1 · Arrive with a draft

Before asking anything, assemble a proposal:

- the matching row in `_brain/workflow-audit.md`, if the audit has run
- `git log` subjects for the relevant project(s), which show the real sequence
- any related instincts from the observation layer (`/instinct-status`)
- the project's `Orientation` and journal entries describing this loop
- an existing sibling procedure, if one is close

Use `project_state_scan.py` rather than exploring project directories — OneDrive
traversal is slow enough to stall the session.

### 2 · Open the dialogue

Present the draft and its uncertainties honestly, then talk it through. House
style, as in `/discover interview`:

- plain-text questions, **one or two at a time**, then wait
- **no `AskUserQuestion`**
- curious, not prescriptive; probe gently ("what would go wrong if you skipped
  that?" rather than "that step is unnecessary")
- build on the answers; stop when it's clear, usually 4–8 exchanges

Three things must come out of the conversation, because evidence cannot supply
them:

1. **The judgment inside each step.** Not "run the estimation" but what you look
   at to decide it worked.
2. **The forks.** Every point where you'd do something different depending on
   what you see. Each becomes a stated rule or an explicit `ask-user`.
3. **The failure modes.** What going wrong looks like, and the tell.

### 3 · Write it

Fill the template. Every step gets an actor tag — `[ai]`, `[human]`,
`[external]`, `[veto]`. An untagged step is unfinished and the quality check
will flag it.

Put everything machine-, employer-, or person-specific in the `Config` block,
not in the steps. This is what later makes the `generic` gate passable — and it
is much easier to do while writing than to retrofit.

Set `automation:` honestly: `manual` until proven, `vetoed` when it must never
be automated (with a permanent `veto_reason`).

Then verify:

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/wiki_quality_check.py" --root <vault>
```

## `status [name]` — the promotion gates

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/procedure_promotion_check.py" --root <vault>
```

Five machine-checkable gates, all of which must pass:

| Gate | Passes when |
|---|---|
| `runs` | ≥ 3 recorded executions |
| `stable` | `steps_hash` unchanged across the last 2 runs |
| `contract` | `inputs`, `outputs`, `done_when` all non-empty |
| `forks_resolved` | every decision point has a rule (`ask-user` counts) |
| `generic` | nothing person/employer-specific in Steps |

Narrate the output; don't just paste it. A procedure stuck on `stable` is still
being rewritten — that is information about the work, not a defect in the note.

## `promote <name>` — draft the skill

Only for a procedure where all five gates pass. If they don't, say which and stop.

1. Re-read the procedure end to end.
2. Draft `skills/<name>/SKILL.md`: frontmatter (`name`, `description`,
   `argument-hint`, `allowed-tools`), the steps as the body, `ask-user` forks as
   explicit conversational checkpoints, failure modes as a Guardrails section.
3. **Generalize as you go.** Every `Config` value becomes a parameter, an
   argument, or something the skill reads from the environment — never a
   hardcoded literal. If a value cannot be generalized, the procedure was not
   actually ready; say so rather than shipping a personal skill.
4. **Show the draft and stop.** Shipping needs one explicit confirm — a skill is
   machinery other people run.
5. On confirm: write the skill, set `promotion: promoted` and `promoted_to:` on
   the procedure. **Keep the procedure note.** It stays the record of how the
   thing is actually done and where its run log lives.

## `map` — regenerate the visual map

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/generate_procedure_map.py" --root <vault>
```

Writes `_brain/procedure-map.html`. Report the path; don't summarize what it shows.

---

## The run log is machine-owned

`/daily-summary` matches each day's observed work against procedure triggers and
appends run stamps and deviations inside the `@generated:start procedure-runs`
markers. **Never hand-maintain that section, and never edit inside those
markers.**

A procedure whose log records the same deviation repeatedly is a procedure whose
steps are wrong. Surface that; it is the layer's most valuable signal.

## Guardrails

Do not:
- generate steps from a session transcript — author them in dialogue
- use `AskUserQuestion` for the authoring conversation
- write a step without an actor tag
- leave machine-specific literals in Steps when `Config` exists for them
- promote a procedure that fails any gate, or override a gate by judgment
- ship a promoted skill without an explicit confirm
- delete a procedure after promotion
- edit inside `@generated` markers
- recursively glob project directories (OneDrive; it will stall)
- turn a `veto` into a low score, or re-score a veto away
