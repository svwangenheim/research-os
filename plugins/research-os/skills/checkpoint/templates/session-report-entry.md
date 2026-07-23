# Session Handoff Format

Session boundaries live in `passport.yaml` `sessions:` (the resume point). A longer narrative note in `00_admin/process/sessions/` is optional -- write one only when a single `sessions:` line cannot hold the session. Both are append-only; never overwrite prior entries.

## 1. passport.yaml `sessions:` entry (always)

Append newest-last:

```yaml
sessions:
  - date: "YYYY-MM-DD"
    summary: "<what was done — concrete, one or two lines>"
    next: "<planned next step>"
```

If the pipeline advanced, also update `pipeline.current_stage` and the relevant `pipeline.stages.<stage>` (`status`, `score`).

## 2. 00_admin/process/sessions/YYYY-MM-DD_<topic>.md (optional, longer)

Only when the one-line `sessions:` entry is insufficient:

```markdown
## YYYY-MM-DD HH:MM — [Brief Title]

**Operations:**
- [Scripts run, files created/modified/deleted]

**Decisions:**
- [Choice made] — [rationale]

**Results:**
- [Key findings, outputs produced]

**Commits:**
- `[hash]` [commit message]

**Status:**
- Done: [what's complete]
- Pending: [what remains]
```
