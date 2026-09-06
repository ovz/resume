#!/usr/bin/env -S uvx --with pymupdf --with pypdf python
# /// script
# requires-python = ">=3.11"
# dependencies = ["pymupdf", "pypdf"]
# ///
"""Canonical PDF-to-Markdown extractor for any doc/wiki ingest in this repo.

Extracts each page's text and detects embedded images or vector drawings. Pages
with non-text resources get deterministic full-page PNG renders, Markdown image
references, and explicit transcription-review cues.

Usage:
    uvx --with pymupdf --with pypdf python .github/skills/pdf-extraction/extract_pdf.py <src.pdf> <dst.md>
"""
import sys
from pathlib import Path

import pymupdf
from pypdf import PdfReader
from pypdf.errors import PdfReadError


def extract_pdf(src: Path, dst: Path) -> tuple[str, int]:
    """Extract text and render pages whose resources require visual review."""
    reader = PdfReader(src)
    assets_dir = dst.with_name(f"{dst.stem}-assets")
    rendered_pages = 0
    parts: list[str] = []

    if assets_dir.exists():
        for stale_asset in assets_dir.glob("page-*.png"):
            stale_asset.unlink()

    with pymupdf.open(src) as document:
        if len(document) != len(reader.pages):
            raise PdfReadError(
                "page-count mismatch between text and rendering backends"
            )

        for page_number, (text_page, visual_page) in enumerate(
            zip(reader.pages, document), start=1
        ):
            parts.append(f"\n\n<!-- page {page_number} -->\n\n")
            parts.append(text_page.extract_text() or "")

            image_count = len(visual_page.get_images(full=True))
            drawing_count = len(visual_page.get_drawings())
            if image_count == 0 and drawing_count == 0:
                continue

            assets_dir.mkdir(parents=True, exist_ok=True)
            asset_name = f"page-{page_number}.png"
            asset_path = assets_dir / asset_name
            visual_page.get_pixmap(dpi=200, alpha=False).save(asset_path)
            relative_asset = (Path(assets_dir.name) / asset_name).as_posix()
            parts.append(
                "\n\n"
                f"<!-- non-text-review: page={page_number}; "
                f"embedded_images={image_count}; vector_drawings={drawing_count}; "
                "transcription=required -->\n\n"
                f"![Page {page_number} non-text content]({relative_asset})\n\n"
                "> **Transcription required:** Review this page image and describe or "
                "transcribe every meaningful figure, label, connector, decision, table "
                "relationship, and other non-text detail in the source or synthesis page.\n"
            )
            rendered_pages += 1

    if rendered_pages == 0 and assets_dir.exists() and not any(assets_dir.iterdir()):
        assets_dir.rmdir()

    return "".join(parts), rendered_pages


def main() -> None:
    if len(sys.argv) != 3:
        print(
            "usage: uvx --with pymupdf --with pypdf python .github/skills/pdf-extraction/extract_pdf.py <src.pdf> <dst.md>",
            file=sys.stderr,
        )
        sys.exit(2)

    src, dst = Path(sys.argv[1]), Path(sys.argv[2])

    try:
        text, rendered_pages = extract_pdf(src, dst)
    except FileNotFoundError:
        print(f"error: input not found: {src}", file=sys.stderr)
        sys.exit(1)
    except (PdfReadError, pymupdf.FileDataError) as exc:
        print(f"error: unreadable PDF {src}: {exc}", file=sys.stderr)
        sys.exit(1)

    dst.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {dst}; rendered {rendered_pages} page(s)")


if __name__ == "__main__":
    main()
