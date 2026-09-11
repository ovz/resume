#!/usr/bin/env python3
"""Thin launcher. The real logic lives in the large-import skill, kept
self-contained there so the skill is transferable on its own -- copy
.github/skills/large-import/ into another repo and it works unmodified. This
wrapper exists only because script/ is the path a person or agent finds by
looking at the repo, without needing to know a skill exists.

Python rather than bash, deliberately: the thing it launches is the repo's
cross-platform tool, so its launcher has to run on Windows too.

    python3 script/large-import.py pack   <source> --out <raw-store>/
    python3 script/large-import.py verify <archive.xz> --sha256 <hex>
    python3 script/large-import.py unpack <archive.xz> --out <dir>
"""
import runpy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TARGET = REPO_ROOT / ".github" / "skills" / "large-import" / "archive.py"

if not TARGET.is_file():
    sys.exit(f"error: cannot find the large-import skill at {TARGET}")

sys.argv[0] = str(TARGET)
runpy.run_path(str(TARGET), run_name="__main__")
