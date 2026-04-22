---
description: Full pre-submission audit — go/no-go verdict
argument-hint: "[spoke_dir]"
allowed-tools: Bash, Read
---

Auto-detect spoke as in `/verify-citations`. Run all checks even if earlier ones fail.

```
PY=shared/.venv/Scripts/python.exe  S=shared/scripts
$PY $S/verify_citations.py $SPOKE/manuscript.md $SPOKE/references.bib
$PY $S/verify_numbers.py $SPOKE/manuscript.md
$PY $S/paper_status.py $SPOKE
cd $SPOKE && make check
```

Then grep manuscript for:
- Vietnamese leftovers: `Kết quả`, `điều`, `thuyết`
- `p = 0.000` (must be `p < 0.001`)
- Any paper-specific forbidden patterns listed in spoke CLAUDE.md

| Check | OK/FAIL | Notes |
|---|---|---|
| Citations | | |
| Numbers | | |
| Open markers | | [CHECK:] + {{placeholder}} count |
| Build | | |
| Forbidden patterns | | |

Verdict: **READY** / **NOT READY**.

Argument: $ARGUMENTS
