# Testing guide

A walkthrough for exercising every capability area at least once. Each
section says what to run and what "it worked" actually looks like —
concrete files/entries to check, not just "no errors." Linked from the root
[README.md](../../../README.md).

## 0. Start here — `/research-os-help`

This is the fundamental guide-through capability, so it's worth testing
first, before anything else on this page. Try it a few different ways:

- **`/research-os-help`** with no arguments, from inside a real project.
  **Working looks like:** it reads that project's `passport.yaml`, names
  exactly where you are in the pipeline, and gives you one concrete next
  step (not a menu of everything).
- **`/research-os-help eli5`** — the newcomer mode. **Working looks like:** a
  plain-language walkthrough of the whole system a first-time user could
  follow without already knowing the terminology.
- **`/research-os-help list`** (or "what can you do") — **Working looks
  like:** it can name every skill/agent group from the README, not just the
  pipeline ones.
- Ask it something free-form, e.g. "why isn't Dataview working" or "what's
  next" — **Working looks like:** it answers directly, and — if you
  confirm — actually runs the next step rather than just describing it.

## 1. Wiki setup — three scenarios

research-os separates *structure* (`/wiki-setup`, `/add-vault` — folders,
registry, config) from *content quality* (`/wiki-maintain` — summaries,
dedup, links). Test the structural side first.

**Scenario A — from scratch, on a machine with nothing set up.** Delete or
rename `~/.claude/vaults.json` first if you want a true clean-slate test (or
just try this on a machine that's never run it). Run `/wiki-setup`. Expect:
a direct opening question ("do you already have a wiki, or starting fresh?"),
then — since nothing exists — the **fresh-bootstrap branch**: the full
folder tree, `_templates/`, root docs (`CLAUDE.md`/`README.md`/`index.md`/
`log.md`), `.obsidian` config, `~/.claude/vaults.json`, and
`~/.claude/settings.json`/`VAULT_PATH` wiring created in one pass, followed
by the profile interview. **Working looks like:** `~/.claude/vaults.json`
exists with a `root` and `brain` key; the vault folder has all the root docs;
`_brain/profile.md` has real content, not a placeholder.

**Scenario B — improving an existing (possibly drifted) setup.** Run
`/wiki-setup` again on a real setup — optionally rename a folder first
(e.g. `60_people_institutions` → `60_people_instructions`) to manufacture
drift. Expect the **existing/possibly-drifted branch**: one gap surfaced and
confirmed at a time, never a silent bulk fix. **Working looks like:** the
drift you introduced gets named specifically and only fixed after you say
yes; nothing else in the vault changes.

**Scenario C — adding just one new vault.** Run `/add-vault` and try both new
paths:
- *Create empty:* answer "create a brand-new one," give it a throwaway theme
  name. **Working looks like:** 8 numbered folders + generic READMEs at
  `<root>/<slug>/`, a new entry in `vaults.json`, a new row in
  `_brain/wikis-index.md`.
- *Adopt existing:* point it at some other folder with a few files in it
  (doesn't need to match the standard layout). **Working looks like:** it
  reports what's missing before touching anything, only adds the missing
  numbered folders (existing files untouched), and asks before deciding
  whether to move it under the vault root or register it in place.

## 2. Second-brain layer

- **Profile interview** — part of `/wiki-setup` Step 3 (or re-triggered any
  time your profile looks stale). It summarizes what it already knows first,
  then asks only about gaps. **Working looks like:** `_brain/profile.md` gets
  updated, not overwritten from scratch.
- **`/checkpoint`** — run it after any real work. **Working looks like:** a
  new or updated `_brain/projects/<slug>.md`, an appended `passport.yaml`
  `sessions:` entry, and the project dashboard refreshed.
- **`/daily-summary`** — run once at the end of a session. **Working looks
  like:** a new `_brain/daily/<YYYY-MM-DD>.md`, and today's work committed
  locally in each touched project (check `git log` in that project — no
  push should happen).
- **`/weekly-planning`** — run once at the end of a week. **Working looks
  like:** a new `_brain/weekly/<Monday>.md` with last week's check-off and
  this week's goals; calendar blocks only get created if you explicitly
  authorized Microsoft 365 and confirmed them.

## 3. Research project capabilities

- **`/create-project "a throwaway test question"`** — **Working looks
  like:** a full numbered project folder tree, `passport.yaml`, `CLAUDE.md`,
  `wiki-links.md`, and a dashboard seed, plus a `main_wiki` assignment (or a
  question about which wiki this belongs to).
- **`/discover interview`** — the Socratic dialogue mode. A good run asks one
  focused question at a time, doesn't rush to a research question before
  probing the "why," and by the end has written the spec into
  `passport.yaml`'s discovery section. Try `/discover lit` and `/discover
  data` too — separate literature-search and dataset-search modes.
- **One pass through the pipeline** — `/strategize` → `/analyze` → `/write`
  → `/peer-review`, on deliberately trivial content (a toy dataset, a
  one-paragraph "finding"). You're not testing whether the science is good —
  you're checking that each phase's worker+critic pair actually fires, that
  `passport.yaml`'s `pipeline.current_stage` advances, and that
  `/dashboard` picks up the new sections afterward.

## 4. Admin / scheduled tasks

Only two of the four routines run unattended in the cloud; the other two
are manual/local. See [scheduled-agents.md](scheduled-agents.md) for why.

- **Manual dry-run first, all four.** Paste each routine's exact prompt text
  from `scheduled-agents.md` directly into a session, one at a time, and
  confirm it behaves as labeled:
  - Morning brief → genuinely makes **no writes** (check `git status` after —
    should be clean).
  - Weekly vault-health audit → reports frontmatter/dedup/broken-link/staleness
    findings, makes **no writes**.
  - Nightly consolidation → commits locally in each touched project, never
    pushes, and only **flags** unpushed wiki knowledge rather than acting on
    it.
  - Weekly review + planning → **drafts** `_brain/weekly/<Monday>.md` and
    proposes calendar blocks but creates nothing without your confirmation.
- **Then verify the cloud registration for the two cloud-feasible routines**
  — run `/schedule` (list mode) and confirm morning brief and weekly
  vault-health audit appear with the correct UTC cron expressions from
  `scheduled-agents.md`, pointed at the vault's private GitHub repo.
- **Nightly consolidation and weekly planning have no cloud registration to
  check** — by design, for now. Run them by hand, or set up `/loop` on a
  machine that stays on if you want them automatic too.

## 5. Learning (engram)

- **`/learn`** on some small concept (real or invented) you don't already
  know well. **Working looks like:** a first-principles breakdown, questions
  that make *you* produce the answer rather than just being told it, and a
  new entry in engram's state under `_brain/learning/` (check `ENGRAM_HOME`
  is actually pointed there, per the plugin README's setup note — otherwise
  state lands in `~/.claude/learning/` instead).
- **`/recall`** once something is due. If nothing's due yet same-day, that's
  expected — FSRS schedules reviews days out by design; don't force a fake
  due date just to test it, this is a case where seeing an empty due-queue
  the first time is itself the "it worked" signal.
- **`/coach`** (dashboard mode) — **Working looks like:** retention stats and
  a self-contained HTML dashboard reflecting whatever you just learned.

## 6. What "it's working" looks like — quick reference

| Area | Concrete signal |
|---|---|
| `/research-os-help` | Names your exact pipeline stage unprompted; ELI5 mode reads as newcomer-friendly |
| Wiki setup | `~/.claude/vaults.json` has `root`, `brain`, and every expected wiki key |
| Add-vault | New wiki folder + `vaults.json` entry + `wikis-index.md` row all appear together |
| Second brain | `_brain/profile.md`, `_brain/projects/<slug>.md`, `_brain/daily/*.md` exist and read like *your* notes |
| Project pipeline | `passport.yaml`'s `pipeline.current_stage` advances after each phase |
| Scheduled tasks | `/schedule` list shows the 2 cloud routines with correct UTC crons; the 2 manual ones behave correctly when dry-run by hand |
| Learning | A due-review queue that behaves like FSRS scheduling, not immediate every time |
