#!/usr/bin/env bash
set -Eeuo pipefail

if ! command -v brew >/dev/null 2>&1; then
  echo "Homebrew is required. Install it from https://brew.sh/ then rerun this script." >&2
  exit 1
fi

brew update
brew install git make pandoc --quiet
brew install --cask mactex --quiet || true

if ! command -v context >/dev/null 2>&1; then
  echo "ConTeXt was not found after install. Add /Library/TeX/texbin to PATH and rerun." >&2
  exit 1
fi

echo "macOS prerequisites installed."
