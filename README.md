# Research Workspace — DiSC × Driver-gene monorepo

Workspace root for the **DiSC × Driver-gene** research programme.  
This folder holds the hub and all paper spoke repos as sibling directories.

---

## Structure

```
Research_Workspace/        ← this meta-repo
├── research_shared/       ← hub: shared Python package + Claude tooling + paper template
└── paper-disc-grn/        ← spoke: DiSC profiling of the human GRN (active paper)
```

Each sub-directory is an **independent git repository**:

| Repo | GitHub | Role |
|---|---|---|
| `research_shared` | [hoangtien07/research_shared](https://github.com/hoangtien07/research_shared) | Hub — `ddl-pipeline` package, scripts, Claude tooling |
| `paper-disc-grn` | [hoangtien07/paper-disc-grn](https://github.com/hoangtien07/paper-disc-grn) | Spoke — DiSC-GRN paper (private) |

---

## Hub-and-spoke model

```
research_shared/    ← shared utilities (ddl-pipeline), paper template, Claude commands
        ↓  pip install -e ../research_shared/ddl-pipeline
paper-disc-grn/     ← manuscript, pipeline, data, results for the GRN paper
paper-disc-ppi/     ← future spoke (DiSC-PPI paper)
```

**Design principles:**

- Shared analysis code lives in `research_shared/ddl-pipeline` (versioned, pip-installable).
- Paper-specific pipeline scripts, data, and results stay inside the spoke repo.
- Claude Code tooling (`.claude/`) is maintained in `research_shared/` and inherited by spokes.

---

## Cloning the full workspace

```bash
# 1. Create workspace root
mkdir Research && cd Research

# 2. Clone hub
git clone https://github.com/hoangtien07/research_shared.git

# 3. Clone active spokes
git clone https://github.com/hoangtien07/paper-disc-grn.git

# 4. Set up shared venv (reused by all spokes)
cd research_shared
py -m venv .venv
.venv/Scripts/python.exe -m pip install --upgrade pip
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe -m pip install -e ./ddl-pipeline

# 5. Install spoke-specific deps
cd ../paper-disc-grn
..\research_shared\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

---

## Active paper

### DiSC-GRN — `paper-disc-grn/`

**Working title**: DiSC profiling of the human gene regulatory network: a four-dimensional  
functional feature space reveals homophilous community structure and cancer-driver predictive power  
**Target journal**: *Briefings in Bioinformatics* (Q1, IF ≈ 9.5); backup: *Computers in Biology and Medicine*  
**Target submission**: 2026-08-23  
**Pre-registration tag**: `prereg-tier2` (locked in paper-disc-grn)

See [paper-disc-grn/CLAUDE.md](paper-disc-grn/CLAUDE.md) for paper-specific rules and execution plan.

---

## Starting a new paper

```bash
# Open Claude Code in research_shared/:
/new-paper paper-SLUG
```

This scaffolds `../paper-SLUG/` from `research_shared/paper_template/` with:
- Self-contained `Makefile`, `requirements.txt`, `make_figures.py`
- Pre-wired `from ddl_pipeline.X import Y` imports
- CLAUDE.md deferring to hub rules

---

## Requirements

| Tool | Version | Notes |
|---|---|---|
| Python | 3.14 | `.venv/` inside `research_shared/` |
| Pandoc | ≥ 3.0 | Required for `make docx` |
| Git | any recent | Each spoke is an independent repo |
| make | optional | Each spoke has a portable `build.py` fallback |
