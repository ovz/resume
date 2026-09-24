> Shard of the root [`AGENTS.md`](../../AGENTS.md). Load when the task matches its title.

# Building

```bash
script/bootstrap.sh              # fresh machine: submodule + toolchain + first build
script/pandoc_resume.sh all      # html, pdf, docx, rtf, linkedin, then verify
script/pandoc_resume.sh linkedin # regenerate the LinkedIn copy-paste blocks
script/pandoc_resume.sh verify   # assert the portrait PNG is embedded in every artifact
script/pandoc_resume.sh clean
```

Artifacts land in `pandoc_resume/output/` and are gitignored, as are `*.pdf` and `*.htm*` repo-wide. The build must never be "fixed" by committing generated output.

Pasting the result into the profile is [its own workflow](../../llm-wiki/wiki/workflows/linkedin-publish.md), on its own clock: resume edits are committed as they go, and `script/linkedin-sync.py status` / `round` **regenerate the blocks from the Markdown themselves** before saying what has not reached LinkedIn. The paste record is committed so it survives a commit and a fresh clone; a non-zero `status` is a low-priority owner item in the tracker, never a blocker. **There is no API for it** — the write path exists but is behind a closed partner permission, and browser automation is prohibited; the workflow page carries the evidence.

**`linkedin/` is the one tracked exception**, and it is tracked *because* it is generated. LinkedIn accepts no formatting and caps each field — 2,600 characters for the About section, 2,000 per Experience entry — so the profile cannot be a copy of the resume; it is a rendering of it, produced from sections marked `<!-- linkedin: <slug> limit=<n> -->` in the Markdown. Updating the profile is a human pasting into a web form, so the committed diff is the only thing that can say *which* fields have drifted and need re-pasting: a changed file is a field to paste, an unchanged one is a field to leave alone. Files there are never hand-edited, and a block that outgrows its field fails the build rather than being silently truncated on paste. Details: [`.github/skills/resume-tooling/SKILL.md`](../../.github/skills/resume-tooling/SKILL.md) § *The LinkedIn export*.

Every artifact is expected to embed the portrait image from `markdown/assets/`. Each output format embeds it by a different mechanism, so it fails silently and per-format; `script/pandoc_resume.sh verify` is the check that catches it. Treat a `NO IMAGE` line from `verify` as a build failure.
