# Model and Effort Routing

Every agent declares an explicit `model:` and `effort:`. None inherit.

## Why pinning, not cost

The usual argument for routing is cost. That is the secondary benefit here. The primary one is **protection**: with every agent on `model: inherit`, running a session on a cheaper model silently downgrades the methods-referee, the verifier, and the integrity gate along with it. The gates that decide whether a paper is sound would quietly get weaker because someone picked a different session model for an unrelated reason.

Pinning makes the judgment tier independent of what the session happens to be running. Cost discipline falls out of routing the genuinely mechanical work down, and is not the reason to do it.

## The routing principle

**Match the model to the cognitive demand of the task. Nothing else.**

A fixed ratio (70/20/10 or any other) is a description of some other fleet's workload, not a target. This fleet is judgment-dense: eight worker–critic pairs, two referees, an editor, an integrity gate, and a council that decides what enters a permanent knowledge base. Its distribution should look nothing like a fleet built mostly for mechanical document work, and forcing it to would be the wrong move.

Three rules, in priority order:

1. **Anything that exercises judgment gets the strongest model, whatever it costs.** Identification validity, proof correctness, referee dispositions, editorial decisions, claim verification, what enters the wiki. A false-positive PASS from a cheap judge costs a desk reject or a wrong published number — orders of magnitude more than the routing saving.
2. **Haiku only where the task is genuinely mechanical:** no interpretation, no trade-off, a checkable right answer. On this fleet that list is short, and it is fine for it to be short. Do not manufacture Haiku work to hit a ratio.
3. **Effort is a separate axis and the cheaper lever.** Reach for `effort` before changing tier. Opus 5's `high` is already deep; reserve `xhigh` for the hardest gates rather than setting it reflexively.

## The roster

| Model / effort | Agents | Why |
|---|---|---|
| **opus / xhigh** | `methods-referee`, `domain-referee`, `editor`, `verifier`, `claim-verifier`, `strategist-critic`, `theorist-critic` | The gate-keepers. Identification, proofs, citation triangulation, anachronism audit, desk-reject decisions. A wrong "looks fine" here is the expensive one. |
| **opus / high** | `theorist`, `strategist`, `writer-critic`, `coder-critic`, `orchestrator`, `wiki-promotion-council`, `engram-curriculum-architect`, `engram-assessor` | Genuine reasoning under constraints. `coder-critic` runs 16 check categories over numerical discipline. `wiki-promotion-council` decides what enters a permanent knowledge base *and* licenses auto-writes. `engram-assessor` grades blind. |
| **sonnet / high** | `writer`, `coder`, `data-engineer`, `librarian-critic`, `explorer-critic`, `storyteller-critic`, `code-reviewer`, `python-reviewer`, `wiki-librarian`, `engram-artifact-smith` | Generation with a stronger critic downstream, or review against an explicit rubric. |
| **sonnet / medium** | `librarian`, `explorer`, `storyteller`, `guide-writer` | Search, collection, and drafting where the paired critic carries the judgment. |
| **haiku / low** | *(none currently)* | Reserved for genuinely mechanical helpers — a citation reformatter, a bib-key normalizer. No current agent qualifies. |

## Anti-patterns

- **Never demote a gate-keeper to save cost.** `methods-referee`, `verifier`, `claim-verifier`, `editor`. One false PASS dominates the savings.
- **Never let a critic sit below its worker.** A critic weaker than what it reviews cannot catch what the worker missed. Where worker and critic would otherwise match, the critic is deliberately one tier above: `writer` (sonnet) → `writer-critic` (opus), `coder` (sonnet) → `coder-critic` (opus).
- **Avoid same-model self-pairing.** Identical worker and critic share blind spots, and a same-tier challenger launders correlated errors as independent confirmation.
- **Do not raise effort reflexively.** Tune effort before swapping tiers, and only where a gate is demonstrably missing findings.

## Where Fable fits

Nowhere in this fleet. Fable is built for long-horizon autonomous work; these agents are bounded, single-sitting tasks with a human auditing the disagreements they surface — not the shape it is priced for. Keep it as a per-session choice (`/model fable`) for the hardest interactive work: a multi-day refactor, or a deep synthesis you are steering by hand. Revisit if a genuinely long-horizon routine ever gets built.

## Changing the roster

A retier needs a reason recorded here, not just an edited frontmatter field. And verify rather than assume: run the same artifact through the agent before and after, and compare the findings count and severity distribution. **If a retiered critic surfaces fewer MAJORs on the same artifact, put it back.** Cost is the tiebreaker, never the criterion.

`scripts/check_plugin_integrity.py` enforces that every agent declares both fields.
