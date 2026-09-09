# Manual installer downloads

Fallbacks for when a package manager cannot install a tool, or the installer must be run interactively. Prefer the OS scripts in this folder; use this page only when they fail.

All of these are free. The build has no paid dependency.

## Required

- **Pandoc** — https://github.com/jgm/pandoc/releases (static binaries for every platform; extract and put on `PATH`)
- **ConTeXt / TeX** — https://www.contextgarden.net/download, or TeX Live as the fallback: https://tug.org/texlive/
- **Git** — https://git-scm.com/downloads

On Linux, prefer the distribution packages; a hand-installed TeX Live alongside a packaged one causes `mtxrun` path conflicts that are tedious to unpick.

## Package managers

- Homebrew (macOS): https://brew.sh/
- winget (Windows): https://learn.microsoft.com/windows/package-manager/winget/
- Chocolatey (Windows): https://chocolatey.org/install

Arch and its derivatives, including Omarchy, need nothing extra — `pacman` covers the whole toolchain. See `linux/install-prereqs.sh` for the exact package names.

## Verification

Reopen the terminal after any manual installer, then:

```bash
script/bootstrap.sh --check
```

That checks `git`, `pandoc` and `mtxrun` and reports what is missing. If `mtxrun` is present but ConTeXt still fails, run `mtxrun --generate` once to build the file database.

Finish with a real render, which is the only check that proves the toolchain works end to end:

```bash
script/pandoc_resume.sh all
```
