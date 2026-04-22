"""Workspace status line — git branch | changes | active spoke(s) word count."""
from __future__ import annotations
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # Research/

def _git(args: list[str]) -> str:
    try:
        return subprocess.check_output(["git"] + args, cwd=ROOT,
                                       stderr=subprocess.DEVNULL, timeout=2).decode().strip()
    except Exception:
        return ""

def _words(md: Path) -> int:
    if not md.exists():
        return 0
    text = md.read_text(encoding="utf-8", errors="ignore")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    return len(re.findall(r"\S+", text))

def main() -> int:
    branch  = _git(["rev-parse", "--abbrev-ref", "HEAD"]) or "-"
    changes = len([l for l in _git(["status", "--porcelain"]).splitlines() if l.strip()])
    spokes  = [d for d in ROOT.iterdir() if d.is_dir() and (d / "manuscript.md").exists()]

    parts = [f"\033[36m{branch}\033[0m"]
    if changes:
        parts.append(f"\033[33m*{changes}\033[0m")
    else:
        parts.append("\033[32mclean\033[0m")
    for s in spokes:
        w = _words(s / "manuscript.md")
        parts.append(f"\033[35m{s.name}\033[0m ({w:,}w)")

    print(" | ".join(parts))
    return 0

if __name__ == "__main__":
    sys.exit(main())
