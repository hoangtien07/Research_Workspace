---
description: Cross-check quantitative claims in manuscript against pipeline CSVs
argument-hint: "[spoke_dir]"
allowed-tools: Bash, Read
---

Auto-detect spoke as in `/verify-citations`.

```
shared/.venv/Scripts/python.exe shared/scripts/verify_numbers.py $SPOKE/manuscript.md
```

On `[NO]` mismatch: show table (claim | manuscript | csv | file). Recommend fix manuscript or re-run pipeline. Do NOT modify without user confirmation.

Argument: $ARGUMENTS
