<#
Weekly literature delta — search + diff, notifies only on genuinely new,
directly-relevant work. Its only write is the seen-list state file it diffs
against. Registered as a Windows Scheduled Task
("ResearchOS-WeeklyLiteratureDelta", weekly, Monday). See
../../references/scheduled-agents.md for the full design rationale. Logs each
run under vault/_brain/scheduled-logs/<date>/. The seen-list is state, not a
per-run transcript, so it lives at a fixed routine-keyed path instead of
moving to a new dated folder every week.

Project directories are granted from vault/_brain/projects/*.md frontmatter via
_common.ps1 — never hardcoded here.
#>

. "$PSScriptRoot\_common.ps1"

$LogFile = Get-LogFile -Routine "weekly-literature-delta"
$AddDirArgs = Get-ProjectAddDirArgs
$SeenFile = Join-Path $VaultRoot "_brain\scheduled-logs\weekly-literature-delta\seen.md"
New-Item -ItemType Directory -Force -Path (Split-Path $SeenFile) | Out-Null

$Prompt = @"
Weekly literature sweep with a delta against what I have already been shown.
The only file you may write is the seen-list at:
$SeenFile
Do not touch any project file, any wiki, any _brain/ note, or bibliography.bib.

Project roots have already been granted to this session with --add-dir; the
authoritative list is the ``working_directory:`` frontmatter field in each
_brain/projects/*.md note (status: active). If a granted directory is
unreachable, say so once and move on.

1. Resolve the watch topics, in this order:
   - _brain/lit-watch.md if it exists -- one topic per line, and it wins.
   - Otherwise, each active project's passport.yaml: research.question,
     research.methodology, and the recurring themes in literature_corpus
     claim_used fields.
   - Plus the registered wiki themes from ~/.claude/vaults.json.
   If nothing resolves, say so in one line and stop. Do not invent topics.

2. Sweep each topic for work that appeared in the last week: NBER and CEPR
   working papers, SSRN and RePEc, arXiv econ, and the field journals listed in
   each project's 00_admin/domain-profile.md. Search; do not answer from memory.
   Record for each hit: title, authors, date, venue, and URL or DOI. Never
   fabricate a citation, a DOI, or a date -- if a field is unverified, mark it
   [UNVERIFIED] rather than filling it in.

3. Diff against what I have already seen:
   - Everything listed in the seen-list from prior runs.
   - Everything already in a project's passport.yaml literature_corpus.
   - Everything already summarized in a wiki's 10_sources/ or 20_summaries/.
   A paper present in any of those is not new, whatever its publication date.

4. Filter the remainder hard for direct relevance. A paper qualifies only if it
   would change something concrete: the identification strategy, the estimator,
   the data source, the positioning of a contribution, or a claim currently in a
   draft. Same-field-adjacent is not relevant. Being recent is not relevant.
   Say why each survivor qualifies, in one sentence naming the project and the
   thing it would change. If you cannot write that sentence, drop the paper.

5. Append every hit you evaluated in step 3 -- kept and dropped alike -- to the
   seen-list as one line each (date, title, first author, venue, verdict), so
   next week does not re-surface it. This is the only write. If the write is
   refused, still report the delta and add one line saying the seen-list was not
   updated, so I know next week's run may repeat itself.

6. Apply the notification rule, which is the point of this routine:
   - If nothing survives step 4, output exactly the single line
     "LIT DELTA: none" and nothing else. No topic list, no counts, no summary of
     what you searched. A weekly digest that always has content is a digest I
     stop reading.
   - Otherwise output a report headed "LIT DELTA: N new" listing, per paper:
     citation, link, the one-sentence relevance statement, the project it
     affects, and the suggested next step (/wiki-ingest for something worth
     keeping, /discover lit for a topic that needs a fuller re-sweep). Nothing
     is ingested automatically -- I decide what enters the corpus.
"@

Set-Location $VaultRoot
$transcript = & claude -p $Prompt `
  --model sonnet `
  --permission-mode acceptEdits `
  --allowedTools "Read Grep Glob WebSearch WebFetch Write(./_brain/scheduled-logs/weekly-literature-delta/seen.md)" `
  @AddDirArgs `
  *>&1 | Out-String

Write-Output $transcript
Save-RoutineTranscript -Path $LogFile -Content $transcript
