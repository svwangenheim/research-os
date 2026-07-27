---
name: daily-summary
description: End-of-day routine - commits today's work per project, summarizes it, scans mail and Slack if authorized, and logs to _brain/daily/. Use on "daily summary" or "wrap up today".
argument-hint: "[project paths, optional — asked conversationally if omitted]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, ToolSearch, Skill
---

# Daily Summary

End-of-day routine: commit, summarize, and log — per project, then rolled up
into the second brain.

**Input:** `$ARGUMENTS` — optionally one or more project paths. If omitted,
ask conversationally rather than defaulting silently.

## Step 1 — Which projects

**Conversational, not a form.** If `$ARGUMENTS` wasn't given: offer to scan
for likely candidates (git repos with today's-dated commits or uncommitted
changes under common project roots), then ask directly — "Which project(s)
did you work in today? I found `<candidates>` with changes today, if that
helps." One or two exchanges, not a checklist form.

## Step 2 — Per project: commit + summarize

For each confirmed project, in its directory:

1. **Commit today's work** — invoke `/tools commit` (this is the daily
   routine's whole point; running it counts as the explicit ask per
   `git-workflow.md` — still never `--force`, never push/PR unless asked).
2. **Read what changed today**:
   ```bash
   git log --since=midnight --oneline --stat
   ```
   (Adjust `--since` if the user's work session crossed midnight — ask if
   the git log looks empty but they said they worked today.)
3. **Write a short summary** — 3-6 bullets synthesizing the commits and
   `git diff --stat`, not a mechanical commit-message dump. Note stage
   transitions if `passport.yaml` `pipeline.stages` changed today.
4. **Append to `00_admin/process/journal.md`** (newest-first, per
   `${CLAUDE_PLUGIN_ROOT}/rules/logging.md`) — this project's own durable
   record, independent of the cross-project daily log in Step 4.

## Step 2.5 — If nothing changed in a project

Don't force a summary out of nothing. Note it briefly ("no changes in
`<project>` today") and move on — this is the update-over-create /
output-discipline principle applied to daily logging, not just file content.

## Step 3 — Scan Slack + Microsoft 365 mail (best-effort, graceful)

Use `ToolSearch` to look for available Slack and Microsoft 365 mail tools
(query something like `"slack search"` / `"microsoft 365 mail"` /
`"outlook"`). Availability depends on the user having authorized those
connectors in claude.ai's connector settings — this cannot be done from
within a skill.

- **If found:** search for messages from today relevant to the project(s)
  just summarized (mentions of the project name, collaborators, blockers).
  Keep this light — a handful of relevant items, not a full inbox triage.
  Note: this is a narrower, project-scoped scan, not the full multi-channel
  triage the `chief-of-staff` agent does — that agent assumes a different
  stack (Gmail CLI, LINE/Messenger bridges) not present in this setup, so
  this skill talks to the Slack/M365 MCP tools directly instead.
- **If not found:** say so once, briefly, and move on — don't repeat the
  "not authorized" note per project. Never fail the whole routine over it.

## Step 4 — Write the consolidated daily entry

`_brain/daily/<YYYY-MM-DD>.md` (create if absent, otherwise **update in
place** — this is still the same day, not a new artifact). The canonical
layout is the shipped template `${CLAUDE_PLUGIN_ROOT}/templates/brain-notes/daily_template.md`;
the block below is the same content, inline as a fallback:

```markdown
---
title: "Daily Summary — <YYYY-MM-DD>"
note_type: daily
updated: "<YYYY-MM-DD>"
---

# <YYYY-MM-DD>

## Projects

### <project-name>
- <bullets from Step 2>

## Relevant comms
- <items from Step 3, or "none found / not checked — connectors not authorized">
```

## Step 5 — Report

Per-project commit status (committed / nothing to commit), the daily entry
path, and whether Slack/M365 were actually checked or skipped.

## Guardrails

Do not:
- push or open a PR without being separately asked — `/tools commit` commits
  locally, that's the scope of a daily routine
- silently pick projects without confirming — even a good guess gets a
  quick confirm
- fail the whole run because a connector is unavailable — report and continue
- create a second daily file for the same date — update the existing one
- fabricate a project summary when nothing actually changed
