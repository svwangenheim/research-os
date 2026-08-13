---
name: pending
description: Clear the backlog across every project - uncommitted work, unpushed commits, unpushed wiki knowledge. Asks once per project, then remembers. Use on "pending", "what needs committing", "clear the backlog", or after a sweep flags loss risk.
argument-hint: "[--project <slug>] [--action commit|push|wiki_push] [--dry-run]"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob, Skill
---

# Pending

The consented half of the automation ceiling. A sweep finds everything waiting;
this presents it **grouped by project**, asks once per project per action class,
and records the answer so it is never asked again.

**Input:** `$ARGUMENTS` — optional flags narrowing the sweep to one project or one action class. Omitted, it sweeps every project and asks once per project per action.

**Reads:** `_brain/.pending-actions.yaml` (the queue) · `_brain/automation-consent.yaml` (the ledger)

---

## The division of labour

> **Detection is autonomous. Mutation is consented.**

`pending_actions.py` sweeps and writes the queue; it can never act — it has no
mutating code path at all. This skill is the only thing that acts, and only
where consent says it may.

## Step 1 — Sweep

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/pending_actions.py" --root <vault>
```

Refresh rather than trusting a stale queue — work may have been committed by
hand since the last sweep. If the queue is empty, say so in one line and stop.

## Flags

All three narrow an otherwise full sweep. The default is every project, every
action class, acting on confirmation.

- `--project <slug>` — only this project. Use when returning to clear one
  backlog rather than reviewing all of them.
- `--action commit|push|wiki_push` — only this action class. Consent is still
  asked per project; this narrows *what* is offered, not *who* is asked.
- `--dry-run` — present the grouped backlog and stop. Nothing is committed,
  pushed, or written, and no consent is recorded. Use it to see the shape of
  the backlog before deciding.

## Step 2 — Present, grouped by project

**Group by project, never by action type.** Consent is granted per project, so
the user must see everything one project is asking for in a single view — the
decision is "do I trust the routine with this repo", not "do I like committing".

For each project show: the action classes pending, the counts, and a short
sample of what would change. Lead with the biggest loss risk. State plainly what
each grant would mean in future runs, since a grant persists.

Use `AskUserQuestion` here — this *is* a decision between discrete options, and
one tap per project is the whole point. (This is the opposite of `/automate new`
and `/workflow-audit`, which are conversations.) Offer, per project:

- **Grant** — do it now and from now on, without asking again
- **Just this once** — act now, keep asking next time
- **Not now** — skip this run, leave the queue entry
- **Never** — record `denied`; stop offering it for this project

Anything already `granted` in the ledger is **not** re-asked: report it as
"granted previously" and proceed. Anything `denied` is skipped silently.

## Step 3 — Act, within the grant

| Action | What is allowed |
|---|---|
| `commit` | `git add -A` and `git commit` in that project only. A real message describing the change — never "wip". Never `--amend`, never `--force`, never a rebase. |
| `push` | `git push` to the configured upstream **only**. Never `--force`, never a new remote, never a PR. |
| `wiki_push` | Invoke `/wiki-push` for that project. It has its own promotion council; do not bypass it. |
| `wiki_fix` | Only remediations `wiki_quality_check.py` reports. Never a judgment call. |

**Commit each project separately**, with its own message. Never one sweeping
commit across repos.

**Never canonicalize or merge wiki content here.** `/pending` can push knowledge
into the queue that `/wiki-push` handles; deciding what a concept page *says*
stays command-invoked and council-gated.

If a project is not a git repo (currently the judges design and the
`Research Ideas` index), say so once and move on — `git init` is a decision for
the user, not something to do on their behalf.

## Step 4 — Record consent

Write answers into `_brain/automation-consent.yaml`:

```yaml
projects:
  macro-fiscal-growth-model:
    commit: granted
    push: ask
  microsimulation-model:
    commit: granted
    wiki_push: denied
```

Only record **Grant** and **Never**. "Just this once" and "Not now" leave the
ledger untouched — that is what makes them one-shot.

## Step 5 — Report

Per project: what was done, what was skipped and why, what consent was recorded.
Then re-run the sweep so the queue reflects reality.

---

## Guardrails

Do not:
- act on anything without a grant, or a "just this once" in this run
- ask about a project already `granted` or `denied` — the ledger exists so the question is asked once
- group the presentation by action type instead of by project
- push without a grant for `push` specifically — a `commit` grant is not a `push` grant
- use `--force`, `--amend`, `git reset --hard`, or a rebase, under any grant
- open a PR
- commit across multiple repos in one message
- canonicalize, merge, or rewrite wiki content
- `git init` a project on the user's behalf
- commit files a project's own `.claude/settings.json` denies reading — a
  gitignored-but-sensitive path (the SOEP workspace) stays untouched, and AD-5
  makes that non-negotiable
