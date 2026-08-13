#!/usr/bin/env python3
"""
check_plugin_integrity.py - deterministic drift checks over the plugin tree.

Some classes of defect are mechanical: a frontmatter field is present or it is
not, an anchor resolves or it does not, a rule names an agent that never
implements it. An agent prompt asked to check twelve things will drift on the
eleventh. A script does not drift, so those checks live here rather than in a
review prompt.

Six checks over `plugins/research-os/`:

  1. Frontmatter <-> body tool parity. Every tool a SKILL.md body says it
     invokes must appear in that skill's `allowed-tools`.
  2. `argument-hint` <-> body flag parity, both directions. A documented flag
     missing from the hint misleads as much as a hinted flag that does nothing.
  3. Internal anchor resolution. Every `[text](path#anchor)` in skills/,
     agents/ and rules/ must land on a real heading.
  4. Rule <-> implementation parity. If a rule names an agent or skill as
     following its protocol, that agent or skill must mention the protocol.
  5. Agent frontmatter completeness. `name`, `description` and `model` are
     required; `effort` is advisory until model routing lands.
  6. House style, per `references/authoring-conventions.md`. Em dash over `--`,
     Title-Case H1 without a leading slash, an `**Input:**` line wherever a skill
     takes arguments, a `Use when ...` clause in every description, `SKILL.md`
     under 300 lines, and `tools:` rather than `allowed-tools:` on agents. All
     advisory except the agent tool key, which silently grants every tool.

Severities: P0 structural breakage, P1 real drift, P2 advisory.

Usage:
    python check_plugin_integrity.py [--plugin-root PATH] [--verbose]

Exit codes:
    0  clean, or advisories only
    1  at least one P0 or P1 finding
    2  the script itself failed

Fail-open per file: a file that cannot be read or parsed produces a P2 and the
run continues. A checker that crashes on one bad file checks nothing.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable, NamedTuple

# --- Findings ---------------------------------------------------------------

P0, P1, P2 = "P0", "P1", "P2"
BLOCKING = (P0, P1)


class Finding(NamedTuple):
    severity: str
    check: str
    path: str
    message: str


# --- Shared parsing ---------------------------------------------------------

TOOL_NAMES: tuple[str, ...] = (
    "Task",
    "Bash",
    "Write",
    "Edit",
    "Read",
    "Grep",
    "Glob",
    "WebSearch",
    "WebFetch",
    "Skill",
)
TOOLS_ALT = "|".join(TOOL_NAMES)

FENCE_RE = re.compile(r"^\s*(```+|~~~+)")
INLINE_CODE_RE = re.compile(r"``[^`]+``|`[^`\n]+`")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
LINK_RE = re.compile(r"\[[^\]\n]*\]\(([^)\s]+)\)")
FLAG_RE = re.compile(r"--[A-Za-z][A-Za-z0-9-]*")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return (frontmatter mapping, body). Only top-level scalar keys are kept."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            front = lines[1:index]
            body = "\n".join(lines[index + 1 :])
            break
    else:
        return {}, text

    mapping: dict[str, str] = {}
    for line in front:
        if not line or line[0].isspace() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if sep and key.strip():
            mapping[key.strip()] = value.strip()
    return mapping, body


def parse_tool_list(raw: str) -> list[str]:
    """Accept both frontmatter dialects: `["Read", "Grep"]` and `Read, Grep`."""
    value = raw.strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    parts = (part.strip().strip("\"'") for part in value.split(","))
    return [part for part in parts if part]


def strip_fenced_blocks(text: str) -> str:
    """Blank out fenced code blocks, keeping line numbering intact."""
    out: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if fence is None:
            if match:
                fence = match.group(1)[:3]
                out.append("")
                continue
            out.append(line)
        else:
            if match and match.group(1).startswith(fence):
                fence = None
            out.append("")
    return "\n".join(out)


def strip_code(text: str) -> str:
    """Fenced blocks and inline spans removed - what remains is prose."""
    return INLINE_CODE_RE.sub(" ", strip_fenced_blocks(text))


def slugify(heading: str) -> str:
    """GitHub's anchor slug: lowercase, punctuation dropped, spaces hyphenated."""
    text = heading.strip().lower()
    text = LINK_RE.sub(lambda m: m.group(0).split("]")[0][1:], text)
    text = text.replace("`", "").replace("*", "").replace("~", "")
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"\s+", "-", text.strip())


def heading_anchors(text: str) -> set[str]:
    """Every anchor a markdown file exposes, including GitHub's -1/-2 suffixes."""
    seen: dict[str, int] = {}
    anchors: set[str] = set()
    for line in strip_fenced_blocks(text).splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        slug = slugify(match.group(2))
        if not slug:
            continue
        count = seen.get(slug, 0)
        anchors.add(slug if count == 0 else f"{slug}-{count}")
        seen[slug] = count + 1
    return anchors


def slug_of(name: str) -> str:
    """Normalise a display name to the on-disk slug: `Writer-Critic` -> writer-critic."""
    return re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")


# --- Check 1: frontmatter <-> body tool parity ------------------------------

# A body mentions a tool constantly in ordinary English ("read the memo",
# "write the section"). Only invocation-shaped prose counts as a claim that the
# skill calls the tool, and code samples are stripped before matching so that
# documentation examples do not register as invocations.
_VERBS = r"(?:via|using|use|uses|used|invoke|invokes|invoking|call|calls|calling|through|with)"
INVOKE_PRE_RE = re.compile(rf"\b{_VERBS}\s+(?:a\s+|an\s+|the\s+)?({TOOLS_ALT})\b")
INVOKE_POST_RE = re.compile(rf"\b({TOOLS_ALT})\s+tool\b")
INVOKE_CALL_RE = re.compile(rf"\b({TOOLS_ALT})\(")


def body_tools(body: str) -> set[str]:
    prose = strip_code(body)
    found: set[str] = set()
    for pattern in (INVOKE_PRE_RE, INVOKE_POST_RE, INVOKE_CALL_RE):
        found.update(match.group(1) for match in pattern.finditer(prose))
    return found


def check_tool_parity(skill_files: Iterable[Path], root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in skill_files:
        rel = path.relative_to(root).as_posix()
        try:
            front, body = split_frontmatter(read_text(path))
        except OSError as exc:
            findings.append(Finding(P2, "tool-parity", rel, f"unreadable: {exc}"))
            continue
        raw = front.get("allowed-tools")
        if raw is None:
            findings.append(Finding(P1, "tool-parity", rel, "no `allowed-tools` in frontmatter"))
            continue
        declared = set(parse_tool_list(raw))
        for tool in sorted(body_tools(body) - declared):
            findings.append(
                Finding(
                    P1,
                    "tool-parity",
                    rel,
                    f"body says it invokes `{tool}`, which is not in `allowed-tools`",
                )
            )
    return findings


# --- Check 2: argument-hint <-> body flag parity ----------------------------

# Flags that belong to shell commands quoted in a skill body, not to the skill.
GENERIC_FLAGS = frozenset(
    {
        "--all",
        "--amend",
        "--cached",
        "--color",
        "--depth",
        "--force",
        "--force-with-lease",
        "--global",
        "--hard",
        "--help",
        "--no-edit",
        "--no-pager",
        "--no-verify",
        "--oneline",
        "--porcelain",
        "--quiet",
        "--set-upstream",
        "--short",
        "--soft",
        "--staged",
        "--stat",
        "--version",
    }
)

# Metavariables an `argument-hint` uses to stand in for "some flag", e.g.
# "[file path or --flag]". They name no mode and are not checked either way.
PLACEHOLDER_FLAGS = frozenset({"--flag", "--flags", "--option", "--options", "--arg", "--args"})


def hint_flags(hint: str) -> set[str]:
    return {flag for flag in FLAG_RE.findall(hint) if flag not in PLACEHOLDER_FLAGS}


def declared_body_flags(body: str, skill_name: str) -> set[str]:
    """
    Flags the body documents as belonging to this skill: those written after
    the skill's own slash command, and those used as a section heading. Other
    `--flag` text is quoted shell, not a documented mode.
    """
    text = strip_fenced_blocks(body)
    flags: set[str] = set()

    invocation = re.compile(rf"/{re.escape(skill_name)}\b([^\n`]*)")
    for match in invocation.finditer(text):
        flags.update(FLAG_RE.findall(match.group(1)))

    for line in text.splitlines():
        heading = HEADING_RE.match(line)
        if heading:
            flags.update(FLAG_RE.findall(heading.group(2)))

    return {flag for flag in flags if flag not in GENERIC_FLAGS}


def check_flag_parity(skill_files: Iterable[Path], root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in skill_files:
        rel = path.relative_to(root).as_posix()
        try:
            front, body = split_frontmatter(read_text(path))
        except OSError as exc:
            findings.append(Finding(P2, "flag-parity", rel, f"unreadable: {exc}"))
            continue

        name = front.get("name") or path.parent.name
        hint = front.get("argument-hint", "")
        hinted = hint_flags(hint)
        documented = declared_body_flags(body, name)
        body_text = strip_fenced_blocks(body)

        for flag in sorted(hinted):
            if flag not in body_text:
                findings.append(
                    Finding(
                        P1,
                        "flag-parity",
                        rel,
                        f"`argument-hint` offers `{flag}`, which the body never explains",
                    )
                )
        if not hint:
            continue
        for flag in sorted(documented - hinted):
            findings.append(
                Finding(
                    P1,
                    "flag-parity",
                    rel,
                    f"body documents `{flag}`, which is missing from `argument-hint`",
                )
            )
    return findings


# --- Check 3: internal anchor resolution ------------------------------------


def check_anchors(files: Iterable[Path], root: Path) -> list[Finding]:
    findings: list[Finding] = []
    anchor_cache: dict[Path, set[str] | None] = {}

    def anchors_for(target: Path) -> set[str] | None:
        if target not in anchor_cache:
            try:
                anchor_cache[target] = heading_anchors(read_text(target))
            except OSError:
                anchor_cache[target] = None
        return anchor_cache[target]

    for path in files:
        rel = path.relative_to(root).as_posix()
        try:
            text = strip_fenced_blocks(read_text(path))
        except OSError as exc:
            findings.append(Finding(P2, "anchors", rel, f"unreadable: {exc}"))
            continue

        for match in LINK_RE.finditer(text):
            href = match.group(1)
            if "#" not in href or href.startswith(("http://", "https://", "mailto:")):
                continue
            file_part, _, anchor = href.partition("#")
            if not anchor:
                continue
            target = path if not file_part else (path.parent / file_part).resolve()
            if not target.is_file():
                findings.append(
                    Finding(P1, "anchors", rel, f"link target does not exist: `{href}`")
                )
                continue
            available = anchors_for(target)
            if available is None:
                findings.append(Finding(P2, "anchors", rel, f"could not read `{file_part}`"))
                continue
            if anchor.lower() not in available:
                findings.append(
                    Finding(
                        P1,
                        "anchors",
                        rel,
                        f"anchor `#{anchor}` has no heading in `{file_part or path.name}`",
                    )
                )
    return findings


# --- Check 4: rule <-> implementation parity --------------------------------

# The keywords a rule's protocol is recognisable by. Falls back to the words in
# the rule's filename, which is right for most of them.
RULE_KEYWORDS: dict[str, tuple[str, ...]] = {
    "wiki-integration": ("wiki", "vault", "_brain"),
    "content-invariants": ("invariant", "INV-"),
    "content-standards": ("content standard", "caption", "table"),
    "folder-map": ("00_admin", "03_analysis", "04_paper"),
    "meta-governance": ("governance", "meta-rule"),
    "output-discipline": ("output", "update-over-create"),
    "working-paper-format": ("working paper", "latex", ".tex"),
    "html-dashboard": ("dashboard",),
    "logging": ("log", "journal"),
    "lifecycle": ("lifecycle", "phase", "stage"),
    "summary-parity": ("summary", "enumerative"),
    "prompt-shaping": ("prompt",),
    "confidential-data": ("confidential", "restricted", "microdata"),
}

BOLD_NAME_RE = re.compile(
    r"(?:^|\|)\s*[-*]?\s*\*\*([A-Za-z][A-Za-z0-9 /_-]{2,40})\*\*", re.MULTILINE
)
PATH_REF_RE = re.compile(r"\b(agents|skills)/([a-z0-9][a-z0-9-]*)\b")

# A rule mentions plenty of files it does not govern - "see also" pointers,
# sibling skills, examples inside tables. A bare path is only read as a claim of
# implementation when the same line carries a normative verb.
NORMATIVE_RE = re.compile(
    r"\b(MUST|SHALL|applies|apply|follows?|following|enforces?|implements?|obeys?|conforms?)\b"
)


def rule_keywords(stem: str) -> tuple[str, ...]:
    return RULE_KEYWORDS.get(stem, tuple(part for part in stem.split("-") if len(part) > 2))


def check_rule_parity(
    rule_files: Iterable[Path],
    agents: dict[str, Path],
    skills: dict[str, Path],
    root: Path,
) -> list[Finding]:
    findings: list[Finding] = []
    body_cache: dict[Path, str] = {}

    def body_of(path: Path) -> str:
        if path not in body_cache:
            body_cache[path] = read_text(path).lower()
        return body_cache[path]

    for path in rule_files:
        rel = path.relative_to(root).as_posix()
        try:
            text = strip_fenced_blocks(read_text(path))
        except OSError as exc:
            findings.append(Finding(P2, "rule-parity", rel, f"unreadable: {exc}"))
            continue

        keywords = rule_keywords(path.stem)
        if not keywords:
            continue

        named: dict[str, Path] = {}
        for match in BOLD_NAME_RE.finditer(text):
            slug = slug_of(match.group(1))
            if slug in agents:
                named[f"agents/{slug}.md"] = agents[slug]
            elif slug in skills:
                named[f"skills/{slug}/SKILL.md"] = skills[slug]
        for line in text.splitlines():
            if not NORMATIVE_RE.search(line):
                continue
            for kind, slug in PATH_REF_RE.findall(line):
                if kind == "agents" and slug in agents:
                    named[f"agents/{slug}.md"] = agents[slug]
                elif kind == "skills" and slug in skills:
                    named[f"skills/{slug}/SKILL.md"] = skills[slug]

        for label, target in sorted(named.items()):
            try:
                body = body_of(target)
            except OSError as exc:
                findings.append(
                    Finding(P2, "rule-parity", rel, f"unreadable target {label}: {exc}")
                )
                continue
            if not any(keyword.lower() in body for keyword in keywords):
                findings.append(
                    Finding(
                        P1,
                        "rule-parity",
                        rel,
                        f"names {label} as following this rule, but that file mentions "
                        f"none of {list(keywords)}",
                    )
                )
    return findings


# --- Check 5: agent frontmatter completeness --------------------------------


def check_agent_frontmatter(agent_files: Iterable[Path], root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in agent_files:
        rel = path.relative_to(root).as_posix()
        try:
            front, _ = split_frontmatter(read_text(path))
        except OSError as exc:
            findings.append(Finding(P2, "agent-frontmatter", rel, f"unreadable: {exc}"))
            continue
        if not front:
            findings.append(Finding(P0, "agent-frontmatter", rel, "no YAML frontmatter"))
            continue
        for field in ("name", "description"):
            if not front.get(field):
                findings.append(Finding(P0, "agent-frontmatter", rel, f"missing `{field}:`"))
        if not front.get("model"):
            findings.append(Finding(P1, "agent-frontmatter", rel, "missing `model:`"))
        if not front.get("effort"):
            findings.append(Finding(P2, "agent-frontmatter", rel, "missing `effort:`"))
    return findings


# --- Check 6: house style ---------------------------------------------------

MAX_SKILL_LINES = 300
PROSE_DASH_RE = re.compile(r"(?<=\S) -- (?=\S)")
TRIGGER_RE = re.compile(r"\bUse (?:when|on|for|to|before|after|in|whenever)\b", re.I)


def first_heading(body: str) -> str | None:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def check_house_style(
    skill_files: Iterable[Path], agent_files: Iterable[Path], root: Path
) -> list[Finding]:
    """Advisory conformance with references/authoring-conventions.md.

    Style findings are P2 on purpose: none of them break a skill at runtime, and a
    blocking style gate would only teach people to bypass the whole hook.
    """
    findings: list[Finding] = []

    for path in skill_files:
        rel = path.relative_to(root).as_posix()
        try:
            text = read_text(path)
        except OSError as exc:
            findings.append(Finding(P2, "house-style", rel, f"unreadable: {exc}"))
            continue
        front, body = split_frontmatter(text)

        # Vendored skills carry `origin:` and are kept byte-close to upstream so
        # /check-update-upstream-repos can still diff them. Restyling them would
        # trade a real capability for a cosmetic one.
        if front.get("origin"):
            continue

        n_lines = len(text.splitlines())
        if n_lines > MAX_SKILL_LINES:
            findings.append(
                Finding(
                    P2,
                    "house-style",
                    rel,
                    f"{n_lines} lines (over {MAX_SKILL_LINES}) - move content into "
                    f"templates/, references/ or config/ and list it in Bundled Resources",
                )
            )

        heading = first_heading(body)
        if heading is None:
            findings.append(Finding(P2, "house-style", rel, "no H1 heading"))
        elif heading.startswith("/") or heading.startswith("`/"):
            findings.append(
                Finding(P2, "house-style", rel, f"H1 `{heading}` should be Title Case without the slash")
            )

        if front.get("argument-hint") and "**Input:**" not in body:
            findings.append(
                Finding(P2, "house-style", rel, "takes arguments but has no `**Input:**` line")
            )

        description = front.get("description", "")
        if description and not TRIGGER_RE.search(description):
            findings.append(
                Finding(
                    P2,
                    "house-style",
                    rel,
                    "description has no `Use when/on/for ...` clause - the router matches on it",
                )
            )

        for count, line_no in dash_hits(body):
            findings.append(
                Finding(P2, "house-style", rel, f"line {line_no}: {count} prose `--`, use an em dash")
            )

    for path in agent_files:
        rel = path.relative_to(root).as_posix()
        try:
            text = read_text(path)
        except OSError as exc:
            findings.append(Finding(P2, "house-style", rel, f"unreadable: {exc}"))
            continue
        front, body = split_frontmatter(text)

        if "allowed-tools" in front:
            findings.append(
                Finding(
                    P1,
                    "house-style",
                    rel,
                    "agents declare `tools:`, not `allowed-tools:` - the key is ignored "
                    "and the agent silently gets every tool",
                )
            )
        elif not front.get("tools"):
            findings.append(
                Finding(P1, "house-style", rel, "missing `tools:` - the agent gets every tool")
            )

        for count, line_no in dash_hits(body):
            findings.append(
                Finding(P2, "house-style", rel, f"line {line_no}: {count} prose `--`, use an em dash")
            )

    return findings


def dash_hits(body: str) -> list[tuple[int, int]]:
    """Return (occurrences, line number) for prose `--` outside code."""
    hits: list[tuple[int, int]] = []
    for line_no, line in enumerate(strip_code(body).splitlines(), start=1):
        found = len(PROSE_DASH_RE.findall(line))
        if found:
            hits.append((found, line_no))
    return hits


# --- Driver -----------------------------------------------------------------


def collect(plugin_root: Path) -> tuple[list[Path], list[Path], list[Path]]:
    skills = sorted(plugin_root.glob("skills/*/SKILL.md"))
    agents = sorted(p for p in plugin_root.glob("agents/*.md") if p.name != "README.md")
    rules = sorted(p for p in plugin_root.glob("rules/*.md") if p.name != "README.md")
    return skills, agents, rules


def run(plugin_root: Path, verbose: bool) -> list[Finding]:
    skill_files, agent_files, rule_files = collect(plugin_root)
    agents_by_slug = {path.stem: path for path in agent_files}
    skills_by_slug = {path.parent.name: path for path in skill_files}

    if verbose:
        print(
            f"scanning {len(skill_files)} skills, {len(agent_files)} agents, "
            f"{len(rule_files)} rules under {plugin_root}"
        )

    linked = skill_files + agent_files + rule_files
    findings: list[Finding] = []
    findings += check_tool_parity(skill_files, plugin_root)
    findings += check_flag_parity(skill_files, plugin_root)
    findings += check_anchors(linked, plugin_root)
    findings += check_rule_parity(rule_files, agents_by_slug, skills_by_slug, plugin_root)
    findings += check_agent_frontmatter(agent_files, plugin_root)
    findings += check_house_style(skill_files, agent_files, plugin_root)
    return findings


def report(findings: list[Finding], verbose: bool) -> None:
    checks = (
        "tool-parity",
        "flag-parity",
        "anchors",
        "rule-parity",
        "agent-frontmatter",
        "house-style",
    )
    for check in checks:
        subset = [f for f in findings if f.check == check]
        if not subset:
            if verbose:
                print(f"[ok] {check}")
            continue
        print(f"\n{check} ({len(subset)})")
        for finding in sorted(subset, key=lambda f: (f.severity, f.path, f.message)):
            print(f"  {finding.severity}  {finding.path}: {finding.message}")

    counts = {level: sum(1 for f in findings if f.severity == level) for level in (P0, P1, P2)}
    print(f"\nP0 {counts[P0]}  P1 {counts[P1]}  P2 {counts[P2]}")


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--plugin-root",
        type=str,
        default=str(Path(__file__).resolve().parents[1]),
        help="Path to plugins/research-os (defaults to this script's plugin).",
    )
    parser.add_argument("--verbose", action="store_true", help="Also report checks that passed.")
    args = parser.parse_args(argv)

    plugin_root = Path(args.plugin_root).expanduser().resolve()
    if not plugin_root.is_dir():
        print(f"plugin root not found: {plugin_root}", file=sys.stderr)
        return 2

    findings = run(plugin_root, args.verbose)
    report(findings, args.verbose)
    blocking = [f for f in findings if f.severity in BLOCKING]
    if blocking:
        print(f"\nintegrity: FAIL ({len(blocking)} blocking)")
        return 1
    print("\nintegrity: PASS")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001 - a checker crash is exit 2, not a traceback
        print(f"check_plugin_integrity.py failed: {exc}", file=sys.stderr)
        sys.exit(2)
