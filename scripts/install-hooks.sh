#!/usr/bin/env bash
#
# Point this repository's git hooks at the tracked .githooks/ directory.
#
#     bash scripts/install-hooks.sh
#
# Idempotent: re-running reports that nothing changed. Uses core.hooksPath
# rather than copying into .git/hooks, so the hooks stay under version control
# and an update arrives with a pull instead of a reinstall.

set -eu

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || {
  echo "not inside a git repository" >&2
  exit 1
}

HOOKS_DIR=".githooks"

if [ ! -d "$ROOT/$HOOKS_DIR" ]; then
  echo "$HOOKS_DIR/ does not exist in $ROOT" >&2
  exit 1
fi

current=$(git -C "$ROOT" config --local --get core.hooksPath || true)

if [ "$current" = "$HOOKS_DIR" ]; then
  echo "core.hooksPath already set to $HOOKS_DIR - nothing to do"
else
  git -C "$ROOT" config core.hooksPath "$HOOKS_DIR"
  if [ -n "$current" ]; then
    echo "core.hooksPath changed from '$current' to '$HOOKS_DIR'"
  else
    echo "core.hooksPath set to $HOOKS_DIR"
  fi
fi

# Git honours the executable bit on POSIX filesystems and ignores it on
# Windows. chmod is harmless either way.
changed=0
for hook in "$ROOT/$HOOKS_DIR"/*; do
  [ -f "$hook" ] || continue
  if [ ! -x "$hook" ]; then
    chmod +x "$hook" 2>/dev/null && changed=1
  fi
done
if [ "$changed" -eq 1 ]; then
  echo "made hook scripts executable"
fi

echo
echo "active hooks:"
for hook in "$ROOT/$HOOKS_DIR"/*; do
  [ -f "$hook" ] && echo "  $(basename "$hook")"
done
echo
echo "bypass a single commit with: SKIP_INTEGRITY_GATE=1 git commit"
