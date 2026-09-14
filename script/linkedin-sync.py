#!/usr/bin/env python3
"""Thin launcher. The real logic lives in the linkedin-publish skill, kept
self-contained there so the skill is transferable on its own -- copy
.github/skills/linkedin-publish/ into another repo with the same layout and it
works unmodified. This wrapper exists only because script/ is the path a person
or agent finds by looking at the repo, without needing to know a skill exists.

Python rather than bash, to match the tool it launches.

    python3 script/linkedin-sync.py status           # regenerate blocks from the Markdown, then what is stale
    python3 script/linkedin-sync.py round            # regenerate, then guided pass; Enter confirms each paste
    python3 script/linkedin-sync.py copy <block> [--open]
    python3 script/linkedin-sync.py done <block> | --all
    python3 script/linkedin-sync.py --no-regenerate status   # compare the files exactly as on disk

This tool touches no secrets and makes no network requests. Credential handling
for the unbuilt announce-post workflow was archived out of the working set; see
llm-wiki/wiki/sources/archived-linkedin-secrets-tool.md.
"""
import runpy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TARGET = REPO_ROOT / ".github" / "skills" / "linkedin-publish" / "linkedin_sync.py"

if not TARGET.is_file():
    sys.exit(f"error: cannot find the linkedin-publish skill at {TARGET}")

sys.argv[0] = str(TARGET)
runpy.run_path(str(TARGET), run_name="__main__")
