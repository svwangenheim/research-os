#!/usr/bin/env python3
"""
Stop hook - push/propagate nudge.

Implements the standing two-output rule (rules/wiki-integration.md): if the
current project's wiki-links.md still lists unchecked "to push back" items,
gently remind (once per session) to run /wiki-push. This is an OFFER, never an
auto-write - it only prints a reminder.

Hook Event: Stop. Always exits 0 (never blocks). Degrades to silence on error.
"""

import hashlib
import json
import os
import sys
from pathlib import Path

YELLOW = "\033[0;33m"
CYAN = "\033[0;36m"
NC = "\033[0m"


def find_wiki_links(project_dir: Path) -> Path | None:
    """Walk up from the project dir looking for a wiki-links.md bridge."""
    p = project_dir.resolve()
    for _ in range(6):
        candidate = p / "wiki-links.md"
        if candidate.is_file():
            return candidate
        if p == p.parent:
            break
        p = p.parent
    return None


def unpushed_items(wiki_links: Path) -> list[str]:
    """Unchecked `- [ ]` items under the 'To push back' section (real, not template)."""
    try:
        text = wiki_links.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    items: list[str] = []
    in_section = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.lower().startswith("## to push back"):
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if in_section and stripped.startswith("- [ ]"):
            item = stripped[len("- [ ]"):].strip()
            if item and not item.startswith("<"):  # skip the template placeholder
                items.append(item)
    return items


def already_nudged(session_id: str) -> bool:
    """Nudge at most once per session - avoid nagging on every Stop."""
    if not session_id:
        return False
    marker_dir = Path.home() / ".claude" / "sessions"
    marker = marker_dir / f"push-nudge-{hashlib.md5(session_id.encode()).hexdigest()[:12]}"
    if marker.exists():
        return True
    try:
        marker_dir.mkdir(parents=True, exist_ok=True)
        marker.write_text("1")
    except OSError:
        pass
    return False


def main() -> int:
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, IOError):
        hook_input = {}

    # Avoid loops: if this Stop was itself triggered by a stop hook, bail.
    if hook_input.get("stop_hook_active"):
        return 0

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR") or hook_input.get("cwd") or ""
    if not project_dir:
        return 0

    wiki_links = find_wiki_links(Path(project_dir))
    if wiki_links is None:
        return 0

    items = unpushed_items(wiki_links)
    if not items:
        return 0

    if already_nudged(str(hook_input.get("session_id", ""))):
        return 0

    lines = [
        "",
        f"{YELLOW}⇪ Unpushed durable knowledge{NC}",
        f"  {wiki_links.name} still lists {len(items)} item(s) to push back:",
    ]
    lines.extend(f"  • {item[:80]}" for item in items[:3])
    lines.append(f"{CYAN}  Run /wiki-push to route them (offer only - nothing is written automatically).{NC}")
    lines.append("")
    print("\n".join(lines), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
