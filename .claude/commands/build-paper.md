---
description: verify + pandoc → build/manuscript.docx
argument-hint: "[spoke_dir] [target=docx|pdf|all|figures|check]"
allowed-tools: Bash, Read
---

Auto-detect spoke as in `/verify-citations`. Default target: `docx`.

1. Run verify-citations. If failures → STOP, report, do not build.
2. Run verify-numbers and paper-status (warnings only, don't block).
3. Build: `cd $SPOKE && make <target>`
4. Report output path + file size, or show `build/pandoc.log` on failure.

Argument: $ARGUMENTS
