"""PreToolUse — block destructive writes to protected paths."""
from __future__ import annotations
import json, re, sys

BLOCKED = [
    (re.compile(r"\brm\b[^|;&]*-rf?[^|;&]*\bdata/(?:raw|processed)/"), "rm on data/"),
    (re.compile(r"\brm\b[^|;&]*-rf?[^|;&]*\bresults/"), "rm on results/"),
    (re.compile(r"\brm\b[^|;&]*-rf?[^|;&]*\bDrivergene/"), "rm on Drivergene/"),
    (re.compile(r"\bgit\b.*\breset\b.*--hard"), "git reset --hard"),
    (re.compile(r"\bgit\b.*\bpush\b.*--force"), "git push --force"),
]

def main() -> int:
    try:
        cmd = json.load(sys.stdin).get("tool_input", {}).get("command", "")
    except Exception:
        return 0
    for rx, label in BLOCKED:
        if rx.search(cmd):
            print(f"[guard] blocked: {label}\n  {cmd}", file=sys.stderr)
            return 2
    return 0

if __name__ == "__main__":
    sys.exit(main())
