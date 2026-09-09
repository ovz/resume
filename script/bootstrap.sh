#!/usr/bin/env bash
# Thin launcher. The real logic lives in the resume-tooling skill, kept
# self-contained there so the skill is transferable on its own — copy
# .github/skills/resume-tooling/ into another repo with the same layout and it
# works unmodified. This wrapper exists only because script/ is the path a
# person or agent finds by looking at the repo, without needing to know a
# skill exists.
set -Eeuo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/.." && pwd)"

exec bash "${repo_root}/.github/skills/resume-tooling/bootstrap.sh" "$@"
