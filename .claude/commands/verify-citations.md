---
description: Verify every [@key] in a manuscript resolves in references.bib
argument-hint: "[spoke_dir]  — auto-detected if only one spoke exists"
allowed-tools: Bash, Read
---

**Auto-detect spoke**: if `$ARGUMENTS` is empty, run `ls */manuscript.md` to find spokes.
Use the only result, or ask if multiple exist.

```
PY=shared/.venv/Scripts/python.exe
SPOKE=<detected or from $ARGUMENTS>
$PY shared/scripts/verify_citations.py $SPOKE/manuscript.md $SPOKE/references.bib
```

Report missing keys → suggest `/add-ref <DOI>` or remove orphan. Report unused `.bib` entries as warning.

Argument: $ARGUMENTS
