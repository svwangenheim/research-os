# Freeze Skill — Gotchas

- Freeze paths are relative to project root. `/freeze 04_paper/` means `$PROJECT_ROOT/04_paper/`.
- `.claude/` is always editable regardless of freeze — you can't lock yourself out of configuration.
- Freeze doesn't affect Read or Bash — you can always read and run commands, just not edit files outside allowed paths.
- Multiple paths: `/freeze 04_paper/ 03_analysis/` allows both directories.
- Session-scoped means it survives `/compact` but not conversation end.
- Paths use the numbered scheme (`00_admin` … `05_outreach`) — see `rules/folder-map.md`.
