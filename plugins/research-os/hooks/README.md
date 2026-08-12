# hooks/

`hooks.json` plus the hook scripts. The originals were ported from clo-author (protect-files, session-guard, post-edit-lint, pre-compact / post-compact-restore) and rewired to the numbered folder scheme; several have since been rewritten or replaced, and the harness layer was extended with patterns adapted from Pedro Sant'Anna's academic Claude Code workflow (see `docs/PROVENANCE.md`).

**Design principle.** Rules live in context and can be compressed away. Hooks fire every time, regardless of context state. So hooks are reserved for enforcement that *must* survive compaction — anything needing nuanced judgement belongs in `rules/` instead. Every hook fails open: a bug in a hook must never block the session.

## Every script in this directory

Eleven are registered in `hooks.json`; the last two are not Claude Code hooks at all and are listed here because they live in this directory.

<!-- surface-sync-table: hooks -->

| Script | Event | Matcher | What it does |
|---|---|---|---|
| `protect-files.py` | PreToolUse | `Edit\|Write\|MultiEdit` | Denies writes to single-writer artifacts by basename (`settings.json`, `passport.yaml`, `strategy-memo-*.md`, `referee-report-*.md`, `quality-score-*.json`). |
| `git-guardrails.py` | PreToolUse | `Bash\|Write\|Edit\|MultiEdit` | Always-on. Denies destructive git (`reset --hard`, `clean -f`, `push --force`, blanket `add -A/.`, `checkout -- .`); warns on absolute machine paths written into analysis code (INV-16), or denies them under `RESEARCH_OS_STRICT_PATHS=1`. |
| `session-guard.py` | PreToolUse | `Edit\|Write\|Bash` | Opt-in `/freeze` and `/careful`, driven by `.claude/state/session-guards.json`. Pass-through when absent. |
| `pre-compact.py` | PreCompact | — | Captures active plan, current task, recent decisions and pipeline stage before compaction. |
| `post-compact-restore.py` | SessionStart | `compact\|resume` | Reads and clears the pre-compact state, re-injecting it so the session knows where it left off. |
| `wiki-context.py` | SessionStart | `startup\|resume\|clear` | Injects a bounded, stage-aware digest of the resolved thematic wiki, so the first fact about a session is what is already known. Read-only, line-capped, silent when no wiki resolves. |
| `engram-session-start.sh` | SessionStart | `startup\|resume\|clear` | Two-line nudge for due spaced-repetition reviews. Silent when nothing is due. |
| `session-journal.py` | Stop | — | Writes a structured change-set entry to `00_admin/process/sessions/YYYY-MM-DD_auto.md` (files touched, pipeline stage, integrity state, active plan, unpushed wiki items). Throttled on the `git status` hash. |
| `post-edit-lint.py` | PostToolUse | `Write\|Edit\|MultiEdit` | Mechanical lint of R/Python/Julia under `03_analysis/scripts/` against INV-14 .. INV-19. Throttled per file per 2 min. |
| `claim-reconcile.py` | PostToolUse | `Write\|Edit\|MultiEdit` | On a write to a tracked analysis input, reports how many `passport.yaml` `claim_manifest` claims now depend on stale evidence, and points at `/peer-review --replicate`. Notifier only — never writes the passport. |
| `context-monitor.py` | PostToolUse | `Bash\|Task` | Progressive context nudges (40/55/65% → `/checkpoint` or `/wiki-push`; 80% info; 90% finish-at-quality). Persists `context-pct.txt` for the status line. |
| `lint-scripts.sh` | not a hook | — | The grep-based linter library `post-edit-lint.py` calls. Also runnable standalone (`/tools lint`). |
| `post-merge.sh` | not a hook | — | A **git** hook, not a Claude Code hook: prints a `/checkpoint` reminder after a merge. |

## Related, outside this directory

- `../scripts/statusline.py` — renders permission mode, model, branch, pipeline stage, integrity gate state, and the context estimate. Wire it via `statusLine` in `~/.claude/settings.json`.

## Rewrites and replacements worth knowing about

- **`post-edit-lint.py`** replaced `post-edit-lint.sh`, which read `$CLAUDE_TOOL_ARG_FILE_PATH` — a legacy variable Claude Code no longer sets. The old hook silently never ran, so the code invariants had no write-time enforcement at all.
- **`protect-files.py`** replaced `protect-files.sh`, which shelled out to `jq` — not present by default on Windows, so the guard failed silently on a fresh machine. It also now uses the modern PreToolUse decision protocol (exit 0 + a `permissionDecision` object) rather than `exit 2` + stderr.
- **`session-journal.py`** replaced `stop-push-nudge.py`, which only printed a reminder to run `/wiki-push`. Bookkeeping that depends on remembering to type a command happens on the sessions that went smoothly and not on the ones that didn't. The replacement writes the record and keeps the nudge as one section of it.

## Testing a hook

Hooks read JSON on stdin. To exercise one directly:

```bash
echo '{"tool_name":"Bash","tool_input":{"command":"git reset --hard"}}' \
  | python hooks/git-guardrails.py
```

Expect a decision object for a blocked operation and silence (exit 0) otherwise. Every hook should also exit 0 on malformed stdin — that is the fail-open contract, and it is worth re-checking after any edit:

```bash
for h in hooks/*.py; do echo garbage | python "$h" >/dev/null 2>&1 || echo "FAIL $h"; done
```
