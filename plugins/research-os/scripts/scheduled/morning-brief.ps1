<#
Morning brief — read-only. Registered as a Windows Scheduled Task
("ResearchOS-MorningBrief", daily). See ../../references/scheduled-agents.md
for the full design rationale. Logs each run under vault/_brain/scheduled-logs/<date>/.

Project state is gathered by project_state_scan.py BEFORE Claude is invoked, and
handed to it as text. This is deliberate: the project repos live on OneDrive with
Files-On-Demand, where directory traversal is ~20x slower than local (measured
2026-08-11: `git status` 0.7s vs a depth-2 `find` 3.8s for 68 files). The first
reach-fixed brief let the model explore nine roots itself and blocked for 25
minutes on 2.4 seconds of CPU. The scan does the same job in ~9 seconds because
it reads git's index instead of walking the tree.
#>

. "$PSScriptRoot\_common.ps1"

$LogFile = Get-LogFile -Routine "morning-brief"
$AddDirArgs = Get-ProjectAddDirArgs

$ProjectState = "(project scan unavailable -- no Python interpreter found)"
$WeekState = ""
if ($Py) {
    $scan = Join-Path $PluginRoot "scripts\project_state_scan.py"
    $ProjectState = (& $Py $scan --root $VaultRoot --since "1 day ago" 2>&1 | Out-String)

    # Keep the weekly plan and the week dashboard current.
    #
    # Note what is NOT happening here: Claude is not given write access. These
    # two scripts are deterministic and their blast radius is fixed in code --
    # reconcile_week.py can only ever rewrite the region between the
    # `@generated:start week-state` markers, and the dashboard generator only
    # writes week.html. So the routine keeps a structurally read-only
    # --allowedTools list while still leaving a living plan behind, which is
    # strictly safer than granting Write and trusting the prompt.
    $reconcile = Join-Path $PluginRoot "scripts\reconcile_week.py"
    $WeekState = (& $Py $reconcile --root $VaultRoot 2>&1 | Out-String)

    $dashboard = Join-Path $PluginRoot "scripts\generate_week_dashboard.py"
    $WeekState += (& $Py $dashboard --root $VaultRoot 2>&1 | Out-String)
}

$Prompt = @"
Read-only morning brief. Do not modify any file. Do not explore the project
directories yourself -- traversing them is slow enough to hang this run, and the
scan below already contains their real state, taken moments ago.

=== PROJECT STATE (authoritative, pre-scanned) ===
$ProjectState
=== END PROJECT STATE ===

=== WEEK RECONCILE (already done for you) ===
$WeekState
=== END WEEK RECONCILE ===

Using only the scan above plus the _brain/ notes in the working directory,
report in a few tight lines:

1. The single next step per active project. Take the stage from the scan; take
   the substance from that project's _brain/projects/*.md Orientation section.
   A project with no passport.yaml is a BMAD project, not a broken one -- do not
   report that as a defect.
2. Loss risk: anything uncommitted or unpushed, worst first, named with counts.
   Report it; do not act on it.
3. Any due engram spaced-repetition reviews -- read _brain/learning/'s FSRS
   state (learner-model.json, experiments.json, misconceptions.json) and report
   the count due today. Don't run /recall.
4. Today's calendar if the Microsoft 365 connector is authorized. It is
   read-only for this account, so report only -- never attempt to create an
   event. If unauthorized, say so once in a single line and move on.
5. Anything the week reconcile flagged as drift, in one line. The weekly plan
   and `_brain/week.html` have already been refreshed by script before you were
   invoked -- report what that found; do not try to rewrite either yourself.

No writes, no commits, no git push. You have no write tools in this run: the
only mutations in this routine are the two deterministic scripts above, whose
blast radius is fixed in code.
"@

Set-Location $VaultRoot
$transcript = & claude -p $Prompt `
  --model sonnet `
  --permission-mode acceptEdits `
  --allowedTools "Read Grep Glob" `
  @AddDirArgs `
  *>&1 | Out-String

Write-Output $transcript
Save-RoutineTranscript -Path $LogFile -Content $transcript
