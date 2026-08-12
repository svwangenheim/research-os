# Prompt Shaping — a standing habit, not a skill

**When a request arrives informal, dictated, or ambiguous, shape it before acting on it — silently, every time.**

This used to be something you invoked (`/prompt-optimizer`, now disabled). That ceremony is backwards: you should always be resolving a fuzzy ask into a clear one, not only when someone remembers to ask for it. So it is a habit, not a surface.

## The shape

Before executing a non-trivial informal request, resolve five things:

1. **Role** — whose expertise answers this? Econometrician, referee, data engineer, librarian.
2. **Task** — the single concrete deliverable, as a verb plus an object.
3. **Context** — which files, datasets, prior decisions and constraints bear on it. In a research-os project this usually means `passport.yaml`, the relevant `00_admin/process/` notes, and the thematic wiki.
4. **Constraints** — what must hold: journal style, replication tolerances, no absolute paths, the integrity gate.
5. **Output format** — exactly what to return: a memo, a diff, a table, a plan, a score.

Then a sixth, for the output: **bookend** — restate the goal at the end and confirm it was met.

## How to apply it

- **Mostly silent.** Resolve the shape and proceed. Do not narrate a five-section preamble back to the user; the point is a better answer, not a visible form.
- **Surface only genuine ambiguity.** If a *decision* is the user's to make — which journal, which estimator, overwrite or append — ask it briefly via `AskUserQuestion`. Everything else, infer and state the assumption in one line.
- **Multi-turn specification is a different job.** Turning a fuzzy research idea into a full spec is `/discover interview`, not this. Prompt shaping is the single-shot habit; the interview is the conversation.

## Why this is a rule and not a skill

In a goal-first, gate-enforced workflow the lever is the goal and the gates, not the wording. A skill that reformats a request into a six-section prompt adds a step without adding judgement. Shaping belongs in the reflex layer, and the reusable-artifact case is already served by a requirements spec in `00_admin/process/plans/`.

## Cross-references

- `${CLAUDE_PLUGIN_ROOT}/rules/workflow.md` — for non-trivial tasks, shaping feeds the plan and the requirements spec.
- `${CLAUDE_PLUGIN_ROOT}/skills/discover/SKILL.md` — `interview` mode, the multi-turn sibling.
