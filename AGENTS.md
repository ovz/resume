# Resume repository — agent instructions

Personal resume repository for Oleg Zhylin. Markdown sources in `markdown/` are rendered by Pandoc into HTML, PDF, DOCX and RTF. `llm-wiki/` is the maintained knowledge layer behind the resume. This file is the router: hard rules in one line each, everything else in a shard that is read only when the task needs it.

**Cloud direction: round trip** — no claude.ai project of its own; the job-search project is the cloud side, and nothing is durable until committed here. Detail: [`career-repositories.md`](llm-wiki/wiki/workflows/career-repositories.md#cloud-direction).

## Hard rules

- **Agents do not commit.** Never run `git commit`, `git push`, `git tag` or any other history-writing command, however sure the change or however it seemed pre-approved. Leave work in the tree and write a proposed commit message under the session-wiki's `commits/`. → [`commits-and-uncommitted-work.md`](.github/rules/commits-and-uncommitted-work.md)
- **Uncommitted work is the one thing git cannot give back.** Secure a copy before overwriting a region with uncommitted changes; when a request could mean two things and one reading destroys work, ask. → same shard
- **Hand-offs go in the assignment tracker, never in the chat response.** Anything the owner must do, decide, verify or answer goes under `## Open for the owner` in the session-wiki's `tasks/assignment_tracker.md` when discovered; the chat says only that items exist and where. → [`handoffs-and-tracker.md`](.github/rules/handoffs-and-tracker.md)
- **No committed file references a path under `__untracked_stuff/`** (the root `TODO.md` alone may), third-party contact details never leave the references document, and names are recorded in full at T1 but come out at T0. Tiers: **T0 public** (primary resume only), **T1 private repo**, **T2 never committed**. → [`sensitivity-hard-rules.md`](.github/rules/sensitivity-hard-rules.md)
- **Do not edit `pandoc_resume/`.** It is a git submodule tracking a fork of `mszep/pandoc_resume`; it supplies ConTeXt and CSS style assets only. Changes belong upstream in the fork, and local edits break the build's re-merge story.

## Where the rules live

Per-directory `AGENTS.md` files are the primary, load-bearing instructions. Read the one covering the directory you are about to touch; do not rely on this router alone.

| Directory | File | Covers |
|---|---|---|
| `markdown/` | [`markdown/AGENTS.md`](markdown/AGENTS.md) | Editing the outward-facing resume and references documents |
| `llm-wiki/` | [`llm-wiki/AGENTS.md`](llm-wiki/AGENTS.md) | The knowledge layer: schema, sensitivity tiers, ingest and synthesis workflows |
| `.github/` | [`.github/AGENTS.md`](.github/AGENTS.md) | How this repo's agent customizations are laid out and kept discoverable |

## Shards — read the one the task matches

Each is a file in [`.github/rules/`](.github/rules/).

| Task | Shard |
|---|---|
| Recording an accomplishment, stories, coverage, resume edits, dream jobs, LinkedIn, archiving, large imports; a pipeline of **rewrites, never copies**: `raw/brag/` → `accomplishments-by-domain.md` → `markdown/` | [`professional-history.md`](.github/rules/professional-history.md) |
| Writing anything to be read or said outward — **read [`voice-and-prominence.md`](llm-wiki/wiki/workflows/voice-and-prominence.md) before drafting** | [`voice-pillar.md`](.github/rules/voice-pillar.md) |
| Building (`script/pandoc_resume.sh all`; a `NO IMAGE` line from `verify` is a build failure), LinkedIn budgets and paste workflow; artifacts are gitignored except `linkedin/`, which is generated and never hand-edited | [`building.md`](.github/rules/building.md) |
| Loading a skill (brag-capture, resume-editing, linkedin-publish, resume-tooling, pdf-extraction, large-import; each has a `.claude/skills/` symlink) or planning a long assignment (`session-wiki-pattern`, shared from the agentic_linux repo) | [`skills-list.md`](.github/rules/skills-list.md) |
| Sending material to the about-me repository or Claude Cowork | [`about-me-and-cowork.md`](.github/rules/about-me-and-cowork.md) |
| How Claude Code reaches this file (`CLAUDE.md` imports) | [`claude-code-bridge.md`](.github/rules/claude-code-bridge.md) |
