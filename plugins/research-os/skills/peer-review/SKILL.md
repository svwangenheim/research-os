---
name: peer-review
description: All quality reviews for the paper (any type) or code -- routes to the appropriate critics based on target and flags. Owns the BLOCKING ARS integrity gate (claim tracing, citation triangulation, temporal/anachronism audit, figure-caption fidelity) that must pass before a peer-review or submission pass. Supports every paper type -- imrad, literature_review, theory, case_study, conference. Review phase of the research-os pipeline; writes referee/editorial reports to 04_paper/reviews/ and scores into passport.yaml.
argument-hint: "[file path or --flag] Options: --peer [journal], --peer --r2/--r3 [journal], --stress [journal], --methods, --theory [target], --proofread, --code [file], --replicate [lang], --all"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash,WebSearch,Task
---

# Peer Review

Unified review command that routes to the appropriate critic agents based on the target and flags.

**Input:** `$ARGUMENTS` -- file path and/or flags.

State lives in **`passport.yaml`** (schema: `${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml`). Paths follow `${CLAUDE_PLUGIN_ROOT}/rules/folder-map.md`: manuscript peer-review reports (editorial decision, referee reports) live in `04_paper/reviews/`; standalone code reviews update `03_analysis/output/code_review.md`; talk reviews live beside the talk in `05_outreach/talks/`. Outputs obey `${CLAUDE_PLUGIN_ROOT}/rules/output-discipline.md`: **update the existing report in place with a `## Changelog`; a new file only for a genuinely new target (a different manuscript, a different script).** Critic scores land in `passport.yaml` `pipeline.stages.review` (gate 90); Review-phase severity is Adversarial/maximum (`${CLAUDE_PLUGIN_ROOT}/rules/quality.md` Section 2).

**This skill owns the ARS integrity gate.** No `--peer`, `--stress`, or `--all` pass may report PASS, and the editor may not be dispatched, until the gate in `${CLAUDE_PLUGIN_ROOT}/rules/quality.md` Section 3 has run and returned PASS. See "The ARS Integrity Gate" below.

---

## Routing Logic

### Auto-detect by file type
- `.tex` paper file (in `04_paper/academic_paper/`) -> **Comprehensive review** (writer-critic + strategist-critic [+ theorist-critic if a theory section exists] + verifier)
- `.R`, `.py`, `.do`, `.jl` file -> **Code review** (coder-critic standalone, categories 5-16)
- `.tex` talk file (in `05_outreach/talks/`) -> **Talk review** (storyteller-critic, advisory)

### Explicit flags (override auto-detect)
- `--peer [journal]` -> **Full peer review** (integrity gate -> editor desk review -> referee dispatch -> editorial decision)
- `--peer --r2 [journal]` / `--peer --r3 [journal]` -> **R&R round 2/3** (integrity gate re-run -> same referees, same dispositions, memory of prior review, anti-sycophancy scoring)
- `--stress [journal]` -> **Hostile stress test** (same flow, adversarial referee dispositions; advisory, non-blocking)
- `--methods` -> **Causal audit** (strategist-critic standalone, 4-phase review)
- `--theory [target]` -> **Proof audit** (theorist-critic standalone, 4-phase review -- logical validity, assumption minimality, citations, linkage)
- `--proofread` -> **Manuscript polish** (writer-critic standalone, categories 4/5/6/8)
- `--code [file]` -> **Code review** (coder-critic standalone, categories 5-16)
- `--replicate [language]` -> **Cross-language replication check** (Coder re-implements in target language + coder-critic + comparison)
- `--all` or no file -> **Paper excellence** (all critics in parallel + weighted score -- theorist-critic included only when a theory section is present, per the CONDITIONAL flag in `permissions.md`)

---

## The ARS Integrity Gate (BLOCKING -- runs before `--peer`, `--peer --r2/--r3`, `--stress`, and `--all`)

Adapted from ARS. `/peer-review` is the sole invoker: no other skill triggers this gate, and the editor may not be dispatched until it returns PASS (`${CLAUDE_PLUGIN_ROOT}/rules/permissions.md`: editor's REQUIRES includes "the integrity gate has passed").

1. **Dispatch verifier** (primary owner, per `quality.md` Section 3 ownership table) to run the four checks against `passport.yaml` and the manuscript:
   - **Claim tracing** -- every `claim_manifest` entry traces to a real `evidence_origin` (a `bibkey` in `literature_corpus`, `data:<path>`, `analysis:<script>`, or `reasoning`). Sets `claims_verified` / `claims_total`.
   - **Citation triangulation** (co-owned with methods-referee) -- every cited reference checked against Semantic Scholar, OpenAlex, Crossref, and arXiv. Unverifiable -> `% UNVERIFIED`; fabricated or contradicted -> FAIL. Sets `citations_triangulated`.
   - **Temporal / anachronism audit** (owned by methods-referee) -- no claim may rely on evidence that postdates the event it explains; no citation to work that did not yet exist at the stated time.
   - **Figure-caption fidelity** (owned by writer-critic) -- every caption's numbers, variables, and stated sample/source match the underlying output.
2. **Write results to `passport.yaml` `integrity`**: `last_gate` (timestamp), `claims_verified`/`claims_total`, `citations_triangulated`, `unresolved` (blocking issues), `contamination_signals` (anachronisms/fabrications found).
3. **PASS** -> proceed to the requested mode. **FAIL** -> stop immediately; report every item in `integrity.unresolved` to the user; do **not** dispatch the editor or referees. Per Separation of Powers (`agents.md`), the flagging agents (verifier, methods-referee, writer-critic) never fix what they found -- the writer/coder remediate, then the gate re-runs.
4. **Partial pass** (e.g. plausible-but-unconfirmed `% UNVERIFIED` citations, no fabrications) -> surface as a warning, not a block, but the user must acknowledge it before proceeding.
5. **Skip for standalone diagnostic modes** that do not move `pipeline.stages.review` -- `--methods`, `--theory`, `--proofread` alone, `--code`, `--replicate`. Still surface any integrity concern noticed incidentally during those reviews.

---

## Paper-Type Awareness (mandatory for all critics)

Review scope adapts to `passport.yaml` `research.paper_type`. Do not penalize a paper for lacking elements that don't apply to its type (a structural paper missing parallel trends is not a defect; a descriptive paper using causal language is).

| Paper/output type | Review emphasis | Typically skipped |
|---|---|---|
| `imrad` (reduced-form / structural / theory+empirics / descriptive) | Full 8-category manuscript review + causal audit matched to the design | -- |
| `literature_review` | writer-critic categories 4/5/6/8 + librarian-critic's 6-category coverage/gap/recency check | strategist-critic (no identification claim to audit) |
| `theory` | theorist-critic 4-phase proof audit + writer-critic notation/exposition | strategist-critic, unless empirics are also tested (theory+empirics) |
| `case_study` | writer-critic + explorer-critic external-validity framing | Causal audit, unless the case study makes an explicit identification claim |
| `conference` | Same as `imrad`, length-calibrated to the venue's page/word limit | -- |

---

## Mode Details

### Comprehensive Review (default for `.tex` paper, `--all`)
Dispatch in parallel:
1. **strategist-critic** -- causal design audit (4 phases)
2. **theorist-critic** -- proof audit (4 phases), only if a theory section exists (CONDITIONAL, `permissions.md`)
3. **writer-critic** -- manuscript polish (8 categories)
4. **verifier** -- compilation check + integrity-gate contribution (Section 1 of `quality.md`)

Compute the weighted aggregate per `quality.md` Section 1 (renormalize if a component is absent). Save the combined report to `04_paper/reviews/[FILENAME]_comprehensive_review.md`, updating in place.

### Full Peer Review (`--peer [journal]`)

Simulates a realistic journal submission. Integrity gate first, then three phases, orchestrated sequentially.

#### Phase 0: Integrity Gate
Run "The ARS Integrity Gate" above. FAIL stops here.

#### Phase 1: Editor Desk Review
Dispatch the **editor** agent with the paper and target journal.

The editor:
1. Reads the paper (abstract, intro, contribution, identification, results)
2. Searches the literature via WebSearch to verify novelty claims
3. Applies **paper-type-aware** judgment (`imrad|literature_review|theory|case_study|conference`) when weighing fit and contribution -- a literature review is not judged against AER's novelty bar for a single empirical result
4. Decides: **DESK REJECT** or **SEND TO REFEREES**
5. If desk reject -> write the decision (with reasons + suggested alternative journals) to `04_paper/reviews/editorial_decision.md`. Done.
6. If send to referees -> editor selects referee dispositions and pet peeves from the journal's **Referee pool**, with paper-type awareness (e.g. a `literature_review` draws less from STRUCTURAL/THEORY; a `case_study` weights CREDIBILITY differently than an `imrad` paper) -- see `${CLAUDE_PLUGIN_ROOT}/references/journal-profiles.md` and `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/disposition-pool.md`

#### Phase 2: Referee Reports
The editor's referee assignment specifies for each referee:
- **Disposition** (one of: STRUCTURAL, CREDIBILITY, MEASUREMENT, POLICY, THEORY, SKEPTIC)
- **Critical pet peeve** (one from the critical pool)
- **Constructive pet peeve** (one from the constructive pool)

Dispatch **domain-referee** and **methods-referee** in parallel, each receiving:
1. The paper manuscript
2. The target journal name (for `journal-profiles.md` calibration)
3. Their assigned disposition and pet peeves, injected into the prompt:

```
DISPOSITION: [disposition name]
You approach this paper with the following intellectual prior: [disposition description]
This shapes your emphasis, not your scoring rubric -- the 5 dimensions remain the same.

PET PEEVES:
- Critical: [critical pet peeve]
- Constructive: [constructive pet peeve]
Give extra weight to these in your review.
```

Both reviews are independent and blind -- neither referee sees the other's report.

Every major comment MUST include a **"What would change my mind"** statement -- the specific evidence, test, or analysis that would resolve the concern.

Save to `04_paper/reviews/referee_domain.md` and `04_paper/reviews/referee_methods.md` (`${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/referee-report-template.md`).

#### Phase 3: Editorial Decision
Dispatch the **editor** agent again with both referee reports.

The editor:
1. Classifies each concern as FATAL / ADDRESSABLE / TASTE
2. When referees disagree, takes a side and explains why (paper-type context informs which disagreements matter)
3. Produces a decision letter: Accept / Minor Revisions / Major Revisions / Reject
4. Lists MUST address, SHOULD address, and MAY push back items

Save to `04_paper/reviews/editorial_decision.md`, updating in place. Log the referee assignments (dispositions + pet peeves) in the decision so the user can re-run with different combinations. Refresh the dashboard: run `/dashboard`.

### R&R Round 2/3 (`--peer --r2 [journal]` / `--peer --r3 [journal]`)

Continues the review cycle after the author has revised the paper.

1. **Re-run the integrity gate** (Phase 0) -- a revision can introduce new claims, new citations, or a new figure that needs its own fidelity check.
2. **Load prior review state** -- read `04_paper/reviews/referee_domain.md`, `referee_methods.md`, `editorial_decision.md`.
3. **Skip desk review** -- the paper was already accepted for review.
4. **Same referees, same dispositions and pet peeves** -- reloaded from round 1.
5. **Referee R&R mode with anti-sycophancy** -- each referee receives their previous report alongside the revised manuscript and the author's response. Per `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/disposition-pool.md` Anti-Sycophancy & Frame-Lock:
   - Score each addressed concern's rebuttal **1-5**.
   - Concede (mark Resolved) **only if the score is >= 4 AND the rebuttal addresses the core critique** -- not a reframed, easier version of it. Otherwise hold the concern (Partially resolved / Not addressed) and restate it.
   - A polite tone, author seniority, or confident phrasing never raises the score -- only evidence in the revised manuscript does.
   - Run the dialogue-health self-check before finalizing (frame-lock vs. goalpost-moving vs. scope-creep-in-reverse -- see the template).
   - New concerns may arise from the revisions themselves; flag them separately.
6. **Editor R&R decision** -- Round 2 allows Accept/Minor/Major/Reject. Round 3 allows Accept/Minor/Reject only. Max 3 rounds total.
7. **Update the same three files in place** (`referee_domain.md`, `referee_methods.md`, `editorial_decision.md`) with a new `## Changelog` entry and the round's R&R addendum -- do not create `_r2.md` / `_r3.md` copies (output-discipline).

### Hostile Stress Test (`--stress [journal]`)

Same three-phase flow as `--peer` (integrity gate still runs first), with these changes:

1. **Editor assigns adversarial dispositions** -- both referees get SKEPTIC or the most demanding disposition for that journal
2. **Double pet peeves** -- each referee gets 2 critical and 1 constructive (instead of 1 and 1)
3. **Referee prompt addition:**
```
You are looking for reasons to REJECT this paper. Your prior is that
the paper is not good enough for [journal]. The authors must convince
you otherwise. Be specific about what would change your mind.
```

This is for pre-submission stress testing. Advisory -- does not block `pipeline.stages.review`. Save to `04_paper/reviews/[FILENAME]_stress_test.md`.

### Code Review (`--code` or auto-detect `.R`/`.py`/`.do`/`.jl`)

**Step 1: Mechanical lint** -- run the grep-based linter first:
```bash
"$CLAUDE_PROJECT_DIR"/.claude/hooks/lint-scripts.sh [file]
```
Include the lint report in the coder-critic's input so it can skip already-flagged patterns and focus on judgment calls.

**Step 2: Judgment review** -- dispatch **coder-critic** in standalone mode (categories 5-16, no strategy-memo comparison). Full checklist: `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/code-review-16-categories.md`.

**Do NOT edit any source files.** Only produce reports. Fixes are applied after user review, via the Coder agent.

Save to `03_analysis/output/code_review.md`, updating in place (one consolidated review, sectioned per script, per `output-discipline.md` -- the same file `/analyze` writes to).

### Causal Audit (`--methods`)

Dispatch **strategist-critic** standalone for a full 4-phase causal inference review (`${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/causal-audit-4-phases.md`):

1. **Phase 1: Claim Identification** -- design, estimand, treatment, control
2. **Phase 2: Core Design Validity** -- design-specific assumption checks; **early-stopping** on CRITICAL issues
3. **Phase 3: Inference** -- clustering, multiple testing, code-theory alignment
4. **Phase 4: Polish and Completeness** -- robustness, sensitivity bounds, citation fidelity

Overall assessment: SOUND / MINOR ISSUES / MAJOR ISSUES / CRITICAL ERRORS. Save to `04_paper/reviews/[FILENAME]_strategy_review.md`.

### Proof Audit (`--theory [target]`)

Dispatch **theorist-critic** standalone for the 4-phase theory review (`${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/theory-review-4-phases.md`): claim identification -> proof validity (early-stop on gaps) -> assumption minimality + notation (INV-7) -> citation fidelity + linkage. Save to `04_paper/reviews/[FILENAME]_theory_review.md`.

### Manuscript Polish (`--proofread`)
Dispatch **writer-critic** standalone -- categories 4, 5, 6, 8 only (writing quality, LaTeX/format, compilation, notation); no strategy alignment. Save to `04_paper/reviews/[FILENAME]_proofread_report.md`.

### Cross-Language Replication (`--replicate [language]`)
1. Auto-detect source language from file extension
2. Dispatch **Coder** in replication mode -- re-implement in target language
3. **coder-critic** reviews both implementations
4. Compare numerical outputs per `${CLAUDE_PLUGIN_ROOT}/skills/analyze/config/replication-tolerances.json` / `00_admin/domain-profile.md`
5. Save replicated script and comparison report to `04_paper/reviews/[FILENAME]_replication_check.md`

---

## Verifier Pass/Fail Definition

The Verifier produces a binary PASS/FAIL result, in addition to its integrity-gate role above.

**For papers (`.tex`):** LaTeX compiles error-free; all figures/tables referenced exist and render; all references resolve (no `??`); bibliography compiles.

**For code (`.R`, `.py`, `.do`, `.jl`):** Runs without errors; all packages loaded at top; no hardcoded absolute paths; `set.seed()` present once if stochastic; output files created at expected paths.

**For replication packages:** All scripts run in declared order; outputs match paper tables/figures within tolerance; README accurately describes the pipeline.

Verifier score maps to 0 (FAIL) or 100 (PASS) for weighted aggregation.

---

## Scoring

| Mode | Blocking? | Gate |
|------|-----------|------|
| Comprehensive (`--all`) | Yes | `pipeline.stages.review.gate` (90) |
| Full Peer Review (`--peer`) | Yes | Integrity gate PASS + editorial decision |
| R&R Round 2/3 | Yes | Integrity gate PASS + editorial decision |
| Stress Test (`--stress`) | Advisory | Reported, non-blocking |
| Code Review (`--code`) | Yes | 80 (analysis component) |
| Causal Audit (`--methods`) | Yes | 80 |
| Proof Audit (`--theory`) | Yes | 80 |
| Proofread (`--proofread`) | Yes (paper) / Advisory (talks) | 80 |

---

## Bundled Resources

### Templates (checklists and report formats)

| File | Used By | Content |
|------|---------|---------|
| `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/manuscript-review-8-categories.md` | writer-critic | 8 check categories: structure, claims, ID fidelity, writing, LaTeX, compilation, voice, notation |
| `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/code-review-16-categories.md` | coder-critic | 16 check categories: strategic alignment (4) + code quality (12) |
| `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/causal-audit-4-phases.md` | strategist-critic | 4-phase sequential protocol: claim, design, inference, polish |
| `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/theory-review-4-phases.md` | theorist-critic | 4-phase theory review: claim, proof validity, assumptions, citations/linkage |
| `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/talk-review-6-categories.md` | storyteller-critic | 6 check categories: narrative, visual, content, scope, compilation, coherence |
| `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/literature-review-6-categories.md` | librarian-critic | 6 check categories: coverage, journal quality, scope, recency, categorization, BibTeX |
| `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/data-review-6-categories.md` | explorer-critic | 6 check categories: measurement, sample, external validity, alternatives, feasibility, ID compatibility |
| `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/disposition-pool.md` | editor | Referee dispositions, pet peeves, desk reject criteria, decision rules, report formats, Anti-Sycophancy & Frame-Lock |
| `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/templates/referee-report-template.md` | domain-referee, methods-referee | Standard report format, incl. R&R rebuttal-score addendum |

### Config
| File | Content |
|------|---------|
| `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/config/scoring-rubrics.md` | Consolidated deduction tables for all critics + quality gates |

### Gotchas
| File | Content |
|------|---------|
| `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/gotchas.md` | Known failure points and edge cases for all review modes |

---

## Principles
- **Integrity before everything.** No `--peer`/`--stress`/`--all` PASS, and no editor dispatch, without the ARS integrity gate passing first.
- **Smart routing.** File type determines the default review mode; flags override.
- **Critics never edit.** All reviews produce reports only.
- **Journal drives everything.** The journal profile shapes the editor's bar, referee selection, and review culture.
- **Referees vary.** Different dispositions and pet peeves mean running `/peer-review --peer` twice gives different feedback -- just like submitting to two journals would.
- **Anti-sycophancy across rounds.** In R&R, referees score rebuttals 1-5 and concede only on strong evidence addressing the core critique -- never on tone. Run the dialogue-health self-check every round.
- **"What would change my mind."** Every major referee comment must include the specific evidence or analysis that would resolve the concern.
- **Paper-type aware, always.** All five types (`imrad|literature_review|theory|case_study|conference`) are first-class; don't penalize a paper for lacking elements its type doesn't require.
- **Sequential phases in causal/theory audits.** Never skip to polish before verifying the core design or proof holds.
- **Worker-critic separation.** The reviewer never fixes code or rewrites text -- it only critiques.
- **Update over create.** One report per target, updated in place with a Changelog -- R&R rounds update, never duplicate.
