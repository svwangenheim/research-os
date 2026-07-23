# Revision Protocol — R&R Cycle

**When referee reports arrive, `/revise` classifies each comment and routes it to the right agent.**

Inputs (real referee reports) and outputs live in `04_paper/revisions/`: the R&R tracker (which comments are resolved / pending) and the response letter. Any new estimation or draft changes land in their normal folder-map homes (`03_analysis/`, `04_paper/academic_paper/`), and re-scored components update `passport.yaml` `pipeline.stages`.

## Comment Classification

| Classification | What It Means | Routed To |
|---------------|---------------|-----------|
| **NEW ANALYSIS** | Requires new estimation or data work | Coder → coder-critic |
| **CLARIFICATION** | Text revision sufficient | Writer → writer-critic |
| **DISAGREE** | Diplomatic pushback needed | Flagged for User review |
| **MINOR** | Typos, formatting | Writer |

## The R&R Flow

```
Referee reports arrive (real, not simulated)
        │
        ▼
   /revise classifies each comment
        │
        ├── NEW ANALYSIS → Coder → coder-critic → Writer updates
        ├── CLARIFICATION → Writer → writer-critic
        ├── DISAGREE → User decides → diplomatic response drafted
        └── MINOR → Writer
        │
        ▼
   Revised paper → writer-critic → Orchestrator re-checks (+ integrity gate)
        │
        ▼
   Response letter produced → 04_paper/revisions/
```

## Rules

- This uses the same agents but in a targeted way — not a full pipeline restart
- Each comment gets its own routing — a single referee report may trigger multiple agent pairs
- The response letter maps each referee comment to the specific change made; it is written to `04_paper/revisions/`
- DISAGREE items are always flagged for user review — Claude never autonomously pushes back on referees
- The Orchestrator tracks which comments are resolved and which are pending in the R&R tracker (`04_paper/revisions/`)
- Before the revised paper returns to review/submission, the ARS integrity gate must re-pass (see `quality.md`)
