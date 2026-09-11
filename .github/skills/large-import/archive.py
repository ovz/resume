#!/usr/bin/env python3
"""Pack, verify and unpack large source files for a version-controlled raw store.

Standard library only, on purpose. A committed archive is worthless if the
machine that needs it cannot open it, so this script depends on nothing beyond
a Python 3.8+ interpreter -- which every platform this repo targets already has,
and which reads xz through the stdlib ``lzma`` module with no install at all.

Format is xz (LZMA2), preset 9 + EXTREME, with the container's own integrity
check set to SHA-256. Rationale and the numbers behind the choice: SKILL.md.

Usage:
    python3 archive.py pack   <source> [--out DIR] [--force]
    python3 archive.py verify <archive.xz> [--sha256 HEX]
    python3 archive.py unpack <archive.xz> [--out DIR] [--force]

``pack`` prints a manifest row for the raw store's README; ``verify`` re-reads
the archive and confirms the plaintext still hashes to what was recorded.
"""
from __future__ import annotations

import argparse
import hashlib
import lzma
import sys
from pathlib import Path

CHUNK = 1 << 20  # 1 MiB; keeps memory flat regardless of source size.

FILTERS = [{"id": lzma.FILTER_LZMA2, "preset": 9 | lzma.PRESET_EXTREME}]


def _open_xz_write(path: Path) -> lzma.LZMAFile:
    return lzma.open(
        path, "wb", format=lzma.FORMAT_XZ, check=lzma.CHECK_SHA256, filters=FILTERS
    )


def _human(n: int) -> str:
    """Render a byte count the way a README table wants to read."""
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:,.1f} {unit}"
        n /= 1024.0
    return f"{n} B"


def pack(source: Path, out_dir: Path | None, force: bool) -> int:
    if not source.is_file():
        sys.exit(f"error: not a file: {source}")

    dest_dir = out_dir or source.parent
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / (source.name + ".xz")

    # A snapshot store never overwrites: a re-export is a new dated file, and
    # silently replacing one destroys the only copy of what a board held then.
    if dest.exists() and not force:
        sys.exit(f"error: {dest} exists; snapshots are never overwritten (use --force to override)")

    digest = hashlib.sha256()
    raw_size = 0
    with source.open("rb") as src, _open_xz_write(dest) as dst:
        while chunk := src.read(CHUNK):
            digest.update(chunk)
            raw_size += len(chunk)
            dst.write(chunk)

    packed_size = dest.stat().st_size
    sha = digest.hexdigest()
    ratio = packed_size / raw_size * 100 if raw_size else 0.0

    print(f"packed  {source.name} -> {dest.name}")
    print(f"  plaintext {_human(raw_size)} ({raw_size:,} bytes)  sha256 {sha}")
    print(f"  archive   {_human(packed_size)} ({packed_size:,} bytes)  {ratio:.1f}% of original")
    print()
    print("manifest row:")
    print(f"| `{dest.name}` | {_human(raw_size)} | {_human(packed_size)} | `{sha[:16]}` |")
    return 0


def _rehash(archive: Path) -> tuple[str, int, int]:
    """Stream the archive back out and hash the plaintext without unpacking it."""
    digest = hashlib.sha256()
    raw_size = 0
    with lzma.open(archive, "rb", format=lzma.FORMAT_XZ) as src:
        while chunk := src.read(CHUNK):
            digest.update(chunk)
            raw_size += len(chunk)
    return digest.hexdigest(), raw_size, archive.stat().st_size


def verify(archive: Path, expected: str | None) -> int:
    if not archive.is_file():
        sys.exit(f"error: not a file: {archive}")

    try:
        sha, raw_size, packed_size = _rehash(archive)
    except lzma.LZMAError as exc:
        sys.exit(f"FAIL {archive.name}: archive is corrupt ({exc})")

    print(f"{archive.name}: decompresses cleanly")
    print(f"  plaintext {_human(raw_size)} ({raw_size:,} bytes)  sha256 {sha}")
    print(f"  archive   {_human(packed_size)} ({packed_size:,} bytes)")

    if expected:
        # Accept a truncated hash so a README's shortened value can be checked
        # without copying the full 64 characters back out of it.
        want = expected.strip().lower().replace(" ", "")
        if not sha.startswith(want):
            sys.exit(f"FAIL {archive.name}: plaintext sha256 {sha} does not match expected {want}")
        print(f"  sha256 matches expected {want}")
    return 0


def unpack(archive: Path, out_dir: Path | None, force: bool) -> int:
    if not archive.is_file():
        sys.exit(f"error: not a file: {archive}")
    if archive.suffix != ".xz":
        sys.exit(f"error: expected a .xz archive: {archive}")

    dest_dir = out_dir or archive.parent
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / archive.stem  # drops the .xz, restoring the original name

    if dest.exists() and not force:
        sys.exit(f"error: {dest} exists (use --force to overwrite)")

    digest = hashlib.sha256()
    raw_size = 0
    with lzma.open(archive, "rb", format=lzma.FORMAT_XZ) as src, dest.open("wb") as out:
        while chunk := src.read(CHUNK):
            digest.update(chunk)
            raw_size += len(chunk)
            out.write(chunk)

    print(f"unpacked {archive.name} -> {dest}")
    print(f"  plaintext {_human(raw_size)} ({raw_size:,} bytes)  sha256 {digest.hexdigest()}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="archive.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_pack = sub.add_parser("pack", help="compress a source file to <name>.xz")
    p_pack.add_argument("source", type=Path)
    p_pack.add_argument("--out", type=Path, default=None, help="destination directory")
    p_pack.add_argument("--force", action="store_true", help="overwrite an existing archive")

    p_verify = sub.add_parser("verify", help="check an archive decompresses and matches its hash")
    p_verify.add_argument("archive", type=Path)
    p_verify.add_argument("--sha256", default=None, help="expected plaintext hash (may be truncated)")

    p_unpack = sub.add_parser("unpack", help="restore the original file from an archive")
    p_unpack.add_argument("archive", type=Path)
    p_unpack.add_argument("--out", type=Path, default=None, help="destination directory")
    p_unpack.add_argument("--force", action="store_true", help="overwrite an existing file")

    args = parser.parse_args(argv)
    if args.command == "pack":
        return pack(args.source, args.out, args.force)
    if args.command == "verify":
        return verify(args.archive, args.sha256)
    return unpack(args.archive, args.out, args.force)


if __name__ == "__main__":
    sys.exit(main())
