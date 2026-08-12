# output-styles/

Two output styles for research work: `academic-writing` (drafting papers, abstracts, referee responses) and `referee` (writing or simulating peer review).

## These files are the source; they are not loaded from here

`output-styles/` is **not** a recognized Claude Code plugin component. The plugin loader knows `skills/`, `commands/`, `agents/`, `hooks/`, `monitors/`, `bin/`, `.mcp.json`, `.lsp.json` and `settings.json` — nothing else. A style sitting in a plugin directory is an inert file.

Output styles are discovered at **user scope** (`~/.claude/output-styles/`) and **project scope** (`.claude/output-styles/`). So these are kept here under version control as the authoritative copies, and installed by copying:

```bash
mkdir -p ~/.claude/output-styles
cp plugins/research-os/output-styles/*.md ~/.claude/output-styles/
```

Then switch per task with `/output-style academic-writing` or `/output-style referee`.

The same trap caught `rules/` in this plugin, which is why it is worth stating plainly: a directory that looks like a component is not one, and a plugin that ships an unrecognized directory produces documentation describing behaviour that never happens.

## Do not set `outputStyle` globally

It is tempting to pin `academic-writing` in `~/.claude/settings.json`. Don't. The style would then apply to every response in every project — infrastructure work, debugging, shell output — and hedge-to-the-evidence discipline reads as stilted when the subject is a broken hook. These are per-task voices, switched deliberately.

## Keeping the copies in sync

Copying creates two files that can drift. The plugin copy is authoritative: edit here, re-run the copy. If you find yourself editing `~/.claude/output-styles/` directly, copy the change back before it is lost on the next install.
