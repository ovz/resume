# Resume repository — agent instructions

Personal resume repository for Oleg Zhylin. Markdown sources in `markdown/` are rendered by Pandoc into HTML, PDF, DOCX and RTF. `llm-wiki/` is the maintained knowledge layer behind the resume. This file is the router; the load-bearing rules live in the per-directory `AGENTS.md` files listed below.

## Agents do not commit

**Never run `git commit`, `git push`, `git tag`, or any other history-writing command.** Every change in this repository is reviewed by a human before it lands. This holds without exception, including for changes an agent is confident about and changes the owner appeared to pre-approve in conversation.

What an agent does instead:

1. Leave the work in the working tree, unstaged or staged, and say what changed and why.
2. Write the **proposed commit message** into the session-wiki scratch scope, never into a tracked file and never into the repo. The `session-wiki-pattern` skill owns that scope's layout; commit messages belong alongside its other session artifacts, under a `commits/` directory in the session-wiki. One file per proposed commit, each naming the exact paths it covers.
3. Hand off **through the tracker** — see the next section. The owner reviews, edits the message if needed, and commits.

`git status`, `git diff`, `git log`, `git show` and other read-only inspection are always fine. So is `git stash` when protecting uncommitted work from a destructive operation.

## Uncommitted work is the only thing git cannot give back

Everything in this repository is reviewed before it lands, which means the working tree routinely holds hours of work that exists nowhere else. Two rules follow, and both are about the asymmetry rather than the odds:

- **Before overwriting any region of a file that has uncommitted changes, secure a copy.** `git stash` is sanctioned for exactly this; a copy in the session scratch scope works too. Prefer a section-scoped edit to a whole-file write when the file holds in-flight work — restoring one section is recoverable, rewriting a file is not. Verify a restore by equality against the snapshot, never by eye.
- **When an answer could mean two things and one reading destroys work, ask.** "Rewrite it" and "add to it" are the same three words. The cost of asking is one turn; the cost of guessing wrong is unbounded, so the asymmetry decides it and not the probability.

## Hand-offs go in the assignment tracker, never in the chat response

**Anything the owner has to do, decide, verify, or answer is written into the session-wiki's `tasks/assignment_tracker.md`, under an `## Open for the owner` heading, at the moment it is discovered** — never into the chat response, which is not durable. The chat says *that* there are open items and where they live; it does not restate them. A response ending in a list of owner to-dos is a defect.

Full rationale, and the four tracker-hygiene rules (done items leave promptly, owner items re-judged on every resume, commit guides are owner assignments, `TODO.md` traces): [`.github/rules/handoffs-and-tracker.md`](.github/rules/handoffs-and-tracker.md). Read it before opening or resuming a tracker.

## Where the rules live

Per-directory `AGENTS.md` files are the primary, load-bearing instructions. Read the one covering the directory you are about to touch; do not rely on this router alone.

| Directory | File | Covers |
|---|---|---|
| `markdown/` | [`markdown/AGENTS.md`](markdown/AGENTS.md) | Editing the outward-facing resume and references documents |
| `llm-wiki/` | [`llm-wiki/AGENTS.md`](llm-wiki/AGENTS.md) | The knowledge layer: schema, sensitivity tiers, ingest and synthesis workflows |
| `.github/` | [`.github/AGENTS.md`](.github/AGENTS.md) | How this repo's agent customizations are laid out and kept discoverable |

`pandoc_resume/` is a git submodule tracking a fork of `mszep/pandoc_resume`. It supplies the ConTeXt and CSS style assets only. **Do not edit files inside it** — changes there belong upstream in the fork, and local edits break the build's re-merge story.

## Tracking professional history

This repository is a pipeline: `llm-wiki/raw/brag/` → `llm-wiki/wiki/concepts/accomplishments-by-domain.md` → `markdown/`. **Each hop is a rewrite, never a copy**; skipping a hop skips the sensitivity and depth checks. The routing table (recording an accomplishment, stories, coverage, resume edits, dream jobs, LinkedIn, sensitivity, archiving, large imports) is [`.github/rules/professional-history.md`](.github/rules/professional-history.md).

## How the record gets told — a foundation pillar

Anything written to be read or said outward goes through [`llm-wiki/wiki/workflows/voice-and-prominence.md`](llm-wiki/wiki/workflows/voice-and-prominence.md) **before** it is drafted: one voice with a register per era; prominence follows evidence (false humility is a defect, as overclaiming is); blocked, frozen and never-shipped work is tellable, and honest telling never requires disclosure. Summary of the three rules: [`.github/rules/voice-pillar.md`](.github/rules/voice-pillar.md).

## Building

`script/pandoc_resume.sh all` builds html, pdf, docx, rtf, the LinkedIn blocks, then verifies; a `NO IMAGE` line from `verify` is a build failure. Artifacts are gitignored — never commit generated output, except `linkedin/`, which is tracked because it is generated and never hand-edited. Commands, the LinkedIn character budgets and the paste workflow: [`.github/rules/building.md`](.github/rules/building.md).

## Sensitivity

Three tiers govern what may be written where: **T0 public** (the primary resume only), **T1 private repo** (everything else committed), **T2 never committed** (employer-internal material, large binaries). Definitions and promotion rules: [`llm-wiki/wiki/workflows/sensitivity-tiers.md`](llm-wiki/wiki/workflows/sensitivity-tiers.md).

Two hard rules apply everywhere:

- No committed file may reference a path under `__untracked_stuff/`. A committed file must stand alone in a fresh clone; a pointer into scratch is dead on arrival for every other reader, and dead *silently*. Describe the shape of the scratch convention if you must, but never a concrete scratch path. **The one exception is the root `TODO.md`**, the owner's worklist: it names every session-wiki assignment tracker that still holds action items — in this repository and in its [sibling career repositories](llm-wiki/wiki/workflows/career-repositories.md) — so that `git diff` shows what is outstanding. An agent adds the line when a tracker gains owner items and removes it when none remain. `TODO.md` is otherwise the owner's scratch space, and the owner may delete a trace whenever they like. No other committed file may cite those paths.
- Third-party contact details are never copied out of `markdown/Oleg.Zhylin.professional.references.md`.
- Colleague names, roles and the substance of working relationships are recorded in full at T1 — they are the professional record, not an aside to it. Capture is not disclosure: what the owner chooses to say in an interview is a separate judgement, and names still come out at T0.

## Skills

Reusable procedures live in `.github/skills/<name>/SKILL.md`, the single copy of each (brag-capture, resume-editing, linkedin-publish, resume-tooling, pdf-extraction, large-import, session-wiki-pattern); load one when its `description` matches the task. Claude Code scans `.claude/skills/`, so each has a symlink there. List with triggers and the bridge: [`.github/rules/skills-list.md`](.github/rules/skills-list.md).

## Reading this file with Claude Code

Claude Code reads `CLAUDE.md`, not `AGENTS.md`, so it never sees this router — or any nested `AGENTS.md` — on its own. The root [`CLAUDE.md`](CLAUDE.md) and a `CLAUDE.md` in every directory listed above import the local `AGENTS.md` via `@AGENTS.md`, which is how the content actually reaches Claude Code. Do not rely on that import from inside this file or any other `AGENTS.md` — they must stay literal, tool-agnostic Markdown for every other reader.
