# Quality: Scoring, Thresholds, and Severity

---

## 1. Scoring Protocol

**How individual agent scores aggregate into the overall project score.**

### Weighted Aggregation

The overall project score that gates submission (>= 95) is a weighted aggregate. Each agent's QUALITY_WEIGHT is declared in `permissions.md`.

The Orchestrator reads the registry to compute the weighted average:
- Sum each agent's critic score multiplied by its declared weight
- Theory weight applies only when the theorist agent was dispatched (see CONDITIONAL flag in `permissions.md`)
- If a component hasn't been scored, exclude it and renormalize remaining weights
- The **integrity gate** (Section 3) folds in as a pass/fail component — a FAIL blocks regardless of the weighted total

Component scores and the current phase live in `passport.yaml` `pipeline.stages`; the integrity gate's results live in `passport.yaml` `integrity`.

### Minimum Per Component

No component can be below 80 for submission. A perfect literature review can't compensate for broken identification.

### Score Sources

- Each critic produces a score from 0 to 100 based on its deduction table
- Scores start at 100 and deduct for issues found
- The verifier is pass/fail (mapped to 0 or 100)
- Referee scores are averaged: `(domain-referee + methods-referee) / 2`

### Gate Thresholds

| Gate | Overall Score | Per-Component Minimum | Action |
|------|--------------|----------------------|--------|
| Commit | >= 80 | None enforced | Allowed |
| PR | >= 90 | None enforced | Allowed |
| Submission | >= 95 | >= 80 per component | Allowed |
| Below 80 | < 80 | — | Blocked |

### When Components Are Missing

Not every project uses all components. If a component hasn't been scored:
- It's excluded from the weighted average
- Remaining weights are renormalized
- Example: no literature review → weights become 11%, 28%, 17%, 28%, 11%, 6%

---

## 2. Severity Gradient

**Critics calibrate severity based on the phase of the project.**

### Phase-Based Severity

| Phase | Critic Stance | Rationale |
|-------|--------------|-----------|
| Discovery | Encouraging (low severity) | Early ideas need space to develop |
| Strategy | Constructive (medium severity) | Identification must be sound, but alternatives should be suggested |
| Analysis | Strict (high severity) | Code and results are near-final — bugs are costly |
| Writing | Strict (high severity) | Manuscript is near-final — bugs are costly |
| Review | Adversarial (maximum severity) | Simulates real referees — no mercy |
| Presentation | Professional (medium-high) | Talks should be polished but scored as advisory |

### How It Works

The Orchestrator includes the severity level in the critic's prompt:

```
You are reviewing at SEVERITY: HIGH (Analysis phase).
Flag all issues. Do not suggest "consider" — state what must change.
```

### Deduction Scaling

The same issue may have different deductions by phase:

| Issue | Discovery | Strategy | Analysis/Writing | Review |
|-------|-----------|----------|------------------|--------|
| Missing citation | -2 | -5 | -10 | -15 |
| Notation inconsistency | -1 | -3 | -5 | -5 |
| Hedging language | — | — | -3 | -5 |
| Missing robustness check | — | -5 | -15 | -20 |

### Principle

Early phases are about getting the direction right. Late phases are about getting the details right. Critics should match their tone and rigor to the phase.

---

## 3. The ARS Integrity Gate (BLOCKING)

**A blocking gate that runs before `/peer-review` and again before `/submit`.** Adapted from ARS (academic-research-skills). It is not advisory: a FAIL blocks advancement to Review or Submission no matter how high the weighted aggregate is. Results are written to `passport.yaml` `integrity` (with any blocking issues in `integrity.unresolved` and flags in `contamination_signals`).

### The Four Checks

1. **Claim tracing** — Every claim in `passport.yaml` `claim_manifest` must trace to a real evidence origin (a `bibkey` in `literature_corpus`, a `data:<path>`, an `analysis:<script>`, or explicit reasoning). Any claim with no traceable origin, or whose `evidence_origin` does not exist, FAILS. Sets `claims_verified` / `claims_total` in `passport.yaml` `integrity`.
2. **Citation triangulation** — Every cited reference is checked against **Semantic Scholar, OpenAlex, Crossref, and arXiv**. The goal is to catch **fabricated or mis-cited references** — a paper that does not exist, a wrong author/year/venue, a working paper cited as published, or a DOI that resolves to something else. Unverifiable entries are marked `% UNVERIFIED`; fabricated or contradicted entries FAIL. Sets `citations_triangulated`.
3. **Temporal / anachronism audit** — No claim may cite or rely on evidence that postdates the event it explains, and no citation may reference work that did not yet exist at the stated time. Anachronisms (a result attributed to a paper published later, a dataset used before it was released) FAIL and are recorded in `contamination_signals`.
4. **Figure–caption fidelity** — Every figure/table caption must faithfully describe what the figure/table actually shows: the numbers in the caption match the underlying output, the described variables match the axes/columns, and the stated sample/source matches the data. Captions that overstate, mislabel, or describe a different result FAIL.

### Scoring and Aggregation

- The gate produces an overall **PASS / FAIL** plus a per-check breakdown.
- **FAIL is blocking:** the Orchestrator does not dispatch `/peer-review` and does not permit `/submit` while any check fails. Blocking issues are listed in `passport.yaml` `integrity.unresolved`.
- On PASS, the gate contributes to the weighted aggregate as part of the verifier's replication-readiness component (Section 1). A partial pass (e.g. some `% UNVERIFIED` citations that are plausible but unconfirmed) is surfaced to the user as a warning, not an automatic block, but must be acknowledged before `/submit`.

### Ownership (Separation of Powers preserved)

The gate is co-owned so that no single agent both writes and clears its own work:

| Check | Owner |
|-------|-------|
| Claim tracing | verifier (reads `claim_manifest`), cross-checked by writer-critic |
| Citation triangulation | verifier + methods-referee (external-database lookups) |
| Temporal / anachronism audit | methods-referee |
| Figure–caption fidelity | writer-critic |

The verifier is the primary owner and records the gate result; writer-critic and methods-referee supply the checks that touch the manuscript text and citations. Consistent with `agents.md`, critics never fix what they flag — they score and list; the writer/coder remediate.
