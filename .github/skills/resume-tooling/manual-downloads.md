# Manual installer downloads

Use these links when the package manager cannot install the tool automatically or when the required installer must be launched interactively.

## Required

- Git for Windows: https://git-scm.com/download/win
- Pandoc: https://github.com/jgm/pandoc/releases
- TeX/ConTeXt: https://www.contextgarden.net/download
- TeX Live (fallback): https://tug.org/texlive/

## Optional but useful

- winget: https://learn.microsoft.com/windows/package-manager/winget/
- Homebrew: https://brew.sh/
- Chocolatey: https://chocolatey.org/install

## Post-install verification

After every manual installer finishes, reopen the terminal and confirm:

```bash
git --version
pandoc --version
context --version
mtxrun --version
```

If `context` is still missing, install the ConTeXt/TeX bundle and add it to PATH before rerunning the project build.
