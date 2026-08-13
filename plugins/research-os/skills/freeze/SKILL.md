---
name: freeze
description: Block edits outside specified directories for this session, protecting files during focused work. Use on "freeze", "lock the paper", "only let me edit X"; deactivate with /freeze off.
argument-hint: "[dir1 dir2 ... (activate) | off (deactivate)]"
user-invocable: true
allowed-tools: Read, Write, Edit
---

# Freeze — Session-Scoped Edit Guard

Blocks Write and Edit operations on files outside the specified directories. Use when reviewing code (freeze everything except notes), when writing (freeze `03_analysis/scripts/`), or when editing data pipelines (freeze `04_paper/`).

**Input:** `$ARGUMENTS` — the directories that stay editable, or `off` to lift the guard.

## Usage

```
/freeze 04_paper/                    # Only allow edits in 04_paper/
/freeze 03_analysis/ 02_data/        # Only allow edits in 03_analysis/ and 02_data/
/freeze off                          # Deactivate all freeze guards
```

Paths use the numbered project scheme (see the plugin's `rules/folder-map.md`): `00_admin · 01_literature · 02_data · 03_analysis · 04_paper · 05_outreach`.

## How It Works

1. Parse the directory arguments from the user's input
2. Write the guard configuration to `.claude/state/session-guards.json`
3. The `session-guard` PreToolUse hook reads this file and blocks Edit/Write operations on files outside the allowed directories
4. Report what's frozen and what's editable

## Activation

When the user invokes `/freeze [dirs]`:

1. Read the current `.claude/state/session-guards.json` (create if it doesn't exist)
2. Set the `freeze` guard:
```json
{
  "freeze": {
    "active": true,
    "allowed_paths": ["04_paper/", "03_analysis/scripts/"],
    "activated_at": "2026-07-22T14:30:00",
    "reason": "User invoked /freeze"
  }
}
```
3. Confirm: "Freeze active. Edits allowed only in: [dirs]. Run `/freeze off` to deactivate."

## Deactivation

When the user invokes `/freeze off`:

1. Read `.claude/state/session-guards.json`
2. Set `freeze.active` to `false`
3. Confirm: "Freeze deactivated. All paths editable."

## Gotchas

- Freeze is session-scoped — it resets when the conversation ends
- The guard file persists on disk but the hook checks a session flag
- `.claude/` is always editable (can't freeze yourself out of config changes)
- Paths are relative to the project root
