> Shard of the root [`AGENTS.md`](../../AGENTS.md).

# Skills

Reusable procedures live in `.github/skills/<name>/SKILL.md`, the single copy of each. Load one when its `description` matches the task:

- `brag-capture` — recording an accomplishment, folding captured entries into the knowledge layer, and graduating them into stories and reading lists.
- `resume-editing` — editing an outward-facing resume document.
- `linkedin-publish` — getting the generated blocks onto the LinkedIn profile, and the researched answer to whether any of it can be automated.
- `resume-tooling` — setting up or repairing the toolchain on a workstation.
- `pdf-extraction` — ingesting a PDF into a wiki.
- `large-import` — preserving a source file too large to commit as-is, compressed and checksummed.
- `session-wiki-pattern` — planning or maintaining a long, multi-step assignment.

Not every agent scans `.github/skills/` on its own — Claude Code, for one, only scans `.claude/skills/`. Where a tool needs a different path, this repo adds a symlink back to the real folder rather than a second copy; see [`.github/AGENTS.md`](../../.github/AGENTS.md) § *The two bridges Claude Code needs* for the current list.

See [`.github/AGENTS.md`](../../.github/AGENTS.md) for the full customization map and the conventions each file type must follow.
