# CLAUDE.md

The instructions for this repository live in [`AGENTS.md`](AGENTS.md). Read it first; it routes to the per-directory `AGENTS.md` files that carry the actual rules.

This file is intentionally a pointer, not a copy — see [`.github/AGENTS.md`](.github/AGENTS.md) § *Single source of truth*.

One rule is repeated here because it is a guardrail rather than guidance, and it must be visible at every entry point:

> **Agents do not commit.** Never run `git commit`, `git push`, or any other history-writing command. Leave changes in the working tree, write the proposed commit message into the session-wiki scratch scope, and hand off to the owner for review.
