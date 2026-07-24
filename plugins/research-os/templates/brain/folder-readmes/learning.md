# Learning

Durable, reusable research and process learnings — plus the home of the spaced-repetition engine. **This folder is shared; mind what owns what.**

**Engram (machine-owned — do not hand-edit).** The engram spaced-repetition engine is vendored into research-os and stores its state here via `ENGRAM_HOME`. It owns the JSON state (`learner-model.json`, `experiments.json`, `misconceptions.json`, `sessions.jsonl`, `stash-*.json`) and the subdirectories `artifacts/ audits/ exports/ gold/ graphs/ receipts/`. Drive it through `/learn`, `/recall`, and `/coach` — never edit its files by hand.

**`pending-topics.md` (skill-owned).** `/learn` maintains this queue of topics to teach later.

**Human learning notes (`.md`).** Durable lessons worth keeping as reference use `note_type: learning` (template `learning_template.md`), with a `confidence` level and, for aging facts, an `(as of YYYY-MM-DD)` stamp. Use ordinary note names — **do not** reuse engram's reserved JSON filenames or create a directory matching its reserved subdirs.
