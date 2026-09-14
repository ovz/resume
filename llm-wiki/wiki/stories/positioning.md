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

"Accurate location is not a feature on an Emergency Response device; it is the product." Eight years, one thread: the company's positioning subject-matter expert on Lively Mobile+, an architecture that made positioning a non-issue in the power budget, field diagnosis of a fault that lost the fix, one engine for every location source, and state that survives a firmware update.

## Stories

| # | Working title | The claim | Draws on | Status |
|---|---|---|---|---|
| P1 | Becoming the company's positioning expert | Became the go-to authority on GNSS, ECID, Wi-Fi and BLE positioning for an emergency-response device, and led a major upgrade of its positioning infrastructure | *No entry yet* — the primary resume states it; the owner's R4-era material is owed | needs capture |
| P2 | [We decided the battery before we decided what the device looked like](positioning/power-budget-non-issue.md) | Decided the battery before the form factor, then designed a sensor path that keeps the application processor asleep | [2021-11-15 power budget](../../raw/brag/2021-11-15-r5-product-architecture-power-budget-tradeoffs.md) · [2021-11-22 sensor cluster](../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) · [2021-10-16 battery specialization](../../raw/brag/2021-10-16-battery-power-second-specialization.md) | **draft written** |
| P3 | [The fault that lost the fix](positioning/the-fault-that-lost-the-fix.md) | Root-caused a recurring multithreading fault in a vendor positioning library from telemetry alone, and closed the recovery gap | [2024-05-15 positioning root cause](../../raw/brag/2024-05-15-skyhook-positioning-root-cause-diagnostics.md) | **draft written** |
| P4 | [One engine for every location source](positioning/one-engine-for-every-source.md) | Unified beacon, GPS and Wi-Fi behind per-provider interfaces with arbitration and fallback, and made paired-beacon state survive firmware updates | [2025-11-15 location engine](../../raw/brag/2025-11-15-r5-location-engine-design.md) · [2026-09-01 beacon persistence](../../raw/brag/2026-09-01-r5-beacon-tracking-fota-persistence.md) | **draft written** |

## Reach for these when

- **Embedded or firmware roles** — P2, P4.
- **"Tell me about your hardest bug"** — P3.
- **Principal or architecture conversations** — P2, then P4.
- **Working with vendors and silicon partners** — P3.
- **Product sense** — P1, with [fall detection](../../raw/brag/2026-09-11-fall-detection-product-driver.md) as its companion.

## Status

P2, P3 and P4 are written as drafts (2026-09-13) and are ready to **rehearse** — read each aloud once, then set `status: rehearsed` in its frontmatter. P1 still waits on the owner's R4-era material.

## Before writing

The R5 board holds positioning material not yet in any entry — geofence entry and exit behaviour, debug logging for positioning failures, a memory-leak experiment on the positioning library, and positioning with silicon-vendor telemetry. Harvest it into the entries first, so the stories rest on the record rather than on memory.
