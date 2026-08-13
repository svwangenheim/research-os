# Provenance

research-os is assembled from other people's work. This file is the single
adoption log: what came from where, where it lives now, and which upstream
commit it was last reconciled against.

Provenance used to be scattered across README acknowledgments, the `role`
fields in `plugins/research-os/state/upstream-repos.json`, a gitignored build
history, and two per-item READMEs. When attribution lives in four places it
goes stale in four places. This table is the one that is maintained.

`/check-update-upstream-repos` diffs the tracked repositories against their
last-seen SHA and reports what changed. Update the last-synced column here when
you act on that report.

## Two people named Sant'Anna

This is the easiest thing on the page to get wrong, so it is stated first.

**Hugo Sant'Anna** (University of Alabama at Birmingham) wrote **clo-author**.
**Pedro H. C. Sant'Anna** (Emory University) wrote
**claude-code-my-workflow**. They are different people at different
institutions. Neither repository is derived from the other, and research-os
adopted from each of them independently.

Where influence does run between them, it runs from Hugo to Pedro, not the
reverse: Pedro's README credits clo-author for the `/review-paper --peer
<journal>` pipeline, adapted with Hugo's permission, and credits clo-author
v4.2.0 for `/checkpoint`.

Do not collapse the two into one attribution, and do not describe research-os's
pipeline as descending from Pedro's template. The pipeline came from Hugo. What
came from Pedro is the harness around it.

## Adoption log

| Upstream | What was taken | Where it lives now | Last synced |
|---|---|---|---|
| [`hugosantanna/clo-author`](https://github.com/hugosantanna/clo-author) — Hugo Sant'Anna, UAB | Base paper pipeline: 14 skills, 22 agents, the worker-critic pairing model, separation of powers, quality gates, `passport.yaml` as the single ledger, the original hooks (protect-files, session-guard, post-edit-lint, pre-compact / post-compact-restore), the 13-rule governance backbone, and the HTML report design system | `plugins/research-os/{skills,agents,hooks,rules}/`, rewired to the numbered project folder scheme; `plugins/research-os/styles/styles.css`, `styles/components.js`, `scripts/generate_html_report.py` | `d36c408458b0135d2ebf16072da6b0d54864f6fb` (2026-07-23) |
| [`Imbad0202/academic-research-skills`](https://github.com/Imbad0202/academic-research-skills) (ARS) | Integrity gate: claim tracing, four-database citation triangulation, temporal and anachronism audit. Anti-sycophancy guards, PRISMA systematic-review mode, multi-style citation conversion, AI-use disclosure | Merged into the ported agents and skills rather than kept separate — `agents/verifier.md`, `agents/methods-referee.md`, `agents/writer-critic.md`, `skills/peer-review/`, `skills/submit/`, `skills/discover/` | `1788e08155d24da729233e3e4b480ffb53d799c6` (2026-07-23) |
| [`nagisanzenin/engram`](https://github.com/nagisanzenin/engram) | Spaced-repetition learning engine and its teaching, review and telemetry loops | Vendored, not installed as a separate plugin: `plugins/research-os/scripts/engram.py`, `agents/engram-*.md`, `skills/{learn,recall,coach}/`, `skills/_shared/{dialogue,problem}-grammar.md` and `explorable-contract.md`, `references/engram-*`. The three SKILL.md files were adapted — simplified for Claude Code only, with wiki and project linkage woven in. An upstream diff means re-copy the changed files and re-apply the adaptation by hand; it is not a plugin update | `688877e0b72df3623cd7ccb6d95e0da922c83d0b` (2026-07-23) |
| [`eugeniughelbur/obsidian-second-brain`](https://github.com/eugeniughelbur/obsidian-second-brain) | Nothing yet — watched, not integrated | No code adopted. A peer LLM-maintained vault system (the OKM standard), tracked for adoptable ideas: freshness and confidence conventions, map-of-content designs, the capture-to-graduate flow, scheduled-agent patterns. research-os is deliberately stricter for research use (immutable sources, preserved contradictions, notes a human can read), so a diff here means scan for patterns worth porting, never wholesale adoption | `ff3867b8fe95ff8a28fc2dafda3af579c739d80c` (2026-07-23) |
| [`pedrohcgs/claude-code-my-workflow`](https://github.com/pedrohcgs/claude-code-my-workflow) — Pedro H. C. Sant'Anna, Emory | The harness layer, adopted as patterns rather than copied files: hooks as enforcement that survives context compression; path-scoped rule loading with a small always-on core; per-agent model and effort pinning; context-survival hooks; the five-critic promotion council; deterministic self-governance (integrity and surface-sync checkers, pre-commit gate, CI, changelog, committed backlog) | `plugins/research-os/hooks/{git-guardrails,claim-reconcile,context-monitor,session-journal}.py`, `scripts/statusline.py`, `scripts/check_plugin_integrity.py`, `scripts/check_surface_sync.py`, `.githooks/pre-commit`, `.github/workflows/gates.yml`, `CHANGELOG.md`, `BACKLOG.md`, `rules/{summary-parity,prompt-shaping,confidential-data}.md` | not pinned (reviewed at v2.0.0, 2026-08-10) |

## Files whose only attribution is this page

Three files were ported from clo-author and carried a clo-author header
comment. The headers were renamed to research-os so the shipped dashboard does
not credit a project the user never installed. That makes this table the sole
record of where they came from:

- `plugins/research-os/styles/styles.css`
- `plugins/research-os/styles/components.js`
- `plugins/research-os/scripts/generate_html_report.py`

If any of the three is rewritten from scratch, remove it from this list. Until
then, the attribution lives here and nowhere else.

## What research-os added on its own

Recorded so the boundary stays visible when the next upstream is adopted:

- The two-layer knowledge vault — personal `_brain/` plus Claude-maintained
  thematic wikis, immutable sources, canonical concept, method and dataset
  pages, and the `.research-os-wiki` resolution ladder.
- `passport.yaml` extended from a numeric-claims file into the project's single
  ledger: research spec, claim manifest, literature corpus, provenance,
  pipeline stage, integrity state, session history.
- The blocking pre-submission integrity gate as a single co-owned gate, rather
  than separate verify and audit commands.
- German policy-research fit: `rules/confidential-data.md` for administrative
  and register data.
