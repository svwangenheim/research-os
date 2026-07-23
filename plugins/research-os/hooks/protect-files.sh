#!/bin/bash
# Block accidental edits to protected files
# Customize PROTECTED_PATTERNS below for your project
INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name')
FILE=""

# Extract file path based on tool type
if [ "$TOOL" = "Edit" ] || [ "$TOOL" = "Write" ]; then
  FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
fi

# No file path = not a file operation, allow
if [ -z "$FILE" ]; then
  exit 0
fi

# ============================================================
# Protected basenames — edit manually, or remove protection here.
# passport.yaml replaces pipeline-state.json/SESSION_REPORT.md/MEMORY.md
# as the single state ledger; guard it the same way settings.json is guarded.
# ============================================================
PROTECTED_PATTERNS=(
  "settings.json"
  "passport.yaml"
  "strategy-memo-*.md"
  "referee-report-*.md"
  "quality-score-*.json"
)

BASENAME=$(basename "$FILE")
for PATTERN in "${PROTECTED_PATTERNS[@]}"; do
  if [[ "$BASENAME" == "$PATTERN" ]]; then
    echo "Protected file: $BASENAME. Edit manually or remove protection in hooks/protect-files.sh" >&2
    exit 2
  fi
done

exit 0
