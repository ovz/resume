> Shard of the root [`AGENTS.md`](../../AGENTS.md). Load when the task matches its title.

# Tracking professional history

This repository is a pipeline, not a single document. An accomplishment reaches the resume in three hops, and **each hop is a rewrite, never a copy**:

```
llm-wiki/raw/brag/     →   llm-wiki/wiki/concepts/        →   markdown/
one dated file per         accomplishments-by-domain.md       the public resume
accomplishment,            plus the ledger, entities          and any tailored
captured when it happens   and themes                         variant
```

| Need | Start here |
|---|---|
| Record something that just happened, in any format | `brag-capture` skill → [`llm-wiki/wiki/workflows/brag-file.md`](../../llm-wiki/wiki/workflows/brag-file.md) §§ *Part 0*–*Part 1* |
| Fold captured entries into the knowledge layer | `brag-capture` skill → same page, § *Part 2* |
| The owner's memory and the mailbox disagree about an episode | [`llm-wiki/wiki/workflows/brag-file.md`](../../llm-wiki/wiki/workflows/brag-file.md) § *Part 1c* — the email record wins; his account stays verbatim beside it |
| Turn entries into told-able stories, or get a reading list for an interview, event or employer | `brag-capture` skill → [`llm-wiki/wiki/workflows/brag-stories.md`](../../llm-wiki/wiki/workflows/brag-stories.md) |
| See what the resume is missing, and how much is covered | [`llm-wiki/wiki/resume/coverage.md`](../../llm-wiki/wiki/resume/coverage.md) |
| Put something on the outward-facing resume | `resume-editing` skill → [`llm-wiki/wiki/resume/update-workflow.md`](../../llm-wiki/wiki/resume/update-workflow.md) |
| Decide where this career should point next, or judge a role against the record | [`llm-wiki/wiki/dream-jobs/dream-job-hub.md`](../../llm-wiki/wiki/dream-jobs/dream-job-hub.md) — candidates graded on evidence, the owner's own ideas marked apart from an agent's |
| Work across the career repositories — this one holds the past, the job-search and C++ training repositories hold the search and the future | [`llm-wiki/wiki/workflows/career-repositories.md`](../../llm-wiki/wiki/workflows/career-repositories.md) — what each owns, how knowledge moves between them, where Claude Cowork fits |
| Decide how often to touch the LinkedIn profile, and what actually gets it found | [`llm-wiki/wiki/analysis/2026-09-14-linkedin-profile-visibility.md`](../../llm-wiki/wiki/analysis/2026-09-14-linkedin-profile-visibility.md) |
| Refresh the LinkedIn profile from the resume | `linkedin-publish` skill → [`llm-wiki/wiki/workflows/linkedin-publish.md`](../../llm-wiki/wiki/workflows/linkedin-publish.md) |
| Find out whether the LinkedIn update can be automated | Same page, § *The answer, first* — it cannot, and the research is recorded so it is not repeated |
| Decide whether a fact may be written down at all | [`llm-wiki/wiki/workflows/sensitivity-tiers.md`](../../llm-wiki/wiki/workflows/sensitivity-tiers.md) |
| Retire a document that has stopped being outward-facing | [`llm-wiki/wiki/workflows/archive-source.md`](../../llm-wiki/wiki/workflows/archive-source.md) |
| Preserve a source too large to commit as-is | `large-import` skill → [`llm-wiki/wiki/workflows/large-imports.md`](../../llm-wiki/wiki/workflows/large-imports.md) |
| Ingest any other source, answer a question from the wiki, or lint it | [`llm-wiki/AGENTS.md`](../../llm-wiki/AGENTS.md) § *Workflows* |

Skipping a hop is the failure this layout exists to prevent: text copied straight from a brag entry into the resume has passed neither the sensitivity check nor the depth check, and both are easy to lose silently.
