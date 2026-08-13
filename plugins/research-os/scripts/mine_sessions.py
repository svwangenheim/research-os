#!/usr/bin/env python3
"""
Mine real prompt sequences out of past Claude Code sessions, to seed personal
procedure drafts with actual evidence instead of invented steps.

Why this exists: `/automate new` should draft from how a task was ACTUALLY
done, not from a guess. `~/.claude/projects/<project>/*.jsonl` holds the full
session record for every project ever opened on this machine -- 117 sessions,
283 MB, 23 projects, verified during planning. The signal is almost entirely
in the USER turns: what was asked, in what order, and where a correction
happened ("no, actually..."). Assistant turns and tool results are the bulk of
the bytes and mostly noise for this purpose.

Read-only and advisory. Writes one report per project under
`_brain/.session-mining/` -- not a permanent routine; run during procedure
authoring and on demand.

Safety. Every extracted prompt is checked against the project's OWN
`.claude/settings.json` deny-list (via `capture_policy.py` -- the same policy
that gates the observation layer and passes the AD-5 canary) and against the
generic sensitive-directory hints, before being written to the report. A
prompt that mentions a denied path or a sensitive-directory hint is redacted
WHOLESALE, never partially -- this is prompt text a human typed or pasted, not
a structured file read, so there is no safe way to redact just a span of it.

Usage:
    python mine_sessions.py --project "<absolute project path>"
    python mine_sessions.py --all
    python mine_sessions.py --all --out <dir>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from capture_policy import SENSITIVE_DIR_HINTS, force_utf8_console, load_deny_globs  # noqa: E402

CLAUDE_PROJECTS_DIR = Path.home() / ".claude" / "projects"

MIN_PROMPT_CHARS = 3
MAX_PROMPT_CHARS = 4000  # a mined report is evidence, not a transcript archive
MAX_PROMPTS_PER_SESSION = 400  # bound a pathological session; report says if truncated

# Injected content that arrives as a "user" record but is not something the
# human typed: skill preambles (an entire SKILL.md dumped as the first
# message when a skill is invoked -- observed live in this very session),
# slash-command wrapper XML, and system reminders.
INJECTION_MARKERS = (
    "Base directory for this skill:",
    "<command-name>",
    "<command-message>",
    "<local-command-caveat>",
    "<system-reminder>",
    "<ide_selection>",
)

CORRECTION_PATTERNS = re.compile(
    r"^\s*(no[,.]|nope|wrong|not (quite|right)|actually[,.]?\s|that'?s (not|wrong)|"
    r"stop[,.]?\s|don'?t\b|instead\b|nein[,.]|falsch\b|doch\b)",
    re.IGNORECASE,
)

# A real message rarely opens with several markdown headings AND runs long --
# that shape is a skill-preamble dump, not something a person typed.
HEADING_RE = re.compile(r"^##?\s", re.MULTILINE)

# A real, human-typed prompt essentially never opens with a raw angle-bracket
# tag -- that shape is a system/tool wrapper (<task-notification>,
# <user-prompt-submit-hook>, <local-command-caveat>, ...). Catching the SHAPE
# rather than enumerating every tag name is the point: a new wrapper tag this
# machine's harness starts using tomorrow is caught without an edit here --
# the explicit INJECTION_MARKERS list stays as a second, defense-in-depth net
# for injected content that doesn't happen to open the message.
WRAPPER_TAG_RE = re.compile(r"^\s*</?[a-z][a-z0-9_-]*>")


@dataclass
class MinedPrompt:
    session: str
    index: int
    text: str
    is_correction: bool
    redacted: bool


@dataclass
class SessionMining:
    project_path: str
    project_dir_name: str
    sessions: dict[str, list[MinedPrompt]] = field(default_factory=dict)
    truncated_sessions: list[str] = field(default_factory=list)
    redacted_count: int = 0
    total_prompts: int = 0


def looks_injected(text: str) -> bool:
    if WRAPPER_TAG_RE.match(text):
        return True
    if any(marker in text for marker in INJECTION_MARKERS):
        return True
    if len(text) > 1500 and len(HEADING_RE.findall(text)) >= 3:
        return True
    return False


def extract_text(message: Any) -> str:
    content = message.get("content") if isinstance(message, dict) else None
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = [
            block.get("text", "")
            for block in content
            if isinstance(block, dict) and block.get("type") == "text"
        ]
        return " ".join(p for p in parts if p)
    return ""


def find_cwd(records: list[dict[str, Any]]) -> str | None:
    for record in records[:50]:
        cwd = record.get("cwd")
        if cwd:
            return str(cwd)
    return None


def redaction_needed(text: str, project_root: Path | None, deny_globs: list[str]) -> bool:
    lowered = text.lower()
    if any(hint in lowered for hint in SENSITIVE_DIR_HINTS):
        return True
    for pattern in deny_globs:
        bare = pattern.replace("\\", "/").removeprefix("./").rstrip("/*").lower()
        if bare and bare in lowered.replace("\\", "/"):
            return True
    return False


def load_session_records(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    try:
        with path.open(encoding="utf-8", errors="replace") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    except OSError:
        pass
    return records


def mine_session(path: Path, deny_globs: list[str], project_root: Path | None) -> tuple[list[MinedPrompt], bool]:
    records = load_session_records(path)
    prompts: list[MinedPrompt] = []
    truncated = False

    for record in records:
        if record.get("type") != "user":
            continue
        message = record.get("message")
        if not isinstance(message, dict):
            continue
        text = extract_text(message).strip()
        if len(text) < MIN_PROMPT_CHARS or looks_injected(text):
            continue

        redacted = redaction_needed(text, project_root, deny_globs)
        stored = "<redacted: mentions a denied path or sensitive directory>" if redacted else text[:MAX_PROMPT_CHARS]

        prompts.append(
            MinedPrompt(
                session=path.stem,
                index=len(prompts),
                text=stored,
                is_correction=bool(CORRECTION_PATTERNS.match(text)) and not redacted,
                redacted=redacted,
            )
        )
        if len(prompts) >= MAX_PROMPTS_PER_SESSION:
            truncated = True
            break

    return prompts, truncated


def mine_project(project_dir: Path) -> SessionMining:
    jsonl_files = sorted(project_dir.glob("*.jsonl"))
    mining = SessionMining(project_path="", project_dir_name=project_dir.name)

    # Resolve the real project path once, from whichever session has it, so
    # the deny-list lookup uses the project's OWN .claude/settings.json --
    # not a decoded guess at the directory name (lossy: both spaces and
    # hyphens in the real path collapse to "-" in the encoded name).
    project_root: Path | None = None
    for jsonl_path in jsonl_files:
        records = load_session_records(jsonl_path)
        cwd = find_cwd(records)
        if cwd:
            candidate = Path(cwd)
            if candidate.is_dir():
                project_root = candidate
                mining.project_path = str(candidate)
            break

    deny_globs, _ = load_deny_globs(project_root)

    for jsonl_path in jsonl_files:
        prompts, truncated = mine_session(jsonl_path, deny_globs, project_root)
        if not prompts:
            continue
        mining.sessions[jsonl_path.stem] = prompts
        mining.total_prompts += len(prompts)
        mining.redacted_count += sum(1 for p in prompts if p.redacted)
        if truncated:
            mining.truncated_sessions.append(jsonl_path.stem)

    return mining


def top_terms(mining: SessionMining, n: int = 20) -> list[tuple[str, int]]:
    """Crude recurring-verb/noun signal -- not NLP, just frequency over
    non-trivial words, to point a human at what to look for, not to replace
    reading the actual sequence."""
    STOPWORDS = {
        "the", "and", "for", "with", "this", "that", "have", "from", "your",
        "you", "are", "was", "but", "not", "can", "will", "just", "also",
        "should", "would", "there", "here", "please", "yes", "okay", "then",
        "request", "interrupted", "user", "continue", "which", "need",
        "what", "where", "everything", "want", "more", "start", "first",
        "when", "does", "some", "into", "over", "than", "them", "they",
        "been", "were", "these", "those", "about", "could", "each", "same",
        "such", "only", "even", "still", "much", "many", "make", "made",
        "like", "well", "know", "think", "look", "looks", "actually",
    }
    counts: Counter[str] = Counter()
    for prompts in mining.sessions.values():
        for prompt in prompts:
            if prompt.redacted:
                continue
            for word in re.findall(r"[a-zA-Z][a-zA-Z_-]{3,}", prompt.text.lower()):
                if word not in STOPWORDS:
                    counts[word] += 1
    return counts.most_common(n)


def render_report(mining: SessionMining) -> str:
    lines = [
        f"# Session mining — {mining.project_dir_name}",
        "",
        f"Project path: `{mining.project_path or '(unresolved -- generic filter only)'}`",
        f"Sessions with signal: {len(mining.sessions)} · total prompts: {mining.total_prompts} · redacted: {mining.redacted_count}",
        "",
    ]
    if mining.truncated_sessions:
        lines.append(f"**Truncated at {MAX_PROMPTS_PER_SESSION} prompts:** {', '.join(mining.truncated_sessions)}")
        lines.append("")

    terms = top_terms(mining)
    if terms:
        lines.append("## Recurring terms (frequency signal, not a summary)")
        lines.append(", ".join(f"{word} ({count})" for word, count in terms))
        lines.append("")

    corrections = [
        (session, p) for session, prompts in mining.sessions.items() for p in prompts if p.is_correction
    ]
    if corrections:
        lines.append(f"## Correction turns ({len(corrections)}) — where the real rules usually live")
        for session, prompt in corrections[:40]:
            lines.append(f"- [{session}#{prompt.index}] {prompt.text[:280]}")
        lines.append("")

    lines.append("## Prompt sequences by session")
    for session, prompts in mining.sessions.items():
        lines.append(f"\n### {session} ({len(prompts)} prompt(s))")
        for prompt in prompts:
            marker = " **[correction]**" if prompt.is_correction else ""
            lines.append(f"{prompt.index}.{marker} {prompt.text}")

    return "\n".join(lines)


def discover_project_dirs(name_filter: str | None) -> list[Path]:
    if not CLAUDE_PROJECTS_DIR.is_dir():
        return []
    dirs = [d for d in CLAUDE_PROJECTS_DIR.iterdir() if d.is_dir()]
    if name_filter:
        dirs = [d for d in dirs if name_filter.lower() in d.name.lower()]
    return sorted(dirs)


def resolve_by_path(target_path: str) -> Path | None:
    """Find the project dir whose sessions' cwd matches target_path exactly."""
    target = str(Path(target_path))
    for project_dir in discover_project_dirs(None):
        for jsonl_path in sorted(project_dir.glob("*.jsonl"))[:1]:
            records = load_session_records(jsonl_path)
            cwd = find_cwd(records)
            if cwd and str(Path(cwd)) == target:
                return project_dir
    return None


def main(argv: list[str] | None = None) -> int:
    force_utf8_console()
    parser = argparse.ArgumentParser(description="Mine past session history for procedure evidence.")
    parser.add_argument("--project", help="Absolute project path (matched against sessions' cwd).")
    parser.add_argument("--all", action="store_true", help="Mine every project under ~/.claude/projects/.")
    parser.add_argument("--out", type=Path, help="Output directory (default: <vault>/_brain/.session-mining).")
    parser.add_argument("--root", type=Path, help="Vault root, to derive the default --out.")
    args = parser.parse_args(argv)

    if not args.project and not args.all:
        parser.error("pass --project <path> or --all")

    if args.out:
        out_dir = args.out
    elif args.root:
        brain_root = args.root if args.root.name == "_brain" else args.root / "_brain"
        out_dir = brain_root / ".session-mining"
    else:
        parser.error("pass --out <dir> or --root <vault>")
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.all:
        project_dirs = discover_project_dirs(None)
    else:
        found = resolve_by_path(args.project)
        project_dirs = [found] if found else []
        if not found:
            print(f"error: no session found with cwd == {args.project!r}", file=sys.stderr)
            return 1

    written = 0
    for project_dir in project_dirs:
        mining = mine_project(project_dir)
        if not mining.sessions:
            continue
        out_path = out_dir / f"{project_dir.name}.md"
        out_path.write_text(render_report(mining), encoding="utf-8")
        written += 1
        print(f"{project_dir.name}: {mining.total_prompts} prompt(s), {mining.redacted_count} redacted -> {out_path}")

    print(f"\n{written} report(s) written to {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
