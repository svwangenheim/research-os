# Checkpoint Skill — Gotchas

- The primary vault write is a direct filesystem write to `<_brain>/projects/<slug>.md`. Obsidian MCP is a secondary, optional visual layer — if the MCP is offline, the `_brain/` write already captured the session.
- Resolve `<_brain>` and wiki paths from `~/.claude/vaults.json` (the registry). Fall back to `~/.claude/VAULT_PATH` only if the registry is absent. If neither exists, skip the brain write silently — `passport.yaml` + `00_admin/process/journal.md` still capture the session.
- Convert relative dates to absolute dates in entries ("Thursday" --> "2026-05-09").
- Don't save code patterns or architecture to auto-memory — those are derivable from reading the code.
- Check existing memory files before creating new ones to avoid duplicates.
- `passport.yaml` `sessions:` is append-only (newest last). Never rewrite prior entries. `00_admin/process/journal.md` is append-only (newest first).
- The research journal only gets an entry if agent work happened this session. Don't log empty sessions.
- `passport.yaml` and the journal are complementary, not redundant: the passport answers "where are we / what's next" (`pipeline.current_stage`, `sessions:`); the journal answers "how did we get here."
- Never hand-edit the Claude-maintained thematic wikis from checkpoint. Human-facing notes go to `_brain/`; objective knowledge goes down into a wiki via `/wiki-ingest`.
- Don't confuse Claude Code auto-memory (`~/.claude/projects/.../memory/MEMORY.md`) with clo-author's retired project-root `MEMORY.md` — the latter folds into `passport.yaml` + `_brain/learning/`.
