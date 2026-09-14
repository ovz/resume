---
cluster: positioning
aliases:
  - "Positioning stories"
  - "Location stories"
  - "GPS stories"
---

# Positioning, location and GPS — story cluster

> **Doc type:** reference
>
> Hub for the positioning cluster: the through-line, the stories planned and written, and the entries each draws on. Open this note's local graph to see the cluster as a sub-graph. Audience: the owner preparing to talk about location work; agents writing these stories.

## The through-line

"Accurate location is not a feature on an Emergency Response device; it is the product." Eight years, one thread: the company's positioning subject-matter expert on Lively Mobile+, an architecture that made positioning a non-issue in the power budget, field diagnosis of a fault that lost the fix, and a beacon feature handed to him in 2023, kept deliberately small while the classic pitfalls around it multiplied — which three years later still carries the home cradle across a firmware update.

## Stories

| # | Working title | The claim | Draws on | Status |
|---|---|---|---|---|
| P1 | Becoming the company's positioning expert — and buying calendar time | Fixed positioning through engineer-to-engineer work with the platform vendor's team in India; argued to license Skyhook per device because reliable location is vital to commercial customers and home-grown fusion costs the one resource nobody can buy back, calendar time; built a direct engineering relationship with Skyhook where chip-vendor talk otherwise runs through the manufacturer; researched Skyhook and Qualcomm observability with AI's help | Owner statement 2026-09-14 in the brag inbox; Skyhook and positioning cards on the device board, 2022–2025; R4-era material still owed | **needs ingest** |
| P2 | [We decided the battery before we decided what the device looked like](positioning/power-budget-non-issue.md) | Decided the battery before the form factor, then designed a sensor path that keeps the application processor asleep | [2021-11-15 power budget](../../raw/brag/2021-11-15-r5-product-architecture-power-budget-tradeoffs.md) · [2021-11-22 sensor cluster](../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) · [2021-10-16 battery specialization](../../raw/brag/2021-10-16-battery-power-second-specialization.md) | **draft written** |
| P3 | [The fault that lost the fix](positioning/the-fault-that-lost-the-fix.md) | Root-caused a recurring multithreading fault in a vendor positioning library from telemetry alone, and closed the recovery gap | [2024-05-15 positioning root cause](../../raw/brag/2024-05-15-skyhook-positioning-root-cause-diagnostics.md) | **draft written** |
| P4 | [Every classic pitfall around beacon tracking was survivable alone; together they multiplied](positioning/home-away-kept-simple.md) | Handed beacon tracking as an assignment, met a run of classic pitfalls at once — a frozen cradle, a missing consumer, gold-plating, a long-lived branch, accreted add-ons, an implicit state machine — saw that they multiply, and kept driving down the one factor he controlled: Home/Away in 2023, a location state machine as the next stage in 2026 | [2023-11-27 Home/Away](../../raw/brag/2023-11-27-r5-home-away-beacon-tracking.md) · [2026-09-01 beacon persistence](../../raw/brag/2026-09-01-r5-beacon-tracking-fota-persistence.md) | **draft written** (replaced 2026-09-14) |

## Related, not conflated

Positioning is mostly the record of things done right: the current device positions well, and the buy-versus-build call behind it held. The rough ride of the same years — the state machines, the keep-alive build, MCU Fatal UI — is its own cluster, [state machines](state-machines.md). P4 sits on the border: its beacon design belongs here; its add-ons and the location state machine it now argues for belong there, and are due to move when that cluster's first story is written.

## Reach for these when

- **Embedded or firmware roles** — P2, P4.
- **"Tell me about your hardest bug"** — P3.
- **Principal or architecture conversations** — P2, then P4.
- **Working with vendors and silicon partners** — P3, then P4.
- **Principal behaviours, compounding pitfalls, scope you do not control, YAGNI, or AI and risk** — P4.
- **Product sense** — P1, with [fall detection](../../raw/brag/2026-09-11-fall-detection-product-driver.md) as its companion.

## Status

P2 and P3 are written as drafts (2026-09-13); P4 was rewritten on 2026-09-14 after the owner corrected it — the earlier "one engine for every location source" telling was wrong and is retired. All three are ready to **rehearse** — read each aloud once, then set `status: rehearsed` in its frontmatter. P1 still waits on the owner's R4-era material.

## Before writing

The R5 board holds positioning material not yet in any entry — geofence entry and exit behaviour, debug logging for positioning failures, a memory-leak experiment on the positioning library, and positioning with silicon-vendor telemetry. Harvest it into the entries first, so the stories rest on the record rather than on memory.
