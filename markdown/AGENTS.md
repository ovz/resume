# Outward-facing documents

Everything in this directory is a document that leaves the repository. `Oleg.Zhylin.resume.achievements.md` is the **primary, public resume**, mirrored to LinkedIn. `Oleg.Zhylin.professional.references.md` is **private** and never published. Both are Pandoc inputs; see the root [`AGENTS.md`](../AGENTS.md) for the build.

## Read before editing

Before changing any file here, read, in this order:

1. [`../llm-wiki/wiki/resume/primary-resume.md`](../llm-wiki/wiki/resume/primary-resume.md) — structure, the half-page / one-page / two-page cut principle, section and style rules.
2. [`../llm-wiki/wiki/resume/link-conventions.md`](../llm-wiki/wiki/resume/link-conventions.md) — every hyperlink is a pinned Wayback Machine snapshot.
3. [`../llm-wiki/wiki/resume/update-workflow.md`](../llm-wiki/wiki/resume/update-workflow.md) — the edit pass: draft, place at the right depth, link-check, sensitivity-check, render, lint, hand off.

Skipping step 1 produces text that reads well and sits at the wrong depth, which is the most common failure on this repo.

## Rules

- **Public tier.** The primary resume is T0 public. Nothing employer-internal, unpublished, or attributable to a colleague goes in it. Tier definitions: [`../llm-wiki/wiki/workflows/sensitivity-tiers.md`](../llm-wiki/wiki/workflows/sensitivity-tiers.md).
- **Brag entries are not promoted directly.** They flow `../llm-wiki/raw/brag/` → [`../llm-wiki/wiki/concepts/accomplishments-by-domain.md`](../llm-wiki/wiki/concepts/accomplishments-by-domain.md) → here, being rewritten at each step. Copying a brag entry into the resume skips the tier check and the depth check.
- **Contact details in the references document stay there.** Third-party names, phone numbers and emails are never copied into another file, a wiki page, a commit message, or a chat summary.
- **Links are Wayback snapshots.** A bare live URL rots; follow the link conventions page rather than pasting the URL you found.
- **Reference-style links.** Both documents define links at the bottom of the file (`[key]:url "Title"`). Keep new links in that block rather than inlining them.

## The portrait image

Both documents open with the portrait, written as a reference-style image link resolving to `assets/oleg-zhylin-gravatar.png` — a path relative to *this* directory, not to the build's working directory.

Two consequences:

- If you move or rename anything under `assets/`, update both documents and re-run the build.
- After any edit, run `script/pandoc_resume.sh all`. It ends with a `verify` pass asserting the image is embedded in all four formats. HTML, PDF, DOCX and RTF each embed images by a different mechanism, so a broken image path typically breaks *some* formats while others still look fine — the eye is not a reliable check here, and a rendered-looking HTML file proves nothing about the PDF.

## The LinkedIn character budget

Sections wrapped in `<!-- linkedin: <slug> limit=<n> -->` … `<!-- linkedin: end -->` are exported to `linkedin/` as the plain text pasted into the profile, and **the build fails when one exceeds its limit** — 2,600 characters for the About section, 2,000 for each Experience entry. Three consequences when editing:

- **Adding a sentence inside a marked section costs one somewhere else.** The counts are printed on every build; check them before deciding a paragraph is too tight to trim.
- **Never widen a `limit=` to make the build pass.** It is LinkedIn's number, not this repo's. Raising it only moves the truncation to the paste, where nothing reports it.
- **Keep the Markdown formatted.** The same text renders to PDF, HTML, DOCX and RTF, where emphasis is doing real work; the export strips it. Do not flatten the source to match what LinkedIn shows.

Only the primary resume carries these markers — one profile, one source. A duplicate slug in a second variant is a hard build error.

## Rendering check

An edit is not finished until the artifacts build clean:

```bash
script/pandoc_resume.sh all
```

Then read the rendered output, not just the Markdown — line breaks, table widths and page cuts in the PDF are where formatting regressions show up. The same run regenerates `linkedin/`; whatever `git status` reports as changed there is what has to be re-pasted into the profile.

Agents do not commit; see the root [`AGENTS.md`](../AGENTS.md).
