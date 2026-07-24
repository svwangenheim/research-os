---
name: wiki-setup
description: |
  Structural setup and health-check for the two-layer knowledge model (personal
  brain + Claude-maintained thematic wikis) and the Obsidian vault it lives in.
  Conversational, interview-first — opens by asking whether you already have a
  wiki set up (letting you point to it) rather than silently guessing from
  files, mirroring how the dz-core onboarding skill detects-then-guides. On a
  brand-new machine, creates everything scriptable in one pass — folder
  structure, `_templates/`, root docs (CLAUDE.md/README.md/index.md/log.md),
  `.obsidian` config, the `~/.claude/vaults.json` registry, and
  `~/.claude/settings.json` / `VAULT_PATH` wiring — then runs the profile
  interview (which first summarizes what's already known about you for
  confirmation, then asks only about gaps), and prints the two manual steps a
  skill genuinely cannot do for you (installing the Obsidian app, enabling the
  Dataview plugin). On an existing setup, diagnoses structural drift from the
  standard (missing root docs, missing templates, folder-name typos like
  `60_people_instructions`, stale registry, missing Obsidian config) and walks
  through each fix one at a time before applying it — additive-only, never a
  silent batch fix, never a delete/overwrite. This is a distinct, complementary
  tool from `wiki_quality_check.py` / `/wiki-maintain`, which check content
  quality (summaries, dedup, broken links) inside an already-structurally-sound
  wiki. Idempotent — safe to re-run any time. Use when the user wants to set up
  the personal wiki / second-brain system for the first time, set it up on a
  new computer, "set up my wiki", "initialize the knowledge base", "set up the
  second brain", "check my wiki setup", "is my wiki structured correctly",
  "fix my wiki structure", "set up Obsidian for my wiki", or "why isn't
  Dataview working".
argument-hint: "[path to vault root, only needed if nothing is registered yet]"
allowed-tools: Read, Write, Edit, Glob, Bash
---

# Wiki Setup

Structural setup **and** structural health-check for the research-os two-layer
knowledge model: the registry (`~/.claude/vaults.json`), the personal brain
(`_brain/`), every registered thematic wiki's folder layout, the shared
`_templates/`, the root docs, the `.obsidian` config, and the
`~/.claude/settings.json` / `VAULT_PATH` wiring that makes the vault visible to
Claude. **Idempotent** — re-running it recognizes what already exists,
diagnoses gaps, and never overwrites or deletes existing content.

This skill is about **structure**, not content. It never touches note
*quality* (summary depth, dedup, broken links, canonicalization) — that's
`${CLAUDE_PLUGIN_ROOT}/scripts/wiki_quality_check.py` and `/wiki-maintain`.
Mention that distinction to the user if they seem to be asking about content
rather than structure.

Every invocation starts with **Step 1 — Ask, then diagnose**: a direct,
conversational opening question decides whether you're setting up fresh or
pointing at something existing, and only then does the technical diagnostic
run against the confirmed location. Path comparisons throughout this skill
must be case-insensitive and slash-normalized (`C:/x/y` and `C:\x\y` are the
same path) — never flag a correctly-pointed path as missing just because its
separators or case differ from what you'd write yourself.

Step 1's outcome determines which of the two branches runs: **Step 2A — Fresh
bootstrap** (nothing exists yet, one bulk confirmation, create everything in
one pass) or **Step 2B — Existing / possibly drifted** (something is already
there, walk through each gap one at a time). Both branches converge on the
same **Step 3** (profile interview), **Step 4** (Obsidian manual-step
reminder), and **Step 5** (report).

**Every step in this skill is mandatory, and the full sequence runs
automatically in one invocation.** Step 1 -> (Step 2A or Step 2B) -> Step 3 ->
Step 4 -> Step 5 always executes in order, without stopping between steps and
without waiting for the user to prompt you to continue or to point out that a
step was skipped. Finishing file creation or repair (Step 2A/2B) is a
midpoint, not the end of the run — continue directly into Step 3, then Step
4, then Step 5, in the same response. The only step with a documented,
conditional skip is Step 3 (when `profile.md` is already initialized) — every
other step runs unconditionally, every invocation. Treat stopping after Step
2A/2B — producing a summary, waiting for input, or declaring the run
finished before Steps 3-5 have run or been explicitly accounted for — as an
incomplete execution of this skill.

## Step 1 — Ask, then diagnose

### 1.0 — Open with a direct question (don't silently assume from files)

This skill is interview-first, like `/discover` and the dz-core onboarding
skill: lead with a plain-language question, informed by a quick, silent peek
at what's on disk — but let the user's answer decide, don't let the peek
decide on its own.

1. **Silently peek** (no output yet): does `~/.claude/vaults.json` exist and
   parse with a `root` key? Does `~/.claude/VAULT_PATH` exist? Was a path
   given in `$ARGUMENTS`?
2. **Ask, conversationally** — one plain question, not a form:
   - If the peek found a candidate path, name it and ask for confirmation:
     "I found what looks like an existing wiki registered at `<path>` — is
     that your setup, or do you have a different one I should use instead?"
   - If the peek found nothing: "Do you already have a wiki or second-brain
     set up somewhere on this machine? If so, point me to the folder —
     otherwise I'll set one up fresh for you."
3. **Resolve `<root>` from the answer**, not from the peek alone:
   - User confirms the found path, or gives a different existing path → that
     is `<root>`. Proceed to 1.1 (the diagnostic runs against it — an
     existing answer doesn't mean it's already correct, just that it's not
     starting from nothing).
   - User says they don't have one / wants a fresh start → skip the
     structural checks (1.1–1.10 don't apply — there's nothing to diagnose
     yet); ask where to put it if `$ARGUMENTS`/`VAULT_PATH` didn't already
     suggest a path (offer a sensible default, e.g. `~/Research-OS/vault`),
     and go straight to **Step 2A**.
   - User isn't sure ("I don't know if I have one"): offer to look — check
     `$ARGUMENTS` → `~/.claude/VAULT_PATH` → common locations (e.g.
     `~/Research-OS/vault`) — report what you find and let them decide from
     that, rather than guessing on their behalf.

### 1.1–1.10 — Structural checks (only once a root is confirmed as existing)

Run each check against the candidate root. Classify every gap found as one of:
**auto-fixable** (Step 2B will offer a yes/no fix), **manual-only** (goes into
the Step 4 reminder, never a yes/no), or **informational** (flagged, never
auto-registered).

1. **Registry.** Does `~/.claude/vaults.json` exist and parse as valid JSON
   with `root`, `brain`, and `wikis` keys? *(auto-fixable: create it)*
2. **Registry root on disk.** Does the registry's `root` path actually exist?
   *(auto-fixable: recreate the full structure at that path — effectively
   Step 2A's creation pass, run inside Step 2B and confirmed like any other
   finding)*
3. **Root docs.** Do `<root>/CLAUDE.md`, `README.md`, `index.md`, `log.md`
   all exist? Check each independently. *(auto-fixable per missing file: copy
   from `${CLAUDE_PLUGIN_ROOT}/templates/vault-root/`)*
4. **`_templates/`.** Does `<root>/_templates/` exist, and does it contain all
   11 templates — the 6 wiki-note templates (`concept_template.md`,
   `method_template.md`, `dataset_template.md`, `entity_template.md`,
   `source_summary_template.md`, `synthesis_template.md`) and the 5 brain-note
   templates (`daily_template.md`, `weekly_template.md`, `thought_template.md`,
   `learning_template.md`, `project_template.md`)? *(auto-fixable per missing
   file: copy wiki templates from `${CLAUDE_PLUGIN_ROOT}/templates/wiki-notes/`,
   brain templates from `${CLAUDE_PLUGIN_ROOT}/templates/brain-notes/`)*
5. **`_brain/`.** Does `<root>/_brain/` exist with `profile.md`,
   `wikis-index.md`, `README.md`, and the six subfolders `daily/ weekly/
   thoughts/ projects/ synthesis/ learning/` — **each subfolder containing a
   `README.md`**? *(auto-fixable per missing piece: create the missing
   subfolder, copy `_brain/README.md` from
   `${CLAUDE_PLUGIN_ROOT}/templates/brain/README.md`, copy each folder
   `README.md` from `${CLAUDE_PLUGIN_ROOT}/templates/brain/folder-readmes/<folder>.md`,
   or recreate `profile.md` / `wikis-index.md` — see Step 2B)*
6. **Per-wiki folder layout.** For each registered wiki (from the registry's
   `wikis` map), or — if there is no registry yet — any folder directly under
   the candidate root that contains a `10_sources/` subfolder: check all 8
   subfolders exist with the **correct** names (`00_inbox`, `10_sources`,
   `20_summaries`, `30_concepts`, `40_methods`, `50_datasets`,
   `60_people_institutions`, `90_synthesis`) and each has a `README.md`.
   Specifically check for the old typo `60_people_instructions` sitting where
   `60_people_institutions` should be. *(auto-fixable per missing
   folder/README — copy the matching file from
   `${CLAUDE_PLUGIN_ROOT}/templates/wiki-folder-readmes/`; the typo is a
   **rename**, not a pure addition — describe exactly what will be renamed
   and get the same explicit yes/no as any other finding, never treat it as
   more automatic)*
7. **`.obsidian/` config.** Does `<root>/.obsidian/` exist? Do
   `core-plugins.json`, `templates.json`, `community-plugins.json` exist
   inside it? *(auto-fixable per missing file: copy from
   `${CLAUDE_PLUGIN_ROOT}/templates/obsidian/`)*
8. **Dataview usability.** Does `<root>/.obsidian/plugins/dataview/manifest.json`
   exist? An entry in `community-plugins.json` is not enough — that file can
   be stale or aspirational; only the actual plugin files under
   `.obsidian/plugins/dataview/` mean Dataview is usable. **Never a yes/no
   finding** — if missing, it always goes into the Step 4 manual-step
   reminder instead, since a skill cannot fetch third-party plugin code.
9. **Claude-side wiring.** Does `~/.claude/settings.json`'s
   `permissions.additionalDirectories` include `<root>`? Does
   `~/.claude/VAULT_PATH` exist and point at `<root>`? Check each
   independently. *(auto-fixable: merge `<root>` into
   `additionalDirectories` without touching any other entry; write/update
   `VAULT_PATH`)*
10. **Unregistered wiki-looking folders.** Any top-level folder under
    `<root>` with a `10_sources/` subfolder that is *not* a key in the
    registry's `wikis` map. *(informational only — never silently register
    it; point to `/add-thematic-wiki`, exactly as before)*

You cannot reliably detect whether the **Obsidian desktop app itself** is
installed — there's no cross-platform file or command probe worth trusting.
Don't try. Always include the "make sure Obsidian is installed and this
folder is opened as a vault" reminder in Step 4, exactly once, regardless of
every other finding — it is never a numbered finding.

### 1.11 — Decide the branch

The branch follows primarily from the user's **Step 1.0 answer**, not from
file state alone:

- **Step 2A (fresh bootstrap)** if the user said they don't have one / want a
  fresh start. Skip 1.1–1.10 entirely — there's nothing to diagnose.
- **Step 2B (existing / possibly drifted)** if the user pointed you at a
  path, confirmed a found one, or wasn't sure and you located one together.
  Run 1.1–1.10 against it regardless of how populated it turns out to be —
  the user told you it's "their wiki," so even a mostly-empty result is
  drift to repair, not a reason to silently re-route to Step 2A.
  - **Edge case:** if that path turns out to not exist on disk at all, or is
    completely empty (nothing checks 3–9 would find), don't decide for the
    user — say so and ask directly: "That folder doesn't exist yet, or is
    empty — did you mean a different path, or should I set up a fresh wiki
    there?" Their answer picks the branch from here.

Nothing ambiguous or customizable is at stake in Step 2A specifically because
the user has already told you there's nothing there to protect; in Step 2B
something might be intentionally customized, so every fix is confirmed
individually.

## Step 2A — Fresh bootstrap

1. The root was already resolved in Step 1.0. If it doesn't exist yet, note
   that it will be created.
2. Give **one** summary confirmation naming everything that will be created —
   not a per-item confirmation, since nothing existing is at risk:
   > I'll set up the full wiki/second-brain structure at `<root>`: the
   > `_brain/` folders, `_templates/`, the root docs (CLAUDE.md, README.md,
   > index.md, log.md), the `.obsidian` config, and register it in
   > `~/.claude/vaults.json` (plus wire it into `~/.claude/settings.json` and
   > `~/.claude/VAULT_PATH`). Proceed?
3. On yes, create everything in one pass:
   - `<root>/_templates/` ← copy all wiki-note templates from
     `${CLAUDE_PLUGIN_ROOT}/templates/wiki-notes/` **and** all brain-note
     templates from `${CLAUDE_PLUGIN_ROOT}/templates/brain-notes/`.
   - `<root>/CLAUDE.md`, `README.md`, `index.md`, `log.md` ← copy from
     `${CLAUDE_PLUGIN_ROOT}/templates/vault-root/`.
   - `<root>/_brain/README.md` ← copy from
     `${CLAUDE_PLUGIN_ROOT}/templates/brain/README.md`.
   - `<root>/_brain/{daily,weekly,thoughts,projects,synthesis,learning}/`,
     each with a `.gitkeep` and a `README.md` copied from
     `${CLAUDE_PLUGIN_ROOT}/templates/brain/folder-readmes/<folder>.md`.
   - `<root>/_brain/profile.md` ← copy the uninitialized placeholder from
     `${CLAUDE_PLUGIN_ROOT}/templates/brain/profile-placeholder.md`.
   - `<root>/_brain/wikis-index.md` ← copy the empty-wikis version from
     `${CLAUDE_PLUGIN_ROOT}/templates/brain/wikis-index-empty.md`.
   - `<root>/.obsidian/` ← copy all 5 files from
     `${CLAUDE_PLUGIN_ROOT}/templates/obsidian/`.
   - Write `~/.claude/vaults.json`:
     ```json
     {
       "$schema": "research-os vault registry v1",
       "root": "<absolute root path, forward slashes>",
       "brain": {
         "path": "<root>/_brain",
         "description": "Personal second brain: profile, daily/weekly notes, thoughts, per-project journals, personal + cross-theme synthesis, durable learnings."
       },
       "wikis": {}
     }
     ```
   - Merge `<root>` into `~/.claude/settings.json`'s
     `permissions.additionalDirectories` (create the key/array if absent;
     read-modify-write, preserving every other key untouched), and write
     `~/.claude/VAULT_PATH` with the root path.
4. Continue to **Step 3** (profile interview — triggers because `profile.md`
   is freshly the placeholder).
5. Print **Step 4** (Obsidian manual-step reminder).
6. Produce **Step 5** (report).

## Step 2B — Existing / possibly drifted

1. Step 1 already ran the full diagnostic.
2. **If zero structural findings** (checks 1–7, 9 all clean; check 8 and the
   Obsidian-app reminder are handled in Step 4 regardless): say so plainly —
   "structure looks correct, nothing to fix" — then continue to **Step 3**
   (profile interview) and the check-10 unregistered-folder flagging below.
3. **If findings exist:** first list **all** of them as a single clear
   numbered report, each with what's wrong, what the fix would be, and
   whether it's auto-fixable or manual-only (dataview, check 8, is always
   manual-only here). Then walk through each **auto-fixable** finding **one
   at a time**, in order, asking a plain yes/no before applying it — never a
   single batch confirmation, never a silent fix. On "no", skip it, note it
   as declined in the running list, and move to the next finding.
   - **Principle: fixes are additive-only.** Create missing files/folders;
     never delete or overwrite something that already has content — even if
     it looks like boilerplate (e.g. a root `README.md` may be deliberately
     customized).
   - **Exception — the folder-name typo** (`60_people_instructions` →
     `60_people_institutions`): this is a rename/move, not a pure addition.
     Describe exactly what will be renamed (source path → destination path,
     and that its contents move with it) and get the same explicit
     confirmation as any other finding — do not treat it as more automatic
     just because the fix is "obvious."
   - The 8 generic per-folder placeholder `README.md` bodies used when
     scaffolding a wiki folder are shipped templates, one file each, at
     `${CLAUDE_PLUGIN_ROOT}/templates/wiki-folder-readmes/<folder>.md` — copy
     the matching one verbatim rather than re-deriving or duplicating it
     here (the same files `/add-thematic-wiki` copies from).
   - When check 5 needs to recreate `wikis-index.md` from scratch (missing
     entirely, not just missing rows), seed it with the registry's *current*
     wikis rather than leaving it empty — mirror the real table format (see
     Step 2A's empty version for the header; add one row per registered
     wiki).
4. The **dataview-plugin-files-missing** finding (check 8) is never offered
   as a yes/no fix here — it is always resolved via Step 4's manual-step
   reminder, since a skill cannot fetch third-party plugin code.
5. Continue with **Step 3** (profile interview) and the check-10
   unregistered-folder flagging below.

## Step 3 — Personal brain interview (only if `profile.md` is uninitialized)

Read `<brain>/profile.md`. If it does **not** contain the marker **"Not yet
initialized,"** the profile is already set up — report that and **skip this
entire step**; do not re-interview or overwrite an existing profile. If it
does contain the marker, run 3.0 then 3.1 below — don't jump straight to
asking questions from a blank slate.

### 3.0 — Summarize what's already known, before asking anything

Gather whatever is already legitimately available, without fabricating or
overreaching into unrelated projects' private context:
- **This project's auto-memory**, if loaded into your context for this
  session (the `MEMORY.md` index and any linked memory files under this
  project's `~/.claude/projects/.../memory/`) — it exists specifically to
  carry standing understanding of the user forward; use it.
- **The conversation so far** — anything the user has already told you this
  session (or that you've directly observed, e.g. what they're working on,
  how they've asked you to work) that's relevant to who they are or how they
  want to collaborate.
- **`git config user.name` / `user.email`**, if set — a lightweight, common
  signal (`git config --get user.name`, `git config --get user.email`).
- **Any ambient system context** you've been given (e.g. an email address),
  and what it implies (domain → likely organization) — label this as
  inferred, not confirmed.
- **A partially-filled existing `profile.md`**, if this is a re-run after an
  earlier incomplete attempt — don't discard prior answers.

Do not go hunting through unrelated projects' memory or files — this is about
what's already legitimately in view, not a search task.

### 3.1 — Present the summary, then interview only the gaps

Open with the summary, clearly distinguishing **stated** (the user told you
or it's in memory) from **inferred** (you're guessing from a signal like an
email domain), then ask for correction and what's missing — in one message,
not a wall of separate questions:

> Here's what I already know or can infer about you: [bulleted summary, each
> item tagged inline as *(from memory)*, *(you mentioned earlier)*, *(from
> your email domain)*, etc.]. Does this look right? What's missing or wrong?

**This is conversational**, like the rest of this skill and `/discover`. Ask
in plain text, one or two things at a time, wait for the reply. Do NOT use
`AskUserQuestion`. After the user confirms/corrects the summary, continue —
but only ask about what's still genuinely missing from the three areas
below; skip anything the summary already covered and the user confirmed.
Keep it short: the goal is filling real gaps, not a fixed question count.

1. **Who you are** — role/institution, primary research focus or domain(s),
   what they're generally working on. (Likely partially known already.)
2. **How Claude should work with you** — collaboration style: how much
   autonomy to take, how much to explain vs. just do, tone/terseness
   preferences, anything Claude should always or never do.
3. **Standing context** — recurring constraints, deadline rhythms,
   tools/workflow habits that should carry across every session.

Be curious, not prescriptive — draw out how the user actually wants to work,
don't impose a template. Know when to stop once the picture is clear.

Write the result to `<brain>/profile.md`, replacing the placeholder, using
the file's own section structure:
```markdown
---
title: "Profile"
note_type: profile
updated: "YYYY-MM-DD"
---

# Profile

## Who I am

## How Claude should work with me

## Standing context
```
Keep it tight — a handful of bullets per section synthesizing the confirmed
summary plus what was newly learned, not an essay, and never fabricated
content beyond what was actually confirmed or stated. Tell the user
afterward: "This file is yours — edit it directly any time your context
changes; you don't need to re-run `/wiki-setup` for small updates."

## Step 4 — The Obsidian manual-step reminder

Print this once, near the end of every run, regardless of branch and
regardless of what else was found — these two things genuinely cannot be
done by a skill, only detected:

1. **If check 8 found no `.obsidian/plugins/dataview/manifest.json`** (or
   `.obsidian/` doesn't exist yet at all): note that the wiki's `index.md`
   tables need the Dataview plugin to render, and it has to be installed
   through the Obsidian UI:
   - Open the vault in Obsidian, then Settings → Community plugins → turn
     off Restricted mode if it's on → Browse → search "Dataview" → Install →
     Enable.
   - `community-plugins.json` will populate itself once Dataview is enabled
     this way — don't hand-edit it.
2. **Always**, regardless of check 8's result: remind the user that Obsidian
   the desktop app itself can't be detected or installed by this skill —
   if it isn't already running against this vault: download it from
   https://obsidian.md, install it, then use "Open folder as vault" pointing
   at `<root>`.

Keep both to a few lines each — exact steps, not a tutorial.

## Step 5 — Report

Summarize:
- **Branch:** fresh bootstrap | existing (clean) | existing (repaired N of M
  findings)
- **Registry:** already existed (recognized N wikis) | created (registered N
  wikis + `_brain`)
- **Structural findings:** if Step 2B ran with findings, a short table — #,
  what, fix applied / declined / manual-only
- **Brain structure:** already present | scaffolded this run
- **Profile interview (Step 3):** already initialized, skipped | ran this run,
  profile written — never report the run as complete if this line is missing
- **Obsidian config:** created/present; **Dataview:** usable (plugin files
  found) | not yet enabled (see manual steps)
- **Manual steps still pending:** the Step 4 items, kept visually separate
  from anything that actually failed
- **Wikis registered:** a small `theme -> path` table
- **Unregistered folders found:** (if any, from check 10) → point to
  `/add-thematic-wiki`
- **Next steps:** `/add-thematic-wiki` to register a new theme, `/wiki-pull` to start
  pulling from what's here

## Guardrails

Do not:
- stop the run after Step 2A/2B file creation or repair and call it done —
  Steps 3, 4, and 5 are mandatory and always continue in the same response;
  the Step 5 report is the only valid end point for this skill
- decide fresh-vs-existing from file state alone without asking — Step 1.0's
  question is the decider; a technical peek only informs how you phrase it
- overwrite or delete existing content — every fix is additive, or (for the
  one rename case) an explicitly-confirmed move that preserves contents
- silently batch-apply Step 2B's fixes — each auto-fixable finding gets its
  own yes/no, after the full list has been shown once
- treat the folder-name-typo rename as more automatic than any other
  finding just because the fix seems obvious
- offer the Dataview-plugin-files-missing finding as a yes/no fix — it is
  always resolved via the Step 4 reminder, never invented, never claimed
  "enabled" when only the `community-plugins.json` entry exists
- re-run the profile interview if `profile.md` is already initialized
- jump straight to Step 3.1's questions without first doing 3.0's summary —
  the user confirms/corrects what's already known before being asked to
  repeat it
- present an inferred fact (e.g. organization from an email domain) as if it
  were confirmed — label stated vs. inferred in the 3.0 summary
- fabricate profile content — only write what the user actually confirmed or
  stated
- silently register a wiki folder found on disk into the registry — flag it
  (check 10) and point to `/add-thematic-wiki` instead, so it gets scaffolded and
  described properly
- create a second, competing vault root if one is already registered
- claim "all clean" if any auto-fixable finding was declined or any manual
  step is still outstanding — name it explicitly in the report instead
