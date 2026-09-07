# Resume Brag File — drop and ingest

> **Doc type:** how-to
>
> Casual, regular capture of anything the owner thinks might belong in the resume someday, plus the periodic pass that folds those captures into the wiki. Deliberately separate from [updating the outward-facing resume](../resume/update-workflow.md). Audience: the owner (dropping) and any agent (dropping on the owner's behalf, or ingesting).

## The idea

A brag file is a low-friction note written *when the thing happens*, while the detail is fresh — not a polished resume line. It goes under `raw/` because it is source material: dated by the accomplishment, cited later. Unlike the rest of `raw/`, brag entries are **living records**: one file per accomplishment, edited or appended as new evidence turns up, with every change day logged at the bottom of the file. The wiki knows about brag entries, orients them by domain in [accomplishments by domain](../concepts/accomplishments-by-domain.md), and leaves the decision of what reaches the resume to a separate, deliberate pass.

## Part 1 — Drop an entry

**Where:** `llm-wiki/raw/brag/YYYY-MM-DD-<slug>.md` — one file per accomplishment, date first, short kebab-case slug (`2026-09-06-positioning-upgrade-shipped.md`).

**The date is the accomplishment's date, never the day the file was written.** Use the evidence date (the email, note, demo, or release that proves it happened). For work spanning a range, put the full range on the `date:` line and use one end of it in the filename; the ledger and the record history carry the capture date.

**Before writing, check for an existing entry on the same accomplishment** (`ls raw/brag/`, then the [brag ledger](../sources/brag-ledger.md)). Same accomplishment — same outcome, same evidence trail, overlapping dates — means *augment* the existing file (Part 1b), not a second file. A later, distinct event in the same programme (a validation a year after a launch, a follow-up presentation) is a new entry that links back to the earlier one by filename.

**Template** (copy, fill what you know, leave the rest — a partial entry beats no entry):

```markdown
# <One-line headline of the accomplishment>

- date: YYYY-MM-DD (or range)
- context: <employer / project / team, as publicly describable>
- domains: <one or more from accomplishments-by-domain.md, e.g. positioning, observability>
- sensitivity: public-friendly | private-repo
- resume-worthy: yes | maybe | no

## What I did

<what happened, in the owner's words>

## Why it matters

<outcome, scale, who benefited, what it unblocked; numbers if they are publishable>

## Skills demonstrated

<technologies, practices, leadership behaviours>

## Evidence

<generic description only — "post-mortem doc", "PR review thread", "customer email". Never a path under __untracked_stuff/ or an internal URL.>

## Record history

- YYYY-MM-DD: created
```

**Rules:**

1. Apply the tier tag honestly — see [sensitivity tiers](sensitivity-tiers.md). If the entry cannot be written at `private-repo` level without losing its point, it is T2: write the raw version in the maintainer scope's `raw/` (never committed) and drop a `private-repo`-safe abstract here instead. Naming colleagues and collaborators is fine at `private-repo` (this is the owner's professional record); use a role instead only where a grounded reason applies — NDA-covered partner, unannounced partnership, or a person who asked not to be named.
2. Every entry ends with a **`## Record history`** section: one line per calendar day the file was created or changed, `- YYYY-MM-DD: <what changed>`. It sits last so it is easy to append. These are the only dates in the file that describe the record rather than the accomplishment.
3. Do not edit the primary resume, `accomplishments-by-domain.md`, or any wiki page as part of a drop. Dropping is capture only.
4. No index update is required at drop time. "Not yet ingested" is defined as *present in `raw/brag/`, absent from [brag-ledger.md](../sources/brag-ledger.md)*.

An agent asked to "add this to my brag file" does exactly the above: checks for an existing entry, writes or augments the file, confirms the path, stops.

### Part 1b — Augment an existing entry

Edits and appends are both normal. When new evidence, a correction, or a related later event arrives for an accomplishment that already has a file:

1. Edit the section(s) concerned in place, or append a new dated sub-section (`### Follow-up, YYYY-MM-DD`) when the addition is a distinct later event worth its own paragraph. Keep the headline and `date:` line true to the original accomplishment; widen the `date:` range only if the accomplishment itself continued.
2. Cross-link related entries by filename in both directions.
3. Append a `## Record history` line for the day: what changed and, briefly, why (`- 2026-09-07: added forward link to 2025-05-29 validation entry`).
4. If the entry is already in the ledger and the change alters its headline, domains, or `resume-worthy` value, re-run the ingest steps for it (Part 2) so [accomplishments by domain](../concepts/accomplishments-by-domain.md) and the ledger row stay current; note the re-ingest in the ledger's *Ingested* column (`2026-09-07; re-ingested 2026-09-20`).

## Part 2 — Ingest entries (periodic)

Run when the owner asks, or when un-ingested entries accumulate (a handful is a good trigger).

1. List un-ingested entries: files in `raw/brag/` not present in [brag-ledger.md](../sources/brag-ledger.md). Also list ledger rows whose entry's latest *Record history* date is newer than the row's *Ingested* date — those need a re-ingest.
2. Read each entry fully. Check the tier tag against the content; if the content exceeds its tag, stop and ask the owner before proceeding. Check that the filename date and `date:` line describe the accomplishment, not the capture; fix the `date:` line (with a record-history note) if they do not. Check for two entries describing the same accomplishment; if found, merge into the earlier file per Part 1b and leave a one-line stub in the later file pointing at the survivor until the owner deletes it.
3. Update [accomplishments by domain](../concepts/accomplishments-by-domain.md): add or strengthen the headline bullet(s) under each listed domain, citing the entry file with a relative link. Keep the page's per-domain shape; do not paste the entry.
4. If the entry names a new employer, product, or role, update [organizations](../entities/organizations.md); if it evidences a new recurring capability, update [technical themes](../concepts/technical-themes.md) or [skills matrix](../concepts/skills-matrix.md).
5. Append a row to [brag-ledger.md](../sources/brag-ledger.md): entry file, ingest date, pages touched, `resume-worthy` value, promotion status `not promoted`.
6. Update [`index.md`](../../index.md) only if a new wiki page was created.
7. Record the pass in the maintainer's operations log (outside version control).

**Never** modify the primary resume during ingest. If an entry is clearly resume-worthy, say so in the ledger row; the owner triggers [update-workflow.md](../resume/update-workflow.md) separately.

## Part 3 — Promote to the resume (separate workflow)

Handled entirely by [update the outward-facing resume](../resume/update-workflow.md). When a promotion lands, that workflow sets the ledger row's promotion status to `promoted <date>`.

## Related

- [Accomplishments by domain](../concepts/accomplishments-by-domain.md) — the landing page for ingested entries.
- [Brag ledger](../sources/brag-ledger.md) — ingest and promotion state.
- [Sensitivity tiers](sensitivity-tiers.md) — the tag definitions.
