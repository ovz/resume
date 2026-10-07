# Source Map

> **Doc type:** reference
>
> One row per source document: what it is, its sensitivity tier, its current disposition, and the wiki page that summarizes it. Read this before citing anything. Tier definitions: [workflows/sensitivity-tiers.md](workflows/sensitivity-tiers.md). Archiving procedure: [workflows/archive-source.md](workflows/archive-source.md).

## Live documents (build inputs in `markdown/`)

| Source | Tier | Status | Summary page | Use it for |
|---|---|---|---|---|
| [`Oleg.Zhylin.resume.achievements.md`](../../markdown/Oleg.Zhylin.resume.achievements.md) | T0 public | **PRIMARY** — live, mirrored to LinkedIn | [sources/resume-achievements.md](sources/resume-achievements.md) | The canonical statement of the career; edited by the [update workflow](resume/update-workflow.md). |
| [`Oleg.Zhylin.resume.compact.md`](../../markdown/Oleg.Zhylin.resume.compact.md) | T0 public | live variant for page-limited submissions, not mirrored to LinkedIn | [sources/resume-compact.md](sources/resume-compact.md) | The primary under a 7-page budget, for any submission that caps the length. Shares *My Story* and the common plugs with the primary; says nothing the primary does not. |
| [`Oleg.Zhylin.resume.embedded.md`](../../markdown/Oleg.Zhylin.resume.embedded.md) | T0 public | live tailored variant — not mirrored to LinkedIn | [resume/variants.md](resume/variants.md) (no per-source page yet) | Principal Engineer, C++/Rust, embedded audience. Derived from the primary; shares `_parts/` fragments. |
| [`Oleg.Zhylin.resume.networking.md`](../../markdown/Oleg.Zhylin.resume.networking.md) | T0 public | live tailored variant — not mirrored to LinkedIn | [resume/variants.md](resume/variants.md) (no per-source page yet) | Network software engineer audience: device-side transport, cellular, fleet telemetry. Derived from the primary; shares `_parts/` fragments. Names its own gap — no routing or switch-configuration practice. |
| [`Oleg.Zhylin.resume.engineering-manager.md`](../../markdown/Oleg.Zhylin.resume.engineering-manager.md) | T0 public | live tailored variant, not mirrored to LinkedIn | [sources/resume-engineering-manager.md](sources/resume-engineering-manager.md) | Distributed-team delivery, coaching, technical depth and risk-informed engineering management. |
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
| `raw/brag/YYYY-MM-DD-<slug>.md` | T1 private or T0-eligible per tag | rolling | [sources/brag-ledger.md](sources/brag-ledger.md) | Accomplishments captured as they happen, synthesized into [accomplishments by domain](concepts/accomplishments-by-domain.md); ingest and promotion state per entry is in the ledger. |

## Historical material (`archive/`)

| Source | Tier | Status | Summary page | Use it for |
|---|---|---|---|---|
| [`archive/minitab/severance_2018/`](../../archive/minitab/severance_2018/) | T1 private — personal/legal, restricted | committed; removal recommended | [sources/minitab-2018-correspondence.md](sources/minitab-2018-correspondence.md) | Nothing. Exists so it is not mistaken for evidence. |

## Pattern reference (`llm-wiki/raw/`)

| Source | Tier | Status | Use it for |
|---|---|---|---|
| [`raw/llm-wiki.md`](../raw/llm-wiki.md) | public idea document | reference | The abstract LLM-wiki pattern this directory instantiates. Repo-specific rules override it (notably: no committed operations log). |

## Personal reading, annotated (the book itself is not committed)

| Source | Tier | Status | Summary page | Use it for |
|---|---|---|---|---|
| *Release It!* 2nd ed. (Nygard) — the owner's annotated copy | T1 for **the annotations only**; the book is a copyrighted commercial work and stays out of version control | harvested 2026-09-20, one pass, complete | [sources/release-it-annotations.md](sources/release-it-annotations.md) | Production-readiness vocabulary; the operators-as-customers framing; the owner's own arguments about failure-mode testing, availability zones and toil. **Never quote the book from the harvest — only the owner's notes.** |

## Not under version control

Large or employer-internal material lives in the maintainer's session-wiki scratch area (`__untracked_stuff/<scope>/session-wiki/raw/`) and is never referenced from here by path. See [`../AGENTS.md`](../AGENTS.md) § *Large and sensitive files*.
