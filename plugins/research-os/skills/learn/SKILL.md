---
name: learn
description: Point Claude at a method, piece of code, or concept that just confused you — extracts a clear topic from the current session/project context and hands off to engram's real teaching loop (first-principles curriculum, Socratic tutoring, verified free recall, FSRS scheduling). No need to name a topic yourself; point at what you don't understand and this finds the words for it. Also checks _brain/learning/pending-topics.md for things flagged earlier. Use when the user says "I don't get this", "explain this properly", "wait, how does that work", "I want to actually learn this, not just have it work", or similar — or when Claude itself notices real confusion and offers this (see Proactive Offer below).
argument-hint: "[optional: a pointer to what confused you — a file, a term, 'that last thing', or 'continue'. Omit to infer from the session or check the pending queue.]"
allowed-tools: Read, Grep, Glob, Write, Edit, Skill
---

# Learn

research-os's only real job here is the **intake**: turning "I don't get this"
into a clear topic string, with project/wiki context attached. Everything
after that — the concept map, the Socratic tutoring, confidence picks,
grading, spaced-repetition scheduling — is entirely **engram's** (`engram:learn`),
untouched. Do not reimplement any of it.

**Input:** `$ARGUMENTS` — a pointer to what confused you, `continue`, or
nothing.

## Step 1 — Resolve the topic

1. **`continue` or nothing, with candidates in `_brain/learning/pending-topics.md`**
   (see Auto-Capture below): show the pending list, let the user pick one or
   say "something else."
2. **Nothing, no pending candidates**: look at the current conversation —
   what code, method, or concept did Claude just introduce that the user
   reacted to with confusion, or that's genuinely non-trivial and new (an
   estimator, an algorithm, a design pattern)? Name it plainly and confirm:
   "It sounds like it's the `<X>` that didn't land — want to learn that
   properly?"
3. **An explicit pointer** (a file path, a term, "that last thing"): resolve
   it against the current session/project — read the file or find the thing
   referred to.

**Compose a specific topic string**, not a vague word — engram's curriculum
architect builds a real concept map from this, so precision here saves a
wrong-scoped map later. Not *"DiD"* — *"the Callaway & Sant'Anna (2021)
staggered-adoption difference-in-differences estimator, as used in
`03_analysis/scripts/R/02_estimate.R`"*. Include the concrete context (file,
project, what it's for), not just the abstract name.

## Step 2 — Check for existing wiki context (if inside a project)

Quick check, not a full `/wiki-pull`: does a matching page already exist in
the project's main wiki (`40_methods/` or `30_concepts/`)? Note it either way
— found (for linking after the session) or not found (flag that `/wiki-ingest`
could seed one later, from what gets learned). Don't block on this.

## Step 3 — Hand off to engram

Invoke the Skill tool with **`engram:learn "<topic>"`** (or `engram:learn continue`
if resuming). This is the entire substantive step. Let engram run its real
flow end to end — the concept map, the "building your concept map, ~1-2 min"
expectation-setting, the Socratic beats, the confidence picker, the stash,
the assessor, the FSRS scheduling, the capstone, the return-commitment. Do
not shortcut, summarize, or duplicate any of engram's own steps.

## Step 4 — Link back into the knowledge graph (after engram's session closes)

engram's own state lives in `_brain/learning/` (`ENGRAM_HOME`) as JSON — it
is not itself an Obsidian note. Add the connective tissue research-os owns:

1. If in a project, append a line to `_brain/projects/<slug>.md`'s journal
   (the same file `/checkpoint` writes): *"Learned: `<topic>` (engram) —
   arose from `<file/context>`."*
2. If Step 2 found a matching wiki page, note the link there too (a line in
   the project note, not an edit to the wiki page itself — the wiki stays
   Claude-maintained via `/wiki-ingest`, not touched by a learning session).
3. If Step 2 found **no** matching wiki page and the session surfaced a real,
   durable concept/method worth keeping, mention that `/wiki-ingest` could
   seed one — don't do it automatically; that's a separate, deliberate act.

## Auto-Capture (research-os addition — a pending queue, not part of engram)

When Claude notices something genuinely worth learning properly but the
moment isn't right (mid-task, low signal that the user is actually stuck),
it may add a line to `_brain/learning/pending-topics.md`:

```markdown
# Pending Topics

- [ ] <topic string> — noticed <date>, from <project/file>
```

**Update in place** (append a line; don't create a second file). This list
is only ever consulted at the start of `/learn` (Step 1) — never nagged
about elsewhere, never surfaced by `/coach` (that skill is entirely
engram's own; research-os does not extend it). Remove a line once it's
picked up in Step 1 or the user says "not that one."

## Proactive Offer (guidance, not a separate trigger)

When the user signals real confusion — "wait, I don't get how that works",
"why does that work", "explain that properly" — about something Claude just
did or introduced, **offer** `/learn`, once, plainly: *"Want to actually
learn that (spaced-repetition, sticks properly), or just a quick
explanation now?"* Respect either answer. Never invoke `/learn` without
this offer being answered yes — it is never a silent/hard interrupt.

## Guardrails

Do not:
- reimplement any part of engram's teaching, grading, or scheduling logic —
  this skill's only job is composing a good topic string and the
  project/wiki linkage around it
- invoke `/learn` (the handoff in Step 3) without the user having said yes,
  whether via explicit invocation or the Proactive Offer
- edit the wiki directly from a learning session — link to it, don't touch it
- let the pending-topics list grow into a nag mechanism — it's consulted,
  never pushed
- fabricate a wiki-page match in Step 2 — actually check
