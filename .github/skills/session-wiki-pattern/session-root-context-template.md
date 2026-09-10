# <SCOPE-ID> — Session Context (outer, thin pointer)

> Copy this file to `__untracked_stuff/<scope>/AGENTS.md` and fill in the stable scope identity once. It is a cache-stable routing pointer, never a status, task, evidence, or navigation index.

**Scope:** <SCOPE-ID> — <short description>

## Resume
Read [`tasks/assignment_tracker.md`](tasks/assignment_tracker.md) first; it is the sole task/status routing index and resume token. Then read [`session-wiki/AGENTS.md`](session-wiki/AGENTS.md) for stable session routing.

## Stable routing

- [`tasks/assignment_tracker.md`](tasks/assignment_tracker.md) — resume state and task/status routing.
- [`session-wiki/index.md`](session-wiki/index.md) — session knowledge navigation.
- [`session-wiki/log/index.md`](session-wiki/log/index.md) — session-wiki operations history.

Do not add mutable status or content inventories here. Follow the `session-wiki-pattern` skill for physical design and archive rules.

## Agents do not commit
Human review is mandatory before any commit; proposed messages go in `session-wiki/commits/`. See the `session-wiki-pattern` skill § *Proposed commits*, plus whatever the host repo's own instructions say.
