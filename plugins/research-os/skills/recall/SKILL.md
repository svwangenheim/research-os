---
name: recall
description: Clear your due spaced-repetition reviews (free recall, FSRS-scheduled). This is engram's own /review — renamed here purely so it reads clearly next to /peer-review (manuscript review) instead of colliding with it in meaning. Use when reviews are due, or the user wants to review/practice what they've learned via /learn.
argument-hint: "[quick | <topic>]"
allowed-tools: Skill
---

# Recall

A thin alias, nothing more. All the real logic — the retrieval protocol,
confidence-integrity picker, amnesty-on-return, transfer probes, FSRS
scheduling — is entirely **engram's own `/review`** (`engram:review`),
untouched. research-os renames it here only for naming clarity in this
plugin's command surface: `/peer-review` is manuscript peer review,
`/recall` is spaced-repetition memory review — two very different things
that would otherwise both read as "/review."

## What to do

Invoke the Skill tool with **`engram:review`**, forwarding `$ARGUMENTS`
verbatim (`quick`, a topic name, or nothing). That is the entire skill.

## Guardrails

Do not reimplement, summarize, or shortcut any part of engram's retrieval
protocol here — this is a pure pass-through.
