# Lifecycle: Handoff Validation Protocol

Validation rules for agent dispatch and completion. The Orchestrator runs these checks before and after every agent invocation.

---

## PRE-Dispatch Validation

Before dispatching any agent, run:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/graph.py" why <node>
```

This evaluates the node's `REQUIRES` from `${CLAUDE_PLUGIN_ROOT}/graph/pipeline.json` — the
machine-readable twin of `permissions.md` — against the filesystem, `passport.yaml`, and the run
ledger, and prints exactly which predicate is unmet. It replaces re-deriving REQUIRES from prose
by hand: file-glob checks, section-heading checks, and score-gate lookups are all executed, not
re-interpreted, so the same REQUIRES clause is evaluated identically every time.

1. **`ready` or `ungated`** → dispatch is valid. `ungated` means the artifact exists but the
   critic hasn't scored it yet — dispatch the *critic*, not the worker.
2. **`blocked`** → do NOT dispatch. `why` names the missing predicate directly (a file glob with
   no match, a section heading absent from an existing file, or a score below its gate).
   Report: "Cannot dispatch [agent]: [predicate from `why`'s output]"
   Suggest: the prerequisite node's `skill` field.
3. **`stale`** → the node has already run, but a declared input changed since. This is
   **advisory, never blocking** — surface it, let the user decide whether to re-run.
4. **Fallback** (graph.py unavailable): read the agent's entry in `permissions.md` and check
   REQUIRES by hand — `Glob` for file paths, `passport.yaml` `pipeline.stages` for score gates,
   read the artifact for required section headings. This is the degraded path, not the default.

---

## POST-Completion Validation

After an agent completes, before advancing the pipeline:

1. **PRODUCES artifacts exist:**
   - For file paths: verify the file was created or updated
   - For directories: verify at least one file was created

2. **PRODUCES required sections present** (when specified):
   - Read the output artifact
   - Verify each required section heading exists
   - Missing sections: flag as incomplete, do not advance

3. **Critic score recorded:**
   - Verify the paired critic has produced a scored report
   - Write the score to `passport.yaml` `pipeline.stages`, note it in `00_admin/process/journal.md`, **and** run:
     ```bash
     python3 "${CLAUDE_PLUGIN_ROOT}/scripts/graph.py" record <node> --score <N>
     ```
     This appends to `00_admin/process/runs.jsonl` (append-only — never rewritten) and hashes the
     node's declared inputs, which is what makes staleness detection possible on the *next* PRE
     check. Skipping this step doesn't break routing (the graph falls back to `pipeline.stages`),
     but it does silently disable staleness for that node.

4. **If POST validation fails:**
   - Do NOT advance to the next phase
   - Report: "Agent [name] completed but output is incomplete: [specifics]"
   - Re-dispatch the agent with the specific gaps noted

---

## FAIL-FAST Principle

When validation fails:
- Report immediately with a clear, actionable message
- Never dispatch an agent with missing inputs and hope it works
- Never advance past an agent with missing outputs
- The Orchestrator includes the validation failure in its report to the user
