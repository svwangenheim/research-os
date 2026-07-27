---
name: discover
description: Discovery phase combining research interviews, literature search (narrative or PRISMA systematic), data discovery, and ideation. Routes to the appropriate agents based on arguments. First step of the research-os pipeline; writes the research spec into passport.yaml and the literature into the corpus.
argument-hint: "[mode: interview | lit | lit systematic | data | ideate] [topic or query]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash,WebSearch,WebFetch,Task
---

# Discover

Launch the Discovery phase of research. Routes to the appropriate agents based on the mode specified.

**Input:** `$ARGUMENTS` — a mode keyword followed by a topic or query.

State lives in **`passport.yaml`** (schema: `${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml`). Paths follow `${CLAUDE_PLUGIN_ROOT}/rules/folder-map.md` — treat it as the single source of truth. Literature outputs obey `${CLAUDE_PLUGIN_ROOT}/rules/output-discipline.md`: **update the existing review in place; a new file only for a genuinely new question/literature.**

## The two-layer knowledge model

research-os separates the durable knowledge layer from the project:

- **Thematic wikis** (the durable layer) live outside the project. The project's default is its **main wiki**, recorded in `passport.yaml` (`meta.main_wiki`) and `CLAUDE.md`. Resolve any wiki's path via the registry `~/.claude/vaults.json` (theme → path). All registered wikis are readable; the main wiki is just the default. Each wiki has the numbered layout `10_sources/` (PDFs), `20_summaries/` (scored, concept-linked summaries), `30_concepts/`, `40_methods/`, `50_datasets/`.
- **The project** holds only its working slice: project-local PDFs in `01_literature/sources/`, review outputs in `01_literature/reviews/`, and the bridge `wiki-links.md` at the project root that tracks which wiki notes are relevant and their citation status.

If `~/.claude/vaults.json` does not exist yet (knowledge layer not built), fall back to the legacy single-vault pointer `~/.claude/VAULT_PATH` if present; otherwise skip all vault steps silently.

---

## Modes

### Default (no mode specified)
If no mode keyword is given, start with an interactive interview to build the research specification.

### `/discover interview [topic]` — Research Interview
Conduct a structured conversational interview to formalize a research idea.

**This is conversational.** Ask questions directly in your text responses, one or two at a time. Wait for the user to respond before continuing. Do NOT use AskUserQuestion.

**Agents:** Direct conversation (no agent dispatch)
**Output:** `research:` block in `passport.yaml` + `00_admin/research_outline.md` + a domain profile + a decision record

Interview structure:
1. **Big Picture** (1-2 questions): "What phenomenon are you trying to understand?" "Why does this matter?"
2. **Theoretical Motivation** (1-2 questions): "What's your intuition for why X happens?" "What would standard theory predict?"
3. **Data and Setting** (1-2 questions): "What data do you have access to?" "Is there a specific institutional setting?"
4. **Identification** (1-2 questions): "Is there a natural experiment or policy change you can exploit?" "What's the biggest threat to causal interpretation?"
5. **Expected Results** (1-2 questions): "What would you expect to find?" "What would surprise you?"
6. **Contribution** (1 question): "How does this differ from what's been done? What gap are you filling?"

Interview style:
- **Be curious, not prescriptive.** Draw out the researcher's thinking, don't impose your own ideas.
- **Probe weak spots gently.** "What would a skeptic say about...?" not "This won't work because..."
- **Build on answers.** Each question should follow from the previous response.
- **Know when to stop.** If the researcher has a clear vision after 4-5 exchanges, move to the specification.

After interview (5-8 exchanges), produce three outputs:

**Output 1: Research Specification** → update `passport.yaml` `research:` block (question, motivation, hypothesis, paper_type, methodology, contribution, open_questions) **and** write the human-readable brief `00_admin/research_outline.md` (structure below). Do not create a standalone `research_spec_*.md` — the passport is the ledger, the outline is the narrative brief.
```markdown
# Research Specification: [Title]
## Research Question — [one sentence]
## Motivation — [why this matters, theoretical context, policy relevance]
## Hypothesis — [testable prediction with expected direction]
## Empirical Strategy — [method, treatment, control, identifying assumption, robustness]
## Data — [primary dataset, key variables, sample, unit of observation]
## Expected Results — [what the researcher expects and why]
## Contribution — [how this advances the literature]
## Open Questions — [issues needing further thought]
```
Then set `pipeline.stages.discovery.status: in_progress` (and `passed` once the spec is complete).

**Output 2: Domain Profile** → `00_admin/domain-profile.md`
Fill in field, target journals, common data sources, identification strategies, field conventions, seminal references, and referee concerns based on the interview. This file calibrates the librarian, explorer, and referee agents; keep it updated as the project sharpens.

**Output 3: Decision Record** → `00_admin/process/decisions/discovery_[topic].md`
Using `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/decision-record.md`, record:
- **Decision:** The research question chosen
- **Alternatives:** Other angles, framings, or questions that came up during the interview
- **Why rejected:** For each alternative, why this framing was preferred (scope, data availability, novelty, feasibility)
- **Key assumptions:** What must hold for this question to be answerable
- **What would invalidate:** What would force a pivot (e.g., "if the policy change turns out to have been anticipated")

### `/discover lit [topic]` — Literature Review (narrative synthesis)
Search and synthesize academic literature.

**Agents:** Librarian (collector) → librarian-critic (reviewer)
**Output:** Annotated bibliography + BibTeX entries + frontier map, written to `01_literature/reviews/<question-slug>.md`

Workflow:
1. Read `00_admin/domain-profile.md` for field journals and seminal references
2. Check `01_literature/sources/` for project-local papers AND `<main_wiki>/10_sources/` for the wiki corpus (resolve `<main_wiki>` via `~/.claude/vaults.json`). Treat both as a unified corpus — papers already in the wiki do not need to be copied into `01_literature/sources/`.
3. Check `<main_wiki>/20_summaries/` for papers already summarized in the wiki. These have proximity scores and concept links — use them as a head start before searching the web.
4. Read `01_literature/bibliography.bib` for papers already in the project
5. Dispatch Librarian to search:
   - Top-5 journals (AER, Econometrica, QJE, JPE, REStud)
   - Field journals from domain-profile.md
   - NBER/SSRN/IZA working papers
   - **Citation chains** — forward and backward citation tracking from key papers. Follow: (a) backward citations (what do the key papers cite?), and (b) forward citations (who cites the key papers?). This is often the most productive search vector.
6. Assign **proximity scores** to each paper:
   - **1** — Directly competes (same question, similar method)
   - **2** — Closely related (same question, different method or setting)
   - **3** — Related (overlapping topic, different angle)
   - **4** — Background (provides theory, method, or context)
   - **5** — Tangentially related (useful framing only)
7. Dispatch librarian-critic to check coverage, gaps, recency, scope
8. If gaps found, re-dispatch Librarian for targeted search (max 1 round)
9. **Write the review to `01_literature/reviews/<question-slug>.md`, updating in place if it already exists** (per output-discipline.md). Prepend a dated entry to the file's `## Changelog` section describing what changed (e.g. "added 4 sources, revised gap statement"). Create a new review file only if this is a materially distinct literature (a genuinely different question), not a re-run of the same one.
10. Record every paper in `passport.yaml` `literature_corpus` (bibkey, proximity, `citation_status: relevant`, `wiki_path` if summarized — this is the primary source the dashboard reads for the Literature panel; the dashboard resolves authors/title/DOI/abstract live from that `wiki_path` note's frontmatter, so don't duplicate them here, only set `title` as a fallback label for a paper not yet summarized in the wiki). Also refresh the `wiki-links.md` `## Sources` table (inside its `<!-- @generated:start wiki-links-sources -->` markers) with the same rows, so the two stay in sync; do not add papers only as a free-form bullet list, the dashboard's Literature panel won't see them there.
11. Refresh the dashboard: run `/dashboard`.

12. **Wiki sync check** (if a wiki is resolvable): Compare every paper in the bibliography against `<main_wiki>/20_summaries/`. For papers not yet summarized, append a `WIKI-PENDING` block to the review:

```
## WIKI-PENDING — Not yet in the wiki

Run `/wiki-ingest [path]` for each paper to preserve it across projects.

| Paper | File in <main_wiki>/10_sources/ | Action |
|-------|---------------------------------|--------|
| Author (Year), Short Title | [filename.md or — if not yet in the wiki] | /wiki-ingest |
```

If all papers are already in the wiki, print: "All papers already in the wiki — no action needed."
If no wiki is resolvable, skip this step silently.

**Unverified citations:** If you cannot verify a citation, mark the BibTeX entry with `% UNVERIFIED`. Do NOT fabricate or guess citation details. Note when working papers have been published — cite the published version.

Output format for each paper:

```markdown
### [Author (Year)] — [Short Title]
- **Journal:** [venue]
- **Proximity:** [1-5 score]
- **Main contribution:** [1-2 sentences]
- **Identification strategy:** [DiD / IV / RDD / SC / descriptive]
- **Key finding:** [result with effect size]
- **Relevance:** [why it matters for our research]
```

### `/discover lit systematic [topic]` — Systematic Review (PRISMA)
A rigorous evidence-synthesis mode for questions that warrant a defensible, reproducible search rather than a narrative scan (e.g. a standalone literature-review paper, a policy evidence base, or a contested empirical claim). Same agents (Librarian → librarian-critic), but the process and output follow PRISMA.

**Output:** `01_literature/reviews/<question-slug>.md` — **updated in place**, same file as narrative `lit` would use for the same question, upgraded to the PRISMA structure below with a Changelog entry noting the upgrade.

Workflow (PRISMA flow):
1. **Protocol** — state the review question in PICO(S)-style terms (population/intervention/comparison/outcome/setting, adapted to the field), and the inclusion/exclusion criteria, *before* searching.
2. **Search log** — record each database/source queried, the exact query string, the date, and the hit count. Sources: the wiki corpus (`<main_wiki>/10_sources`, `/20_summaries`), Semantic Scholar, OpenAlex, Crossref, arXiv, plus the field journals from the domain profile. Reproducibility is the point — a reader must be able to re-run it.
3. **Screening** — report the counts at each stage (records identified → duplicates removed → title/abstract screened → full-text assessed → included) so a PRISMA flow diagram can be drawn. List excluded full-texts with the exclusion reason.
4. **Risk-of-bias assessment** — for each included study, grade risk of bias with a tool appropriate to the design (e.g. ROBINS-I for observational, RoB 2 for RCTs, or a transparent field-specific rubric). Summarize in a risk-of-bias table.
5. **Synthesis** — synthesize findings across included studies; if the studies are commensurable and the user wants it, run an **optional meta-analysis** (effect sizes + a random-effects pooled estimate + a heterogeneity statistic), clearly flagged as optional and caveated.
6. Dispatch librarian-critic to check the protocol adherence, search completeness, screening consistency, and bias grading.
7. Populate `passport.yaml` `literature_corpus` (as in narrative lit) and refresh `wiki-links.md`; run the same WIKI-PENDING sync check as narrative lit; refresh `/dashboard`.

> `/discover lit systematic` and dz-core's `deep-research` systematic mode cover the same ground — use this one for the in-project literature layer that feeds `passport.claim_manifest`.

### `/discover data [requirements]` — Data Discovery
Find and assess datasets for the research question.

**Agents:** Explorer (finder) → explorer-critic (assessor)
**Output:** Ranked data sources with feasibility grades → `02_data/data-sources.md`

Workflow:
1. Read the `research:` block in `passport.yaml` and the strategy memo (`03_analysis/strategy/`) if it exists
2. Read `00_admin/domain-profile.md` for common data sources in the field
3. Understand what variables are needed: treatment, outcome, controls, time period, geography
4. Dispatch Explorer to search across source categories:
   - Public microdata (CPS, ACS, NHIS, MEPS, etc.)
   - Administrative data (Medicare claims, tax records, court records)
   - Survey data (RAND HRS, PSID, Add Health, NLSY)
   - International (World Bank, OECD, Eurostat)
   - Novel/alternative (satellite imagery, web scraping, proprietary)
5. For each dataset found, report:
   - Name, provider, access level (public/restricted)
   - Key variables available
   - Coverage (time period, geography, sample size)
   - **Feasibility grade:**
     - **A** — Ready to use (public download, documented, standard format)
     - **B** — Accessible with effort (application required, moderate cost, needs cleaning)
     - **C** — Restricted but obtainable (FSRDC, data use agreement, IRB approval)
     - **D** — Very difficult (proprietary, requires partnership, rare access)
   - Strengths and limitations
6. Dispatch explorer-critic to critique each proposed dataset using the **5-point assessment:**
   1. **Measurement validity** — Does the variable actually measure what we need?
   2. **Sample selection** — Who is in the data? Who is missing?
   3. **External validity** — Can we generalize from this sample?
   4. **Identification compatibility** — Does this data support the proposed design?
   5. **Known issues** — Documented problems with this dataset in the literature
7. Save the assessment to `02_data/data-sources.md` (update in place on re-run). Record any externally declared datasets in `passport.yaml` `data_provenance`.

**Rejected datasets:** Include a rejection table:

| Dataset | Reason for Rejection | Deal-breaker? |
|---------|---------------------|---------------|
| [Name]  | [explorer-critic's finding] | [Yes/No] |

### `/discover ideate [topic]` — Research Ideation
Generate structured research questions and hypotheses from a topic or dataset.

**Agents:** Direct generation (no agent dispatch)
**Output:** Research questions with empirical strategies → `explorations/research_ideas_[topic].md`

Generate:
1. 3-5 research questions with clear hypotheses
2. For each: potential identification strategy, data requirements, expected contribution
3. Rank by feasibility and novelty
4. Save to `explorations/research_ideas_[topic].md` (the research sandbox). A chosen idea graduates to the interview + a decision record.

---

## Bundled Resources

| Resource | Path | What It Contains |
|----------|------|-----------------|
| Research spec | `${CLAUDE_PLUGIN_ROOT}/skills/discover/templates/research-spec.md` | 8-section research specification output format |
| Interview flow | `${CLAUDE_PLUGIN_ROOT}/skills/discover/templates/interview-flow.md` | 6-category conversational structure for interview mode |
| Lit review entry | `${CLAUDE_PLUGIN_ROOT}/skills/discover/templates/lit-review-entry.md` | Per-paper annotation format with proximity scoring |
| Data assessment | `${CLAUDE_PLUGIN_ROOT}/skills/discover/templates/data-assessment.md` | Data source evaluation with 5-point critique and feasibility grades |
| Research ideas | `${CLAUDE_PLUGIN_ROOT}/skills/discover/templates/research-ideas.md` | Ideation output format with feasibility/novelty ranking |
| PDF processing | `${CLAUDE_PLUGIN_ROOT}/skills/discover/references/pdf-processing.md` | Safe workflow for reading reference papers |
| Decision record | `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/decision-record.md` | Shared decision-record format (lives in the strategize skill) |
| Gotchas | `${CLAUDE_PLUGIN_ROOT}/skills/discover/gotchas.md` | Known failure points and edge cases |

---

## Principles

- **Interview style:** Be curious, not prescriptive. Draw out the researcher's thinking. Free-form conversation, one or two questions at a time — never AskUserQuestion.
- **State in the passport:** The interview writes the `research:` block; lit modes populate `literature_corpus`; never scatter state into per-step files.
- **Update over create:** Improve the existing `01_literature/reviews/<question-slug>.md` with a Changelog entry. A new review file only for a genuinely new question/literature.
- **Literature honesty:** Never fabricate citations. Mark unverified as `% UNVERIFIED`.
- **Proximity scoring:** Always assign 1-5 proximity scores to papers found.
- **Citation chains:** Forward and backward citation tracking is an explicit search vector — do not skip it.
- **Systematic when it matters:** Use `lit systematic` (PRISMA) when the evidence base must be defensible and reproducible — protocol first, search log, screening counts, risk-of-bias, optional meta-analysis.
- **Effect sizes matter:** Report magnitudes, not just signs. Note identification strategy for every paper.
- **Data feasibility matters:** A perfect dataset you can't access is useless. Always assign A/B/C/D grades and run the 5-point critique.
- **Two-layer aware:** Read the wiki corpus (`<main_wiki>/10_sources`, `/20_summaries`) before searching the web; always run the WIKI-PENDING sync so nothing is lost to future projects; refresh `wiki-links.md`.
- **Domain-profile aware:** Always read `00_admin/domain-profile.md` first for field calibration.
- **Worker-critic pairing:** Librarian + librarian-critic, Explorer + explorer-critic. Never skip the critic.
