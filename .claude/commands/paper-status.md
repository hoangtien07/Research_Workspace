---
description: Word count, citations, figures, open [CHECK:] markers
argument-hint: "[spoke_dir]"
allowed-tools: Bash
---

Auto-detect spoke as in `/verify-citations`.

```
shared/.venv/Scripts/python.exe shared/scripts/paper_status.py $SPOKE
```

Flag: `[CHECK:]` > 0, `{{placeholder}}` > 0, word count over journal budget (see spoke CLAUDE.md §1).

Argument: $ARGUMENTS
