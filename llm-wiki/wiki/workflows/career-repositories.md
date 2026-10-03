# Career repositories — the past, the search, the practice

> **Doc type:** reference
>
> How the owner's career work is split across repositories, what each one owns, how agents move knowledge between them, and where Claude Cowork fits. Audience: the owner, and any agent in one repository that needs something from another.

## The division

| Where | Owns | Orientation | Remote |
|---|---|---|---|
| **resume** (this repository) | The record: brag entries, synthesis, stories, the resume and its LinkedIn rendering, and the [dream-job hub](../dream-jobs/dream-job-hub.md), which grades futures against that record | The past, and how it is told | `bitbucket.org/ovz/resume` |
| **job-search-infra** | The search, meaning how the owner looks for jobs: the application pipeline and recruiting contacts (a live tracker page with its own data store, plus its source and snapshots), per-application reading lists and tailoring | The present and the next move | `bitbucket.org/ovz/job-search-infra` |
| **cpp_edu** | The practice, meaning how the owner prepares for jobs: C++ training (standards essays for embedded work, guides, problem sets) and the prospective employers themselves, one folder each under `jobs/<employer>/` | The skills the next stage needs | `bitbucket.org/ovz/cpp_edu` |
| **about-me** | Who the owner is, for any assistant: a curated profile, preferences, trends register, and dated voice reports on how he writes and speaks across email, notes and AI-assistant history. It is kept in sync with a Claude project, and it is the one aggregator: it ingests Cowork's weekly zips and, on request, scans the other repositories' committed history | Identity and voice, not career record | `bitbucket.org/ovz/about-me` |
| **Claude Cowork** | The glue: conversations and tasks that keep going with every laptop off, through connectors and published pages | Continuous | — no repository of its own; what it produces lands in one of the three |

**about-me is read, not written, from here, and it pulls rather than being sent to.** Nothing here writes digests for it ([`about-me-and-cowork.md`](../../../.github/rules/about-me-and-cowork.md)). Its voice reports help a spoken draft rehearse better; this repository's own [voice and prominence](voice-and-prominence.md) rules win wherever the two differ ([spoken drafts](spoken-drafts.md)). A fact about the career belongs here even when about-me mentions it too.

**Rule of thumb: the past here, the search and the future in the siblings.** The dream-job hub stays here because its grades are only as good as the record beside it; acting on it — applications, outreach, preparation — happens in the siblings.

**Employer research follows the same line, and the owner has drawn it (2026-09-25): this repository is about actual employers — the ones the owner has worked for.** Research on a past employer that explains the record (for example the Best Buy Health public-record page) lives here under `wiki/analysis/employers/`. Research on a prospective employer belongs in cpp_edu, under `jobs/<employer>/`, beside the preparation for that employer (owner, 2026-10-02). The owner will work in this repository while talking to employers, but it must not grow as interviews accumulate: it is about what the owner has accomplished, and resume work here focuses on that.

## Why this exists: a ten-year stage

The owner's career has moved in stages of roughly a decade — cybersecurity as an undergraduate, the Salford Systems years from Ukraine, becoming an American principal engineer, then an embedded principal engineer — and another stage is due ([Oleg Zhylin](../entities/oleg-zhylin.md) § *Ten-year stages*). The repositories are split so that each can move at its own cadence without the others' history getting in the way, and the whole system is judged by one question: **does it help set up the next ten years?**

The program-level tracker for the whole system is the tracker of the `career-system-plan` scope in this repository, reached through the root `TODO.md`. The three repositories are sibling checkouts under one directory on the owner's workstation.

## How the repositories talk

1. **Each repository keeps its own gitignored scratch area**, `__untracked_stuff/<scope>/`, holding a session-wiki: raw capture, findings, commit proposals, a log, and an assignment tracker that is the resume token. The pattern's one copy is the `session-wiki-pattern` skill in the agentic_linux repo, reached from every repository through the user's own skill directories; no repository copies it.
2. **Cross-repository work opens a scope in every repository it touches**, with the same scope name. A scratch file may cite another repository's committed files by path; a committed file never cites scratch.
3. **Every open tracker is traced in its repository's root `TODO.md`** — one line per tracker with action items, added when it opens them, removed when it closes. A tracker in one repository may also be traced from another's `TODO.md` when the owner should see it there. This is the single, deliberate exception to "no committed file references scratch" (root [`AGENTS.md`](../../../AGENTS.md)).
4. **Hand-offs go in the tracker, never only in a chat reply** — for Claude and for the owner alike.
5. **Knowledge is promoted into the repository that owns it**: a story graduates here; an application's reading list stays in job-search-infra's scratch; a study plan for an employer lands in cpp_edu's `jobs/<employer>/`.
6. **Agents do not commit** in any of them. Each scope writes its proposed commit messages under its own `session-wiki/commits/`.

## What flows where

| From | To | What |
|---|---|---|
| resume | job-search-infra | Stories and reading-list material, tailored resume variants, dream-job grades |
| job-search-infra | resume | New evidence — an interview that probed a claim, feedback on a telling — as a brag inbox note; only new evidence about the record comes here |
| job-search-infra | cpp_edu | Which employers need which C++ preparation, and when |
| resume | cpp_edu | Domain depth to study against — Boost MSM for state-machine design, embedded C++ standards behind the 2022 guidelines |
| cpp_edu | resume | Demonstrated skill, as a brag entry when a series or a solution set is finished |

## Cloud direction

Owner's decision, 2026-09-25: this repository is a **round trip** with the cloud. It has no claude.ai project of its own; the cloud side is the job-search project, tracked from `cpp_edu` and the other career repositories. Inputs arrive from brag notes and varied upstream sources (mailbox messages, Cowork output). What goes back out is material for the job-search project; about-me takes what it needs from this repository's history itself. The repository stays the durable copy in both directions.

## Claude Cowork

Cowork is where the owner can talk to the system with every laptop powered off. It can read connected mail and documents, update a published tracker page's data, and draft notes. It cannot commit, and nothing it produces is durable until a session carries it into the repository that owns it — as a brag inbox note here, a raw capture in the right scope, or a data snapshot in job-search-infra. Setting up the project and its connectors is the owner's step, and is tracked in the job-search-infra scope.

## Related

- [Dream-job hub](../dream-jobs/dream-job-hub.md) — the future, graded against the record.
- [Brag stories](brag-stories.md) — how stories and reading lists are built before they travel.
- [Professional contacts](../entities/professional-contacts.md) — the mentor and colleagues the career questions involve.
- [LinkedIn profile visibility](../analysis/2026-09-14-linkedin-profile-visibility.md) — the one outward channel the search depends on.
