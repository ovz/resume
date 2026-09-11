---
title: "Fall detection is Lively Mobile's killer feature, and its next innovation is mine to drive"
date: "2018–present (captured 2026-09-11)"
thread: FALL
domains:
  - "embedded and safety-critical devices"
  - "architecture and API design"
context: "GreatCall → Best Buy Health; Lively Mobile+ (R4) and Lively Mobile 2 (R5)"
sensitivity: private-repo
resume-worthy: yes
---

# Fall detection is Lively Mobile's killer feature, and its next innovation is mine to drive

## What I did

In the owner's words: **"Fall Detection is the killer feature of Lively Mobile, with Care call center being central load bearing one, but not a focused driver the way fall detection is."** And, of the current work: **"We are on track to innovate fall detection and other aspects of active seniors needs."**

That is a product judgement, not just an engineering one: the Care center is what makes the service work, and fall detection is what the product is chosen for. The owner's record on the feature runs the whole arc:

- **Built it.** Fully automated fall detection on Lively Mobile+ — filtering MCU signals and coordinating device subsystems to place a call, with falls tracked across a reboot. *(Source: the primary resume.)*
- **Architected where it goes next.** The 2021 sensor-cluster architecture puts motion classification in the sensor's own machine-learning core so the application processor stays asleep, with the sensor and MCU lineup selected against fall and stair-transition requirements — see [2021-11-22](2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md), and the power budget behind it in [2021-11-15](2021-11-15-r5-product-architecture-power-budget-tradeoffs.md).
- **Driving its next innovation.** As owner of Architecture for the Wearables line since April 2026, the owner is driving the next round of fall-detection innovation for active seniors.

*(To supply: the owner's specific contributions to the R4 implementation beyond the resume's summary; what "active seniors' needs" covers beyond falls — at T1 only.)*

## Why it matters

- **Knowing which feature is the driver is principal-level product sense.** A load-bearing service and a focused driver need different engineering investment; naming the difference is what lets architecture spend go where it moves the product.
- **Continuity from build to architecture to innovation** on one feature across eight years is unusual evidence of ownership.

## Sensitivity

**The owner's call, 2026-09-11** — [sensitivity tiers](../../wiki/workflows/sensitivity-tiers.md) rule 6: the owner may downgrade a tier; an agent may not. On 2026-09-10 an agent had held "on track to innovate fall detection" at T1 as current-employer roadmap. The owner reversed that: the **direction** — driving the next round of fall-detection innovation — may be stated outward. What still stays out of every outward document: any feature, sensor, algorithm, date or roadmap specific that has not shipped publicly.

## Related

- [2023-09-01 Lively Mobile 2 manufacturer transition](2023-09-01-r5-odm-transition.md) — the programme this continues on.

## Record history

- 2026-09-11: created from the owner's direct statements; supersedes the 2026-09-10 decision to hold the innovation direction at T1.
