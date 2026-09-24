> Shard of [`../AGENTS.md`](../AGENTS.md).

# Layers

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
  - `wiki/stories/` — **told-able stories** graduated from brag entries, grouped by cluster: a hub note per cluster (`<cluster>.md`) beside a folder of its stories, and a [story map](../wiki/stories/story-map.md). See `wiki/workflows/brag-stories.md`.
  - `wiki/dream-jobs/` — **where the career could go next**: a hub note plus one page per candidate direction, each graded on what the record supports. Candidates carry an `origin` property — `owner` for the owner's own ideas, `suggested` for an agent's — and **an agent may only ever add `suggested`**. See `wiki/dream-jobs/dream-job-hub.md`.
  - `wiki/concepts/`, `wiki/entities/`, `wiki/overview.md` — the career synthesis proper.
  - `wiki/sources.md` — the source map: every source's tier and disposition on one page.
- `../archive/` — historical personal material predating the wiki; classified in `wiki/sources/`, not synthesized.
- `index.md` — navigation. There is **no committed operations log**; see *Operations log* below.
