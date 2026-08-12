# agents/

Sub-agents dispatched by skills. Each is a single `.md` file whose frontmatter declares `name`, `description`, `tools`, `model`, and `effort`.

**Every agent pins its model and effort. None inherit.** The argument is protection rather than cost: with agents on `model: inherit`, running a session on a cheaper model silently downgrades the referees, the verifier, and the integrity gate along with it, and the gates that decide whether a paper is sound get weaker because someone picked a different session model for an unrelated reason. `rules/model-routing.md` records the roster, the routing rules, and the reason for each tier; `scripts/check_plugin_integrity.py` fails the commit if an agent drops back to `inherit` or loses its `effort`.

Capabilities and dispatch routing are declared once in `rules/permissions.md` — adding an agent means adding a file here and a row there, and nothing else changes.

## Every agent

<!-- surface-sync-table: agents -->

| Agent | Model / effort | Dispatched by | What it does |
|---|---|---|---|
| `claim-verifier` | opus / xhigh | post-flight verification, `/peer-review` | Fresh-context fact-checker, forked so it never sees the draft. Answers verification questions about citations, numbers, dataset fields, and negative-literature claims from source material alone. |
| `code-reviewer` | sonnet / high | after code changes | Senior-engineer review pass over a diff. |
| `coder` | sonnet / high | `/analyze` | Implements the empirical strategy in R, Python, or Julia. |
| `coder-critic` | opus / high | `/analyze` | Reviews analysis and cleaning scripts across 16 check categories — strategic alignment, numerical discipline, reproducibility. |
| `data-engineer` | sonnet / high | `/analyze` | Cleaning scripts, publication-quality figures, data documentation. |
| `domain-referee` | opus / xhigh | `/peer-review` | Blind referee on subject substance — contribution, positioning, external validity. Holds its frame under author pushback. |
| `editor` | opus / xhigh | `/peer-review` | Desk-reviews, then synthesizes the two referee reports into an independent editorial decision. Its added CRITICALs go through the hallucination gate. |
| `engram-artifact-smith` | sonnet / high | `/learn` | Builds interactive HTML explorables for threshold concepts. |
| `engram-assessor` | opus / high | `/learn`, `/recall`, `/coach` | Grades learner productions, deliberately blind to the tutoring dialogue. |
| `engram-curriculum-architect` | opus / high | `/learn` | Decomposes a topic into a first-principles concept DAG. |
| `explorer` | sonnet / medium | `/discover` | Finds and evaluates datasets; produces a ranked source list with feasibility grades. |
| `explorer-critic` | sonnet / high | `/discover` | Reviews the data assessment for measurement validity, sample selection, and identification compatibility. |
| `guide-writer` | sonnet / medium | writing skills | Documentation and guide pages in a pedagogical, tutorial voice. |
| `librarian` | sonnet / medium | `/discover` | Collects and organizes literature; PRISMA-aware systematic-review mode. |
| `librarian-critic` | sonnet / high | `/discover` | Reviews the bibliography for coverage gaps, journal quality, scope calibration, recency. |
| `methods-referee` | opus / xhigh | `/peer-review` | Blind referee on empirical methods. Co-owns the integrity gate — citation triangulation and the temporal/anachronism audit. |
| `orchestrator` | opus / high | infrastructure | Phase transitions, agent dispatch, escalation routing, separation of powers, quality gates. |
| `python-reviewer` | sonnet / high | after Python edits | PEP 8, idiom, type-hint, security, and performance review. |
| `storyteller` | sonnet / medium | `/talk` | Builds the presentation in Beamer or Quarto RevealJS across four formats. |
| `storyteller-critic` | sonnet / high | `/talk` | Reviews narrative flow, visual quality, content fidelity, and whether it compiles. |
| `strategist` | opus / high | `/strategize` | Designs the empirical strategy and writes the strategy memo. |
| `strategist-critic` | opus / xhigh | `/strategize` | Gatekeeper on identification. Four sequential review phases; must sign off before analysis begins. |
| `theorist` | opus / high | `/strategize` | Assumptions, definitions, lemmas, theorems, and formal proofs. |
| `theorist-critic` | opus / xhigh | `/strategize` | Checks logical validity, minimality of conditions, measurability, notation, and linkage to the empirical claims. |
| `verifier` | opus / xhigh | `/tools`, `/peer-review`, `/submit` | Infrastructure inspector and primary owner of the integrity gate — claim tracing, citation triangulation against the wiki corpus and external databases, anachronism audit, figure–caption fidelity. |
| `wiki-librarian` | sonnet / high | wiki skills | Enforces the two-layer knowledge model's standards — retrieval, routing, deduplication, note quality. |
| `wiki-promotion-council` | opus / high | `/wiki-push`, `/wiki-ingest`, `/wiki-maintain` | Five isolated critics voting YES/NO on layer-routing, canonicity, staleness, evidence, and format. The gate that licenses auto-write into the wiki. |
| `writer` | sonnet / high | `/write` | Drafts paper sections using paragraph-level argument moves, then strips AI patterns. |
| `writer-critic` | opus / high | `/write` | Reviews structure, claims–evidence alignment, identification fidelity, voice fidelity, and claim–source traceability across 8 check categories. Co-owns the integrity gate. |

## Pairing

Most workers have a paired critic, and the pairing is adversarial by construction: critics have read-only tools, workers cannot grade their own output, and no agent clears its own work through a gate. Where worker and critic sit at the same tier the critic is pinned deliberately above it — a critic weaker than what it reviews cannot catch what the worker missed. `rules/agents.md` covers the dispatch and escalation protocol, including the two-strikes rule that escalates a finding surviving two review rounds instead of patching it a third time.
