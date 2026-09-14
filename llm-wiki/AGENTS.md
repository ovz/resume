# Resume Wiki Schema

This directory is the maintained knowledge layer for the resume repository: how the owner's career is documented, what the primary resume must look like, and how new accomplishments flow from casual capture to the published document. It is not the resume build input and must not change the generated files under `pandoc_resume/output/`.

Start at [`index.md`](index.md). It lists every page with a one-line purpose and a *load when* hint; read it first and then the smallest set of pages that answers the question.

## Layers

- `../markdown/` — **outward-facing documents** and the pandoc build input. Today: the primary resume `Oleg.Zhylin.resume.achievements.md` (public, mirrored to LinkedIn), the `Oleg.Zhylin.resume.embedded.md` variant, and `Oleg.Zhylin.professional.references.md` (private). Files here are edited only through the workflows in `wiki/resume/`.
- `../linkedin/` — **generated**, and tracked for that reason. Marked sections of the primary resume rendered to the plain text LinkedIn accepts, checked against its per-field character limits. Never edited by hand and never a source: a changed file there means a profile field to re-paste. See `wiki/resume/primary-resume.md` § *The LinkedIn mirror*.
- `raw/` — **source material, immutable once written** (brag entries excepted, below).
  - `raw/archive/` — superseded documents moved out of `../markdown/` (see `wiki/workflows/archive-source.md`). Readable and citable; never edited.
  - `raw/brag/` — the **Resume Brag File** drop zone: one file per accomplishment, dated by the accomplishment, written casually when it happens and augmented as evidence accrues; every change day is logged in the entry's trailing `## Record history` (see `wiki/workflows/brag-file.md`).
  - `raw/llm-wiki.md` — the abstract pattern this directory instantiates. Repo-specific rules here override it.
- `wiki/` — **synthesis written by the LLM**, organized as:
  - `wiki/resume/` — the always-on shard for editing the primary resume (structure and cut points, link conventions, update workflow, and the coverage map that says which captured material has not reached the resume yet).
  - `wiki/workflows/` — how-tos and rules that govern the repo's state (brag capture/ingest, **voice and prominence** — the storytelling pillar, archiving, sensitivity tiers, large imports, the Obsidian vault).
  - `wiki/sources/` — one summary page per source document: role, vintage, what it uniquely contributes, harvest status, tier. Plus the brag ledger.
  - `wiki/analysis/` — durable answers to questions that came up, including researched external context. Employer research lives under `wiki/analysis/employers/<employer>/`, one dated page per piece of research (`YYYY-MM-DD-<subject>.md`) — past employers and prospective ones alike, so preparing for a conversation starts in one folder.
  - `wiki/stories/` — **told-able stories** graduated from brag entries, grouped by cluster: a hub note per cluster (`<cluster>.md`) beside a folder of its stories, and a [story map](wiki/stories/story-map.md). See `wiki/workflows/brag-stories.md`.
  - `wiki/dream-jobs/` — **where the career could go next**: a hub note plus one page per candidate direction, each graded on what the record supports. Candidates carry an `origin` property — `owner` for the owner's own ideas, `suggested` for an agent's — and **an agent may only ever add `suggested`**. See `wiki/dream-jobs/dream-job-hub.md`.
  - `wiki/concepts/`, `wiki/entities/`, `wiki/overview.md` — the career synthesis proper.
  - `wiki/sources.md` — the source map: every source's tier and disposition on one page.
- `../archive/` — historical personal material predating the wiki; classified in `wiki/sources/`, not synthesized.
- `index.md` — navigation. There is **no committed operations log**; see *Operations log* below.

## Size and shape

- Every Markdown file in this directory stays **under roughly 200–500 lines; 500 is the ceiling**. Split by topic before exceeding it. Router pages (this file, `index.md`) stay well under 200. Short is fine — pages are sized by knowledge, not padded.
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

| Need | Page |
|---|---|
| **Write anything outward — a story, a resume line, a LinkedIn block, a reading list** | `wiki/workflows/voice-and-prominence.md` **first**: one voice across era registers, prominence that follows evidence, and honest handling of blocked or unshipped work |
| Decide where the career should point next, or judge a role against the record | `wiki/dream-jobs/dream-job-hub.md`; market evidence in `wiki/analysis/2026-09-13-specializations-landscape.md` |
| Refine, improve, or update the primary resume | `wiki/resume/update-workflow.md` (load `wiki/resume/primary-resume.md`, `link-conventions.md` and `coverage.md` first) |
| See what the resume is missing, or how much is covered | `wiki/resume/coverage.md` |
| Capture an accomplishment right now, in any format | `wiki/workflows/brag-file.md` §§ *Part 0*–*Part 1* |
| Fold captured accomplishments into the wiki | `wiki/workflows/brag-file.md` § *Part 2* |
| Graduate entries into stories, or build a reading list for an interview, event or employer | `wiki/workflows/brag-stories.md` |
| Work that spans the resume, job-search and C++ training repositories, or Claude Cowork | `wiki/workflows/career-repositories.md` |
| Get the generated blocks onto the LinkedIn profile, or answer whether that can be automated | `wiki/workflows/linkedin-publish.md` |
| Retire a superseded `../markdown/` document | `wiki/workflows/archive-source.md` |
| Decide whether something may be written down here | `wiki/workflows/sensitivity-tiers.md` |
| Change the Obsidian vault, the graph, or the brag entry schema | `wiki/workflows/obsidian-vault.md` |
| Preserve a source too large to commit as-is | `wiki/workflows/large-imports.md` (the owner decides the tier first; an agent never grants the exception) |
| Ingest any other new source | Read it fully; write or update its `wiki/sources/` page; update `wiki/sources.md`, the affected synthesis pages, and `index.md`; log the ingest (below). |
| Answer a question | `index.md` → smallest set of pages → answer with source links and stated uncertainty. File durable answers under `wiki/analysis/` (create on first use) and index them. |
| Lint | Broken relative links; pages over 500 lines; claims without sources; `__untracked_stuff` references; orphan pages; `raw/brag/` entries missing from the ledger; entries missing from `wiki/resume/coverage.md`, or coverage totals that no longer match its own tables; `wiki/sources/` pages whose harvest map is stale; dream-job candidates whose `origin` was changed to `owner` without the owner saying so, or whose evidence grade no longer matches the entries they cite; Obsidian colour groups that disagree with the legend in `wiki/workflows/obsidian-vault.md`. Record findings in the operations log. |

## Operations log

The wiki's append-only operations history (ingests, archives, lint passes, decisions) is **not version-controlled**. It lives in the maintainer's session-wiki scope under `__untracked_stuff/<scope>/session-wiki/log/`, following the chunk and header conventions of the `session-wiki-pattern` skill. Committed pages carry the resulting knowledge, never the record of the session that produced it. When resuming maintenance work, read that scope's `tasks/assignment_tracker.md` first.

## Agents do not commit

Human review is mandatory before any commit. Prepare diffs and evidence; the owner commits and mirrors the resume to LinkedIn. The proposed commit message is written into the session-wiki scratch scope, never into a tracked file. Full rule and hand-off shape: the repository root [`AGENTS.md`](../AGENTS.md).
