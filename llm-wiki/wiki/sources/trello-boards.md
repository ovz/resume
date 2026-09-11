# Source: Trello board exports

> **Doc type:** reference
>
> Summary of the committed board snapshots in [`raw/trello/`](../../raw/trello/), stored compressed and checksummed per [large imports](../workflows/large-imports.md). Tier **T1 by owner decision** (T2 by default rule — see [sensitivity tiers](../workflows/sensitivity-tiers.md) rule 5). Status: **live** — the owner still uses these boards and will re-export. Harvest status: **substantially complete** — thematic lists harvested 2026-09-10; dated working lists remain as corroboration.

## What these are

Two Trello boards the owner has kept as a personal working record, exported 2026-09-09:

- **Device programme board** (`2026-09-09-r5-jira-board.json.xz`) — 1254 cards across 195 lists. Organized thematically rather than chronologically: location and positioning, beacon tracking, the capability framework, C++ guidelines, Conan packaging, dead reckoning and sensor research, observability, power budget, ODM documentation, plus dated sprint-planning lists running 2022 → 2026.
- **Leadership board** (`2026-09-09-leadership-board.json.xz`) — 1445 cards across 166 lists. Organized by counterpart and by ritual: one-on-one lists per person, quarterly-conversation lists, promotion and behaviour material, and a "To Add to Resume" list the owner maintained himself.

They are the owner's own notes, not employer systems of record — which is what makes them both unusually candid and unusually useful for reconstructing a career narrative.

## Why this source is unusual

Most sources in this wiki are documents written to be read by someone. These are working boards written to be used by one person, so they carry the reasoning behind decisions rather than the polished conclusion — the ruled-out options, the vendor limitations discovered, the thing that did not work. That is exactly the material a resume claim needs underneath it and exactly the material polished documents lose.

The "To Add to Resume" list deserves specific mention: eight cards from 2021 in which the owner flagged his own accomplishments as resume-worthy at the time. It is the closest thing in the corpus to a contemporaneous brag file predating the brag file.

## Harvested (2026-09-09 and 2026-09-10)

**First pass, 2026-09-09** — four entries: [GitHub Enterprise migration](../../raw/brag/2021-08-15-github-enterprise-migration-monorepo.md) and [quarterly-conversation practice](../../raw/brag/2021-06-23-quarterly-conversation-practice.md) from the leadership board; [C++ safety-critical guidelines](../../raw/brag/2022-02-18-cpp-safety-critical-embedded-guidelines.md) and [Conan and cross-build](../../raw/brag/2022-04-06-conan-package-management-embedded-cross-build.md) from the device board. Plus roles into professional contacts.

**Second pass, 2026-09-10** — the full ingest, after the restriction on named and performance-related material was withdrawn. Twelve entries:

| Entry | Board and lists |
|---|---|
| [2020-07-14 upward feedback practice](../../raw/brag/2020-07-14-upward-feedback-practice.md) | leadership — manager positive/negative feedback lists |
| [2021-06-29 engineering excellency and facilitation](../../raw/brag/2021-06-29-engineering-excellency-and-meeting-facilitation.md) | leadership — *Engineering Excellency*, *R5 Processes* |
| [2021-11-15 product architecture and power budget](../../raw/brag/2021-11-15-r5-product-architecture-power-budget-tradeoffs.md) | device — *R5 Vision*, *Trade Offs*, *Strategic directions*, *Power Budget* |
| [2021-11-22 dead reckoning and sensor cluster](../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) | device — *Dead Reckoning*, *BLE Examples*, *BLE Beaconing*, *SensorTile*, vendor lists |
| [2022-05-18 Snowflake device telemetry](../../raw/brag/2022-05-18-snowflake-edw-device-telemetry.md) | device — *Snowflake Based EDW* |
| [2022-08-03 ODM specification authoring](../../raw/brag/2022-08-03-odm-specification-authoring.md) | device — *ODM Documentation for R5*; leadership — the retrospective list |
| [2023-05-02 performance conversation](../../raw/brag/2023-05-02-performance-conversation-and-promotion-context.md) | leadership — *Performance Allegations*, *Tactical Empathy* |
| [2023-12-05 launch readiness](../../raw/brag/2023-12-05-operational-excellence-launch-readiness.md) | device — *Operational Excellence* |
| [2024-12-31 device test automation](../../raw/brag/2024-12-31-device-test-automation-robot-framework.md) | device — *R5.5 Automation* |
| [2025-04-01 Staff Engineer positioning](../../raw/brag/2025-04-01-staff-engineer-behaviors-principal-positioning.md) | leadership — *Staff Engineer behaviors* |
| [2025-05-23 mentorship toward Principal](../../raw/brag/2025-05-23-mentorship-principal-engineer-goal.md) | leadership — the four mentor lists |
| [2025-07-18 FOTA vendor escalation](../../raw/brag/2025-07-18-fota-vendor-escalation-lively-mobile2.md) | leadership — mentor lists, 2025 quarterly preparation |

Professional contacts gained six itemized entries in the same pass.

## Known to remain (harvest map)

The thematic lists are now largely harvested. What is left is thinner and more diffuse — worth a pass, but no longer the bulk.

**Device board**

- Sprint-planning and dated working lists, 2022 → 2026 (roughly 120 lists). These are a working log rather than accomplishment material; the value in them is corroborating dates and filling detail into entries that already exist, not new entries. Mine them when a specific claim needs evidence.
- Smaller thematic lists not yet worked: *Hack Blue 22*, *R4-style R5*, *Development Goals*, *LED*, *Birds*, *R6+ Ideas*, *R5 Ticket Ideas*, *TODO backburners*, *Learning*.
- *Current Health* and *Hospital at Home* lists — the 2025–2026 platform the owner moved toward; overlaps the CCF and architecture-ownership entries and may be better captured from more recent sources.
- *puffin* and *mdm9607 documentation* — component-level detail, largely superseded.

**Leadership board**

- *Unasked Questions* (131 cards) and *Edgy questions for One on One* (25) — a question bank the owner built for one-on-ones. Not accomplishments, but arguably an artifact of the managing-upward practice worth one entry describing the practice itself.
- *Roller-Deck Best Buy* (64 cards) — a relationship-tracking deck; feed into professional contacts rather than a brag entry.
- Individual dated one-on-one lists, 2019 → 2026 (roughly 100 lists). Same status as the device sprint lists: corroboration, not new entries.
- *Hiring*, *Growth Opportunities at GreatCall*, *Top Management Questions*, *Questions to Organization* — organizational-context material; the hiring list may support a hiring/interviewing entry.
- Quarterly-conversation lists 2023 → 2026 beyond what the practice entry and the mentorship entry already carry.

## Harvest these boards in full

These are hand-curated notes the owner wrote about the owner's own working life, and **nothing in them needs withholding from the professional record.**

An earlier version of this page carved out the leadership board's performance discussions, promotion material and named accounts of colleagues as off-limits to synthesis. **That restriction has been withdrawn.** Those interactions are not a sensitive residue around the real content — they are among the most valuable material in the corpus for a principal-level narrative, because they are the evidence of how the owner led, mentored, disagreed, and was assessed. Harvest them at T1 with names, roles and substance intact, per [sensitivity tiers](../workflows/sensitivity-tiers.md) rule 8.

Where relationship narrative belongs: the brag entry or synthesis page describing that work, cross-linked from [professional contacts](../entities/professional-contacts.md), which stays a roster rather than absorbing the narrative.

## What still stays in the archive

Two ordinary limits, unchanged:

- **Contact details** are never copied out into a wiki page ([sensitivity tiers](../workflows/sensitivity-tiers.md) rule 3).
- **Internal ticket identifiers, deep links, repository paths, and ODM and component-vendor specifics** stay in the archive and do not travel into committed entries — these are the employer's internals, not the owner's record.

And the standing T0 rule: colleague names come out when anything is promoted to the public resume. Capture is not disclosure.

## Re-ingest

The owner intends to tidy the boards and export again. New snapshots are added alongside, never replacing — see [`raw/trello/README.md`](../../raw/trello/README.md). Diff against the previous snapshot rather than re-reading in full.

A new export follows [large imports](../workflows/large-imports.md): uncompressed working copy into the scratch scope, compressed and checksummed copy into `raw/trello/`, manifest row added here and in that README.

## Related

- [Large imports](../workflows/large-imports.md) — how a snapshot gets archived, and how to unpack one.
- [Brag file workflow](../workflows/brag-file.md) — how material from here becomes an entry.
- [Sensitivity tiers](../workflows/sensitivity-tiers.md) — why this source is committed at all, and what that does not license.
- [Professional contacts](../entities/professional-contacts.md) — the roster; relationship narrative from these boards lives with the work it describes.
