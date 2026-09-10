# Brag drop zone

**Capturing something new? Write it in [`inbox/`](inbox/), not here.** Any filename, any shape, no polish — a note in the inbox is un-ingested, and an empty inbox means everything has been. This folder holds the finished entries the ingest step produces from those notes.

One file per accomplishment as `YYYY-MM-DD-<slug>.md`, dated by the accomplishment (evidence date), not by the day the file was written. Template and rules: [`../../wiki/workflows/brag-file.md`](../../wiki/workflows/brag-file.md).

**These files are the durable record.** The verbatim input they were written from lives in the maintainer's gitignored scratch scope, which does not survive a new machine — so the entry itself has to carry the technical substance. Preserve mechanisms, schemas, failure modes, reasoning and the owner's own wording; abstract only what the sensitivity tier requires, never for brevity. Keep every rendering the owner supplied rather than choosing between them.

Check for an existing entry on the same accomplishment first and classify what you have — duplicate (merge), update (augment in place), or related (new entry, cross-linked). Entries are living records: edit or append freely, and log every change day in the trailing `## Record history` section.

Ingest state lives in [`../../wiki/sources/brag-ledger.md`](../../wiki/sources/brag-ledger.md); what has and has not reached the resume lives in [`../../wiki/resume/coverage.md`](../../wiki/resume/coverage.md). Tag every entry `sensitivity: public-friendly` or `sensitivity: private-repo` — anything that cannot be tagged either way does not belong in this repository.
