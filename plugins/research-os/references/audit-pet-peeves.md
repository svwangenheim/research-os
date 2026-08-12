# Audit pet peeves

A catalogue of drift classes that have actually occurred in this repository.
Every entry names the bug, where it was found, why the audit that was running
at the time missed it, and what catches it now.

The point is inheritance. An audit agent that starts from a blank prompt
rediscovers the same five defects and misses the sixth. An audit agent that
reads this file starts where the last one finished. When a new class of defect
turns up, add it here before fixing it.

Two habits produce most of the entries below:

- **Documentation asserting infrastructure that does not exist.** A file
  describes a hook, a check or a corpus read, and nothing implements it. This
  is worse than a missing feature, because it stops anyone from noticing the
  feature is missing.
- **Scope atrophy in the audit itself.** A checker or review prompt is written
  against the surface as it was, and the surface grows past it. The check keeps
  passing on a shrinking fraction of the tree.

---

## 1. A hook that reads an environment variable nobody sets

**Where.** `hooks/post-edit-lint.sh`.

**The bug.** It read `$CLAUDE_TOOL_ARG_FILE_PATH` instead of parsing the hook
JSON on stdin. That variable is legacy and unset, so `lint-scripts.sh` never
ran and INV-14 to INV-19 had no write-time enforcement at all.

**Why the audit missed it.** The hook was registered, syntactically valid, and
exited 0 every time. Nothing distinguishes "ran and found nothing" from "never
ran" unless you feed it a violating input on purpose.

**What catches it now.** The fail-open test in `hooks/README.md`: feed every
hook a crafted payload and assert output on a violating input, silence on a
clean one. Exit status alone proves nothing.

## 2. A hard dependency on a tool the platform does not ship

**Where.** `hooks/protect-files.sh`.

**The bug.** It shelled out to `jq`, which is not present by default on
Windows. On a fresh machine the file-protection hook failed silently.

**Why the audit missed it.** It was audited on a machine where `jq` happened to
be installed. Portability defects are invisible from inside the environment
that works.

**What catches it now.** Hooks and scripts are stdlib-only Python or POSIX
shell. Any new external dependency has to be argued for.

## 3. Documentation claiming a hook that was never shipped

**Where.** `skills/continuous-learning-v2/SKILL.md`.

**The bug.** It stated that `observe.sh` "is already registered in the plugin
`hooks/hooks.json`". No such file, no such entry.

**Why the audit missed it.** The claim was specific, plausible, and named a
real file path in a real directory. Reviewers check whether prose is coherent,
not whether the paths in it resolve.

**What catches it now.** Nothing fully automatic yet. Any claim of the form
"X is registered in Y" should be treated as a path assertion and checked. The
skill was deleted rather than repaired.

## 4. A rule asserting a protocol no implementation follows

**Where.** `rules/wiki-integration.md` said the verifier checks the wiki corpus
for citation coverage. `agents/verifier.md` contained no `wiki`, `vault` or
`_brain` string anywhere.

**Why the audit missed it.** Both files were individually correct. The defect
existed only in the relationship between them, and nothing was reading them as
a pair.

**What catches it now.** `check_plugin_integrity.py` check 4, rule-to-
implementation parity: when a rule names an agent or skill as following its
protocol, that file must mention the protocol's keywords. This is the check the
defect was used to design, and it fails on the pre-fix tree and passes on the
current one.

## 5. A rules directory loaded by nothing

**Where.** `~/.claude/rules/common/`, eleven files, roughly 48 KB.

**The bug.** Zero references from any plugin, skill or agent.
`additionalDirectories` grants read access, not loading, so `skill-router.md`
described itself as always-on and never ran once.

**Why the audit missed it.** The audit checked that the files were good. It did
not ask what loads them. "Is this correct" and "does this ever execute" are
different questions and the second is asked far less often.

**What catches it now.** Backlog item 3 holds the decision. For new material
the rule is: anything added to a rules directory names its loading mechanism in
the same commit.

## 6. Configuration accretion

**Where.** `~/.claude/settings.json`: roughly 75 `permissions.allow` entries
with escaped-regex artifacts, no `deny` list, and an `ECC_HOOK_PROFILE`
variable for a plugin that is disabled.

**Why the audit missed it.** Every individual entry was added for a real
reason. Nothing ever reviewed the set.

**What catches it now.** Nothing automatic. Settings are reviewed as a whole,
not entry by entry, and a permission added for a one-off gets removed when the
one-off is done.

## 7. A generated file regenerated too rarely

**Where.** `_map.md`, the map-of-content that `/wiki-pull` reads first.

**The bug.** Only `/wiki-maintain` regenerated it, so the first thing read at
the start of a research session was routinely the stalest file in the vault.

**Why the audit missed it.** The generator worked. Nobody checked how often it
was invoked relative to how often its inputs changed.

**What catches it now.** A staleness guard: any note newer than `_map.md`
triggers a regeneration before the read. For any generated artifact, ask what
writes it and how that compares to what changes its inputs.

## 8. An audit tool pointed at the wrong tree

**Where.** The retired `/skill-stocktake`.

**The bug.** It scanned `~/.claude/skills/` and `{cwd}/.claude/skills/`, which
means it never once examined the plugin's own skills. It was also disabled in
`skillOverrides`, so it had not run at all.

**Why the audit missed it.** Having an audit tool reads as having audit
coverage. Nobody checked its scope against the tree it was supposed to cover.

**What catches it now.** `check_plugin_integrity.py` and
`check_surface_sync.py` both take the plugin root as their scope and enumerate
from disk, so their coverage grows with the tree instead of drifting away from
it. Scope every audit tool against disk, never against a hardcoded list.

## 9. Renamed command, unrenamed references

**Where.** `vault/CLAUDE.md` and `_brain/wikis-index.md` still said
`/add-vault` after the skill was renamed to `add-thematic-wiki`.

**Why the audit missed it.** The rename touched the skill directory and the
skill body. The audit scope was the plugin tree; the stale references were in
the vault.

**What catches it now.** A rename is a repository-wide grep for the old name,
including the vault and the templates, and it is not done until the grep is
empty.

## 10. Residual upstream naming in ported files

**Where.** `styles/styles.css:1`, `styles/components.js:1`,
`scripts/generate_html_report.py:1783`.

**The bug.** Files ported from clo-author kept clo-author headers, so a
generated dashboard credited a project the user never installed.

**Why the audit missed it.** Line-one comments and `argparse` description
strings are not where anyone looks for content defects.

**What catches it now.** The headers were renamed, and `docs/PROVENANCE.md` is
now the sole record of where those three files came from. Attribution belongs
in one maintained place, not scattered through the files it describes.

## 11. The most-read tier is the thinnest on disk

**Where.** `90_synthesis/` holds 1 page in one wiki and 5 in another against
167 source summaries. `60_people_institutions/` is empty in both.

**The bug.** The highest tier in the `/wiki-pull` reading order has almost
nothing in it, so the retrieval order optimises for a layer that does not
exist.

**Why the audit missed it.** Quality checks ran per note. Every note that
existed was fine. Nothing compared the distribution across folders to the order
in which they are read.

**What catches it now.** Nothing automatic yet. When a retrieval order is
defined, check the population of each tier against its position in that order.
