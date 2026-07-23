# Research Wiki + Second Brain

This is the unified knowledge root for research-os: one Obsidian vault holding a personal
**second brain** and one or more **Claude-maintained thematic wikis**.

## Layout

- **`_brain/`** — the human's space: profile, daily/weekly notes, freeform thoughts, per-project
  journals, personal + cross-theme synthesis, durable learnings. Humans write here; Claude writes
  here too (via `/checkpoint`, `/wiki-push`).
- **`<theme>/`** (e.g. a wiki registered via `/add-vault`) — thematic wikis. Claude maintains these
  automatically (ingesting sources, writing summaries, canonicalizing concepts/methods/datasets).
  Humans read them; they don't hand-edit them.
- **`_templates/`** — shared note templates used across every wiki and `_brain/`.
- **`CLAUDE.md`** — the operating rules for this root (points to the plugin's canonical policy).
- **`index.md`** — cross-wiki catalog (Dataview).
- **`log.md`** — unified chronological record of ingests, queries, and maintenance.

## Core principle

Raw sources (`<wiki>/10_sources/`) are the source of truth. Each wiki is the Claude-maintained
interpretation layer for one research theme. `_brain/` is where personal thinking, planning, and
cross-theme synthesis lives. New knowledge should update existing pages, not just create isolated
notes — the wiki (and the brain) should feel cumulative, not scattered.

## Adding a new theme

Run `/add-vault` rather than creating a folder by hand — it registers the theme in
`~/.claude/vaults.json` and scaffolds the numbered layout.

## Checking structural health

Run `/wiki-setup` any time — it's idempotent, diagnoses drift from the standard layout, and offers
to repair each gap it finds.
