---
name: connect
description: Cross-theme bridge-finder. Surfaces non-obvious connections between research themes and the personal brain. Read-only. Use for "what connects X and Y" or "find non-obvious links".
argument-hint: "[themeA] [themeB]  — or no args to scan across all registered wikis"
allowed-tools: Read, Glob, Grep
---

# Connect

Find the connections your knowledge base implies but has not yet drawn. This
is a **global**, **read-only** skill — it proposes, it never writes.

## When to use

The user wants to discover latent cross-theme structure: "is there anything
linking cognitive-load and innovation-policy?", "what would transfer from my
labor work to this?", or a periodic sweep for emergent connections. This is
the cross-*theme* complement to `/wiki-pull` (which retrieves within a task's
theme) and `/wiki-push` (which files new knowledge). `/emerge` (bottom-up
pattern surfacing within one corpus) is a separate, future skill.

## Resolve the layers

Follow the same registry resolution as `/wiki-pull`:
1. Read `~/.claude/vaults.json` (theme → path map, plus `brain.path`).
2. If absent, fall back to `~/.claude/VAULT_PATH` (one flat vault).
3. If neither exists: say so plainly and stop — there is nothing to connect.

**Pick the scope:**
- Two theme arguments → connect those two wikis.
- One argument → connect that theme against every other registered wiki.
- No arguments → scan across all registered wikis (and `_brain/synthesis`),
  reporting the strongest few cross-theme bridges.

## Workflow

### Step 1: Map each side cheaply
For each theme in scope, read its `_map.md` first (the generated catalog);
fall back to listing `30_concepts/`, `40_methods/`, `50_datasets/`, and
`90_synthesis/` if the map is absent. Also skim `_brain/synthesis/` for
cross-theme notes the user already started. Build a compact picture of each
side's concepts, methods, datasets, and open questions — do not read every
note in full.

### Step 2: Trace what is already linked
Note existing cross-theme wikilinks and shared entities/methods. **These are
not the output** — the goal is what is *not* yet linked. If a connection is
obvious or already drawn, dig past it.

### Step 3: Find non-obvious bridges
Surface **3–5** connections, each in exactly one bucket:
- **Structural analogy** — the same mechanism/identification/shape appears in
  both themes under different names (e.g. a bandwidth mechanism in one, an
  attention-cost mechanism in the other).
- **Transfer opportunity** — a method, dataset, or design from one theme could
  answer an open question in the other.
- **Collision idea** — putting the two together suggests a new question
  neither theme has posed.

For each: name the two concrete notes/pages it connects (by path), state the
connection in one or two sentences, and say why it is non-obvious.

### Step 4: Propose, don't write
End with concrete, optional follow-ups the user can choose to run:
- specific `[[wikilinks]]` worth adding (and in which notes),
- a candidate `_brain/synthesis/<slug>.md` if a bridge is substantial enough
  to deserve a page (name it; don't create it),
- which bridge, if any, is worth a fuller `/wiki-push`.

## Output format

```
## Bridges: <themeA> ↔ <themeB>

### Structural analogy
- [[A/30_concepts/x]] ↔ [[B/30_concepts/y]] — <one-line connection>. Non-obvious because <…>.

### Transfer opportunity
- <method/dataset in A> → <open question in B> — <one line>.

### Collision idea
- <A> + <B> → <new question neither has posed>.

## Suggested follow-ups (optional — nothing written yet)
- add [[…]] in <note>
- candidate synthesis page: _brain/synthesis/<slug>.md
- worth a /wiki-push? <yes/no + which>
```

## Guardrails

Do not:
- write or modify any file — this skill only proposes
- restate connections that are already linked or obvious ("both use regressions")
- invent notes or claims not present in the wikis
- return more than ~5 bridges — precision over volume
- read entire corpora when the `_map.md` catalogs suffice

## Standard

Successful if the user sees at least one genuinely non-obvious, actionable
connection they had not already drawn — with the exact notes it links and a
clear next step they can choose to take.
