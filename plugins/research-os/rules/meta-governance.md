# Meta-Governance: This Plugin's Dual Nature

research-os is both a working system and a reusable template for empirical research. Its default domain is empirical economics, but it adapts to adjacent fields (finance, accounting, marketing, management, public policy) by customizing the domain profile and journal profiles — and it produces DZ policy outputs (`policy_brief`, `fachtext`, `hintergrundpapier`, `geldbrief`) alongside academic papers.

## Working System
- We develop research papers, policy outputs, seminars, guides, and documentation
- We accumulate project-specific learnings and institutional context
- We test and iterate on the architecture itself

## Reusable Template
- Others adopt this plugin (or fork the template) to run their own research workflows
- They share the same pipeline (discover → strategize → analyze → write → peer-review → revise → submit) and tools (LaTeX, R/Python/Julia, Beamer)
- Field-specific differences (journals, methods, conventions) are handled by `00_admin/domain-profile.md` (per project) and `${CLAUDE_PLUGIN_ROOT}/references/journal-profiles.md` (shared)

## The One Rule

Before committing, ask: **would another researcher adopting this plugin benefit from this?**

- **Yes** → commit (workflow patterns, skills, agents, rules, templates)
- **No** → keep local (machine paths, tool versions, institution-specific requirements, API keys) in project-local state (`.claude/state/`), never in the shared plugin

## Learning Promotion

When a learning has been validated across 3+ projects (confirmed by user):

| Pattern Type | Promotion Target | Requires |
|-------------|-----------------|----------|
| PATTERN (replicable success) | New best-practice in relevant agent's protocol | User approval |
| FRICTION (recurring failure) | Agent prompt revision or rubric adjustment | User approval |
| HIGH-PERF (consistent excellence) | New content invariant (INV-XX) or rule addition | User approval |

**Protocol:**
1. The orchestrator identifies a pattern recurring across 3+ traces (`00_admin/process/traces/`, derived from `passport.yaml` `pipeline` history — see `logging.md`)
2. The orchestrator drafts the specific change (new invariant text, agent prompt addition, or rubric adjustment)
3. The user reviews and approves or rejects
4. If approved, the change is committed to the plugin

**Constraint:** Promotion ALWAYS requires user approval. The system suggests; the user decides. No autonomous self-modification of rules, invariants, or agent prompts.
