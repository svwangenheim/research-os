# templates/

Scaffolds used by `create-project`, `add-vault`, and the wiki skills:

- **Project scaffold:** the numbered `00_admin … 05_outreach` tree, `CLAUDE.md`, `passport.yaml` (material-passport state ledger), `wiki-links.md`, `project_dashboard.html` seed.
- **Vault (thematic wiki) scaffold:** numbered `00_inbox … 90_synthesis` + `60_people_institutions` (from the existing `vault/_templates/` note templates), minus projects/synthesis (those live in `_brain/`).
- **Second-brain scaffold:** `_brain/` layout (`profile.md`, `daily/`, `weekly/`, `thoughts/`, `projects/`, `synthesis/`, `learning/`, `wikis-index.md`).
- **`vault-root/`:** the 4 vault-root docs (`CLAUDE.md`, `README.md`, `index.md`, `log.md`) — generic, no bespoke wiki names or migration history baked in. Used by `/wiki-setup` to bootstrap a fresh vault root.
- **`wiki-notes/`:** the 7 shared note templates (`concept`, `method`, `dataset`, `entity`, `source_summary`, `synthesis`, `project`) — copied into `<root>/_templates/` by `/wiki-setup`.
- **`obsidian/`:** the `.obsidian` config JSON `/wiki-setup` copies into a fresh vault root (`core-plugins.json`, `templates.json`, `app.json`, `appearance.json`, `community-plugins.json`). `community-plugins.json` ships as `[]` deliberately — Dataview's actual plugin code can't be shipped here; the user enables it via the Obsidian GUI, which populates this file itself.
