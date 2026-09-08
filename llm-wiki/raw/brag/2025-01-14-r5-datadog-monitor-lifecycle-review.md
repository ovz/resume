# Initiated lifecycle review of obsolete and overlapping R5 Datadog monitors

- date: 2025-01-14
- context: Best Buy Health, R5 / Lively Mobile 2 production reliability
- domains: operational excellence and observability, embedded and safety-critical devices
- sensitivity: private-repo
- resume-worthy: yes

## What I did

After a BMA accelerometer-error monitor triggered, I questioned whether it still served a distinct purpose now that newer MCU-oriented monitoring was becoming available. I proposed removing or narrowing the older monitor only after the newer device-replacement monitoring stabilized, so the transition would not create a coverage gap. Firmware engineering agreed that the BMA monitor could be removed because MCU error-resolvable monitoring was available.

I then expanded the question from one alert to the broader set of Datadog monitors associated with my work, requesting a structured review of two categories: obsolete monitors and monitors requiring modification. This extended my ownership from creating and tuning monitors to maintaining the relevance and boundaries of the monitoring portfolio. The earlier production-monitoring foundation is documented in [the R5 Datadog launch entry](2024-03-07-r5-datadog-monitoring-launch.md).

## Why it matters

Datadog is a foundational tool in Best Buy Health's 24/7 operations, but operational excellence is broader than any single tool. I treated monitoring as an operational product that must evolve as better telemetry and more precise diagnostic approaches become available. The review balanced two risks: retaining obsolete or overlapping alerts, and removing coverage before a replacement was established.

The immediate outcome was an agreed retirement decision for the BMA monitor and an accepted request to examine the remaining monitors. The source does not confirm the monitor's deletion date or completion of the broader portfolio review, so this entry claims initiation, classification, and agreement rather than completed cleanup or quantified alert reduction.

## Skills demonstrated

- Operational ownership of monitoring lifecycle and signal quality
- Alert rationalization and overlap analysis
- Risk-managed transition between monitoring generations
- Cross-functional collaboration with firmware engineering
- Datadog monitor portfolio stewardship
- Systems thinking applied to operational excellence

## Evidence

January 14, 2025 email thread titled "Triggered: BMA accelerometer errors for R5 Devices." The thread documents the monitor-trigger question, the connection to newer MCU monitoring, firmware engineering's agreement that the older monitor could be removed, and the request to classify the remaining monitors as obsolete or needing modification. It does not document the actual deletion date, a completed portfolio review, or measured alert reduction.

## Performance-review version

Recognized that newer MCU-oriented monitoring had superseded an older R5 accelerometer-error monitor and initiated a deliberate monitor-lifecycle review. Secured agreement that the older monitor could be retired, tied broader cleanup to stability of its replacement, and requested classification of the remaining monitors into obsolete items and monitors requiring modification.

## Concise brag-file version

Initiated rationalization of the R5 Datadog monitoring portfolio after identifying that newer MCU coverage had superseded an older accelerometer-error monitor. Secured agreement on the older monitor's retirement and expanded the review to identify obsolete monitors and alerts requiring modification.

## Resume-style version

Initiated rationalization of the R5 Datadog monitoring portfolio by identifying superseded coverage, coordinating retirement of an obsolete monitor, and establishing review categories for monitor removal and refinement.

## Related

- [2024-03-07-r5-datadog-monitoring-launch](2024-03-07-r5-datadog-monitoring-launch.md) — the monitoring foundation this review rationalizes.
- [2026-09-01-r5-beacon-tracking-fota-persistence](2026-09-01-r5-beacon-tracking-fota-persistence.md) — the deliberate MCU reboot/fatal handling there is what the MCU-oriented monitoring generation favoured here observes (2026).

## Record history

- 2026-09-08: created from the owner's January 14, 2025 evidence summary
- 2026-09-08: added *Related* links to the 2024-03-07 launch and 2026-09-01 beacon-tracking entries