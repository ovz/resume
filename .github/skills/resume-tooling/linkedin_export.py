#!/usr/bin/env python3
"""Extract LinkedIn copy-paste blocks from the resume Markdown sources.

LinkedIn is a *lossy* target. It accepts no formatting at all — no bold, no
italics, no links, no headings — and it caps each field: 2,600 characters for
the About section ("My Story") and 2,000 for each Experience description. The
Markdown sources, meanwhile, must stay fully formatted, because the same text
is rendered to PDF, HTML, DOCX and RTF where emphasis is doing real work.

So the profile is not maintained by hand. Sections of the resume are marked as
LinkedIn blocks, this script renders each one down to plain text through Pandoc
and checks it against its budget, and the results are committed. A block that
outgrows its field fails the build rather than being silently truncated on
paste, and the committed output means `git status` after a build names exactly
which LinkedIn fields have drifted from the resume and need re-pasting.

Marking a block, in any document under markdown/:

    <!-- linkedin: about limit=2600 title="About (My Story)" -->
    ... Markdown ...
    <!-- linkedin: end -->

`limit` is required; `title` is optional and only labels the generated index.
The slug names the output file and must be unique across every source.

This file is the skill's own copy of the logic, not a pointer to one elsewhere:
dropped into another repo with the same markdown/ conventions, this skill
directory works unmodified. `script/pandoc_resume.sh` is a thin launcher onto
the build driver that calls this.

    python3 linkedin_export.py --out-dir <dir> <prepared.md> [<prepared.md> ...]
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# Opening marker: slug, then whitespace-separated key=value attributes.
BLOCK_OPEN = re.compile(
    r"^<!--\s*linkedin:\s*(?P<slug>[a-z0-9][a-z0-9-]*)\s+(?P<attrs>[^>]*?)\s*-->\s*$"
)
BLOCK_END = re.compile(r"^<!--\s*linkedin:\s*end\s*-->\s*$")
ATTR = re.compile(r'(?P<key>[a-z_]+)\s*=\s*(?:"(?P<quoted>[^"]*)"|(?P<bare>\S+))')

# Reference-link definitions live at the bottom of the file, in a shared
# fragment. A block lifted out of the middle of the document therefore carries
# `[text][key]` references whose definitions are nowhere in the extract, and
# Pandoc renders an undefined reference as its literal source text — so every
# link would arrive on LinkedIn as "Lively Mobile 2][r5]". The definitions are
# collected from the whole file and appended to each extracted block.
#
# The whitespace after the colon is optional, and must be: the shared fragment
# has always mixed `[key]: url` and `[key]:url`, Pandoc accepts both, and a
# pattern that demands the space silently drops half the definitions — which
# does not fail anything, it just publishes the unresolved source text.
LINK_DEF = re.compile(r"^\[[^\]]+\]:\s*\S")

# Pandoc's plain writer emits list items as a hyphen and padding — the padding
# width varies with --wrap, so match either. LinkedIn has no list markup either,
# but it does render a pasted bullet character, which is the closest thing to
# the Markdown intent that survives the round trip.
PANDOC_BULLET = re.compile(r"^(\s*)-[ ]{1,3}(?=\S)", re.M)


class BlockError(Exception):
    """A malformed marker, or a block over its character budget."""


def origin(path: Path) -> str:
    """The name of the file a person would actually edit.

    Blocks are read from the build's `<name>.prepared.md`, because that is where
    the shared _parts/ content — above all the reference-link definitions — has
    been resolved. Nobody edits that file, and its line numbers are shifted from
    the source by however much each include expanded, so every message names the
    original document instead.
    """
    return path.name.replace(".prepared.md", ".md")


def locate(block: dict) -> str:
    """A message-safe pointer to a block: a file to open and a string to find."""
    return f"{origin(block['source'])} (search for '<!-- linkedin: {block['slug']}')"


def parse_attrs(raw: str, slug: str, where: str) -> dict[str, str]:
    attrs = {
        m.group("key"): m.group("quoted") if m.group("quoted") is not None else m.group("bare")
        for m in ATTR.finditer(raw)
    }
    if "limit" not in attrs:
        raise BlockError(f"{where}: block '{slug}' has no limit= attribute")
    try:
        int(attrs["limit"])
    except ValueError:
        raise BlockError(f"{where}: block '{slug}' has a non-numeric limit={attrs['limit']!r}")
    return attrs


def extract_blocks(path: Path) -> list[dict]:
    """Return every marked block in one Markdown file, in document order."""
    lines = path.read_text(encoding="utf-8").splitlines()
    link_defs = [ln for ln in lines if LINK_DEF.match(ln)]

    blocks: list[dict] = []
    open_at: int | None = None
    slug = ""
    attrs: dict[str, str] = {}
    body: list[str] = []

    for lineno, line in enumerate(lines, start=1):
        where = f"{origin(path)}, line {lineno} of the prepared copy"
        # End first: "end" is a syntactically valid slug, so an opening-marker
        # test would claim the closing marker and every block would run to the
        # end of the file.
        if BLOCK_END.match(line):
            if open_at is None:
                raise BlockError(f"{where}: <!-- linkedin: end --> with no block open")
            blocks.append(
                {
                    "slug": slug,
                    "title": attrs.get("title", slug.replace("-", " ").title()),
                    "limit": int(attrs["limit"]),
                    "markdown": "\n".join(body),
                    "link_defs": link_defs,
                    "source": path,
                    "line": open_at,
                }
            )
            open_at = None
            continue
        opened = BLOCK_OPEN.match(line)
        if opened:
            if open_at is not None:
                raise BlockError(
                    f"{where}: block '{opened.group('slug')}' opens while "
                    f"'{slug}' (line {open_at}) is still open; add a "
                    f"<!-- linkedin: end --> marker"
                )
            slug = opened.group("slug")
            attrs = parse_attrs(opened.group("attrs"), slug, where)
            open_at, body = lineno, []
            continue
        if open_at is not None:
            body.append(line)

    if open_at is not None:
        raise BlockError(
            f"{origin(path)}: block '{slug}' is never closed; "
            f"add a <!-- linkedin: end --> marker after it"
        )
    return blocks


def to_plain_text(block: dict, bullet: str) -> str:
    """Render one block's Markdown to the plain text LinkedIn will receive.

    Pandoc's `plain` writer does the lossy part properly — emphasis dropped,
    reference links resolved to their visible text, URLs and link definitions
    discarded, Unicode punctuation preserved. `--wrap=none` keeps each
    paragraph on a single line, because LinkedIn reflows text itself and a
    hard-wrapped paste renders as a column of ragged short lines.
    """
    source = block["markdown"]
    if block["link_defs"]:
        source = source + "\n\n" + "\n".join(block["link_defs"])

    result = subprocess.run(
        ["pandoc", "--from", "markdown", "--to", "plain", "--wrap=none"],
        input=source,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        raise BlockError(
            f"pandoc failed on block '{block['slug']}' in "
            f"{locate(block)}:\n{result.stderr.strip()}"
        )

    text = PANDOC_BULLET.sub(rf"\1{bullet} ", result.stdout)
    text = "\n".join(line.rstrip() for line in text.splitlines())
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text + "\n"


def write_index(out_dir: Path, results: list[dict], bullet: str) -> None:
    """Write the human-facing index of what to paste where.

    Deliberately carries no timestamp or build counter: the whole point of
    committing this directory is that a file changes only when its *content*
    changes, so `git status` after a build is a precise list of the LinkedIn
    fields that need re-pasting. A generated-on line would dirty every file on
    every build and destroy that signal.
    """
    rows = "\n".join(
        f"| [`{r['slug']}.txt`]({r['slug']}.txt) | {r['title']} | {r['chars']:,} | "
        f"{r['limit']:,} | {r['limit'] - r['chars']:,} | "
        f"[`{origin(r['source'])}`](../markdown/{origin(r['source'])}) |"
        for r in results
    )
    # Each block is fenced so nothing re-renders: what the reviewer reads is
    # byte-for-byte what lands on the clipboard. Four backticks, because a
    # block quoting code in three would otherwise close the fence early.
    full = "\n\n".join(
        f"### {r['title']}\n\n"
        f"`{r['slug']}.txt` · {r['chars']:,} of {r['limit']:,} characters\n\n"
        f"````text\n{r['text'].rstrip()}\n````"
        for r in results
    )
    out_dir.joinpath("README.md").write_text(
        f"""# LinkedIn copy-paste blocks

**Generated — do not edit by hand.** `script/pandoc_resume.sh linkedin` rewrites
every file in this directory from the marked sections of the resume sources in
[`markdown/`](../markdown/). Edit the Markdown, re-run the build, paste the
result.

## Why this is committed

Generated output is normally kept out of version control, and the rest of this
repository's build output is. This directory is the deliberate exception,
because the artifact being tracked is not the text — it is **the diff**.
LinkedIn has no API in this workflow: updating the profile means a human
opening a field and pasting. Committing the rendered blocks makes `git status`
after a build the exact answer to "which LinkedIn fields have drifted from my
resume?" — a changed file is a field to re-paste, and an unchanged file is one
to leave alone. Nothing else in the pipeline can answer that question.

## What to paste where

| File | LinkedIn field | Characters | Limit | Headroom | Source |
|---|---|---:|---:|---:|---|
{rows}

A build **fails** when a block exceeds its limit, so these files are always
within budget. Character counts include line breaks, which LinkedIn counts too.

## The blocks, in full

Review the whole profile here, top to bottom, before running a single `copy`.
Each block is fenced so nothing is re-rendered — line breaks, bullets and
punctuation appear exactly as LinkedIn will receive them. The per-field `.txt`
files are still what `linkedin-sync copy` puts on the clipboard and what
`git status` reports; this section duplicates them on purpose, so the profile
reads as one document.

{full}

## How the conversion works

LinkedIn accepts no formatting whatsoever — no bold, no italics, no links, no
headings. The Markdown sources keep all of it, because the same text renders to
PDF, HTML, DOCX and RTF where emphasis carries meaning. Pandoc's `plain` writer
does the stripping: emphasis markers are removed, reference links collapse to
their visible text, URLs and link definitions are dropped, and Unicode
punctuation (em dashes, curly quotes) is preserved. Markdown bullets become
`{bullet}`, which LinkedIn renders as pasted. Each paragraph is left on a single
long line — LinkedIn reflows text itself, and a hard-wrapped paste renders as a
column of ragged short lines.

**Emphasis is lost, not faked.** Pasting Unicode look-alike bold (𝗹𝗶𝗸𝗲 𝘁𝗵𝗶𝘀) is
a common trick and is deliberately not used here: screen readers announce those
code points as gibberish or skip them, and LinkedIn's own search and third-party
resume parsers do not match them as words. The bolded terms in the resume are
exactly the keywords worth being found by, so they are emitted as plain text
that indexes correctly.

## Adding a block

Wrap a section of a document in `markdown/` and rebuild:

```markdown
<!-- linkedin: headline limit=220 title="Headline" -->
Text that LinkedIn will receive.
<!-- linkedin: end -->
```

`limit` is required, `title` optional. The slug names the output file and must
be unique across all sources. Removing a marker deletes its file on the next
build — this directory holds nothing that is not generated.
""",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("sources", nargs="+", type=Path, help="Markdown files to scan")
    parser.add_argument("--out-dir", required=True, type=Path, help="directory to write")
    parser.add_argument("--bullet", default="•", help="bullet character (default: •)")
    args = parser.parse_args()

    try:
        blocks: list[dict] = []
        for source in args.sources:
            blocks.extend(extract_blocks(source))

        seen: dict[str, dict] = {}
        for block in blocks:
            prior = seen.get(block["slug"])
            if prior is not None:
                raise BlockError(
                    f"duplicate block '{block['slug']}': defined in both "
                    f"{origin(prior['source'])} and {origin(block['source'])}. "
                    f"One LinkedIn field "
                    f"cannot be fed by two documents — rename one, or mark only "
                    f"the document that mirrors the profile."
                )
            seen[block["slug"]] = block

        results = []
        for block in blocks:
            text = to_plain_text(block, args.bullet)
            results.append({**block, "text": text, "chars": len(text.rstrip("\n"))})
    except BlockError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if not results:
        print("    no <!-- linkedin: --> blocks found in any source")
        return 0

    args.out_dir.mkdir(parents=True, exist_ok=True)

    over = [r for r in results if r["chars"] > r["limit"]]
    for r in results:
        args.out_dir.joinpath(f"{r['slug']}.txt").write_text(r["text"], encoding="utf-8")
        status = "OVER" if r["chars"] > r["limit"] else "ok  "
        print(
            f"    {status} {r['slug'] + '.txt':38s} "
            f"{r['chars']:5d} / {r['limit']:5d}  "
            f"({r['limit'] - r['chars']:+d})"
        )

    # This directory is generated in full, so a file with no block behind it is
    # a block that was renamed or removed. Leaving it would keep publishing text
    # the resume no longer contains.
    #
    # paste-state.json is the exception: it is written by the publish workflow,
    # not by this build, and records which blocks have actually reached the
    # LinkedIn profile. Pruning it would silently reset that record on every
    # build and report the whole profile as needing a re-paste.
    keep = {f"{r['slug']}.txt" for r in results} | {"README.md", "paste-state.json"}
    for stale in sorted(args.out_dir.iterdir()):
        if stale.is_file() and stale.name not in keep:
            stale.unlink()
            print(f"    removed stale {stale.name}")

    write_index(args.out_dir, results, args.bullet)

    if over:
        print(file=sys.stderr)
        for r in over:
            print(
                f"error: {r['slug']} is {r['chars'] - r['limit']} characters over the "
                f"{r['limit']} LinkedIn allows — in {locate(r)}",
                file=sys.stderr,
            )
        print(
            "       LinkedIn truncates silently on paste. Shorten the marked "
            "section in the\n       Markdown source rather than raising the limit.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
