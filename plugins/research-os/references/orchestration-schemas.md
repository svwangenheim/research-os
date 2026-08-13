# Orchestration Schemas — the review runtime's data contracts

Critics in this plugin return prose reports carrying a score, and the orchestrator aggregates by reading them. That works, and it has two costs: the verdict depends on how carefully the synthesizer read, and the same severity word can mean different things in different critics.

These schemas are the shared shape critics return **in addition to** their prose report — a fenced `yaml` block at the end. The synthesizer stacks typed objects and applies a predicate, so the verdict becomes a function of the findings rather than a re-judgement of the artifact.

This is a reference, not a runtime. A Claude Code session has no JSON validator in the loop. The schemas are a target shape and a shared vocabulary; the discipline they buy is that "CRITICAL" means one thing everywhere.

---

## 1. `FINDING` — one issue

```yaml
findings:
  - id: M1                       # stable within this run; lens-prefixed is fine
    lens: methods                # the reviewing agent or dimension
    severity: CRITICAL           # CRITICAL | MAJOR | MINOR - the one vocabulary
    location: "Sec 4.2, Table 2 col 3"
    finding: "Identification rests on conditional parallel trends, but the text claims unconditional."
    evidence: "p.11 'parallel trends holds unconditionally' vs Eq.(4), which conditions on X_i."
    recommendation: "State the conditional assumption explicitly, or drop the covariates."
    change_my_mind: "A sentence in Sec 4 reconciling Eq.(4) with the unconditional claim."
    confidence: high             # high | medium | low - the critic's own certainty
```

**Severity is the single cross-skill vocabulary.** Map local wording onto it:

| Local term | Severity |
|---|---|
| fatal, desk-reject-worthy, blocks submission, hard-gate failure | CRITICAL |
| major concern, must fix before review | MAJOR |
| minor concern, polish, nit | MINOR |

Two fields carry more weight than they look:

- **`change_my_mind` is required on every CRITICAL and MAJOR.** A criticism with no achievable ask is a complaint. Forcing the field turns "the identification seems weak" into something the author can act on — or reveals that the critic could not name what would satisfy it, which is itself the finding.
- **`confidence`** is for the judge, not the author. A `low`-confidence CRITICAL is the prime candidate for the hallucination gate below.

## 2. `SCORECARD` — one critic's aggregate

```yaml
scorecard:
  lens: methods
  critical: 1
  major: 3
  minor: 5
  score: 74                      # 0-100, this critic's deduction-table result
  verdict: REVISE-MAJOR          # SUBMIT | REVISE-MINOR | REVISE-MAJOR | REJECT
```

The orchestrator stacks these and computes the weighted aggregate per `rules/quality.md` §1, using the `QUALITY_WEIGHT` declared in `rules/permissions.md`.

## 3. Gate predicates — how the verdict is computed

Deterministic, not a re-judgement:

| Predicate | Rule |
|---|---|
| **PASS** | `sum(CRITICAL) == 0` across all lenses, and every hard gate true |
| **REVISE** | `sum(CRITICAL) == 0` and `sum(MAJOR) > 0` |
| **BLOCK** | `sum(CRITICAL) > 0` |
| **converged** | a round produces **0 new** CRITICAL/MAJOR, deduped on `(location, finding)` |

"New" is measured against the running set of findings already seen. So a critic re-flagging an unfixed issue does not count as progress, and a worker quietly reintroducing one cannot hide inside a clean-looking round.

## 4. The post-judge hallucination gate

A synthesizer reduces findings. It must not **introduce** a blocking claim no critic raised.

This matters here specifically: `/peer-review` has an `editor` that synthesizes two independent referee reports into an editorial decision. Nothing in the current design stops that editor from desk-rejecting on a reason neither referee gave — and a desk-reject is the most consequential verdict the system produces.

The gate:

1. After the judge produces its verdict, diff its CRITICAL / desk-reject reasons against the union of the referees' `findings`.
2. Any CRITICAL not traceable to a referee finding is a **candidate hallucination**.
3. Re-verify each candidate in a fresh fork — `claim-verifier` via `Task` with `context: fork`, given the claim and the artifact location it cites (`rules/post-flight-verification.md`).
   - Grounded in a quote or location → keep it, annotate `[JUDGE-ADDED, verified]`.
   - Cannot be grounded → drop to a flagged note, tag `[JUDGE-HALLUCINATED]`, and **recompute the verdict** under §3 without it.
4. A judge may always *downgrade* or *de-duplicate* freely. It may only *introduce* a blocking finding that survives this gate.

It is cheap — it runs on the 0–2 findings a judge actually introduces — and it is the difference between an autonomous review you can act on and one you have to re-read.

## 5. Loop-until-dry and two strikes

`rules/agents.md` caps worker–critic pairs at three rounds and then escalates. Two refinements:

**Convergence, not a round count.** Stop after **two consecutive dry rounds** — rounds adding zero new CRITICAL/MAJOR, deduped on `(location, finding)`. The three-round cap stays as a fallback for a loop that will not converge, not as the primary stop.

**Two strikes escalates.** The *same* finding surviving rounds N and N+2 goes to the user rather than being patched a third time. Two strikes means the artifact is the wrong shape, not that the wording needs one more pass. This is the same rule `summary-parity.md` applies to prose and `/peer-review --replicate` applies to a claim downgraded to EXPLAINED twice without ever reaching PASS.

## 6. `RUN_CONFIG` — collect interactivity before launch

A forked subagent cannot stop to ask a question. So every interactive choice a fan-out needs is gathered **before** the fleet spawns, echoed back, and only then launched. The Pre-Strategy / Pre-Code / Pre-Theory Reports already do most of this; `RUN_CONFIG` is the same idea for `/peer-review`.

```yaml
run_config:
  artifact: 04_paper/academic_paper/main.tex
  mode: peer                     # peer | stress | methods | theory | replicate | all
  journal: "Journal of Public Economics"
  dispositions: [SKEPTIC, MEASUREMENT]
  fresh_context: true            # re-audit rounds run in a fresh fork
  max_rounds: 3                  # fallback cap, not the primary stop
```

An unresolved required field (an unknown journal, an unreadable artifact) halts **before** launch, never mid-run.

## Cross-references

- `${CLAUDE_PLUGIN_ROOT}/rules/agents.md` — pairing, separation of powers, three-strikes escalation.
- `${CLAUDE_PLUGIN_ROOT}/rules/quality.md` — weighted aggregation, severity gradient, the integrity gate.
- `${CLAUDE_PLUGIN_ROOT}/rules/post-flight-verification.md` — the forked-verifier mechanism §4 reuses.
