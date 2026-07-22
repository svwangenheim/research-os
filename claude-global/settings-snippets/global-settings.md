# Global Settings Setup

Follow these steps once to make the wiki and research skills available in all
Claude Code sessions across all your projects.

---

## Step 1: Install wiki skills globally

From the Research-OS root directory:

```bash
# Create directories if they don't exist
mkdir -p ~/.claude/agents
mkdir -p ~/.claude/skills

# Copy wiki agents and skills
cp claude-global/agents/wiki-librarian.md ~/.claude/agents/
cp -r claude-global/skills/wiki-pull  ~/.claude/skills/
cp -r claude-global/skills/wiki-push  ~/.claude/skills/
cp -r claude-global/skills/wiki-ingest ~/.claude/skills/
```

After this, `/wiki-pull`, `/wiki-push`, `/wiki-ingest`, and the `wiki-librarian`
agent are available in every Claude Code session.

---

## Step 2: Create ~/.claude/VAULT_PATH

This file stores the absolute path to your vault so that the wiki-ingest skill
can locate it for Bash commands (markitdown needs the full path).

**Windows (Git Bash):**
```bash
echo 'C:/Users/YOUR_USERNAME/Research-OS/vault' > ~/.claude/VAULT_PATH
```

**Mac/Linux:**
```bash
echo '/Users/YOUR_USERNAME/Research-OS/vault' > ~/.claude/VAULT_PATH
```

Replace the path with the actual location of your `vault/` directory.

Verify:
```bash
cat ~/.claude/VAULT_PATH
```

---

## Step 3: Add to ~/.claude/settings.json

Open `~/.claude/settings.json` and merge the following into the `permissions`
section. If the file doesn't exist yet, create it with this content:

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": [
      "Bash(markitdown *)",
      "Bash(python -m markitdown *)"
    ],
    "additionalDirectories": [
      "C:/Users/YOUR_USERNAME/Research-OS/vault"
    ]
  }
}
```

Replace `C:/Users/YOUR_USERNAME/Research-OS/vault` with the actual path.

**What this does:**
- `additionalDirectories` — makes the vault readable and writable by Claude in
  every session automatically. You won't need to pass `--add-dir` each time.
- `Bash(markitdown *)` — allows wiki-ingest to call markitdown without prompting.

**If you prefer per-session control** (instead of always-on), skip the
`additionalDirectories` entry and use this when launching Claude:
```bash
claude --add-dir /path/to/Research-OS/vault
```

---

## Step 4: Install markitdown

```bash
pip install 'markitdown[pdf]'
```

Verify:
```bash
python -m markitdown --version
```

This is required for converting PDF sources to markdown via `/wiki-ingest`.

---

## Verification

After completing setup, open any project in Claude Code and run:

```
/wiki-pull test
```

You should see a response that reads the vault's `index.md` (even if it's empty).
If you see "wiki not available", check that `additionalDirectories` in
`~/.claude/settings.json` points to the correct path.
