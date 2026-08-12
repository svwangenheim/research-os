# Dialogue Triggers — when a Socratic beat fires without being asked for

Single declarative place for **when** the research pipeline opens a conversation on its own, in the mould of `permissions.md` (which declares agent dispatch in one place so nothing else hardcodes it).

Machine-readable mirror: `${CLAUDE_PLUGIN_ROOT}/state/dialogue-triggers.json`
Implementation: `${CLAUDE_PLUGIN_ROOT}/hooks/dialogue-triggers.py`

---

## The problem this solves

The Socratic machinery already exists and is good — `/discover`'s interview style, the eight-beat `_shared/dialogue-grammar.md`, `/wiki-pull`, `/learn`, `/recall`. What was missing is that **every one of them waits for the user to type a command.**

Two standing instructions in this repo were, until now, hopes rather than mechanisms:

- `skill-router.md`: *"Wiki — start of any research session → `/wiki-pull`"*
- `_brain/profile.md`: *"All code Claude writes must be clearly explained, in an easy-to-follow pattern, so the user can learn alongside the implementation."*

Both are instructions to a model that may or may not remember. `continuous-learning-v2`'s own rationale states the general principle: **hooks fire 100% of the time; skills fire 50–80%.** The research side deserves the same treatment as the personal side.

## Two binding rules

### 1 · Ambient offer — never a block, never an auto-execute

Both existing hooks in this directory already set the precedent: `engram-session-start.sh` says *"ambient, never nagging"*; the push nudge is *"an OFFER, never an auto-write."*

A trigger **opens a dialogue**. It never makes a research judgment, never edits a file, never blocks a tool call, and never exits non-zero. Identification decisions, referee responses, and design choices stay human — that is the point of the semi-autonomous collaboration model in `profile.md`, not an obstacle to it.

### 2 · An annoyance budget

Auto-prompting's real failure mode is not being wrong. It is being *frequent*, becoming nagware, and getting switched off wholesale — taking the useful triggers down with it.

So: **at most 2 offers per session**, and a dismissed trigger goes quiet for 24 hours. Tunable in `state/dialogue-triggers.json`; `enabled: false` at the top disables the whole layer.

The snooze log is also the instrument: whichever triggers get dismissed repeatedly are the ones to delete.

## The registry

| Trigger | Event | Condition | Fires | Status |
|---|---|---|---|---|
| `session-anchor` | SessionStart | project has `passport.yaml` | prior context + stage + next step | **superseded** by `hooks/wiki-context.py`, which does it stage-aware and bounded |
| `stage-transition` | PostToolUse `Edit\|Write` | `passport.yaml` written, stage changed | reports what `graph/pipeline.json` says is actually ready — never a hardcoded one-skill-per-stage guess, which can disagree with the graph on a mid-pipeline or fan-out project; falls back to a fixed hint only if the graph itself can't be evaluated | active |
| `learn-alongside` | PostToolUse `Edit\|Write` | path under `03_analysis/scripts/` | the explanation beat `profile.md` mandates | active |
| `undocumented-decision` | Stop | stage flipped, no new decision record | Socratic decision-record beat | declared, not yet implemented |
| `critic-finding` | Stop | critic returned CRITICAL/HIGH | ask what the user thinks the fix is, before patching | declared, not yet implemented |
| `encode-worthy-confusion` | Stop | ≥2 clarifying exchanges on one concept | offer `/learn` on that concept | declared, not yet implemented |
| `due-reviews` | SessionStart | FSRS due count > 0 | offer `/recall` | shipped (`engram-session-start.sh`) |
| `unpushed-knowledge` | Stop | unchecked `wiki-links.md` items | remind to `/wiki-push` | shipped (session journal / push nudge) |
| `session-close-needed` | Stop | `git status --porcelain` nonempty in the project dir | offer the session-close ritual (`git-workflow` → `checkpoint` → `wiki-push`), matching the `phd-session-close` procedure | active |

Entries marked *declared, not yet implemented* are in the registry deliberately: the registry is the complete statement of intent, so the next person extends it rather than inventing a parallel mechanism. Entries marked *superseded* record that a need is already met — `session-anchor` stays listed at `enabled: false` precisely so nobody re-implements what `wiki-context.py` already does.

**2026-08-12:** a plugin sync silently reverted `session-anchor` back to
`enabled: true`, which would have fired alongside `wiki-context.py`'s own
digest and duplicated it. Re-disabled — see the plugin-volatility finding in
`docs/13-the-automation-layer.md`: plugin-side state that isn't committed can
be reverted out from under you, so re-check registry state like this after
any sync rather than assuming it holds.

## Adding a trigger

1. Add the entry to `state/dialogue-triggers.json` with a `why` that names the specific failure it prevents.
2. Add a handler in `hooks/dialogue-triggers.py`. It must return `(trigger_id, [line, line])` or `None`.
3. **Test the negative case.** The most likely defect is misfiring on a project that does not follow the pipeline — the Microsimulation and Macro-Fiscal repos run BMAD and have **no `passport.yaml`**. Every condition must test that the artifact exists rather than assuming it. Silence in those repos is a required behaviour, not an omission.
4. Add a row to the table above.

## Guardrails

- Never block a tool call. Never exit non-zero. Degrade to silence on any error.
- Never write a file from a trigger.
- Never bypass the budget, and never let one trigger emit more than two lines.
- Keep output ASCII — it goes to a raw console that may be on a legacy Windows codepage, where an em-dash arrives as a replacement character and a nudge that renders as mojibake reads as a bug.
- Never assume `passport.yaml` exists.
