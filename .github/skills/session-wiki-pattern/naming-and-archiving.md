---
name: session-wiki-naming-and-archiving
description: "Reference for session-wiki-pattern — scope directory naming, archive invariants, and retrofitting the pattern onto existing work."
---

# Naming, archiving, retroactive bootstrap

> Companion to [`SKILL.md`](SKILL.md). Load when creating or renaming a scope directory, archiving cold material, or applying the pattern to work that predates it.

## Scope directory naming: handle + condensed title

A scope directory name is `<handle>-<condensed-title-slug>` — the durable handle (ticket ID, branch-derived identifier, or other stable identifier) followed by a short, human-readable slug condensed from the ticket/assignment title.

Illustrative shapes (hypothetical — see *The one-way reference rule* above):

```
__untracked_stuff/ABC-123-beacon-tracking-corner-cases/    # handle + condensed title
__untracked_stuff/ABC-456-keep-alive-validation-and-pr/
__untracked_stuff/docs-audit-2026-01/                      # non-ticket handle, same shape
```

A bare `__untracked_stuff/ABC-456/` is NOT sufficient. A directory listing is the cheapest discovery surface an agent or human has — a bare ID forces opening files just to learn what a scope is about, and after several tickets the listing becomes unreadable.

Rules:

1. **Handle first, verbatim.** Keep the exact ticket/branch identifier as the leading token so
ID-based search (`ls -d *123*`, `grep ABC-123`) still resolves.
2. **Slug is lowercase kebab-case,** roughly 2–5 words / ≤ 40 characters. Condense the title;
do not transcribe it. Drop filler ("update", "fix", "add") that every assignment shares.
3. **Separator is `-`, not `_`.** One separator style keeps the listing scannable.
4. **The slug names the SUBJECT, not the status.** No `-wip`, `-done`, `-v2`. Status lives in
the outer `AGENTS.md` banner and the tracker.
5. **Distinguish continuations by subject, not by number alone.** When a successor scope covers
the same feature (`ABC-455-keep-alive-via-config` → `ABC-456-keep-alive-validation-and-pr`), let the slug say what each one actually did.
6. **Derive the slug from a real source, not from guesswork:** the ticket title, the scope's
`README.md`/`AGENTS.md` heading, or the branch name — in that order of preference.

## Normalizing an existing bare-ID scope (audited rename)

Existing scopes named with a bare handle SHOULD be normalized. This is the one sanctioned exception to the freeze rule in *Ticket migration* below, and it is only safe as a single audited operation:

1. Derive each slug from that scope's own `README.md`/`AGENTS.md`/branch — never invent one.
2. Rename, then **rewrite every cross-scope path reference in the same operation** —
`../<old>/`, `../../<old>/`, and `__untracked_stuff/<old>/` — across scope docs AND any version-controlled file that cites the path (wiki shards, skills). Restrict the rewrite to path contexts: a blind substitution corrupts branch names, which share the `<ID>/` prefix shape (`ABC-456/keep_alive_beacon_tracking`).
3. Re-run a dead-link audit over the scope afterwards — mechanically where the host repo has a link-checking tool, otherwise by grepping the old scope name across scope documents and committed files.
4. Log the full old→new mapping in the acting scope's `session-wiki/log/`, and leave already-
written historical log chunks in other scopes unedited — they are an immutable audit trail; the mapping entry is what makes their old paths resolvable.


## Archive: `session-wiki-archive/` is a separate sibling, never nested

`session-wiki-archive/` sits next to `session-wiki/`, at the same level — never inside it. It holds COLD or superseded material, on the same "never modified once written" footing as `raw/`, but for material that is no longer live session state rather than fresh captures.

- `session-wiki/` MAY reference archive material.
- Nobody needs to open `session-wiki-archive/` under normal circumstances — the latest `session-wiki/` materials must be self-sufficient on their own.
- Archived material participates in future work strictly **as-needed**: pulled in only when explicitly relevant to a specific question, never loaded by default.

## Archiving invariants (checkable)

Derived from a real failure (a scope that archived to a scope-root `archive/`, left stale banners presenting superseded state as current, and accumulated dead references in its inner `AGENTS.md`):

1. **Archive location invariant.** Archived material lives ONLY in the sibling
`session-wiki-archive/` — never a scope-root `archive/`, never nested inside `session-wiki/`. Any other archive directory in a scope is a defect: MOVE its contents (unmodified) to `session-wiki-archive/` and record the move in `session-wiki/log/`.
2. **Context-stability invariant.** Outer and inner `AGENTS.md` files MUST NOT present branch heads,
status banners, task lists, completed-item inventories, or other volatile resume state. Status,
succession, and tracker-generation changes update the tracker and `session-wiki/log/` operations
log, leaving context files unchanged unless stable routing actually changes.
3. **Dead-reference audit at session close.** Before ending a session (and always during a
migration), audit the scope's outer/inner `AGENTS.md` and live tracker for references to files that were archived, moved, or never created; fix or remove each one. A link-checking tool, where the host repo has one, mechanizes this detection; absent one it is a grep and a read.


## Retroactive bootstrap

When applying the session-wiki pattern to a work area that predates the structure:
1. Create `raw/README.md` documenting what was captured before the session-wiki and where the evidence resides. Do NOT fabricate raw captures.
2. Create the `session-wiki/log/` directory with an initial chunk as an append-only record going forward. Only add a scope-root `logs/` too if genuine non-wiki narrative already exists to retroactively capture.
3. Record stable repo-local name mappings in the session-wiki index or owning design; record
   provenance gaps in the tracker, findings, or operations log rather than in loaded `AGENTS.md`.

No prior evidence needs to be retrofitted into `raw/` — an honest gap note in `raw/README.md` is sufficient.

