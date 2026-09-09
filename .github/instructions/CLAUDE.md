# CLAUDE.md

@AGENTS.md

Claude Code does not read `AGENTS.md` on its own; this file imports [`AGENTS.md`](AGENTS.md) so the path-scoped-instructions rules load automatically when Claude works in this directory. Note that the `applyTo`-glob auto-injection mechanism described there is a GitHub Copilot / VS Code feature — Claude Code does not implement it and will not auto-apply files here based on the edited path.
