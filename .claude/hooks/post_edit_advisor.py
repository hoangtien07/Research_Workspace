"""PostToolUse — non-blocking reminder after manuscript/bib/figure edits."""
from __future__ import annotations
import json, sys
from pathlib import Path

PY      = "shared/.venv/Scripts/python.exe"
SCRIPTS = "shared/scripts"

def _spoke(path: str) -> str | None:
    """Return spoke directory name (paper-*) from an absolute file path."""
    for part in Path(path).parts:
        if part.startswith(("paper-", "paper_")):
            return part
    return None

def main() -> int:
    try:
        ti = json.load(sys.stdin).get("tool_input", {})
    except Exception:
        return 0
    path = ti.get("file_path") or ti.get("path") or ""
    if not path:
        return 0
    name  = Path(path).name
    spoke = _spoke(path)
    if not spoke:
        return 0

    if name == "manuscript.md":
        print(
            f"[advisor] edited manuscript — consider:\n"
            f"  {PY} {SCRIPTS}/verify_citations.py {spoke}/manuscript.md {spoke}/references.bib\n"
            f"  {PY} {SCRIPTS}/verify_numbers.py {spoke}/manuscript.md",
            file=sys.stderr,
        )
    elif name == "references.bib":
        print(
            f"[advisor] edited .bib — run:\n"
            f"  {PY} {SCRIPTS}/verify_citations.py {spoke}/manuscript.md {spoke}/references.bib",
            file=sys.stderr,
        )
    elif name == "make_figures.py":
        print(f"[advisor] edited figures — regenerate: cd {spoke} && make figures", file=sys.stderr)
    return 0

if __name__ == "__main__":
    sys.exit(main())
