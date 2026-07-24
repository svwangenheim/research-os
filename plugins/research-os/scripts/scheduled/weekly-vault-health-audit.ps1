<#
Weekly vault-health audit — read-only, never remediates. Registered as a
Windows Scheduled Task ("ResearchOS-WeeklyVaultHealthAudit", weekly, Friday,
before weekly planning). See ../../references/scheduled-agents.md for the
full design rationale. Logs each run under vault/_brain/.scheduled-logs/.
#>

$VaultRoot = "C:\Users\dzsve\research-os\vault"
$PluginRoot = "C:\Users\dzsve\research-os\plugins\research-os"
$LogDir = Join-Path $VaultRoot "_brain\.scheduled-logs\weekly-vault-health-audit"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$LogFile = Join-Path $LogDir ((Get-Date -Format "yyyy-MM-dd_HHmm") + ".log")

$Prompt = @"
Read-only audit. Run:
python "$PluginRoot\scripts\wiki_quality_check.py" --root "$VaultRoot"
(covers every wiki + the _brain/ personal layer) and report the findings
grouped by wiki and for _brain/ (frontmatter gaps, catalog-invisible project
notes, stale active projects, duplicates, broken links, index/log
staleness). Also surface any WIKI-PENDING sources. Do not remediate and do
not invoke /wiki-maintain automatically -- this is a report I act on by hand
(via /wiki-maintain for wikis, /checkpoint for project notes).
"@

Set-Location $VaultRoot
& claude -p $Prompt `
  --model sonnet `
  --permission-mode acceptEdits `
  --allowedTools "Read Grep Glob Bash(python*)" `
  *>&1 | Tee-Object -FilePath $LogFile
