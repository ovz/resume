#!/usr/bin/env bash
set -Eeuo pipefail

if command -v apt-get >/dev/null 2>&1; then
  sudo apt-get update
  sudo apt-get install -y git make pandoc context texlive-xetex
  exit 0
fi

if command -v dnf >/dev/null 2>&1; then
  sudo dnf install -y git make pandoc texlive-context
  exit 0
fi

if command -v yum >/dev/null 2>&1; then
  sudo yum install -y git make pandoc texlive-context
  exit 0
fi

if command -v pacman >/dev/null 2>&1; then
  sudo pacman -Syu --noconfirm git make pandoc texlive-core
  exit 0
fi

if command -v zypper >/dev/null 2>&1; then
  sudo zypper install -y git make pandoc texlive-context
  exit 0
fi

echo "No supported Linux package manager found. Use the manual downloads file." >&2
exit 1
