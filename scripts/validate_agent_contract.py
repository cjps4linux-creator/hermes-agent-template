#!/usr/bin/env python3
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "Identity", "Mission", "Scope", "Inputs", "Outputs",
    "Constraints", "Dependencies", "Tools", "Memory Model",
    "Failure Taxonomy", "Observability", "Evaluation"
]

def check(path: str) -> int:
    text = Path(path).read_text(encoding="utf-8")
    missing = [s for s in REQUIRED_SECTIONS if s not in text]
    if missing:
        print(f"missing:{','.join(missing)}")
        return 1
    print("ok")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: validate_agent_contract.py <contract.md>")
        raise SystemExit(2)
    raise SystemExit(check(sys.argv[1]))
