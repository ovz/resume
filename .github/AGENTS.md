# Agent customization layout

How this repository's instructions for AI coding agents are organized. Read this before adding, moving, or renaming any customization file — every file type is matched by an exact filename or glob, and a file in the wrong shape is ignored *silently*.

## Layout, discovery and shape rules

Which customization file each tool reads, and the shape each file type must have to be discovered, are the agentic_linux repo's own `.github/AGENTS.md` (§ *The conventions*, § *Required shapes*) — read there, not here; its `tools/wiki_lint.py` checks them. What follows is what is intrinsic to this repo: its VS Code configuration, its two Claude Code bridges, and its Windows caveat.

## Single source of truth

`AGENTS.md` files carry the content; `CLAUDE.md` and `copilot-instructions.md` are thin pointers, because all of them are always-on and a copy is paid for on every request and drifts. When a rule changes, change the `AGENTS.md` that owns it and nothing else. A skill body or wiki page links to the rule rather than restating it. The full reasoning, and the guardrails that are deliberately repeated at every entry point, are in the agentic_linux repo's `.github/AGENTS.md` under the same heading.

## VS Code specifics

One editor's Copilot Chat extension has experimental settings (`chat.useAgentsMdFile`, `chat.useNestedAgentsMdFiles`, `chat.useClaudeMdFile` — a trap: it does not gate Claude Code — and others) carried in `.vscode/settings.json`. They affect nothing outside VS Code. Table and cautions: [`vscode-settings.md`](vscode-settings.md).

## The two bridges Claude Code needs

Claude Code's rule is simple and worth stating plainly: **it reads `CLAUDE.md`, not `AGENTS.md`, and it scans `.claude/skills/`, not `.github/skills/`.** Everything below exists to close that gap without duplicating content or moving the canonical files. Two consequences are easy to miss: a nested `CLAUDE.md` loads only when Claude Code reads a file in its directory, and Claude Code has **no** `applyTo` path-scoped injection, so a rule in `instructions/*.instructions.md` reaches Claude only through the `AGENTS.md` it points at.

- **AGENTS.md → CLAUDE.md.** Every directory with a load-bearing `AGENTS.md` (root, here, `instructions/`, `../markdown/`, `../llm-wiki/`) has a sibling `CLAUDE.md` containing `@AGENTS.md` — Claude Code's file-import syntax — plus a one-line explanation. The import is what actually loads the content; the prose around it is for a human or another agent opening the file. Do not put `@`-imports inside an `AGENTS.md` file itself — Copilot and other AGENTS.md-standard readers treat that file as literal text, not an import directive, and would show the raw `@AGENTS.md` string to the user.
- **`.github/skills/` → `.claude/skills/` and `.agents/skills/`.** Each of those two paths is one symlink to `../.github/skills`. The skill's real files — `SKILL.md`, scripts, templates — live only under `.github/skills/`; the symlinks make Claude Code's and Codex's scanners find them without a second copy to drift, and a new skill folder is picked up with no further step. Git stores the links as symlinks (mode `120000`), which a Windows clone only reproduces when `core.symlinks` is enabled — see *Keeping it honest* below.

## Keeping it honest

- On a **Windows** clone, the `.claude/skills` and `.agents/skills` symlinks only materialize when git is configured with `core.symlinks=true` and the account may create links (Developer Mode, or an elevated shell). Without that, git writes each as a small text file containing the target path, Claude Code finds no skills, and — as with every gap in this layout — nothing reports an error. Check with `git config core.symlinks` before concluding a skill is broken. This repo supports a Windows workstation (see `windows/install-prereqs.ps1` in the `resume-tooling` skill), so the caveat is live, not theoretical.
