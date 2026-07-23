# Output Discipline — update over create

The default failure mode of an AI research assistant is **file proliferation**: a fresh literature review, critic report, or analysis note every time a step is re-run. research-os forbids this. Mirror the wiki's update-over-create philosophy (`wiki-integration.md`).

## Principle

**Improve the existing file. Create a new file only for a genuinely new question or literature.**

## Rules for creator agents

1. **Before writing, look for the existing artifact.** A lit review for the project's core question already lives at `01_literature/reviews/<question-slug>.md` — update it (add findings, revise synthesis, refresh the date), do not create `review-2.md` / `review-final.md` / `review-2026-07-22.md`.
2. **A new file is warranted only when the topic is materially distinct** — e.g. the paper draws on two separate literatures (labor supply *and* air-quality epidemiology) → two review files, each stable. Ask: "is this a new question, or the same question re-examined?" Same question → update.
3. **Critic reports are attached to their target, not accumulated.** A critic updates the single review/verdict for the artifact under review; it records the latest verdict + a short changelog, not a new timestamped report each pass.
4. **Analysis outputs overwrite deterministically.** Re-running a script replaces its figures/tables in `03_analysis/output/`; it does not version them by date. (Provenance/history lives in git + `passport.yaml`, not in filename proliferation.)
5. **Session/journal entries append, newest-first, within one file** (`00_admin/process/journal.md`, `00_admin/process/sessions/`), rather than one file per session.
6. **State is centralized in `passport.yaml`**, not scattered across per-step JSON.

## Changelog convention

When updating in place, prepend a one-line changelog entry at the top of the file's `## Changelog` section:

```
## Changelog
- 2026-07-22 — added Callaway & Sant'Anna (2021) to identification section; revised gap statement.
- 2026-07-15 — initial synthesis (6 sources).
```

## Enforcement

- The critics and `verifier` check for proliferation (duplicate-purpose files) and flag it.
- The dashboard surfaces "duplicate-purpose files detected" if the discipline is violated.
