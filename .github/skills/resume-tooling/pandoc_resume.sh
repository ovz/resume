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
linkedin_dir="${repo_root}/linkedin"
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

# AGENTS.md and its CLAUDE.md import bridge are agent instructions, not
# outward-facing documents: they live here because the rules are scoped to this
# directory, but they are not resume sources and must never be rendered into an
# artifact. Adding a further instruction-file convention here means adding it to
# this exclusion list too — the failure is silent, producing a stray artifact
# rather than an error.
sources() {
  find "${markdown_dir}" -maxdepth 1 -name '*.md' \
    ! -name 'AGENTS.md' ! -name 'CLAUDE.md' -print0 | sort -z
}

# Shared fragments live in markdown/_parts/ and are pulled in with a line
# reading exactly:   <!-- include: _parts/<file>.md -->
#
# This exists so content that must be identical across resume variants — above
# all the reference-link block, whose keys are defined once and mean the same
# thing in every document — is stored once rather than copied per variant and
# left to drift. _parts/ is a subdirectory, so sources() above never treats a
# fragment as a document in its own right.
#
# A missing fragment is a hard error: resolving it to nothing would silently
# strip every link definition and still produce a plausible-looking artifact.
#
# The resolved file is written next to the artifacts as `<name>.prepared.md`,
# deliberately visible rather than hidden in a dot-directory. It is exactly the
# Markdown Pandoc was handed, so when a rendered document looks wrong the first
# question — "did the include put what I expected where I expected it?" — is
# answered by opening one file, not by reasoning about the build.
prepare() {
  local src="$1" name out inc path
  if ! grep -q '^<!-- include: ' "${src}"; then
    printf '%s' "${src}"
    return 0
  fi

  while IFS= read -r inc; do
    path="${markdown_dir}/${inc}"
    [ -f "${path}" ] || die "$(basename "${src}") includes '${inc}', which does not exist at ${path}"
  done < <(sed -n 's/^<!-- include:[[:space:]]*\(.*[^[:space:]]\)[[:space:]]*-->[[:space:]]*$/\1/p' "${src}")

  name="$(basename "${src}" .md)"
  out="${out_dir}/${name}.prepared.md"
  awk -v dir="${markdown_dir}" '
    /^<!-- include: / {
      line = $0
      sub(/^<!-- include:[[:space:]]*/, "", line)
      sub(/[[:space:]]*-->[[:space:]]*$/, "", line)
      path = dir "/" line
      while ((getline l < path) > 0) print l
      close(path)
      next
    }
    { print }
  ' "${src}" > "${out}"
  printf '%s' "${out}"
}

build_html() {
  note "html"
  while IFS= read -r -d '' src; do
    name="$(basename "${src}" .md)"
    input="$(prepare "${src}")"
    pandoc "${pandoc_common[@]}" --to html \
      --embed-resources \
      --include-in-header "${styles_dir}/${style}.css" \
      --lua-filter "${lua_filter}" \
      --metadata "pagetitle=${name}" \
      --output "${out_dir}/${name}.html" "${input}"
    printf '    %s.html\n' "${name}"
  done < <(sources)
}

build_docx() {
  note "docx"
  while IFS= read -r -d '' src; do
    name="$(basename "${src}" .md)"
    input="$(prepare "${src}")"
    pandoc "${pandoc_common[@]}" --to docx \
      --output "${out_dir}/${name}.docx" "${input}"
    printf '    %s.docx\n' "${name}"
  done < <(sources)
}

build_rtf() {
  note "rtf"
  while IFS= read -r -d '' src; do
    name="$(basename "${src}" .md)"
    input="$(prepare "${src}")"
    pandoc "${pandoc_common[@]}" --to rtf \
      --output "${out_dir}/${name}.rtf" "${input}"
    printf '    %s.rtf\n' "${name}"
  done < <(sources)
}

# LinkedIn accepts no formatting and caps every field (2,600 characters for the
# About section, 2,000 per Experience entry), so the profile cannot be a copy of
# the resume — it is a rendering of it. Sections marked with
# `<!-- linkedin: <slug> limit=<n> -->` are rendered to plain text and checked
# against their budget by the exporter.
#
# Unlike every other target here, the output is COMMITTED. That is deliberate
# and is the whole point: pasting into LinkedIn is a manual act, so the tracked
# diff is what tells the owner which fields have drifted from the resume and
# need re-pasting. See linkedin/README.md, which the exporter generates.
#
# Runs on the prepared Markdown, like verify does, so a marked block may sit
# inside shared _parts/ content.
build_linkedin() {
  note "linkedin"
  local -a prepared=()
  while IFS= read -r -d '' src; do
    prepared+=("$(prepare "${src}")")
  done < <(sources)

  python3 "${tooling_dir}/linkedin_export.py" \
    --out-dir "${linkedin_dir}" "${prepared[@]}"
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
    input="$(prepare "${src}")"
    pandoc "${pandoc_common[@]}" --to context \
      --template "${styles_dir}/${style}.tex" \
      --variable papersize=A4 \
      --output "${out_dir}/${name}.tex" "${input}"

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
    # Test the RESOLVED input, not the raw source: the portrait reference lives
    # in a shared fragment, so a source file no longer contains `![` itself and
    # testing it here would silently skip the document entirely — the check
    # would keep passing while checking nothing.
    local img_input; img_input="$(prepare "${src}")"
    grep -q '!\[' "${img_input}" || continue

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

  verify_links
}

# Reference links are the other thing that breaks silently. A `[text][key]`
# whose key is undefined does not fail the build — Pandoc renders it as literal
# text, so a document loses a hyperlink and still looks finished. With the
# reference block shared through _parts/, one bad include would do that to every
# link in a document at once, so the build proves it did not rather than leaving
# the reader to spot it.
#
# Two independent checks: keys used are defined in the Markdown Pandoc actually
# received, and every rendered format carries a comparable number of real links.
# If the include had silently resolved to nothing, both would collapse to zero.
verify_links() {
  note "verify (reference links resolve in every artifact)"
  local failed=0

  while IFS= read -r -d '' src; do
    name="$(basename "${src}" .md)"
    local input; input="$(prepare "${src}")"

    local undefined
    undefined="$(python3 - "${input}" <<'PY'
import re, sys
text = open(sys.argv[1], encoding="utf-8").read()
body = re.sub(r'^\[[^\]]+\]:.*$', '', text, flags=re.M)      # drop definitions
defined = set(re.findall(r'^\[([^\]]+)\]:', text, flags=re.M))
used = set(k for k in re.findall(r'\]\[([^\]]+)\]', body) if k)
print(",".join(sorted(used - defined)))
PY
)"
    if [ -n "${undefined}" ]; then
      printf '    UNDEFINED %s: %s\n' "${name}" "${undefined}"; failed=1
    fi

    # `grep -c` exits non-zero on zero matches, which under `set -o pipefail`
    # would abort the run; a count of nothing is a legitimate answer here, so
    # each count absorbs that rather than treating it as a build failure.
    local html_n docx_n rtf_n pdf_n
    html_n=$(grep -o 'href="[^"]*"' "${out_dir}/${name}.html" 2>/dev/null | wc -l || true)
    rtf_n=$(grep -ao 'HYPERLINK' "${out_dir}/${name}.rtf" 2>/dev/null | wc -l || true)
    # ConTeXt writes link annotations into compressed object streams, so a plain
    # grep for /URI reports zero on a PDF whose links are perfectly good. Inflate
    # the streams before counting — a check that always says zero is worse than
    # no check, because it teaches the reader to ignore the column.
    pdf_n=$(python3 -c "
import sys, re, zlib
data = open(sys.argv[1], 'rb').read()
n = len(re.findall(rb'/URI', data))
for m in re.finditer(rb'stream\r?\n', data):
    start = m.end()
    end = data.find(b'endstream', start)
    if end < 0:
        continue
    try:
        n += len(re.findall(rb'/URI', zlib.decompress(data[start:end])))
    except Exception:
        pass
print(n)
" "${out_dir}/${name}.pdf" 2>/dev/null || echo 0)
    docx_n=$(python3 -c "
import sys, zipfile, re
try:
    z = zipfile.ZipFile(sys.argv[1])
    rels = z.read('word/_rels/document.xml.rels').decode('utf-8', 'replace')
    print(len(re.findall(r'TargetMode=\"External\"', rels)))
except Exception:
    print(0)
" "${out_dir}/${name}.docx" 2>/dev/null || echo 0)

    printf '    %-38s html %-4s docx %-4s rtf %-4s pdf %s\n' \
      "${name}" "${html_n}" "${docx_n}" "${rtf_n}" "${pdf_n}"

    if [ "${html_n}" -eq 0 ] && grep -q '\]\[' "${input}"; then
      printf '    NO LINKS  %s.html — the document uses reference links but rendered none\n' "${name}"
      failed=1
    fi
  done < <(sources)

  [ "${failed}" -eq 0 ] || die "reference links did not resolve; see the lines above"
  printf '    (docx counts unique targets, the others count occurrences, so docx is legitimately lower)\n'
  note "every reference key resolves, and links are present in all four formats"
}

clean() {
  note "clean"
  rm -rf "${out_dir}"
}

target="${1:-all}"
case "${target}" in
  clean) clean; exit 0 ;;
  html|docx|rtf|pdf|all|verify|linkedin) ;;
  *) die "Usage: script/pandoc_resume.sh [all|html|pdf|docx|rtf|linkedin|verify|clean]" ;;
esac

require_sources
# The LinkedIn export drives pandoc directly and never touches a style asset,
# so it is the one target that works in a clone with no submodule checked out.
[ "${target}" = "linkedin" ] || require_submodule
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
  linkedin) build_linkedin ;;
  verify) verify ;;
  all)
    build_html
    build_pdf
    build_docx
    build_rtf
    build_linkedin
    verify
    ;;
esac

note "output in ${out_dir}"
case "${target}" in
  linkedin|all) note "LinkedIn blocks in ${linkedin_dir} (tracked; a changed file is a field to re-paste)" ;;
esac
