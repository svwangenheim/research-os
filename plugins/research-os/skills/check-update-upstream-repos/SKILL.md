---
name: check-update-upstream-repos
description: Diff research-os's tracked upstream repositories (clo-author, ARS/academic-research-skills, engram, and obsidian-second-brain) against their live current state, summarize what changed since we last looked, and recommend what's worth adopting. Manual, ~bimonthly cadence — not automated. Use when the user asks "check for upstream updates", "is clo-author/ARS ahead of us", "any new engram or obsidian-second-brain changes", or runs this on a schedule they set up themselves.
argument-hint: "[repo name, optional — checks all tracked repos by default]"
allowed-tools: Read, Write, Edit, Bash, WebFetch
---

# Check Update: Upstream Repos

research-os's pipeline is built on three reference repos (clo-author, ARS,
engram) and watches one more for adoptable ideas (obsidian-second-brain).
This skill diffs their **live** current state against what we last looked at —
never a static local mirror, which would itself need to be kept in sync to
stay meaningful as a diff target.

**Input:** `$ARGUMENTS` — optionally a repo name (`clo-author`, `academic-research-skills`,
`engram`, `obsidian-second-brain`) to check just one; otherwise checks every tracked repo.

State lives in `${CLAUDE_PLUGIN_ROOT}/state/upstream-repos.json` — the single
source of truth for what "last checked" means per repo. Read it first.

## Step 1 — Check each tracked repo's live HEAD

For a repo with a non-null `last_seen_sha`:

```bash
git ls-remote https://github.com/<github-slug>.git HEAD
```

Compare the returned SHA to `last_seen_sha`.
- **Same** → up to date. Report and move on; no further steps for this repo.
- **Different** → there's a gap. Continue to Step 2.

If any repo's `last_seen_sha` is `null` (freshly added, not yet baselined):
skip the diff, fetch the current HEAD, and — after the user confirms — record
it as the baseline. Do not fabricate a baseline or diff against nothing.

## Step 2 — Summarize what changed (repos with a gap)

Fetch the commit range between the old and new SHA without cloning:

```bash
gh api "repos/<github-slug>/compare/<last_seen_sha>...<new_sha>" \
  --jq '.commits[] | .sha[0:7] + " " + (.commit.message | split("\n")[0])'
```

If `gh` isn't authenticated or the call fails, fall back to `WebFetch` on
`https://github.com/<github-slug>/compare/<last_seen_sha>...<new_sha>` and
extract the same information from the rendered page.

Read through the commit list. Group into rough categories (new skills/modes,
bug fixes, doc changes, dependency changes, breaking changes) — don't just
paste the raw log.

## Step 3 — Recommend, don't auto-apply

For each repo with real changes, write a short recommendation:
- What changed that's **relevant to research-os** (a new integrity check, a
  new paper-type mode, a scheduling algorithm fix, etc.) — call out
  specifically which of our ported skills/agents/rules it would touch.
- What's **not relevant** (upstream-specific packaging, CI config, docs for
  features we didn't port) — skip these, don't recommend adopting them.
- A concrete next step per relevant item: "port into
  `${CLAUDE_PLUGIN_ROOT}/agents/verifier.md`'s integrity-gate section" or
  similar — specific enough that a future session could act on it directly
  without re-reading the upstream diff.

This is a recommendation, not an action. Do not edit any plugin files in
this skill run — that's separate follow-up work the user decides on.

## Step 4 — Update the state file (only after the user has seen the summary)

Ask before writing. On confirmation, update `last_seen_sha` and
`last_checked` (today's date) for each repo that was actually reviewed —
even if the user decides not to adopt anything, "reviewed and declined" is
still a legitimate reason to advance the baseline. Do not silently update
the state file without the user seeing what changed first.

## Step 5 — Report

Summarize: which repos were checked, which had changes, the recommendations
from Step 3, and confirm which `last_seen_sha` values were updated. Remind
the user this is a manual, ~bimonthly check — not something research-os runs
on its own; if they want it automated, point them at the `/schedule` skill
to set up their own cadence.

## Adding a new tracked repo

When adopting or starting to watch another upstream reference, add an entry
to `state/upstream-repos.json` with a real `last_seen_sha` fetched via
`git ls-remote` at add time — never a placeholder.

## Guardrails

Do not:
- diff against a local checkout — always the live upstream via `git ls-remote`
- fabricate a `last_seen_sha` for a repo — fetch the real HEAD via `git ls-remote`
- silently apply a recommended change — this skill reports, it doesn't edit
- update the state file before the user has seen the summary
- recommend adopting something irrelevant to research-os just because it
  showed up in the diff (upstream's own CI/packaging/docs, features we
  never ported in the first place)
