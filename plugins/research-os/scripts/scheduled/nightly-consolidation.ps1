<#
Nightly consolidation — bounded mutation, local commits only, never pushes.
Registered as a Windows Scheduled Task ("ResearchOS-NightlyConsolidation",
daily). See ../../references/scheduled-agents.md for the full design
rationale. Logs each run under vault/_brain/.scheduled-logs/.
#>

$VaultRoot = "C:\Users\dzsve\research-os\vault"
$LogDir = Join-Path $VaultRoot "_brain\.scheduled-logs\nightly-consolidation"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$LogFile = Join-Path $LogDir ((Get-Date -Format "yyyy-MM-dd_HHmm") + ".log")

$Prompt = @'
Run /research-os:daily-summary -- but non-interactively, since this is an
unattended scheduled run and no one is here to answer questions. Instead of
asking conversationally which projects to summarize (its normal Step 1),
autonomously detect touched projects today: git repos with today's-dated
commits or uncommitted changes, using _brain/projects/*.md's Orientation
section to find known project paths (skip gracefully and say so if none are
recorded yet). Then proceed through its Steps 2-4 without stopping to
confirm. Still respect its guardrails exactly: never push or open a PR
(commit locally only), never fail the whole run just because a Slack/M365
connector isn't authorized (skip that step gracefully, note it once), never
touch the thematic wikis, never fabricate a summary when nothing changed.
After Step 4, additionally flag -- don't act on -- any durable knowledge
that looks unpushed (unchecked items in a project's wiki-links.md) and any
contradictions noticed; leave /wiki-push and wiki canonicalization for me.
'@

Set-Location $VaultRoot
& claude -p $Prompt `
  --model sonnet `
  --permission-mode acceptEdits `
  --allowedTools "Read Write Edit Grep Glob Bash(git add:*) Bash(git commit:*) Bash(git status:*) Bash(git log:*) Bash(git diff:*)" `
  *>&1 | Tee-Object -FilePath $LogFile
