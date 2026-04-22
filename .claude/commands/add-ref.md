---
description: Fetch BibTeX by DOI → append to references.bib
argument-hint: "<DOI> [spoke_dir] [--key=firstauthoryearword]"
allowed-tools: Bash, Read, Edit
---

Auto-detect spoke as in `/verify-citations` if no `spoke_dir` given.

```
shared/.venv/Scripts/python.exe shared/scripts/add_ref.py <DOI> \
  --append $SPOKE/references.bib [--key <newkey>]
```

Verify: author + title + year + DOI present. If no `--key`, suggest `firstauthor<year><firstword>` and ask. Do NOT auto-cite in manuscript.

Argument: $ARGUMENTS
