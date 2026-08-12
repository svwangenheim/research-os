# Research Wiki Root — Two-Layer Schema

This is the unified Obsidian root for research-os: a **personal brain** (`_brain/`) plus one or
more **thematic wikis** (registered via `/add-thematic-wiki`). One `.obsidian`, one graph, cross-links work
everywhere. The canonical policy for how these layers relate is the plugin rule
**`${CLAUDE_PLUGIN_ROOT}/rules/wiki-integration.md`** — read it first; this file only covers what's
specific to *this* root (folder names, verification command, registry entry).

## The two layers

**Thematic wikis** are fully **Claude-maintained**. Humans read them but do not hand-edit them —
curation flows through `/wiki-ingest` and `/wiki-maintain`. Each wiki uses:

```
<theme>/
  00_inbox/               # unprocessed captures awaiting triage/ingest
  10_sources/             # raw, immutable source materials — never overwrite
  20_summaries/           # one detailed, scored page per source
  30_concepts/            # canonical concept/mechanism pages
  40_methods/             # canonical method pages
  50_datasets/            # canonical dataset pages
  60_people_institutions/ # author, institution, journal, organization pages
  90_synthesis/           # theme-internal synthesis (comparisons WITHIN this theme only)
```

### Claude writes here without being asked

As of the auto-write change, Claude files durable knowledge into these wikis on its own
rather than waiting for `/wiki-push`. It is bounded, gated, and reversible:

- **Gate.** Every candidate is judged by five independent critics (layer-routing, canonicity,
  staleness, evidence, format) before it lands. Four of five must agree; three proposes to you;
  two or fewer is discarded.
- **Blast radius.** Append or create in `30_concepts/`, `40_methods/`, `50_datasets/`,
  `60_people_institutions/` only. Never `10_sources/` (immutable), never `_brain/` (yours),
  never `90_synthesis/` (interpretation stays proposal-only).
- **Never destructive.** An existing claim is never deleted or rewritten. A contradicting
  finding is appended *as* a contradiction and both stand — that audit trail is what the
  integrity gate reads.
- **Reviewable.** Each batch is a separate `wiki(auto):` commit with a `## Changelog` line
  carrying the vote tally. `/wiki-maintain --review-auto` lists them; `git revert` undoes one.
- **Off switch.** `RESEARCH_OS_WIKI_AUTOWRITE=0`, or `autowrite: false` in
  `~/.claude/vaults.json`, returns to propose-only.

The full contract is `rules/wiki-integration.md` in the plugin; this is the summary.


**`_brain/`** is the personal, human-owned layer — see `_brain/wikis-index.md` for what's there.
Cross-theme or personal synthesis goes in `_brain/synthesis/`, not inside a wiki's `90_synthesis/`.

## Registry

This root and its wikis are registered in `~/.claude/vaults.json`. Each project names its
**main wiki** in `passport.yaml` (`meta.main_wiki`). To add a new theme, run `/add-thematic-wiki` — do not
create wiki folders by hand.

## Ingest / query / maintain

The full workflow (ingest standard, canonical-note dedup rule, synthesis triggers, project bridge,
lint checks) is specified once in the plugin's `wiki-integration.md` and the four global skills
(`/wiki-pull`, `/wiki-push`, `/wiki-ingest`, `/wiki-maintain`). Do not duplicate that policy here —
if it drifts, fix it at the source.

**Structural health** (folders, registry, Obsidian config, root docs) — run `/wiki-setup` any time;
it's idempotent and safe to re-run, and will diagnose + offer to repair drift.

**Content quality** (summaries, dedup, links) — after any ingest or maintenance pass:

```bash
python "${CLAUDE_PLUGIN_ROOT}"/scripts/wiki_quality_check.py --root "$(pwd)"
```

(Or `--vault <theme-path>` to check a single wiki.) Do not report an ingest or push complete if it
created shallow, unsupported, or disconnected notes — report unresolved issues explicitly.

## General rules (unchanged from the original wiki philosophy)

- Prefer updating existing pages over creating duplicates.
- Use clear markdown with informative headings; link related pages.
- Preserve uncertainty; flag contradictions explicitly.
- Distinguish source claims, inferred conclusions, and open questions.
- Do not turn the wiki into a chat transcript archive.
- When creating a new page, use the matching template from `_templates/` (shared across all wikis
  and `_brain/`).
- Do not create many shallow pages just because you can. A smaller number of useful, updated,
  interlinked pages beats many thin stubs.
