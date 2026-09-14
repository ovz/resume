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

**Anything the owner has to do, decide, verify, or answer is written into the session-wiki's `tasks/assignment_tracker.md`, under an `## Open for the owner` heading, at the moment it is discovered.** Not at the end of the session, and not into the chat.

The chat response says *that* there are open items and where they live. It does not restate them.

Why the rule is absolute:

- **A chat response is not durable.** It disappears with the session, it is not on disk, it cannot be reopened in the editor, and a fresh session cannot read it. An item that exists only in a chat message is an item that will be lost — silently, because nothing reports it missing.
- **The tracker is the resume token.** It is the first thing any session reads. Putting the owner's items anywhere else guarantees the next agent does not know they are outstanding.
- **The owner works from one list.** Two lists — one in the tracker, one scrolled past in a terminal — is worse than either alone, because neither is trustworthy.

A response that ends with a list of things for the owner to do is a defect, even when the list is correct. The correct ending points at the tracker.

If work is under way and no scope exists yet, that is the signal to create one (`session-wiki-pattern` skill), not a licence to hand off in chat.

## Where the rules live

Per-directory `AGENTS.md` files are the primary, load-bearing instructions. Read the one covering the directory you are about to touch; do not rely on this router alone.

| Directory | File | Covers |
|---|---|---|
| `markdown/` | [`markdown/AGENTS.md`](markdown/AGENTS.md) | Editing the outward-facing resume and references documents |
| `llm-wiki/` | [`llm-wiki/AGENTS.md`](llm-wiki/AGENTS.md) | The knowledge layer: schema, sensitivity tiers, ingest and synthesis workflows |
| `.github/` | [`.github/AGENTS.md`](.github/AGENTS.md) | How this repo's agent customizations are laid out and kept discoverable |

`pandoc_resume/` is a git submodule tracking a fork of `mszep/pandoc_resume`. It supplies the ConTeXt and CSS style assets only. **Do not edit files inside it** — changes there belong upstream in the fork, and local edits break the build's re-merge story.

## Tracking professional history

This repository is a pipeline, not a single document. An accomplishment reaches the resume in three hops, and **each hop is a rewrite, never a copy**:

```
llm-wiki/raw/brag/     →   llm-wiki/wiki/concepts/        →   markdown/
one dated file per         accomplishments-by-domain.md       the public resume
accomplishment,            plus the ledger, entities          and any tailored
captured when it happens   and themes                         variant
```

| Need | Start here |
|---|---|
| Record something that just happened, in any format | `brag-capture` skill → [`llm-wiki/wiki/workflows/brag-file.md`](llm-wiki/wiki/workflows/brag-file.md) §§ *Part 0*–*Part 1* |
| Fold captured entries into the knowledge layer | `brag-capture` skill → same page, § *Part 2* |
| Turn entries into told-able stories, or get a reading list for an interview, event or employer | `brag-capture` skill → [`llm-wiki/wiki/workflows/brag-stories.md`](llm-wiki/wiki/workflows/brag-stories.md) |
| See what the resume is missing, and how much is covered | [`llm-wiki/wiki/resume/coverage.md`](llm-wiki/wiki/resume/coverage.md) |
| Put something on the outward-facing resume | `resume-editing` skill → [`llm-wiki/wiki/resume/update-workflow.md`](llm-wiki/wiki/resume/update-workflow.md) |
| Decide where this career should point next, or judge a role against the record | [`llm-wiki/wiki/dream-jobs/dream-job-hub.md`](llm-wiki/wiki/dream-jobs/dream-job-hub.md) — candidates graded on evidence, the owner's own ideas marked apart from an agent's |
| Work across the career repositories — this one holds the past, the job-search and C++ training repositories hold the search and the future | [`llm-wiki/wiki/workflows/career-repositories.md`](llm-wiki/wiki/workflows/career-repositories.md) — what each owns, how knowledge moves between them, where Claude Cowork fits |
| Decide how often to touch the LinkedIn profile, and what actually gets it found | [`llm-wiki/wiki/analysis/2026-09-14-linkedin-profile-visibility.md`](llm-wiki/wiki/analysis/2026-09-14-linkedin-profile-visibility.md) |
| Refresh the LinkedIn profile from the resume | `linkedin-publish` skill → [`llm-wiki/wiki/workflows/linkedin-publish.md`](llm-wiki/wiki/workflows/linkedin-publish.md) |
| Find out whether the LinkedIn update can be automated | Same page, § *The answer, first* — it cannot, and the research is recorded so it is not repeated |
| Decide whether a fact may be written down at all | [`llm-wiki/wiki/workflows/sensitivity-tiers.md`](llm-wiki/wiki/workflows/sensitivity-tiers.md) |
| Retire a document that has stopped being outward-facing | [`llm-wiki/wiki/workflows/archive-source.md`](llm-wiki/wiki/workflows/archive-source.md) |
| Preserve a source too large to commit as-is | `large-import` skill → [`llm-wiki/wiki/workflows/large-imports.md`](llm-wiki/wiki/workflows/large-imports.md) |
| Ingest any other source, answer a question from the wiki, or lint it | [`llm-wiki/AGENTS.md`](llm-wiki/AGENTS.md) § *Workflows* |

Skipping a hop is the failure this layout exists to prevent: text copied straight from a brag entry into the resume has passed neither the sensitivity check nor the depth check, and both are easy to lose silently.

## How the record gets told — a foundation pillar

Anything written to be read or said outward — a story, a resume line, a LinkedIn block, a reading list — goes through [`llm-wiki/wiki/workflows/voice-and-prominence.md`](llm-wiki/wiki/workflows/voice-and-prominence.md) **before** it is drafted. It is not a style guide; it is load-bearing, and it carries three rules that the rest of this repository assumes:

- **One voice, many registers.** Every telling sounds like the same person, so the owner drops into storytelling mode from the first line — but thirty years cannot be told in one register, and the page defines one per era. The mode is role-play: channel the genuine past self, then let the present self narrate.
- **Prominence follows evidence.** How loudly a claim is made is set by support *and* impact, never by stated impact alone. **False humility is a defect**, exactly as overclaiming is: a well-grounded, high-impact accomplishment that appears nowhere prominent is a bug in the record.
- **Blocked, frozen and never-shipped work is tellable.** What shipped, what was built then stopped, and what was argued for and refused — each has an honest sentence, and the lesson from a blocker is part of the win. Honest telling never requires disclosure; the boundary stays [the sensitivity tiers](llm-wiki/wiki/workflows/sensitivity-tiers.md).

## Building

```bash
script/bootstrap.sh              # fresh machine: submodule + toolchain + first build
script/pandoc_resume.sh all      # html, pdf, docx, rtf, linkedin, then verify
script/pandoc_resume.sh linkedin # regenerate the LinkedIn copy-paste blocks
script/pandoc_resume.sh verify   # assert the portrait PNG is embedded in every artifact
script/pandoc_resume.sh clean
```

Artifacts land in `pandoc_resume/output/` and are gitignored, as are `*.pdf` and `*.htm*` repo-wide. The build must never be "fixed" by committing generated output.

Pasting the result into the profile is [its own workflow](llm-wiki/wiki/workflows/linkedin-publish.md): `script/linkedin-sync.py status` says which blocks have not reached LinkedIn, and that record is committed so it survives a commit and a fresh clone. **There is no API for it** — the write path exists but is behind a closed partner permission, and browser automation is prohibited; the workflow page carries the evidence.

**`linkedin/` is the one tracked exception**, and it is tracked *because* it is generated. LinkedIn accepts no formatting and caps each field — 2,600 characters for the About section, 2,000 per Experience entry — so the profile cannot be a copy of the resume; it is a rendering of it, produced from sections marked `<!-- linkedin: <slug> limit=<n> -->` in the Markdown. Updating the profile is a human pasting into a web form, so the committed diff is the only thing that can say *which* fields have drifted and need re-pasting: a changed file is a field to paste, an unchanged one is a field to leave alone. Files there are never hand-edited, and a block that outgrows its field fails the build rather than being silently truncated on paste. Details: [`.github/skills/resume-tooling/SKILL.md`](.github/skills/resume-tooling/SKILL.md) § *The LinkedIn export*.

Every artifact is expected to embed the portrait image from `markdown/assets/`. Each output format embeds it by a different mechanism, so it fails silently and per-format; `script/pandoc_resume.sh verify` is the check that catches it. Treat a `NO IMAGE` line from `verify` as a build failure.

## Sensitivity

Three tiers govern what may be written where: **T0 public** (the primary resume only), **T1 private repo** (everything else committed), **T2 never committed** (employer-internal material, large binaries). Definitions and promotion rules: [`llm-wiki/wiki/workflows/sensitivity-tiers.md`](llm-wiki/wiki/workflows/sensitivity-tiers.md).

Two hard rules apply everywhere:

- No committed file may reference a path under `__untracked_stuff/`. A committed file must stand alone in a fresh clone; a pointer into scratch is dead on arrival for every other reader, and dead *silently*. Describe the shape of the scratch convention if you must, but never a concrete scratch path. **The one exception is the root `TODO.md`**, the owner's worklist: it names every session-wiki assignment tracker that still holds action items — in this repository and in its [sibling career repositories](llm-wiki/wiki/workflows/career-repositories.md) — so that `git diff` shows what is outstanding. An agent adds the line when a tracker opens items and removes it when the tracker closes; no other committed file may cite those paths.
- Third-party contact details are never copied out of `markdown/Oleg.Zhylin.professional.references.md`.
- Colleague names, roles and the substance of working relationships are recorded in full at T1 — they are the professional record, not an aside to it. Capture is not disclosure: what the owner chooses to say in an interview is a separate judgement, and names still come out at T0.

## Skills

Reusable procedures live in `.github/skills/<name>/SKILL.md`, the single copy of each. Load one when its `description` matches the task:

- `brag-capture` — recording an accomplishment, folding captured entries into the knowledge layer, and graduating them into stories and reading lists.
- `resume-editing` — editing an outward-facing resume document.
- `linkedin-publish` — getting the generated blocks onto the LinkedIn profile, and the researched answer to whether any of it can be automated.
- `resume-tooling` — setting up or repairing the toolchain on a workstation.
- `pdf-extraction` — ingesting a PDF into a wiki.
- `large-import` — preserving a source file too large to commit as-is, compressed and checksummed.
- `session-wiki-pattern` — planning or maintaining a long, multi-step assignment.

Not every agent scans `.github/skills/` on its own — Claude Code, for one, only scans `.claude/skills/`. Where a tool needs a different path, this repo adds a symlink back to the real folder rather than a second copy; see [`.github/AGENTS.md`](.github/AGENTS.md) § *The two bridges Claude Code needs* for the current list.

See [`.github/AGENTS.md`](.github/AGENTS.md) for the full customization map and the conventions each file type must follow.

## Reading this file with Claude Code

Claude Code reads `CLAUDE.md`, not `AGENTS.md`, so it never sees this router — or any nested `AGENTS.md` — on its own. The root [`CLAUDE.md`](CLAUDE.md) and a `CLAUDE.md` in every directory listed above import the local `AGENTS.md` via `@AGENTS.md`, which is how the content actually reaches Claude Code. Do not rely on that import from inside this file or any other `AGENTS.md` — they must stay literal, tool-agnostic Markdown for every other reader.
