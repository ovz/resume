---
title: "Resilient and assured PNT"
dream-job: DJ-3
origin: suggested
specialization: established
evidence: strong
horizon: now
fits: [positioning, embedded, architecture, sensors, vendor]
status: candidate
---

# ○ Resilient and assured PNT

> **Doc type:** reference · **origin: suggested** — proposed by an agent on 2026-09-13 from this repository's positioning record plus outside research. Not the owner's idea; he has not weighed in.

## The job

Position, navigation and timing that keeps working when GNSS cannot be trusted — jammed, spoofed, or simply absent. The work is architecture: multiple independent sources, an arbitration layer that decides which to believe, inertial and timing holdover while the trusted source is gone, and an honest account of accuracy degradation over time. Employers are avionics, maritime, defence, autonomy, critical timing infrastructure, and increasingly ordinary civil products that have discovered their location stack has no fallback.

## Under the Value and Impact tests

**Product line.** In avionics, maritime, defence and autonomy, PNT is the product or a certified part of it — never an internal service — so the differential is measured by the customer rather than by an internal dashboard. It is also a market where the buyer already knows the problem is hard, which is the condition under which technical power gets funded rather than negotiated.

## Why it is a real field

The threat is cheap and routine: "cheap one-watt jammers, though illegal in most countries, are readily available on the internet" and can "defeat GNSS reception for several kilometers". The countermeasure is an architecture, not a part — controlled-reception-pattern antennas giving "20 – 50 dB of jamming protection", inertial systems disciplined by GNSS while it is trustworthy and carrying the solution when it is not, multi-constellation receivers, atomic-clock holdover. Sources: [specializations landscape](../analysis/2026-09-13-specializations-landscape.md) § *Resilient and assured PNT*.

## What the record already supports

Unusually direct, once the vocabulary is translated:

- **Company subject-matter expert on positioning** across GNSS, ECID, Wi-Fi and BLE — a genuinely multi-source record, not a GPS record ([resume][primary]).
- **The arbitration layer already built**: [per-provider interfaces with a state-management layer that arbitrates between sources and falls back cleanly when one fails](../../raw/brag/2025-11-15-r5-location-engine-design.md). That is the core of a resilient-PNT design, shipped on a consumer wearable.
- **Failure behaviour treated as the design problem**: [root-causing a positioning library losing the fix, finding the recovery step the fallback path was missing, and reinterpreting an error counter as a proxy for *time without a fix*](../../raw/brag/2024-05-15-skyhook-positioning-root-cause-diagnostics.md). Time-without-fix is exactly the assured-PNT metric.
- **Dead reckoning from first principles** — [sensor and MCU selection justified against heading and gyroscope-precession requirements](../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) — which is the inertial half of the discipline.
- **Silicon-partner fluency**: the vendor question set on what the modem can serve alone, and [the engineer-to-engineer practice across silicon and firmware partners](../../raw/brag/2026-09-11-hardware-cadence-engineer-to-engineer.md).
- **Safety-critical habits and a security professional's reading of a system** — and spoofing is a security problem wearing a navigation costume.

## The gap, and the shortest path

Three named gaps, none deep: **no anti-spoofing or anti-jamming work**; **no inertial navigation at the filter level** (he specified and architected dead reckoning, he did not implement the estimator); and **no exposure to the certification regimes** of aviation or defence timing.

Shortest path: learn the threat model properly (spoofing detection signatures, the standard countermeasure stack), then re-tell the location-engine story in PNT terms — sources, arbitration, fallback, degradation — because the structure already matches and only the words are missing. A first role is more likely to be a systems or architecture seat on a resilient-PNT product than a filter-design seat, and that is the right entry anyway.

## The vocabulary to foreground

Multi-source PNT · arbitration and source selection · GNSS denial and degradation · time without a fix · fallback and graceful degradation · inertial aiding and holdover · multi-constellation · ECID and Wi-Fi positioning · power-constrained positioning · spoofing as a security problem.

## Stories to tell for it

- [The fault that lost the fix](../stories/positioning.md) (P3) — a positioning failure diagnosed from telemetry, plus the recovery gap.
- [One engine for every location source](../stories/positioning.md) (P4) — arbitration and fallback, verbatim the job description.
- [Positioning as a non-issue in the power budget](../stories/positioning.md) (P2) — for any battery-powered PNT product.

## How to tell if this is the one

Read one spoofing-detection paper and one jamming-mitigation datasheet. **If the reaction is "our fallback logic would have been fooled by that" rather than "interesting", the instinct is already there** — this candidate rewards someone who finds adversarial conditions interesting rather than annoying, and eight years of making location work on a device that must not fail is the right temperament.

## Related

- [Next-generation AI sensor fusion](ai-sensor-fusion.md) — the same fusion skill, aimed at activity rather than trust.
- [Dream-job hub](dream-job-hub.md) · [specializations landscape](../analysis/2026-09-13-specializations-landscape.md).

[primary]: ../../../markdown/Oleg.Zhylin.resume.achievements.md "Primary resume (achievements)"
