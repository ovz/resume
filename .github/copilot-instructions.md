# Copilot instructions

`.github/copilot-instructions.md` is **the** place for GitHub Copilot–specific instructions and configuration — the Copilot counterpart to root [`CLAUDE.md`](../CLAUDE.md). Universal, tool-agnostic rules do not belong here; they belong in `AGENTS.md`. (`.github/instructions/*.instructions.md` is a different, narrower Copilot mechanism — path-scoped rules applied by `applyTo` glob, not general always-on instructions; see its own [`AGENTS.md`](instructions/AGENTS.md).)

This file itself is loaded into every Copilot Chat request per GitHub's own docs, in principle on any surface Copilot Chat runs on. Whether Copilot *also* reads `AGENTS.md` automatically is a narrower, VS-Code-specific claim: it needs the experimental `chat.useAgentsMdFile` / `chat.useNestedAgentsMdFiles` settings turned on, which this repo does in [`../.vscode/settings.json`](../.vscode/settings.json) — other Copilot surfaces (CLI, Visual Studio, JetBrains, github.com) aren't verified here and may differ. Unlike Claude Code, Copilot needs no per-directory *import* bridge for `AGENTS.md` content, once that setting is on; see [`AGENTS.md`](AGENTS.md) § *VS Code specifics* for the exact settings and their sharp edges.

Start at [`../AGENTS.md`](../AGENTS.md) — it is the router, and it also links the skills in [`skills/`](skills/).
