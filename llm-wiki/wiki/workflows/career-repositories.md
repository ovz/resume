# Career repositories — the past, the search, the practice

> **Doc type:** reference
>
> How the owner's career work is split across repositories, what each one owns, how agents move knowledge between them, and where Claude Cowork fits. Audience: the owner, and any agent in one repository that needs something from another.

## The division

| Where | Owns | Orientation | Remote |
|---|---|---|---|
| **resume** (this repository) | The record: brag entries, synthesis, stories, the resume and its LinkedIn rendering, and the [dream-job hub](../dream-jobs/dream-job-hub.md), which grades futures against that record | The past, and how it is told | `bitbucket.org/ovz/resume` |
| **job-search-infra** | The search: the application pipeline and recruiting contacts (a live tracker page with its own data store, plus its source and snapshots), per-application reading lists and tailoring | The present and the next move | `bitbucket.org/ovz/job-search-infra` |
| **cpp_edu** | The practice: C++ training — standards essays for embedded work, guides, problem sets — tailored to specific employers under `jobs/<employer>/` | The skills the next stage needs | `bitbucket.org/ovz/cpp_edu` |
| **Claude Cowork** | The glue: conversations and tasks that keep going with every laptop off, through connectors and published pages | Continuous | — no repository of its own; what it produces lands in one of the three |

**Rule of thumb: the past here, the search and the future in the siblings.** The dream-job hub stays here because its grades are only as good as the record beside it; acting on it — applications, outreach, preparation — happens in the siblings.

**One boundary is still the owner's to draw:** employer research. It lives today in this repository under `wiki/analysis/employers/`, for past and prospective employers alike. Prospective employers may belong in job-search-infra instead; until that is decided, keep adding it here.

## Why this exists: a ten-year stage

The owner's career has moved in stages of roughly a decade — cybersecurity as an undergraduate, the Salford Systems years from Ukraine, becoming an American principal engineer, then an embedded principal engineer — and another stage is due ([Oleg Zhylin](../entities/oleg-zhylin.md) § *Ten-year stages*). The repositories are split so that each can move at its own cadence without the others' history getting in the way, and the whole system is judged by one question: **does it help set up the next ten years?**

## How the repositories talk

1. **Each repository keeps its own gitignored scratch area**, `__untracked_stuff/<scope>/`, holding a session-wiki: raw capture, findings, commit proposals, a log, and an assignment tracker that is the resume token. The pattern's one copy is this repository's `session-wiki-pattern` skill; sibling repositories refer to it rather than copying it.
2. **Cross-repository work opens a scope in every repository it touches**, with the same scope name. A scratch file may cite another repository's committed files by path; a committed file never cites scratch.
3. **Every open tracker is traced in its repository's root `TODO.md`** — one line per tracker with action items, added when it opens them, removed when it closes. A tracker in one repository may also be traced from another's `TODO.md` when the owner should see it there. This is the single, deliberate exception to "no committed file references scratch" (root [`AGENTS.md`](../../../AGENTS.md)).
4. **Hand-offs go in the tracker, never only in a chat reply** — for Claude and for the owner alike.
5. **Knowledge is promoted into the repository that owns it**: a story graduates here; an application's reading list stays in job-search-infra's scratch; a study plan for an employer lands in cpp_edu's `jobs/<employer>/`.
6. **Agents do not commit** in any of them. Each scope writes its proposed commit messages under its own `session-wiki/commits/`.

## What flows where

| From | To | What |
|---|---|---|
| resume | job-search-infra | Stories and reading-list material, tailored resume variants, dream-job grades |
| job-search-infra | resume | New evidence — an interview that probed a claim, feedback on a telling — as a brag inbox note; employer research worth keeping |
| job-search-infra | cpp_edu | Which employers need which C++ preparation, and when |
| resume | cpp_edu | Domain depth to study against — Boost MSM for state-machine design, embedded C++ standards behind the 2022 guidelines |
| cpp_edu | resume | Demonstrated skill, as a brag entry when a series or a solution set is finished |

## Claude Cowork

Cowork is where the owner can talk to the system with every laptop powered off. It can read connected mail and documents, update a published tracker page's data, and draft notes. It cannot commit, and nothing it produces is durable until a session carries it into the repository that owns it — as a brag inbox note here, a raw capture in the right scope, or a data snapshot in job-search-infra. Setting up the project and its connectors is the owner's step, and is tracked in the job-search-infra scope.

## Related

- [Dream-job hub](../dream-jobs/dream-job-hub.md) — the future, graded against the record.
- [Brag stories](brag-stories.md) — how stories and reading lists are built before they travel.
- [Professional contacts](../entities/professional-contacts.md) — the mentor and colleagues the career questions involve.
- [LinkedIn profile visibility](../analysis/2026-09-14-linkedin-profile-visibility.md) — the one outward channel the search depends on.
