---
name: recall
description: Clear due spaced-repetition reviews with free recall - the habit that makes /learn permanent. Use when reviews are due, or on "review", "practice", "do my engram reviews".
argument-hint: "[quick | <topic>]"
allowed-tools: Read, Write, Bash, Task, AskUserQuestion
---

# /recall -- the retention loop

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/dialogue-grammar.md` (hard rules, confidence integrity, park-and-resume, the rating map apply here verbatim). The engine is always at:

```bash
ENGRAM="${CLAUDE_PLUGIN_ROOT}/scripts/engram.py"
```

**Never inline a learner's answer into a shell command** -- pass productions via `--production-file` (or `--production-file -` on stdin); a stray quote or `$(...)` in what they typed would otherwise execute.

**Spawning agents.** "Spawn **engram-assessor**" / "**engram-artifact-smith**" means: dispatch that agent via the Task tool, by name -- this plugin's own `agents/engram-*.md`.

## 1 -- Load the queue

```bash
python3 "$ENGRAM" stash count     # a previous session's ungraded work?
python3 "$ENGRAM" due --limit <cap>
```

If stash > 0, settle it first (assessor -> `receipt` -> `stash clear`, per `/learn` Step 5) with one explanatory line. Caps: `quick` -> 5 items; otherwise mode default (Standard ~= 12). `--topic <t>` if the user named one, but note interleaving across topics is the default *on purpose* -- don't undo it for tidiness. Open with the session ticket. Empty queue -> one line of honest celebration, then stop (suggest `/learn continue` only if a topic has frontier nodes). Never invent reviews.

**Return-after-absence (the amnesty protocol).** If the due queue is large after a gap (roughly `due > 2x` the mode cap, or the last session was many days ago), do **not** dump the debt. One calm line of amnesty + load renegotiation, then a real choice:
- Frame it as normal, owed nothing: *"You've got 40 due after the break -- that's just spacing doing its job, not a debt. FSRS handles backlog fine."*
- Offer (arrow-key): **clear a capped set today** (this mode's cap, most-overdue first -- recommended) / **a longer catch-up** / **just the highest-value topic**. Never a marathon.
- Then run only the chosen cap. What's left stays due and un-guilted.

**The honest number, exactly once.** After the amnesty line and **before** the arrow-key offer, read the engine and state what the decay actually costs -- one line, then move on:

```bash
python3 "$ENGRAM" decay --topic <t>     # or bare, for everything
```

Say it flatly, lab-notebook register: *"Those seven are at ~70% and still falling -- four minutes today is the difference between keeping them and re-learning them."* Information, never pressure. Once, on return. Amnesty first, always. `settings.decay_notice = "off"` means silent, honor it without comment.

## 2 -- Per item -- the retrieval protocol

The `due` payload gives `probe`, `claim` (canonical answer), `rubric`, `node_kind`, `practice`. Show a progress marker per item: `[3/6] * residual-stream`. The order of operations is sacred:

**`node_kind: "procedure"` items first take a detour** (read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/problem-grammar.md` once per session when one appears): serve a fresh algorithmic variant generated from `practice.problem_frame` -- new values, same structure, never the stored numbers -- compute the answer key by execution first. When a `practice.discriminates_from` sibling is co-due, serve the pair adjacently, open with the naming step, and until answered the progress marker shows the topic, never the node id. Grade with the problem grammar's table -- method-wrong caps the grade regardless of the answer; slip-only miss is `partial`/`hard` with `--error-class slip`; wrong-method carries `--error-class conceptual`. No usable `practice` -> fall back to the stored probe, concept-style. Everything below applies unchanged.

1. Show the **probe only**. Free recall -- no options, no hints, no "remember when we...". Do not ask for a typed confidence number.
2. They produce. (Silence is fine; "no idea" is an answer -- treat as lapse, warmly.) Collect confidence via `AskUserQuestion` (four-band picker) **before the reveal**. Skip only if they volunteered a number unprompted; "Other" -> exact number; dismiss/skip -> null, never estimated.
3. Reveal: canonical `claim` + one-line gap analysis against `rubric`. Consequence-only answer -> one terse-production nudge ("and the mechanism?") *before* the reveal.
4. Map to a rating with the shared table (round down when torn), commit immediately via a file:

```bash
python3 "$ENGRAM" rate --topic <t> --node <n> --rating <r> --confidence <c-or-omit> \
  --grade <g> --production-file <tmp-answer.txt> --kind review --source self
# procedure items only: --error-class slip|conceptual
# engine rejects --error-class (version skew)? retry without the flag -- never lose the rating
```

Relay the returned due date in passing. Durability crossing a threshold (first reps, ~7d/~30d clearing, roughly doubling) -> one flat growth line; mature node creeping up -> stay silent; `hard`/`again` -> honest task-feedback, never a manufactured win; silent if `settings.momentum = off`.

**Special cases:**

- **`transfer_ready: true`** -- serve the `transfer_probe` **instead of** `probe`, rate with `--kind transfer`. Say it plainly: *"You've held this one for a month, so let's not ask you to recite it. Let's see if it fires."* Grade honestly and separately -- `stats.transfer` is its own number, never pooled into retention. A lapse here is not a memory failure: *"you remember it fine -- it just doesn't fire yet. That's a different muscle."* (v0.8.1: a failed transfer probe leaves the memory schedule completely untouched -- no stability hit, no lapse recorded, no `learning` demotion.)
- **High confidence (>=70) + lapse** -- hypercorrection: pause the queue, re-derive from `why_chain` prerequisites (or rebuild the mnemonic if `arbitrary`), `misconception add`.
- **Second+ lapse on the same node** (`lapses >= 2`) -- the encoding failed, not their memory. Re-encode differently after rating: new analogy (their interests), a contrast case, or an explorable; on a **procedure** node prefer a find-explain-fix erroneous example. `artifact: true` in the payload -> offer to regenerate the explorable differently (background-spawn **engram-artifact-smith** with current node state + open misconceptions); `false` -> offer to build one if `settings.artifacts != off` or asked. Say it plainly: "this card keeps dying, so we're changing the card, not blaming you."
- **Instant + correct + low confidence** -- note it aloud; calibration data surfaces at `/coach`.

## 3 -- Assessor audit (keep self-grading honest)

If the session had >=8 items, any disputed grade, or >=3 `partial`s: stash `{topic, node, probe, claim, rubric, production, confidence, kind:"audit", tutor_rating:"<r>"}` (plus `node_kind:"procedure"` where relevant) per item, spawn **engram-assessor** on `stash list` for an audit verdict, `stash clear` after. Report disagreements; log a `misconception add` or a note -- do not re-rate already-committed items. Learner disputes: same path, once.

## 4 -- Close

```bash
python3 "$ENGRAM" log-session --kind review --mode <mode> --minutes <est> --items <n>
python3 "$ENGRAM" stats
```

Close with the **receipt strip**: items -> outcomes, streak, one meaningful number (month-bucket recall rate, or a momentum number from `stats.momentum` when there was real growth). Queue large and they stopped early -- fine, say what's left, zero guilt.

**Research-os addition (light-touch):** if a recurring misconception surfaced this session (`lapses >= 2` on the same node, or the assessor flagged the same wrong model twice), mention once that it might be worth a wiki note (`40_methods/` or `30_concepts/`) if it isn't documented anywhere yet -- don't act on it; that's a `/wiki-ingest` call, not this skill's job.

## Guardrails

Do not reimplement, summarize, or shortcut any part of the retrieval protocol, confidence integrity, or FSRS scheduling. State changes only through `python3 "$ENGRAM" ...`; learner text only via file/stdin, never inline.
