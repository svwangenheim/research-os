# Logging

State is centralized in **`passport.yaml`** (schema: `${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml`). The retired clo-author artifacts (`SESSION_REPORT.md`, `MEMORY.md`, `pipeline-state.json`) all fold into it: session boundaries → `sessions`; pipeline/phase/scores → `pipeline.stages`; corpus → `literature_corpus`; claims → `claim_manifest`; integrity results → `integrity`. Human-readable narrative lives in `00_admin/process/`.

## Session Boundaries

Appended by `/checkpoint` at end of session or before context compression.
- **`passport.yaml` `sessions:`** — one entry per session, appended newest-last: `date`, `summary` (what was done), `next` (planned next step).
- **`00_admin/process/sessions/`** — optional longer per-session handoff notes when a `sessions:` line is not enough.

Session entry (in `passport.yaml`):
```yaml
sessions:
  - date: "2026-07-22"
    summary: "Drafted results section; coder-critic scored 86."
    next: "Address writer-critic hedging flags in discussion."
```

**Rules:** Append only. Include file paths and commit hashes in the `00_admin/process/sessions/` note when available.

## Research Journal

Append to `00_admin/process/journal.md` (newest-first) whenever an agent completes work — writing code, drafting a section, producing a review, making an editorial decision, or transitioning between phases.

**Rules:** Append only. One entry per agent invocation. Include phase transitions and editorial decisions.

**Entry format:**
```markdown
### YYYY-MM-DD HH:MM — [Agent Name]
**Phase:** [Discovery/Strategy/Analysis/Writing/Review/Revision/Submission]
**Node:** [graph node id, e.g. `coder` — see graph/pipeline.json]
**Run:** [run_id from `graph.py record`, e.g. `r_531fcefabd5c` — omit if the node has no graph entry]
**Target:** [file or topic]
**Score:** [XX/100 or PASS/FAIL or N/A]
**Verdict:** [one line — key finding or decision]
**Report:** [path to full report]
```

`Node` and `Run` are what let a journal entry be traced back to the exact evidence `graph.py stale`
diffs against — the run ledger (`00_admin/process/runs.jsonl`) is append-only, so a run_id always
resolves to one immutable record. `graph.py record <node> --score N` prints a ready-to-paste
`journal line:` for this purpose; use it rather than inventing the run_id by hand.

**Why it exists:** The journal is the *narrative* — "what happened and why." Scores and phase state are read from `passport.yaml` `pipeline.stages`; the journal explains the reasoning behind them. They are complementary, not redundant: the passport answers "where are we and what's next," the journal answers "how did we get here."

Agent outputs (reports, scripts, memos, decisions) are saved to their folder-map homes by the skills that produce them: reviews to `04_paper/reviews/`, decisions to `00_admin/process/decisions/`, results to `03_analysis/output/`.

## Pipeline State

Structured pipeline state lives in `passport.yaml` `pipeline` (not a separate JSON file).

**Triggers:**
- Initialized by `/create-project`
- Updated after every agent completion, critic score, or phase transition
- Read as the first action in session recovery (see `workflow.md`)

**Execution traces:**
After pipeline completion, the orchestrator may write an execution trace to `00_admin/process/traces/` (a sub-folder of the process log). A trace is derived from the `pipeline` history in `passport.yaml`.

### Trace Analysis

After pipeline completion, read the execution trace and the last 5 traces (if available in `00_admin/process/traces/`) to identify recurring patterns.

Analysis covers:
- Agents with first-pass >= 90 (HIGH-PERF)
- Agents that hit 3 strikes (FRICTION)
- Escalations to user (USER ESCALATION)
- Agents whose scores improved most between rounds (learning curve)

Save analysis to: `00_admin/process/traces/analysis_{date}.md`.

The orchestrator uses this analysis for the Learning Promotion loop (see `meta-governance.md`).

---

## 4. Project Dashboard

**Managed by the `/dashboard` skill.** See `${CLAUDE_PLUGIN_ROOT}/skills/dashboard/SKILL.md` for the full specification and `html-dashboard.md` for the structure and design system.

The dashboard is `project_dashboard.html` (project root) — a single unified HTML page with all project information. Generated and refreshed by `/dashboard refresh`. Changelog entries appended by `/dashboard add-changelog`.
