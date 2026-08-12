<#
Nightly reproducibility check — read-only, notifies only on FAIL, silent on
PASS and EXPLAINED. Registered as a Windows Scheduled Task
("ResearchOS-NightlyReproCheck", daily). See
../../references/scheduled-agents.md for the full design rationale. Logs each
run under vault/_brain/.scheduled-logs/.

Project directories are granted from vault/_brain/projects/*.md frontmatter via
_common.ps1 — never hardcoded here.
#>

. "$PSScriptRoot\_common.ps1"

$LogFile = Get-LogFile -Routine "nightly-repro-check"
$AddDirArgs = Get-ProjectAddDirArgs

$Prompt = @'
Read-only reproducibility drift check. Do not modify any file, do not commit,
do not push, do not run analysis scripts that write output.

Project roots have already been granted to this session with --add-dir; the
authoritative list is the `working_directory:` frontmatter field in each
_brain/projects/*.md note (status: active). If a granted directory is
unreachable, say so once and move on -- do not guess at its state. A project
without a passport.yaml has no claim manifest; skip it silently.

For each project that has one, re-verify the numeric claims recorded in
passport.yaml's claim_manifest against the artifacts they cite:

1. Resolve each claim's evidence_origin -- analysis:<script>, data:<path>, a
   bibkey in literature_corpus, or reasoning.
2. Compare the claim's recorded value against the number currently present in
   the referenced output (03_analysis/output/, 04_paper/academic_paper/tables/
   and figures/). Apply the tolerances in the plugin's
   skills/analyze/config/replication-tolerances.json -- do not eyeball them.
3. Assign each claim one of: PASS (within tolerance), EXPLAINED (outside
   tolerance, but the manifest or the surrounding notes name a concrete,
   specific alternative specification that accounts for the gap -- a vague or
   blank note is not an explanation and never downgrades a FAIL), FAIL (outside
   tolerance, unexplained), STALE (the referenced artifact is newer than the
   recorded claim), or UNMATCHED (the referenced artifact or number could not be
   located at all).

A mismatch means one of {paper, code} must change. Report it that way and
isolate which. Never conclude that the code should be reverted to match the
paper -- a refactor may have fixed a real bug that the paper still reflects.

Then apply the notification rule, which is the whole point of this routine:

- If every claim across every project is PASS or EXPLAINED, output exactly the
  single line "REPRO OK" and nothing else. No summary, no per-project table, no
  reassurance. A job that reports "all good" every night trains me to stop
  reading it.
- If any claim is FAIL, STALE, or UNMATCHED, output a report headed "REPRO
  DRIFT" listing, per affected project: the claim id and text, its
  evidence_origin, the recorded value, the value found now, the disposition, and
  the specific next step (/peer-review --replicate for a FAIL, /analyze to
  regenerate for a STALE, manual inspection of the cited artifact for an
  UNMATCHED). Put the count of affected claims in the first line so it is
  visible without opening the log.

Do not write the dispositions back into passport.yaml. This routine detects; a
supervised run decides.
'@

Set-Location $VaultRoot
& claude -p $Prompt `
  --model sonnet `
  --permission-mode acceptEdits `
  --allowedTools "Read Grep Glob Bash(git status:*) Bash(git log:*) Bash(git diff:*)" `
  @AddDirArgs `
  *>&1 | Tee-Object -FilePath $LogFile
