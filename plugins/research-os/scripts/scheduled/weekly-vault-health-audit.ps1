<#
Weekly vault-health audit — read-only, never remediates. Registered as a
Windows Scheduled Task ("ResearchOS-WeeklyVaultHealthAudit", weekly, Friday,
before weekly planning). See ../../references/scheduled-agents.md for the
full design rationale. Logs each run under vault/_brain/scheduled-logs/<date>/.

Project directories are granted so the audit can also verify that every
`working_directory:` in _brain/projects/*.md actually resolves — a broken path
there silently blinds every other routine.
#>

. "$PSScriptRoot\_common.ps1"

$LogFile = Get-LogFile -Routine "weekly-vault-health-audit"
$AddDirArgs = Get-ProjectAddDirArgs

$Prompt = @"
Read-only audit. Do not modify any file.

1. Run:
   & "$Py" "$PluginRoot\scripts\wiki_quality_check.py" --root "$VaultRoot"
   (covers every wiki + the _brain/ personal layer) and report the findings
   grouped by wiki and for _brain/ (frontmatter gaps, catalog-invisible project
   notes, stale active projects, duplicates, broken links, index/log staleness).

2. Run:
   & "$Py" "$PluginRoot\scripts\resolve_project_paths.py" --root "$VaultRoot" --format json
   and report any project note that is status: active but has no
   working_directory, or whose working_directory does not resolve on this
   machine. These are reach defects: every other scheduled routine goes blind
   to that project until it is fixed.

3. Also surface any WIKI-PENDING sources.

Do not remediate and do not invoke /wiki-maintain automatically -- this is a
report I act on by hand (via /wiki-maintain for wikis, /checkpoint for project
notes).
"@

Set-Location $VaultRoot
$transcript = & claude -p $Prompt `
  --model sonnet `
  --permission-mode acceptEdits `
  --allowedTools "Read Grep Glob Bash(python*)" `
  @AddDirArgs `
  *>&1 | Out-String

Write-Output $transcript
Save-RoutineTranscript -Path $LogFile -Content $transcript
