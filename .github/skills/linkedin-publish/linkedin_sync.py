#!/usr/bin/env python3
"""Track which generated LinkedIn blocks have actually reached the profile.

LinkedIn has no writable API for the About section or an Experience
description (see the workflow page this skill points at), so publishing is a
human pasting into a web form. That leaves a gap this tool closes.

`git status` after a build tells you which blocks changed — until you commit,
after which the signal is gone and the only record of whether you ever pasted
is memory. This tool keeps that record in `linkedin/paste-state.json`: the
SHA-256 of each block's text as of the last time you confirmed pasting it. A
block whose current text hashes differently is out of sync with the profile,
and it stays reported as out of sync across commits, reboots and machines.

    linkedin-sync status              what is out of sync
    linkedin-sync copy about          put one block on the clipboard
    linkedin-sync done about          record that it reached the profile
    linkedin-sync done --all          record every block as pasted

This tool touches no secrets and makes no network requests, which is why the
paste round works anywhere with a clipboard and needs no setup at all.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

STATE_NAME = "paste-state.json"
PROFILE_KEY = "oleg_linkedin"


def repo_root() -> Path:
    """The repo this file is installed in, whether via the skill or a launcher."""
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "markdown").is_dir() and (parent / ".git").exists():
            return parent
    return Path.cwd()


def blocks(linkedin_dir: Path) -> dict[str, str]:
    """Every generated block, slug -> text. Excludes the index and the state."""
    return {
        f.stem: f.read_text(encoding="utf-8")
        for f in sorted(linkedin_dir.glob("*.txt"))
    }


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_state(path: Path) -> dict:
    if not path.is_file():
        return {"blocks": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        sys.exit(f"error: {path} is not valid JSON ({exc}). Fix or delete it.")
    data.setdefault("blocks", {})
    return data


def save_state(path: Path, state: dict) -> None:
    # Sorted keys and a trailing newline: this file is committed, and a diff
    # should show a paste, not a reordering.
    path.write_text(
        json.dumps(state, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def profile_url(root: Path) -> str | None:
    """Read the profile URL from the resume's own reference-link block."""
    links = root / "markdown" / "_parts" / "links.md"
    if not links.is_file():
        return None
    m = re.search(rf"^\[{PROFILE_KEY}\]:\s*(\S+)", links.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else None


def rows(linkedin_dir: Path, state: dict) -> list[tuple[str, str, str, int]]:
    """(slug, verdict, when, chars) for every block, worst first."""
    out = []
    for slug, text in blocks(linkedin_dir).items():
        rec = state["blocks"].get(slug)
        chars = len(text.rstrip("\n"))
        if rec is None:
            out.append((slug, "NEVER PASTED", "—", chars))
        elif rec.get("sha256") != digest(text):
            out.append((slug, "NEEDS PASTE", rec.get("pasted_at", "?"), chars))
        else:
            out.append((slug, "in sync", rec.get("pasted_at", "?"), chars))
    order = {"NEVER PASTED": 0, "NEEDS PASTE": 1, "in sync": 2}
    return sorted(out, key=lambda r: (order[r[1]], r[0]))


def cmd_status(args, root: Path, linkedin_dir: Path, state_path: Path) -> int:
    state = load_state(state_path)
    table = rows(linkedin_dir, state)
    if not table:
        print("No generated blocks. Run: script/pandoc_resume.sh linkedin")
        return 0

    print(f"{'BLOCK':34s} {'STATUS':14s} {'LAST PASTED':12s} {'CHARS':>6s}")
    for slug, verdict, when, chars in table:
        print(f"{slug:34s} {verdict:14s} {when:12s} {chars:6d}")

    stale = [r for r in table if r[1] != "in sync"]
    print()
    if not stale:
        print("Profile matches the resume. Nothing to paste.")
        return 0
    print(f"{len(stale)} block(s) to paste. For each:")
    for slug, *_ in stale:
        print(f"    linkedin-sync copy {slug}   # then paste, then: linkedin-sync done {slug}")
    # A non-zero exit makes this usable as a check in a script or a prompt hook
    # without having to parse the output.
    return 1


def clipboard_command() -> list[str] | None:
    if os.environ.get("WAYLAND_DISPLAY") and shutil.which("wl-copy"):
        return ["wl-copy"]
    for cmd in (["xclip", "-selection", "clipboard"], ["xsel", "--clipboard", "--input"]):
        if shutil.which(cmd[0]):
            return cmd
    return None


def cmd_copy(args, root: Path, linkedin_dir: Path, state_path: Path) -> int:
    available = blocks(linkedin_dir)
    text = available.get(args.slug)
    if text is None:
        print(f"error: no block '{args.slug}'. Available: {', '.join(available)}", file=sys.stderr)
        return 1

    clip = clipboard_command()
    if clip is None:
        print("error: no clipboard tool found (wl-copy, xclip or xsel).", file=sys.stderr)
        print(f"       The text is in {linkedin_dir / (args.slug + '.txt')}", file=sys.stderr)
        return 1

    body = text.rstrip("\n")
    subprocess.run(clip, input=body, text=True, check=True)
    print(f"Copied {args.slug} to the clipboard — {len(body)} characters.")

    if args.open:
        url = profile_url(root)
        if url and shutil.which("xdg-open"):
            subprocess.Popen(
                ["xdg-open", url],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
            print(f"Opened {url}")
        else:
            print("Could not resolve the profile URL; open LinkedIn yourself.")

    print()
    print("Select all in the LinkedIn field before pasting — LinkedIn appends to")
    print("whatever is already there rather than replacing it.")
    print(f"Then record it:  linkedin-sync done {args.slug}")
    return 0


def cmd_done(args, root: Path, linkedin_dir: Path, state_path: Path) -> int:
    available = blocks(linkedin_dir)
    if args.all:
        slugs = list(available)
    elif args.slug:
        if args.slug not in available:
            print(f"error: no block '{args.slug}'. Available: {', '.join(available)}", file=sys.stderr)
            return 1
        slugs = [args.slug]
    else:
        print("error: name a block, or pass --all", file=sys.stderr)
        return 1

    state = load_state(state_path)
    today = date.today().isoformat()
    for slug in slugs:
        text = available[slug]
        state["blocks"][slug] = {
            "sha256": digest(text),
            "chars": len(text.rstrip("\n")),
            "pasted_at": today,
        }
        print(f"recorded {slug} as pasted ({today})")

    # Blocks that no longer exist were renamed or dropped from the resume;
    # their record is meaningless and would show up forever as a stale entry.
    for gone in set(state["blocks"]) - set(available):
        del state["blocks"][gone]
        print(f"dropped record for removed block {gone}")

    save_state(state_path, state)
    print(f"\nState written to {state_path}. Commit it — that is what makes the")
    print("record survive a fresh clone.")
    return 0


def main() -> int:
    root = repo_root()
    parser = argparse.ArgumentParser(
        prog="linkedin-sync",
        description=__doc__.split("\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--linkedin-dir",
        type=Path,
        default=root / "linkedin",
        help="directory holding the generated blocks (default: <repo>/linkedin)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="show which blocks are out of sync with the profile")

    p_copy = sub.add_parser("copy", help="put one block on the clipboard")
    p_copy.add_argument("slug")
    p_copy.add_argument(
        "--open", action="store_true", help="also open the LinkedIn profile in a browser"
    )

    p_done = sub.add_parser("done", help="record that a block reached the profile")
    p_done.add_argument("slug", nargs="?")
    p_done.add_argument("--all", action="store_true", help="record every block as pasted")

    args = parser.parse_args()
    linkedin_dir = args.linkedin_dir
    if not linkedin_dir.is_dir():
        print(f"error: no {linkedin_dir}. Run: script/pandoc_resume.sh linkedin", file=sys.stderr)
        return 1

    handler = {"status": cmd_status, "copy": cmd_copy, "done": cmd_done}[args.command]
    return handler(args, root, linkedin_dir, linkedin_dir / STATE_NAME)


if __name__ == "__main__":
    sys.exit(main())
