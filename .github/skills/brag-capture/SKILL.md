---
name: brag-capture
description: "Record a professional accomplishment in the brag file, fold captured entries into the knowledge layer, or graduate them into told-able stories and build reading lists from them. Handles input in any form — an email or chat export, a pull-request description, a planning note, a dictated paragraph, or several differently-worded versions of the same story. USE WHEN the owner mentions having shipped, launched, presented, fixed or led something worth remembering, says 'add this to my brag file', hands over material to file, asks to process the brag inbox, asks to ingest or catch up on brag entries — including the quarterly pass around a Quarterly Conversation — or asks for a story, a story cluster, or a reading list to prepare for an interview, a networking event or an employer. DO NOT USE for putting something on the outward-facing resume — that is resume-editing, a separate deliberate pass."
---

# Capture an accomplishment

The rules live in [`llm-wiki/wiki/workflows/brag-file.md`](../../../llm-wiki/wiki/workflows/brag-file.md): the capture step, the entry template, the dating rule, the duplicate/update/related test, and the ingest sequence. Read that page before writing anything. Nothing is duplicated here, so the two cannot drift.

This skill is the on-demand entry point for agents that match on skill descriptions; [`llm-wiki/AGENTS.md`](../../../llm-wiki/AGENTS.md) delivers the same routing automatically once an agent is already working inside `llm-wiki/`. The gap this closes is the cold start — the owner mentioning an accomplishment while nothing in `llm-wiki/` is open.

## The two principles

**Never discard information.** Input arrives however it arrives. It is not trimmed to fit a template, rephrased into house style, or compressed because it seems long. Preserve it, then enrich it as evidence accrues.

**The committed entry is the durable record.** The verbatim capture lands in the session-wiki, which is gitignored and therefore transient — a laptop is not a backup. Anything that must outlive this machine has to reach the committed entry, which makes the entry's job preservation rather than summary.

## Why capture is its own step

An accomplishment reaches the resume in three hops, each a **rewrite that re-checks tier and depth**:

```
llm-wiki/raw/brag/  →  llm-wiki/wiki/concepts/accomplishments-by-domain.md  →  markdown/
```

This skill owns the first two. Capture is deliberately low-friction because it is worth little when deferred — the numbers, the names and the reason it mattered are all available on the day and mostly gone a month later. A partial entry beats no entry.

## Capture, then write

1. **Capture before interpreting.** The owner's own notes land in `llm-wiki/raw/brag/inbox/` — any filename, any shape. **A note in that folder is un-ingested; an empty inbox means everything is ingested**, which is the whole status mechanism, so never leave a processed note behind. Material handed to an agent instead goes verbatim to the session-wiki (`raw/<YYYYMMDD>_brag-<slug>.<ext>`), noting source and date received, never edited afterwards.
2. **Check for an existing entry**, then classify: *duplicate* (nothing new — merge, no second file), *update* (new evidence or outcome — augment in place), or *related* (distinct accomplishment in the same programme — new entry, reciprocal links, same thread).
3. **Date by the accomplishment, not by today.** The filename and `date:` line describe when the thing happened; the trailing `## Record history` is the only place that records when the file changed.
4. **Check the tier** against [`sensitivity-tiers.md`](../../../llm-wiki/wiki/workflows/sensitivity-tiers.md). Input is usually clean, but check every time. A case the policy does not resolve cleanly is a defect in the policy: apply the conservative reading, record the case, and propose the refinement — never settle it with a silent one-off call.
5. **Write down what the evidence does *not* support, while it is fresh.** An `## Evidence limitations` section, and a `## What was blocked, cut short, or wrong` section where there is anything to say, are what make later prominence decisions possible — and the owner's position is explicit: honest telling of blockers, including the ones not overcome, beats a record that only holds wins.
6. **Preserve the technical substance.** Mechanisms, schemas, algorithms, failure modes, thresholds and the actual reasoning stay in. Keep the owner's own words where they carry meaning, and keep every rendering supplied — a performance-review version, a concise version and a resume-style version are three useful compressions, not one to pick from. Abstract only what the tier requires.
7. **Capture only.** A drop never edits the resume, the synthesis pages, or the coverage map.
8. **Confirm the paths back to the owner and stop.**

## Ingest — periodic

Run when the owner asks, when the inbox fills, or **around a Quarterly Conversation** — the employer asks the same question this workflow does ("big wins and key learnings since your last QC"), on a reliable cadence, so that is the natural quarterly trigger. Pending work is: everything in `inbox/`, plus entries in `llm-wiki/raw/brag/` with no row in [`brag-ledger.md`](../../../llm-wiki/wiki/sources/brag-ledger.md), plus rows whose entry's latest record-history date is newer than the ledger *Ingested* date.

Clearing an inbox note means turning it into a dated entry (or merging it into the one it belongs to) **built around the owner's wording**, then deleting the note and recording its origin in the entry's `## Record history`.

Follow § *Part 2* of the workflow page. Two steps are easy to forget and both matter:

- **Shard lookup** — always [`accomplishments-by-domain.md`](../../../llm-wiki/wiki/concepts/accomplishments-by-domain.md), then the entity, theme and skills pages *only* where the entry genuinely adds something.
- **Coverage registration** — assign the entry to a thread in [`coverage.md`](../../../llm-wiki/wiki/resume/coverage.md), decompose it into claims, add them as `absent`, and recompute the totals. An entry that never reaches the coverage map is invisible during resume work.

**Ingest never touches the outward-facing resume.** If an entry is clearly resume-worthy, say so in the ledger row and tell the owner; promotion is a separate pass under `resume-editing`.

## Stories and reading lists

The third stage. An entry whose substance is told in a **story** graduates: a `storied:` property goes on the entry, its body is never touched, and the main Obsidian graph steps it out of the working view. Stories live in `llm-wiki/wiki/stories/<cluster>/`, beside a hub note per cluster. A **reading list** is the three to seven stories worth rereading before one conversation.

Procedure, structure and reading-list steps: [`llm-wiki/wiki/workflows/brag-stories.md`](../../../llm-wiki/wiki/workflows/brag-stories.md). **Voice, prominence and how to talk about work that was blocked: [`llm-wiki/wiki/workflows/voice-and-prominence.md`](../../../llm-wiki/wiki/workflows/voice-and-prominence.md)** — read it before writing any outward text, including a resume line or a LinkedIn block. Two rules are easy to break:

- **Never add an empty `storied:`** — the graph tests for the property's presence, so an empty one hides an entry that has not graduated.
- **A reading list belongs to one conversation.** Keep it in the session scratch scope; only durable employer research goes into `llm-wiki/wiki/analysis/employers/<employer>/`.

## Hand off

Agents do not commit — see the root [`AGENTS.md`](../../../AGENTS.md). Report the files written and let the owner review.
