<#
Weekly review + planning — draft only, never creates calendar events.
Registered as a Windows Scheduled Task ("ResearchOS-WeeklyPlanning", weekly,
Friday). See ../../references/scheduled-agents.md for the full design
rationale. Logs each run under vault/_brain/.scheduled-logs/.
#>

$VaultRoot = "C:\Users\dzsve\research-os\vault"
$LogDir = Join-Path $VaultRoot "_brain\.scheduled-logs\weekly-planning"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$LogFile = Join-Path $LogDir ((Get-Date -Format "yyyy-MM-dd_HHmm") + ".log")

$Prompt = @'
Run /research-os:weekly-planning -- but non-interactively and in draft mode,
since this is an unattended scheduled run and no one is here to answer
questions. Instead of its normal conversational Steps 2-4, infer everything:
read every _brain/daily/*.md from the past 7 days and the most recent
_brain/weekly/*.md (if any), then infer last week's check-off status per
stated goal from git commit activity in the relevant project (label anything
genuinely unclear "unclear -- needs your input" rather than guessing a
confident status). Infer this week's likely goals and open work timeslots
from unresolved threads in the daily notes and any explicit TODOs -- if
nothing concrete surfaces, leave that section for me to fill in by hand
rather than inventing goals. For Step 5 (calendar), if the Microsoft 365
connector is authorized, read the existing calendar and propose blocks
checked against it, but do NOT create them under any circumstances -- leave
every proposed block written into the weekly file for me to confirm by
hand later; if the connector isn't authorized, say so once and skip. Write
the weekly file per its normal format (Step 6), including the Questions for
next week section.
'@

Set-Location $VaultRoot
& claude -p $Prompt `
  --model sonnet `
  --permission-mode acceptEdits `
  --allowedTools "Read Write Edit Grep Glob" `
  *>&1 | Tee-Object -FilePath $LogFile
