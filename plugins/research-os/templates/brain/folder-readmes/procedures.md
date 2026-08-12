# Procedures

One note per recurring process — **how you actually do a thing**, step by step, and **executable**. The layer that holds working knowledge, as distinct from `projects/` (what is being worked on) and the thematic wikis (what is known).

Each note (`note_type: procedure`, template `procedure_template.md`) holds a trigger, an optional `schedule:`, numbered steps tagged by who executes them (`[ai]` / `[human]` / `[external]` / `[veto]`), the decision points that are still judgment calls, known failure modes, a machine-specific `Config` block, and an appended run log.

## This is a spec that runs, not documentation about one

`/automate run <name>` walks the Steps: it executes every `[ai]` step itself, stops and asks at every `[human]` step, and refuses every `[veto]` step outright — identically whether you invoked it or a schedule did. **There is no promotion gate.** A procedure is runnable the moment it validates against the template. (An earlier version of this layer had a five-gate promotion mechanism requiring ≥3 recorded runs before anything could execute — that mechanism could never actually be reached, and it isn't how the source guide this layer is based on works. See `docs/13-the-automation-layer.md` for the full account.)

## Procedure vs. skill — still a real distinction, just not a gate

> A **procedure** is *this researcher's own* recurring task, judgment calls and all — a scenario run, a specific committee's meeting prep, a personal coursework habit. It lives here, in the vault, and never ships.
>
> A **skill** is generalizable research machinery any researcher could run — `/strategize`, `/write`, `/peer-review`. It lives in `plugins/research-os/skills/` and ships to everyone.

**Procedures may call skills; skills never call procedures.** A DZ modelling procedure can compose a BMAD workflow (`mmm-qa-verify`) or a research-os skill (`/diagnose`) as one of its `[ai]` steps — recorded in `calls:` — while adding what those don't do: commit, checkpoint, project-note update, wiki push. The composition, not a promotion path, is what turns a personal task into leverage.

## Who writes these

`/workflow-audit` identifies and scores candidates. `/automate new` authors a procedure in dialogue when there's time for one; when there isn't, a procedure is drafted from evidence (mined session history, git logs, the audit) and marked `draft: true`, with every uncertain step tagged `[human]` — the first real `/automate run` is where it gets corrected. Either way, nothing here is scraped verbatim from a session transcript: the steps record what you *mean* to do, not a replay of one session's detours.

The run log is appended by `/automate run` itself on every execution — actor mix, which `[human]` steps it stopped at, deviations from what the note describes. **Never hand-edit inside the `@generated` markers.** A procedure whose log keeps recording the same deviation has steps that are wrong; fix the note.

## Vetoes are permanent

A step tagged `[veto]` is refused by the runner, always — the reference case is AD-5: Claude must never read, process, log, or cache real SOEP microdata in any form, and R2 generalizes this to any unfamiliar data file in any project (`hooks/data-consent.py`). A veto carries a `veto_reason` and survives every re-scoring; nothing about a schedule or a `calls:` composition can bypass it.
