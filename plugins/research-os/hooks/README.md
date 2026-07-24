# hooks/

`hooks.json` plus hook scripts, ported from clo-author (protect-files, session-guard, post-edit-lint, pre-compact / post-compact-restore) and rewired to the numbered folder scheme.

- **PreToolUse** — `protect-files.sh` and `session-guard.py`: the wiki write-guard steering human edits to `_brain/`, not the Claude-maintained thematic wikis.
- **PreCompact** — `pre-compact.py`: captures plan/stage/decisions before compaction (restored by `post-compact-restore.py` on SessionStart compact|resume). Its checklist reminds to `/wiki-push` durable knowledge.
- **SessionStart (startup|resume|clear)** — `engram-session-start.sh`: nudge for due spaced-repetition reviews (engram; silent unless due — composes with continuous-learning-v2's observe hook).
- **Stop** — `stop-push-nudge.py`: the standing two-output rule. If the project's `wiki-links.md` still lists unchecked "to push back" items, it reminds once per session to run `/wiki-push`. Offer only — it never auto-writes.
- **PostToolUse** — `post-edit-lint.sh`.
