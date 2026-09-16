# Update the Outward-Facing Resume

> **Doc type:** how-to
>
> The deliberate, owner-triggered pass that changes [`markdown/Oleg.Zhylin.resume.achievements.md`](../../../markdown/Oleg.Zhylin.resume.achievements.md). This is **not** the brag-file ingest — brag entries are captured and synthesized by [workflows/brag-file.md](../workflows/brag-file.md) without touching the resume. Audience: the owner and any agent asked to "update / refine / improve the resume".

## Before you start

1. Load [primary-resume.md](primary-resume.md) and [link-conventions.md](link-conventions.md). They are the rules; this page is the sequence.
2. Load [accomplishments by domain](../concepts/accomplishments-by-domain.md) — the pool of candidate material — and [coverage.md](coverage.md), then only its relevant subject shard. The map gives aggregate gaps; the shard owns the claims and evidence caveats. Load [editorial guidance](coverage/editorial.md) when judging promotion trade-offs. If the request names an employer, load the relevant part of [organizations](../entities/organizations.md).
3. Read [`sources/resume-achievements.md`](../sources/resume-achievements.md) § *Known defects* so the pass can clear them.
4. Confirm the **target**: which cut level (C0/C1/C2/beyond) the change affects, and whether the goal is a general refresh or a role-specific tailoring. Role-specific variants are separate files; do not tailor the primary in place.
5. Check the **LinkedIn budgets** before drafting, not after. `script/pandoc_resume.sh linkedin` prints how much headroom each marked section has. *My Story* and every *Employment History* section are capped; if the one you are about to add to has no room, the pass is a trade rather than an addition, and that is worth knowing before writing the sentence. See [primary-resume.md](primary-resume.md) § *The LinkedIn mirror*.

## Steps

1. **Draft in the Markdown source only.** Never edit rendered outputs or LinkedIn first.
2. **Place new material at the right depth.** A new accomplishment enters *Projects Overview* or the employer's *Employment History* paragraph first. Promote a sentence to *Most prominent achievements* (C2) only if it changes what a reader should know at two pages; promote to the summary or *My Story* (C0/C1) only if it changes the frame.
3. **Keep every C2 bullet traceable** to a section below it. If you add a bullet, add or extend the section it points to.
4. **Apply the link conventions** to every new or touched hyperlink: pinned Wayback snapshot, reference-style definition with a proper title, shared key names.
5. **Run the sensitivity check** in [sensitivity-tiers.md](../workflows/sensitivity-tiers.md) § *Public tier*: no employer-internal names, numbers, customers, code names, or unreleased plans. Outcome and skill, not internal artifact.
6. **Render and check page fit.** `script/pandoc_resume.sh all` from the repo root; open the PDF and note where the half-page, one-page, and two-page boundaries fall relative to the intended cut map. Adjust wording length before adjusting structure. The same run regenerates the LinkedIn blocks and **fails the build** if a marked section is over its field limit — shorten the section rather than raising the limit, which is LinkedIn's number and not this repo's.
7. **Lint the file:** every `[key]` used is defined once; no dangling emphasis markers; headings follow the section conventions; the *Side Note* still precedes the link-dense sections.
8. **Update the wiki, not just the resume.** Refresh [`sources/resume-achievements.md`](../sources/resume-achievements.md) (structure map, defects list). If the change came from brag material, flip the affected claims in the owning shard linked from [coverage.md](coverage.md) to `in` or `partial` **in the same edit** — a promotion recorded nowhere is a promotion the next pass will make again — and mark the promotion in [brag-ledger.md](../sources/brag-ledger.md). Recompute thread, shard and headline totals and run `python3 script/check-coverage.py`. Record the pass in the maintainer's operations log (outside version control; see [`../../AGENTS.md`](../../AGENTS.md) § *Operations log*).
9. **Hand off for review.** Present the diff and the render observations, **including which files under `linkedin/` changed** — that set is exactly the list of LinkedIn fields the owner has to re-paste, and it is the reason that directory is tracked. Say it explicitly rather than leaving it to be inferred from the diff. The owner commits resume edits as they go; pasting runs on its own clock. Record **LinkedIn paste due** as a low-priority owner item in the tracker whenever `script/linkedin-sync.py status` exits non-zero, and leave the round to the owner — it regenerates the blocks itself, so nothing is lost by pasting later ([publish to LinkedIn](../workflows/linkedin-publish.md)). Agents do not commit.

## Tailored variants

A role-specific resume is a **new file** in `markdown/` named `Oleg.Zhylin.resume.<audience>.md`, derived from the primary by retargeting the summary, compressing *My Story*, re-ordering and pruning C2 bullets, and cutting beyond-C2 sections that do not serve that audience. It inherits every convention here. When a variant is retired, archive it via [workflows/archive-source.md](../workflows/archive-source.md) with its own summary page.

**Existing variants:**

| File | Audience | Cut relative to the primary |
|---|---|---|
| `Oleg.Zhylin.resume.achievements.md` | General — the primary, mirrored to LinkedIn | — |
| `Oleg.Zhylin.resume.embedded.md` | Principal Engineer, C++/Rust, embedded (hosted or bare metal), owning operational excellence | Summary retargeted to Principal and embedded; *My Story* compressed from six paragraphs to four, with the ML-product era reframed as systems work; C2 reordered with a Quality-Engineering bullet added and the ML-GUI, API-design and Big-Data bullets dropped; *Projects Overview* replaced by a shorter *Selected Projects* keeping the cross-platform, systems and toolchain work |

### Keeping variants from drifting

Content that must be identical across variants lives once, in `markdown/_parts/`, and is pulled in by a line reading exactly:

```
<!-- include: _parts/links.md -->
```

`_parts/` is a subdirectory, so the build never mistakes a fragment for a document. Five fragments exist:

| Fragment | Why it is shared |
|---|---|
| `links.md` | The reference-link block — 75 keys, where a key must mean the same thing in every document ([link conventions](link-conventions.md)) |
| `header.md` | Portrait, name and the contact line. Contact details changing in one variant and not the other is the most embarrassing possible drift |
| `side-note-links.md` | The Wayback explanation. Pure boilerplate that must read identically wherever it appears |
| `education.md` | The two degrees. The primary appends its own earlier-schooling section *after* the include; the variant does not |
| `bullet-operational-excellence.md` | The observability bullet — long, newly written, and therefore the most likely to be refined in one file and forgotten in the other |

One thing is deliberately *not* shared: the `<!-- linkedin: -->` markers. LinkedIn is a single profile, so exactly one document may feed it — the primary. A duplicate slug across two documents is a hard build error naming both, which is the desired behaviour rather than a limitation to work around.

Factoring is not free: a fragment removes a variant's freedom to say something differently. A variant that needs to diverge inlines its own copy and drops the include, which is a deliberate act rather than an accident. **The test is not "is this text identical today" but "must this text be identical, and is it likely to be edited."** Education failed the first test by one character — a stray full stop had already appeared in one file within a day of the variant being created — which is exactly the drift the fragments exist to prevent.

Nothing in the `pandoc_resume` submodule is involved in this. That submodule supplies style assets only and is never edited; includes are resolved by this repository's own build driver before Pandoc is invoked.

Three properties make the indirection safe to trust when reviewing rendered output:

1. **The resolved Markdown is a visible artifact.** Each document that uses an include is written to `pandoc_resume/output/<name>.prepared.md` — exactly the Markdown Pandoc received, sitting next to the PDF and DOCX. When a rendered document looks wrong, open that file: it answers "did the include put what I expected where I expected it?" without reasoning about the build.
2. **A missing fragment stops the build**, naming the document, the fragment and the path it looked for. It never resolves to nothing, because that would strip every link from a document and still produce a plausible-looking artifact.
3. **`verify` proves the links survived.** It checks that every `[key]` used is defined in the Markdown Pandoc actually received, then counts real links in all four rendered formats and prints them side by side. A collapsed include shows up immediately as zeros. DOCX counts unique targets while the others count occurrences, so a lower DOCX number is expected, not a fault.

Add a fragment when content must be *identical* across variants. Divergence between variants is the point of having them — do not factor out something a variant should be free to change.

### Choosing a variant to submit

Read the position description for its centre of gravity. Embedded, firmware, C/C++/Rust, device, real-time, or an explicit Principal/Staff title on a systems team → the embedded variant. Mixed or data/ML-leaning, or where breadth across the whole career is the asset → the primary. When genuinely unsure, the primary is the safer default: it claims less about focus and nothing about it is wrong.

## Related

- [Brag file workflow](../workflows/brag-file.md) — capture and synthesis that feeds this pass.
- [Archive a source](../workflows/archive-source.md) — what happens to superseded documents.
