---
name: resume-tooling
description: "Set up the resume build toolchain on a fresh workstation, repair a broken environment, or diagnose a failing render. Covers the submodule, the Pandoc and ConTeXt prerequisites per OS, and the verified build. USE WHEN a clone is new, a build fails on a missing tool, the portrait image is absent from an artifact, or the pandoc_resume submodule is empty. DO NOT USE for editing resume content — that is resume-editing."
---

# Resume toolchain setup

Everything the build needs is free and open source. Nothing here depends on a paid tool or an active AI subscription, and the repository's agent customizations are deliberately harness-agnostic (`AGENTS.md`, `SKILL.md`), so the build and the instruction layer both survive a change of assistant.

`bootstrap.sh` and `pandoc_resume.sh` in this folder are the real implementation — self-contained, so this whole skill folder is portable to another repo with the same `markdown/`/`pandoc_resume/` layout. `script/bootstrap.sh` and `script/pandoc_resume.sh` at the repo root are thin launchers onto them, kept because `script/` is the path someone finds by looking at the repo, without needing to know a skill exists first. The two are interdependent — bootstrap ends by calling the build, the build tells failures to rerun bootstrap — which is why they live together as one skill rather than two.

## New machine

```bash
git clone <repo>
cd <repo>
script/bootstrap.sh
```

That does everything: checks out the `pandoc_resume` submodule, installs the OS prerequisites, verifies the toolchain, and runs a verified build. It is idempotent — rerun it any time an environment looks wrong.

Variants: `script/bootstrap.sh --check` verifies without installing or building; `--no-build` sets up but stops short of rendering.

## What the pipeline needs

| Tool | Why |
|---|---|
| `git` | the repo and its submodule |
| `pandoc` | renders HTML, DOCX and RTF, and the ConTeXt source for the PDF |
| `mtxrun` (ConTeXt) | turns that source into the PDF; the needy part of the toolchain |
| TeX Gyre fonts | the style template asks for `helvetica`, which ConTeXt resolves to TeX Gyre Heros |

`make` is **not** required. The build driver is `pandoc_resume.sh` in this folder (invoke it via `script/pandoc_resume.sh`), which calls Pandoc directly rather than the submodule's Makefile — the upstream Makefile hardcodes its Pandoc invocations, leaving no way to pass `--resource-path` or `--embed-resources`, without which the portrait PNG is silently dropped.

## Package names

`linux/install-prereqs.sh` is the source of truth; `macos/install-prereqs.sh` and `windows/install-prereqs.ps1` cover the other platforms. Two names commonly copied from old guides are wrong on current Arch and fail outright:

- `pandoc` → **`pandoc-cli`** (`pandoc` is now the Haskell library)
- `texlive-core` → **`texlive-context`** (the monolithic package was split)

On Arch, install with a full `-Syu`, never `-Sy` followed by an install: partial upgrades are unsupported and break the system.

## Installing needs root

The package step needs `sudo`. An agent's shell usually has no TTY, so `sudo` cannot prompt and the install fails rather than hanging — `script/bootstrap.sh` detects this and prints the command to run interactively instead. Do not work around it by piping a password into `sudo -S`, which exposes it in shell history and process arguments, and never ask the owner to paste a password into a chat transcript.

## Validate

```bash
script/bootstrap.sh --check     # git, pandoc, mtxrun
script/pandoc_resume.sh all     # build, ending in the verify pass
```

The build ends by asserting the portrait PNG is embedded in all four artifacts. A `NO IMAGE` line is a build failure: each format embeds images by a different mechanism, so a bad path typically breaks some formats while others still render fine, and inspecting one artifact proves nothing about the others.

## Known failure modes

- **`pandoc_resume/` is empty.** The submodule commit recorded in this repo does not exist in the fork — the fork's history was rewritten by an upstream merge. `script/bootstrap.sh` falls back to the fork's default branch and warns; the owner then commits the corrected submodule pointer.
- **`Cannot find context.lua` / ConTeXt fails on a fresh TeX Live.** The file database has not been generated. `script/pandoc_resume.sh` retries once through `mtxrun --generate` automatically; if it still fails, read `pandoc_resume/output/context_<name>.log`.
- **PDF builds but the portrait is missing.** ConTeXt resolves `\externalfigure` paths relative to its working directory; the build stages `markdown/assets/` next to the generated `.tex` for exactly this reason.

## Guardrails

- Prefer official package managers and installer URLs; `manual-downloads.md` has the fallbacks.
- Keep every command idempotent.
- Never edit files inside `pandoc_resume/` — it is a submodule, and changes belong upstream in the fork.
- Never commit generated output; `pandoc_resume/output/`, `*.pdf` and `*.htm*` are gitignored.
- Agents do not commit — see the root [`AGENTS.md`](../../../AGENTS.md).
