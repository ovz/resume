---
name: pdf-extraction
description: "Extract text and discover non-text PDF content using the repo's canonical uv script. Emits page-marked Markdown plus deterministic review images and transcription cues for pages containing raster or vector resources. USE WHEN ingesting any PDF into the LLM-Wiki, a session-wiki, or another doc/wiki pipeline. DO NOT USE for non-PDF formats or OCR of scanned/image-only text."
---

# PDF Extraction

Canonical, reusable PDF-to-Markdown extractor for **any** doc/wiki ingestion need in this repo. It preserves embedded text and makes pages with raster or vector resources visible for human/agent review. One script, one location; no ad-hoc PDF extraction scripts elsewhere in the repo.

## Script

[`extract_pdf.py`](extract_pdf.py) is a uv PEP 723 single-file script using `pypdf` for text and PyMuPDF for resource discovery and rendering, following [`python-uv-scripting`](../python-uv-scripting/SKILL.md) conventions.

```sh
uvx --with pymupdf --with pypdf python .github/skills/pdf-extraction/extract_pdf.py <src.pdf> <dst.md>
```

`uvx python` does not read the script's PEP 723 `dependencies` block, so the `--with` list mirrors it; keep the two in sync when adding a dependency. (Expected output with no arguments: a `usage:` line on stderr, exit 2.)

The script writes each page's embedded text to `<dst.md>`, separated by `<!-- page N -->` provenance markers. When a page contains embedded images or vector drawings, it also:

- renders the full page at 200 DPI to `<dst-stem>-assets/page-N.png`;
- appends a relative Markdown image reference under that page marker;
- records raster/vector counts in a `non-text-review` comment; and
- emits an explicit transcription requirement covering meaningful labels, connectors, decisions, tables, and other visual relationships.

Asset naming is deterministic. A rerun removes only extractor-owned `page-*.png` files before rendering, so stale page images cannot survive a changed source and reviewer-authored transcriptions in the assets directory remain intact.

## Behavior notes (read the script before trusting this)

- Text extraction still uses embedded text layers only. There is no OCR. Scanned/image-only pages are rendered and flagged for transcription, but their image text is not machine-transcribed.
- Resource discovery is deliberately conservative. Decorative vector paths can trigger a page render; a false-positive review image is preferable to silently losing a vector-only diagram.
- Full-page renders preserve relationships among text, connectors, and graphics that isolated embedded-image extraction can lose.
- Exit codes: `2` bad argc, `1` missing file or unreadable/corrupt PDF (`PdfReadError`), `0` success.
- Output is not reformatted/reflowed — table-of-contents entries, Smart-Link cards, and body text may interleave out of reading order (a known caveat already documented on ingested source pages, e.g. [`doc/llm-wiki/wiki/sources/cradle-tracking-current-state-2026-08-06.md`](../../../doc/llm-wiki/wiki/sources/cradle-tracking-current-state-2026-08-06.md)). Treat the output as a grep-friendly raw capture, not a clean read.

## Review and transcription workflow

1. Inspect every emitted page image against the source PDF.
2. Inventory meaningful non-text content per page, including figures, arrows, decision labels, code/table relationships, and visual grouping.
3. Transcribe the semantics into the source or synthesis page. Prefer Mermaid for flowcharts, plus concise factual notes for source details Mermaid cannot represent without inference.
4. Record ambiguous or unlabeled edges as ambiguous; do not silently invent labels.
5. Keep the generated image reference with the transcription so a human can verify it without reopening the PDF.

The extractor discovers and preserves review evidence. It does not claim to understand a figure automatically; ingestion is incomplete until the explicit review cue is resolved by a semantic transcription or description.

## Focused tests

[`tests/test_extract_pdf.py`](tests/test_extract_pdf.py) generates deterministic fixture PDFs and verifies text-only behavior, vector-only non-text discovery, deterministic asset naming and Markdown references, and stale-asset cleanup.

## Consumers

- **LLM-Wiki ingest** — [`doc/llm-wiki/schema/workflows.md`](../../../doc/llm-wiki/schema/workflows.md) § Ingest step 1 invokes this script for any PDF source landing under `raw/`.
- Any future doc/wiki ingestion pipeline in this repo (session-wikis, other doc systems) reuses this same script. If you're about to write a new `pypdf`/`pdfplumber` one-off, stop and use this instead.

## Relationship

- [`python-uv-scripting`](../python-uv-scripting/SKILL.md) — the uv/PEP 723 conventions this script follows.
- [`doc/llm-wiki/schema/workflows.md`](../../../doc/llm-wiki/schema/workflows.md) — the primary current consumer.
