# Large imports

> **Doc type:** how-to
>
> How a large source — a board or ticket export, a mailbox or chat archive, a data dump — is preserved in this wiki without bloating the repository. Audience: the owner, and any agent asked to bring in a source too big to commit as-is.

## When this applies

Any source that is worth keeping **verbatim and permanently**, and is either a binary or larger than roughly 1 MB of text. Below that, commit it plainly; the machinery here is not worth its overhead.

This page is the repo-specific half. The mechanics — the format decision, the tool, the verification step — belong to the [`large-import` skill](../../../.github/skills/large-import/SKILL.md), which is written to be transferable and knows nothing about this wiki. Load it when doing the work; read this page for where things go and who decides.

## The tier question comes first

A large file is **T2 by size alone** under [sensitivity tiers](sensitivity-tiers.md) rule 5. Committing one is an exception, and an exception is **the owner's call, never an agent's**.

An agent that believes a large source should be preserved says so and stops. It does not compress and commit on its own initiative, and it does not treat an earlier exception as precedent — each source is decided on its own.

Once the owner has decided, the exception is recorded where the files live (the raw store's `README.md`), stating what it does *not* license. Preservation is not permission to quote outward: material still travels the normal path to `markdown/`, through a brag entry and a promotion pass.

## Where it goes

```
llm-wiki/raw/<source>/               committed: the archives + README manifest
  README.md                          what these are, the tier exception, the manifest
  YYYY-MM-DD-<name>.<ext>.xz         one compressed, checksummed snapshot per export

llm-wiki/wiki/sources/<source>.md    committed: the source page — what it contributes,
                                     what has been harvested, what remains
```

The **uncompressed working copy lives in the maintainer's session-wiki scratch scope**, under that scope's `session-wiki/raw/`. That is the copy ingest actually reads. It is never committed, and — per the one-way reference rule — **no committed file names a path to it.** The raw store's README may say that a working copy convention exists; it may not say where.

## Procedure

1. **Get the owner's tier decision.** Do not proceed without it.
2. **Land the uncompressed original** in the owning scope's `session-wiki/raw/`, renamed to `YYYY-MM-DD-<source>-<kind>.<ext>`, dated by when the export was taken. Record the exporter's original filename in that scratch directory's own README — export filenames often carry a board or account ID that is genuine provenance.
3. **Pack, verify, and record the manifest row** — the [`large-import` skill](../../../.github/skills/large-import/SKILL.md) § *Procedure* owns these three steps:
   ```bash
   python3 script/large-import.py pack   <scratch>/<name>.json --out llm-wiki/raw/<source>/
   python3 script/large-import.py verify llm-wiki/raw/<source>/<name>.json.xz --sha256 <recorded>
   ```
4. **Write or update `wiki/sources/<source>.md`** — role, vintage, what it uniquely contributes, harvest status, tier. This is what makes the archive findable; an archive with no source page is a file nobody will ever open again.
5. **Update `wiki/sources.md`, `index.md`, and the raw store's README manifest.**
6. **Harvest into brag entries** as normal — [brag file workflow](brag-file.md) § *Part 2*. Archiving a source is not ingesting it; the source page's harvest map is what tracks the difference.

## Re-exports are additive

A later export is a **new dated file beside the old one**, never a replacement. A tidied board loses cards, and a snapshot's whole value is that it still holds what the source held that day. The packing tool refuses to overwrite for this reason.

On re-ingest, diff against the previous snapshot rather than re-reading everything — what matters is what is new.

## Why the committed copy is compressed and checksummed

Both properties exist to defend the same thing: a file declared immutable actually staying that way.

Compression means a stray shell redirection cannot quietly append plausible-looking text to a source file. The recorded plaintext SHA-256 means that if something does go wrong, it is detectable in seconds rather than discovered years later when the original is gone. This is not theoretical — a committed board export in this repo was found with a filename appended to it by a misdirected redirect, leaving a 5.9 MB JSON that no longer parsed. The checksum is what identified the good copy.

## Related

- [`large-import` skill](../../../.github/skills/large-import/SKILL.md) — the format decision, the tool, and the verification step.
- [Sensitivity tiers](sensitivity-tiers.md) — rule 5 (large files) and rule 6 (only the owner downgrades).
- [Trello board exports](../sources/trello-boards.md) — the standing instance of this workflow.
- [Brag file workflow](brag-file.md) — how harvested material becomes an entry.
