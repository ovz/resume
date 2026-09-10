# Update the Outward-Facing Resume

> **Doc type:** how-to
>
> The deliberate, owner-triggered pass that changes [`markdown/Oleg.Zhylin.resume.achievements.md`](../../../markdown/Oleg.Zhylin.resume.achievements.md). This is **not** the brag-file ingest — brag entries are captured and synthesized by [workflows/brag-file.md](../workflows/brag-file.md) without touching the resume. Audience: the owner and any agent asked to "update / refine / improve the resume".

## Before you start

1. Load [primary-resume.md](primary-resume.md) and [link-conventions.md](link-conventions.md). They are the rules; this page is the sequence.
2. Load [accomplishments by domain](../concepts/accomplishments-by-domain.md) — the pool of candidate material — and [coverage.md](coverage.md), which says which of that pool has *not* reached the resume and is therefore where the pass has the most to gain. If the request names an employer, load the relevant part of [organizations](../entities/organizations.md).
3. Read [`sources/resume-achievements.md`](../sources/resume-achievements.md) § *Known defects* so the pass can clear them.
4. Confirm the **target**: which cut level (C0/C1/C2/beyond) the change affects, and whether the goal is a general refresh or a role-specific tailoring. Role-specific variants are separate files (not created yet); do not tailor the primary in place.

## Steps

1. **Draft in the Markdown source only.** Never edit rendered outputs or LinkedIn first.
2. **Place new material at the right depth.** A new accomplishment enters *Projects Overview* or the employer's *Employment History* paragraph first. Promote a sentence to *Most prominent achievements* (C2) only if it changes what a reader should know at two pages; promote to the summary or *My Story* (C0/C1) only if it changes the frame.
3. **Keep every C2 bullet traceable** to a section below it. If you add a bullet, add or extend the section it points to.
4. **Apply the link conventions** to every new or touched hyperlink: pinned Wayback snapshot, reference-style definition with a proper title, shared key names.
5. **Run the sensitivity check** in [sensitivity-tiers.md](../workflows/sensitivity-tiers.md) § *Public tier*: no employer-internal names, numbers, customers, code names, or unreleased plans. Outcome and skill, not internal artifact.
6. **Render and check page fit.** `script/pandoc_resume.sh pdf` (or `html`) from the repo root; open the PDF and note where the half-page, one-page, and two-page boundaries fall relative to the intended cut map. Adjust wording length before adjusting structure.
7. **Lint the file:** every `[key]` used is defined once; no dangling emphasis markers; headings follow the section conventions; the *Side Note* still precedes the link-dense sections.
8. **Update the wiki, not just the resume.** Refresh [`sources/resume-achievements.md`](../sources/resume-achievements.md) (structure map, defects list). If the change came from brag material, flip the affected claims in [coverage.md](coverage.md) to `in` or `partial` **in the same edit** — a promotion recorded nowhere is a promotion the next pass will make again — and mark the promotion in [brag-ledger.md](../sources/brag-ledger.md). Record the pass in the maintainer's operations log (outside version control; see [`../../AGENTS.md`](../../AGENTS.md) § *Operations log*).
9. **Hand off for review.** Present the diff and the render observations. The owner commits, then mirrors the text to LinkedIn. Agents do not commit.

## Tailored variants (when asked)

A role-specific resume is a **new file** in `markdown/` named `Oleg.Zhylin.resume.<audience>.md`, derived from the primary by re-ordering C2 bullets and pruning beyond-C2 sections. It inherits every convention here. When the variant is retired, archive it via [workflows/archive-source.md](../workflows/archive-source.md) with its own summary page.

## Related

- [Brag file workflow](../workflows/brag-file.md) — capture and synthesis that feeds this pass.
- [Archive a source](../workflows/archive-source.md) — what happens to superseded documents.
