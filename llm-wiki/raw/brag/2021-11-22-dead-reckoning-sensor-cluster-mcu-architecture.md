---
title: "Defined the dead-reckoning and sensor-cluster architecture for the next-generation wearable, and ran the hardware evaluation behind it"
date: "2021-11 to 2022-01"
thread: DEV
domains:
  - "embedded and safety-critical devices"
  - "positioning and location"
  - "architecture and API design"
context: "Best Buy Health, R5 senior-care wearable, embedded architecture and R&D"
sensitivity: private-repo
resume-worthy: yes
storied:
  - "positioning/power-budget-non-issue"
---

# Defined the dead-reckoning and sensor-cluster architecture for the next-generation wearable, and ran the hardware evaluation behind it

## What I did

The next-generation wearable needed to know where its user was — indoors, outdoors, and in the gaps between — without the positioning subsystem dominating a battery budget that had not yet been set. I ran the research and architecture work that answered how, from first principles through to a component shortlist and a working evaluation programme.

**Wrote the dead-reckoning implementation blueprint.** The design put a low-power sensor cluster and a dedicated BLE MCU between the sensors and the application processor, so the AP could stay asleep:

- The accelerometer/gyroscope cluster (LSM6DSOX) raises *significant motion detection* whenever the user starts moving, with output data rate and detection parameters tunable to trade power against false positives.
- Significant motion wakes the BLE MCU (STM32WB5MMG), which consumes output from the **machine-learning core embedded in the sensor itself** plus the other sensors, rather than streaming raw samples upward.
- The MCU measures distance from the cradle beacon to establish an initial fix, then maintains a relative position estimate while movement continues, periodically (every 1–5 s) recomputing an absolute position.
- During wake time it can surface beacon loss, fall detection and fall-risk signals to the AP when useful; dead-reckoning failure or an outdoors transition (detected via temperature, possibly light) wakes the AP so a GNSS fix can be attempted.
- By default the AP queries the MCU for the best current position estimate during an emergency event or a periodic check; GNSS fixes, when taken, are fed *back* to the MCU to correct the reckoning.

The shape of this is the point: positioning becomes a mostly-asleep, sensor-triggered subsystem that reports position on demand, instead of a continuously running consumer of the power budget.

**Selected and justified the component lineup.** Focused on LSM6DSOX for motion, step and fall detection; LPS22HH barometer for stair ascent/descent and fall discrimination; LIS2MDL magnetometer for heading and for correcting gyroscope precession; a temperature sensor for the outdoor-transition signal; and a GNSS module in the cradle. Evaluated the STM32WB family across value-line, full and module variants, weighing pinout flexibility, memory size, certification status and the option to prototype on a certified module and move to a chip-down design later.

**Ran the vendor engagement and the evaluation programme.** Worked with the component vendor and their field engineers, drove an on-site/technical meeting series, and specified the discovery hardware the team needed to answer open questions empirically — discovery kits, a programmable power-supply source with power-measurement capability for current-consumption work, a sensor tile for free-fall testing, pressure-sensor breakout, BLE test dongles and RF tooling. Set out the specific experiments each purchase was meant to settle.

**Framed the open questions as experiments, not opinions.** Whether built-in fall/tilt/orientation detection could be consumed as-is; whether sensor fusion could be offloaded to the vendor and how that would interact with the application processor's sensor requirements; what the ultra-low-power mode actually costs in accelerometer RMS noise (roughly double, 5 mg vs 2.5 mg); whether RAM-hungry buffering was viable on the power budget; how much latency waking a deep-sleeping processor would add.

**Assessed the incumbent path in parallel.** Investigated BLE support on the existing application processor by digging into the previous generation's BLE application — building it, tracing its advertising and scanning paths, working out how scan interval and window were parameterized, and reading the commit history back to its origin as a vendor reference codebase. Established what beacon tracking on the AP would actually cost, which is what made the MCU-offload argument concrete rather than theoretical.

**Kept it connected to the team.** Coordinated with the hardware side, who had boards with the same sensor cluster already, on whether the sensor hub could deliver high-level data packs to both the BLE MCU and the application processor. Circulated the blueprint for review and folded in questions from the hardware lead — position quality indicators and their categorization (precision, reliability, custom and industry-standard parameters), gyroscope precession under centrifugal force, step counting as a vector quantity, MCU-side beacon scanning, and deep-sleep wake latency.

## Why it matters

- **It set the architecture for how the device knows where it is** — an approach where positioning is triggered by motion and normally costs nothing, rather than a continuous drain, which was the difference between positioning being a feature and positioning being a battery problem.
- **It made the power budget tractable** before the industrial design was fixed, by turning "how much power does location cost?" into a set of measurable experiments with hardware on the bench.
- **It exploited on-sensor machine learning** — using the sensor's embedded ML core to classify motion, so the wake-up chain starts as low in the stack as possible.
- **It was genuinely from first principles**, spanning MEMS sensor physics, BLE radio behaviour, RF and matching-network fundamentals, MCU power modes and system-level wake-up strategy, then reduced to a component shortlist and a purchase list a team could act on.

## Skills demonstrated

Embedded systems architecture; sensor fusion and dead reckoning; MEMS sensor selection and evaluation; on-sensor machine learning; BLE and RF fundamentals; low-power design and power budgeting; multi-processor wake-up strategy; component-vendor and field-engineer engagement; hardware evaluation programme design; translating open questions into bench experiments; cross-functional coordination with hardware engineering.

## Evidence

Trello device-programme board, *Dead Reckoning*, *BLE Examples*, *Research for BLE Beaconing*, *SensorTile data collection*, *MCU Accelerometer Data Streaming* and vendor-strategy lists, 2021-11 to 2022-01: the blueprint, the component analysis, the discovery-hardware request with per-item rationale, the experiment checklists, and the AP-side BLE investigation notes. Internal ticket identifiers, wiki deep links, repository paths, vendor pricing and lead times, and the reseller's contact details remain in the board archive and are deliberately not reproduced here.

## Related

- [2026-09-01 R5 beacon tracking and FOTA persistence](2026-09-01-r5-beacon-tracking-fota-persistence.md) — the late chapter of the beacon tracking later assigned on the R5; not built on this research, and never exposed to customers.
- [2025-11-15 R5 location engine design](2025-11-15-r5-location-engine-design.md) — the eventual multi-source location engine; this entry is its distant ancestor on the sensor side.
- [2021-11-15 R5 product architecture and power-budget trade-offs](2021-11-15-r5-product-architecture-power-budget-tradeoffs.md) — the product-level framing this research fed.
- [2023-11-27-r5-home-away-beacon-tracking](2023-11-27-r5-home-away-beacon-tracking.md) — the 2023 beacon tracking assignment. Related by technology only: this research explored BLE beaconing for a different question and did not originate that feature.

## Record history

- 2026-09-10: created from the Trello device-programme board during the full board ingest.
- 2026-09-13: graduated into story `positioning/power-budget-non-issue`; `storied` property added, body untouched.
- 2026-09-14: *Related* corrected — beacon tracking did not ship to customers and was an assignment, not an outgrowth of this research; link to the 2023-11-27 entry added.
