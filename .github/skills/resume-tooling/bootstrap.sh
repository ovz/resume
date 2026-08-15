#!/usr/bin/env bash
set -Eeuo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/../../.." && pwd)"

case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*|Windows_NT)
    powershell -ExecutionPolicy Bypass -File "${script_dir}/windows/install-prereqs.ps1"
    ;;
  Linux)
    bash "${script_dir}/linux/install-prereqs.sh"
    ;;
  Darwin)
    bash "${script_dir}/macos/install-prereqs.sh"
    ;;
  *)
    echo "Unsupported OS: $(uname -s)" >&2
    echo "Use the OS-specific helper under .github/skills/resume-tooling/" >&2
    exit 1
    ;;
esac

echo "Validating toolchain..."
for cmd in git make pandoc; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "Missing required command: $cmd" >&2
    exit 1
  fi
done

if ! command -v context >/dev/null 2>&1 && ! command -v mtxrun >/dev/null 2>&1; then
  echo "Context/ConTeXt is not installed. Follow the manual download instructions in .github/skills/resume-tooling/manual-downloads.md" >&2
  exit 1
fi

echo "Toolchain OK. Building resume..."
cd "${repo_root}"
bash "${repo_root}/script/pandoc_resume.sh" all
