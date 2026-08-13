# rules/

Governance rules. Agents and skills read these; several are the single source of truth for something the rest of the system depends on (`folder-map.md` for paths, `permissions.md` for agent capabilities, `model-routing.md` for the model roster).

**Loading.** Rules carrying `paths:` frontmatter are scoped to the files they govern and cost nothing until a matching file is touched. The rest are read by the skills and agents that cite them. Enforcement that must survive context compaction does not live here at all — it lives in `hooks/`, which fire regardless of context state.

## Every rule

<!-- surface-sync-table: rules -->

| Rule | Loading | What it governs |
|---|---|---|
| `agents.md` | on reference | Adversarial pairing, separation of powers, dispatch and escalation, convergence and the two-strikes escalation. |
| `confidential-data.md` | on reference | Restricted and administrative data — never commit raw microdata, disclosure clearance before a figure leaves, access process in handoffs rather than the data. |
| `content-invariants.md` | on reference | The numbered non-negotiables (INV-*). Critics cite invariant numbers, and violations are deductions rather than suggestions. |
| `content-standards.md` | path-scoped | Table, figure, PDF-processing, and exploration standards for analysis code, LaTeX, and generated output. |
| `dialogue-triggers.md` | on reference | The ambient dialogue-trigger registry (`state/dialogue-triggers.json`) — what fires, on what event, budget, and why. The `stage-transition` trigger defers to `graph/pipeline.json` rather than carrying its own next-step logic. |
| `folder-map.md` | on reference | The numbered project layout. Every agent, hook, and skill resolves project paths through this file. |
| `html-dashboard.md` | on reference | Structure and design system of the single-page project dashboard. |
| `lifecycle.md` | on reference | Pre-dispatch and post-completion handoff validation around every agent invocation. |
| `logging.md` | on reference | `passport.yaml` as the single ledger — sessions, pipeline stages, corpus, claims, integrity results — and the narrative journal under `00_admin/process/`. |
| `meta-governance.md` | on reference | The plugin's dual nature: a working system and a reusable template for empirical research. |
| `model-routing.md` | on reference | The model and effort roster, the routing rules, and the anti-patterns — never demote a gate-keeper, never let a critic sit below its worker. |
| `output-discipline.md` | on reference | Update over create. A new file only for a genuinely new question or literature. |
| `permissions.md` | on reference | The agent capability matrix — tools, dependencies, routing, quality weights. Read by the orchestrator to decide dispatch. |
| `post-flight-verification.md` | on reference | Verifying checkable claims at the point of generation through a forked verifier that never saw the draft. PASS ships, PARTIAL ships flagged, FAIL regenerates. |
| `prompt-shaping.md` | on reference | Shaping an informal or ambiguous request before acting on it — a silent standing habit, not an invoked step. |
| `quality.md` | on reference | Scoring, gate thresholds, severity, and the blocking integrity gate. |
| `revision.md` | on reference | The R&R cycle — classifying referee comments and routing them to the right agent. |
| `summary-parity.md` | on reference | Re-verify a whole summary paragraph against its body instead of patching the flagged phrase; prefer abstraction over enumeration. Two flags on one paragraph means rewrite. |
| `wiki-integration.md` | on reference | The two-layer knowledge model — registry resolution, source immutability, and the auto-write blast radius, council gate, audit trail, and kill switch. |
| `workflow.md` | on reference | Plan-first protocol, orchestration, and the dependency graph between phases. |
| `working-paper-format.md` | on reference | The LaTeX working-paper standard for the `academic_paper` output type. |

## Where they came from

The core backbone was ported from clo-author and extended. `folder-map.md` and `output-discipline.md` were written for the numbered project scheme; `model-routing.md`, `post-flight-verification.md`, `summary-parity.md`, `prompt-shaping.md`, and `confidential-data.md` came out of adopting harness-layer patterns from Pedro Sant'Anna's academic Claude Code workflow. See `docs/PROVENANCE.md`.
