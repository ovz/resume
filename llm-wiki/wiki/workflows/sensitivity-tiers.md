# Sensitivity Tiers

> **Doc type:** reference
>
> Where each kind of information may live in this repository, and what must happen before it moves up a tier. Audience: the owner and every agent writing into `llm-wiki/`, `markdown/`, or `__untracked_stuff/`.

## Why tiers

The owner is a principal-level engineer; a great deal of what makes the career story true is knowledge an employer would consider internal. That knowledge legitimately lives in the owner's head and may be *used* to write accurate, outcome-level claims — but the artifacts, names, numbers, and internals themselves must not be published, and much of it should not even be committed. The repository is private; only the primary resume is public. Three tiers make the line explicit.

## The tiers

| Tier | Name | Where it lives | Who can see it | Examples |
|---|---|---|---|---|
| **T0** | **Public** | `markdown/Oleg.Zhylin.resume.achievements.md` and any future tailored variant in `markdown/` | Anyone (LinkedIn mirror, sent to recruiters) | Employers, product names already public, released products, publicly documented technologies, outcome-level claims ("drastically reduced cost of operation"), the owner's own contact details (owner's choice). |
| **T1** | **Private repo** | Everything else under version control: `llm-wiki/**` (including `raw/brag/`), `markdown/Oleg.Zhylin.professional.references.md`, `archive/**` | The owner and collaborators with repo access | Brag entries written at outcome level; wiki synthesis; reference contacts (third-party PII — handled below); personal correspondence already committed (see `sources/minitab-2018-correspondence.md`). |
| **T2** | **Never committed** | `__untracked_stuff/<scope>/session-wiki/raw/` (gitignored) or outside the repo entirely | The owner's workstation only | Employer-internal documents, OneNote/Confluence exports, PDFs, screenshots, meeting notes, internal metrics, customer names, code names, unreleased plans, incident details, anything "illegal, unprofessional, or unfair to reveal about a current or former employer". Also any file large enough to bloat the repo, regardless of content. |

## Rules

1. **Promotion is a rewrite, not a copy.** T2 → T1 means rewriting the fact at the level of *what the owner did, what skill it demonstrates, and what outcome it had*, with no internal artifact names, figures the employer has not published, or customer identities. Colleague and collaborator names are fine at T1 — they are part of the owner's own professional record — unless a grounded reason says otherwise (an NDA-covered partner, an unannounced partnership, a person who asked not to be named). T1 → T0 means an additional pass through [primary-resume.md](../resume/primary-resume.md) § *Style conventions*, a check that every named product or technology is already public, and dropping colleague names.
2. **Committed files never reference T2 paths** (`__untracked_stuff/...`). A committed page may say "evidence retained offline"; it may not say where. This is the one-way reference rule from the `session-wiki-pattern` skill.
3. **Third-party PII stays in its source.** The references document holds phone numbers and emails of former colleagues. Wiki pages cite the document and may list name, relationship, and period; they never copy contact details. Consent to be a reference is not consent to be indexed.
4. **Brag entries carry a tier tag** (`sensitivity: public-friendly` or `sensitivity: private-repo`). An entry that cannot honestly be tagged either way is T2 material and belongs in the maintainer scope's `raw/`, not in `llm-wiki/raw/brag/`.
5. **Large files are T2 by size alone.** PDFs, images beyond the single avatar, exports. `.gitignore` already excludes `*.pdf`, `*.htm*`, and `__untracked_stuff`. Do not add exceptions.
6. **The owner may downgrade a tier, never an agent.** If an agent believes something committed should not be, it flags it in the maintainer tracker and leaves the file in place.
7. **A case that resists the policy is a defect in the policy.** Most brag input is written with the professional record in mind and classifies without effort. When something genuinely does not — an artifact type these rules do not cover, an ambiguous partner or customer reference — do not settle it with a silent one-off judgement. Apply the most conservative reading, record the case, and propose a refinement here. Repeated judgement calls in the same spot mean this page needs rewriting, not that the reader needs to be more careful.

## Where the line usually falls (heuristics)

- A technology, vendor, or partner the employer has publicly acknowledged (e.g. a vendor named in a press release or product page) → T0-eligible.
- The *fact* that an OKR was met, an operational metric improved, a launch shipped → T0-eligible at outcome level; the metric's value and the internal dashboard → T2.
- An internal system's name → T2; its *function* ("a telemetry pipeline", "device-side test harness") → T0-eligible.
- A colleague's contribution → name the person and describe the collaboration; T1 only (names come out at T0). Contact details stay in the references document. Exception: partners or individuals covered by an NDA, an unannounced partnership, or an explicit request not to be named → role only.
- Anything about a current employer's roadmap → T2 until it ships publicly.

## Related

- [Brag file workflow](brag-file.md) — where the tier tag is applied.
- [Archive a source](archive-source.md) — archived documents keep the tier they had.
- [Primary resume](../resume/primary-resume.md) — the T0 document.
