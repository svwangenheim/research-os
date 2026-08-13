---
name: careful
description: Block destructive bash commands for this session — rm -rf, git reset --hard, git push --force, and similar. Use on "careful", "protect this branch", or before risky work; deactivate with /careful off.
argument-hint: "[nothing (activate) | off (deactivate)]"
user-invocable: true
allowed-tools: Read, Write, Bash
---

# Careful — Session-Scoped Destructive Command Guard

Blocks Bash commands matching destructive patterns. Use when working on critical branches, before a deadline, or whenever you want an extra safety net.

**Input:** `$ARGUMENTS` — nothing to activate the guard, `off` to lift it.

## Usage

```
/careful       # Activate destructive command blocking
/careful off   # Deactivate
```

## Blocked Patterns

When active, the following Bash command patterns are blocked:

| Pattern | What It Catches |
|---------|----------------|
| `rm -rf` | Recursive force delete |
| `rm -r` without explicit path | Broad recursive delete |
| `git reset --hard` | Discard all uncommitted changes |
| `git push --force` | Force push (overwrites remote history) |
| `git push -f` | Same |
| `git clean -f` | Delete untracked files |
| `git checkout -- .` | Discard all working tree changes |
| `git branch -D` | Force delete branch |
| `DROP TABLE` | SQL table deletion |
| `DROP DATABASE` | SQL database deletion |
| `> /dev/null` at start | Overwriting with null |
| `chmod 777` | Overly permissive permissions |

## Activation

When the user invokes `/careful`:

1. Read `.claude/state/session-guards.json` (create if needed)
2. Set the `careful` guard:
```json
{
  "careful": {
    "active": true,
    "activated_at": "2026-07-22T14:30:00",
    "reason": "User invoked /careful"
  }
}
```
3. Confirm: "Careful mode active. Destructive bash commands are blocked. Run `/careful off` to deactivate."

## Deactivation

When `/careful off`:
1. Set `careful.active` to `false`
2. Confirm: "Careful mode deactivated."

## Gotchas

- Session-scoped — resets when conversation ends
- Only blocks Bash tool calls — doesn't affect user's terminal
- Can be overridden if the user explicitly approves the blocked command
- `rm` without `-rf` is still allowed (single file deletion)
