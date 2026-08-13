<#
Weekly review + planning — draft only, never creates calendar events.
Registered as a Windows Scheduled Task ("ResearchOS-WeeklyPlanning", weekly,
Friday). See ../../references/scheduled-agents.md for the full design
rationale. Logs each run under vault/_brain/scheduled-logs/<date>/.

Project directories are granted from vault/_brain/projects/*.md frontmatter via
_common.ps1 — never hardcoded here.
#>

. "$PSScriptRoot\_common.ps1"

$LogFile = Get-LogFile -Routine "weekly-planning"
$AddDirArgs = Get-ProjectAddDirArgs

$Prompt = @'
Run /research-os:weekly-planning -- but non-interactively and in draft mode,
since this is an unattended scheduled run and no one is here to answer
questions. Instead of its normal conversational Steps 2-4, infer everything:
read every _brain/daily/*.md from the past 7 days and the most recent
_brain/weekly/*.md (if any), then infer last week's check-off status per stated
goal from git commit activity in the relevant project (label anything genuinely
unclear "unclear -- needs your input" rather than guessing a confident status).

The project roots have already been granted to this session with --add-dir; the
authoritative list is the `working_directory:` frontmatter field in each
_brain/projects/*.md note. Use real git history from those repos as the
evidence base, not inference from the daily notes alone.

Infer this week's likely goals and open work timeslots from unresolved threads
in the daily notes and any explicit TODOs -- if nothing concrete surfaces, leave
that section for me to fill in by hand rather than inventing goals.

Plan at the level of goals plus a weekly hour budget per role (PhD, DZ
modelling, DZ outreach, admin) rather than assigning goals to specific days --
day-level assignment has been repeatedly overtaken by rescheduling while the
goals themselves held.

For Step 5 (calendar), if the Microsoft 365 connector is authorized, read the
existing calendar and propose blocks checked against it, but do NOT create them
under any circumstances -- the connector is read-only for this account anyway
(org policy blocks outlook_create_event), so leave every proposed block written
into the weekly file for me to enter by hand; if the connector isn't authorized,
say so once and skip. When naming categories, use the real Outlook category
names (Work Blocker, Self-imposed Deadline, External Deadline, External
Appointment, Private Appointment, DZ), not colour words.

Write the weekly file per its normal format (Step 6), including the Questions
for next week section.
'@

Set-Location $VaultRoot
$transcript = & claude -p $Prompt `
  --model sonnet `
  --permission-mode acceptEdits `
  --allowedTools "Read Write Edit Grep Glob Bash(git status:*) Bash(git log:*) Bash(git diff:*)" `
  @AddDirArgs `
  *>&1 | Out-String

Write-Output $transcript
Save-RoutineTranscript -Path $LogFile -Content $transcript
