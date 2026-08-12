# Summary–Body Parity — against whack-a-mole

**When you edit a summary paragraph, do not apply a surgical word-level fix.** Summaries drift from their bodies when the body changes and the summary is not re-verified. Patching the flagged phrase almost always introduces a new drift elsewhere in the same paragraph, so the next review flags it again and the paragraph never converges.

This rule exists because the failure is structural, not lexical. research-os carries counts and enumerations across five surfaces (`README.md`, `plugins/research-os/README.md`, and the `skills/`, `rules/`, `hooks/` READMEs), and every skill, agent and rule carries a `description:` that summarizes a body that keeps changing.

## What counts as a summary paragraph

- Skill / agent / rule frontmatter `description:` — the highest-traffic case
- README taglines and section ledes
- `CHANGELOG.md` entry ledes
- Commit message `## Summary` blocks and PR titles
- Dashboard section ledes and `_map.md` note ledes
- Any paragraph of the form "This does X. It does not do Y. Counts are Z." — the triple-claim shape is a drift magnet

## The protocol

1. **Read the full body** the summary summarizes. Not the diff — the whole thing.
2. **Enumerate every substantive claim** in the current summary: every noun list, every count, every superlative ("no new"), every inclusion or exclusion ("except X").
3. **Check each claim against the body**, finding the content that supports or refutes it.
4. **Edit the whole paragraph, not the flagged phrase.** Any claim that no longer holds is corrected in place.
5. **Re-scan for orphans.** A claim removed from the summary must not survive in the body unreferenced, and vice versa.

## Two strikes means rewrite

If the same summary paragraph is flagged **twice** — even on different words — stop patching and rewrite it structurally. Two hits on one paragraph means the paragraph is the wrong shape, not that the wording needs one more touch.

**Rewrite bias: prefer abstraction over enumeration.** A summary that makes no enumerative claim cannot drift.

| Drift-prone | Drift-proof |
|---|---|
| "No new skills, no new rules, no new hooks" | "No new directories on disk" |
| "43 skills / 27 agents / 16 rules / 10 hooks" | "On-disk inventory unchanged — see README for counts" |
| "Edits to `agents/verifier.md` and `skills/discover/SKILL.md`" | "Existing pipeline components revised" |

The specific form is more informative when fresh and more likely to rot. The abstract form stays true across edits.

## Where the mechanical check ends and this rule begins

`scripts/check_surface_sync.py` verifies counts and enumerative table rows against disk. It cannot tell whether a *prose* claim still describes its body. The script owns the countable half; this rule owns the rest.

## The two-strikes pattern travels

The rule generalizes to anywhere a disagreement can be quietly re-papered each round rather than resolved:

- **Worker–critic loops** (`agents.md` three-strikes) — the same finding surviving rounds N and N+2 is escalated, not patched a third time.
- **Replication audits** — a numeric claim downgraded to EXPLAINED in two consecutive audits without ever reaching PASS is surfaced prominently rather than left behind its recorded note.

In each case two strikes means the artifact is the wrong shape.

## Cross-references

- `${CLAUDE_PLUGIN_ROOT}/rules/output-discipline.md` — update-over-create; the sibling discipline for whole files.
- `${CLAUDE_PLUGIN_ROOT}/references/audit-pet-peeves.md` — the catalogue of drift classes this rule keeps out.
