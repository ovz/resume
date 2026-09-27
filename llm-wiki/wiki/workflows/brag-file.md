# Resume Brag File — capture and ingest

Stewardship: strict · home: resume

> **Doc type:** how-to
>
> Low-friction capture of anything that might belong in the resume someday, plus the periodic pass that folds captures into the wiki. Deliberately separate from [updating the outward-facing resume](../resume/update-workflow.md). Audience: the owner (dropping) and any agent (dropping on the owner's behalf, or ingesting).

## The idea

A brag file is a note written *when the thing happens*, while the detail is fresh — not a polished resume line. It goes under `raw/` because it is source material: dated by the accomplishment, cited later. Unlike the rest of `raw/`, brag entries are **living records**: one file per accomplishment, edited or appended as new evidence turns up, with every change day logged at the bottom.

Two principles govern everything below.

**Never discard information.** Input arrives in whatever shape it arrives — an email thread, a chat export, a pull-request description, a planning note, a paragraph typed straight into a conversation, three differently-worded versions of the same story. None of that is trimmed to fit a template. It is preserved, then enriched.

**The committed entry is the durable record.** The verbatim capture (Part 0) lives in the session-wiki, which is gitignored and therefore transient — a laptop is not a backup. Anything that must outlive this machine has to reach the committed entry. That makes the entry's job *preservation*, not summary: it carries the technical substance, and the raw copy is only the audit trail for how it got there.

## Part 0 — Capture the input as-is

Capture happens before interpretation, by one of two routes depending on who is holding the material.

### Route A — the owner writes it directly (`raw/brag/inbox/`)

The owner drops a note into [`raw/brag/inbox/`](../../raw/brag/inbox/) from Obsidian or any editor: any filename, any shape, no polish. This is the default and the lowest-friction path, and it exists because the note that gets written today is worth more than the better note that never gets written.

**The folder is the status.** A note in `inbox/` has not been ingested; an empty inbox means everything has. That replaces any need to cross-reference the ledger to answer "what still needs doing?", and it is visible in the file sidebar and colour-coded in the graph view.

### Route B — an agent is handed the material

When material arrives mid-conversation — an email thread, a chat export, a board export, a dictated paragraph — write it verbatim into the session-wiki's raw capture area first:

```
__untracked_stuff/<scope>/session-wiki/raw/<YYYYMMDD>_brag-<slug>.<ext>
```

1. **Verbatim.** No cleanup, no reformatting, no truncation. If the owner supplied three renderings of the same accomplishment, all three are the input.
2. **Record where it came from** at the top: source, date received, and the date the *accomplishment* happened if they differ.
3. **Never edit it afterwards.** Corrections become a new capture, not an edit to an old one.
4. **This copy is transient** — the audit trail, not the archive. Where an export is large and worth keeping permanently, the owner may commit it instead; [`raw/trello/`](../../raw/trello/) is the standing example.

Either route, capture comes before any decision about tiers, duplicates, or wording.

## Part 1 — Write or update the committed entry

**Where:** `llm-wiki/raw/brag/YYYY-MM-DD-<slug>.md` — one file per accomplishment, date first, short kebab-case slug.

**The metadata is YAML frontmatter**, so Obsidian indexes it as properties: the vault can then filter and group entries by thread, domain or `resume-worthy` without reading any of them. Frontmatter must be the very first thing in the file, before the `#` heading, and the `title` repeats the heading because Obsidian's property views show the former and the graph shows the latter. Conventions: [Obsidian vault](obsidian-vault.md).

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
---
title: "<One-line headline of the accomplishment>"
date: "YYYY-MM-DD"                      # or a range: "2021-11 to 2022-01"
thread: <CODE>                          # the coverage.md thread this belongs to
domains:
  - "<one or more from accomplishments-by-domain.md>"
context: "<employer / project / team, as publicly describable>"
sensitivity: private-repo               # or public-friendly
resume-worthy: yes                      # or maybe / no
# storied: [<cluster>/<story>]         # added only when a story graduates this entry; never pre-filled
---

# <One-line headline of the accomplishment>

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

Optional sections are welcome when the input supplies them: dated sub-sections for multi-episode work, and any alternate renderings the owner wrote. Two more are **expected wherever there is anything to say**, because they are what makes later prominence decisions possible:

- `## Evidence limitations` — which parts of the entry rest on the owner's own statement rather than on an artifact. Say it plainly; an entry that names its weakest point is *more* usable outward, because the outward version can then be drawn exactly at the line the evidence reaches.
- `## What was blocked, cut short, or wrong` — work proposed and refused, built and stopped, or a negative result reached and acted on. The owner's standing position is that these are part of the record and part of the win: the lesson from a blocker, including the ones not overcome, is tellable. See [voice and prominence](voice-and-prominence.md) § *Blocked, frozen, and never shipped*.

**Dropping is capture only.** Do not edit the resume, `accomplishments-by-domain.md`, or any other wiki page during a drop. No index update is needed. An entry is *not yet ingested* while it is present in `raw/brag/` and absent from the ledger.

### Part 1b — Same accomplishment, new input

Three cases, distinguished by what the new input adds:

| Case | Test | What to do |
|---|---|---|
| **Duplicate** | Same accomplishment, same evidence trail, nothing new | Merge anything phrased better into the existing entry; do **not** create a second file. Log the merge in *Record history*. |
| **Update** | Same accomplishment, new evidence, outcome, metric or correction | Augment in place: edit the section concerned, or append `### Follow-up, YYYY-MM-DD` for a distinct later episode. Widen `date:` only if the accomplishment itself continued. |
| **Related** | A distinct accomplishment in the same programme | New entry. Add reciprocal `## Related` links naming the relationship, and put both in the same thread in [coverage.md](../resume/coverage.md). |

In all three cases append a `## Record history` line for the day, saying what changed and briefly why. If an updated entry is already in the ledger and the change alters its headline, domains, or `resume-worthy` value, re-run Part 2 for it and note the re-ingest in the ledger's *Ingested* column.

### Part 1c — When the owner's memory and the email record disagree

Where the owner's recollection of an episode (dates, order of events, who did what) disagrees with the mailbox, **the email record is authoritative**, and his original account is kept verbatim alongside it. Ruled by the owner on 2026-09-25 ("Use the information grounded in emails as authoritative"), after the Intel compiler episodes turned out to be in the opposite order from his memory; the same pass found several survey-level entries overstated or misdated once the full threads were read.

- **Ground entries in full threads, not snippets.**
- Record the settled version in *What was blocked, cut short, or wrong* or *Evidence limitations*, keep his account verbatim next to it, and add a *Record history* line.
- Anything that touches the public resume is an **owner item** in the tracker, not an edit: promotion is a separate pass ([Part 3](#part-3--promote-to-the-resume)).

## Part 2 — Ingest (periodic)

Run when the owner asks, or when un-ingested entries accumulate — a handful is a good trigger.

1. **List what is pending.** Everything in [`raw/brag/inbox/`](../../raw/brag/inbox/) (excluding its `README.md`), plus entries in `raw/brag/` with no ledger row, plus rows whose entry's latest *Record history* date is newer than the row's *Ingested* date.

   **Clearing the inbox.** Each note becomes a properly dated entry in `raw/brag/`, or is merged into the entry it belongs to. Build the entry *around the owner's wording* rather than rewriting it, keep the technical substance, and derive the filename date from the accomplishment. Then delete the inbox note — its content now lives in the entry — and record the origin in that entry's `## Record history` (`ingested from inbox note "<name>"`). An inbox note is never left behind "just in case": that would break the one rule that makes the folder a reliable status signal.
2. **Read each entry fully.** Re-check the tier tag against the content. Check that the filename date and `date:` line describe the accomplishment rather than the capture. Check for a second entry describing the same accomplishment and merge per Part 1b.
3. **Look up the shards it touches.** Always [accomplishments by domain](../concepts/accomplishments-by-domain.md) — add or strengthen a headline bullet under each domain the entry lists, citing the entry file. Then, only where the entry genuinely adds something: [organizations](../entities/organizations.md) for a new employer, product or role; [technical themes](../concepts/technical-themes.md) or [skills matrix](../concepts/skills-matrix.md) for a newly evidenced capability. Record every page touched in the ledger row.
4. **Register it in the coverage map.** Start at [coverage.md](../resume/coverage.md), then open only the owning subject shard. Assign the entry to exactly one primary thread (cross-list it elsewhere without duplicating claims, or open a new thread if it starts one), then decompose it into claims — one promotable assertion each — and add them with status `absent`. Recompute thread, shard and headline figures; run `python3 script/check-coverage.py` from the repository root. Follow the map's physical-design rules when a shard grows; never append claim tables to the router.
5. **Append the ledger row:** entry file, ingest date, pages touched, `resume-worthy` value, promotion status `not promoted`.
6. **Update [`index.md`](../../index.md)** only if a new wiki page was created.
7. **Record the pass** in the maintainer's operations log, outside version control.

**Never modify the primary resume during ingest.** If an entry is clearly resume-worthy, say so in the ledger row and tell the owner; promotion is a separate pass.

## The quarterly hook

The owner runs the employer's **Quarterly Conversation** cycle every quarter, and it asks — in the employer's own words — *what are the big wins and key learnings you are proud of since your last Quarterly Conversation?*

That is this workflow's question, asked by someone else, on a reliable cadence. Treat each QC as the standing quarterly trigger:

- **Before** the conversation, run an ingest. The inbox is the quarter's raw material, and [accomplishments by domain](../concepts/accomplishments-by-domain.md) is a better prompt than memory for what the quarter actually contained.
- **After** it, drop whatever surfaced in the conversation that is not yet captured — the wins articulated out loud, the commitments made for next quarter, anything a leader reflected back that you had not framed that way yourself.

Quarterly is also roughly the right cadence for the ingest itself: often enough that detail survives, rare enough that it stays a single deliberate pass. The practice is recorded as its own entry, [2021-06-23 quarterly-conversation practice](../../raw/brag/2021-06-23-quarterly-conversation-practice.md), because sustaining it for five years is itself an accomplishment.

## Part 3 — Promote to the resume

Handled by [update the outward-facing resume](../resume/update-workflow.md). When a promotion lands, that pass sets the ledger row's promotion status and flips the affected claims in [coverage.md](../resume/coverage.md) to `in` or `partial` in the same edit.

## Part 4 — Graduate into stories

Once an entry's substance is told in a story, it graduates: a `storied:` property is added and the entry steps out of the main graph, while its body stays exactly as recorded. The procedure, the story structure and reading lists are [brag stories](brag-stories.md).

## Related

- [Coverage map](../resume/coverage.md) — threads, claims, and how much has reached the resume.
- [Accomplishments by domain](../concepts/accomplishments-by-domain.md) — the landing page for ingested entries.
- [Brag ledger](../sources/brag-ledger.md) — ingest and promotion state.
- [Sensitivity tiers](sensitivity-tiers.md) — the tag definitions and the policy this workflow refines.
- [Voice and prominence](voice-and-prominence.md) — why an entry records its own limitations, and how support decides prominence later.
