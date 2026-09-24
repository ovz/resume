> Shard of [`AGENTS.md`](AGENTS.md).

# VS Code specifics — read this before trusting a setting name

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
