# Source Map

> **Doc type:** reference
>
> One row per source document: what it is, its sensitivity tier, its current disposition, and the wiki page that summarizes it. Read this before citing anything. Tier definitions: [workflows/sensitivity-tiers.md](workflows/sensitivity-tiers.md). Archiving procedure: [workflows/archive-source.md](workflows/archive-source.md).

## Live documents (build inputs in `markdown/`)

| Source | Tier | Status | Summary page | Use it for |
|---|---|---|---|---|
| [`Oleg.Zhylin.resume.achievements.md`](../../markdown/Oleg.Zhylin.resume.achievements.md) | T0 public | **PRIMARY** — live, mirrored to LinkedIn | [sources/resume-achievements.md](sources/resume-achievements.md) | The canonical statement of the career; the only document edited by the [update workflow](resume/update-workflow.md). |
| [`Oleg.Zhylin.professional.references.md`](../../markdown/Oleg.Zhylin.professional.references.md) | T1 private (third-party PII) | live hand-out | [sources/professional-references.md](sources/professional-references.md) | Who can vouch, relationship, period. Never copy contact details into the wiki. |

## Archived resume variants (`llm-wiki/raw/archive/`, immutable)

| Source | Tier | Status | Summary page | Use it for |
|---|---|---|---|---|
| [`Oleg.Zhylin.resume.md`](../raw/archive/Oleg.Zhylin.resume.md) | T1 private | archived 2026-09-06 | [sources/resume-full.md](sources/resume-full.md) | Deepest project detail 1996–2018; harvest map with ~20 open rows. |
| [`Oleg.Zhylin.resume.overview.md`](../raw/archive/Oleg.Zhylin.resume.overview.md) | T1 private | archived 2026-09-06 | [sources/resume-overview.md](sources/resume-overview.md) | Nothing left to harvest; ancestor of the primary. |
| [`Oleg.Zhylin.skills_and_responsibilities.md`](../raw/archive/Oleg.Zhylin.skills_and_responsibilities.md) | T1 private | archived 2026-09-06 | [sources/skills-and-responsibilities.md](sources/skills-and-responsibilities.md) | Skills-years baseline (carried to [skills matrix](concepts/skills-matrix.md)); GreatCall responsibilities. |

## Archived tooling (`llm-wiki/raw/archive/tools/`, immutable)

Code that was written, works, and has no caller. Archived rather than deleted so the effort and the findings survive; kept out of the live tool directories because unused code sitting next to used code reads as a claim that it is used.

| Source | Tier | Status | Summary page | Use it for |
|---|---|---|---|---|
| [`tools/linkedin-secrets.sh`](../raw/archive/tools/linkedin-secrets.sh) | T1 private | archived 2026-09-10, never wired up | [sources/archived-linkedin-secrets-tool.md](sources/archived-linkedin-secrets-tool.md) | `secret-tool` keyring storage and an AES-256 backup bundle, for a LinkedIn announce post that was never built. Read the summary page before writing **any** credential handling here: two silent `secret-tool` traps, a backup classification, and why secrets never go in argv. |

## Brag entries (`llm-wiki/raw/brag/`)

| Source | Tier | Status | Ledger | Use it for |
|---|---|---|---|---|
| `raw/brag/YYYY-MM-DD-<slug>.md` (none yet) | T1 private or T0-eligible per tag | rolling | [sources/brag-ledger.md](sources/brag-ledger.md) | Fresh accomplishments awaiting synthesis into [accomplishments by domain](concepts/accomplishments-by-domain.md). |

## Historical material (`archive/`)

| Source | Tier | Status | Summary page | Use it for |
|---|---|---|---|---|
| [`archive/minitab/severance_2018/`](../../archive/minitab/severance_2018/) | T1 private — personal/legal, restricted | committed; removal recommended | [sources/minitab-2018-correspondence.md](sources/minitab-2018-correspondence.md) | Nothing. Exists so it is not mistaken for evidence. |

## Pattern reference (`llm-wiki/raw/`)

| Source | Tier | Status | Use it for |
|---|---|---|---|
| [`raw/llm-wiki.md`](../raw/llm-wiki.md) | public idea document | reference | The abstract LLM-wiki pattern this directory instantiates. Repo-specific rules override it (notably: no committed operations log). |

## Not under version control

Large or employer-internal material lives in the maintainer's session-wiki scratch area (`__untracked_stuff/<scope>/session-wiki/raw/`) and is never referenced from here by path. See [`../AGENTS.md`](../AGENTS.md) § *Large and sensitive files*.
