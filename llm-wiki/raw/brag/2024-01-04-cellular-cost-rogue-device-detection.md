---
title: "Caught devices burning cellular data cost, and made replacing and root-causing them routine"
date: "2024-01-04 to 2025-06"
thread: COST
domains:
  - "battery, power and cost of operation"
  - "data engineering"
  - "operational excellence and observability"
context: "Best Buy Health — Lively device fleet on the company's own MVNO; carrier data, device telemetry and the enterprise data warehouse"
sensitivity: private-repo
resume-worthy: yes
---

# Caught devices burning cellular data cost, and made replacing and root-causing them routine

## What I did

Brought together data that had never been in the same place: **cellular-operations data ingested from the network operator, device telemetry from the fleet, and the warehouse's own event tables** — joined on device identity (IMEI) — and used the combination to find individual devices that were consuming cellular data far outside any plausible pattern. Some were costing hundreds of dollars each in data charges.

The work had three parts.

**1. Establish what "rogue" means, by building one.** Rather than argue about a threshold, I wrote a **rogue-device emulation script** that drove deliberate excessive cellular data consumption on a device, so the detection path could be validated against a device known to be misbehaving. The calibration notes from the time: roughly 1 MB is trivially easy to move on a development device; the emulation ran at about **100 MB per hour**; and the proposal I put to the team was to treat **about 50 MB inside one hour as the indicator of rogue behaviour**. Getting the team to agree to that number *before* an incident is the point — a threshold negotiated during an incident is a threshold nobody trusts.

Doing this on the device meant working inside an embedded BusyBox environment with no convenient upload path: plain HTTP endpoints returned empty responses while HTTPS returned bad requests, `wget` could pull but pushing was the harder half, and bounding a continuous generator meant relying on `head` closing the pipe and the writer taking `SIGPIPE`. Small details, but they are the difference between a script that emulates a rogue device and a script that hangs.

**2. Turn it into an operational procedure.** I published a **rogue-device runbook** so that the response did not depend on me, and fed the scenario into the launch **tabletop exercise** — the same exercise that also rehearsed location accuracy, a message-broker outage, and self-reported device errors. Devices identified this way then went through a standard route: replace the unit, and root-cause it rather than only retiring it, so the fleet learns something from each one.

**3. Find the real ones.** The rogue-device work **did reveal an actual misbehaving device** shortly after it was built — a unit at roughly **1 GB per day**, which is excessive even for a test device — and the team was able to investigate it quickly because the detection and the runbook were already in place. Analysis of fleet data usage ran through a **Jupyter notebook** kept in the device test-automation repository rather than through spreadsheets, alongside warehouse queries that pulled behaviour per IMEI list.

This sat inside a wider cost-of-operation interest: I also submitted five ideas to the organization's cost-reduction programme in the same period, and later carried the same question into the enterprise data catalog — whether warehoused device-event tables earn their storage and cellular cost.

## Why it matters

The company is its own MVNO, so **cellular data is a direct per-device operating cost**, not somebody else's problem. On a fleet of tens of thousands of devices the distribution has a long tail, and a handful of units can quietly account for a disproportionate share of the bill while looking healthy by every other measure. Before this, nothing in the toolchain could name them; afterwards, naming them was routine, the threshold was agreed in advance, the response was written down, and each bad unit produced a root cause rather than just a replacement. It is the clearest example in the corpus of observability work paying for itself in money rather than in reassurance.

## Skills demonstrated

Joining carrier, device-telemetry and warehouse datasets on device identity; outlier detection on operating-cost data; threshold design validated against a deliberately misbehaving device; embedded scripting under BusyBox constraints; runbook authoring and tabletop-exercise design; Jupyter and warehouse SQL as the analysis surface; cost-of-operation framing for a device fleet.

## What was blocked, cut short, or wrong

- The **replacement-and-root-cause route** worked, but I cannot show from the record that it became a formally published SOP on the same footing as the patch-management SOP. Treat it as an established practice, not a signed procedure.
- The **five cost-reduction ideas** submitted to the organization's programme have no recorded outcome. Submitted is not adopted, and the entry says only that they were submitted.

## Evidence

The owner's device-programme board carries the rogue-device emulation ticket with its calibration notes and BusyBox findings, the runbook publication, and the tabletop-exercise scenarios; the leadership board carries the one-on-one note recording that the work revealed a real device at roughly 1 GB/day, the cost-reduction submissions, and a later meeting with the network operator. Both are the committed Trello snapshots. The analysis notebook lives in the device test-automation repository; the runbook and the tabletop materials are internal documents.

## Evidence limitations

- **"Hundreds of dollars" per device is the owner's figure.** The archive corroborates a device at about 1 GB/day and the thresholds above, but carries no billing data, so the dollar amount rests on the owner's statement.
- **The carrier-side ingest as a standing joined dataset** is likewise owner-stated. What the record shows directly is carrier engagement, device telemetry, warehouse queries per IMEI, and the notebook — the joined pipeline is the owner's account of how they were used together.
- Naming the network operator stays at T1. A public rendering says "the company's own MVNO" and claims the detection, the threshold and the runbook — all of which are the owner's own work.

## Related

- [2026-01-01-qualcomm-device-observability-evaluation](2026-01-01-qualcomm-device-observability-evaluation.md) — later vendor-platform evaluation considered whether additional telemetry reporting could affect cellular operating cost.

- [2022-05-18-snowflake-edw-device-telemetry](2022-05-18-snowflake-edw-device-telemetry.md) — learning the warehouse well enough to interrogate device telemetry directly, which is what made this join possible at all.
- [2025-10-29-ai-data-product-in-alation](2025-10-29-ai-data-product-in-alation.md) — the same cost question asked one layer up: do the warehoused device-event tables earn their storage and cellular cost?
- [2023-12-05-operational-excellence-launch-readiness](2023-12-05-operational-excellence-launch-readiness.md) — the launch-readiness argument that put chaos-style testing where failures actually live; the tabletop exercise this fed is that argument carried out.
- [2025-05-01-r5-device-specific-failure-investigations](2025-05-01-r5-device-specific-failure-investigations.md) — the same move on error activity rather than on data cost: from fleet-wide signal to the individual units driving it.
- [2021-10-16-battery-power-second-specialization](2021-10-16-battery-power-second-specialization.md) — the other operating-cost resource on the same device.

## Record history

- 2026-09-13: created from the owner's direct statement of 2026-09-13, grounded the same day in the committed Trello snapshots.
