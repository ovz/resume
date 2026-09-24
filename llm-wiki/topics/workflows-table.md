> Shard of [`../AGENTS.md`](../AGENTS.md). The task-to-page routing table.

# Workflows

| Need | Page |
|---|---|
| **Write anything outward — a story, a resume line, a LinkedIn block, a reading list** | `../wiki/workflows/voice-and-prominence.md` **first**: one voice across era registers, prominence that follows evidence, and honest handling of blocked or unshipped work |
| Decide where the career should point next, or judge a role against the record | `../wiki/dream-jobs/dream-job-hub.md`; market evidence in `../wiki/analysis/2026-09-13-specializations-landscape.md` |
| Refine, improve, or update the primary resume | `../wiki/resume/update-workflow.md` (load `../wiki/resume/primary-resume.md`, `link-conventions.md` and `coverage.md` first) |
| See what the resume is missing, or how much is covered | `../wiki/resume/coverage.md` |
| Capture an accomplishment right now, in any format | `../wiki/workflows/brag-file.md` §§ *Part 0*–*Part 1* |
| Fold captured accomplishments into the wiki | `../wiki/workflows/brag-file.md` § *Part 2* |
| Graduate entries into stories, or build a reading list for an interview, event or employer | `../wiki/workflows/brag-stories.md` |
| Work that spans the resume, job-search and C++ training repositories, or Claude Cowork | `../wiki/workflows/career-repositories.md` |
| Get the generated blocks onto the LinkedIn profile, or answer whether that can be automated | `../wiki/workflows/linkedin-publish.md` |
| Retire a superseded `../markdown/` document | `../wiki/workflows/archive-source.md` |
| Decide whether something may be written down here | `../wiki/workflows/sensitivity-tiers.md` |
| Change the Obsidian vault, the graph, or the brag entry schema | `../wiki/workflows/obsidian-vault.md` |
| Preserve a source too large to commit as-is | `../wiki/workflows/large-imports.md` (the owner decides the tier first; an agent never grants the exception) |
| Ingest any other new source | Read it fully; write or update its `../wiki/sources/` page; update `../wiki/sources.md`, the affected synthesis pages, and `index.md`; log the ingest (below). |
| Answer a question | `index.md` → smallest set of pages → answer with source links and stated uncertainty. File durable answers under `../wiki/analysis/` (create on first use) and index them. |
| Lint | Broken relative links; pages over 500 lines (sharding review) or 1,024 lines (failure); claims without sources; `__untracked_stuff` references; orphan pages; `raw/brag/` entries missing from the ledger; entries missing from the subject shards routed by `../wiki/resume/coverage.md`, or coverage totals that fail `python3 script/check-coverage.py`; `../wiki/sources/` pages whose harvest map is stale; dream-job candidates whose `origin` was changed to `owner` without the owner saying so, or whose evidence grade no longer matches the entries they cite; Obsidian colour groups that disagree with the legend in `../wiki/workflows/obsidian-vault.md`. Record findings in the operations log. |
