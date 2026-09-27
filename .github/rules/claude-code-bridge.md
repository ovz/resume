> Shard of the root [`AGENTS.md`](../../AGENTS.md). Load when the task matches its title.

# Reading `AGENTS.md` with Claude Code

Claude Code reads `CLAUDE.md`, not `AGENTS.md`, so it never sees the root router — or any nested `AGENTS.md` — on its own. The root [`CLAUDE.md`](../../CLAUDE.md) and a `CLAUDE.md` in every directory listed in the router's table import the local `AGENTS.md` via `@AGENTS.md`, which is how the content actually reaches Claude Code. Do not rely on that import from inside the router or any other `AGENTS.md` — they must stay literal, tool-agnostic Markdown for every other reader.

The full layout conventions and the two bridges (`AGENTS.md` → `CLAUDE.md`, `.github/skills/` → `.claude/skills/`) are in [`.github/AGENTS.md`](../AGENTS.md).

The root `CLAUDE.md` is intentionally an import, not a copy — see `.github/AGENTS.md` § *Single source of truth*. The imported router already carries the "agents do not commit" guardrail, so `CLAUDE.md` does not restate it.
