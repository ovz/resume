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
| P1 | [I argued to buy our positioning per device instead of building it](positioning/buying-calendar-time.md) | Argued to license a commercial positioning service per device over home-grown fusion — commercial customers set the bar and calendar time cannot be bought back — after evaluating it against the previous generation as the baseline; built a direct engineering relationship with the library's engineers. Follow-ups carry the R4 origin (fixing location engineer to engineer with the manufacturer's team) and the "no product means no churn" reasoning | [2022-09-16 buying calendar time](../../raw/brag/2022-09-16-skyhook-license-buy-calendar-time.md) · [2020-01-01 R4 location fix](../../raw/brag/2020-01-01-r4-location-fix-engineer-to-engineer-borqs.md) | **draft written** (2026-09-24) |
| P2 | [Every number in the power budget was observed on the bench, and added the way anyone in the industry would add it](positioning/power-budget-non-issue.md) | Refused to cut corners on the estimate: observed each sensor feature on discovery hardware rather than trusting the feature list, took the right datasheet rows, added them by duty cycle and measured — then set positioning to be a non-issue in the budget | [2021-11-15 power budget](../../raw/brag/2021-11-15-r5-product-architecture-power-budget-tradeoffs.md) · [2021-11-22 sensor cluster](../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) · [2021-10-16 battery specialization](../../raw/brag/2021-10-16-battery-power-second-specialization.md) | **draft written** (rewritten 2026-09-24 on the owner's correction: the trade-off is obvious; the rigour is the story) |
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
- **Product sense** — P1, with [fall detection](../../raw/brag/2026-09-11-fall-detection-product-driver.md) as its companion: the button reaches a caring agent for any reason, while fall detection and Home/Away are what the device does without being asked.
- **Build versus buy, or vendor relationships** — P1, then P3.

## Status

P1 was written and P2 rewritten on 2026-09-24; P3 was corrected the same day so that its stakes say what the owner does — the device calls for help by itself when it detects a fall. P2, P3 and P4 are ready to **rehearse**; P1 is a fresh draft. Read each aloud once, then set `status: rehearsed` in its frontmatter.

## Before writing

The R5 board holds positioning material not yet in any entry — geofence entry and exit behaviour, debug logging for positioning failures, a memory-leak experiment on the positioning library (now harvested into [2024-04-03](../../raw/brag/2024-04-03-skyhook-file-descriptor-leak-reproduction.md)), and positioning with silicon-vendor telemetry. Harvest it into the entries first, so the stories rest on the record rather than on memory.
