# Oleg Zhylin — résumé repository

Personal resume repository. Markdown sources in `markdown/` render via Pandoc into HTML, PDF, DOCX and RTF. `llm-wiki/` is the maintained knowledge base behind the resume content.

## Quick start

```bash
git clone <repo> && cd resume
script/bootstrap.sh              # submodule + toolchain + first build
script/pandoc_resume.sh all      # html, pdf, docx, rtf, then verify
```

Full build details, sensitivity rules, and everything else: [`AGENTS.md`](AGENTS.md).

## Layout

| Path | What it is |
|---|---|
| `markdown/` | The outward-facing resume and references documents (Pandoc input) |
| `llm-wiki/` | Durable, committed knowledge base behind the resume |
| `pandoc_resume/` | Git submodule — build styling only, never edited directly |
| `script/` | Thin launchers for bootstrapping and building — see below |
| `__untracked_stuff/` | Gitignored scratch area — session notes, nothing load-bearing |

## Scripts vs. skills

`script/bootstrap.sh` and `script/pandoc_resume.sh` are where a person or agent looks first — `script/` is the discoverable path, found by browsing the repo, with no README required. But they are launchers only, a few lines each, that hand off to `.github/skills/resume-tooling/`:

```
script/bootstrap.sh        --> .github/skills/resume-tooling/bootstrap.sh
script/pandoc_resume.sh    --> .github/skills/resume-tooling/pandoc_resume.sh
```

The real implementation lives in the skill directory, not in `script/`, so that the skill is self-sufficient: copy `.github/skills/resume-tooling/` into another repo with the same `markdown/`/`pandoc_resume/` layout and it works unmodified, with no dependency on this repo's `script/` folder. Bootstrapping and building are one skill rather than two because they're interdependent — bootstrap ends by invoking the build, and the build's error messages point back to bootstrap — splitting them would just make each half depend on the other's private paths.

The same split applies to every skill under `.github/skills/`: a skill folder is meant to be self-contained and portable, and anything at the repo root that invokes one should stay a thin launcher rather than growing logic of its own.

## Instructions for AI coding agents — who reads what

This repo is edited with more than one AI coding assistant, and no single file or setting is read by all of them. Nothing below should be assumed to work "everywhere" just because it works in one editor:

| File / mechanism | Read by | Scope |
|---|---|---|
| [`AGENTS.md`](AGENTS.md) (root and per-directory) | Any tool implementing the open [AGENTS.md](https://agents.md) convention | **Universal.** Not tied to any editor or vendor — this repo's actual rules live here. |
| [`CLAUDE.md`](CLAUDE.md) (root and per-directory) | Claude Code (Anthropic's CLI and IDE extension), wherever it runs | **Claude Code specific.** Each one just imports the sibling `AGENTS.md`. |
| [`.github/copilot-instructions.md`](.github/copilot-instructions.md) | GitHub Copilot Chat's repository custom-instructions feature | **GitHub Copilot specific**, in principle across whichever surface runs Copilot Chat (VS Code, Visual Studio, JetBrains, github.com) — this repo has only configured and verified the VS Code path. |
| `.github/skills/<name>/SKILL.md` | The cross-tool "Agent Skills" file format — GitHub Copilot and Claude Code both implement it, with different discovery paths | **The format is shared; the discovery path is not.** Claude Code only scans `.claude/skills/`, never `.github/skills/`, so each skill has a symlink bridging the two. |
| `.github/instructions/**/*.instructions.md` | GitHub Copilot Chat's path-scoped instructions feature | **GitHub Copilot specific.** No Claude Code equivalent. |
| `.vscode/settings.json` | **VS Code only** — specifically opt-in settings for the GitHub Copilot Chat *extension* | Not GitHub Copilot generally, not Claude Code, not any other editor. Several are experimental as of this writing and may change in a future VS Code release. |

The full per-tool table, exact setting names, and the sharp edges (a VS Code setting whose name suggests it's about Claude Code but isn't) live in [`.github/AGENTS.md`](.github/AGENTS.md) — read that before adding, moving, or renaming any customization file.

## Agents do not commit

Every change in this repository — human- or AI-assisted — is reviewed before it lands. Full rule: [`AGENTS.md`](AGENTS.md) § *Agents do not commit*.
