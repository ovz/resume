# Agent customization layout

How this repository's instructions for AI coding agents are organized, and the conventions each file type must follow to stay discoverable. Read this before adding, moving, or renaming any customization file — every type below is matched by an exact filename or glob, and a file in the wrong shape is ignored *silently*.

## The conventions, and what this repo uses

No single mechanism is honoured by every tool. And "GitHub Copilot" is not one thing — it ships inside VS Code, Visual Studio, JetBrains IDEs, a CLI, and github.com, each with its own settings surface and its own rollout schedule for a given feature. **This repo has only configured and verified the VS Code surface**, because that is the editor in use here. The table below states what a feature does per GitHub's own docs; the *VS Code specifics* section right after it says which of these additionally need a VS Code setting turned on, in this repo, today — treat anything not covered there as unverified on Copilot's other surfaces.

| Type | Location / glob | GitHub Copilot | Claude Code |
|---|---|---|---|
| Always-on, repo-wide | `AGENTS.md` at repo root | Loaded — VS Code gates this behind an experimental setting; other surfaces not verified here | **Not read directly.** Bridged — see below |
| Always-on, per-directory | `AGENTS.md` in any subdirectory | Loaded when work touches that directory — VS Code gates this behind a second, separate experimental setting | **Not read directly.** Bridged — see below |
| Copilot always-on | `.github/copilot-instructions.md` | Loaded into every Copilot Chat request, per GitHub's docs, in principle on any surface | Ignored — Copilot-only file |
| Claude always-on | `CLAUDE.md` at repo root and per-directory | Ignored, **except** VS Code's own chat has a separate opt-in setting to also read `CLAUDE.md` — see the naming-collision warning below; that setting is not "does Claude Code work in VS Code" | Loaded automatically: root at startup, nested on demand when Claude reads a file in that directory |
| Path-scoped instructions | `.github/instructions/**/*.instructions.md`, `applyTo` glob | Applied when the edited file matches `applyTo` — a GitHub Copilot Chat feature | **Not supported.** No Claude Code equivalent auto-injection by edited path |
| Agent skills | `.github/skills/<name>/SKILL.md` | Loaded on demand when `description` matches the task — a cross-editor Agent Skills format, not VS-Code-only | **Not discovered directly** — Claude Code only scans `.claude/skills/<name>/SKILL.md`. Bridged — see below |
| Prompt files | `.github/prompts/*.prompt.md` | Invoked by the user on demand | not yet; no equivalent used here |
| Custom agents | `.github/agents/*.agent.md` | Selected by the user on demand | not yet; Claude equivalent would be `.claude/agents/*.md` |

## VS Code specifics — read this before trusting a setting name

Everything in this section is about **one editor's Copilot Chat extension**, not GitHub Copilot as a whole, not Claude Code, and not this repo's own rules. `.vscode/settings.json` carries these because a fresh clone opened in VS Code would otherwise silently use only part of this layout — but every one of them does nothing outside VS Code, and several are labeled experimental by VS Code's own docs as of this writing, so a name, default, or existence here can change in a future VS Code release. Verify against `code.visualstudio.com/docs/agent-customization` if something doesn't load as expected.

| Setting | What it actually gates |
|---|---|
| `chat.useAgentsMdFile` | Whether VS Code's Copilot Chat reads the root `AGENTS.md` at all. Experimental, off by default upstream — this repo turns it on. |
| `chat.useNestedAgentsMdFiles` | Whether it additionally reads per-directory `AGENTS.md` files. Experimental, and separate from the setting above — one can be on without the other. |
| `chat.useClaudeMdFile` | Whether VS Code's **own** Copilot Chat also reads `CLAUDE.md` (and `GEMINI.md`). **This name is a trap: it does not gate whether the standalone Claude Code CLI/extension works.** Claude Code reads `CLAUDE.md` unconditionally on its own, regardless of this setting. This setting only controls whether Copilot, running inside VS Code, additionally honors a file written for a different tool. |
| `chat.instructionsFilesLocations` | Where VS Code looks for `*.instructions.md` files. Defaults to `{ ".github/instructions": true }`, which already matches this repo's layout. |
| `github.copilot.chat.codeGeneration.useInstructionFiles` | Whether `.github/copilot-instructions.md` is added to context. Reportedly on by default in VS Code Copilot already; listed for completeness, not because this repo depends on flipping it. |
| `github.copilot.chat.skillTool.enabled` | Enables running a skill in a *forked sub-context* specifically — an experimental execution mode, **not** a blanket prerequisite for basic skill discovery, despite how it reads. |

None of these settings exist for, or affect, Copilot in the CLI, Visual Studio, JetBrains IDEs, or github.com, nor Claude Code anywhere. If a rule in this repo isn't loading and you're not looking at VS Code's own Copilot Chat, this table is not why.

## The two bridges Claude Code needs

Claude Code's rule is simple and worth stating plainly: **it reads `CLAUDE.md`, not `AGENTS.md`, and it scans `.claude/skills/`, not `.github/skills/`.** Everything below exists to close that gap without duplicating content or moving the canonical files.

- **AGENTS.md → CLAUDE.md.** Every directory with a load-bearing `AGENTS.md` (root, here, `instructions/`, `../markdown/`, `../llm-wiki/`) has a sibling `CLAUDE.md` containing `@AGENTS.md` — Claude Code's file-import syntax — plus a one-line explanation. The import is what actually loads the content; the prose around it is for a human or another agent opening the file. Do not put `@`-imports inside an `AGENTS.md` file itself — Copilot and other AGENTS.md-standard readers treat that file as literal text, not an import directive, and would show the raw `@AGENTS.md` string to the user.
- **`.github/skills/` → `.claude/skills/`.** Each skill folder has a symlink at `.claude/skills/<name>` pointing back to `.github/skills/<name>`. The skill's real files — `SKILL.md`, scripts, templates — live only under `.github/skills/`; the symlink makes Claude Code's scanner find them without a second copy to drift. Adding a skill means adding one matching symlink; nothing else in this bridge changes. Note that git stores these as symlinks (mode `120000`), which a Windows clone only reproduces when `core.symlinks` is enabled — see *Keeping it honest* below.

## Single source of truth

`AGENTS.md` files carry the actual content. `copilot-instructions.md` and `CLAUDE.md` are deliberately thin pointers, because duplicating rules across them means every request pays for the same text more than once, and the copies drift. When a rule changes, change the `AGENTS.md` that owns it and nothing else — including when the change happens because a `CLAUDE.md` bridge file imports it.

The same logic applies to skills. A skill body should not restate what an `AGENTS.md` already says; it links to it. Skills exist so an agent can pull in a *procedure* on demand, which is a different job from the always-on rules that constrain every edit.

## Required shapes

**`SKILL.md`** — YAML frontmatter with both fields, or the skill is not registered:

```yaml
---
name: resume-editing        # required; lowercase, digits and hyphens only; matches the folder name
description: "What it does AND when to use it."   # required; this is what the agent matches on
---
```

`applyTo` is **not** a skill field. A rule that should fire automatically based on which file is being edited is a path-scoped instruction, not a skill.

**`*.instructions.md`** — frontmatter with an `applyTo` glob; `name` and `description` are optional:

```yaml
---
description: "Short summary."
applyTo: "markdown/**/*.md"
---
```

The filename must end in `.instructions.md`. A plain `.md` file in `.github/instructions/` is not picked up by the instructions mechanism.

**`AGENTS.md`** — no frontmatter. Plain Markdown, scoped to the directory it sits in.

## Keeping it honest

- After adding a skill, confirm the frontmatter has `name` and `description`, that the folder name matches `name`, and add the matching `.claude/skills/<name>` symlink — Claude Code will not see a skill that only exists under `.github/skills/`.
- After adding an `AGENTS.md` to a new directory, add a sibling `CLAUDE.md` with `@AGENTS.md` in it — Claude Code will silently skip a directory's rules otherwise.
- Cross-references between customization files use relative paths; a broken one fails silently.
- On a **Windows** clone, the `.claude/skills/` symlinks only materialize when git is configured with `core.symlinks=true` and the account may create links (Developer Mode, or an elevated shell). Without that, git writes each one as a small text file containing the target path, Claude Code finds no skills, and — as with every gap in this layout — nothing reports an error. Check with `git config core.symlinks` before concluding a skill is broken. This repo supports a Windows workstation (see `windows/install-prereqs.ps1` in the `resume-tooling` skill), so the caveat is live, not theoretical.
- No file here may reference a path under `__untracked_stuff/` — see the root [`AGENTS.md`](../AGENTS.md).
- Agents do not commit. That rule is stated in the root `AGENTS.md` and applies to everything in this directory too.
