<#
Shared wrapper for every scheduled procedure. One script, many Scheduled Tasks
-- each task passes -Name <procedure> as its argument, so adding a new
scheduled procedure never means writing a new .ps1 file.

Registered by scripts/automate_schedule.py from a procedure's own `schedule:`
frontmatter field. See rules/dialogue-triggers.md's sibling doc,
docs/13-the-automation-layer.md, for why a scheduled run uses the exact same
stop semantics as an interactive one: [ai] executes, [human] stops and leaves a
note, [veto] refuses. A scheduled run that tried to guess past a [human] step
would be exactly the "no indication of work" failure mode from 2026-07-27,
inverted -- confident action where there should have been a stop.
#>

param(
    [Parameter(Mandatory = $true)]
    [string]$Name
)

. "$PSScriptRoot\_common.ps1"

$LogFile = Get-LogFile -Routine "automate-$Name"
$AddDirArgs = Get-ProjectAddDirArgs

$PlanText = "(plan unavailable -- no Python interpreter found)"
if ($Py) {
    $runner = Join-Path $PluginRoot "scripts\automate_run.py"
    $PlanText = (& $Py $runner --root $VaultRoot --name $Name 2>&1 | Out-String)
}

$Prompt = @"
Run the procedure '$Name' via /automate run $Name -- this is an unattended
scheduled invocation, so there is no one here to answer a [human] step.

The pre-built execution plan is below. Execute every [ai] step yourself, in
order, exactly as the procedure's Steps describe -- including any [ai] step
that composes a research-os skill or a BMAD workflow named in its `calls:`
list. The moment you reach a [human] or [veto] step (or an unclassified step
the plan below marks as a stop), STOP. Do not guess what the human would say,
do not attempt the step anyway, and do not skip past it. Leave a note in your
final report naming exactly what you stopped on and why.

After you finish (whether you completed every step or stopped early), record
the run:

$Py "$PluginRoot\scripts\automate_run.py" --root "$VaultRoot" --name $Name --record-run --ran-by scheduled --stopped-at <n or omit> --deviations "<anything that differed from the note, or empty>"

=== EXECUTION PLAN (already computed -- do not re-derive it) ===
$PlanText
=== END EXECUTION PLAN ===
"@

Set-Location $VaultRoot
$transcript = & claude -p $Prompt `
  --model sonnet `
  --permission-mode acceptEdits `
  --allowedTools "Read Write Edit Grep Glob Bash(git status:*) Bash(git log:*) Bash(git diff:*) Bash(git add:*) Bash(git commit:*)" `
  @AddDirArgs `
  *>&1 | Out-String

Write-Output $transcript
Save-RoutineTranscript -Path $LogFile -Content $transcript
