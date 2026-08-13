---
name: add-thematic-wiki
description: Register a new thematic research wiki - adopt an existing vault on disk or scaffold a new one with the standard numbered layout. Use to start tracking a research theme, or add or split a wiki.
argument-hint: "[theme-name or path to an existing vault]"
allowed-tools: Read, Write, Edit, Glob, Bash
---

# Add Thematic Wiki

Register a wiki with the two-layer knowledge system. This is the only
supported way to add one — never hand-create `<theme>/00_inbox` etc. or
hand-edit `~/.claude/vaults.json`; that skips the shared-template wiring and
the index/README conventions this skill keeps consistent.

**Input:** `$ARGUMENTS` — a theme name to scaffold a new wiki, or a path to an existing vault to adopt. Omitted, the skill asks which of the two you want.

## Step 0: Require the registry

Read `~/.claude/vaults.json`. If it does not exist, stop and tell the user to
run `/wiki-setup` first (it creates the root + registry); re-run
`/add-thematic-wiki` afterward. Do not bootstrap a root here — that's `/wiki-setup`'s job.

Resolve `<ROOT>` = registry `root`, `<BRAIN>` = registry `brain.path`. Also
check `<ROOT>/_templates/` exists (Step 5 below wires new pages to it) — if
it's missing, stop and tell the user to run `/wiki-setup` first to repair the
structure, then re-run `/add-thematic-wiki`.

## Step 0.5: Ask, then branch — adopt or create?

Interview-first, like `/wiki-setup`'s opening: ask directly rather than
guessing from `$ARGUMENTS` alone (a bare word could be a new theme name or an
existing folder name — don't assume).

> "Are we (A) registering a vault you already have somewhere on disk, or (B)
> creating a brand-new empty one?"

If `$ARGUMENTS` looks like a path (contains a slash, or resolves to an
existing directory) rather than a short name, lead with a confirmation
instead of the open question: "Looks like `<path>` already exists — want me
to register that as-is?"

- **(A) Adopt an existing vault** → go to **Path A** below.
- **(B) Create a new empty vault** → go to **Path B** below.

Both paths converge on the shared registration steps (Step 6 onward).

---

## Path A — Adopt an existing vault

For a vault that already has content: another Obsidian vault, a notes folder
from before this system existed, or an unregistered folder already sitting
under `<ROOT>`. Additive-only — never move, rename, or delete anything that's
already there without an explicit per-item confirmation, mirroring
`/wiki-setup`'s existing-setup remediation style.

### A1: Get the path

Ask for the path if not already given (accept relative or absolute; resolve
relative to the cwd). Validate it exists and is a directory — if not, say so
and stop rather than creating one (that's Path B's job).

### A2: Diagnose against the standard layout

Silently check:
- Which of the 8 numbered folders (`00_inbox` … `90_synthesis`) already
  exist?
- Does it have a `README.md`? A `_map.md`?
- Roughly how much content is already inside (a source count is enough — no
  need to read everything)?

Report this back in plain language before touching anything: "This folder
already has `10_sources/`, `20_summaries/`, and a README, but nothing else in
the standard layout. I'd add the 6 missing folders with their generic
placeholder READMEs, and leave everything else untouched — sound right?"

### A3: Fill gaps one at a time, confirmed

Once confirmed, for each **missing** numbered folder only: create it and
copy the matching generic placeholder `README.md` from
`${CLAUDE_PLUGIN_ROOT}/templates/wiki-folder-readmes/<folder>.md` (Step B4
below uses the same set). Never touch a folder that already exists, even if
its README looks different from the standard placeholder.

If there's no `README.md` at the vault's root, offer the short Socratic
scope interview from Path B Step 2 and write one. If a `README.md` already
exists, summarize it back ("looks like this covers X — that the right scope
description to register?") for confirmation rather than overwriting it.

### A4: Decide where it lives

Ask whether to leave the vault at its current path or move/copy it under
`<ROOT>/<slug>/`. Default to **leaving it in place** — `vaults.json` already
supports an arbitrary absolute path per wiki (nothing requires nesting under
`<ROOT>`). Only move it if the user asks, and treat that as its own
confirmed, reversible step (copy first, don't delete the original until
they've confirmed the copy is good).

### A5: Determine the slug

Derive from the folder's own name (normalized to kebab-case, same rule as
Path B Step 1) unless that collides with an existing registry key or isn't
descriptive — ask if ambiguous. Same uniqueness check as Path B: must not
already be a key in `wikis`, and not `_brain` or `_templates`.

Then continue to **Step 6** below.

---

## Path B — Create a brand-new empty vault

### B1: Determine the theme slug

- Use `$ARGUMENTS` if given; otherwise ask: "What should this new wiki be
  called?" (a short theme name — it becomes the folder name).
- Normalize to kebab-case: lowercase, spaces/underscores → hyphens, strip
  anything that isn't `[a-z0-9-]`.
- Check the slug isn't already a key in the registry's `wikis` map, and isn't
  `_brain` or `_templates`. If a folder with that name already exists under
  `<ROOT>` but isn't registered, tell the user and ask how to proceed (adopt
  it via Path A instead vs. pick a different name) rather than silently
  overwriting anything inside it.

### B2: Short Socratic scope interview

**Conversational, not a form.** Ask 1-2 questions at a time in plain text;
wait for replies. Do NOT use `AskUserQuestion`. Keep it to 2-4 exchanges —
just enough to write an honest one-paragraph scope description, modeled on
`vault/cognitive-load/README.md`'s style: what this theme covers, and how it
differs from (or feeds) related work.

Cover:
1. **Scope** — "What does this wiki cover? What research question or family
   of questions does it serve?"
2. **Boundary** — "What's explicitly out of scope — the thing someone might
   expect here but that actually belongs in a different wiki?" (probe gently
   if the answer suggests this should be a section of an existing wiki
   instead of a new one — a new theme should earn its own top-level folder)
3. *(optional, if unclear)* "Which project(s), if any, will this feed?"

### B3: Confirm before creating anything

Summarize: theme slug, one-paragraph scope description, target path
(`<ROOT>/<slug>/`). Get a yes before scaffolding.

### B4: Scaffold the folder tree

```bash
cd "<ROOT>/<slug>"
mkdir -p 00_inbox 10_sources 20_summaries 30_concepts 40_methods 50_datasets 60_people_institutions 90_synthesis
```

Every wiki in this vault documents each numbered folder's purpose with a
short `README.md` — these eight placeholders are generic and
theme-independent (do not customize their content per theme; Path A uses
this same set for whichever folders it's filling in) and are shipped as
standalone files, not re-derived here — copy each one verbatim:

| Folder | Copy from |
|---|---|
| `00_inbox/README.md` | `${CLAUDE_PLUGIN_ROOT}/templates/wiki-folder-readmes/00_inbox.md` |
| `10_sources/README.md` | `${CLAUDE_PLUGIN_ROOT}/templates/wiki-folder-readmes/10_sources.md` |
| `20_summaries/README.md` | `${CLAUDE_PLUGIN_ROOT}/templates/wiki-folder-readmes/20_summaries.md` |
| `30_concepts/README.md` | `${CLAUDE_PLUGIN_ROOT}/templates/wiki-folder-readmes/30_concepts.md` |
| `40_methods/README.md` | `${CLAUDE_PLUGIN_ROOT}/templates/wiki-folder-readmes/40_methods.md` |
| `50_datasets/README.md` | `${CLAUDE_PLUGIN_ROOT}/templates/wiki-folder-readmes/50_datasets.md` |
| `60_people_institutions/README.md` | `${CLAUDE_PLUGIN_ROOT}/templates/wiki-folder-readmes/60_people_institutions.md` |
| `90_synthesis/README.md` | `${CLAUDE_PLUGIN_ROOT}/templates/wiki-folder-readmes/90_synthesis.md` |

New note pages inside this wiki use the shared templates at
`<ROOT>/_templates/` (`concept_template.md`, `method_template.md`,
`dataset_template.md`, `entity_template.md`, `synthesis_template.md`,
`source_summary_template.md`) — they are not duplicated per wiki. The note
conventions (the **In brief** lede, inline `(confidence: …)` tags, and
`(as of YYYY-MM-DD)` freshness stamps) are canonical in the plugin rule
`wiki-integration.md`.

### B5: Write the theme `README.md`

At `<ROOT>/<slug>/README.md`, using the interview answers, modeled on
`vault/cognitive-load/README.md`'s length and tone (2-4 sentences):
```markdown
# <slug>

<one-paragraph scope description from the interview.>

Fully Claude-maintained — see the root `CLAUDE.md` and the plugin's
`wiki-integration.md` for the schema and rules. Don't hand-edit; use
`/wiki-ingest` and `/wiki-maintain`.
```

---

## Step 6: Register in `~/.claude/vaults.json`

Add an entry under `wikis` (never touch `root`, `brain`, or other wikis'
entries). `path` is the vault's actual location — for Path A vaults left in
place, this is wherever they already live, not necessarily under `<ROOT>`:
```json
"<slug>": {
  "path": "<vault path>",
  "description": "<one-line scope>",
  "registered": "<YYYY-MM-DD>"
}
```

## Step 7: Update `<BRAIN>/wikis-index.md`

Add a row to its table:
```markdown
| [[<slug>/README\|<slug>]] | `<slug>/` | <one-line scope> | <YYYY-MM-DD> |
```

## Step 8: Update the root `index.md` Dataview queries (if present)

`<ROOT>/index.md` is Dataview-driven with per-section `FROM` clauses listing
every wiki (e.g. `FROM "cognitive-load/20_summaries" OR
"innovation-policy/20_summaries"`). Extend every `FROM` clause in that file
to include `"<slug>/<folder>"` alongside the existing wikis, for all six
content folders (summaries, concepts, methods, datasets, people/
institutions, synthesis). If the vault lives outside `<ROOT>` (Path A, left
in place), skip this step — Dataview's `FROM` only indexes paths under the
vault root — and say so in the report.

## Step 9: Report

Summarize:
- Which path was taken: adopted an existing vault at `<path>`, or created a
  new one at `<ROOT>/<slug>/`
- Theme registered: `<slug>`
- Path A: which folders/README were added vs. left untouched. Path B:
  folders scaffolded (8) + README placeholders written
- `~/.claude/vaults.json`: entry added
- `_brain/wikis-index.md`: row added
- `index.md`: `FROM` clauses extended (or "outside vault root — skipped" /
  "no `index.md` found — skipped")
- Next step: `/wiki-ingest [source]` to start populating it, or set this as
  a project's `main_wiki` in its `passport.yaml`

## Guardrails

Do not:
- create or adopt a wiki without registering it (always do both together)
- customize the eight per-folder README placeholders per theme — they are
  intentionally generic and consistent across every wiki
- silently reuse an unregistered folder that already has content — ask first
- in Path A, move, rename, or delete any pre-existing file or folder without
  an explicit per-item confirmation
- touch other wikis' entries in `vaults.json` or their rows in
  `wikis-index.md`
- skip the scope interview and guess a description from the slug alone
- guess adopt-vs-create from `$ARGUMENTS` without at least a one-line
  confirmation back to the user
