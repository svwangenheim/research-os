#!/usr/bin/env python3
"""
Generate a self-contained HTML project dashboard for a research-os project.

Scans the numbered project layout and passport.yaml — the state ledger — and
renders the single living overview `project_dashboard.html` at the project root.

Paths follow rules/folder-map.md; state follows templates/passport.yaml. The
literature citation-status panel is built from passport.yaml `literature_corpus`
cross-referenced with `wiki-links.md`. See rules/html-dashboard.md and the
/dashboard skill for the full specification.

Usage:
    python3 scripts/generate_dashboard.py [--project-root .] [--output project_dashboard.html]
"""

import argparse
import json
import os
import re
import subprocess
from datetime import datetime
from html import escape
from pathlib import Path

# The single output folder lives under 04_paper/academic_paper/ (see folder-map.md).
OUTPUT_TYPES = ["academic_paper"]


def find_project_root(start=None):
    p = Path(start or os.getcwd()).resolve()
    while p != p.parent:
        if (p / "passport.yaml").exists() or (p / "CLAUDE.md").exists():
            return p
        p = p.parent
    return Path(start or os.getcwd()).resolve()


# ---------- Passport loader ----------

def load_passport(root):
    """Load passport.yaml. Prefers PyYAML; falls back to a targeted line parser
    for the fields the dashboard needs (meta, pipeline, literature_corpus,
    sessions, integrity, research)."""
    pf = root / "passport.yaml"
    if not pf.exists():
        return {}
    text = pf.read_text(errors="replace")
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(text)
        return data if isinstance(data, dict) else {}
    except Exception:
        return _fallback_passport(text)


def _fallback_passport(text):
    """Minimal, defensive parser for the passport's regular structure.
    Handles top-level scalars/sections, inline flow maps under pipeline.stages,
    and simple block lists of mappings (literature_corpus, sessions)."""
    data = {"meta": {}, "research": {}, "pipeline": {"stages": {}},
            "literature_corpus": [], "sessions": [], "integrity": {}}

    def scalar(v):
        v = v.strip()
        if v in ("null", "~", ""):
            return None
        if v in ("[]", "{}"):
            return []
        if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
            return v[1:-1]
        if re.fullmatch(r"-?\d+", v):
            return int(v)
        return v

    # Top-level scalars under meta:
    m = re.search(r"^meta:\s*$(.*?)(?=^\S|\Z)", text, re.MULTILINE | re.DOTALL)
    if m:
        for line in m.group(1).split("\n"):
            km = re.match(r"\s{2}(\w+):\s*(.*)", line)
            if km:
                data["meta"][km.group(1)] = scalar(km.group(2).split("#")[0])

    # pipeline.current_stage
    cs = re.search(r"^\s{2}current_stage:\s*(.*)", text, re.MULTILINE)
    if cs:
        data["pipeline"]["current_stage"] = scalar(cs.group(1).split("#")[0])

    # pipeline.stages.<name>: { status: "...", score: ..., gate: ... }
    for sm in re.finditer(r"^\s{4}(\w+):\s*\{([^}]*)\}", text, re.MULTILINE):
        name = sm.group(1)
        body = sm.group(2)
        stage = {}
        for kv in re.finditer(r"(\w+):\s*([^,]+)", body):
            stage[kv.group(1)] = scalar(kv.group(2))
        data["pipeline"]["stages"][name] = stage

    # Block lists of mappings: literature_corpus, sessions
    for key in ("literature_corpus", "sessions"):
        lm = re.search(rf"^{key}:\s*(\[\])?\s*$(.*?)(?=^\S|\Z)", text, re.MULTILINE | re.DOTALL)
        if not lm or lm.group(1) == "[]":
            continue
        items = []
        current = None
        for line in lm.group(2).split("\n"):
            im = re.match(r"\s+-\s+(\w+):\s*(.*)", line)
            km = re.match(r"\s+(\w+):\s*(.*)", line)
            if im:
                if current:
                    items.append(current)
                current = {im.group(1): scalar(im.group(2).split(" #")[0])}
            elif km and current is not None:
                current[km.group(1)] = scalar(km.group(2).split(" #")[0])
        if current:
            items.append(current)
        data[key] = items

    return data


# ---------- Scanners (numbered scheme) ----------

def scan_metadata(root, passport):
    """Project metadata from passport.meta first, CLAUDE.md as fallback."""
    meta = {"title": "", "slug": "", "main_wiki": "", "field": ""}
    pm = passport.get("meta", {}) if passport else {}
    meta["title"] = pm.get("name") or ""
    meta["slug"] = pm.get("slug") or ""
    meta["main_wiki"] = pm.get("main_wiki") or ""

    claude_md = root / "CLAUDE.md"
    if claude_md.exists():
        text = claude_md.read_text(errors="replace")
        if not meta["title"]:
            mt = re.search(r"\*\*Project:\*\*\s*(.+)", text)
            if mt:
                meta["title"] = mt.group(1).strip().strip("[]")
        mf = re.search(r"\*\*Field:\*\*\s*(.+)", text)
        if mf:
            meta["field"] = mf.group(1).strip().strip("[]")
    return meta


def _active_outputs(root, meta):
    """The single academic_paper output folder, if it exists under 04_paper/."""
    return ["academic_paper"] if (root / "04_paper" / "academic_paper").is_dir() else []


def scan_sections(root, meta):
    """Paper sections in 04_paper/academic_paper/."""
    sections = []
    for out in _active_outputs(root, meta):
        pdir = root / "04_paper" / out
        seen = set()
        main_tex = pdir / "main.tex"
        if main_tex.exists():
            text = main_tex.read_text(errors="replace")
            for m in re.finditer(r"\\input\{([^}]+)\}", text):
                path_str = m.group(1)
                if not path_str.endswith(".tex"):
                    path_str += ".tex"
                sec_path = pdir / path_str
                if sec_path.exists():
                    wc = len(re.findall(r"\b\w+\b", sec_path.read_text(errors="replace")))
                    mtime = datetime.fromtimestamp(sec_path.stat().st_mtime).strftime("%Y-%m-%d")
                    sections.append({"name": f"{out}: {sec_path.stem.replace('_', ' ').title()}",
                                     "file": f"04_paper/{out}/{path_str}", "words": wc, "modified": mtime})
                    seen.add(sec_path.name)
        sec_dir = pdir / "sections"
        if sec_dir.is_dir():
            for f in sorted(sec_dir.glob("*.tex")):
                if f.name in seen:
                    continue
                wc = len(re.findall(r"\b\w+\b", f.read_text(errors="replace")))
                mtime = datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d")
                sections.append({"name": f"{out}: {f.stem.replace('_', ' ').title()}",
                                 "file": f"04_paper/{out}/sections/{f.name}", "words": wc, "modified": mtime})
    return sections


def scan_data(root):
    """02_data/raw and 02_data/cleaned."""
    inventory = {"raw": [], "cleaned": []}
    for sub in ["raw", "cleaned"]:
        d = root / "02_data" / sub
        if d.is_dir():
            for f in sorted(d.rglob("*")):
                if f.is_file() and f.name != ".gitkeep":
                    size_kb = f.stat().st_size / 1024
                    inventory[sub].append({
                        "name": f.name,
                        "size": f"{size_kb:.0f} KB" if size_kb < 1024 else f"{size_kb/1024:.1f} MB",
                        "modified": datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d"),
                    })
    return inventory


def scan_scripts(root):
    """Analysis scripts in 03_analysis/scripts/{R,py,jl}. Excludes generators."""
    scripts = []
    script_dir = root / "03_analysis" / "scripts"
    if not script_dir.is_dir():
        return scripts
    exts = {".R": "R", ".r": "R", ".py": "Python", ".jl": "Julia"}
    skip_names = {"generate_dashboard.py", "generate_html_report.py"}
    for f in sorted(script_dir.rglob("*")):
        if f.is_file() and f.suffix in exts and f.name not in skip_names:
            lang = exts[f.suffix]
            rel = str(f.relative_to(root)).replace("\\", "/")
            lines = f.read_text(errors="replace").split("\n")
            purpose = ""
            for line in lines[:15]:
                stripped = line.strip()
                if stripped.startswith('"""') or stripped.startswith("'''"):
                    continue
                cleaned = stripped.lstrip("#").lstrip("//").lstrip("'").lstrip('"').strip()
                if cleaned and not cleaned.startswith("!") and not cleaned.startswith("library") \
                   and not cleaned.startswith("import") and not cleaned.startswith("env ") \
                   and not cleaned.startswith("usr/") and len(cleaned) > 5:
                    purpose = cleaned[:80]
                    break
            scripts.append({"name": f.name, "path": rel, "lang": lang, "purpose": purpose})
    return scripts


def scan_results(root):
    """Current results: figures/tables in 03_analysis/output/ + results_summary.md."""
    out_dir = root / "03_analysis" / "output"
    result = {"figures": [], "tables": [], "summary": ""}
    if out_dir.is_dir():
        for f in sorted(out_dir.rglob("*")):
            if not f.is_file() or f.name == ".gitkeep":
                continue
            if f.name.lower() == "results_summary.md":
                result["summary"] = f.read_text(errors="replace").strip()[:1200]
                continue
            mtime = datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d")
            entry = {"name": f.name, "modified": mtime}
            if f.suffix.lower() in (".pdf", ".png", ".svg", ".jpg", ".jpeg", ".eps"):
                result["figures"].append(entry)
            elif f.suffix.lower() in (".tex", ".csv", ".txt", ".md"):
                result["tables"].append(entry)
    return result


def scan_figures_tables(root, meta):
    """Count paper figures and tables across selected outputs + analysis output."""
    n_figs = 0
    n_tabs = 0
    for out in _active_outputs(root, meta):
        fdir = root / "04_paper" / out / "figures"
        tdir = root / "04_paper" / out / "tables"
        if fdir.is_dir():
            n_figs += len([f for f in fdir.glob("*") if f.is_file() and f.name != ".gitkeep"])
        if tdir.is_dir():
            n_tabs += len([t for t in tdir.glob("*.tex") if t.name != ".gitkeep"])
    return n_figs, n_tabs


def scan_bibliography(root):
    """Count entries in 01_literature/bibliography.bib."""
    bib = root / "01_literature" / "bibliography.bib"
    if not bib.exists():
        return 0
    return len(re.findall(r"@\w+\{", bib.read_text(errors="replace")))


def scan_literature_citation_status(root, passport):
    """Build cited / intended / relevant-not-cited buckets.

    Primary source: passport.yaml literature_corpus (structured). Supplemented
    by the wiki-links.md Sources table when the corpus is sparse. Deduped by bibkey.
    """
    buckets = {"cited": [], "intended": [], "relevant": []}
    seen = set()

    def add(bibkey, title, proximity, status, wiki):
        key = (bibkey or title or "").lower()
        if not key or key in seen:
            return
        status = (status or "relevant").strip().lower()
        if status not in buckets:
            status = "relevant"
        seen.add(key)
        buckets[status].append({
            "bibkey": bibkey or "", "title": title or "",
            "proximity": proximity, "wiki": bool(wiki),
        })

    for item in (passport.get("literature_corpus") or []):
        if not isinstance(item, dict):
            continue
        add(item.get("bibkey"), item.get("title"), item.get("proximity"),
            item.get("citation_status"), item.get("wiki_path"))

    # wiki-links.md Sources table (supplement / fallback)
    wl = root / "wiki-links.md"
    if wl.exists():
        text = wl.read_text(errors="replace")
        sec = re.search(r"##\s*Sources.*?\n(.*?)(?=\n##\s|\Z)", text, re.DOTALL)
        if sec:
            for line in sec.group(1).split("\n"):
                if "|" not in line or "---" in line:
                    continue
                cols = [c.strip() for c in line.split("|")]
                cols = [c for c in cols if c != ""]
                if len(cols) < 4:
                    continue
                if cols[0].lower().startswith("bibkey") or cols[0].startswith("<"):
                    continue
                bibkey = cols[0].strip("`")
                short = cols[1]
                prox = None
                pm = re.search(r"\d", cols[2])
                if pm:
                    prox = int(pm.group(0))
                status = cols[3]
                wiki = len(cols) >= 5 and bool(cols[4]) and not cols[4].startswith("<")
                add(bibkey, short, prox, status, wiki)

    return buckets


def scan_reviews(root):
    """Review + integrity reports in 04_paper/reviews/, plus journal/session logs."""
    reviews = []
    rev_dir = root / "04_paper" / "reviews"
    if rev_dir.is_dir():
        for f in sorted(rev_dir.rglob("*.md"), key=lambda x: x.stat().st_mtime, reverse=True):
            if f.name == ".gitkeep":
                continue
            text = f.read_text(errors="replace")
            report_type = "review"
            score = None
            verdict = ""
            fname = f.name.lower()
            if "referee" in fname:
                report_type = "peer-review"
                m = re.search(r"\*\*Overall Score:\*\*\s*(\d+)", text)
                if m:
                    score = int(m.group(1))
                m = re.search(r"\*\*Recommendation:\*\*\s*(.+)", text)
                if m:
                    verdict = m.group(1).strip()
            elif "editorial" in fname:
                report_type = "editorial"
                m = re.search(r"\*\*Decision:\*\*\s*(.+)", text)
                if m:
                    verdict = m.group(1).strip()
            elif "verification" in fname or "integrity" in fname:
                report_type = "integrity"
            reviews.append({
                "file": str(f.relative_to(root)).replace("\\", "/"),
                "name": f.stem.replace("_", " ").replace("-", " ").title(),
                "type": report_type,
                "date": datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d"),
                "score": score, "verdict": verdict,
            })
    # journal
    journal = root / "00_admin" / "process" / "journal.md"
    if journal.exists():
        for m in re.finditer(r"^###\s+(\d{4}-\d{2}-\d{2}[^\n]*)\n(.*?)(?=^###\s|\Z)",
                             journal.read_text(errors="replace"), re.MULTILINE | re.DOTALL):
            head = m.group(1)
            body = m.group(2)
            verdict = ""
            vm = re.search(r"\*\*Verdict:\*\*\s*(.+)", body)
            if vm:
                verdict = vm.group(1).strip()
            date_m = re.match(r"(\d{4}-\d{2}-\d{2})", head)
            reviews.append({
                "file": "00_admin/process/journal.md",
                "name": head.split("—")[-1].strip() if "—" in head else head,
                "type": "journal",
                "date": date_m.group(1) if date_m else "",
                "score": None, "verdict": verdict,
            })
    return reviews


def scan_plans(root):
    """Active plans in 00_admin/process/plans/."""
    plans = []
    plan_dir = root / "00_admin" / "process" / "plans"
    if not plan_dir.is_dir():
        return plans
    for f in sorted(plan_dir.glob("*.md"), reverse=True):
        text = f.read_text(errors="replace")
        status = "DRAFT"
        m = re.search(r"\*\*Status:\*\*\s*(\w+)", text)
        if m:
            status = m.group(1)
        if status.upper() != "COMPLETED":
            plans.append({
                "name": f.stem.replace("_", " ").replace("-", " ").title(),
                "file": str(f.relative_to(root)).replace("\\", "/"),
                "status": status,
                "date": datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d"),
            })
    return plans[:5]


def get_git_activity(root):
    try:
        result = subprocess.run(
            ["git", "log", "--oneline", "-15", "--format=%h|%ai|%s"],
            capture_output=True, text=True, cwd=root, timeout=5,
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if "|" in line:
                parts = line.split("|", 2)
                if len(parts) == 3:
                    commits.append({"hash": parts[0], "date": parts[1][:10], "message": parts[2]})
        return commits
    except Exception:
        return []


# ---------- HTML helpers ----------

def is_placeholder(text):
    return not text or text.startswith("[") or text.startswith("<") or text.startswith("YOUR")


def score_color(score):
    if score is None:
        return "var(--g500)"
    if score >= 90:
        return "var(--accept)"
    if score >= 80:
        return "var(--minor-rev)"
    if score >= 65:
        return "var(--major-rev)"
    return "var(--reject)"


def score_pill_class(score):
    if score is None:
        return "pill-neutral"
    if score >= 90:
        return "pill-accept"
    if score >= 80:
        return "pill-minor"
    if score >= 65:
        return "pill-major"
    return "pill-reject"


def status_pill_class(status):
    s = (status or "").upper()
    if s in ("PASS", "PASSED", "ACCEPT", "ACCEPTED", "COMPLETED", "DONE"):
        return "pill-pass"
    if s in ("WARN", "MINOR", "IN PROGRESS", "IN_PROGRESS", "DRAFT", "PENDING"):
        return "pill-warn"
    if s in ("FAIL", "REJECT", "BLOCKED", "MAJOR"):
        return "pill-fail"
    return "pill-neutral"


def lang_pill_class(lang):
    return {"R": "pill-r", "Python": "pill-python", "Julia": "pill-julia"}.get(lang, "pill-neutral")


def type_pill_class(t):
    return {"peer-review": "pill-accent", "editorial": "pill-accent",
            "integrity": "pill-r", "journal": "pill-neutral"}.get(t, "pill-neutral")


# ---------- Panel builders ----------

def build_header(meta, stats, stage):
    title = escape(meta["title"]) if not is_placeholder(meta["title"]) else "Research Project"
    field = escape(meta["field"]) if not is_placeholder(meta.get("field", "")) else ""
    wiki = escape(meta.get("main_wiki", "")) if not is_placeholder(meta.get("main_wiki", "")) else ""

    stage_pill = ""
    if stage:
        stage_pill = f'<span class="pill pill-accent">stage: {escape(str(stage))}</span> '
    if wiki:
        stage_pill += f'<span class="pill pill-neutral">wiki: {wiki}</span> '

    stats_html = ""
    for label, val in stats:
        stats_html += f"""
      <div class="stat-card">
        <div class="stat-number">{val}</div>
        <div class="stat-label">{escape(label)}</div>
      </div>"""

    subtitle = field
    return f"""
    <header style="padding-bottom:24px;border-bottom:1.5px solid var(--g300);margin-bottom:8px">
      <div class="eyebrow">Project Dashboard</div>
      <div class="flex-between" style="align-items:flex-start">
        <div>
          <h1>{title}</h1>
          {"<p style='color:var(--g500);font-size:14px;margin-top:4px'>" + subtitle + "</p>" if subtitle else ""}
        </div>
        <div class="toolbar">
          <button class="toolbar-btn" id="dark-toggle">Dark</button>
          <button class="toolbar-btn" id="print-btn">Print</button>
        </div>
      </div>
      {('<div style="margin-top:12px">' + stage_pill + '</div>') if stage_pill else ''}
      <div class="stats-row">{stats_html}</div>
    </header>"""


def build_nav():
    links = [
        ("data", "Data"), ("literature", "Literature"), ("analysis", "Analysis"),
        ("results", "Results"), ("paper", "Paper"), ("quality", "Quality"),
        ("history", "History"), ("plans", "Plans"),
    ]
    items = "".join(f'<a class="nav-link" href="#{k}">{v}</a>' for k, v in links)
    return f'<nav class="nav-bar">{items}</nav>'


def build_data_panel(data):
    has = data["raw"] or data["cleaned"]
    if not has:
        return """
    <section id="data">
      <h2>Data</h2>
      <div class="empty-state">No data files yet. Add datasets to <code>02_data/raw/</code> or <code>02_data/cleaned/</code>.</div>
    </section>"""
    rows = ""
    for sub, files in [("raw", data["raw"]), ("cleaned", data["cleaned"])]:
        for f in files:
            rows += f"""
        <tr>
          <td><span class="pill pill-neutral" style="font-size:9px">{sub}</span> &nbsp;{escape(f['name'])}</td>
          <td class="text-right"><span class="mono" style="font-size:12px">{f['size']}</span></td>
          <td class="text-right" style="color:var(--g500);font-size:12px">{f['modified']}</td>
        </tr>"""
    total = len(data["raw"]) + len(data["cleaned"])
    return f"""
    <section id="data">
      <h2>Data</h2>
      <p style="color:var(--g500);font-size:13px">{len(data['raw'])} raw, {len(data['cleaned'])} cleaned &mdash; {total} files</p>
      <table class="report-table">
        <thead><tr><th>File</th><th class="text-right">Size</th><th class="text-right">Modified</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </section>"""


def _paper_row(p):
    prox = p.get("proximity")
    prox_s = f"Prox {prox}" if prox is not None else "Prox —"
    wiki = ' <span class="pill pill-pass" style="font-size:9px">in wiki</span>' if p.get("wiki") else ""
    label = escape(p["bibkey"] or p["title"])
    title = escape(p["title"]) if p["title"] and p["title"] != p["bibkey"] else ""
    return (f'<tr><td style="font-weight:500;color:var(--slate)">{label}</td>'
            f'<td style="color:var(--g700);font-size:12.5px">{title}</td>'
            f'<td><span class="pill pill-neutral" style="font-size:10px">{prox_s}</span>{wiki}</td></tr>')


def build_literature_panel(buckets):
    n_cited = len(buckets["cited"])
    n_intended = len(buckets["intended"])
    n_relevant = len(buckets["relevant"])
    total = n_cited + n_intended + n_relevant
    if total == 0:
        return """
    <section id="literature">
      <h2>Literature</h2>
      <div class="empty-state">No literature recorded yet. Run <code>/discover lit [topic]</code> — it populates
        <code>passport.yaml</code> <code>literature_corpus</code> and <code>wiki-links.md</code>.</div>
    </section>"""

    def block(title, cls, items, note):
        if not items:
            body = '<p style="color:var(--g500);font-size:13px;font-style:italic">None.</p>'
        else:
            rows = "".join(_paper_row(p) for p in sorted(
                items, key=lambda x: (x.get("proximity") or 9)))
            body = f'<table class="report-table"><thead><tr><th>Cite</th><th>Title</th><th>Proximity</th></tr></thead><tbody>{rows}</tbody></table>'
        return f"""
      <h3 id="lit-{cls}">{title} &nbsp;<span class="pill {status_pill_class('PASS' if cls=='cited' else 'WARN' if cls=='intended' else 'NEUTRAL')}">{len(items)}</span></h3>
      <p style="color:var(--g500);font-size:12.5px;margin:0 0 8px">{note}</p>
      {body}"""

    return f"""
    <section id="literature">
      <h2>Literature &nbsp;<span style="font-family:var(--mono);font-size:13px;color:var(--g500);font-weight:400">{n_cited} cited &middot; {n_intended} intended &middot; {n_relevant} relevant-not-cited</span></h2>
      <nav class="section-nav">
        <a href="#lit-cited">Cited</a><a href="#lit-intended">Intended</a><a href="#lit-relevant">Relevant</a>
      </nav>
      {block("Cited", "cited", buckets["cited"], "Actually \\cite{}d in a paper section.")}
      {block("Intended to cite", "intended", buckets["intended"], "Planned for citation but not yet in the draft — the citation to-do list.")}
      {block("Relevant, not cited", "relevant", buckets["relevant"], "In the corpus/wiki and relevant, but not (yet) planned for citation. A proximity 1–2 paper here is a coverage flag.")}
    </section>"""


def build_analysis_panel(scripts_list, results):
    has = scripts_list or results["summary"]
    if not has:
        return """
    <section id="analysis">
      <h2>Analysis</h2>
      <div class="empty-state">No analysis yet. Add scripts to <code>03_analysis/scripts/{R,py,jl}/</code>.</div>
    </section>"""
    rows = ""
    for s in scripts_list:
        lcls = lang_pill_class(s["lang"])
        purpose = escape(s["purpose"]) if s["purpose"] and '"""' not in s["purpose"] else ""
        rows += f"""
        <tr>
          <td style="font-weight:500;color:var(--slate)">{escape(s['name'])}</td>
          <td><span class="pill {lcls}">{s['lang']}</span></td>
          <td style="color:var(--g700);font-size:13px">{purpose}</td>
        </tr>"""
    scripts_html = ""
    if scripts_list:
        langs = ", ".join(sorted({s["lang"] for s in scripts_list}))
        scripts_html = f"""
      <h3 id="analysis-scripts">Scripts &nbsp;<span style="font-family:var(--mono);font-size:12px;color:var(--g500)">{len(scripts_list)} &middot; {langs}</span></h3>
      <table class="report-table"><thead><tr><th>Script</th><th>Lang</th><th>Purpose</th></tr></thead><tbody>{rows}</tbody></table>"""
    done_html = ""
    if results["summary"]:
        done_html = f"""
      <h3 id="analysis-done">Analysis done</h3>
      <div class="card" style="font-size:13px;color:var(--g700);white-space:pre-wrap">{escape(results['summary'])}</div>"""
    return f"""
    <section id="analysis">
      <h2>Analysis</h2>
      {scripts_html}
      {done_html}
    </section>"""


def build_results_panel(results):
    n = len(results["figures"]) + len(results["tables"])
    if n == 0:
        return """
    <section id="results">
      <h2>Results</h2>
      <div class="empty-state">No results yet. This populates when estimation writes figures/tables to <code>03_analysis/output/</code>.</div>
    </section>"""
    rows = ""
    for kind, items in [("figure", results["figures"]), ("table", results["tables"])]:
        for f in items:
            rows += f"""
        <tr><td><span class="pill pill-neutral" style="font-size:9px">{kind}</span> &nbsp;{escape(f['name'])}</td>
          <td class="text-right" style="color:var(--g500);font-size:12px">{f['modified']}</td></tr>"""
    return f"""
    <section id="results">
      <h2>Results &nbsp;<span style="font-family:var(--mono);font-size:13px;color:var(--g500);font-weight:400">{len(results['figures'])} figures &middot; {len(results['tables'])} tables</span></h2>
      <table class="report-table"><thead><tr><th>Output</th><th class="text-right">Modified</th></tr></thead><tbody>{rows}</tbody></table>
    </section>"""


def build_paper_panel(sections, n_figs, n_tabs):
    if not sections:
        return f"""
    <section id="paper">
      <h2>Paper</h2>
      <div class="empty-state">No paper sections yet. Sections live under <code>04_paper/&lt;output&gt;/sections/</code>. ({n_figs} figures, {n_tabs} tables staged.)</div>
    </section>"""
    total_words = sum(s["words"] for s in sections)
    rows = ""
    for s in sections:
        rows += f"""
        <tr>
          <td style="font-family:var(--serif);font-weight:500;color:var(--slate)">{escape(s['name'])}</td>
          <td><span class="mono" style="font-size:11px;color:var(--g500)">{escape(s['file'])}</span></td>
          <td class="text-right"><span class="mono">{s['words']:,}</span></td>
          <td class="text-right" style="color:var(--g500);font-size:12px">{s['modified']}</td>
        </tr>"""
    return f"""
    <section id="paper">
      <h2>Paper &nbsp;<span style="font-family:var(--mono);font-size:13px;color:var(--g500);font-weight:400">{len(sections)} sections &middot; {total_words:,} words &middot; {n_figs} figs &middot; {n_tabs} tables</span></h2>
      <table class="report-table">
        <thead><tr><th>Section</th><th>File</th><th class="text-right">Words</th><th class="text-right">Modified</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </section>"""


def build_quality_panel(passport):
    stages = ((passport.get("pipeline") or {}).get("stages") or {})
    if not stages:
        return """
    <section id="quality">
      <h2>Quality</h2>
      <div class="empty-state">No pipeline scores yet. Stages are scored in <code>passport.yaml</code> <code>pipeline.stages</code>.</div>
    </section>"""
    order = ["discovery", "strategy", "analysis", "writing", "review", "revision", "submission"]
    cards = '<div class="grid-2">'
    for name in [s for s in order if s in stages] + [s for s in stages if s not in order]:
        st = stages[name] or {}
        score = st.get("score")
        status = st.get("status", "")
        gate = st.get("gate")
        scls = score_pill_class(score) if score is not None else status_pill_class(status)
        badge = f"{score}" if score is not None else escape(str(status))
        color = score_color(score)
        pct = score if isinstance(score, (int, float)) else 0
        gate_s = f"gate {gate}" if gate is not None else ""
        cards += f"""
      <div class="card" style="margin-bottom:0">
        <div class="flex-between" style="margin-bottom:8px">
          <span style="font-family:var(--serif);font-weight:500;color:var(--slate);font-size:14px">{escape(name.title())}</span>
          <span class="pill {scls}">{badge}</span>
        </div>
        <div class="score-bar-track"><div class="score-bar-fill" style="width:{pct}%;background:{color}"></div></div>
        <div style="font-family:var(--mono);font-size:11px;color:var(--g500);margin-top:6px">{escape(str(status))} &middot; {gate_s}</div>
      </div>"""
    cards += "</div>"
    return f"""
    <section id="quality">
      <h2>Quality Scorecard</h2>
      {cards}
    </section>"""


def build_history_panel(reviews):
    if not reviews:
        return """
    <section id="history">
      <h2>History</h2>
      <div class="empty-state">No reviews or journal entries yet.</div>
    </section>"""
    items = ""
    for r in reviews[:20]:
        tcls = type_pill_class(r["type"])
        score_str = ""
        if r["score"] is not None:
            score_str = f' <span class="pill {score_pill_class(r["score"])}">{r["score"]}</span>'
        verdict_str = f' <span style="color:var(--g500);font-size:12px">&mdash; {escape(r["verdict"])}</span>' if r["verdict"] else ""
        title_html = f'<a href="{escape(r["file"])}" style="color:var(--slate);text-decoration:none">{escape(r["name"])}</a>' if r.get("file") else escape(r["name"])
        items += f"""
      <div class="timeline-item">
        <div class="timeline-date">{r['date']}</div>
        <div class="timeline-title">{title_html}</div>
        <div><span class="pill {tcls}">{escape(r['type'].replace('-', ' ').title())}</span>{score_str}{verdict_str}</div>
      </div>"""
    return f"""
    <section id="history">
      <h2>History &nbsp;<span style="font-family:var(--mono);font-size:13px;color:var(--g500);font-weight:400">{len(reviews)} entries</span></h2>
      <div class="timeline">{items}</div>
    </section>"""


def build_plans_panel(plans):
    if not plans:
        return """
    <section id="plans">
      <h2>Plans</h2>
      <div class="empty-state">No active plans. Run <code>/strategize</code> or enter plan mode.</div>
    </section>"""
    cards = ""
    for p in plans:
        scls = status_pill_class(p["status"])
        cards += f"""
      <div class="card">
        <div class="flex-between" style="margin-bottom:4px">
          <span style="font-family:var(--serif);font-weight:500;color:var(--slate);font-size:15px">{escape(p['name'])}</span>
          <span class="pill {scls}">{escape(p['status'])}</span>
        </div>
        <div style="font-family:var(--mono);font-size:11px;color:var(--g500)">{p['date']} &middot; {escape(p['file'])}</div>
      </div>"""
    return f"""
    <section id="plans">
      <h2>Active Plans &nbsp;<span style="font-family:var(--mono);font-size:13px;color:var(--g500);font-weight:400">{len(plans)}</span></h2>
      {cards}
    </section>"""


def build_dashboard(root):
    passport = load_passport(root)
    meta = scan_metadata(root, passport)
    data = scan_data(root)
    scripts_list = scan_scripts(root)
    results = scan_results(root)
    sections = scan_sections(root, meta)
    n_figs, n_tabs = scan_figures_tables(root, meta)
    n_bib = scan_bibliography(root)
    buckets = scan_literature_citation_status(root, passport)
    reviews = scan_reviews(root)
    plans = scan_plans(root)
    stage = (passport.get("pipeline") or {}).get("current_stage")

    n_lit = sum(len(v) for v in buckets.values())
    stats = [
        ("stage", escape(str(stage)) if stage else "—"),
        ("papers cited", str(len(buckets["cited"]))),
        ("references", str(n_bib or n_lit)),
        ("scripts", str(len(scripts_list))),
        ("figures", str(n_figs + len(results["figures"]))),
    ]

    # Base assets from styles/ (embedded inline).
    base_dir = Path(__file__).resolve().parent.parent / "styles"
    css = (base_dir / "styles.css").read_text() if (base_dir / "styles.css").exists() else ""
    js = (base_dir / "components.js").read_text() if (base_dir / "components.js").exists() else ""

    dashboard_data = {
        "type": "dashboard",
        "generated": datetime.now().isoformat()[:19],
        "project": meta["title"],
        "stage": stage,
        "cited": len(buckets["cited"]),
        "intended": len(buckets["intended"]),
        "relevant_not_cited": len(buckets["relevant"]),
        "scripts": len(scripts_list),
        "references": n_bib,
        "figures": n_figs + len(results["figures"]),
        "tables": n_tabs,
    }

    panels = [
        build_header(meta, stats, stage),
        build_nav(),
        build_data_panel(data),
        build_literature_panel(buckets),
        build_analysis_panel(scripts_list, results),
        build_results_panel(results),
        build_paper_panel(sections, n_figs, n_tabs),
        build_quality_panel(passport),
        build_history_panel(reviews),
        build_plans_panel(plans),
    ]

    generated = datetime.now().strftime("%Y-%m-%d %H:%M")
    body = "\n".join(panels)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(meta['title'] or 'Project Dashboard')} — Dashboard</title>
  <style>{css}</style>
</head>
<body>
  <script type="application/json" id="report-data">{json.dumps(dashboard_data, indent=None)}</script>
  <div class="page">
    {body}
    <footer class="generated-footer">
      Generated {generated} by research-os
    </footer>
  </div>
  <script>{js}</script>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Generate research-os project dashboard")
    parser.add_argument("--project-root", default=".", help="Project root directory")
    parser.add_argument("--output", default=None, help="Output HTML file path")
    args = parser.parse_args()

    root = find_project_root(args.project_root)
    output = Path(args.output) if args.output else root / "project_dashboard.html"

    html = build_dashboard(root)
    output.write_text(html, encoding="utf-8")
    print(f"Dashboard generated: {output}")


if __name__ == "__main__":
    main()
