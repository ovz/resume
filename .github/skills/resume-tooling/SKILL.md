---
name: resume-tooling
description: Set up the resume toolchain on a fresh workstation, install prerequisites, handle manual installers, and validate the Pandoc-based resume build.
---

# Resume toolchain setup

Use this skill when setting up the repo on a new machine, repairing a broken environment, or validating a fresh clone.

## Workflow

1. Run the bootstrap helper in this folder.
2. Detect the OS and install the minimal toolchain via the matching script.
3. If a dependency must be installed manually, download the official installer and stop only for that step.
4. Validate the toolchain before generating output.
5. Build the resume with the project script.

## Files

- `bootstrap.sh` — entry point
- `windows/install-prereqs.ps1` — Windows bootstrap
- `linux/install-prereqs.sh` — Debian/Ubuntu/Fedora/etc
- `macos/install-prereqs.sh` — Homebrew-based setup
- `manual-downloads.md` — URLs for required manual installers

## Required toolchain

The resume pipeline needs:

- Git
- Make
- Pandoc
- A TeX/ConTeXt runtime that provides `context` and `mtxrun`
- Optionally a package manager (`winget`, `brew`, `apt`, `dnf`, `yum`, or `pacman`)

## Validation steps

After installation:

- `git --version`
- `make --version`
- `pandoc --version`
- `context --version` or `mtxrun --version`
- `bash script/pandoc_resume.sh all`

## Guardrails

- Prefer official package managers and installer URLs.
- Keep shell commands idempotent; rerunning must be safe.
- Do not modify project logic unless the bootstrap flow is missing a required dependency.
- If a required tool is missing and cannot be installed automatically, stop and point to the exact manual download in `manual-downloads.md`.
- Use the repo’s real build entry point, not ad hoc commands.

## Typical new-machine flow

```bash
bash .github/skills/resume-tooling/bootstrap.sh
bash script/pandoc_resume.sh all
```

The bootstrap script should choose the correct OS-specific setup and fail clearly if a dependency still requires a manual install.
