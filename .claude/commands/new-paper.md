---
description: Scaffold a new spoke repo from paper_template (run from Research/ or shared/)
argument-hint: "<slug>  (e.g. paper-grn-v2)"
allowed-tools: Bash, Read, Edit
---

Slug must start with `paper-` or `paper_`.

```
shared/.venv/Scripts/python.exe shared/scripts/new_paper.py <slug>
```

New repo created at `Research/paper-<slug>/`. After success, walk user through:
1. Fill `{{placeholders}}` in CLAUDE.md, metadata.yaml, manuscript.md
2. Download CSL: see csl/README.md
3. Create GitHub repo (private): https://github.com/new
4. `cd paper-<slug> && git remote add origin <url> && git push -u origin main`

Do NOT write paper content — scaffold only.

Argument: $ARGUMENTS
