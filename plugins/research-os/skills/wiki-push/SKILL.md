---
name: wiki-push
description: Write durable knowledge from this session back - personal synthesis UP into _brain/, objective concept, method, and dataset knowledge DOWN into the thematic wiki. Use after work blocks.
argument-hint: "[--wiki <theme>] [--no-autowrite] [optional: specific notes or topic to push]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task
---

# Wiki Push

Write durable knowledge from the current project back into the two-layer
knowledge model. This is a **global** skill: it works standalone and inside
any research-os project.

## Goal

Turn project work into reusable long-term knowledge, routed to the layer
that actually owns it:

- **UP into `_brain/`** — the session's own narrative, personal reasoning,
  and any synthesis that is personal or spans multiple themes. This is now
  wiki-push's **primary** job.
- **DOWN into the thematic wiki** — objective, source-grounded knowledge that
  any future project on this theme could reuse (new/updated concept, method,
  or dataset pages; theme-internal synthesis when a result changes the
  picture within one theme).

This skill should:
- identify what is worth preserving, and in which layer
- distinguish durable knowledge from temporary project clutter
- update existing notes where possible, in either layer
- create clean new notes only when needed
- keep both layers coherent and non-duplicative

## Resolve the knowledge layers

1. **Read the registry** `~/.claude/vaults.json`. If it exists, use it
   (`brain.path` + the `theme -> path` map).
2. **If it does not exist**, fall back to `~/.claude/VAULT_PATH` (one flat
   legacy vault — no `_brain` split; everything durable goes there, skip the
   `_brain` routing below).
3. **If neither exists**: stop — say the knowledge layer is not available,
   ask the user to run `/wiki-setup`, and do not invent file updates.
4. **Pick the target wiki** (full algorithm:
   `${CLAUDE_PLUGIN_ROOT}/rules/wiki-integration.md` §"Picking the target
   wiki — no project required"): `--wiki <theme>` argument > current
   project's `passport.yaml` `meta.main_wiki` > a `.research-os-wiki` pin
   file in the cwd (`wiki:` value) > the registry's only wiki > ask the user
   (list registered themes, wait for the answer, then offer to write the pin
   file so this folder doesn't ask again).
5. Resolve `<WIKI>` and `<BRAIN>` (`brain.path`).

## Routing: which layer does this belong in?

| This session produced... | Goes to | Why |
|---|---|---|
| A session narrative (what happened, decisions made, next steps) | `<BRAIN>/projects/<slug>.md` | Personal, project-specific — not reusable by other themes/projects |
| An insight that reframes how the user thinks about their own research program, spanning >1 theme | `<BRAIN>/synthesis/` | Personal/cross-theme — not a single-theme objective fact |
| A new or sharper understanding of a concept/method/dataset, grounded in sources | `<WIKI>/30_concepts/`, `/40_methods/`, `/50_datasets/` | Objective, theme-scoped, reusable by any future project on this theme |
| A comparison/synthesis across multiple papers **within this one theme** | `<WIKI>/90_synthesis/` | Theme-internal — stays in the wiki, not `_brain/` |
| A clean paper summary that doesn't exist yet | Not this skill — run `/wiki-ingest` | Single-source ingest is a separate, dedicated flow |

**Good candidates (either layer):** method lessons, dataset notes, conceptual
clarifications, synthesis across sources, reusable project insights,
definitions that will matter again, decisions future work may benefit from.

**Poor candidates:** scratch notes, temporary logistics, half-formed
thoughts, duplicate notes, raw copied text without synthesis, clutter with no
reuse value in either layer.

## Inputs to Inspect

Check, when available:
- the current user request and recent session outputs/decisions
- `wiki-links.md` in the current project
- `<BRAIN>/projects/<slug>.md` (does today's entry already cover this?)
- the wiki structure: `<WIKI>/20_summaries/`, `/30_concepts/`, `/40_methods/`,
  `/50_datasets/`, `/60_people_institutions/`, `/90_synthesis/`

## Workflow

### Step 1: Identify durable knowledge, and classify by layer
Decide what has been learned that deserves to survive beyond this session,
then route each item using the table above.

### Step 2: Push UP into `_brain/`
- **`<BRAIN>/projects/<slug>.md`** — if the file doesn't exist, create it
  from the hybrid template `${CLAUDE_PLUGIN_ROOT}/templates/brain-notes/project_template.md`
  (frontmatter + `## Orientation` + `## Journal`). Append project-specific
  durable takeaways in a distinct `## Findings` section. `/checkpoint` owns
  the `## Journal` and the Orientation snapshot — don't duplicate today's
  journal entry, and never write inside the `<!-- @generated -->` Orientation
  markers or any `<!-- @user -->` region.
- **`<BRAIN>/synthesis/`** — for personal/cross-theme insight, update an
  existing synthesis note if one fits, else create one.

### Step 3: Push DOWN into `<WIKI>` — check for an existing destination first
Look for an existing wiki note to update. Prefer updating over creating. For
concepts, methods, and datasets, search aliases and near-duplicates before
writing — there must be only one substantive canonical page per concept,
method, or dataset per wiki.

### Step 3b: Convene the council (the gate that licenses auto-write)

Before anything lands in `<WIKI>`, put each candidate through the five-critic council. This is what makes writing without asking safe, so it is not optional and nothing bypasses it.

Spawn **five `Task` invocations in parallel**, one per critic, each with `subagent_type=wiki-promotion-council` and `context: fork`. Name the critic's role in the prompt (**Layer-routing**, **Canonicity**, **Staleness**, **Evidence**, **Format**) and hand it the candidate plus the wiki path. They must not see each other's verdicts — the isolation is the point.

Then act on the tally:

| Vote | Action |
|---|---|
| 5 of 5 YES | Write it. Record the tally in the note's `## Changelog`. |
| 4 of 5 YES | Write it. Record the tally **and the dissenting critic's one-line rationale** in the `## Changelog`. |
| 3 of 5 YES | Do not write. Present the candidate and the five verdicts to the user and let them decide. |
| 2 or fewer YES | Discard. Log the reason in `log.md`; do not re-submit the same candidate hoping for a different roll. |

Candidates for `_brain/` (Step 2) do **not** go through the council — the human layer stays human-written, and anything routed up is proposed, never written unasked.

Respect the kill switch: with `RESEARCH_OS_WIKI_AUTOWRITE=0`, `autowrite: false` in `~/.claude/vaults.json`, or `--no-autowrite`, still run the council but **propose every result instead of writing it**.

Stay inside the blast radius defined in `${CLAUDE_PLUGIN_ROOT}/rules/wiki-integration.md`: append or create in `30_concepts/`, `40_methods/`, `50_datasets/`, `60_people_institutions/`; never touch `10_sources/`; never delete or rewrite an existing claim (append a contradiction instead); `90_synthesis/` stays proposal-only.

### Step 4: Write or update cleanly (both layers)
- write concise, reusable prose; structure clearly; remove redundancy
- preserve or add useful links; link project findings back to relevant
  summaries, canonical pages, and synthesis pages
- distinguish project evidence, source claims, inferred conclusions, and
  open questions
- if a project result changes the interpretation of several papers **within
  one theme**, update/create a `<WIKI>/90_synthesis/` page rather than
  scattering the insight; if it's personal or cross-theme, that's
  `<BRAIN>/synthesis/` instead

### Step 5: Update the project bridge
Update `wiki-links.md`, if it exists, to record:
- what was pushed and to which layer
- which wiki notes now matter for the project
- what still remains to be pushed later

Any paper touched this session gets (or keeps) a row in the `## Sources`
table (bibkey | proximity | status | wiki summary path) —
`project_dashboard.html`'s Literature panel reads only that table, so a
paper recorded elsewhere in the file (a bullet list, a prose note) will not
show up there. Don't add an authors/title column — the dashboard resolves
authors, title, DOI, and abstract live from the `wiki_path` note's own
frontmatter, so make sure that note's frontmatter is actually populated
(the point of Step 4) rather than duplicating those fields here. Only
rewrite content inside the `<!-- @generated:start wiki-links-sources -->` /
`@generated:end` markers (the sources table); preserve any
`<!-- @user:start -->` / `@user:end` region verbatim.

### Step 6: Append to the wiki log
Append an entry to the vault root's `log.md` (one level above `<WIKI>`,
prefixed with the wiki's theme name):
```
## [YYYY-MM-DD] synthesis | <theme> | [short title]
[One-line description of what was pushed and which pages were updated, in
which layer.]
```
Do not hand-edit `index.md` — it is Dataview-driven and stays current
automatically as long as new pages sit in the right numbered folder.

For anything the council auto-wrote, use the `auto-write` form instead, so a
week of them can be reviewed as one list:
```
## [YYYY-MM-DD] auto-write | <theme> | [short title]  (council 5/5)
```

### Step 6b: Refresh `_map.md` and commit the batch

`_map.md` is the flat catalogue `/wiki-pull` and the SessionStart hook read
*first*, so a push that does not refresh it leaves the fast path pointing at a
stale index:
```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/generate_wiki_moc.py" --root "<VAULT_ROOT>"
```

Then commit — the vault is its own git repo, and a separate commit per batch is
what makes an auto-write reversible in one command:
```bash
git -C "<VAULT_ROOT>" add <the pages you touched> log.md _map.md
git -C "<VAULT_ROOT>" commit -m "wiki(auto): <short title> (<theme>, council 5/5)"
```
Use `wiki(auto):` only for council-approved auto-writes and `wiki:` for anything
the user explicitly asked for — the prefix is what `--review-auto` filters on.
Stage the specific files; blanket staging is blocked by the git guardrails hook.

### Step 7: Verify
Run the quality checker when available:
```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/wiki_quality_check.py" --vault "<WIKI>"
```
or manually report required-section gaps, missing source paths, duplicate
canonical candidates, orphan/weak links, and broken wikilinks if the script
is unavailable.

### Step 8: Report clearly
Summarize:
- what was pushed up into `_brain/` (project note, synthesis)
- what was pushed down into the wiki (existing notes updated, new notes
  created)
- what was intentionally left out because it was too temporary
- verification result and unresolved wiki-quality issues

## Output Format

### Durable knowledge identified
- what is worth preserving, and which layer it belongs in

### `_brain/` updates (up)
- `<BRAIN>/projects/<slug>.md` — [updated | created | skipped]
- `<BRAIN>/synthesis/` — [updated | created | skipped]

### Wiki updates (down)
- existing notes updated
- new notes created

### Project bridge update
- what changed in `wiki-links.md`

### Not pushed
- what was intentionally kept out of both layers

## Guardrails

Do not:
- dump raw project notes into the wiki, or wiki content into `_brain/`
- create duplicate pages without checking first, in either layer
- overfit the wiki to one project's temporary needs
- fabricate updates when neither layer is accessible
- overwrite substantial notes carelessly
- push durable findings without updating backlinks, synthesis, the log, and
  the project bridge where relevant
- write personal/project-specific content into the Claude-maintained
  thematic wiki — that belongs in `_brain/`
- **auto-write anything the council has not passed**, or auto-write into
  `10_sources/`, `_brain/`, or `90_synthesis/` — those stay outside the blast
  radius no matter how confident the verdict
- **resolve a contradiction by rewriting the older claim.** Append the new
  finding as an explicit contradiction and leave both standing; the audit
  trail is what the integrity gate reads
- re-run the council on a rejected candidate hoping for a different tally. If
  three or more critics say no, the candidate is wrong for the wiki — fix what
  they named, or route it to `_brain/`

## Standard

This skill is successful if `_brain/` gains an accurate personal record and
the wiki becomes more useful for future work on this theme — without either
layer becoming cluttered or blurred into the other.
