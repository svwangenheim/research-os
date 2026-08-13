# Confidential and Restricted-Data Protocol

**Some data must never leave the machine it was approved for, and some results must never leave the secure environment.** Empirical economics runs on restricted access — administrative registers, social-security and tax records, firm panels, health data, IRB-governed human subjects. In the German setting that means IAB/FDZ, Destatis research data centres, Bundesbank RDSC, SOEP special releases, and the enclave or remote-execution rules attached to each.

This is a template. Replace the placeholder thresholds and providers with the actual terms of your data-use agreement.

## The three hard rules

1. **Never commit raw confidential data.** Raw microdata, identifiers, and provider-supplied extracts do not belong in git — not in a private repo, not once. `.gitignore` must cover `02_data/raw/`, `02_data/restricted/`, and any path your DUA names. Commit *code* and *disclosure-cleared* outputs only.
2. **Nothing leaves without disclosure clearance.** Any table, figure, coefficient or count built on restricted data passes disclosure review *before* it appears in a draft, a slide, a commit, or an email. The provider's official review is mandatory and final; anything done locally is a pre-screen.
3. **Access is per-person, per-agreement.** A co-author without the DUA cannot receive the data, the identifiers, or outputs that fail disclosure rules. A handoff carries *instructions to obtain access*, never the data.

## Disclosure avoidance

Encode your provider's actual thresholds here — they differ, and using the wrong one is itself a violation:

- **Minimum cell count** (commonly n < 5 or n < 20 suppressed; FDZ and Destatis differ).
- **Dominance rules** for establishment data (p-percent, (n,k)).
- **Complementary suppression** — suppressing one cell leaks through row and column totals, so suppress the complements too.
- **No exact extreme values, no unrounded sensitive statistics, no small-group identifiers, no fine geography.**

When a numeric claim rests on restricted data, its `claim_manifest` entry should note the disclosure status, and the replication package deposits cleared outputs plus *access instructions* — never the data. This is the standard restricted-data deposit path for openICPSR and the AEA Data Editor.

## Human subjects and IRB

If the data covers human subjects: record the protocol number, the approved use, and any consent constraints in `00_admin/`. Do not analyse beyond the approved scope. Storage, retention and destruction terms belong in the data management plan.

## Working safely inside a restricted project

- **Turn on strict path enforcement.** `RESEARCH_OS_STRICT_PATHS=1` makes `hooks/git-guardrails.py` *deny* rather than warn on absolute machine paths in analysis code. In a restricted project a hardcoded path is not just a replication problem — it names a location on a secured machine.
- **The git guardrails matter more here.** Blanket staging (`git add -A`) is the single most common way raw data reaches a commit; the hook blocks it unconditionally.
- **Machine-specific restricted paths stay local** — in project-local state, never in a committed file.
- A collaborator joining gets a handoff with environment setup and **access-request steps**, not a data drop.

## Cross-references

- `${CLAUDE_PLUGIN_ROOT}/rules/content-invariants.md` — INV-16 (no absolute paths), enforced at write time by `hooks/git-guardrails.py`.
- `${CLAUDE_PLUGIN_ROOT}/rules/quality.md` — the integrity gate reads `claim_manifest`, where the disclosure status is recorded.
- `${CLAUDE_PLUGIN_ROOT}/skills/submit/SKILL.md` — the replication package and the restricted-data deposit path.
