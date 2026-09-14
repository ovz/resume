---
title: "Battery and power management as a second specialization, interlocked with positioning"
date: "2021-10-16 to present (ongoing; evidence runs 2021-10 → 2026-07)"
thread: PWR
domains:
  - "battery, power and cost of operation"
  - "positioning and location"
  - "embedded and safety-critical devices"
context: "GreatCall / Best Buy Health — Lively Mobile+ and Lively Mobile 2, Qualcomm MDM-class modem SoCs"
sensitivity: private-repo
resume-worthy: yes
storied:
  - "positioning/power-budget-non-issue"
---

# Battery and power management as a second specialization, interlocked with positioning

## What I did

While working on locations I **double-majored in battery and power management**, and the two turned out to be one subject rather than two. On a cellular emergency-response wearable, every positioning decision is a power decision and most power decisions are positioning decisions, because the same few mechanisms — what wakes the application processor, how often the device talks to the network, and how long a radio stays on — drive both.

**Where the interlock actually lives, mechanically.** The clearest instance is the device's sync cadence. The fallback breadcrumbing interval was specified *in units of MQTT keep-alive intervals* — either a count of major syncs between fallback locations, or a number of seconds constrained to be a multiple of the keep-alive interval — for power-efficiency reasons: a location report that rides an existing network wake-up is nearly free, and one that does not costs a modem wake-up of its own. Getting that coupling right is worth more than any amount of tuning downstream of it. The same reasoning runs through the beacon work: keeping devices in low-power presence detection rather than high-frequency polling is a positioning design that exists to protect battery.

**What I acquired is an intuition for what eats battery and what does not.** Much of it is specific to the Qualcomm MDM-class SoCs used in these two device generations — which positioning methods the modem can serve on its own versus which require the application processor to participate, what the fused-location path on the modem processor costs, how much waking the AP costs in milliamps compared to running a low-power MCU continuously, whether the Wi-Fi/BLE combo part can scan for specific beacons and wake the AP only when a status changes, what cellular power-saving modes such as eDRX do to location performance, and how wakelocks let software hold the whole SoC awake by accident. Much of the rest is general and transfers to any battery-powered connected device:

- **Capable hardware costs power twice** — once for the part, and again for the software that uses it.
- **The wake-up chain should start as low in the stack as possible**: sensor, then MCU, then modem, then AP. Every level you climb multiplies the cost.
- **The battery budget is decided before the form factor**, not inherited from an enclosure, so it stays a researchable constraint.
- **A power claim without a measurement is an opinion.** Charger-current data, engineering builds and device soak tests are how a claim becomes a number.

**What the intuition was for.** Product management and the wider business extended team were repeatedly preoccupied with battery life — sometimes rightly, sometimes not — and the useful contribution was to say early which proposals would move battery life and which would not. In recent years those judgements have been consistently right. The method is a stated hypothesis plus a cheap experiment rather than a brute-force analysis campaign: an engineering build, a small set of devices soaking, a notebook, and an answer in days. That saved a great deal of crude quasi-statistical effort that would have produced a weaker answer more slowly. The analytical half of that practice is its own entry — see *Related*.

**Recent, concrete instances (2026).** A keep-alive production-configuration build: reconstructing the accumulated business rules around major sync, deciding the approach, implementing it, publishing a notebook from the engineering build, and soaking devices to confirm the effect on battery life. In the same period, an ODM ticket to remove a Wi-Fi-positioning EULA behaviour on the grounds that it might also help battery life, and an offer to run the battery-life experiments for the following maintenance release.

## Why it matters

Battery life on this product is not a specification to satisfy; it is the thing that decides whether a senior wears the device at all, and whether it is charged when a fall happens. Owning the power question alongside positioning meant the two were never traded against each other by default: the standing design goal was that **positioning be a non-issue in the power budget**, and the architecture was then built to satisfy it rather than to apologize for it. It also made me useful in a specific, repeatable way to people outside engineering — able to answer "will this cost us battery?" before a quarter had been spent finding out.

## Skills demonstrated

Embedded power management and power budgeting; Qualcomm MDM-class modem/AP platform behaviour; low-power positioning architecture; MQTT keep-alive and sync-cadence design; wakelock discipline; measurement design (engineering builds, device soak tests, charger-current data, notebooks); hypothesis-first experiment design; translating an engineering constraint into terms product management and business partners can decide with.

## What was blocked, cut short, or wrong

Recorded deliberately — the wins only mean something next to these.

- **A proposal to add a second positioning timeout and measure accuracy against battery got no traction** at the time. My note from the period says it "landed on deaf ears". The idea was to make the accuracy-versus-battery trade-off measurable rather than argued; it was not taken up.
- **MCU-based positioning was not obviously a power win.** Early in the dead-reckoning research I recorded that backend needs and other reasons to run the application processor might mean MCU-based positioning could not actually reduce the power budget — in which case prototyping should be cut short rather than continued for its own sake. That is a negative result I reached and acted on, not one I was handed.
- **A cellular-hotspot capability was argued down on battery grounds**, as something that "will kill our battery budget". The right call, but it is a refusal rather than a delivery.
- **The 2026 keep-alive production refactoring broke beacon tracking**, which I found myself and which cost the ticket its estimate. I had argued for keeping beacon tracking simple, and that decision is what kept the breakage cheap to fix.

## Evidence

The owner's own device-programme board carries the power-budget list, the trade-off cards ("Battery Budget vs. Hardware Budget", "Form Factor vs. Battery size"), the vendor question set on modem-side positioning and power-saving modes, and the sprint-level record of the 2026 keep-alive build and soak testing. The leadership board carries the one-on-one and mentor threads in which the power budget, the blocked timeout proposal and the battery-life sprint goal were discussed, plus a conference-talk idea on levelling up battery life with MCU power modes that sets out the milliamp argument. Those boards are the committed Trello snapshots. The keep-alive production change itself is a merged pull request.

## Evidence limitations

- **"Consistently right in recent years" is the owner's own assessment.** No before/after battery measurements are committed here, and none of the judgement calls has an independent record of having been validated.
- **The Qualcomm-specific half of the intuition is uncorroborated by anything outside the owner's notes** — it is real working knowledge, but it is knowledge, not an artifact.
- The *interlock* claim, by contrast, is well supported: the sync-cadence specification, the power-budget goal for positioning, and the beacon presence-detection design are all documented.

## Related

- [2021-11-15-r5-product-architecture-power-budget-tradeoffs](2021-11-15-r5-product-architecture-power-budget-tradeoffs.md) — the origin: the argument that the battery budget must be decided before the form factor. This entry is the standing expertise that argument started.
- [2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture](2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) — the architecture built to satisfy the power goal, and where the MCU-versus-AP power question was researched.
- [2026-09-01-r5-beacon-tracking-fota-persistence](2026-09-01-r5-beacon-tracking-fota-persistence.md) — presence detection over polling, the positioning decision made for battery reasons.
- [2026-05-17-statistical-bar-and-data-science-partnership](2026-05-17-statistical-bar-and-data-science-partnership.md) — the analytical half of the same practice: hypothesis and cheap experiment over brute-force analysis.
- [2024-01-04-cellular-cost-rogue-device-detection](2024-01-04-cellular-cost-rogue-device-detection.md) — the other half of the operating-cost story, where cellular data rather than battery is the resource being spent.

## Record history

- 2026-09-13: created from the owner's direct statement of 2026-09-13, grounded the same day in the committed Trello snapshots. Filed at the start of the documented range, per the convention for a standing practice.
- 2026-09-13: graduated into story `positioning/power-budget-non-issue`; `storied` property added, body untouched.
