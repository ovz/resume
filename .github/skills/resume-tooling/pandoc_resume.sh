#!/usr/bin/env bash
# Build the resume artifacts (html, pdf, docx, rtf) from markdown/*.md.
#
# Drives pandoc directly rather than the pandoc_resume submodule's Makefile: the
# upstream Makefile hardcodes its pandoc invocations, which leaves no way to set
# --resource-path or --embed-resources, and without those the portrait PNG is
# silently dropped from every artifact. The submodule is used for its style
# assets only, so it stays on upstream master and remains trivial to re-merge.
#
# This file is the skill's own copy of the logic, not a pointer to one
# elsewhere: dropped into another repo with the same markdown/pandoc_resume
# conventions, this skill directory works unmodified. `script/pandoc_resume.sh`
# in this repo is a thin launcher onto it, kept only because that is the
# discoverable path a person or agent finds without reading docs.
set -Eeuo pipefail

tooling_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${tooling_dir}/../../.." && pwd)"
pandoc_dir="${repo_root}/pandoc_resume"
markdown_dir="${repo_root}/markdown"
styles_dir="${pandoc_dir}/styles"
lua_filter="${pandoc_dir}/pdc-links-target-blank.lua"
out_dir="${pandoc_dir}/output"
style="${RESUME_STYLE:-chmduquesne}"

die() { printf 'error: %s\n' "$*" >&2; exit 1; }
note() { printf '==> %s\n' "$*"; }

require_sources() {
  [ -d "${markdown_dir}" ] || die "no markdown directory at ${markdown_dir}"
  compgen -G "${markdown_dir}/*.md" >/dev/null || die "no .md sources in ${markdown_dir}"
}

require_submodule() {
  [ -f "${styles_dir}/${style}.tex" ] && [ -f "${styles_dir}/${style}.css" ] && return 0
  die "pandoc_resume submodule is not checked out (missing ${styles_dir}/${style}.*).
     Run: script/bootstrap.sh   (or: git submodule update --init --recursive)"
}

require_pandoc() {
  command -v pandoc >/dev/null 2>&1 ||
    die "pandoc not found. Run script/bootstrap.sh to install the toolchain."
}

# Arch's texlive-context ships the runner as `mtxrun.lua` and creates no
# `mtxrun` symlink, while TeX Live's own installer and most distros ship it as
# plain `mtxrun`. Resolve whichever exists rather than assuming either.
mtxrun_bin=""
require_context() {
  local candidate
  for candidate in mtxrun mtxrun.lua; do
    if command -v "${candidate}" >/dev/null 2>&1; then
      mtxrun_bin="${candidate}"
      return 0
    fi
  done
  die "mtxrun (ConTeXt) not found; it is required for PDF output.
     Run script/bootstrap.sh to install the toolchain."
}

# ConTeXt's Lua resolver reads its own texmfcnf.lua, which is separate from
# kpathsea's texmf.cnf and is NOT fixed by having a correct texmf.cnf. Arch's
# texlive-context ships TeX Live's file unpatched, where
#   local distribution_path = "selfautoparent:texmf-dist"
# assumes the TeX Live layout of <root>/bin/<arch>/mtxrun. Arch installs the
# runner at /usr/bin, so selfautoparent is "/" and ConTeXt hunts for
# /texmf-dist, finds no tree, and dies with the badly misleading
#   mtxrun | unknown script 'context.lua' or 'mtx-context.lua'
# Correct the path in a generated copy and point TEXMFCNF at it. Editing the
# original is not an option: it is owned by pacman and any texlive upgrade
# would silently revert the fix.
setup_context_config() {
  [ -n "${TEXMFCNF:-}" ] && return 0          # respect an explicit override

  local bin_path prefix system_cnf generated_dir
  bin_path="$(command -v "${mtxrun_bin}")" || return 0
  prefix="$(cd "$(dirname "${bin_path}")/.." && pwd)"
  system_cnf="${prefix}/share/texmf-dist/web2c/texmfcnf.lua"

  [ -f "${system_cnf}" ] || return 0
  grep -q 'selfautoparent:texmf-dist' "${system_cnf}" || return 0
  # Only a layout where the broken path really is broken needs the fix.
  [ -d "/texmf-dist" ] && return 0
  [ -d "${prefix}/share/texmf-dist" ] || return 0

  note "patching ConTeXt tree resolution (distribution path is unusable as shipped)"
  generated_dir="${out_dir}/.texmf-config"
  mkdir -p "${generated_dir}"
  sed -e 's|^local distribution_path = "selfautoparent:texmf-dist"|local distribution_path = "selfautodir:/share/texmf-dist"|' \
      -e 's|^local system_data = "selfautoparent:../texmf-local"|local system_data = "selfautodir:/share/texmf-local"|' \
      "${system_cnf}" > "${generated_dir}/texmfcnf.lua"
  export TEXMFCNF="${generated_dir}"
}

# Common pandoc flags. --resource-path lets pandoc resolve the `assets/...`
# image links, which are written relative to the markdown source rather than
# to this script's working directory.
pandoc_common=(--standalone --resource-path="${markdown_dir}" --from markdown)

# AGENTS.md is agent instructions, not an outward-facing document: it lives here
# because the rules are scoped to this directory, but it is not a resume source
# and must never be rendered into an artifact.
sources() {
  find "${markdown_dir}" -maxdepth 1 -name '*.md' ! -name 'AGENTS.md' -print0 | sort -z
}

build_html() {
  note "html"
  while IFS= read -r -d '' src; do
    name="$(basename "${src}" .md)"
    pandoc "${pandoc_common[@]}" --to html \
      --embed-resources \
      --include-in-header "${styles_dir}/${style}.css" \
      --lua-filter "${lua_filter}" \
      --metadata "pagetitle=${name}" \
      --output "${out_dir}/${name}.html" "${src}"
    printf '    %s.html\n' "${name}"
  done < <(sources)
}

build_docx() {
  note "docx"
  while IFS= read -r -d '' src; do
    name="$(basename "${src}" .md)"
    pandoc "${pandoc_common[@]}" --to docx \
      --output "${out_dir}/${name}.docx" "${src}"
    printf '    %s.docx\n' "${name}"
  done < <(sources)
}

build_rtf() {
  note "rtf"
  while IFS= read -r -d '' src; do
    name="$(basename "${src}" .md)"
    pandoc "${pandoc_common[@]}" --to rtf \
      --output "${out_dir}/${name}.rtf" "${src}"
    printf '    %s.rtf\n' "${name}"
  done < <(sources)
}

build_pdf() {
  note "pdf"
  # ConTeXt resolves \externalfigure paths relative to its working directory, so
  # the assets tree is staged next to the generated .tex files.
  if [ -d "${markdown_dir}/assets" ]; then
    mkdir -p "${out_dir}/assets"
    cp -f "${markdown_dir}"/assets/* "${out_dir}/assets/"
  fi

  while IFS= read -r -d '' src; do
    name="$(basename "${src}" .md)"
    pandoc "${pandoc_common[@]}" --to context \
      --template "${styles_dir}/${style}.tex" \
      --variable papersize=A4 \
      --output "${out_dir}/${name}.tex" "${src}"

    ( cd "${out_dir}" && run_context "${name}" ) ||
      die "ConTeXt failed for ${name}; see ${out_dir}/context_${name}.log"
    printf '    %s.pdf\n' "${name}"
  done < <(sources)
}

# ConTeXt on a fresh TeX Live install often has no generated file database yet,
# which surfaces as "cannot find context.lua". `mtxrun --generate` is the
# documented fix, so retry once through it before giving up.
run_context() {
  local name="$1" log="context_$1.log"
  if "${mtxrun_bin}" --script context --nonstopmode --result="${name}.pdf" "${name}.tex" >"${log}" 2>&1; then
    return 0
  fi
  note "ConTeXt run failed; regenerating the file database and retrying"
  "${mtxrun_bin}" --generate >>"${log}" 2>&1 || true
  "${mtxrun_bin}" --script context --nonstopmode --result="${name}.pdf" "${name}.tex" >>"${log}" 2>&1
}

# The portrait PNG is the artifact most likely to go missing, because every
# output format embeds it by a different mechanism. Fail loudly if any format
# rendered without it.
verify() {
  note "verify (embedded image in every artifact)"
  local failed=0 found

  while IFS= read -r -d '' src; do
    name="$(basename "${src}" .md)"
    grep -q '!\[' "${src}" || continue

    for ext in html pdf docx rtf; do
      local f="${out_dir}/${name}.${ext}"
      if [ ! -f "${f}" ]; then
        printf '    MISSING  %s.%s\n' "${name}" "${ext}"; failed=1; continue
      fi
      case "${ext}" in
        html) found=$(grep -c 'data:image/png;base64' "${f}" || true) ;;
        rtf)  found=$(grep -ac 'pngblip' "${f}" || true) ;;
        pdf)  found=$(grep -ac '/Image' "${f}" || true) ;;
        docx) found=$(python3 -c "
import sys, zipfile
z = zipfile.ZipFile(sys.argv[1])
print(sum(1 for n in z.namelist() if n.startswith('word/media/')))
" "${f}") ;;
      esac
      if [ "${found}" -gt 0 ]; then
        printf '    ok       %s.%s (image embedded)\n' "${name}" "${ext}"
      else
        printf '    NO IMAGE %s.%s\n' "${name}" "${ext}"; failed=1
      fi
    done
  done < <(sources)

  [ "${failed}" -eq 0 ] || die "one or more artifacts are missing the portrait image"
  note "all artifacts contain the portrait image"
}

clean() {
  note "clean"
  rm -rf "${out_dir}"
}

target="${1:-all}"
case "${target}" in
  clean) clean; exit 0 ;;
  html|docx|rtf|pdf|all|verify) ;;
  *) die "Usage: script/pandoc_resume.sh [all|html|pdf|docx|rtf|verify|clean]" ;;
esac

require_sources
require_submodule
require_pandoc
mkdir -p "${out_dir}"
if [ "${target}" = "pdf" ] || [ "${target}" = "all" ]; then
  require_context
  setup_context_config
fi

case "${target}" in
  html) build_html ;;
  docx) build_docx ;;
  rtf)  build_rtf ;;
  pdf)  build_pdf ;;
  verify) verify ;;
  all)
    build_html
    build_pdf
    build_docx
    build_rtf
    verify
    ;;
esac

note "output in ${out_dir}"
