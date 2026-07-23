# Agents: Pairs, Separation of Powers, and Escalation

---

## 1. Adversarial Pairing

**Every worker agent has a paired critic. The Orchestrator never dispatches a creator without scheduling its critic.**

### Worker-Critic Pairs

| Worker (Creator) | Critic (Reviewer) | What's Reviewed |
|-----------------|-------------------|-----------------|
| librarian | librarian-critic | Literature coverage, gaps, recency |
| explorer | explorer-critic | Data feasibility, quality, identification fit |
| data-engineer | coder-critic | Data pipeline quality, reproducibility, transformation correctness |
| strategist | strategist-critic | Identification validity, assumptions, robustness |
| theorist | theorist-critic | Proof validity, assumption minimality, notation, citations |
| coder | coder-critic | Code quality, reproducibility, code-strategy alignment |
| writer | writer-critic | Manuscript polish, LaTeX quality, hedging |
| storyteller | storyteller-critic | Talk structure, audience calibration, visual quality |

### Peer Review (Special Case)

Peer Review uses a different structure — the Orchestrator dispatches two independent referees:

1. Orchestrator assigns the paper to domain-referee and methods-referee (blind, independent)
2. Both referees produce scored reports
3. Orchestrator synthesizes a decision: Accept / Minor Revisions / Major Revisions / Reject

`/peer-review` may only run once the ARS integrity gate has passed (see `quality.md`).

### Enforcement

- The Orchestrator checks: if a creator artifact exists without a critic score (in `passport.yaml` `pipeline.stages`), it is **not approved**
- No artifact advances to the next phase without its critic's score >= 80
- Critics produce scores; creators produce artifacts — never the reverse

---

## 2. Separation of Powers

**Critics never create. Creators never self-score.**

### Critics Never Create

A critic's job is to evaluate, not to produce artifacts. If a critic produces code, text, or data during its review, something is wrong.

**What critics DO:**
- Score artifacts against a rubric
- List issues with severity and deductions
- Suggest fixes (as recommendations, not implementations)

**What critics DON'T DO:**
- Write code to fix the issues they found
- Rewrite paper sections
- Produce alternative implementations

**Why:** A critic who fixes their own findings has incentive to find only fixable issues. Separation keeps criticism honest. (This principle also governs the integrity gate in `quality.md`: the referees and verifier flag; the writer and coder remediate.)

### Creators Can't Self-Score

A creator cannot evaluate the quality of its own work. The score always comes from the paired critic.

| Agent | Creates | Scored By |
|-------|---------|-----------|
| librarian | Annotated bibliography (`01_literature/reviews/`) | librarian-critic |
| explorer | Data assessment (`02_data/data-sources.md`) | explorer-critic |
| data-engineer | Data pipeline and cleaned datasets (`02_data/cleaned/`) | coder-critic |
| strategist | Strategy memo (`03_analysis/strategy/`) | strategist-critic |
| theorist | Assumptions, theorems, proofs (theory section) | theorist-critic |
| coder | R/Python/Julia scripts (`03_analysis/scripts/`) | coder-critic |
| writer | Paper manuscript (`04_paper/<output>/`) | writer-critic |
| storyteller | Beamer talk (`05_outreach/talks/`) | storyteller-critic |

### Enforcement

The Orchestrator flags violations:
- If a critic invocation produces a file in `03_analysis/scripts/`, `04_paper/<output>/`, or `05_outreach/talks/` → flag
- If a creator reports its own score → discard, dispatch critic

---

## 3. Three Strikes Escalation

**If a worker-critic pair fails to converge after 3 rounds, the Orchestrator escalates.**

### The Protocol

```
Round 1: Critic reviews → Worker fixes
Round 2: Critic reviews → Worker fixes
Round 3: Critic reviews → Worker fixes
         Still failing?
              ↓
         ESCALATION
```

### Escalation Routing

Escalation targets are declared in each agent's entry in `permissions.md` (ESCALATION_TARGET field). The Orchestrator reads this field when a pair hits 3 strikes.

### Rules

- **Max 3 rounds per pair per invocation** — no infinite loops
- **Escalation is logged** in `00_admin/process/journal.md` with the strike count (the round count also lives in `passport.yaml` `pipeline.stages`)
- **User escalation requires a clear question** — not "they disagree," but "strategist-critic requires X, which contradicts Y. Which takes priority?"
- **Post-escalation:** The worker starts fresh from the escalation target's decision, not from its previous attempt
