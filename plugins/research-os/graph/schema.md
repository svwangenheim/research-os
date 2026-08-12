# The research-os graph — schema

`pipeline.json` is the machine-readable form of the pipeline. `rules/permissions.md` stays the
human-readable narrative of the same thing; `scripts/graph.py selftest` asserts the two never
drift.

**Nothing in this graph stores state.** A node's state is *computed* on every call from the
graph + the filesystem + `passport.yaml` + `00_admin/process/runs.jsonl`. Derived state cannot
desync from reality, which is the whole reason it is derived.

---

## Node kinds

| Kind | Blocks successors? | Example | Notes |
|---|---|---|---|
| `work` | yes, via its `gate` | `coder`, `writer` | produces project artifacts; paired with a critic |
| `gate` | yes, hard | `integrity` | pass/fail checkpoint; produces no artifact of its own |
| `router` | yes | `editor` | picks one outgoing edge from a decision (`routes`) |
| `ambient` | **never** | `wiki-pull` | session-scoped; `advises` edges only; surfaces as *optional* |

`ambient` is how the knowledge layer joins the graph without becoming a gate. Its nodes are
scoped to the session rather than the project, so "did you pull prior knowledge first?" is a
checkable, surfaceable recommendation — never a precondition.

## Node fields

| Field | Meaning |
|---|---|
| `id` | unique; matches the `permissions.md` heading and (for `work`) the agent filename |
| `kind` | one of the four above |
| `phase` | `permissions.md` PHASE; also where `score` predicates read from `passport.pipeline.stages` |
| `skill` | the exact command a user runs to execute this node |
| `agents` / `critic` | `permissions.md` agent + CRITIC |
| `parallel_group` | `permissions.md` PARALLEL_GROUP — nodes sharing one may run concurrently |
| `requires` | inbound predicates (below). All must hold for the node to be `ready`. |
| `produces` | outbound artifacts. Used for edge derivation and for staleness hashing. |
| `gate` | the critic score this node must reach to count as `done` |
| `when` | applicability condition; a definite failure makes the node `n/a` |
| `optional` | never reported as *required* work in the frontier |
| `escalates_to` | `permissions.md` ESCALATION_TARGET |
| `weight` | `permissions.md` QUALITY_WEIGHT (`null` = not separately scored) |
| `routes` | `router` only: `{on, to}` pairs |
| `advises` / `scope` / `ready_when` | `ambient` only |
| `blocking` / `terminal` | `integrity` blocks hard; `verifier` permits no re-entry |

## Predicates

Eight kinds. Between them they express every `REQUIRES` string currently in `permissions.md`.

```jsonc
{"file": "01_literature/reviews/*.md"}                    // >= 1 glob match
{"file": "…/strategy_memo.md", "sections": ["Estimand"]}  // + those headings present
{"score": {"node": "strategist", "min": 80}}              // that node's critic score
{"passport": "research.question"}                          // dotted path, non-empty
{"passport": "research.paper_type", "not_in": ["imrad"]}   // also: "in"
{"gate": "integrity"}                                      // that gate node has passed
{"overall": {"min": 95}}                                   // weighted aggregate (quality.md §1)
{"all_components": {"min": 80}}                            // every scored component
{"file_contains": {"file": "…", "pattern": "WIKI-PENDING"}} // literal substring present
{"wiki_pending_push": {"file": "wiki-links.md"}}            // real unchecked "To push back" item
{"any_of": [ … ]}   {"all_of": [ … ]}                      // boolean combinators
```

`wiki_pending_push` mirrors `hooks/session-journal.py`'s `unpushed_items` exactly — section-scoped
to `## To push back to the wiki / brain`, unchecked `- [ ]` only, skips the `<placeholder>`
template line — so the ambient `wiki-push` node and the Stop hook's nudge never disagree about
what counts as pending. A bare `{"file": "wiki-links.md"}` would be true the moment the file
exists, which is not the same claim.

`sections` is the heading check already specified in `rules/lifecycle.md` §PRE-2 — same
semantics, now executable rather than re-interpreted per dispatch.

`score` resolves in two steps: a run record for that node in `runs.jsonl` first, else
`passport.pipeline.stages[<node's phase>].score`. That fallback is what makes the graph work
on projects that predate it.

### Three-valued evaluation

Predicates return **true**, **false**, or **unknown**. Unknown is not false:

- `{"passport": "research.paper_type"}` on a passport that never set `paper_type` is *unknown*,
  not *failed*.
- A node whose `when` is unknown is offered as **optional** rather than hidden as `n/a`.

The system never silently drops work because a field was blank.

## Edges are derived, not declared

Three derivation rules, all exact — no fuzzy matching:

1. **`score` / `gate` predicates naming a node id** → edge from that node.
2. **`file` predicates whose glob string equals another node's `produces` glob string** → edge
   from that node. (Author the two globs identically where an edge exists; the selftest checks
   that every `file` requirement is produced by *some* node or is a declared project input.)
3. **`advises`** → dashed advisory edge from an `ambient` node.

Listing edges by hand would mean declaring each dependency twice, and two declarations drift.

## Writing to the ledger

`00_admin/process/runs.jsonl` is the only thing the graph layer writes, and it is append-only —
a receipt records what was true at run time and is never rewritten:

```bash
python3 scripts/graph.py record coder --score 86
```

This hashes the node's currently-resolved `file` requirements and appends one JSON line. It is
what makes `graph.py stale` possible: a later edit to a declared input changes its hash, and
`stale` diffs against the recorded one. Recording a score with no artifact on disk does **not**
make a node `done` — the artifact check comes first; a score with nothing to show for it stays
`ready` or `blocked`, honestly.

### Adopting an existing project

A project that predates the graph layer has no `runs.jsonl`. It still routes correctly —
`ctx.score()` falls back to `passport.pipeline.stages` — but staleness has nothing to compare
against, since no baseline hash was ever recorded.

```bash
python3 scripts/graph.py adopt --dry-run   # see what it would record
python3 scripts/graph.py adopt             # write it
```

`adopt` finds every node that is `done` or `stale` by the artifact-and-score check, has no
existing run record, and writes one with a `note` marking it as an adopted baseline rather than a
real run. It is idempotent (already-recorded nodes are skipped) and it never edits an existing
line — consistent with the ledger being append-only. It cannot tell whether an upstream file
changed *before* adoption; the baseline is "as of now," which is why this is an explicit,
reviewable command rather than something that runs automatically.

## Node states

| State | Meaning |
|---|---|
| `done` | `produces` exist **and** the `gate` score is met |
| `ready` | every `requires` predicate holds; not yet done |
| `blocked` | at least one `requires` predicate fails — `graph.py why <id>` names which |
| `stale` | done, but a declared input's content hash changed since the recorded run (advisory) |
| `n/a` | `when` definitively excludes it for this paper type |

## Adding a node

1. Add the entry to `rules/permissions.md` (narrative, for humans and agents).
2. Add the node here with the same PHASE / CRITIC / PARALLEL_GROUP / QUALITY_WEIGHT.
3. Run `python3 scripts/graph.py selftest` — it fails if the two disagree.

No other file changes. The router, `/research-os-help`, and the dashboard all read this file.
