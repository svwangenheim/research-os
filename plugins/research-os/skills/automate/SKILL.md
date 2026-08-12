---
name: automate
description: Author and run the executable procedures in _brain/procedures/ - your own recurring tasks, not general research-os skills. Socratic authoring or evidence-drafted; runnable the moment they validate, no promotion gate. Use on "automate this", "write a procedure", "run my <name> procedure", or "schedule this".
argument-hint: "new <name> | run <name> [--dry-run] | list | status <name> | map | schedule <name> [--off] | schedule --list"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Automate

The workflow layer's working surface — replaces `/procedure`. Procedures live
in `_brain/procedures/` (template: `${CLAUDE_PLUGIN_ROOT}/templates/brain-notes/procedure_template.md`).

**Input:** `$ARGUMENTS` — a subcommand. With none, run `list`.

| Subcommand | Does |
|---|---|
| `new <name>` | Author a procedure — in dialogue, or drafted from evidence |
| `run <name>` | **Execute it.** No gate, no waiting for recorded runs. |
| `list` | Every procedure: role, trigger, schedule, draft state, automation |
| `status <name>` | One procedure in detail — same info, one row |
| `map` | Regenerate `_brain/automation-map.html` |
| `schedule <name> [--off]` | Register/unregister the `schedule:` frontmatter |
| `schedule --list` | Declared-vs-registered drift across every procedure |

---

## The three-layer model (why this exists at all)

> **1 · research-os skills** (`plugins/research-os/skills/`) — generalizable
> research machinery. Ships to every researcher. `/strategize`, `/write`,
> `/peer-review`.
>
> **2 · Personal procedures** (`_brain/procedures/`, this skill) — *your own*
> recurring tasks. Never ships. Executable, not documentation.
>
> **3 · This skill** — authors, runs, maps and schedules layer 2. Ships as part
> of research-os, because every researcher needs it for *their own* tasks —
> just not for the same tasks.

**Composition rule: procedures may call skills; skills never call procedures.**
A DZ modelling procedure can compose a BMAD workflow (`mmm-qa-verify`) or a
research-os skill (`/diagnose`) as one `[ai]` step, recorded in `calls:` —
while adding what those don't: commit, checkpoint, project-note update, wiki
push. See `docs/13-the-automation-layer.md` for the full account, including why
an earlier version of this layer had a five-gate promotion mechanism that
could never actually be reached.

---

## `new <name>` — authoring

**Never scrape a transcript into steps.** Steps record what you *mean* to do,
not a replay of one session's detours.

### 1 · Arrive with a draft

Before writing anything, assemble a proposal:

- the matching row in `_brain/workflow-audit.md`, if the audit has run
- mined evidence in `_brain/.session-mining/`, if `mine_sessions.py` has run —
  real prompt sequences from how this task was actually done in past sessions
- `git log` subjects for the relevant project(s)
- any BMAD workflow or research-os skill this task should compose (→ `calls:`)
- an existing sibling procedure, if one is close

Use `project_state_scan.py` rather than exploring project directories — OneDrive
traversal is slow enough to stall the session.

### 2 · Write it — dialogue when there's time, draft-and-correct when there isn't

**When authoring interactively:** open a dialogue, house style as in
`/discover interview` — plain-text questions, one or two at a time, no
`AskUserQuestion`, curious not prescriptive, stop when it's clear (4–8
exchanges). Three things the conversation must supply because evidence can't:
the judgment inside each step, the forks (a stated rule or explicit
`ask-user`), the failure modes.

**When authoring from evidence alone** (a batch of procedures, no time for a
full dialogue per one): draft every step from the mined evidence and the audit,
tag every uncertain step `[human]` rather than guess, and set `draft: true`.
The first real `/automate run` is where the draft gets corrected — that is the
designed correction point, not a shortcut around the dialogue.

Either way: every step gets an actor tag (`[ai]`/`[human]`/`[external]`/
`[veto]`) — the runner classifies by this tag and stops on anything untagged,
so an untagged step is unfinished, not optional. Put machine/employer/person
specifics in `Config`, not in Steps. Set `name:` to exactly the filename
(validated). Set `schedule:` now if this belongs on a clock — that's the whole
deploy step.

Verify: `python "${CLAUDE_PLUGIN_ROOT}/scripts/wiki_quality_check.py" --root <vault>`

## `run <name>` — execute it

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/automate_run.py" --root <vault> --name <name>
```

Prints the ordered plan: which steps execute, where it stops, whether it
refuses outright. Then **you perform it** — `[ai]` steps with your own tools
(this is what keeps the R2 data-consent gate and every other tool-permission
check in one enforced place, rather than a script shelling out on a second,
unaudited path), `[external]` steps by invoking the named tool/skill/BMAD
workflow, and at the first `[human]` or `[veto]`, stop — ask, or refuse,
exactly as `automate_run.py`'s docstring specifies. `--dry-run` shows the plan
without you acting on it.

**After running, record it:**

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/automate_run.py" --root <vault> --name <name> \
  --record-run --ran-by interactive --stopped-at <n, or omit if completed> \
  --deviations "<what differed from the note, or empty>"
```

This appends inside the procedure's `@generated` run-log markers — never
hand-edit inside them. A run that keeps recording the same deviation means the
note's steps are wrong; fix the note, don't just re-run it.

**Same semantics on a schedule.** `scheduled/automate-procedure.ps1` runs the
identical plan unattended and stops at the identical points — it does not
guess past a `[human]` step just because no one is watching.

## `list` / `status <name>`

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/automate_run.py" --root <vault> --name <name> --dry-run
```

For `list`, read every note in `_brain/procedures/` directly (role, trigger,
schedule, draft, automation) — there is no separate inventory script; the
notes are the inventory.

## `map`

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/generate_automation_map.py" --root <vault>
```

Writes `_brain/automation-map.html` — by role (what a week contains, work and
life), by procedure (step flow), and coverage (which skills/BMAD workflows
each procedure composes). Report the path; don't re-describe what it shows.

## `schedule <name>` / `schedule --list`

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/automate_schedule.py" --root <vault> --name <name>
python "${CLAUDE_PLUGIN_ROOT}/scripts/automate_schedule.py" --root <vault> --name <name> --off
python "${CLAUDE_PLUGIN_ROOT}/scripts/automate_schedule.py" --root <vault> --list
```

Reads the procedure's own `schedule:` field — declaring it *is* the deploy
step. Registers a Windows Scheduled Task pointed at the one shared wrapper
script (`scheduled/automate-procedure.ps1 -Name <name>`); no per-procedure
script gets hand-written. `--list` reports drift both directions: declared but
not registered, and registered but no longer declared (likely stale).

---

## Guardrails

Do not:
- generate steps from a session transcript — author them, in dialogue or from evidence, never a replay
- use `AskUserQuestion` for the authoring dialogue
- write a step without an actor tag
- leave machine-specific literals in Steps when `Config` exists for them
- execute a `[human]` or `[veto]` step yourself, interactively or scheduled — stop, every time
- shell out from `automate_run.py` itself — it returns a plan; the skill acts, inside tool-permission enforcement
- edit inside `@generated` run-log markers
- recursively glob project directories (OneDrive; it will stall)
- turn a `veto` into a low score, or re-score a veto away
- let a procedure call another procedure — only skills/BMAD workflows belong in `calls:`
- write a skill from this command — a skill ships to every researcher; a procedure never does
