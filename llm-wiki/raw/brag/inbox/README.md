# Brag inbox — drop notes here

**Write anything here, any time, in any shape.** This is the zero-friction capture point, meant to be used from Obsidian while the thing is still fresh.

## The one rule that makes this work

**A note in this folder has not been ingested. An empty inbox means everything is ingested.**

That is the whole status mechanism. Nothing to look up, no ledger to cross-reference, no field to remember to set — the folder you can see in the sidebar *is* the answer. In the graph view these notes are coloured differently from ingested entries, so a backlog is visible at a glance.

## Dropping a note

- **Any filename.** `beacon thing.md`, `2026-09-14.md`, `that demo went well.md` — all fine. Naming is the ingest step's job, not yours.
- **Any shape.** A paragraph, a bullet list, a pasted email, three half-sentences. A partial note beats no note, and rough notes are *expected* here.
- **Say when it happened** if it was not today, even loosely ("last week", "around the June release"). The date of the accomplishment is the one thing that is genuinely hard to reconstruct later, and everything else can be filled in from it.
- **Don't polish.** Polishing is what makes people postpone writing, and a postponed note is usually a lost one.

Several notes about the same thing are fine — the ingest step works out whether they are one accomplishment or several.

## What happens on ingest

When you ask for an ingest, each note here is read and turned into a proper dated entry in the parent folder, or merged into the existing entry it belongs to. **Your wording is preserved** — the entry is built around what you wrote, not a rewrite of it — and the technical substance is kept rather than summarized away.

The note is then removed from the inbox, because its content now lives in the entry. Nothing is lost: the entry is the durable record, and the merge is logged in that entry's `## Record history`.

Full rules: [`../../../wiki/workflows/brag-file.md`](../../../wiki/workflows/brag-file.md).

## One thing to keep out

If something cannot be written down at private-repo level without losing its point — genuinely employer-internal detail — it does not belong in this repository at all. Note the *shape* of it here and keep the substance elsewhere. See [sensitivity tiers](../../../wiki/workflows/sensitivity-tiers.md).
