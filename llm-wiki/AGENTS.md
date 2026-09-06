# Resume Wiki Schema

This directory is a maintained knowledge layer for the resume repository. It is
not the resume build input and must not change the generated files under
`pandoc_resume/output/`.

## Layers

- `raw/` contains captured reference material. Treat existing files as
  immutable. New web clippings, notes, or transcripts belong here.
- `../markdown/` is the primary source corpus for resume claims. The files are
  maintained source documents and must not be rewritten as part of wiki work.
- `../archive/` contains historical source material and correspondence.
- `wiki/` contains synthesized pages written by the LLM.
- `index.md` catalogs wiki pages and their source coverage.
- `log.md` is append-only operational history.

## Page conventions

- Use lowercase, descriptive filenames with hyphens.
- Use Markdown links relative to the page making the link.
- Every substantive claim must link to one or more source files.
- Distinguish explicit source claims from synthesis or inference.
- When sources disagree, preserve the disagreement and identify the source
  rather than silently choosing a version.
- Keep raw sources unchanged. Update generated pages, `index.md`, and append a
  dated entry to `log.md` when incorporating a source.

## Workflows

### Ingest

1. Read the source completely and identify its date, provenance, and claims.
2. Add or update the relevant page in `wiki/` with source links.
3. Update `wiki/overview.md` when the overall career synthesis changes.
4. Update `index.md` and append an `ingest` entry to `log.md`.

### Query

1. Read `index.md` first, then the smallest set of relevant wiki pages.
2. Answer with links to the supporting source files and mark uncertainty.
3. File durable comparisons or analyses under `wiki/analysis/` and update the
   index and log.

### Lint

Check for broken links, unsupported claims, stale summaries, contradictions,
orphan pages, and source material that has not been integrated. Record notable
findings in `log.md`; do not alter raw sources during linting.