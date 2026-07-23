# Memory Entry Types

Four types of Claude Code auto-memory entries (`~/.claude/projects/.../memory/`). Check existing memory files before creating new ones to avoid duplicates.

> Auto-memory is the Claude Code harness feature for cross-conversation recall. It is distinct from clo-author's retired project-root `MEMORY.md`, whose role folds into `passport.yaml` (state) and `_brain/learning/` (durable learnings).

## 1. User (`user` type)
**What:** Information about the user -- workflow preferences, research interests, institutional context.
**When to save:** User reveals a personal preference, affiliation, or working style that will persist across sessions.
**Example:** "Sven prefers R over Python for analysis."

## 2. Feedback (`feedback` type)
**What:** User corrections, style preferences, quality standards.
**When to save:** User explicitly corrects an output or states a preference about how things should be done.
**Example:** "Don't add Stata references -- R, Python, Julia only."

## 3. Project (`project` type)
**What:** Project state that isn't captured in git and isn't already in `passport.yaml` -- e.g. a persistent working constraint or an external coordination fact.
**When to save:** A durable fact about the project surfaces that the passport doesn't model.
**Example:** "Co-author reviews drafts every Friday; hold submissions until then."

## 4. Reference (`reference` type)
**What:** External references discovered during work -- papers, tools, parallel projects.
**When to save:** A significant external reference is discovered that will be useful in future sessions.
**Example:** "Goldsmith-Pinkham's claude-container repo for reference."

---

## What Does NOT Go in Memory

- Code patterns or architecture (derivable from reading the code)
- Git history (derivable from `git log`)
- Debugging solutions (the fix is in the code)
- Ephemeral task details (what you're working on right now)
- Pipeline phase, scores, session boundaries, or the literature corpus -- those live in `passport.yaml`
- Anything already documented in `CLAUDE.md`, rules, or skills

## Rules

- Convert relative dates to absolute dates ("Thursday" --> "2026-05-09")
- Keep entries concise -- one line in `MEMORY.md` index, short file for details
- Update existing files rather than creating duplicates
- Objective, reusable *knowledge* (a new concept/method/dataset) does not go in memory -- it goes into a thematic wiki via `/wiki-ingest`, or `_brain/learning/` for durable personal learnings
