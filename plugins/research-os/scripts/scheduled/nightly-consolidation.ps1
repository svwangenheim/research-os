<#
Nightly consolidation — bounded mutation, local commits only, never pushes.
Registered as a Windows Scheduled Task ("ResearchOS-NightlyConsolidation",
daily). See ../../references/scheduled-agents.md for the full design
rationale. Logs each run under vault/_brain/.scheduled-logs/.

Project directories are granted from vault/_brain/projects/*.md frontmatter via
_common.ps1 — never hardcoded here. The allowlist below is the real safety
boundary: it contains no `git push`, so this routine is structurally incapable
of pushing even if it decided to.
#>

. "$PSScriptRoot\_common.ps1"

$LogFile = Get-LogFile -Routine "nightly-consolidation"
$AddDirArgs = Get-ProjectAddDirArgs

$Prompt = @'
Run /research-os:daily-summary -- but non-interactively, since this is an
unattended scheduled run and no one is here to answer questions. Instead of
asking conversationally which projects to summarize (its normal Step 1),
autonomously detect touched projects today: the project roots have already been
granted to this session with --add-dir, and the authoritative list is the
`working_directory:` frontmatter field in each _brain/projects/*.md note
(status: active). Check every one of them for today's-dated commits or
uncommitted changes -- including the vault itself.

Check the WHOLE working tree of each repo, not just the directory you expect
work to be in. A prior run missed a backlog of uncommitted vault content for
three consecutive nights because its git-status check was scoped too narrowly;
that is the specific failure this instruction exists to prevent.

Then proceed through Steps 2-4 without stopping to confirm. Respect the
guardrails exactly: never push or open a PR (commit locally only), never fail
the whole run just because a Slack/M365 connector isn't authorized (skip that
step gracefully, note it once), never touch the thematic wikis, never fabricate
a summary when nothing changed. If a granted directory is unreachable, record
that plainly as a tooling limitation rather than reporting "no work today" --
those two are not the same statement and conflating them has corrupted the
record before.

After Step 4, additionally flag -- don't act on -- any durable knowledge that
looks unpushed (unchecked items in a project's wiki-links.md) and any
contradictions noticed; leave /wiki-push and wiki canonicalization for me.
'@

Set-Location $VaultRoot
$transcript = & claude -p $Prompt `
  --model sonnet `
  --permission-mode acceptEdits `
  --allowedTools "Read Write Edit Grep Glob Bash(git add:*) Bash(git commit:*) Bash(git status:*) Bash(git log:*) Bash(git diff:*)" `
  @AddDirArgs `
  *>&1 | Out-String

Write-Output $transcript
Save-RoutineTranscript -Path $LogFile -Content $transcript
