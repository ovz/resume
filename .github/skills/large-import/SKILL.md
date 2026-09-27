---
name: large-import
description: "Bring a large source file — a board or ticket export, a mailbox or chat archive, a data dump — into a version-controlled raw store without bloating the repository. Establishes the two-copy split: an uncompressed working copy in the session scratch scope where ingest actually reads it, and a compressed, checksummed archive as the committed durable record. USE WHEN a source file is too large to commit as-is, when an export needs preserving verbatim, or when adding a later snapshot of a source already archived. DO NOT USE for deciding whether material may be committed at all — that is the host repo's own sensitivity policy, which this skill defers to."
---

# Large imports

A source file arrives that is worth keeping verbatim and forever, but is too large to drop into the repository as-is. This skill is the procedure that resolves that tension, and the format decision behind it.

The answer is **two copies with different jobs**, never one copy compromising between them:

```
session scratch (gitignored)          version-controlled raw store
  session-wiki/raw/<name>.ext    →      raw/<source>/<name>.ext.xz
  uncompressed, working copy            compressed + checksummed, durable record
  read, grep, parse, ingest from here   never read directly; unpack when needed
```

## Why two copies

They are not redundant, because they answer different questions.

The **scratch copy is what ingest actually uses.** Harvesting a 6 MB JSON export means parsing it, grepping it, and re-reading it across many sessions. Doing that against a compressed blob means decompressing on every access, and doing it against a *committed* file means every incidental edit — a stray shell redirection, an editor's trailing newline — silently rewrites a file that was supposed to be immutable. Scratch is the right place for a working copy precisely because nothing there is precious.

The **committed archive is the durable record.** It survives the workstation, reaches a fresh clone, and carries a checksum that proves it is still the bytes that were exported. It is a preservation copy, not a reading surface.

This split is the reason the archive may be compressed at all. Compression costs nothing in usability when nobody reads the compressed copy directly.

## Format: xz, and why

**Use `.xz` (LZMA2), preset 9 + EXTREME, container check SHA-256.** `archive.py` in this directory is the only thing that needs to know that.

The choice was made against measured numbers on a real 6.0 MB minified-JSON export, not from habit:

| Format | Archive size | % of original | Notes |
|---|---|---|---|
| raw, committed as-is | 6,284,427 B | 100% | git zlib-deflates it to ~635 KB in the pack |
| gzip -9 / zip -9 | ~632,000 B | 10.1% | **no gain** — same deflate git already applies |
| bzip2 -9 | 493,392 B | 7.9% | superseded by both below |
| zstd -19 | 424,025 B | 6.7% | excellent, but not installed by default anywhere |
| **xz -9e** | **394,808 B** | **6.3%** | best ratio; stdlib-decodable everywhere |

Two conclusions drive the decision:

1. **gzip and zip are pointless here.** Git already deflates every blob it stores, so committing a `.gz` produces a pack almost exactly the size of committing the plain file. A format has to beat deflate to be worth the loss of readability, and only xz and zstd do so meaningfully.
2. **xz wins on reach, not just ratio.** Python's standard library decodes xz through `lzma` — no install, on every platform, since Python 3.3. That makes the *guaranteed* decompression path a bare `python3` interpreter, which is a far safer assumption than any particular CLI tool being present. zstd compresses comparably but has no stdlib reader and ships by default on nothing.

Cross-platform decompression paths, in the order to reach for them:

| Platform | Always works | Also works |
|---|---|---|
| Any | `python3 archive.py unpack <file>.xz` | any Python: `import lzma` |
| Linux | `unxz -k`, `xz -dc` | GNOME Files, Ark, most archive managers |
| macOS | Python stdlib (ships with the OS toolchain) | `tar -xJf`, The Unarchiver, `brew install xz` |
| Windows | Python stdlib | 7-Zip, PeaZip, WinRAR; `tar.exe` on Windows 10+ |

### What about delta compression across snapshots?

Worth knowing before someone reopens the question. Git delta-compresses similar blobs, and two *byte-stable* snapshots of the same export do pack better as plain text (measured: 685 KB for two snapshots) than as two independent xz files (780 KB). That is a real effect and the honest counter-argument.

It does not change the decision, for two reasons. The pack difference is under 100 KB and does not compound, whereas the working-tree difference is 15× on every clone, forever. And the delta only materializes if the exporter's serialization stays byte-stable between snapshots — field order, whitespace, and newly added API fields all destroy it, and none of that is under this repo's control. Trading a guaranteed 15× for a conditional 12% is the wrong side of the bet.

## Procedure

### 1. Land the uncompressed copy in scratch

Put the original in the owning scope's `session-wiki/raw/`. Rename it to the archive's naming convention *now*, so the two copies stay obviously paired, and record the exporter's original filename in that directory's `README.md` — export filenames often carry a board or account ID that is real provenance.

Name it `YYYY-MM-DD-<source>-<kind>.<ext>`, dated by **when the export was taken**, not when it was ingested.

### 2. Pack into the raw store

```bash
python3 .github/skills/large-import/archive.py pack <scratch>/<name>.json --out <raw-store>/
```

It prints the plaintext size, the archive size, the plaintext SHA-256, and a ready-made manifest row.

### 3. Verify before trusting it

```bash
python3 .github/skills/large-import/archive.py verify <raw-store>/<name>.json.xz --sha256 <recorded>
```

Do this as a distinct step, not as an assumption. `verify` streams the archive back out and re-hashes the plaintext, so it catches a truncated write, a corrupted blob, and a mismatch against what was recorded — the three failures that otherwise surface years later when the original is long gone.

### 4. Record the manifest

The raw store's `README.md` carries one row per archive: filename, plaintext size, archive size, and plaintext SHA-256. **The hash is of the plaintext, not the archive** — that is what makes integrity checkable independently of which compressor version wrote the file, and what lets a future reader confirm an unpacked copy is genuine.

### 5. Never overwrite a snapshot

A later export is a **new dated file alongside the old one**, never a replacement. A tidied source loses material, and the entire point of a snapshot is that it still holds what the source held that day. `archive.py pack` refuses to overwrite for this reason; `--force` exists for fixing a botched write in the same session, not for re-exporting.

On re-ingest, diff against the previous snapshot rather than re-reading in full — what matters is what changed.

## Integrity is the thing that actually goes wrong

The failure this procedure is built against is not disk loss. It is a "verbatim, immutable" file being quietly modified in place, and nobody noticing until the original is unrecoverable.

That is not hypothetical: this procedure was established after a committed export was found with a stray filename appended to it by a misdirected shell redirection, leaving a 5.9 MB JSON file that no longer parsed. The recorded checksum is what turned that from an undetectable corruption into a five-second diagnosis.

Hence: the committed copy is compressed (so a stray `>>` cannot append plausible-looking text to it), checksummed against its plaintext (so corruption is detectable), and never the copy anyone works from (so nothing routinely has it open for writing).

## What this skill does not decide

**Whether the material may be committed at all.** That is the host repo's sensitivity or classification policy, and it wins. This skill covers only *how* something already cleared for the raw store gets there. Where the host repo tiers its content, a large file is often excluded by size alone, and an exception is the owner's call to make and to record — not an agent's, and not this skill's.

**What the archive licenses.** Preserving a source verbatim is not permission to quote it outward. An archive is a record; anything travelling from it into an outward-facing document goes through whatever review path the host repo defines for that.

## Reference-direction reminder

The raw store is version-controlled and the working copy is not, so the `session-wiki-pattern` skill's (agentic_linux repo) one-way reference rule applies at full strength: **the raw store's `README.md` must never point at the scratch copy.** It may describe the convention that an uncompressed working copy exists in a scratch scope; it may not name a path to one. A fresh clone has no scratch directory, and a pointer into one is dead on arrival and silently so.
