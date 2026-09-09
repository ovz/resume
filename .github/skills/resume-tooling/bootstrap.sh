#!/usr/bin/env bash
# Fresh-clone setup: submodule, toolchain, then a verified build.
#
# Safe to re-run; every step is idempotent. Run it after cloning on a new
# machine, or to repair an environment that has drifted.
#
# This file is the skill's own copy of the logic, not a pointer to one
# elsewhere: dropped into another repo with the same markdown/pandoc_resume/
# submodule conventions, this skill directory works unmodified. `script/
# bootstrap.sh` in this repo is a thin launcher onto it, kept only because
# that is the discoverable path a person or agent finds without reading docs.
#
#   bootstrap.sh            # submodule + install prerequisites + build
#   bootstrap.sh --check    # verify only, install nothing, build nothing
#   bootstrap.sh --no-build # set the environment up but skip the build
set -Eeuo pipefail

tooling_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${tooling_dir}/../../.." && pwd)"

do_install=1
do_build=1
case "${1:-}" in
  --check)    do_install=0; do_build=0 ;;
  --no-build) do_build=0 ;;
  "")         ;;
  *) printf 'Usage: script/bootstrap.sh [--check|--no-build]\n' >&2; exit 1 ;;
esac

step() { printf '\n==> %s\n' "$*"; }
warn() { printf 'warning: %s\n' "$*" >&2; }
die()  { printf 'error: %s\n' "$*" >&2; exit 1; }

# ---------------------------------------------------------------- submodule --
# pandoc_resume supplies the ConTeXt/CSS style assets. If the commit recorded in
# this repo is missing from the fork (the fork's history has been rewritten by an
# upstream merge before now), fall back to the submodule's default branch rather
# than leaving an empty directory that fails much later with a confusing error.
step "Submodule: pandoc_resume"
cd "${repo_root}"
if git submodule update --init --recursive 2>/dev/null; then
  printf '    checked out the recorded commit\n'
elif git submodule update --init --recursive --remote 2>/dev/null; then
  warn "the submodule commit recorded in this repo does not exist in the fork; \
checked out the fork's default branch instead.
     Review 'git -C pandoc_resume log -1' and, if it looks right, ask the owner \
to commit the updated submodule pointer."
else
  die "could not check out the pandoc_resume submodule. Check network and \
credentials for github.com, then rerun."
fi

[ -f "${repo_root}/pandoc_resume/styles/chmduquesne.tex" ] ||
  die "submodule checked out but style assets are missing; expected pandoc_resume/styles/"

# ------------------------------------------------------------- prerequisites --
if [ "${do_install}" -eq 1 ]; then
  step "Toolchain: installing prerequisites"

  # The installers need root. Fail with the exact command instead of hanging on
  # a password prompt that has no terminal to read from (the common case when an
  # agent or CI job runs this).
  if ! sudo -n true 2>/dev/null && [ ! -t 0 ]; then
    die "installing packages needs sudo, and there is no terminal to prompt on.
     Run this script yourself in an interactive terminal:
       ${repo_root}/script/bootstrap.sh
     Or install the prerequisites first and rerun this with --check."
  fi

  case "$(uname -s)" in
    Linux)  bash "${tooling_dir}/linux/install-prereqs.sh" ;;
    Darwin) bash "${tooling_dir}/macos/install-prereqs.sh" ;;
    MINGW*|MSYS*|CYGWIN*|Windows_NT)
      powershell -ExecutionPolicy Bypass -File "${tooling_dir}/windows/install-prereqs.ps1" ;;
    *) die "unsupported OS: $(uname -s). See ${tooling_dir}/manual-downloads.md" ;;
  esac
fi

# ------------------------------------------------------------------- verify --
step "Toolchain: verifying"
missing=0
check() {
  if command -v "$1" >/dev/null 2>&1; then
    printf '    ok       %-8s %s\n' "$1" "$(command -v "$1")"
  else
    printf '    MISSING  %-8s %s\n' "$1" "$2"; missing=1
  fi
}
check git    "install git"
check pandoc "provides all four output formats"
check mtxrun "ConTeXt engine; required for PDF output"

if [ "${missing}" -ne 0 ]; then
  printf '\n'
  die "toolchain incomplete. Install the missing tools (see \
${tooling_dir}/manual-downloads.md) and rerun."
fi

# -------------------------------------------------------------------- build --
if [ "${do_build}" -eq 1 ]; then
  step "Building resume artifacts"
  bash "${tooling_dir}/pandoc_resume.sh" all
else
  step "Skipping build (run: script/pandoc_resume.sh all)"
fi

printf '\nBootstrap complete.\n'
