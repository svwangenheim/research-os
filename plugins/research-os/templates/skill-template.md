# Skill Template

Starter for a new research-os skill. Copy the block below to `skills/<name>/SKILL.md` and fill it in. The conventions it encodes are documented in [`references/authoring-conventions.md`](../references/authoring-conventions.md); the deterministic ones are checked by `scripts/check_plugin_integrity.py`.

---

## When a skill is the right surface

Write a skill when the work is a **named, repeatable workflow the user invokes**: three or more steps, a stable shape, and an output someone would ask for by name.

Write something else when:

- The behaviour must happen *every* time regardless of context — that is a **hook**.
- It states what Claude must always do in a domain — that is a **rule**.
- It is standing knowledge rather than a procedure — that is a **reference**.
- It is one person's recurring busywork rather than generalizable research machinery — that is a **procedure** in `_brain/procedures/`, authored through `/automate`. Procedures may call skills; skills never call procedures.

---

## The template

```markdown
---
name: your-skill-name
description: [What it does, one clause.] [What it produces or dispatches, one clause.] Use when the user says "[trigger phrase]", "[trigger phrase]", or [situation].
argument-hint: "[mode: a | b | c] [target] [--flag]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash,Task
---

# Skill Name

One or two sentences: what this skill accomplishes and why it exists as its own surface.

**Input:** `$ARGUMENTS` — what the arguments mean, and what happens when they are omitted.

---

## Modes

### `/your-skill-name a` — What Mode A Does

**Agent:** [dispatched agent, or "none — runs inline"]
**Output:** [path the artifact lands at]

Workflow:

#### 1. [First step]

[What to read or resolve before acting. Name real paths.]

#### 2. [Second step]

[The substantive work.]

#### 3. Quality Self-Check

Before presenting:
- [ ] [A checkable property of the output]
- [ ] [Another one]

#### 4. Present to User

[What the user sees, and what decision you are asking them for.]

### `/your-skill-name b` — What Mode B Does

...

---

## Bundled Resources (Level 3)

| Resource | Path | When |
|----------|------|------|
| [Name] | `templates/[file].md` | [Always / mode b only / after step 2] |

See also: `gotchas.md` for known failure points and edge cases.

---

## Principles
- **[Short imperative claim.]** [One sentence of why.]
- **[Another.]** [Why.]
```

---

## Filling it in

**`description`.** The `Use when…` clause is what the router matches on. Write the phrases a user would actually type, not a paraphrase of the skill name.

- Weak: `description: Helps with the wiki.`
- Strong: `description: Retrieve prior knowledge from the personal brain and the relevant thematic wiki before substantial work. Use when starting literature review, design, data work, writing, or planning.`

**`allowed-tools`.** List every tool the body tells Claude to invoke, and nothing more. This pre-approves rather than restricts — for a genuinely read-only skill, add `disallowed-tools: ["Write", "Edit", "Bash"]`.

**`argument-hint`.** Every flag documented in the body must appear here, and every flag here must be documented in the body. The integrity checker enforces both directions.

**Bundled resources.** Anything longer than a screen belongs in `templates/`, `references/`, or `config/` beside the skill, listed in the table. Keep `SKILL.md` under 300 lines. Reference bundled files as `` `${CLAUDE_PLUGIN_ROOT}/skills/<name>/templates/<file>.md` `` — relative links do not resolve from an installed plugin.

**`gotchas.md`.** Write it from failures you have actually seen, one bullet each, after the skill has run a few times. An empty `gotchas.md` is worse than none.

---

## Before you commit

```bash
python plugins/research-os/scripts/check_plugin_integrity.py
```

Then add the skill to the tables in [`skills/README.md`](../skills/README.md) and the root [`README.md`](../../../README.md), and to the routing table in `~/.claude/rules/common/skill-router.md` if the user should be routed to it automatically.
