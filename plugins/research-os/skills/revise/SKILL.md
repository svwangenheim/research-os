---
name: revise
description: R&R cycle - classify referee comments, route to agents, draft the response letter, and audit it before it goes back. Revision phase; writes to 04_paper/revisions/.
argument-hint: "[referee-report file path(s)] [paper path (optional)] Options: rebuttal-audit [response-letter path]"
allowed-tools: Read,Grep,Glob,Write,Edit,Task
---

# Revise

Structure point-by-point referee responses with classification, agent routing per the revision protocol, diplomatic drafting, and (before the letter goes out) a rebuttal audit against the referee's own words.

**Input:** `$ARGUMENTS` -- path to referee report file(s), optionally followed by paper path; or `rebuttal-audit [response-letter path]`.

State lives in **`passport.yaml`** (schema: `${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml`). Paths follow `${CLAUDE_PLUGIN_ROOT}/rules/folder-map.md` and the revision protocol in `${CLAUDE_PLUGIN_ROOT}/rules/revision.md`: referee reports are read from `04_paper/reviews/` (`referee_domain.md`, `referee_methods.md`, `editorial_decision.md`); the tracker and response letter are written to `04_paper/revisions/`; revised sections update `04_paper/academic_paper/sections/` in place. Outputs obey `${CLAUDE_PLUGIN_ROOT}/rules/output-discipline.md`: **update the tracker and response letter in place with a `## Changelog`; do not proliferate `_r2.md` / `_final.md` copies -- provenance lives in git.** Re-scored components update `passport.yaml` `pipeline.stages`. Before the revised paper returns to `/peer-review` or `/submit`, the ARS integrity gate (`${CLAUDE_PLUGIN_ROOT}/rules/quality.md` Section 3) must re-pass -- `/revise` does not clear that gate itself.

---

## Workflow

### Step 1: Parse Inputs
1. Read referee report(s) -- default to `04_paper/reviews/referee_domain.md` and `04_paper/reviews/referee_methods.md` if `$ARGUMENTS` doesn't specify a path
2. Read the paper (`04_paper/academic_paper/main.tex` or specified path)
3. Read the revision protocol: `${CLAUDE_PLUGIN_ROOT}/rules/revision.md`
4. Read existing scripts in `03_analysis/scripts/` to know what analyses already exist
5. For comments about the literature -- a missing citation, a mispositioning, a referee's "see X (2019)" -- resolve each affected bibkey to its `wiki_path` in `passport.yaml` `literature_corpus` and read that `<main_wiki>/20_summaries/` note before drafting the response. The summary carries what the paper actually found and how, so the reply answers the referee from the source rather than from the draft's paraphrase of it. Resolve the thematic wiki via the standard ladder in `${CLAUDE_PLUGIN_ROOT}/rules/wiki-integration.md` (`--wiki` > `passport.yaml` `meta.main_wiki` > `.research-os-wiki` > the registry's only wiki), reading `~/.claude/vaults.json` for the path. **Read only** -- `/revise` never writes to the wiki. If no wiki is resolvable, skip this step silently.

### Step 2: Classify Every Comment

| Class | Routing | Action |
|-------|---------|--------|
| **NEW ANALYSIS** | -> Coder agent | Flag for user, create analysis task |
| **CLARIFICATION** | -> Writer agent | Draft rewritten section |
| **REWRITE** | -> Writer agent | Draft structural revision |
| **DISAGREE** | -> User (mandatory) | Draft diplomatic pushback, flag for review |
| **MINOR** | -> Writer agent | Draft fix directly |

### Step 3: Build Tracking Document
Save to `04_paper/revisions/referee_response_tracker.md` (`${CLAUDE_PLUGIN_ROOT}/skills/revise/templates/response-tracker.md`), updating in place:
- Summary counts per referee
- Action items by priority (HIGH: new analysis, MEDIUM: clarification, FLAGGED: disagreements, LOW: minor)

### Step 4: Dispatch Agents
- CLARIFICATION/REWRITE -> dispatch Writer with specific instructions; Writer updates the section file in place (`04_paper/academic_paper/sections/`)
- NEW ANALYSIS -> flag for user approval **before** dispatching Coder -- never start new estimation on a referee's say-so alone
- DISAGREE -> draft diplomatic response using `${CLAUDE_PLUGIN_ROOT}/skills/revise/templates/diplomatic-disagreement.md`, flag prominently for user

### Step 5: Draft Response Letter
Generate the LaTeX response letter (`${CLAUDE_PLUGIN_ROOT}/skills/revise/templates/response-letter.tex`) with:
- Summary of major changes
- Point-by-point responses with exact referee quotes
- Color-coded responses
- Page/section references for each change

### Step 6: Diplomatic Disagreement Protocol
When DISAGREE: open with acknowledgment, provide evidence, offer partial concession, NEVER say "the referee is wrong." FLAG for user review before the letter is finalized -- Claude never autonomously pushes back on a referee.

### Step 7: Save Outputs
1. Tracker: `04_paper/revisions/referee_response_tracker.md` (update in place)
2. Response letter: `04_paper/revisions/response_letter_[journal].tex` (update in place across rounds -- the git history is the version record, not the filename)
3. Revised sections: `04_paper/academic_paper/sections/` (for CLARIFICATION/REWRITE items, update in place)

### Step 8: Re-check Before Returning to Review
Once all HIGH and MEDIUM items are resolved and DISAGREE items are user-confirmed, re-run the relevant critics (writer-critic and/or coder-critic on changed material) and remind the user that `/peer-review --peer --r2` (or `--r3`) re-runs the ARS integrity gate before the referees see the revision -- `/revise` itself does not clear that gate.

---

## `revise rebuttal-audit [response-letter path]` -- QA the Response Before It's Sent

Runs a self-contained audit of the drafted response letter against the referee comments it claims to address -- catching gaps and tone problems before the paper goes back to the editor. This is a **check on the user's own draft**, distinct from Step 5-7 (which draft the letter in the first place); run it whenever a response letter already exists (drafted by `/revise`, or by the user directly) and needs a pass before submission.

**Input:** path to the response letter (defaults to `04_paper/revisions/response_letter_[journal].tex` if present); referee reports from `04_paper/reviews/`.

**Agent:** direct audit (no new agent dispatch -- this is a structured comparison, not a fresh review)

Workflow:
1. **Extract every referee comment** from `04_paper/reviews/referee_domain.md` and `referee_methods.md` (major + minor issues), and every classified item from `04_paper/revisions/referee_response_tracker.md`.
2. **Cross-check coverage.** For each comment: does the response letter address it explicitly, with a page/section reference? Flag:
   - **UNADDRESSED** -- a referee comment with no corresponding response in the letter
   - **VAGUE** -- a response that doesn't map to a specific change ("we revised the text" with no location) -- per `gotchas.md`, vague responses get rejected
   - **MISMATCHED** -- a response that claims a change was made but the cited section doesn't contain it
3. **Tonal check** against `${CLAUDE_PLUGIN_ROOT}/skills/revise/templates/diplomatic-disagreement.md`: flag any instance of the banned phrasings ("the referee is wrong," bare "we disagree," "this is well known," "we already addressed this" without a pointer) and confirm every DISAGREE item follows the acknowledge -> explain -> evidence/partial-concession structure.
4. **Completeness check.** Every item in the tracker with `Status: Complete` has a matching letter entry; every NEW ANALYSIS item cites the specific new table/figure/script produced.
5. **Report.** Produce a pass/fail list (not a numeric score -- this is a QA checklist, not a critic rubric):

```markdown
## Rebuttal Audit -- [journal] R&R round [N]
**Response letter:** [path]
**Referee comments checked:** [N]

### Unaddressed
- [Referee X, comment Y]: [quote] -- no matching response found

### Vague / Unmapped
- [Referee X, comment Y]: response doesn't cite a specific page/section

### Mismatched
- [Referee X, comment Y]: claims change at [section] -- not found there

### Tonal Flags
- [quote from letter] -- reads as [dismissive/defensive/etc.] -- suggested rephrase per diplomatic-disagreement.md

### Clean
- [N] comments fully addressed with clear evidence and location

**Verdict:** [READY TO SEND / FIX BEFORE SENDING]
```

Save to `04_paper/revisions/rebuttal_audit.md`, updating in place with a Changelog entry per round. This audit is advisory but should be run before every submission of a response letter -- treat an "UNADDRESSED" or "MISMATCHED" flag as blocking until resolved.

---

## Bundled Resources

| Resource | Path | When |
|----------|------|------|
| Response tracker | `${CLAUDE_PLUGIN_ROOT}/skills/revise/templates/response-tracker.md` | Step 3 -- tracking document |
| Response letter | `${CLAUDE_PLUGIN_ROOT}/skills/revise/templates/response-letter.tex` | Step 5 -- LaTeX boilerplate |
| Diplomatic disagreement | `${CLAUDE_PLUGIN_ROOT}/skills/revise/templates/diplomatic-disagreement.md` | Step 6 and `rebuttal-audit` -- DISAGREE phrasing and its tonal check |
| Gotchas | `${CLAUDE_PLUGIN_ROOT}/skills/revise/gotchas.md` | Always -- known failure points |

---

## Principles
- **The response letter is the user's voice.** Match their tone, not Claude's.
- **Never fabricate results.** Mark NEW ANALYSIS items as TBD until the Coder actually produces them.
- **Flag all DISAGREE items.** These need human judgment -- Claude never autonomously pushes back on a referee.
- **Track everything.** Every comment appears in both the tracker and the response letter.
- **Audit your own draft.** `rebuttal-audit` treats the response letter with the same skepticism a referee would -- unaddressed or vague responses get flagged before the editor sees them, not after.
- **The gate isn't yours to clear.** `/revise` drafts and tracks; the ARS integrity gate re-run and re-review happen in `/peer-review`.
