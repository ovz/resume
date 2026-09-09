#!/usr/bin/env bash
# Install the resume toolchain on Linux. Source of truth for package names.
#
# Needed:
#   pandoc  — renders html, docx and rtf, and the ConTeXt source for the pdf
#   ConTeXt — the `mtxrun` engine that turns that source into the pdf
#   TeX Gyre fonts — the style template asks for `helvetica`, which ConTeXt
#            resolves to TeX Gyre Heros; without it the pdf run fails on fonts
#
# Everything here is free and open source. Nothing in this repository's build
# depends on a paid tool or an active subscription.
set -Eeuo pipefail

# Arch, and Arch derivatives including Omarchy.
#
# Package names changed and the old ones are still widely copied around:
# `pandoc` is now `pandoc-cli` (the `pandoc` name is the Haskell library), and
# the monolithic `texlive-core` was split, with ConTeXt landing in
# `texlive-context`. Installing the old names fails outright on a current Arch.
#
# A full -Syu rather than -Sy: Arch does not support partial upgrades, and
# `-Sy` followed by an install is the classic way to break a system.
if command -v pacman >/dev/null 2>&1; then
  sudo pacman -Syu --needed git pandoc-cli texlive-context texlive-fontsrecommended
  exit 0
fi

if command -v apt-get >/dev/null 2>&1; then
  sudo apt-get update
  sudo apt-get install -y git pandoc context texlive-fonts-recommended
  exit 0
fi

if command -v dnf >/dev/null 2>&1; then
  sudo dnf install -y git pandoc texlive-context texlive-collection-fontsrecommended
  exit 0
fi

if command -v zypper >/dev/null 2>&1; then
  sudo zypper install -y git pandoc texlive-context texlive-fonts-recommended
  exit 0
fi

echo "No supported Linux package manager found." >&2
echo "Install git, pandoc and ConTeXt manually: .github/skills/resume-tooling/manual-downloads.md" >&2
exit 1
