# Authoring Conventions

The house style for every Claude-facing file in this plugin — skills, agents, rules, references, templates, and hooks. It exists so that a reader who has seen one of our skills can predict the shape of the next one, and so that "is this file written correctly?" is a checkable question rather than a matter of taste.

The conventions are inherited from the two workflows this plugin is built on — Hugo Sant'Anna's [clo-author](https://github.com/hugosantanna/clo-author) (progressive disclosure, worker-critic agents, the phase-skill shape) and Pedro Sant'Anna's [claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) (trigger-rich descriptions, path-scoped rules, deterministic integrity checking). Where the two diverge, this file records which one we follow and why.

Most of what follows is enforced by [`scripts/check_plugin_integrity.py`](../scripts/check_plugin_integrity.py). Anything the script can check, it should check — a convention that lives only in prose drifts.

---

## 1. Language and typography

These apply to every markdown file in the plugin.

- **Em dash, never `--`.** Write `— ` as a real em dash with spaces around it. The `--` spelling survives only inside code fences, inline code spans, and CLI flags (`--no-verify`), where it is literal.
- **Sentence-case prose, Title Case headings.** H1 is `# Title Case`, no leading slash and no command name: `# Write`, `# Wiki Push`, `# Learn: The Acquisition Loop`. The skill's invocation (`/write`) belongs in the body, not the heading.
- **Second person for the agent, third person for the user.** Skills and agents address Claude directly ("Read the passport before dispatching"); descriptions describe the skill to a router ("Draft academic paper sections…").
- **English throughout**, including in skills that produce German output. The output language is a property of the artifact, not of the instruction file.
- **ASCII where it costs nothing.** Curly quotes, arrows (`→`), and section marks (`§`) are fine; replacement characters and mojibake are a bug. Files are UTF-8 with LF endings.
- **No emoji in skill, agent, or rule bodies.** They survive only in user-facing output that a skill explicitly specifies.

---

## 2. Skills

One directory per skill under `skills/<name>/`, kebab-case, with `SKILL.md` at its root.

### Frontmatter

```yaml
---
name: wiki-push
description: Write durable knowledge from this session back — personal synthesis UP into _brain/, objective concept, method, and dataset knowledge DOWN into the thematic wiki. Use after work blocks.
argument-hint: "[scope: session | project | all] [--dry-run]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash,Task
---
```

| Key | Required | Convention |
|---|---|---|
| `name` | yes | Matches the directory name exactly. |
| `description` | yes | One to three sentences: **what it does**, then **when to use it**, ending in a `Use when…` / `Use on…` / `Use for…` clause carrying the literal phrases a user would type. This clause is what the router matches on; a description without it is invisible to auto-invocation. Target 120–250 characters. |
| `argument-hint` | yes, if it takes arguments | Quoted. Mode keywords first, flags last: `"[mode: a \| b] [--flag]"`. Every flag here must be documented in the body, and every documented flag must appear here. |
| `allowed-tools` | yes | Comma-separated, no spaces, no JSON array: `Read,Grep,Glob,Write`. Must cover every tool the body tells Claude to invoke. Note that this **pre-approves**, it does not restrict — use `disallowed-tools` to actually remove a tool from a read-only skill. |
| `disable-model-invocation` | when applicable | `true` for skills that create a persistent, load-bearing file the user must explicitly intend (`/create-project`, `/checkpoint`). Not for skills that write disposable reports. |
| `user-invocable` | when applicable | `true` for session-guard skills with no model-invocation path (`/careful`, `/freeze`). |
| `origin` | vendored skills only | Upstream repo and licence for a skill imported wholesale. Ours only; neither upstream uses it. |

### Body shape

```markdown
# Skill Name

One or two sentences: what this skill accomplishes and why it exists.

**Input:** `$ARGUMENTS` — what the arguments mean, and what happens when they are omitted.

---

## Modes            (or ## Steps, for a single-path skill)

### `/skill mode` — What This Mode Does
...

---

## Bundled Resources (Level 3)

| Resource | Path | When |
|---|---|---|
| Section templates | `templates/section-templates.md` | Always — defines section structure |

See also: `gotchas.md` for known failure points and edge cases.

---

## Principles
- **One bold claim per bullet.** Short, imperative, non-obvious.
```

The `**Input:**` line is mandatory for any skill that accepts `$ARGUMENTS`. The `---` rules separate top-level sections; do not use them between `###` subsections.

### Progressive disclosure

`SKILL.md` is Level 2 — a router that names the work and dispatches it. Heavy content is Level 3 and lives beside it:

| Subdirectory | Holds |
|---|---|
| `templates/` | Output scaffolds the skill fills in — memos, reports, letters, checklists. |
| `references/` | Standing domain knowledge the skill reads but does not produce — standards, protocols, conventions. |
| `config/` | Machine-readable thresholds and rubrics (`.json`, or `.md` when a rubric needs prose). |
| `gotchas.md` | Known failure points, one bullet each, written from observed failures rather than imagined ones. |

**Keep `SKILL.md` under 300 lines.** Past that, the file is carrying content that belongs in `templates/` or `references/`, and the router table above is the mechanism for pointing at it. Shared material used by more than one skill goes in `skills/_shared/`.

### Paths

Reference bundled files as `${CLAUDE_PLUGIN_ROOT}/skills/<name>/templates/<file>.md` in backticks. Relative markdown links do not resolve reliably from an installed plugin, so they are reserved for links *between* documentation files (READMEs, references, this file). Anchor links must resolve — the integrity checker verifies them.

---

## 3. Agents

One file per agent at `agents/<name>.md`, kebab-case.

```yaml
---
name: writer-critic
description: Manuscript critic that reviews paper drafts for structure, claims-evidence alignment, identification fidelity, and LaTeX format. Paper-type aware. Runs 8 check categories. Paired critic for the Writer.
tools: Read, Grep, Glob
model: opus
effort: high
---

You are a **manuscript critic** — the coauthor who reads the draft and says…
```

- `tools` (not `allowed-tools` — that key is for skills) is comma-separated with spaces, plain tool names only. Permission-style scoping such as `Bash(git diff*)` is invalid here and silently grants the agent every tool.
- `model` and `effort` are both required. The roster and the routing rules live in [`rules/model-routing.md`](../rules/model-routing.md); never demote a gate-keeper, and never let a critic sit below its worker.
- The body opens with the persona in second person — `You are a **role** — one clause of what makes this role different.` An H1 before it is permitted when the agent's output is itself a titled document (`# Methods Referee Report`), but the persona line still comes first in substance.
- Critics never edit. A critic's `tools` list contains no `Write` or `Edit`, per [`rules/agents.md`](../rules/agents.md).
- Every agent must appear in [`rules/permissions.md`](../rules/permissions.md), which is the single source of truth for capabilities, dependencies, routing, and quality weights. No other file restates those relationships.

---

## 4. Rules

One file per rule at `rules/<topic>.md`, kebab-case, named for what it governs rather than for who reads it.

- H1 is `# Topic: Subtitle` or `# Topic — clarifying clause`, followed by a bolded one-line mandate before any protocol.
- **Scope with `paths:` frontmatter whenever the rule governs identifiable files.** A path-scoped rule loads automatically the moment a matching file is touched and costs nothing otherwise; an unscoped rule loads only when a skill or agent remembers to read it.

  ```yaml
  ---
  paths:
    - "**/*.R"
    - "**/*.py"
  ---
  ```

- Rules are normative; references are not. If a document tells Claude what it *must* do, it is a rule. If it tells Claude what is *true*, it is a reference.
- Enforcement that must survive context compaction does not belong in a rule at all. It belongs in `hooks/`, which fire regardless of context state.
- Every rule gets a row in [`rules/README.md`](../rules/README.md) naming its loading mode and what it governs.

---

## 5. References and templates

`references/` holds standing knowledge shared across skills and agents — journal profiles, orchestration schemas, this file. Anything under `references/internal/` is gitignored and exists only for whoever maintains the plugin.

`templates/` holds scaffolds the plugin writes into a user's project or vault: project rules, brain and wiki note templates, the passport, folder READMEs. Plugin-level templates live here; skill-specific ones live under that skill.

Both use the same typography and heading rules as everything else.

---

## 6. Hooks

Hooks are the enforcement layer: they fire every time, where rules fire only when the model reads them.

- Python hooks open with a `#!/usr/bin/env python3` shebang and a module docstring whose first line is `<Event> hook - <what it does>`, followed by a paragraph on **why this is a hook and not a rule or a skill**. That paragraph is the part worth writing; the mechanics are readable from the code.
- Shell hooks carry the same first line as a `#` comment.
- A hook never breaks a session. Degrade to silence on any failure, and keep the timeout in `hooks.json` honest.
- Every script in `hooks/` is listed in [`hooks/README.md`](../hooks/README.md), including the ones that are not registered in `hooks.json`.

---

## 7. What gets checked automatically

[`scripts/check_plugin_integrity.py`](../scripts/check_plugin_integrity.py) runs the deterministic half of this document:

| Check | Severity |
|---|---|
| Frontmatter ↔ body tool parity in skills | P1 |
| `argument-hint` ↔ body flag parity, both directions | P1 |
| Internal markdown anchors resolve | P0 |
| Rule ↔ implementation parity | P1 |
| Agent frontmatter completeness (`name`, `description`, `tools`, `model`) | P1 |
| House style: em dash, H1 shape, `**Input:**` line, `Use when…` clause, `SKILL.md` length | P2 |

Run it before any commit that touches the plugin tree:

```bash
python plugins/research-os/scripts/check_plugin_integrity.py
```

Exit code 0 means clean or advisories only; 1 means real drift.
