---
name: diagnose
description: Root-cause a wrong or failing empirical result with a disciplined reproduce, minimise, hypothesise, instrument, fix loop instead of guessing and poking. Use when the user says "why is my regression wrong", "this number changed", "my script errors out", "the result won't reproduce", "debug this", "this estimate looks wrong", "it worked yesterday", or when a replication check FAILs and you need to find which step drifted. Tuned for research code (R, Python, Julia, Stata) where the bug is usually a silent wrong number, not a crash. NOT a code-quality review with no specific symptom (use /peer-review --code) and NOT a whole-paper numeric audit (use /peer-review --replicate).
argument-hint: "[file, script, or a short description of the symptom] [--no-fix]"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, Task
disable-model-invocation: true
---

# Diagnose

Find *why* an analysis errors, returns the wrong number, or will not reconcile.

**Input:** `$ARGUMENTS` — a file, a script, or a short description of the symptom, optionally followed by `--no-fix` to localize the root cause without editing.

**The discipline: never edit before you can reproduce, and never fix before you can explain.** A guessed fix that makes the symptom disappear without a named root cause is how a wrong number gets laundered into a published table. The bug is still there; it has only stopped announcing itself.

Most bugs in research code do not crash. They run cleanly and return something plausible. That is what this skill is shaped around.

## When to use something else

- **`/peer-review --replicate`** — verifying *all* numeric claims against the code (claim-driven, whole-paper). If it reports one FAIL and you want to localize which step produced it, it hands off *to* here.
- **`/peer-review --code`** — code quality with no specific symptom.
- **`/submit environment`** — when version or seed drift is the suspect and you need the environment pinned first.

Diagnose is symptom-driven and single-target: **one wrong number, or one failing run.**

## Phase 0 — Pin the symptom

State the bug as a falsifiable gap before touching anything:

- **Expected:** the value you believe correct, and *why* — a prior run, a paper table, a hand calculation, a theoretical sign.
- **Actual:** what happens now, copied verbatim. The full error, not a paraphrase.
- **Tolerance:** what separates "same" from "different", keyed to where *expected* came from. A prior run on this machine → machine epsilon plus display rounding. A published table → rounding plus a little slack (~1e-3). A hand calculation → ~0.01. A theoretical prediction → an economic-significance band, not a decimal.

Do not chase 1e-12 floating-point noise, and do not wave away a 5% gap. If expected and actual cannot both be stated, the task is *understanding*, not diagnosis — stop and clarify.

## Phase 1 — Reproduce deterministically

A bug you cannot reproduce on demand cannot be fixed, only hidden.

1. Remove every source of nondeterminism you can: set the seed, pin the working directory, record `sessionInfo()` / `pip freeze` / Stata `version`.
2. Re-run the smallest unit that shows the bug and confirm it fails **every time**.

An intermittent failure is itself a hypothesis — uninitialised RNG, order-dependent merge, a race in parallel code. Note it and carry it into Phase 3 rather than re-running until it happens to fail.

## Phase 2 — Minimise to a reproducible example

Shrink until the bug sits in the open.

- **Data:** subset to the fewest rows and columns that still reproduce it — often one group, one period, a handful of rows.
- **Code:** strip to the shortest path from input to wrong output.

Each removal that *keeps* the bug is information; each that *kills* it is a stronger signal. Record which. The minimal example is the deliverable even when the fix turns out to be one character — it is what makes the root cause undeniable rather than asserted.

## Phase 3 — Hypothesise, then rank

**Write the candidate list before testing any of it.** A written list beats poking because it stops you fixating on the first idea that occurs to you.

The usual suspects in research code, all of which run without an error message:

- **Types and coercion** — a numeric read as character or factor, integer overflow, a date parsed wrong, `TRUE`/`FALSE` silently becoming `1`/`0`.
- **Missingness** — `NA` dropped silently, `na.rm` flipping a mean, listwise deletion changing the sample mid-pipeline.
- **Joins and shape** — a many-to-many merge inflating rows, duplicate keys, an unbalanced panel where balance was assumed.
- **Specification** — wrong clustering level, fixed effects absorbed twice, a lag or lead off by one.
- **Bad controls and colliders** — a control that is post-treatment, a mediator on the causal path, a descendant of treatment. Adding it *induces* bias invisibly. The tell is a coefficient that moves the wrong way or shrinks implausibly when the control enters.
- **Numerical stability** — an optimizer that did not converge (check the convergence code, not just the estimates), a near-singular Hessian, collinearity, tolerance set too loose.
- **Weighting** — weights dropped or truncated, renormalised wrong, frequency versus probability versus analytic weights confused, applied after a transform rather than before.
- **Sample** — a filter that runs before rather than after a transform, an outlier rule applied inconsistently.
- **Environment** — a package version bump that changed a default, a moved seed, locale or encoding.

For a genuinely ambiguous bug, fan out the top competing hypotheses to parallel `Task` subagents with `context: fork`, one per hypothesis, each instructed to try to **confirm its own cause** against the minimal example and report back. Three is the practical ceiling.

### Phase 3b — Reduce, so you do not launder a guess

Each hypothesis returns `{hypothesis, evidence for, evidence against, confidence, one-line conclusion}`. Then:

- **One clear winner** (high confidence, others refuted) → Phase 4 to confirm the mechanism.
- **A near-tie** (top two within ~20 points) → do **not** pick one. Go to Phase 4 and instrument to discriminate.
- **Nothing above ~50%** → report the ambiguity and ask. Do not edit on a coin-flip.

## Phase 4 — Instrument and localize

Test the ranked hypotheses cheaply. Do not stare at the code.

- **Bisect the pipeline.** Check the intermediate value at the midpoint of the data flow; the bug is upstream or downstream of it. Repeat. Binary search finds the offending line in `log2(n)` steps rather than `n`.
- **Bisect history.** If it worked yesterday, compare against the last-good commit to pin the change that introduced it. `git bisect` is fine here — it discards nothing, and it is not among the operations the git guardrails hook blocks.
- **Instrument with diagnostics, not guesses.** At each stage: `str()` / `summary()` for types and NA patterns; row and column counts *before and after* every transform; `table()` on factors to catch a silently dropped level; `cor()` or VIF for unexpected collinearity; `range(w)`, `sum(w)`, `anyNA(w)` for weights; the model's convergence flag.

**The stage where a count drops unexpectedly, a factor level vanishes, a correlation jumps, or weights go sparse is the culprit stage.**

End Phase 4 with a one-sentence root cause naming the exact line or step and the mechanism.

## Phase 5 — Fix and verify

**The confidence gate.** Do not apply a fix unless the root cause is named **and** its mechanism is explicit. If Phase 3b left a near-tie, behave as `--no-fix`: report the candidates and ask. Editing research code on an unproven hypothesis is precisely the laundering this skill exists to prevent.

Unless `--no-fix`:

1. Apply the **minimal** fix at the root cause — not a downstream patch that masks it. Fix the bad merge rather than filtering its duplicate rows afterward.
2. Re-run the minimal example; confirm actual matches expected within the Phase 0 tolerance.
3. Re-run the **full** unit and any dependent step; confirm no other number moved. If the result feeds a manuscript claim, re-check it — `hooks/claim-reconcile.py` will already have flagged which claims depend on the file you touched.
4. Propose a **guard** that would have caught this earlier. One per bug class:

   | Bug class | Guard |
   |---|---|
   | Types and coercion | `stopifnot(is.numeric(x))` after read |
   | Missingness | explicit `na.rm = FALSE`; `stopifnot(!anyNA(x))` |
   | Joins and shape | record `nrow` pre-merge; `stopifnot(nrow(out) == nrow(left))` for a 1:1 join |
   | Weighting | `stopifnot(!anyNA(w))`, check `sum(w)` against its expected total |
   | Convergence | assert the convergence flag before using the estimates |
   | Sample | one explicit filter with a stated reason, not a mid-pipe drop |
   | Environment | pin versions (`/submit environment`); `set.seed()` at the top of each script |

   Propose it. Do not silently install a test suite.

With `--no-fix`, stop once the root cause is named and report it for the user to fix by hand. Use this when the file is load-bearing or shared.

## Output

```markdown
# Diagnosis: [one-line symptom]

**Expected:** [value + where it came from]   **Actual:** [value]   **Tolerance:** [threshold]

## Root cause
[One sentence: the exact line or step, and the mechanism.]

## How it was found
- Reproduced: [deterministically? what was pinned]
- Minimal example: [what survived the stripping]
- Hypotheses considered: [ranked, with what refuted the losers]
- Localized by: [bisection point / diagnostic that showed it]

## Fix
[The minimal change, or "not applied (--no-fix)" / "not applied (hypotheses tied)"]

## Verification
- Minimal example: [expected vs actual after fix]
- Full unit re-run: [any other number that moved]
- Dependent claims: [ids flagged by claim-reconcile, and their status]

## Guard proposed
[The one-line assertion that would have caught this.]
```

## Anti-patterns

- **Fixing before reproducing.** If it is intermittent you have not reproduced it, and a fix that coincides with a quiet run proves nothing.
- **Fixing the symptom downstream.** Dropping the duplicate rows a bad merge created leaves the merge bug for the next script.
- **Accepting the first plausible hypothesis.** It is usually the most familiar bug, not this one.
- **Treating the manuscript as ground truth.** The paper's number can be the stale one.
- **Declaring victory on a re-run that happens to match.** Verify against the stated tolerance, and re-run the dependents.

## Cross-references

- `${CLAUDE_PLUGIN_ROOT}/skills/peer-review/SKILL.md` — `--replicate` and the PASS / FAIL / EXPLAINED / STALE / UNMATCHED dispositions this skill localizes.
- `${CLAUDE_PLUGIN_ROOT}/hooks/claim-reconcile.py` — flags which manuscript claims a changed script puts at risk.
- `${CLAUDE_PLUGIN_ROOT}/rules/content-invariants.md` — INV-14 through INV-19; several of the usual suspects are invariant violations.
