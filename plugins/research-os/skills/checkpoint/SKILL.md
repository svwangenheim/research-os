---
name: checkpoint
description: Session handoff - persists the session to passport.yaml, the research journal, and the personal brain, and refreshes the dashboard. Use before /compact, or on "checkpoint", "save progress", "wrap up".
argument-hint: "[--auto | --memory-only | --scaffold-only | --dry-run]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash
---

# Checkpoint: Session Handoff

Captures what happened in the current session and persists it across the two-layer knowledge model (see `${CLAUDE_PLUGIN_ROOT}/rules/wiki-integration.md` and `rules/logging.md`):

1. **`passport.yaml`** — the state ledger. Append a `sessions:` entry (resume point) and update `pipeline.current_stage`. This replaces clo-author's `SESSION_REPORT.md` + `pipeline-state.json`.
2. **`00_admin/process/journal.md`** — the narrative research journal (append, newest-first) when agent work happened.
3. **`00_admin/process/sessions/`** — a longer per-session handoff note when a one-line `sessions:` entry is not enough.
4. **`_brain/projects/<slug>.md`** — the human-facing project note in the personal brain (primary vault write target — two-layer model).
5. **Claude Code auto-memory** (`~/.claude/projects/.../memory/`) — durable learnings for future conversations.
6. **Obsidian MCP** (optional, gated) — a visual layer on top of the `_brain/` write.

State lives in `passport.yaml` (schema: `${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml`). Paths follow `${CLAUDE_PLUGIN_ROOT}/rules/folder-map.md`. You are fast and minimal. One confirmation prompt, then save.

---

## Flow

### Step 1: Gather Context

Run these in parallel (single message, multiple Bash calls):

```bash
basename "$(pwd)"
git log --oneline -10
git diff --stat
git diff --cached --stat
```

Then scan:
- `passport.yaml` — `meta.name`, `meta.slug`, `meta.main_wiki`, `pipeline.current_stage`, latest `sessions:` entry.
  **No `passport.yaml`?** Not an error — the Microsimulation and Macro-Fiscal
  repos run BMAD, not the research-os pipeline, and have never had one. Set
  `has_passport = false` and carry it through the rest of this flow: Step 4a
  is skipped entirely (there is no ledger to append to), and every other step
  (journal, personal brain, memory, dashboard) still runs, unaffected.
- `00_admin/process/plans/` for files modified today
- `00_admin/process/sessions/` for files modified today
- The conversation context for key decisions, corrections, or learnings that qualify for auto-memory

### Step 2: Detect Integrations

Run both checks in parallel:

**2a. Wiki registry + personal brain (primary)**

```bash
cat ~/.claude/vaults.json 2>/dev/null || cat ~/.claude/VAULT_PATH 2>/dev/null || echo "VAULTS: not configured"
```

- If `~/.claude/vaults.json` exists, read it to resolve the `_brain/` path (recorded in the registry) and the main wiki path (`passport.yaml` `meta.main_wiki` → path, or skip that specific lookup when `has_passport = false`).
- **Fallback:** if `~/.claude/vaults.json` does not exist, fall back to the legacy single pointer `~/.claude/VAULT_PATH`. If neither exists, the personal-brain write is inactive — proceed without it (passport + journal still capture the session).
- Derive the project slug from `passport.yaml` `meta.slug` **when `has_passport` is true**; otherwise from `basename $(pwd)` lowercased, spaces → hyphens — this is the path every BMAD project already takes, so no passport means no behavior change here at all.
- Target project note: `<_brain>/projects/<slug>.md`. This is where a no-passport project's checkpoint actually lands — see the existing `microsimulation-model.md` / `macro-fiscal-growth-model.md` notes for the shape (their own "Note on workflow" line names BMAD explicitly and says the note exists purely for second-brain visibility).

**2b. Obsidian MCP (secondary, optional)**

```bash
test -f .claude/state/obsidian-config.md && echo "OBSIDIAN: configured" || echo "OBSIDIAN: not configured"
```

If the file exists, read it for the vault path and project-name mapping. Obsidian MCP is a visual layer on top of the `_brain/` filesystem write — not required. If the MCP is unavailable or the config is absent, skip silently.

### Step 3: Draft Updates (present to user for confirmation)

Present a compact summary:

```
## Checkpoint Summary

**Project:** [meta.name] | **Slug:** [meta.slug] | **Branch:** [current branch]
**Stage:** [pipeline.current_stage] | **Session:** [date, ~duration if inferrable]
**Personal brain:** [configured: <_brain>/projects/<slug>.md | not configured]
**Obsidian MCP:** [configured | not configured]

### What happened
- [bullets from git log + conversation context]

### passport.yaml updates
- [if `has_passport`: **sessions:** entry to append — date / summary / next; **pipeline.current_stage:** old → new, if it changed]
- [if not `has_passport`: "Skipped — no passport.yaml (not a research-os pipeline project)". Not an error; every other section below still runs.]

### Journal / handoff updates
- **00_admin/process/journal.md:** [entry to append — if any agent work happened]
- **00_admin/process/sessions/:** [handoff note filename — only if a one-liner is insufficient]

### Personal brain updates
- [if configured: journal entry + Orientation "where we stand" refresh in <_brain>/projects/<slug>.md]
- [if not configured: "Skipped — no ~/.claude/vaults.json or VAULT_PATH"]

### Memory updates
- [new learnings to save — or "None"]

### Discarded as noise
- [failed hypothesis / abandoned approach / debugging dead-end] — [why it didn't work]
- [or "None — nothing explored and rejected this session"]

### Obsidian MCP updates
- [if configured: project note journal entry, dashboard row, daily journal]
- [if not configured: "Skipped — no .claude/state/obsidian-config.md"]
```

**On "Discarded as noise".** List what was explored and rejected — dead-end
hypotheses, approaches abandoned, numbers that turned out wrong — and say why.
This is the section people skip, and it is the one that pays.

A checkpoint's job is to survive compaction. Compaction is lossy in a specific
way: it keeps what was said and drops the reasoning, so a discarded hypothesis
that was discussed at length survives as text while the fact that it was
*rejected* does not. The next session then finds a plausible-looking idea in
its context with nothing marking it as dead, and re-runs it — or worse, cites
it. Naming the rejects explicitly is what stops a failed idea from being
quoted back as a finding.

Keep it to what was genuinely considered and ruled out. If the same dead-end
shows up in three consecutive checkpoints, the confusion is structural: fix the
document or the workflow that keeps regenerating it rather than discarding it
again.

**Ask the user:** "Look right? I'll save all of this." Wait for confirmation or edits.

Skip confirmation if invoked with `--auto` or the user said "just do it".

### Step 4: Save Everything

Execute all saves. Each section is independent — if one fails, the others still run.

#### 4a. passport.yaml — sessions + pipeline stage

**Skip this entire step if `has_passport` is false** — there is no ledger to
append to, and that is not a partial checkpoint, it's the complete one for a
non-research-os project. Steps 4b-4g are unaffected and still run.

Append a `sessions:` entry (newest last), per `rules/logging.md`:

```yaml
sessions:
  - date: "YYYY-MM-DD"
    summary: "<what was done — concrete>"
    next: "<planned next step>"
```

If the pipeline advanced, update `pipeline.current_stage` and the relevant `pipeline.stages.<stage>` (`status`, `score`) to reflect the latest agent/critic result. Append only to `sessions:`; never rewrite prior entries.

#### 4b. 00_admin/process/journal.md

Append only if agent work happened this session (writer, coder, strategist, referee, etc.). Newest-first. Entry format per `rules/logging.md`:

```markdown
### YYYY-MM-DD HH:MM — [Agent Name]
**Phase:** [Discovery/Strategy/Analysis/Writing/Review/Revision/Submission]
**Target:** [file or topic]
**Score:** [XX/100 or PASS/FAIL or N/A]
**Verdict:** [one line — key finding or decision]
**Report:** [path to full report]
```

#### 4c. 00_admin/process/sessions/ (optional longer handoff)

Only when a one-line `sessions:` entry is insufficient (a complex multi-thread session). Write `00_admin/process/sessions/YYYY-MM-DD_<topic>.md` with operations, decisions, results, commits (hashes), and status (done/pending). See `${CLAUDE_PLUGIN_ROOT}/skills/checkpoint/templates/session-report-entry.md`.

#### 4d. Personal brain — `_brain/projects/<slug>.md` (primary, if the registry/pointer resolves)

Write directly to the personal brain filesystem — no plugin or MCP required. This is the human-facing durable project note (two-layer model: human edits live in `_brain/`, not in the Claude-maintained thematic wikis).

1. Resolve `<_brain>` from `~/.claude/vaults.json` (fallback `~/.claude/VAULT_PATH`).
2. Slug from `passport.yaml` `meta.slug`.
3. Target: `<_brain>/projects/<slug>.md`.
4. **If the file does not exist,** create it from the hybrid template `${CLAUDE_PLUGIN_ROOT}/templates/brain-notes/project_template.md` — frontmatter + the `## Orientation` block + an empty `## Journal`. Seed the header (`Working directory`, `Started`) and as much of the Orientation as the session supports.

5. **Append a Journal entry** under `## Journal` (newest first):

```markdown
### YYYY-MM-DD

**Done:**
- [concrete accomplishments from this session]

**Next:**
- [concrete next steps]
```

6. **Refresh the Orientation snapshot.** Rewrite only the `### Where we stand right now (as of <date>)` region — the content between the `<!-- @generated:start checkpoint-orientation -->` and `<!-- @generated:end -->` sentinels — and bump the date. Leave the stable Orientation subsections (question, gap, data, strategy) untouched unless the session changed them, and never edit text outside the sentinels (human free-text). This keeps the refresh bounded within the ~60s budget.

7. **Update frontmatter:** `updated`; `status` if it changed; keep `summary` synced to the one-breath Orientation line.

**Upgrading a legacy note:** if the note is the old bare `# Title / ## Journal` form (no frontmatter/Orientation), upgrade it **additively** on next touch — add frontmatter and insert an Orientation block seeded from the existing content, without rewriting historical journal entries.

Keep it tight — 3–5 bullets per section max. Objective, reusable knowledge (a new concept/method/dataset) goes *down* into the relevant wiki via `/wiki-ingest`; cross-theme/personal insight goes *up* into `<_brain>/synthesis/`. The project note is the session-by-session narrative plus a kept-current Orientation.

#### 4e. Claude Code Auto-Memory

Check existing memory files first — update rather than duplicate. See `${CLAUDE_PLUGIN_ROOT}/skills/checkpoint/templates/memory-entry-types.md` for the four types.

**Qualifies for memory:** user corrections/preferences (`feedback`), project state not in git (`project`), external references discovered (`reference`), user profile updates (`user`).

**Does NOT go in memory:** code patterns/paths/architecture; git history; debugging solutions (the fix is in the code); ephemeral task details.

Write/update memory files with standard frontmatter, then update `MEMORY.md` index. (This is the Claude Code auto-memory feature — distinct from clo-author's retired project-root `MEMORY.md`, which folds into `passport.yaml` + `_brain/learning/`.)

#### 4f. Obsidian MCP (secondary, optional — only if `.claude/state/obsidian-config.md` exists)

Follow the project's `obsidian-config.md` for vault path and project mapping, then add the journal entry / dashboard row / daily-journal entry via the Obsidian MCP. This mirrors the `_brain/` write into the Obsidian app UI; if the MCP is unavailable, 4d already captured the session.

#### 4g. Refresh Project Dashboard

**Skip if `has_passport` is false** — `generate_dashboard.py` renders the
research-os *paper* pipeline (literature, identification, results, review
history) from `passport.yaml`; a BMAD project has none of that state and
nothing to render. Its own dashboard, if it has one, is a separate concern.

Regenerate the living dashboard to capture the latest session state:
```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/generate_dashboard.py" --project-root .
```

### Step 5: Confirm

Report what was saved:

```
Checkpoint saved:
- passport.yaml: [sessions entry added [ + stage → <new> ] | skipped — no passport.yaml, not a research-os project]
- journal.md: [entry added | skipped — no agent work]
- 00_admin/process/sessions/: [note added | skipped]
- Personal brain: [entry added to <_brain>/projects/<slug>.md | not configured]
- Memory: [updated/created N files | no changes]
- Dashboard: [refreshed]
- Obsidian MCP: [entry added to Project Name | not configured]
```

---

## Flags

| Flag | Effect |
|------|--------|
| `--auto` | Skip user confirmation, just save |
| `--memory-only` | Only update Claude Code memory |
| `--scaffold-only` | Update passport + journal + `_brain/projects/<slug>.md`, skip Obsidian MCP |
| `--dry-run` | Show what would be saved, don't save |
| `--setup-obsidian` | Walk the user through creating `.claude/state/obsidian-config.md` from the example template |

---

## Obsidian Config Setup (on demand)

When invoked with `--setup-obsidian`:

1. Check if `.claude/state/obsidian-config.md.example` exists; if not, flag and stop.
2. Copy the example to `.claude/state/obsidian-config.md`.
3. Walk the user through filling in: vault path, project-name mapping for the current working directory.
4. Verify the Obsidian MCP is connected; if not, point the user to the Obsidian REST API plugin setup.
5. Confirm `.claude/state/` is in `.gitignore`.

Do NOT run this on every checkpoint — only when the user explicitly opts in.

---

## Bundled Resources

| Resource | Path | What It Contains |
|----------|------|-----------------|
| Session handoff entry | `${CLAUDE_PLUGIN_ROOT}/skills/checkpoint/templates/session-report-entry.md` | passport `sessions:` YAML + optional `00_admin/process/sessions/` note format |
| Research journal entry | `${CLAUDE_PLUGIN_ROOT}/skills/checkpoint/templates/research-journal-entry.md` | Append format for `00_admin/process/journal.md` |
| Memory entry types | `${CLAUDE_PLUGIN_ROOT}/skills/checkpoint/templates/memory-entry-types.md` | 4 auto-memory types with when-to-save guidance |
| Gotchas | `${CLAUDE_PLUGIN_ROOT}/skills/checkpoint/gotchas.md` | Known failure points and edge cases |

---

## Rules

- **Never invent progress.** Only log what actually happened — from git, conversation, or user confirmation.
- **Be fast.** The whole checkpoint should take under 60 seconds including user confirmation.
- **No passport.yaml is a normal state, not a partial checkpoint.** BMAD/DZ projects (Microsimulation, Macro-Fiscal) never had one and never will. Steps 4a and 4g are the only ones that read/write it; skip exactly those two, run everything else in full, and report it as a skip, not an error.
- **Don't duplicate.** Check existing memory files before creating new ones. Check if today's `_brain/projects/<slug>.md` entry already covers this session.
- **Passport is the ledger.** Session boundaries → `sessions:`; phase/scores → `pipeline.stages`. Never scatter state into per-step files.
- **Two-layer aware.** Human-facing notes → `_brain/`; objective knowledge → wikis via `/wiki-ingest`; the thematic wikis are Claude-maintained and NOT hand-edited by checkpoint.
- **`.claude/state/obsidian-config.md` is local-only.** It contains user-specific paths; `.gitignore` keeps it out of commits.
- **Registry over pointer.** Resolve paths through `~/.claude/vaults.json`; fall back to `~/.claude/VAULT_PATH` only if the registry is absent.
- **Memory is for future conversations.** Don't save things only useful right now.
- **Minimal user friction.** One confirmation prompt. Default to "looks right? saving."

---

## Precedence

If the user has a user-level `checkpoint` skill at `~/.claude/skills/checkpoint/`, this plugin skill takes precedence when invoked from within a research-os project. The user-level skill continues to work for projects that don't use research-os.
