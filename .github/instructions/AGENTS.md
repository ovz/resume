# Path-scoped instructions

Files here are **path-scoped instructions**: they are injected automatically when the file being edited matches their `applyTo` glob. Use this mechanism for rules that must fire based on *where* an edit lands, without the agent having to choose to load anything.

## Required shape

Every file must be named `*.instructions.md` — a plain `.md` file in this directory is ignored silently. Frontmatter:

```yaml
---
name: resume-editing                # optional
description: "Short summary."       # optional
applyTo: "markdown/**/*.md"         # the glob that triggers injection
---
```

Subdirectories are searched recursively, so instructions may be grouped once there are enough of them to warrant it.

## What belongs here, and what does not

Keep these files thin. The load-bearing rules live in the per-directory `AGENTS.md` file for the path in question; an instructions file points at it and restates only the non-negotiables. Three always-on mechanisms already cover this repo (`AGENTS.md` at root and per directory, `copilot-instructions.md`, `CLAUDE.md`), so content duplicated here is paid for on every matching request and drifts from its source.

A rule that should be loaded *on demand for a task* rather than *automatically for a path* is a skill, in [`../skills/`](../skills/), not an instructions file. `applyTo` is not a skill field.

The full customization map and the conventions for each file type: [`../AGENTS.md`](../AGENTS.md).
