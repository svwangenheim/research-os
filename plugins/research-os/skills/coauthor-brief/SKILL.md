---
name: coauthor-brief
description: Write a handoff brief so a coauthor can take over a piece of the project - git delta by area, pipeline and integrity roll-up, open blockers, environment, and data-access process. Use on "brief my coauthor", "onboard someone onto this paper", "write a handoff for the RA", "what does X need to know to pick up the analysis". NOT for saving your own session state (use /checkpoint).
argument-hint: "[--since <tag|date|Ndays>] [--for <name>] [--no-data-section]"
allowed-tools: Read,Grep,Glob,Write,Bash
disable-model-invocation: true
---

# Coauthor Brief

`/checkpoint` answers **"where am I"** — it persists the session so *you* can
resume tomorrow. `/coauthor-brief` answers **"what do I need to know to take over
a piece of this"** — it produces a document for *someone else* who is starting
cold, has not been in any of these sessions, and needs to be productive without
asking you twenty questions.

That distinction drives every choice below. A checkpoint can rely on shared
context; a brief cannot. Anything the reader would have to already know is
either written out or named as an open question.

State lives in `passport.yaml` (schema:
`${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml`). Paths follow
`${CLAUDE_PLUGIN_ROOT}/rules/folder-map.md`.

---

## Hard rules

- **This skill writes a document and nothing else.** It does not push, open a
  PR, merge, tag, run analysis scripts, or re-run the pipeline. Every `Bash`
  call it makes is a read (`git log`, `git diff --stat`, `git status`, file
  listings). If the brief needs a number that only a rerun would produce, it
  says so and stops.
- **It carries the process to obtain data access, never the data.** No restricted
  values, no live paths into a secure enclave or network share, no credentials,
  no API keys, no tokens, no connection strings, no row counts or summary
  statistics from restricted microdata. What goes in the brief is the sequence a
  coauthor follows to get their own access: which provider, which application
  form, which approval, expected wait, who to name as PI.
- **Never invent state.** Everything in the brief traces to git, `passport.yaml`,
  a file in `00_admin/process/`, or a lockfile. If something is unknown, the
  brief says "unknown" and puts it in Open questions.
- **Facts, not reassurance.** A brief that reads as though everything is fine is
  useless to whoever inherits the problem.

---

## Phase 0 — Resolve the "since" window

The brief covers a window of work. Resolve it in this order and **echo the
resolved window before gathering anything**:

1. **`--since <tag|date|Ndays>`** if given. Accepts a git tag or ref
   (`v0.2`, `HEAD~40`), an ISO date (`2026-07-01`), or an N-day form
   (`30days`, `14d`).
2. Otherwise, **the most recent brief in `00_admin/process/handoffs/`**. Take its
   date from the filename (`YYYY-MM-DD_coauthor-brief.md`) and use that as the
   window start.
3. Otherwise, **14 days**.

```bash
ls -1 00_admin/process/handoffs/*_coauthor-brief.md 2>/dev/null | tail -1
```

Then print one line and continue:

```
Window: since 2026-07-14 (last brief) — 28 days, 41 commits.
```

If the resolved ref does not exist in this repo (a tag that was never pushed, a
date before the first commit), say so and fall back to 14 days rather than
failing.

---

## Phase 1 — Gather

Run the git reads in parallel (single message, multiple `Bash` calls):

```bash
git log --oneline --since="<window>"
git diff --stat <window-ref>..HEAD
git status --porcelain
git log --since="<window>" --format="%an" | sort | uniq -c
```

### 1a. Git delta, grouped by area

Do not hand the reader a flat commit list. Group the changed files into the four
areas a coauthor divides work along, and describe each group in prose:

| Area | Paths |
|---|---|
| **Manuscript** | `04_paper/`, `01_literature/` |
| **Analysis** | `03_analysis/`, `02_data/` |
| **Talks and outreach** | `05_outreach/` |
| **Infrastructure** | `00_admin/`, `.claude/`, `CLAUDE.md`, lockfiles, build config |

For each area: what changed, why (from commit messages and
`00_admin/process/journal.md`), and what state it is in now. Uncommitted work in
`git status --porcelain` gets its own line — it is invisible to anyone who
clones, and it is the single most common thing a handoff loses.

### 1b. Pipeline and integrity roll-up

From `passport.yaml`:

- `pipeline.current_stage` and, per stage, `status`, `score`, `gate`. Say which
  gates are met and which are not.
- `integrity.last_gate`, `claims_verified` / `claims_total`, and every entry in
  `integrity.unresolved`. A non-empty `unresolved` list is blocking for
  `/submit` — state that explicitly, because a new coauthor will not know it.
- Any `claim_manifest` entry whose status is `FAIL`, `EXPLAINED`, or `STALE`,
  with the claim text and its `evidence_origin`. `EXPLAINED` needs its named
  alternative spelled out; without one it is not explained.

### 1c. Open plan items and blockers

Read `00_admin/process/`:

- `plans/` — unchecked items in the most recent plans, with the plan filename.
- `decisions/` — decisions taken in the window that constrain future work. A
  coauthor who reopens a settled question wastes a week.
- `journal.md` — the last few entries, for narrative that the commit log does not
  carry.
- Anything labelled blocked, waiting, or pending anywhere in `00_admin/process/`.

### 1d. Environment

Find what a coauthor needs to reproduce the analysis:

```bash
ls -1 renv.lock requirements.txt environment.yml uv.lock Manifest.toml Project.toml 2>/dev/null
ls -1 03_analysis/scripts/R 03_analysis/scripts/py 03_analysis/scripts/jl 2>/dev/null
```

Report which lockfiles exist, which languages the pipeline actually uses, and
the entry point (the master script, or the numbered script order). If no lockfile
exists for a language that is in use, that is a blocker for the coauthor and goes
in Open questions with a pointer to `/submit environment`.

### 1e. Data access

Skipped entirely under `--no-data-section`.

For each data source in `passport.yaml` and `02_data/codebooks/`, record:

- Provider and the dataset's public name.
- **Access class:** public download, registration required, application and
  approval required, or secure-enclave/on-site only.
- **The steps to obtain access**, as a coauthor would follow them: the form, the
  approving body, what has to be attested, typical wait time, and who is already
  named on the existing approval.
- Any usage constraint that survives access: output-disclosure review, no
  redistribution, embargo, citation requirement, deletion deadline.

Then stop. Do not record where the data currently sits on this machine or any
network share, do not paste any value from it, and do not include credentials of
any kind. If a codebook or script contains a live restricted path, describe the
source without reproducing the path. This follows
`${CLAUDE_PLUGIN_ROOT}/rules/confidential-data.md`: access is per-person and
per-agreement, so a coauthor without the data-use agreement gets the application
route, not a shortcut around it. Numbers built on restricted data also need
disclosure clearance before they appear anywhere, which includes this brief —
when in doubt, name the table rather than quoting a figure from it.

---

## Phase 2 — Write the brief

Structure, in this order. Every section is present even when short; an empty
section says "none" rather than being dropped, so the reader knows it was
considered.

```markdown
# Coauthor brief — <project name>
**Prepared:** YYYY-MM-DD · **Window:** <resolved window> · **For:** <name or "any coauthor">
**Stage:** <pipeline.current_stage> · **Integrity:** <PASS | N unresolved>

## What this paper is
Question, contribution, and current headline result in five sentences or fewer.
Written for someone who has not read the draft.

## Where it stands
Stage-by-stage: what is done, what is in progress, what has not started.
Gates met and gates not met, with the numbers.

## What changed in this window
### Manuscript
### Analysis
### Talks and outreach
### Infrastructure
Prose per area. Uncommitted work called out separately.

## What you would be taking over
The specific piece of work this brief hands off, its current state, its entry
point in the repo, and what "done" looks like for it.

## How to run it locally
Clone, restore the environment, the entry-point script, expected runtime, and
where output lands. Exact commands.

## Data access
Per source: provider, access class, the steps to get your own access, usage
constraints. Process only — no paths, no values, no credentials.

## Open questions and blockers
Numbered. Each with who or what it is waiting on. Include everything the
gathering phase could not resolve.

## Decisions already taken
So they are not reopened. Each with its date and the file it is recorded in.

## Where to look
| What | Path |
|---|---|
| State ledger | passport.yaml |
| Research journal | 00_admin/process/journal.md |
| Plans | 00_admin/process/plans/ |
| Manuscript | 04_paper/academic_paper/ |
| Analysis scripts | 03_analysis/scripts/ |
```

Write in plain declarative prose. Name files by path. Where the brief asserts a
state, name the source of that assertion. No summary that softens a blocker.

---

## Phase 3 — Save and report

Save to `00_admin/process/handoffs/YYYY-MM-DD_coauthor-brief.md`, creating the
directory if it does not exist:

```bash
mkdir -p 00_admin/process/handoffs
```

If a brief with today's date already exists, overwrite it — same-day reruns are
a correction, not a second brief.

Then print exactly one line:

```
Brief written: 00_admin/process/handoffs/2026-08-11_coauthor-brief.md — 28-day window, 41 commits, 3 blockers, integrity 2 unresolved.
```

Nothing else. The document is the output.

---

## Flags

| Flag | Effect |
|------|--------|
| `--since <tag\|date\|Ndays>` | Set the window start explicitly. Git tag or ref, ISO date, or `Ndays`. Overrides the last-brief and 14-day defaults. |
| `--for <name>` | Address the brief to a named coauthor. Sets the `For:` header and lets the "What you would be taking over" section name their specific piece. |
| `--no-data-section` | Omit the Data access section entirely. Use when the recipient will not touch the data, or when the sources are restricted enough that even the access process is not shareable. |

---

## Rules

- **A brief is written, not pushed.** No git mutation, no PR, no merge, no
  rerunning analysis. Reads only.
- **Access process, never access.** Restricted values, live data paths, and
  credentials never enter the document, per
  `${CLAUDE_PLUGIN_ROOT}/rules/confidential-data.md` ("a handoff carries
  instructions to obtain access, never the data"). If in doubt about a line, cut
  it — a coauthor can ask for a detail, but a leaked path or value cannot be
  recalled.
- **Echo the window before gathering.** The reader of the brief and the person
  running the command must both know what period it covers.
- **Unknown is a valid answer.** Put it in Open questions rather than guessing.
- **Blockers are not softened.** Unmet gates, unresolved integrity items, missing
  lockfiles, and stale claims appear plainly.
- **Not a checkpoint.** This does not write `passport.yaml`, the journal,
  `_brain/`, or auto-memory. If the session also needs saving, run `/checkpoint`
  separately.

---

## Precedence

`/coauthor-brief` is `disable-model-invocation: true` — it runs only when
invoked by name. Writing a handoff document is a deliberate act with a named
audience, not something to trigger from context.
