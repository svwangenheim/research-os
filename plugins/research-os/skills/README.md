# skills/

Slash-command skills for research-os. Each is a directory with a `SKILL.md` carrying YAML frontmatter (`name`, `description`, `argument-hint`, `allowed-tools`). `_shared/` holds prose fragments several skills include and is not a skill itself.

Run `claude plugin details research-os@research-os` for the live roster and token-cost inventory. The table below is checked against disk by `scripts/check_surface_sync.py`, so a skill added or retired without editing this file fails the commit.

## Every skill

<!-- surface-sync-table: skills -->

| Skill | Group | What it does |
|---|---|---|
| `add-thematic-wiki` | Knowledge | Register a research theme — adopt a vault already on disk, or scaffold a new one in the numbered layout. |
| `analyze` | Pipeline | Analysis phase. Dispatches `coder` and `data-engineer` under `coder-critic` review; R, Python, Julia. Reads `50_datasets/` before writing loading code. |
| `article-writing` | General | Long-form articles, guides, and newsletters in a voice derived from supplied examples. |
| `careful` | Session | Blocks destructive shell commands for the rest of the session. Layered on top of the always-on `git-guardrails.py` hook. |
| `check-update-upstream-repos` | Maintenance | Diffs the tracked upstream repos against their current state and recommends what to adopt. |
| `checkpoint` | Routine | Session handoff into `passport.yaml`, the research journal, and the personal brain. Records dead ends under "discarded as noise" so a later session does not quote them as conclusions. |
| `coach` | Learning | Learning telemetry — retention stats, calibration, grader audit, dashboard. |
| `coauthor-brief` | Pipeline | Handoff brief so a coauthor can take over a piece of the project: git delta by area, pipeline and integrity roll-up, reproduce-locally steps, open questions. Access process only, never restricted data. |
| `connect` | Knowledge | Read-only cross-theme bridge-finder between wikis and the personal brain. |
| `content-engine` | General | Platform-native content for X, LinkedIn, TikTok, YouTube, and newsletters. |
| `create-project` | Project | Scaffolds a project — folder tree, `passport.yaml`, `CLAUDE.md`, `wiki-links.md`, dashboard seed, and a main thematic wiki. |
| `daily-summary` | Routine | End of day: commits the day's work per project, summarizes it, scans mail and Slack if authorized, logs to `_brain/daily/`. |
| `dashboard` | Pipeline | Generates or refreshes the project dashboard HTML from the passport, literature, data, analysis, results, reviews, and git history. |
| `data-scraper-agent` | General | Builds a scheduled data-collection agent for a public source. |
| `diagnose` | Pipeline | Root-causes a wrong or failing empirical result: reproduce, minimise, hypothesise, instrument, fix. Will not edit before it can reproduce, or fix before it can explain. |
| `discover` | Pipeline | Discovery phase — research interview, literature search (narrative or PRISMA), data discovery, ideation. Post-flight verification runs on the literature and ideation outputs. |
| `documentation-lookup` | General | Current library and framework docs via Context7 rather than training data. |
| `exa-search` | General | Neural web, code, and company search via Exa. |
| `freeze` | Session | Blocks edits outside the named directories for the rest of the session. |
| `frontend-slides` | General | Animated HTML presentations, from scratch or converted from PowerPoint. |
| `git-workflow` | General | Branching strategies, commit conventions, merge-vs-rebase, conflict resolution. |
| `learn` | Learning | Teaches a concept properly — first-principles curriculum, Socratic tutoring, verified free recall, FSRS-scheduled reviews. |
| `peer-review` | Pipeline | Review phase. Routes to referees and the editor, owns the blocking integrity gate, and runs the post-judge hallucination gate over anything the editor added that no referee raised. |
| `procedure` | Routine | Authors, inspects, and promotes the step-by-step processes in `_brain/procedures/`. Promotion to a skill is computed, not remembered. |
| `prompt-optimizer` | General | Advisory prompt rewrite. Never runs the task itself. |
| `python-patterns` | General | Pythonic idioms, PEP 8, type hints. |
| `python-testing` | General | pytest and TDD patterns — fixtures, mocking, parametrization, coverage. |
| `recall` | Learning | Clears due spaced-repetition reviews by free recall. |
| `research-os-help` | Project | The front door. Inside a project it reports the pipeline stage and the exact next step; outside one it routes to the right skill. Has a catalog mode and an ELI5 mode. |
| `revise` | Pipeline | R&R cycle — classify referee comments, route them, draft the response letter, then audit the letter before it goes back. |
| `strategize` | Pipeline | Identification strategy, pre-analysis plan, or formal theory. Reads the wiki's `40_methods/` page for the chosen design first. |
| `submit` | Pipeline | Submission phase — journal targeting, replication package, `environment` capture, audit, citation conversion, AI-use disclosure, final gate. |
| `talk` | Pipeline | Beamer or Quarto RevealJS presentations, with visual audit and compilation. |
| `tools` | Pipeline | Project utilities: commit, compile, validate-bib, lint, journal, context, dashboard, deploy, learn, upgrade, permission-check. |
| `week` | Routine | Refresh the live week view — pull the calendar read-only, reconcile the weekly plan's machine-owned block, and regenerate the week note. |
| `weekly-planning` | Routine | End of week: reviews last week against `_brain/daily/`, sets goals and work slots, creates calendar blockers if authorized. |
| `wiki-ingest` | Knowledge | Ingests a source into a thematic wiki — placement, summary, concept/method/dataset updates, log entry. |
| `wiki-maintain` | Knowledge | Audits and remediates registered wikis to the established standards. `--review-auto` surfaces every auto-written change for human review. |
| `wiki-pull` | Knowledge | Retrieves prior knowledge from the brain and the relevant wiki before substantial work. |
| `wiki-push` | Knowledge | Routes durable knowledge from the session — personal synthesis up into `_brain/`, objective knowledge down into the wiki, through the promotion council. |
| `wiki-setup` | Knowledge | Structural setup and health check for the two-layer knowledge model and its Obsidian vault. |
| `workflow-audit` | Routine | Inventories and scores the recurring work across all your roles, so the highest-leverage processes can become procedures. |
| `write` | Pipeline | Drafts paper sections using paragraph-level argument moves, then strips AI patterns. Reads `20_summaries/` and `30_concepts/` for motivation and mechanism paragraphs. |

## Where they came from

The pipeline skills were ported from clo-author and rewired to the numbered folder scheme, with ARS's integrity checks merged in. The wiki skills were vendored here when research-os itself became the global plugin install, retiring a separate sync mechanism. The learning skills (`learn`, `recall`, `coach`) are vendored engram, with research-os's context-sourced intake and wiki linkage woven in — the engine (`scripts/engram.py`) and its three agents live in this plugin rather than a separate install. The general-purpose skills were consolidated from global skills after an audit of what research-os did not already cover. See `docs/PROVENANCE.md` for the full adoption log.
