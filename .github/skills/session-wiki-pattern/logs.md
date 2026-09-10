---
name: session-wiki-logs
description: "Reference for session-wiki-pattern — operations log physical design, chunking, and why an operations log is never version-controlled."
---

# Session logs: physical design

> Companion to [`SKILL.md`](SKILL.md). Load when creating or rolling a log chunk, or deciding where a knowledge base's operations log belongs.

## Session log: `session-wiki/log/` (always) and scope-root `logs/` (optional)

Two distinct logs may exist, never conflated:

- **`session-wiki/log/`** is ALWAYS present. It is session-wiki's own operations log — raw captured, synthesized, promoted, and archived. Every scope has one, because every scope's session-wiki has construction activity worth logging.
- **Scope-root `logs/`** is OPTIONAL, on the same footing as `session-wiki-archive/`: create it only when the scope has a genuine narrative that is NOT about session-wiki's own construction — e.g. real ticket/engineering work (implementation decisions, bugs found and fixed) that exists independently of building the wiki itself. A scope whose whole story IS the session-wiki (nothing beyond wiki construction happened) has no need for a scope-root `logs/` — do not maintain an empty or duplicate one "just in case".

Unlike curated, version-controlled content, both logs are expected to capture ALL side quests, archival decisions, and dead ends — not just the clean narrative. They are closer to an **audit trail** than a curated index, and are more likely to be inspected or audited precisely because they are the honest, complete record rather than a curated one.

Physical design (transferable — describe the shape generically; applies identically to BOTH `session-wiki/log/` and scope-root `logs/`, when the latter exists — **and to a durable knowledge base's own operations log, which is itself scratch; see *An operations log is never version-controlled* below**):

- **Chunk filename:** `YYYY-MM-DD.md` for the first chunk of a day; `YYYY-MM-DD-2.md`, `YYYY-MM-DD-3.md`, … for subsequent chunks. A wave-based scheme (`<wave>-NN.md`) is equally acceptable, as long as it carries a numeric suffix so same-period rollover has an unambiguous next filename.
- **Cap** each chunk at roughly 1 000 lines; roll to the next suffix once a chunk would exceed that.
- **Entry header convention:** `## [YYYY-MM-DD] <op> | <subject>` — a stable prefix makes the log greppable with `grep "^## \[" <chunk> | tail`.
- **Ingest entries additionally record provenance**, so a claim can be traced back to the artifact it came from:
  ```
  ## [YYYY-MM-DD] ingest | <source title> → <destination>
  <one-line summary of what changed>
  - raw file: `raw/<exact-filename>`
  - sha256: `<full-64-char-hex-digest>`
  ```
- Maintain a lightweight `index.md` (a log-of-logs) that summarizes each chunk — its date/wave range and a one-line summary — so a fresh agent resuming after a long gap can jump straight to the relevant era instead of reading every chunk in order.
- Design for resuming after a long dormancy on the order of a couple of years; do not over-engineer for a decade-plus.

## An operations log is never version-controlled

This holds for a **durable, committed** knowledge base too, where the host repo keeps one — not just for session scratch. Such a base earns its keep through distilled knowledge; an append-only "what happened when" log makes it grow with **time** instead of with **knowledge**, and every entry ages into noise a reviewer must still read past. Worse, log entries are exactly the content most likely to cite scratch paths, work waves, and in-flight state — which would put a committed file in violation of *The one-way reference rule* above.

So: a committed knowledge base keeps its operations log in the **scratch scope of whoever maintains it**, using the same shape described here. What graduates into the committed side is the resulting knowledge page, not the record of the session that produced it. How the team arrived at an explanation is reviewed before the knowledge is committed; it is not maintained under version control afterwards.

