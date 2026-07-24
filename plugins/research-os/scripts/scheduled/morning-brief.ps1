<#
Morning brief — read-only. Registered as a Windows Scheduled Task
("ResearchOS-MorningBrief", daily). See ../../references/scheduled-agents.md
for the full design rationale. Logs each run under vault/_brain/.scheduled-logs/.
#>

$VaultRoot = "C:\Users\dzsve\research-os\vault"
$LogDir = Join-Path $VaultRoot "_brain\.scheduled-logs\morning-brief"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$LogFile = Join-Path $LogDir ((Get-Date -Format "yyyy-MM-dd_HHmm") + ".log")

$Prompt = @'
Read-only morning brief. Do not modify any file. Report, in a few lines:
what's pending across my active projects (scan each project's passport.yaml
pipeline.current_stage and open plan items -- discover project paths from
_brain/projects/*.md's Orientation section; if none are recorded yet, say so
and skip this part rather than guessing), the single next step per project,
any due engram spaced-repetition reviews (read _brain/learning/'s FSRS state
-- learner-model.json, experiments.json, misconceptions.json -- and estimate
how many items are due today; just report the count, don't run /recall), and
today's calendar if the Microsoft 365 connector is authorized (skip
gracefully, note once, if not). No writes, no commits, no git push.
'@

Set-Location $VaultRoot
& claude -p $Prompt `
  --model sonnet `
  --permission-mode acceptEdits `
  --allowedTools "Read Grep Glob" `
  *>&1 | Tee-Object -FilePath $LogFile
