# Resume Wiki Index

Navigation for the synthesized resume knowledge base. Source files remain authoritative; wiki pages are maintained summaries. Each entry says what the page is and **when to load it** so a reader can pull the minimum into context. Schema and conventions: [AGENTS.md](AGENTS.md).

## Start here

- [Career overview](wiki/overview.md) — *explanation.* The arc in four chapters and what makes it distinctive. **Load when** you need the story before anything else.
- [Source map](wiki/sources.md) — *reference.* Every source document, its tier, disposition, and summary page. **Load when** about to cite or edit any source.

## Primary resume (always-on shard for resume work)

- [Primary resume — structure, cut points, editing rules](wiki/resume/primary-resume.md) — *reference.* What the public resume is, the half-page / one-page / two-page cut principle, section and style conventions. **Load before any edit to `markdown/Oleg.Zhylin.resume.achievements.md`.**
- [Link conventions](wiki/resume/link-conventions.md) — *reference.* Wayback Machine snapshots as the default hyperlink; URL forms, key naming, observed inconsistencies. **Load when** adding or touching any link in an outward-facing document.
- [Update the outward-facing resume](wiki/resume/update-workflow.md) — *how-to.* The deliberate edit pass: draft, place at the right depth, link-check, sensitivity-check, render, lint, hand off. **Load when** asked to refine/improve/update the resume or produce a tailored variant.
- [Resume coverage map](wiki/resume/coverage.md) — *reference.* Brag material grouped into threads, decomposed into claims, each marked reflected / partial / absent in the resume, with an estimated coverage percentage. **Load when** deciding what a resume pass should cover, or after ingesting or promoting anything.

## Workflows

- [Resume Brag File — capture and ingest](wiki/workflows/brag-file.md) — *how-to.* Capture the input verbatim, write or enrich the entry in `raw/brag/`, then fold entries into the wiki and the coverage map later. **Load when** the owner says "add this to my brag file", supplies material in any form, or asks to ingest brag entries.
- [Archive a superseded source](wiki/workflows/archive-source.md) — *how-to.* Move a retired `markdown/` document into `raw/archive/` with a summary page. **Load when** a document stops being outward-facing.
- [Sensitivity tiers](wiki/workflows/sensitivity-tiers.md) — *reference.* T0 public / T1 private repo / T2 never committed; promotion is a rewrite. **Load when** deciding whether something may be written down, or before promoting brag content.

## Career synthesis

- [Accomplishments by domain](wiki/concepts/accomplishments-by-domain.md) — *reference.* Headline accomplishments per domain with citations; the landing page for ingested brag entries and the pool the resume draws from. **Load when** drafting resume text or ingesting a brag entry.
- [Skills matrix](wiki/concepts/skills-matrix.md) — *reference.* Skill × years baseline (~2020) plus deltas evidenced since. **Load when** checking keyword coverage or re-aging skills.
- [Technical themes](wiki/concepts/technical-themes.md) — *explanation.* Capabilities that recur across decades. **Load when** writing summary-level prose.
- [Oleg Zhylin](wiki/entities/oleg-zhylin.md) — *reference.* Profile, what he is looking for, working identity, background. **Load when** the question is about the person rather than a project.
- [Organizations](wiki/entities/organizations.md) — *reference.* Best Buy Health/GreatCall, Minitab, Salford Systems, IIT, education institutions. **Load when** the question is scoped to an employer or period.

## Source summaries (one per document)

- [Achievements resume — PRIMARY](wiki/sources/resume-achievements.md) — structure map with line numbers, unique claims, known defects. **Load when** planning an edit pass.
- [Long-form resume (archived)](wiki/sources/resume-full.md) — harvest map of ~20 project sections not yet synthesized. **Load when** you need depth on any pre-2018 project.
- [Resume overview (archived)](wiki/sources/resume-overview.md) — nothing left to harvest. Load only for provenance.
- [Skills and responsibilities (archived)](wiki/sources/skills-and-responsibilities.md) — table carried to the skills matrix; GreatCall responsibilities. Load for provenance.
- [Professional references](wiki/sources/professional-references.md) — who is listed, relationship, period; no contact details. **Load when** references come up.
- [Minitab 2018 correspondence](wiki/sources/minitab-2018-correspondence.md) — classification of personal/legal material; not evidence. Load only to understand why it is not cited.
- [Brag ledger](wiki/sources/brag-ledger.md) — ingest and promotion state of every `raw/brag/` entry. **Load when** ingesting or promoting.

## Raw

- `raw/brag/` — brag drop zone ([README](raw/brag/README.md)).
- `raw/archive/` — archived documents: `Oleg.Zhylin.resume.md`, `Oleg.Zhylin.resume.overview.md`, `Oleg.Zhylin.skills_and_responsibilities.md`.
- [LLM-wiki pattern](raw/llm-wiki.md) — the abstract idea document.

## Maintenance

- [Schema and workflows](AGENTS.md). The operations log is not committed; see AGENTS.md § *Operations log*.