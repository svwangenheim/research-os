# Index

This is the content-oriented catalog across all thematic wikis. Each table groups by wiki via
`theme`, a computed field (top-level folder name). `/add-vault` extends the `FROM` clause of each
wiki-content query below when a new theme is registered.

---

## Summaries

<!-- No wikis registered yet — run /add-vault to add one; this section's Dataview query will be
     extended automatically to include it. -->

## Concepts

<!-- see note above -->

## Methods

<!-- see note above -->

## Datasets

<!-- see note above -->

## People and Institutions

<!-- see note above -->

## Theme-internal Syntheses

<!-- see note above -->

---

## Second brain (`_brain/`)

### Projects

```dataview
TABLE summary, status
FROM "_brain/projects"
WHERE note_type = "project"
SORT file.name ASC
```

### Personal + cross-theme synthesis

```dataview
TABLE summary, tags
FROM "_brain/synthesis"
WHERE note_type = "synthesis"
SORT file.name ASC
```

---

## Maintenance note

Whenever a new source is ingested, this index should stay accurate automatically (Dataview queries
live). Whenever a new wiki is added via `/add-vault`, it extends every wiki-content `FROM` clause
above to include it. Run `python "${CLAUDE_PLUGIN_ROOT}"/scripts/wiki_quality_check.py --root "$(pwd)"`
periodically to catch drift (orphans, duplicates, broken links) that a live query can't show.
