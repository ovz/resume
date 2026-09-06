"""Focused tests for PDF text extraction and non-text review assets."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pymupdf


SCRIPT = Path(__file__).parents[1] / "extract_pdf.py"


def write_pdf(path: Path, *, with_vector_figure: bool) -> None:
    """Create a deterministic one-page fixture PDF."""
    with pymupdf.open() as document:
        page = document.new_page(width=300, height=300)
        page.insert_text((40, 50), "Fixture text")
        if with_vector_figure:
            page.draw_rect(
                pymupdf.Rect(40, 80, 260, 220),
                color=(0, 0, 0),
                fill=(0.9, 0.9, 0.9),
                width=2,
            )
            page.draw_line((60, 150), (240, 150), color=(0, 0, 0), width=2)
        document.save(path)


def run_extractor(src: Path, dst: Path) -> subprocess.CompletedProcess[str]:
    """Run the staged extractor under the current uv-managed interpreter."""
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(src), str(dst)],
        check=False,
        capture_output=True,
        text=True,
        timeout=30,
    )


def test_text_only_page_keeps_text_only_output(tmp_path: Path) -> None:
    src = tmp_path / "text-only.pdf"
    dst = tmp_path / "text-only.md"
    write_pdf(src, with_vector_figure=False)

    result = run_extractor(src, dst)

    assert result.returncode == 0, result.stderr
    text = dst.read_text(encoding="utf-8")
    assert "<!-- page 1 -->" in text
    assert "Fixture text" in text
    assert "non-text-review" not in text
    assert not (tmp_path / "text-only-assets").exists()


def test_vector_figure_emits_deterministic_review_asset(tmp_path: Path) -> None:
    src = tmp_path / "figure.pdf"
    dst = tmp_path / "figure.md"
    assets_dir = tmp_path / "figure-assets"
    write_pdf(src, with_vector_figure=True)

    result = run_extractor(src, dst)

    assert result.returncode == 0, result.stderr
    text = dst.read_text(encoding="utf-8")
    assert "non-text-review: page=1" in text
    assert "embedded_images=0" in text
    assert "transcription=required" in text
    assert "![Page 1 non-text content](figure-assets/page-1.png)" in text
    assert (assets_dir / "page-1.png").is_file()


def test_rerun_removes_only_stale_generated_assets(tmp_path: Path) -> None:
    src = tmp_path / "changing.pdf"
    dst = tmp_path / "changing.md"
    assets_dir = tmp_path / "changing-assets"
    write_pdf(src, with_vector_figure=True)
    assert run_extractor(src, dst).returncode == 0
    assert (assets_dir / "page-1.png").is_file()
    reviewer_note = assets_dir / "transcription.md"
    reviewer_note.write_text("keep", encoding="utf-8")

    src.unlink()
    write_pdf(src, with_vector_figure=False)
    result = run_extractor(src, dst)

    assert result.returncode == 0, result.stderr
    assert assets_dir.is_dir()
    assert reviewer_note.read_text(encoding="utf-8") == "keep"
    assert not (assets_dir / "page-1.png").exists()
    assert "non-text-review" not in dst.read_text(encoding="utf-8")
