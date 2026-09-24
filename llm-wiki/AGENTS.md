# Resume Wiki Schema

This directory is the maintained knowledge layer for the resume repository: how the owner's career is documented, what the primary resume must look like, and how new accomplishments flow from casual capture to the published document. It is not the resume build input and must not change the generated files under `pandoc_resume/output/`.

Start at [`index.md`](index.md). It lists every page with a one-line purpose and a *load when* hint; read it first and then the smallest set of pages that answers the question.

## Layers

Four layers: `../markdown/` (outward-facing documents, edited only through `wiki/resume/` workflows), `../linkedin/` (generated, never hand-edited), `raw/` (immutable sources; brag entries edited in place with a `## Record history` line per change day) and `wiki/` (LLM synthesis: resume, workflows, sources, analysis, stories, dream-jobs, concepts, entities). Directory-by-directory detail: [`topics/layers.md`](topics/layers.md). Navigation: [`index.md`](index.md); there is no committed operations log.

## Size and shape

- Prefer Markdown pages of **500 lines or fewer; 1,024 lines is the hard ceiling**. Split by coherent subject before exceeding the preferred size; do not pad or compress prose to meet a limit. Routers contain navigation, not claim detail, and grow with the number of shards rather than accomplishments. Router pages (this file, `index.md`) stay well under 200 where practical. Coverage's physical design lives in [wiki/resume/coverage.md](wiki/resume/coverage.md#physical-design).
- A prose paragraph is one logical line; do not hard-wrap. Real newlines are for headings, list items, table rows, and paragraph breaks.
- Every synthesized page declares its Diataxis mode right after the title: `> **Doc type:** reference | how-to | explanation | tutorial`. One mode per file.
- Lowercase kebab-case filenames. Links are relative to the page making them.
- Front-load: the first screen of any page must let a reader decide whether to keep reading.

## Page conventions

- Every substantive claim links to one or more source files (`../markdown/...`, `raw/archive/...`, `raw/brag/...`). Prefer reference-style link definitions at the bottom of the page for sources cited repeatedly.
- Distinguish explicit source claims from synthesis or inference, and say which.
- When sources disagree, preserve the disagreement and name the sources; the primary resume wins for public claims.
- Keep raw sources unchanged, except brag entries, which are edited in place with a `## Record history` line per change day; a related later event gets its own entry, cross-linked by filename.
- Cross-reference instead of duplicating; a fact lives on one page and is linked from others.

## Sensitivity

Three tiers govern where information may live: **T0 public** (the primary resume only), **T1 private repo** (everything else committed, including brag entries and the references document), **T2 never committed** (employer-internal material and large files, which live in a session-wiki scratch scope). Definitions, promotion rules, and heuristics: `wiki/workflows/sensitivity-tiers.md`. Two hard rules apply everywhere: no committed file references a path under `__untracked_stuff/` (the root `TODO.md` is the single deliberate exception — see the root `AGENTS.md`), and third-party contact details are never copied out of the references document.

## Large and sensitive files

PDFs, exports, screenshots, and employer-internal notes are never committed (`.gitignore` covers `*.pdf`, `*.htm*`, `__untracked_stuff`). They wait in the maintainer's session-wiki scratch scope — `__untracked_stuff/<scope>/session-wiki/raw/` — and reach this wiki only as distilled, tier-checked text. The `session-wiki-pattern` skill (`.github/skills/session-wiki-pattern/SKILL.md`) owns that scope's structure.

**The one exception is a large source the owner has decided to preserve verbatim** — today, the Trello board exports under `raw/trello/`. Granting that exception is the owner's call and never an agent's. Carrying it out is `wiki/workflows/large-imports.md`: the uncompressed working copy stays in the scratch scope, and the committed copy is compressed to `.xz` and checksummed against its plaintext. The `large-import` skill owns the format decision and the tooling.

## Workflows

A table mapping each task (writing outward, editing the resume, brag capture and ingest, stories, LinkedIn, archiving, sensitivity, Obsidian, large imports, ingest, answering, lint) to its page is [`topics/workflows-table.md`](topics/workflows-table.md). **Writing anything outward: read `wiki/workflows/voice-and-prominence.md` first.** Lint checks are listed in that table.

## Operations log

The wiki's append-only operations history (ingests, archives, lint passes, decisions) is **not version-controlled**. It lives in the maintainer's session-wiki scope under `__untracked_stuff/<scope>/session-wiki/log/`, following the chunk and header conventions of the `session-wiki-pattern` skill. Committed pages carry the resulting knowledge, never the record of the session that produced it. When resuming maintenance work, read that scope's `tasks/assignment_tracker.md` first.

## Agents do not commit

Human review is mandatory before any commit. Prepare diffs and evidence; the owner commits and mirrors the resume to LinkedIn. The proposed commit message is written into the session-wiki scratch scope, never into a tracked file. Full rule and hand-off shape: the repository root [`AGENTS.md`](../AGENTS.md).
