# Global Settings Setup

Follow these steps once to make the two-layer knowledge model (personal
`_brain/` + thematic wikis) and its skills available in every Claude Code
session, across all your projects.

---

## Step 1: Install the wiki skills and agent globally

From the Research-OS root directory:

```bash
# Create directories if they don't exist
mkdir -p ~/.claude/agents
mkdir -p ~/.claude/skills

# Copy the wiki agent and skills
cp claude-global/agents/wiki-librarian.md ~/.claude/agents/
cp -r claude-global/skills/wiki-pull    ~/.claude/skills/
cp -r claude-global/skills/wiki-push    ~/.claude/skills/
cp -r claude-global/skills/wiki-ingest  ~/.claude/skills/
cp -r claude-global/skills/wiki-maintain ~/.claude/skills/
```

After this, `/wiki-pull`, `/wiki-push`, `/wiki-ingest`, `/wiki-maintain`, and
the `wiki-librarian` agent are available in every Claude Code session.

`/wiki-setup` and `/add-vault` (registry + root scaffolding, new-theme
scaffolding) ship with the research-os **plugin**, not as global skills —
they're available automatically inside any research-os project, or by adding
the plugin's `skills/` directory to a session.

---

## Step 2: Initialize the registry — `~/.claude/vaults.json`

The registry replaces the old single `~/.claude/VAULT_PATH` pointer with a
`theme -> path` map, plus the personal brain's path. If you have the
research-os plugin available, just run:

```
/wiki-setup
```

It creates `~/.claude/vaults.json`, scaffolds `_brain/` under your chosen
vault root, and (if it's still the uninitialized placeholder) offers a short
interview to fill in `_brain/profile.md`. It's idempotent — safe to run
again later; it recognizes what already exists rather than clobbering it.

**Without the plugin available**, create the registry by hand:

```bash
mkdir -p ~/YourVaultRoot/_brain/{daily,weekly,thoughts,projects,synthesis,learning}
cat > ~/.claude/vaults.json <<'EOF'
{
  "$schema": "research-os vault registry v1",
  "root": "/absolute/path/to/YourVaultRoot",
  "brain": {
    "path": "/absolute/path/to/YourVaultRoot/_brain",
    "description": "Personal second brain: profile, daily/weekly notes, thoughts, per-project journals, personal + cross-theme synthesis, durable learnings."
  },
  "wikis": {}
}
EOF
```

Then use `/add-vault <theme-name>` (or hand-scaffold, per
`${CLAUDE_PLUGIN_ROOT}/skills/add-vault/SKILL.md`) to register your first
thematic wiki.

**Legacy fallback:** if you never migrate to the registry, the wiki skills
still work against a single flat vault via `~/.claude/VAULT_PATH`:
```bash
echo '/absolute/path/to/vault' > ~/.claude/VAULT_PATH
```
This is a one-wiki, no-`_brain` mode kept only for backward compatibility —
prefer `/wiki-setup` for new installs.

---

## Step 3: Add to `~/.claude/settings.json`

Merge the following into the `permissions` section (create the file with
this content if it doesn't exist yet):

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": [
      "Bash(python -c *pymupdf4llm*)",
      "Bash(markitdown *)",
      "Bash(python -m markitdown *)",
      "Bash(python */wiki_quality_check.py*)"
    ],
    "additionalDirectories": [
      "/absolute/path/to/YourVaultRoot"
    ]
  }
}
```

**What this does:**
- `additionalDirectories` — makes the vault root (both `_brain/` and every
  thematic wiki live under it) readable and writable by Claude in every
  session automatically. You won't need to pass `--add-dir` each time.
- The `Bash(...)` allow rules let `/wiki-ingest` and `/wiki-maintain` run the
  PDF pipeline and the quality checker without prompting each time.

**If you prefer per-session control** (instead of always-on), skip
`additionalDirectories` and use this when launching Claude:
```bash
claude --add-dir /absolute/path/to/YourVaultRoot
```

---

## Step 4: Install the conversion tools

```bash
pip install pymupdf4llm
pip install 'markitdown[all]'
```

Verify:
```bash
python -c "import pymupdf4llm; print(pymupdf4llm.__version__)"
python -m markitdown --version
```

`pymupdf4llm` handles **PDF** conversion for `/wiki-ingest` (mechanical
extraction, followed by a mandatory Claude cleanup pass — see
`skills/wiki-ingest/SKILL.md`). `markitdown` remains the converter for
everything that is **not** a PDF (docx, pptx, xlsx, html, ...). Scanned PDFs
without a text layer additionally need Tesseract OCR on the system PATH for
`pymupdf4llm`'s `force_ocr` fallback.

---

## Verification

After completing setup, open any project (or no project at all) in Claude
Code and run:

```
/wiki-pull test
```

You should see a response that reads `_brain/profile.md` and the relevant
wiki (even if both are still mostly empty). If you see "the knowledge layer
is not available," check that `~/.claude/vaults.json` (or, in legacy mode,
`~/.claude/VAULT_PATH`) points to the correct path, and that
`additionalDirectories` in `~/.claude/settings.json` covers it.
