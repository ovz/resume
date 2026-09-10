# Resume Brag File — capture and ingest

> **Doc type:** how-to
>
> Low-friction capture of anything that might belong in the resume someday, plus the periodic pass that folds captures into the wiki. Deliberately separate from [updating the outward-facing resume](../resume/update-workflow.md). Audience: the owner (dropping) and any agent (dropping on the owner's behalf, or ingesting).

## The idea

A brag file is a note written *when the thing happens*, while the detail is fresh — not a polished resume line. It goes under `raw/` because it is source material: dated by the accomplishment, cited later. Unlike the rest of `raw/`, brag entries are **living records**: one file per accomplishment, edited or appended as new evidence turns up, with every change day logged at the bottom.

Two principles govern everything below.

**Never discard information.** Input arrives in whatever shape it arrives — an email thread, a chat export, a pull-request description, a planning note, a paragraph typed straight into a conversation, three differently-worded versions of the same story. None of that is trimmed to fit a template. It is preserved, then enriched.

**The committed entry is the durable record.** The verbatim capture (Part 0) lives in the session-wiki, which is gitignored and therefore transient — a laptop is not a backup. Anything that must outlive this machine has to reach the committed entry. That makes the entry's job *preservation*, not summary: it carries the technical substance, and the raw copy is only the audit trail for how it got there.

## Part 0 — Capture the input as-is

Before interpreting anything, write the input verbatim into the session-wiki's raw capture area:

```
__untracked_stuff/<scope>/session-wiki/raw/<YYYYMMDD>_brag-<slug>.<ext>
```

Rules:

1. **Verbatim.** No cleanup, no reformatting, no truncation. Keep the original's own structure — if the owner supplied three renderings of the same accomplishment, all three are the input.
2. **Record where it came from** at the top of the capture: source (email, chat, PR, note, dictated), the date received, and the date the *accomplishment* happened if they differ.
3. **Never edit it afterwards.** Corrections become a new capture, not an edit to an old one.
4. **This copy is transient.** It is the audit trail, not the archive. Do not treat it as the place technical detail is preserved — that is the entry's job.

An agent handed material in the middle of a conversation does this first, before deciding anything about tiers, duplicates, or wording.

## Part 1 — Write or update the committed entry

**Where:** `llm-wiki/raw/brag/YYYY-MM-DD-<slug>.md` — one file per accomplishment, date first, short kebab-case slug.

**The date is the accomplishment's date, never the day the file was written.** Use the evidence date. For work spanning a range, put the full range on the `date:` line and one end of it in the filename; the record history carries the capture date.

**Check for an existing entry first** (`ls raw/brag/`, then the [brag ledger](../sources/brag-ledger.md), then [coverage.md](../resume/coverage.md) for the thread it would join). Classify what you have — see *Part 1b*.

### Check the tier, and refine the policy when it resists

Brag input is normally written with the professional record in mind and contains nothing that cannot be committed. **Check anyway, every time**, against [sensitivity tiers](sensitivity-tiers.md): tag the entry `sensitivity: public-friendly` or `private-repo`, and confirm the content does not exceed its tag.

When a case does not resolve cleanly against the current policy — a new kind of artifact, an unclear customer reference, an ambiguity about a partner — that is a **signal the policy is incomplete, not a licence to make a silent one-off call**. Record the case, apply the most conservative reading for now, and propose the policy refinement to the owner. A tier rule that keeps needing judgement in the same spot should be rewritten so it does not.

If the entry cannot be written at `private-repo` level without losing its point, it is T2: the raw version stays in the maintainer's scratch and only a `private-repo`-safe abstract lands here.

### Preserve, don't summarize

The failure mode this workflow exists to prevent is an entry that reads well and has quietly thrown away everything that made the work verifiable. Concretely:

- **Keep technical specifics.** Mechanisms, file and schema shapes, algorithms and their variants, failure modes, thresholds, the actual reasoning. "Hardened error handling" preserves nothing; naming what was wrong, what was changed, and why it works does.
- **Keep the owner's own words** where they carry meaning. Rephrasing into house style loses the texture that makes a claim credible later.
- **Keep every rendering supplied.** If the input contains a performance-review version, a concise version and a resume-style version, keep all of them as their own sections. They are different compressions of the same fact and each is useful for a different downstream purpose.
- **Enrich over time.** Later evidence, outcomes, metrics and corrections get appended, not substituted.
- **Abstract only what the tier requires** — internal URLs, customer identities, unreleased plans. Abstraction is a sensitivity operation, never a brevity one.

`## Evidence` describes what exists and where it lives generically ("merged pull request", "internal design page", "email thread dated …"). It never carries an internal URL or a scratch path — but it should be specific enough that the owner could find the artifact again.

### Template

```markdown
# <One-line headline of the accomplishment>

- date: YYYY-MM-DD (or range)
- context: <employer / project / team, as publicly describable>
- domains: <one or more from accomplishments-by-domain.md>
- sensitivity: public-friendly | private-repo
- resume-worthy: yes | maybe | no

## What I did

<what happened, in the owner's words, with the technical substance intact>

## Why it matters

<outcome, scale, who benefited, what it unblocked; numbers if they are publishable>

## Skills demonstrated

<technologies, practices, leadership behaviours>

## Evidence

<what exists and roughly where — generic description only, no internal URLs or scratch paths>

## Related

<reciprocal links to other entries, each saying how they relate>

## Record history

- YYYY-MM-DD: created
```

Optional sections are welcome when the input supplies them: dated sub-sections for multi-episode work, `## Evidence limitations` where the source does not support a claim, and any alternate renderings the owner wrote.

**Dropping is capture only.** Do not edit the resume, `accomplishments-by-domain.md`, or any other wiki page during a drop. No index update is needed. An entry is *not yet ingested* while it is present in `raw/brag/` and absent from the ledger.

### Part 1b — Same accomplishment, new input

Three cases, distinguished by what the new input adds:

| Case | Test | What to do |
|---|---|---|
| **Duplicate** | Same accomplishment, same evidence trail, nothing new | Merge anything phrased better into the existing entry; do **not** create a second file. Log the merge in *Record history*. |
| **Update** | Same accomplishment, new evidence, outcome, metric or correction | Augment in place: edit the section concerned, or append `### Follow-up, YYYY-MM-DD` for a distinct later episode. Widen `date:` only if the accomplishment itself continued. |
| **Related** | A distinct accomplishment in the same programme | New entry. Add reciprocal `## Related` links naming the relationship, and put both in the same thread in [coverage.md](../resume/coverage.md). |

In all three cases append a `## Record history` line for the day, saying what changed and briefly why. If an updated entry is already in the ledger and the change alters its headline, domains, or `resume-worthy` value, re-run Part 2 for it and note the re-ingest in the ledger's *Ingested* column.

## Part 2 — Ingest (periodic)

Run when the owner asks, or when un-ingested entries accumulate — a handful is a good trigger.

1. **List what is pending.** Entries in `raw/brag/` with no ledger row, plus rows whose entry's latest *Record history* date is newer than the row's *Ingested* date.
2. **Read each entry fully.** Re-check the tier tag against the content. Check that the filename date and `date:` line describe the accomplishment rather than the capture. Check for a second entry describing the same accomplishment and merge per Part 1b.
3. **Look up the shards it touches.** Always [accomplishments by domain](../concepts/accomplishments-by-domain.md) — add or strengthen a headline bullet under each domain the entry lists, citing the entry file. Then, only where the entry genuinely adds something: [organizations](../entities/organizations.md) for a new employer, product or role; [technical themes](../concepts/technical-themes.md) or [skills matrix](../concepts/skills-matrix.md) for a newly evidenced capability. Record every page touched in the ledger row.
4. **Register it in the coverage map.** In [coverage.md](../resume/coverage.md): assign the entry to exactly one primary thread (cross-list it elsewhere without duplicating claims, or open a new thread if it starts one), then decompose it into claims — one promotable assertion each — and add them with status `absent`. Recompute the thread and headline figures.
5. **Append the ledger row:** entry file, ingest date, pages touched, `resume-worthy` value, promotion status `not promoted`.
6. **Update [`index.md`](../../index.md)** only if a new wiki page was created.
7. **Record the pass** in the maintainer's operations log, outside version control.

**Never modify the primary resume during ingest.** If an entry is clearly resume-worthy, say so in the ledger row and tell the owner; promotion is a separate pass.

## Part 3 — Promote to the resume

Handled by [update the outward-facing resume](../resume/update-workflow.md). When a promotion lands, that pass sets the ledger row's promotion status and flips the affected claims in [coverage.md](../resume/coverage.md) to `in` or `partial` in the same edit.

## Related

- [Coverage map](../resume/coverage.md) — threads, claims, and how much has reached the resume.
- [Accomplishments by domain](../concepts/accomplishments-by-domain.md) — the landing page for ingested entries.
- [Brag ledger](../sources/brag-ledger.md) — ingest and promotion state.
- [Sensitivity tiers](sensitivity-tiers.md) — the tag definitions and the policy this workflow refines.
