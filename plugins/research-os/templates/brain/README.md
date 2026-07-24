# _brain — the personal layer

`_brain/` is your human-owned space in the two-layer knowledge model. **You own it; Claude also writes here through specific skills.** The Claude-maintained thematic wikis (objective, canonicalized knowledge) live alongside it — see `../CLAUDE.md` and the plugin rule `wiki-integration.md` for the canonical two-layer policy.

## Folders

| Folder | What it holds | Written by |
|--------|---------------|------------|
| projects/ | one note per project — Orientation + Journal | `/checkpoint` |
| daily/ | one note per day — what changed + comms | `/daily-summary` |
| weekly/ | one note per week — review + plan + questions | `/weekly-planning` |
| thoughts/ | fleeting capture; graduate or delete | you |
| synthesis/ | personal & cross-theme synthesis | `/wiki-push` |
| learning/ | durable lessons + engram's spaced-repetition state | `/learn`, `/recall`, engram |
| `profile.md` | your standing context / "critical facts", loaded each session | `/wiki-setup`, `/wiki-pull` |
| `wikis-index.md` | index of the registered thematic wikis | `/add-vault` |
| `index.md` | Dataview catalog of this layer | generated |

## Note conventions

- **Orientation triage.** Project notes open with a kept-current Orientation block so anyone (you or Claude) can pick the project up cold. `profile.md` is the always-loaded standing-context doc — there is no separate `CRITICAL_FACTS.md`.
- **Confidence.** Learning notes carry a `confidence: stated|high|medium|speculation` level; synthesis tags claims inline.
- **Freshness — light.** Stamp genuinely aging facts `(as of YYYY-MM-DD, source)`. Most notes need no stamp — research facts are mostly timeless.
- **Capture → graduate.** `thoughts/` is the low-friction inbox; durable items graduate up (synthesis/learning) or down (a wiki via `/wiki-ingest`).
- **Lineage.** `supersedes:` records when one project or idea replaced another.

## Scheduled agents

Four routines keep the layer current (all offer/report — never silent high-stakes writes):
- **09:00 morning brief** — what's pending, next pipeline step, due reviews, today's calendar (read-only).
- **22:00 nightly consolidation** — commits the day and writes today's daily note; flags push candidates.
- **Fri 16:30 weekly review + planning** — drafts the weekly note and proposes next week's blocks.
- **Fri 15:00 weekly health audit** — runs the vault + `_brain` quality check and reports (read-only).

## Relationship to the wikis

Objective knowledge goes *down* to a thematic wiki via `/wiki-ingest`; personal or cross-theme insight goes *up* into `synthesis/`; theme-internal synthesis stays in the wiki's own `90_synthesis/`. Humans read the wikis but don't hand-edit them — curation flows through Claude.
