# LinkedIn copy-paste blocks

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
| [`about.txt`](about.txt) | About (My Story) | 2,336 | 2,600 | 264 | [`Oleg.Zhylin.resume.achievements.md`](../markdown/Oleg.Zhylin.resume.achievements.md) |
| [`experience-best-buy-health.txt`](experience-best-buy-health.txt) | Experience — Best Buy Health | 1,969 | 2,000 | 31 | [`Oleg.Zhylin.resume.achievements.md`](../markdown/Oleg.Zhylin.resume.achievements.md) |
| [`experience-minitab.txt`](experience-minitab.txt) | Experience — Minitab | 1,689 | 2,000 | 311 | [`Oleg.Zhylin.resume.achievements.md`](../markdown/Oleg.Zhylin.resume.achievements.md) |
| [`experience-salford-systems.txt`](experience-salford-systems.txt) | Experience — Salford Systems | 1,662 | 2,000 | 338 | [`Oleg.Zhylin.resume.achievements.md`](../markdown/Oleg.Zhylin.resume.achievements.md) |
| [`experience-iit.txt`](experience-iit.txt) | Experience — Institute of Information Technology | 1,122 | 2,000 | 878 | [`Oleg.Zhylin.resume.achievements.md`](../markdown/Oleg.Zhylin.resume.achievements.md) |

A build **fails** when a block exceeds its limit, so these files are always
within budget. Character counts include line breaks, which LinkedIn counts too.

## How the conversion works

LinkedIn accepts no formatting whatsoever — no bold, no italics, no links, no
headings. The Markdown sources keep all of it, because the same text renders to
PDF, HTML, DOCX and RTF where emphasis carries meaning. Pandoc's `plain` writer
does the stripping: emphasis markers are removed, reference links collapse to
their visible text, URLs and link definitions are dropped, and Unicode
punctuation (em dashes, curly quotes) is preserved. Markdown bullets become
`•`, which LinkedIn renders as pasted. Each paragraph is left on a single
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
