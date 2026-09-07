# Archive a Superseded Source Document

> **Doc type:** how-to
>
> Moving a document out of `markdown/` (the pandoc build input and outward-facing set) into `llm-wiki/raw/archive/` once it no longer represents the owner. Audience: any agent maintaining the wiki; the owner approves the move.

## When

A `markdown/*.md` file is due to archive when **all** of these hold:

- It is no longer sent to anyone or mirrored anywhere (the primary resume and the references document are live; see [sources.md](../sources.md)).
- A newer document covers its purpose, or its purpose has lapsed.
- Its summary page under [`wiki/sources/`](../sources.md) exists and states what knowledge it still contributes and where that knowledge has been (or will be) harvested.

A document that still has un-harvested knowledge **may still be archived**: `raw/archive/` is readable, immutable, and citable, so harvesting can continue from there. What must not happen is archiving without a summary page — that is how knowledge gets lost.

## Steps

1. **Write or refresh the summary page** `wiki/sources/<short-name>.md`: role and vintage of the document, what is unique in it, harvest map (section → target wiki page → status), tier, and the archive disposition.
2. **Move with history:** from the repo root, `git mv markdown/<file>.md llm-wiki/raw/archive/<file>.md`. Keep the filename; do not edit the content (raw is immutable).
3. **Note dangling relative links.** Files from `markdown/` reference `assets/oleg-zhylin-gravatar.png` relatively; after the move that image link dangles. Do not fix it in the archived file; mention it in the summary page.
4. **Update navigation:** the row in [sources.md](../sources.md) (status → archived, path → `raw/archive/`), the summary page's source links, and [`index.md`](../../index.md) if the summary page is new.
5. **Check for inbound links** across `llm-wiki/wiki/**` that still point at `markdown/<file>.md` and re-point them.
6. **Confirm the build still runs** (`script/pandoc_resume.sh html`); output for the archived file will simply stop being regenerated. Existing generated files in the `pandoc_resume` submodule are not touched.
7. **Record** the move in the maintainer's operations log (outside version control). Hand the diff to the owner; agents do not commit.

## Reversal

`git mv` back, restore the row in `sources.md`, and note the reversal in the summary page. Nothing else is needed because the content was never edited.

## Related

- [Source map](../sources.md) — the current disposition of every source.
- [Sensitivity tiers](sensitivity-tiers.md) — archived documents keep their tier; archiving is not declassification.
