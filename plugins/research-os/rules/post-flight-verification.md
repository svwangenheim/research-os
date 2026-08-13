# Post-Flight Verification — checking claims at the point of generation

The integrity gate in `quality.md` §3 is thorough and late. It runs at `/peer-review` and again at `/submit`, which means a fabricated citation introduced during `/discover lit` survives into the strategy memo, the introduction, and three days of argument built on top of it. By the time the gate catches it, the fix is structural rather than a corrected line.

Post-Flight closes that gap. Any skill whose output contains independently checkable factual claims verifies them **before returning**, using a forked verifier that has never seen the draft.

This is the output-side twin of the Pre-*-Report phases (`Pre-Strategy`, `Pre-Code`, `Pre-Theory`). Those prove the inputs were read; this proves the output holds.

## Where it applies

| Skill | The claims that go wrong |
|---|---|
| `/discover lit`, `/discover lit systematic` | Citations. A plausible author-year-venue triple for a paper that does not exist is the single most common failure, and search results make it worse rather than better. |
| `/discover ideate` | Negative-literature claims ("nobody has studied X" is usually false) and dataset-field claims ("the CPS contains `educ_attain`" is confidently wrong about variable names, coverage years, and access status). |
| `/strategize` | Estimator feasibility claims — that a design is identified under the stated data structure. |
| `/write` | Paragraph-level citation claims: "Smith (2019) finds X." |
| `/revise` | "We added X on page Y" assertions about revisions that were not actually made. |

It does **not** apply to mechanical skills (`/tools compile`, `/dashboard`, `/talk compile`). Their output is verified by a compiler, not by a source.

## The protocol

**1. Draft.** Produce the output as usual. Do not skip the check because the draft looks obviously correct — that judgement is made by the same process that produced it.

**2. Extract claims.** Every assertion of the form:
- Citation claims — "Author (Year) shows X"
- Existence claims — "Dataset D contains field F", "package P implements estimator E"
- Numerical facts — sample sizes, coefficients, p-values
- Named entities — researchers, paper titles, venues, institutions
- Negative-literature claims — "no prior work studies X"

Skip opinions ("this is a promising direction"), forward-looking suggestions ("the user could try IV here"), and definitions introduced in the draft itself ("let τ denote the treatment effect"). These are not checkable against a source, and padding the list with them buries the claims that are.

**3. Write one verification question per claim.** Specific, answerable, naming the source. The difference is not cosmetic:

| Too vague to falsify | Answerable |
|---|---|
| "Is Callaway and Sant'Anna (2021) about DiD?" | "In Callaway & Sant'Anna (2021), *J. Econometrics*, what is the estimator named in Section 4?" |
| "Does the estimator need parallel trends?" | "Does Assumption 2 state conditional or unconditional parallel trends?" |

**4. Verify in a fresh context, then reconcile.** Spawn `claim-verifier` via `Task` with `subagent_type=claim-verifier` and `context: fork`. Pass the claims, the questions, and pointers to source material. **Do not pass the draft.** Forking removes it automatically; passing it back defeats the point.

Then act on the outcome:

- **PASS** — every claim `VERIFIED`. Return the draft with the Post-Flight block attached.
- **PARTIAL** — some `CANNOT-VERIFY`, no contradictions. Return the draft with explicit uncertainty flags on the unverified claims, so the reader knows which to check.
- **FAIL** — at least one `CONTRADICTED` or `NOT-FOUND`. **Regenerate the affected section** using the verifier's evidence. After two failed regenerations, return the best draft with the discrepancies surfaced as a warning block. Never silently ship a claim you know to be wrong.

## Output contract

Every skill applying this rule appends:

```markdown
## Post-Flight Verification

**Claims extracted:** N · **Verified independently:** N (forked `claim-verifier`)
**Outcome:** PASS | PARTIAL | FAIL → regenerated

### Unverifiable (check these yourself)
- **C4** — paywalled; abstract does not cover the point

### Discrepancies (corrected)
- **C3** — draft said N = 10,000; source shows N = 1,000. Fixed.
```

## Fail-closed

If the verifier errors, times out, or returns malformed output, **do not present the draft as checked**. Say so:

> Post-Flight verification did not complete (verifier error). These claims have not been independently checked; treat the output as provisional.

Hallucination discipline matters most exactly when things are going sideways, because that is when a silent failure is most likely and most expensive.

## Opt-out

`--no-verify` skips Post-Flight. Legitimate when the user is reading the sources themselves, or is iterating fast on a draft nobody will act on yet. Document the flag in the skill's `argument-hint`.

## Relationship to the integrity gate

Both exist; neither replaces the other.

| | Post-Flight | Integrity gate |
|---|---|---|
| When | At generation, inside the skill | At `/peer-review` and `/submit` |
| Scope | The claims in this one output | Every claim in `claim_manifest` |
| Blocking | No — flags and regenerates | Yes — blocks the phase transition |
| Independence | Context isolation (forked, draft-blind) | Separation of powers (no agent clears its own work) |

Post-Flight makes the gate's job smaller. It does not make it optional.

## Cross-references

- `${CLAUDE_PLUGIN_ROOT}/agents/claim-verifier.md` — the forked verifier.
- `${CLAUDE_PLUGIN_ROOT}/rules/quality.md` — the blocking integrity gate.
- `${CLAUDE_PLUGIN_ROOT}/references/orchestration-schemas.md` — the hallucination gate reuses this mechanism against a judge's own findings.
