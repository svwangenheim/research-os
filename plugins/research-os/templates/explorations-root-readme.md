# Explorations

This folder is a **sandbox** for experimental and exploratory work. All new ideas, prototypes, and research experiments go here first — never directly into `03_analysis/`.

## How It Works

1. **Create a subfolder** for each exploration (e.g., `explorations/new-estimator/`) — seed it from `${CLAUDE_PLUGIN_ROOT}/templates/exploration-readme.md`
2. **Work freely** — lower quality threshold (60/100) during exploration
3. **Decide:** graduate to `03_analysis/scripts/{R,py,jl}/` (80/100 required), keep exploring, or archive

## Rules

See `rules/content-standards.md` Section 4 (Exploration Folder Protocol) and Section 5 (Exploration Fast-Track) for the full protocol.

## Structure

```
explorations/
├── [active-project]/       # Work in progress
│   ├── README.md           # Goal, hypotheses, status (from exploration-readme.md)
│   ├── R/                  # Experimental code
│   ├── scripts/            # Test scripts
│   └── output/             # Results
└── ARCHIVE/                # Completed or abandoned
    ├── completed_[name]/   # Graduated to production
    └── abandoned_[name]/   # Documented why stopped (from archive-readme.md)
```
