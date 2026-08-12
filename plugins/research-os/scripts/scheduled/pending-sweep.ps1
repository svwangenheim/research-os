<#
Pending sweep — READ-ONLY detection. Registered as a Windows Scheduled Task
("ResearchOS-PendingSweep", daily, early evening). See
../../references/scheduled-agents.md for the design rationale.

This routine finds everything waiting across every project — uncommitted work,
unpushed commits, unpushed wiki knowledge — and writes it to
vault/_brain/.pending-actions.yaml. It NEVER acts: mutation happens only through
/pending, which asks once per project and records the answer in
automation-consent.yaml.

There is no `claude` invocation here at all. Detection is pure computation, so
it runs as three deterministic scripts and costs nothing. The reporting half
happens when you run /pending.
#>

. "$PSScriptRoot\_common.ps1"

$LogFile = Get-LogFile -Routine "pending-sweep"

if (-not $Py) {
    $msg = "pending-sweep: no working Python interpreter found; nothing swept."
    Write-Output $msg
    Save-RoutineTranscript -Path $LogFile -Content $msg
    exit 0
}

$transcript = ""

# 1. The queue itself.
$sweep = Join-Path $PluginRoot "scripts\pending_actions.py"
$transcript += (& $Py $sweep --root $VaultRoot 2>&1 | Out-String)

# 2. Keep the weekly plan's generated block and the week dashboard current, so
#    loss risk surfaces in the plan rather than only in this log.
$reconcile = Join-Path $PluginRoot "scripts\reconcile_week.py"
$transcript += (& $Py $reconcile --root $VaultRoot 2>&1 | Out-String)

$dashboard = Join-Path $PluginRoot "scripts\generate_week_dashboard.py"
$transcript += (& $Py $dashboard --root $VaultRoot 2>&1 | Out-String)

# 3. Procedure promotion status — the mechanism that stops proven procedures
#    from being forgotten.
$promotion = Join-Path $PluginRoot "scripts\procedure_promotion_check.py"
$transcript += (& $Py $promotion --root $VaultRoot 2>&1 | Out-String)

Write-Output $transcript
Save-RoutineTranscript -Path $LogFile -Content $transcript
