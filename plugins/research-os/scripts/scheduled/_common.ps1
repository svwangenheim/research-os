<#
Shared setup for the scheduled routines. Dot-source it from each wrapper:

    . "$PSScriptRoot\_common.ps1"

Provides $VaultRoot, $PluginRoot, $Py, Get-LogFile, and Get-ProjectAddDirArgs.

Why this file exists: before 2026-08-11 each routine ran with the vault as its
only reachable directory, so two of the three unattended runs in the week of
2026-07-27 reported "no indication of work" while five project repos sat busy
and uncommitted. Granting those directories is now derived from one place --
vault/_brain/projects/*.md frontmatter -- instead of being hardcoded per script.
#>

$VaultRoot = "C:\Users\dzsve\research-os\vault"
$PluginRoot = "C:\Users\dzsve\research-os\plugins\research-os"

# `claude -p` writes UTF-8 to stdout. Windows PowerShell 5.1 decodes a native
# command's output using [Console]::OutputEncoding, which on this machine
# defaults to the OEM codepage (850), not UTF-8 -- so every non-ASCII byte
# (em dashes, umlauts) got misread one byte at a time and re-encoded as UTF-8
# on top of that misreading (confirmed 2026-08-14: an em dash's three UTF-8
# bytes, decoded as cp850, re-encoded as UTF-8, produce exactly the "Ã"-style
# garbage seen in every scheduled log before this fix). Setting both
# encodings before any `& claude ...` call is what actually prevents it --
# `-Encoding utf8` on the write side alone cannot, since the string is already
# corrupted by the time it gets there.
try {
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    [Console]::InputEncoding = [System.Text.Encoding]::UTF8
} catch {
    # Not fatal -- a routine should still run, garbled output and all,
    # rather than not run at all.
}
$OutputEncoding = [System.Text.Encoding]::UTF8

# Portable interpreter resolution.
#
# Get-Command alone is not enough here: this machine has a `python3` on PATH
# that is a *bash* script (`#!/bin/bash exec python "$@"`). PowerShell happily
# reports it as an Application, runs it, produces no output, and exits 0 --
# a silent failure that looks exactly like "no projects found". So each
# candidate is probed by actually executing it and checking what comes back.
$Py = $null
foreach ($candidate in @("python.exe", "python", "py", "python3")) {
    $found = Get-Command $candidate -ErrorAction SilentlyContinue
    if (-not $found) { continue }
    try {
        $probe = & $found.Source -c "print('ok')" 2>$null
    } catch {
        continue
    }
    if ($probe -and ($probe -join "").Trim() -eq "ok") {
        $Py = $found.Source
        break
    }
}

function Get-LogFile {
    <#
    .SYNOPSIS
    Create (if needed) today's log directory and return a routine-named path
    inside it.

    .DESCRIPTION
    Dated-folder-first, not routine-first: `scheduled-logs/2026-08-14/` holds
    every routine that touched that day, so browsing one day answers "what
    ran" without hunting across N routine subfolders. Also drops the leading
    dot the old `.scheduled-logs` had -- Obsidian's file explorer treats a
    dot-prefixed folder as hidden, which made every log invisible from inside
    the vault, the one place these are actually meant to be read.
    #>
    param([Parameter(Mandatory = $true)][string]$Routine)

    $logDir = Join-Path $VaultRoot ("_brain\scheduled-logs\" + (Get-Date -Format "yyyy-MM-dd"))
    New-Item -ItemType Directory -Force -Path $logDir | Out-Null
    return Join-Path $logDir ("$Routine`_" + (Get-Date -Format "HHmm") + ".log")
}

function Save-RoutineTranscript {
    <#
    .SYNOPSIS
    Write a routine's transcript to its log file as UTF-8.

    .DESCRIPTION
    Not cosmetic. `Tee-Object -FilePath` on Windows PowerShell 5.1 writes
    UTF-16LE and has no -Encoding parameter (that arrived in PowerShell 6), so
    every log written before 2026-08-11 is NUL-interleaved: awkward to read,
    and effectively invisible to grep. Since the whole point of these routines
    is to leave a reviewable trail, the log has to be readable.
    #>
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$Content
    )

    Set-Content -LiteralPath $Path -Value $Content -Encoding utf8
}

function Get-ProjectAddDirArgs {
    <#
    .SYNOPSIS
    Return a flat --add-dir argument array for every reachable active project.

    .DESCRIPTION
    Reads working_directory: from vault/_brain/projects/*.md via
    resolve_project_paths.py. Paths covered by an ancestor are collapsed away.
    Returns an empty array on any failure -- a routine must still run, blind,
    rather than not run at all. Splat it: & claude -p $Prompt @AddDirArgs ...
    #>
    if (-not $Py) { return @() }

    $script = Join-Path $PluginRoot "scripts\resolve_project_paths.py"
    if (-not (Test-Path $script)) { return @() }

    try {
        $paths = @(& $Py $script --root $VaultRoot --format list --collapse --quiet)
    } catch {
        return @()
    }

    $addDirArgs = @()
    foreach ($path in $paths) {
        $trimmed = $path.Trim()
        if ($trimmed -and (Test-Path -LiteralPath $trimmed)) {
            $addDirArgs += "--add-dir"
            $addDirArgs += $trimmed
        }
    }
    return $addDirArgs
}
