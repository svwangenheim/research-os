#!/usr/bin/env python3
"""
Decide what an observation may record about a path -- BEFORE anything reads it.

The observation layer watches sessions so the workflow layer can learn how work
actually happens. That is useful, and it is also the most dangerous thing in
this repo: an always-on hook writing a JSONL, running inside a project governed
by AD-5 (Claude must never read, process, log, or cache real SOEP microdata in
any form). Epic 7.2 of the Microsimulation project closed two CRITICAL breaches
of exactly this kind. An observer that logged a dataframe head would reopen them.

So the policy is resolve-permissions-first, and it is deliberately boring:

  1. RESOLVE BEFORE READING. Consult the project's own `.claude/settings.json`
     -- `permissions.deny` and `sandbox.filesystem.denyRead` -- then the global
     `state/capture-policy.json`. Nothing is opened until this resolves.
  2. CLASSIFY BY TYPE. Code and prose may have their content captured, because
     knowing what was implemented is the entire point. DATA FILES NEVER DO.
  3. REDACT, DON'T SKIP. A denied path is recorded as `<redacted:reason>`, never
     as the real path -- a filename can leak a respondent id or a wave.
  4. FAIL CLOSED. Unknown extension, unreadable config, any error at all ->
     metadata only.

Reusing each project's existing deny configuration rather than inventing a
parallel list is the point: the Microsimulation repo already declares its
forbidden paths, verified live, and a second source of truth would drift.

Usage:
    python capture_policy.py --path <file> --project <root>
    python capture_policy.py --project <root> --selftest
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from wiki_quality_check import force_utf8_console  # noqa: E402


class Capture(str, Enum):
    CONTENT = "content"  # metadata + file content may be recorded
    METADATA = "metadata"  # path + tool + timestamp only; never content
    REDACTED = "redacted"  # not even the path; a marker only


# Content-bearing and safe to learn from: this is how the layer discovers what
# was actually implemented.
CODE_EXTENSIONS = frozenset(
    {".py", ".r", ".jl", ".do", ".sh", ".ps1", ".js", ".ts", ".sql", ".stan", ".cpp", ".c", ".h"}
)
DOC_EXTENSIONS = frozenset(
    {".md", ".txt", ".yaml", ".yml", ".toml", ".json", ".bib", ".tex", ".cfg", ".ini"}
)

# Never captured, at any level, in any project. Extension alone is disqualifying
# -- this list does not consult the deny config, it is unconditional.
DATA_EXTENSIONS = frozenset(
    {
        ".csv", ".tsv", ".dta", ".sav", ".por", ".parquet", ".feather", ".h5", ".hdf5",
        ".rds", ".rdata", ".rda", ".xlsx", ".xls", ".xlsm", ".sas7bdat", ".zsav",
        ".sps", ".pkl", ".pickle", ".npy", ".npz", ".db", ".sqlite", ".arrow", ".orc",
    }
)

# Directory names that mean "microdata lives here" regardless of what is in them.
#
# "raw" was removed 2026-08-12: folder-map.md names `02_data/raw/` as STANDARD
# structure in every research-os project (immutable raw data, not necessarily
# sensitive -- a public dataset's raw CSV lives there too). Left in, it hard-
# denied routine reads of an ordinary folder every project has, which is a
# false-positive severe enough to break normal work rather than protect it.
SENSITIVE_DIR_HINTS = ("soep", "microdata", "restricted", "confidential")


@dataclass(frozen=True)
class Decision:
    capture: Capture
    reason: str  # human-readable, for the CLI and the canary; may quote a pattern
    safe_path: str  # what may be written to the log -- possibly a redaction marker
    code: str = "ok"  # short enum-ish tag; the ONLY reason form a log may store

    @property
    def may_record_content(self) -> bool:
        return self.capture is Capture.CONTENT

    @property
    def may_record_path(self) -> bool:
        return self.capture is not Capture.REDACTED

    @property
    def log_reason(self) -> str:
        """The reason as a durable log may record it.

        `reason` deliberately quotes the matching deny pattern, which is what
        makes the canary output readable when something is wrong. But a pattern
        like `./SOEP/data/**` is path-shaped, and a redacted record that echoes
        anything path-shaped defeats the purpose of redacting. So logs get the
        short code and humans get the sentence.
        """
        return self.code


def find_project_root(path: Path) -> Path | None:
    """Nearest ancestor holding a .claude directory or a .git directory."""
    current = path.resolve()
    if current.is_file():
        current = current.parent
    for _ in range(8):
        if (current / ".claude").is_dir() or (current / ".git").exists():
            return current
        if current == current.parent:
            break
        current = current.parent
    return None


def _deny_globs_from_settings(settings: dict) -> list[str]:
    """Extract path patterns from both places a project can declare them."""
    globs: list[str] = []

    for entry in settings.get("permissions", {}).get("deny", []) or []:
        text = str(entry)
        # Shapes like `Read(./SOEP/data/**)` -- take what is inside the parens.
        if "(" in text and text.endswith(")"):
            inner = text[text.index("(") + 1 : -1].strip()
            if inner:
                globs.append(inner)
        else:
            globs.append(text)

    for entry in settings.get("sandbox", {}).get("filesystem", {}).get("denyRead", []) or []:
        raw = str(entry).rstrip("/")
        globs.append(raw)
        globs.append(f"{raw}/**")  # a denied directory denies everything under it

    return globs


def load_deny_globs(project_root: Path | None) -> tuple[list[str], bool]:
    """Deny patterns for a project. Returns (globs, config_was_readable).

    `config_was_readable` is False when a settings file exists but could not be
    parsed -- the caller must then fail closed rather than assume "no denies".
    """
    if project_root is None:
        return [], True

    globs: list[str] = []
    readable = True
    for name in ("settings.json", "settings.local.json"):
        path = project_root / ".claude" / name
        if not path.is_file():
            continue
        try:
            globs.extend(_deny_globs_from_settings(json.loads(path.read_text(encoding="utf-8"))))
        except (OSError, json.JSONDecodeError, AttributeError, TypeError):
            readable = False
    return globs, readable


def matches_deny(path: Path, project_root: Path | None, globs: list[str]) -> str | None:
    """Return the matching pattern, or None. Compares both relative and absolute."""
    candidates: list[str] = [path.as_posix()]
    if project_root is not None:
        try:
            relative = path.resolve().relative_to(project_root.resolve()).as_posix()
            candidates.extend([relative, f"./{relative}"])
        except ValueError:
            pass

    for pattern in globs:
        normalized = pattern.replace("\\", "/")
        bare = normalized[2:] if normalized.startswith("./") else normalized
        for candidate in candidates:
            plain = candidate[2:] if candidate.startswith("./") else candidate
            if fnmatch.fnmatch(plain, bare) or fnmatch.fnmatch(plain, f"{bare}/*"):
                return pattern
            # A denied directory covers everything beneath it.
            if not bare.endswith("*") and (plain == bare or plain.startswith(f"{bare}/")):
                return pattern
    return None


def decide(raw_path: str, project_root: Path | None = None) -> Decision:
    """The single entry point. Never opens the file."""
    if not raw_path:
        return Decision(Capture.METADATA, "no path given", "", "no-path")

    try:
        path = Path(raw_path)
    except (TypeError, ValueError):
        return Decision(Capture.REDACTED, "unparseable path", "<redacted:unparseable>", "unparseable")

    root = project_root if project_root is not None else find_project_root(path)

    # 1. Permission resolution happens first, before any classification.
    globs, config_readable = load_deny_globs(root)
    if not config_readable:
        return Decision(
            Capture.REDACTED,
            "project deny-config unreadable; failing closed",
            "<redacted:config-unreadable>",
            "config-unreadable",
        )

    if (pattern := matches_deny(path, root, globs)) is not None:
        return Decision(
            Capture.REDACTED,
            f"denied by project config: {pattern}",
            "<redacted:project-denied>",
            "project-denied",
        )

    posix_lower = path.as_posix().lower()
    parts = {p.lower() for p in path.parts}
    if any(hint in parts for hint in SENSITIVE_DIR_HINTS) or "/soep/" in posix_lower:
        return Decision(
            Capture.REDACTED,
            "path sits under a sensitive-data directory",
            "<redacted:sensitive-dir>",
            "sensitive-dir",
        )

    # 2. Classification by type. Data is unconditional -- it does not matter
    #    whether the deny config happened to list this particular file.
    suffix = path.suffix.lower()
    if suffix in DATA_EXTENSIONS:
        return Decision(
            Capture.METADATA,
            "data file: content never captured",
            path.as_posix(),
            "data-file",
        )
    if suffix in CODE_EXTENSIONS:
        return Decision(Capture.CONTENT, "code file", path.as_posix(), "code")
    if suffix in DOC_EXTENSIONS:
        return Decision(Capture.CONTENT, "document file", path.as_posix(), "doc")

    # 3. Fail closed on anything unrecognized.
    return Decision(Capture.METADATA, f"unknown type '{suffix}': metadata only", path.as_posix(), "unknown-type")


def selftest(project_root: Path | None) -> int:
    """The AD-5 canary. Ships with the feature; gates it."""
    root = project_root
    cases: list[tuple[str, Capture, str]] = [
        ("SOEP/data/pequiv.dta", Capture.REDACTED, "denied SOEP data"),
        ("./SOEP/data/pequiv.dta", Capture.REDACTED, "denied, ./ prefixed"),
        ("SOEP/crosswalks/map.csv", Capture.REDACTED, "denied crosswalks"),
        ("SOEP/metadata/vars.xlsx", Capture.REDACTED, "denied metadata"),
        ("SOEP/README.txt", Capture.REDACTED, "sensitive dir wins over doc extension"),
        ("euromod_de/adapters/data_source_soep.py", Capture.CONTENT, "code is capturable"),
        ("docs/RUNBOOK.md", Capture.CONTENT, "docs are capturable"),
        ("02_data/cleaned/panel.parquet", Capture.METADATA, "data extension, content never"),
        ("results/table1.csv", Capture.METADATA, "csv is data"),
        ("output/model.bin", Capture.METADATA, "unknown extension fails closed"),
    ]

    failures = 0
    print("AD-5 capture canary")
    print(f"project root: {root}\n")
    for raw, expected, label in cases:
        target = (root / raw) if root else Path(raw)
        decision = decide(str(target), root)
        ok = decision.capture is expected
        failures += 0 if ok else 1
        print(
            f"  [{'PASS' if ok else 'FAIL'}] {label}\n"
            f"         {raw}\n"
            f"         -> {decision.capture.value} ({decision.reason}); logged as {decision.safe_path}"
        )

    print()
    if failures:
        print(f"{failures} FAILURE(S) - observation must NOT be enabled in any DZ repo.")
    else:
        print("All cases pass. No data-file content, and no denied path, can reach a log.")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    force_utf8_console()
    parser = argparse.ArgumentParser(description="Decide what may be captured about a path.")
    parser.add_argument("--path", help="Path to evaluate.")
    parser.add_argument("--project", type=Path, help="Project root (else inferred).")
    parser.add_argument("--selftest", action="store_true", help="Run the AD-5 canary.")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)

    root = args.project.resolve() if args.project else None

    if args.selftest:
        return selftest(root)

    if not args.path:
        parser.error("--path is required unless --selftest is given")

    decision = decide(args.path, root)
    if args.format == "json":
        print(
            json.dumps(
                {
                    "capture": decision.capture.value,
                    "reason": decision.reason,
                    "safe_path": decision.safe_path,
                    "may_record_content": decision.may_record_content,
                }
            )
        )
    else:
        print(f"{decision.capture.value}: {decision.reason}")
        print(f"logged as: {decision.safe_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
