# Resume repository — agent instructions

Personal resume repository for Oleg Zhylin. Markdown sources in `markdown/` are rendered by Pandoc into HTML, PDF, DOCX and RTF. `llm-wiki/` is the maintained knowledge layer behind the resume. This file is the router; the load-bearing rules live in the per-directory `AGENTS.md` files listed below.

## Agents do not commit

**Never run `git commit`, `git push`, `git tag`, or any other history-writing command.** Every change in this repository is reviewed by a human before it lands. This holds without exception, including for changes an agent is confident about and changes the owner appeared to pre-approve in conversation.

What an agent does instead:

1. Leave the work in the working tree, unstaged or staged, and say what changed and why.
2. Write the **proposed commit message** into the session-wiki scratch scope, never into a tracked file and never into the repo. The `session-wiki-pattern` skill owns that scope's layout; commit messages belong alongside its other session artifacts, under a `commits/` directory in the session-wiki. One file per proposed commit, each naming the exact paths it covers.
3. Hand off: point the owner at the changed paths and at the prepared message. The owner reviews, edits the message if needed, and commits.

`git status`, `git diff`, `git log`, `git show` and other read-only inspection are always fine. So is `git stash` when protecting uncommitted work from a destructive operation.

## Where the rules live

Per-directory `AGENTS.md` files are the primary, load-bearing instructions. Read the one covering the directory you are about to touch; do not rely on this router alone.

| Directory | File | Covers |
|---|---|---|
| `markdown/` | [`markdown/AGENTS.md`](markdown/AGENTS.md) | Editing the outward-facing resume and references documents |
| `llm-wiki/` | [`llm-wiki/AGENTS.md`](llm-wiki/AGENTS.md) | The knowledge layer: schema, sensitivity tiers, ingest and synthesis workflows |
| `.github/` | [`.github/AGENTS.md`](.github/AGENTS.md) | How this repo's agent customizations are laid out and kept discoverable |

`pandoc_resume/` is a git submodule tracking a fork of `mszep/pandoc_resume`. It supplies the ConTeXt and CSS style assets only. **Do not edit files inside it** — changes there belong upstream in the fork, and local edits break the build's re-merge story.

## Building

```bash
script/bootstrap.sh              # fresh machine: submodule + toolchain + first build
script/pandoc_resume.sh all      # html, pdf, docx, rtf, then verify
script/pandoc_resume.sh verify   # assert the portrait PNG is embedded in every artifact
script/pandoc_resume.sh clean
```

Artifacts land in `pandoc_resume/output/` and are gitignored, as are `*.pdf` and `*.htm*` repo-wide. The build must never be "fixed" by committing generated output.

Every artifact is expected to embed the portrait image from `markdown/assets/`. Each output format embeds it by a different mechanism, so it fails silently and per-format; `script/pandoc_resume.sh verify` is the check that catches it. Treat a `NO IMAGE` line from `verify` as a build failure.

## Sensitivity

Three tiers govern what may be written where: **T0 public** (the primary resume only), **T1 private repo** (everything else committed), **T2 never committed** (employer-internal material, large binaries). Definitions and promotion rules: [`llm-wiki/wiki/workflows/sensitivity-tiers.md`](llm-wiki/wiki/workflows/sensitivity-tiers.md).

Two hard rules apply everywhere:

- No committed file may reference a path under `__untracked_stuff/`. A committed file must stand alone in a fresh clone; a pointer into scratch is dead on arrival for every other reader, and dead *silently*. Describe the shape of the scratch convention if you must, but never a concrete scratch path.
- Third-party contact details are never copied out of `markdown/Oleg.Zhylin.professional.references.md`.

## Skills

Reusable procedures live in `.github/skills/<name>/SKILL.md`, the single copy of each. Load one when its `description` matches the task:

- `resume-editing` — editing an outward-facing resume document.
- `resume-tooling` — setting up or repairing the toolchain on a workstation.
- `pdf-extraction` — ingesting a PDF into a wiki.
- `session-wiki-pattern` — planning or maintaining a long, multi-step assignment.

Not every agent scans `.github/skills/` on its own — Claude Code, for one, only scans `.claude/skills/`. Where a tool needs a different path, this repo adds a symlink back to the real folder rather than a second copy; see [`.github/AGENTS.md`](.github/AGENTS.md) § *The two bridges Claude Code needs* for the current list.

See [`.github/AGENTS.md`](.github/AGENTS.md) for the full customization map and the conventions each file type must follow.

## Reading this file with Claude Code

Claude Code reads `CLAUDE.md`, not `AGENTS.md`, so it never sees this router — or any nested `AGENTS.md` — on its own. The root [`CLAUDE.md`](CLAUDE.md) and a `CLAUDE.md` in every directory listed above import the local `AGENTS.md` via `@AGENTS.md`, which is how the content actually reaches Claude Code. Do not rely on that import from inside this file or any other `AGENTS.md` — they must stay literal, tool-agnostic Markdown for every other reader.
