#!/usr/bin/env python3
"""
Register or unregister a procedure's `schedule:` frontmatter as a Windows
Scheduled Task. This is the whole deploy step (guide step 5) for anything
that runs on a clock rather than an event: declare `schedule:`, run this.

One shared wrapper script (`scheduled/automate-procedure.ps1`) handles every
scheduled procedure -- each Scheduled Task just passes a different -Name
argument, reusing the `_common.ps1` reach-fix and UTF-8 logging that already
work for the four routines registered before this. No new task-per-procedure
script gets hand-written.

Schedule syntax (validated at ingest by wiki_quality_check.py too, so a typo
is caught before it silently fails to register):
    "daily HH:MM"
    "weekly <mon|tue|wed|thu|fri|sat|sun> HH:MM"
    "monthly <1-31> HH:MM"

Usage:
    python automate_schedule.py --root <vault> --name <procedure>          # register
    python automate_schedule.py --root <vault> --name <procedure> --off    # unregister
    python automate_schedule.py --root <vault> --list                      # declared vs registered
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from wiki_quality_check import force_utf8_console, parse_frontmatter  # noqa: E402

TASK_PREFIX = "ResearchOS-Automate-"
WRAPPER_REL = r"scripts\scheduled\automate-procedure.ps1"

WEEKDAY_MAP = {
    "mon": "MON", "monday": "MON",
    "tue": "TUE", "tues": "TUE", "tuesday": "TUE",
    "wed": "WED", "wednesday": "WED",
    "thu": "THU", "thur": "THU", "thurs": "THU", "thursday": "THU",
    "fri": "FRI", "friday": "FRI",
    "sat": "SAT", "saturday": "SAT",
    "sun": "SUN", "sunday": "SUN",
}


@dataclass
class ScheduleSpec:
    kind: str  # daily | weekly | monthly
    time: str  # HH:MM
    day: str | None = None  # weekday code or day-of-month


class ScheduleError(ValueError):
    pass


def parse_schedule(raw: str) -> ScheduleSpec:
    parts = raw.strip().split()
    if not parts:
        raise ScheduleError(f"empty schedule string")

    kind = parts[0].lower()
    if kind == "daily":
        if len(parts) != 2:
            raise ScheduleError(f"'daily' expects 'daily HH:MM', got {raw!r}")
        return ScheduleSpec("daily", parts[1])

    if kind == "weekly":
        if len(parts) != 3:
            raise ScheduleError(f"'weekly' expects 'weekly <day> HH:MM', got {raw!r}")
        day = WEEKDAY_MAP.get(parts[1].lower())
        if day is None:
            raise ScheduleError(f"unknown weekday {parts[1]!r} in {raw!r}")
        return ScheduleSpec("weekly", parts[2], day)

    if kind == "monthly":
        if len(parts) != 3:
            raise ScheduleError(f"'monthly' expects 'monthly <1-31> HH:MM', got {raw!r}")
        try:
            day_num = int(parts[1])
        except ValueError:
            raise ScheduleError(f"day-of-month must be an integer, got {parts[1]!r}")
        if not 1 <= day_num <= 31:
            raise ScheduleError(f"day-of-month {day_num} out of range 1-31")
        return ScheduleSpec("monthly", parts[2], str(day_num))

    raise ScheduleError(f"schedule must start with daily/weekly/monthly, got {raw!r}")


def load_procedures(brain_root: Path) -> list[tuple[str, dict[str, Any], Path]]:
    folder = brain_root / "procedures"
    if not folder.is_dir():
        return []
    out: list[tuple[str, dict[str, Any], Path]] = []
    for path in sorted(folder.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        fm, _ = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        if fm.get("note_type") != "procedure":
            continue
        name = str(fm.get("name") or path.stem)
        out.append((name, fm, path))
    return out


def find_procedure(brain_root: Path, name: str) -> tuple[dict[str, Any], Path] | None:
    for proc_name, fm, path in load_procedures(brain_root):
        if proc_name == name:
            return fm, path
    return None


def task_name(procedure_name: str) -> str:
    return f"{TASK_PREFIX}{procedure_name}"


def run_schtasks(args: list[str]) -> subprocess.CompletedProcess:
    # encoding="utf-8", errors="replace": schtasks' console output follows the
    # system codepage (German cp1252 on this machine), and column headers like
    # the German locale's own labels contain bytes that crash text=True's
    # default locale decode. Never let a decode error hide whether a task
    # actually got registered.
    return subprocess.run(
        ["schtasks", *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
        check=False,
    )


def registered_tasks() -> set[str]:
    result = run_schtasks(["/query", "/fo", "CSV", "/nh"])
    if result.returncode != 0:
        return set()
    names: set[str] = set()
    for line in result.stdout.splitlines():
        first = line.split(",")[0].strip().strip('"').lstrip("\\")
        if first.startswith(TASK_PREFIX):
            names.add(first)
    return names


def register(plugin_root: Path, procedure_name: str, spec: ScheduleSpec) -> subprocess.CompletedProcess:
    wrapper = plugin_root / WRAPPER_REL
    action = (
        f'powershell.exe -NonInteractive -ExecutionPolicy Bypass -File "{wrapper}" '
        f'-Name "{procedure_name}"'
    )
    args = ["/create", "/tn", task_name(procedure_name), "/tr", action, "/f"]
    if spec.kind == "daily":
        args += ["/sc", "daily", "/st", spec.time]
    elif spec.kind == "weekly":
        args += ["/sc", "weekly", "/d", spec.day, "/st", spec.time]
    else:
        args += ["/sc", "monthly", "/d", spec.day, "/st", spec.time]
    return run_schtasks(args)


def unregister(procedure_name: str) -> subprocess.CompletedProcess:
    return run_schtasks(["/delete", "/tn", task_name(procedure_name), "/f"])


def cmd_list(brain_root: Path) -> int:
    declared = {
        name: fm.get("schedule")
        for name, fm, _ in load_procedures(brain_root)
        if fm.get("schedule") not in (None, "null", "")
    }
    malformed: dict[str, str] = {}
    valid_declared: dict[str, Any] = {}
    for name, raw in declared.items():
        try:
            parse_schedule(str(raw))
            valid_declared[name] = raw
        except ScheduleError as exc:
            malformed[name] = str(exc)

    registered = registered_tasks()
    registered_names = {t[len(TASK_PREFIX):] for t in registered}

    print("# Schedule drift report\n")
    only_declared = sorted(set(valid_declared) - registered_names)
    only_registered = sorted(registered_names - set(declared))
    both = sorted(set(valid_declared) & registered_names)

    if both:
        print(f"## In sync ({len(both)})")
        for name in both:
            print(f"  - {name}: {valid_declared[name]}")
        print()
    if only_declared:
        print(f"## Declared but not registered ({len(only_declared)}) -- run `automate schedule <name>`")
        for name in only_declared:
            print(f"  - {name}: {valid_declared[name]}")
        print()
    if malformed:
        print(f"## MALFORMED schedule -- registering would fail ({len(malformed)})")
        for name, err in sorted(malformed.items()):
            print(f"  - {name}: {declared[name]!r} -- {err}")
        print()
    if only_registered:
        print(f"## Registered but no longer declared ({len(only_registered)}) -- likely stale, consider `--off`")
        for name in only_registered:
            print(f"  - {name}")
        print()
    if not (both or only_declared or malformed or only_registered):
        print("No procedures declare a schedule, and no ResearchOS-Automate-* tasks are registered.")
    return 0


def main(argv: list[str] | None = None) -> int:
    force_utf8_console()
    parser = argparse.ArgumentParser(description="Register/unregister a procedure's schedule.")
    parser.add_argument("--root", type=Path, required=True, help="Vault root or _brain directory.")
    parser.add_argument("--plugin-root", type=Path, help="Defaults to this script's plugin root.")
    parser.add_argument("--name", help="Procedure name to (un)register.")
    parser.add_argument("--off", action="store_true", help="Unregister rather than register.")
    parser.add_argument("--list", action="store_true", help="Report declared-vs-registered drift.")
    args = parser.parse_args(argv)

    brain_root = args.root if args.root.name == "_brain" else args.root / "_brain"
    plugin_root = args.plugin_root or Path(__file__).resolve().parent.parent

    if args.list:
        return cmd_list(brain_root)

    if not args.name:
        parser.error("--name is required unless --list is given")

    if args.off:
        result = unregister(args.name)
        if result.returncode == 0:
            print(f"Unregistered {task_name(args.name)}")
            return 0
        print(f"error: {result.stderr.strip() or result.stdout.strip()}", file=sys.stderr)
        return 1

    found = find_procedure(brain_root, args.name)
    if found is None:
        print(f"error: no procedure named {args.name!r} in {brain_root / 'procedures'}", file=sys.stderr)
        return 1
    fm, _ = found
    raw_schedule = fm.get("schedule")
    if raw_schedule in (None, "null", ""):
        print(f"error: {args.name!r} has no schedule: set -- nothing to register", file=sys.stderr)
        return 1

    try:
        spec = parse_schedule(str(raw_schedule))
    except ScheduleError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    result = register(plugin_root, args.name, spec)
    if result.returncode == 0:
        print(f"Registered {task_name(args.name)} ({raw_schedule})")
        return 0
    print(f"error: {result.stderr.strip() or result.stdout.strip()}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
