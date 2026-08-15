#!/usr/bin/env bash
set -Eeuo pipefail

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
repo_root="$( cd "${script_dir}/.." && pwd )"
pandoc_dir="${repo_root}/pandoc_resume"
markdown_dir="${repo_root}/markdown"

add_to_path_if_exists() {
  local candidate="$1"
  if [ -n "${candidate}" ] && [ -d "${candidate}" ] && [[ ":${PATH}:" != *":${candidate}:"* ]]; then
    PATH="${candidate}:${PATH}"
  fi
}

configure_texlive_paths() {
  local candidate
  for candidate in \
    "/c/texlive/2026/bin/windows" \
    "/c/texlive/2026/bin/win32" \
    "C:/texlive/2026/bin/windows" \
    "C:/texlive/2026/bin/win32" \
    "C:/texlive/2026/bin"; do
    add_to_path_if_exists "${candidate}"
  done

  if [ -d "/c/texlive/2026/bin/windows" ]; then
    export TEXLIVE_BIN="/c/texlive/2026/bin/windows"
  fi
}

configure_texlive_paths
export PATH

make_cmd=(make)
if ! command -v "${make_cmd[0]}" >/dev/null 2>&1; then
  for candidate in \
    "/mingw64/bin/mingw32-make.exe" \
    "/usr/bin/make" \
    "/usr/local/bin/make"; do
    if [ -x "${candidate}" ]; then
      make_cmd=("${candidate}")
      break
    fi
  done
fi

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc not found in PATH. Ensure TeX Live / Pandoc is installed and on PATH." >&2
  exit 1
fi

if ! command -v "${make_cmd[0]}" >/dev/null 2>&1; then
  echo "make is not installed or not on PATH. Install GNU make or use a shell with make available." >&2
  exit 1
fi

run_make() {
  local target="${1:-all}"
  "${make_cmd[@]}" -C "${pandoc_dir}" IN_DIR="${markdown_dir}" "${target}"
}

case "${1:-all}" in
  html|pdf|docx|rtf|all|clean)
    run_make "${1:-all}"
    ;;
  *)
    echo "Usage: $0 [all|html|pdf|docx|rtf|clean]" >&2
    exit 1
    ;;
esac