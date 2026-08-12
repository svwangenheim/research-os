# Permission Registry: Agent Capabilities and Dependencies

Every agent's capabilities, dependencies, and routing are declared here — this is the
**human-readable** narrative. `${CLAUDE_PLUGIN_ROOT}/graph/pipeline.json` is its **machine-readable
twin**: the same PHASE / PARALLEL_GROUP / REQUIRES / PRODUCES / CRITIC / QUALITY_WEIGHT per node,
evaluable by `${CLAUDE_PLUGIN_ROOT}/scripts/graph.py`. Dispatch decisions ("is this node ready?",
"what can run in parallel?") should be computed by the graph, not re-derived from this prose —
`graph.py selftest` fails the build if the two disagree. Read this file to understand *why* a
dependency exists; read the graph (`graph.py why <node>`) to know whether it currently holds.

Paths follow `folder-map.md` (the single source of truth for project paths). State — scores, phase, corpus, claims — lives in `passport.yaml` (schema: `${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml`). Run provenance lives in `00_admin/process/runs.jsonl` (append-only, written by `graph.py record`). Narrative context lives in `00_admin/process/journal.md`.

Adding a new agent: create the agent file in `${CLAUDE_PLUGIN_ROOT}/agents/`, add an entry here, **and** add the matching node to `${CLAUDE_PLUGIN_ROOT}/graph/pipeline.json` (see `graph/schema.md`). Run `graph.py selftest` before committing — it is the check that keeps these two files from drifting apart.

---

## librarian
- **PHASE:** Discovery
- **PARALLEL_GROUP:** discovery
- **REQUIRES:** Research idea or research spec (`passport.yaml` `research:` block)
- **PRODUCES:** `01_literature/reviews/<question-slug>.md` (annotated bibliography + frontier map + positioning, folded into one review — UPDATE IN PLACE per `output-discipline.md`) and `01_literature/bibliography.bib`
  - Records every source in `passport.yaml` `literature_corpus` and refreshes `wiki-links.md`
- **CRITIC:** librarian-critic
- **ESCALATION_TARGET:** User — scope disagreement, user decides breadth vs. depth
- **QUALITY_WEIGHT:** 10% (literature coverage)

## explorer
- **PHASE:** Discovery
- **PARALLEL_GROUP:** discovery
- **REQUIRES:** Research idea or research spec (`passport.yaml` `research:` block)
- **PRODUCES:** `02_data/data-sources.md` (ranked sources with feasibility grades + access instructions) and data dictionaries in `02_data/codebooks/`
  - Records declared external datasets in `passport.yaml` `data_provenance`
- **CRITIC:** explorer-critic
- **ESCALATION_TARGET:** User — data feasibility deadlock, user decides resource trade-offs
- **QUALITY_WEIGHT:** 10% (data quality)

## strategist
- **PHASE:** Strategy
- **PARALLEL_GROUP:** strategy
- **REQUIRES:** `01_literature/reviews/` OR `02_data/data-sources.md`
- **PRODUCES:** `03_analysis/strategy/strategy_memo.md`
  - Required sections: Estimand, Specification, Assumptions, Robustness Plan, Threats
- **CRITIC:** strategist-critic
- **ESCALATION_TARGET:** User — fundamental design question, needs human judgment
- **QUALITY_WEIGHT:** 25% (identification validity)

## theorist
- **PHASE:** Strategy
- **PARALLEL_GROUP:** strategy
- **REQUIRES:** `03_analysis/strategy/strategy_memo.md`
- **PRODUCES:** `03_analysis/strategy/theory_memo.md` and `03_analysis/strategy/notation_glossary.md`; theory `.tex` fragments (`assumptions.tex`, `results.tex`, `proofs.tex`) to `04_paper/academic_paper/sections/`
- **CRITIC:** theorist-critic
- **ESCALATION_TARGET:** User — proof-level disagreement, user adjudicates whether the result holds
- **QUALITY_WEIGHT:** 20% (theory, when present)
- **CONDITIONAL:** Only for paper types with formal theory: econometric methods, theory+empirics, structural identification, methodological reduced-form. Excluded and weight renormalized for applied papers using off-the-shelf estimators.

## data-engineer
- **PHASE:** Analysis
- **PARALLEL_GROUP:** analysis-data
- **REQUIRES:** `03_analysis/strategy/strategy_memo.md` AND strategist-critic score >= 80 (`passport.yaml` `pipeline.stages.strategy`)
- **PRODUCES:** `02_data/cleaned/`, `02_data/codebooks/`, and descriptive/exploratory figures to `03_analysis/output/`
- **CRITIC:** coder-critic
- **ESCALATION_TARGET:** strategist-critic — re-evaluates whether the data specification is tractable
- **QUALITY_WEIGHT:** Included in code quality weight (not scored separately)

## coder
- **PHASE:** Analysis
- **PARALLEL_GROUP:** analysis-code
- **REQUIRES:** `03_analysis/strategy/strategy_memo.md` AND strategist-critic score >= 80
- **PRODUCES:** `03_analysis/scripts/{R,py,jl}/`, `04_paper/academic_paper/tables/`, `04_paper/academic_paper/figures/`, `03_analysis/output/results_summary.md`
- **CRITIC:** coder-critic
- **ESCALATION_TARGET:** strategist-critic — re-evaluates whether the strategy memo is implementable
- **QUALITY_WEIGHT:** 15% (code quality)

## writer
- **PHASE:** Writing
- **PARALLEL_GROUP:** writing
- **REQUIRES:** coder-critic score >= 80 AND `04_paper/academic_paper/tables/` contains `.tex` files
- **PRODUCES:** `04_paper/academic_paper/main.tex`, `04_paper/academic_paper/sections/*.tex`, and the `claim_manifest` in `passport.yaml` (every non-trivial claim traced to its evidence origin — see INV-22)
- **CRITIC:** writer-critic
- **ESCALATION_TARGET:** Orchestrator — structural rewrite, not just polish
- **QUALITY_WEIGHT:** 10% (manuscript polish)

## editor
- **PHASE:** Review
- **PARALLEL_GROUP:** peer-review
- **REQUIRES:** writer-critic score >= 80 AND coder-critic score >= 80 AND the integrity gate has passed (see `quality.md`)
- **PRODUCES:** `04_paper/reviews/editorial_decision.md`
  - Dispatches domain-referee and methods-referee (see below)
  - Synthesizes referee reports into editorial decision
- **CRITIC:** None — the editor IS the review coordinator
- **ESCALATION_TARGET:** User — editorial judgment calls
- **QUALITY_WEIGHT:** None (manages the peer review process, not scored directly)

## domain-referee
- **PHASE:** Review
- **PARALLEL_GROUP:** peer-review
- **REQUIRES:** writer-critic score >= 80 AND coder-critic score >= 80
- **PRODUCES:** `04_paper/reviews/referee_domain.md`
- **CRITIC:** None — referee is already a reviewer
- **ESCALATION_TARGET:** editor
- **QUALITY_WEIGHT:** 12.5% (half of 25% paper quality)

## methods-referee
- **PHASE:** Review
- **PARALLEL_GROUP:** peer-review
- **REQUIRES:** writer-critic score >= 80 AND coder-critic score >= 80
- **PRODUCES:** `04_paper/reviews/referee_methods.md`
- **CRITIC:** None — referee is already a reviewer
- **ESCALATION_TARGET:** editor
- **QUALITY_WEIGHT:** 12.5% (half of 25% paper quality)
- **INTEGRITY GATE:** Co-owns the ARS integrity gate (citation triangulation + anachronism audit) with verifier and writer-critic — see `quality.md`.

## storyteller
- **PHASE:** Presentation
- **PARALLEL_GROUP:** presentation
- **REQUIRES:** writer-critic score >= 80
- **PRODUCES:** `05_outreach/talks/`
- **CRITIC:** storyteller-critic
- **ESCALATION_TARGET:** Writer — talk narrative issues stem from paper structure
- **QUALITY_WEIGHT:** Advisory (reported, non-blocking)

## verifier
- **PHASE:** Submission
- **PARALLEL_GROUP:** submission
- **REQUIRES:** Overall score >= 95 AND all components >= 80 AND the integrity gate has passed (see `quality.md`)
- **PRODUCES:** `04_paper/reviews/verification_report.md`; writes gate results into `passport.yaml` `integrity`
- **CRITIC:** None — infrastructure agent
- **ESCALATION_TARGET:** User
- **QUALITY_WEIGHT:** 5% (replication readiness, 0 or 100)
- **INTEGRITY GATE:** Primary owner of the ARS integrity gate (claim tracing, citation triangulation, temporal/anachronism audit, figure-caption fidelity) — see `quality.md`.

---

## Parallel Groups

Agents in the same parallel group can run concurrently when their REQUIRES are met:

| Group | Agents | When |
|-------|--------|------|
| discovery | librarian, explorer | From the start (only needs research idea) |
| strategy | strategist, theorist | After Discovery (literature OR data assessment) |
| analysis-data | data-engineer | After Strategy (approved strategy memo) |
| analysis-code | coder | After Strategy (approved strategy memo) |
| writing | writer | After Analysis (approved code output) |
| peer-review | editor, domain-referee, methods-referee | After Writing (approved paper + code + integrity gate) |
| presentation | storyteller | After Writing (approved paper) — can run parallel with Review |
| submission | verifier | After Review (editorial accept/minor + overall >= 95 + integrity gate) |

## Phase Order

```
Discovery → Strategy → Analysis → Writing → Review → Revision → Submission
                                      ↕
                                Presentation (parallel)
```

This diagram is the common case, not a waterfall — it names the typical order, not a required
one. **The graph, not this diagram, is authoritative for what can run next.** A project that
already has data can enter at Strategy; a project with an approved strategy memo can run
data-engineer and coder concurrently; a rejected editorial decision loops back to Strategist, not
back to the top. Run `graph.py next` (or `graph.py why <node>`) rather than reading this order as
a strict sequence.

Phase names match `passport.yaml` `pipeline.stages`. Re-entry is allowed for all phases except Submission (terminal). A referee comment can trigger re-entry at any prior phase — the graph's `editor` node encodes exactly this: `major` routes back to `writer`, `reject` routes back to `strategist`.
