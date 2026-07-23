# hooks/

`hooks.json` plus hook scripts, ported from clo-author (protect-files, session-guard, post-edit-lint, pre-compact / post-compact-restore) and rewired to the numbered folder scheme. Additional hooks:

- SessionStart nudge for due spaced-repetition reviews (engram; silent unless due — must compose with continuous-learning-v2's hook).
- Wiki write-guard steering human edits to `_brain/`, not the Claude-maintained thematic wikis.

`hooks.json` is intentionally omitted until real hooks are ported, so nothing malformed loads.
