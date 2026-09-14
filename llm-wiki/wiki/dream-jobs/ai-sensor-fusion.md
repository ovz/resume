---
title: "Next-generation AI sensor fusion"
dream-job: DJ-2
origin: owner
specialization: emerging
evidence: strong
horizon: build
fits: [embedded, positioning, ai, sensors, architecture]
status: candidate
---

# ★ Next-generation AI sensor fusion

> **Doc type:** reference · **origin: owner** — the owner's own statement, 2026-09-13: *"AI opens exciting opportunities for sensor fusion. My positioning expertise gave me unique and massive head start. Next generation of sensor fusion solution not possible in previous years is another dream job candidate."*

## The job

Designing the layer where several imperfect sensors become one trustworthy answer — position, motion, activity, a fall, a vital sign — now that learned models can carry part of the work that filters used to carry alone. In practice: an architect or principal engineer on a perception or motion-intelligence stack, deciding what runs in the sensor, what runs on an MCU, what runs on the application processor and what runs off-device at all.

## Under the Value and Impact tests

**Product line, with a visible differential.** Fall detection is what the product is chosen for, so fusion work is the feature a customer buys rather than a capability sitting behind one. A better algorithm shows up in the thing that generates revenue, and it shows up where people can see it — which is the condition the Impact test adds. Of the nine candidates this is the only one that sits at the top of every axis at once.

## Why it is a real field, and why *now*

The classical discipline is being met by a foundation-model wave aimed precisely at wearable signals. An April 2026 survey frames sensor-based activity recognition's own problems as "scarce labels, sensor heterogeneity, and poor generalization across users and contexts" — the exact three problems a wearable team hits — and argues foundation models offer "a unifying paradigm". Industrially, IMU fusion plus on-device inference is being named as the basis of "physical AI systems that can perceive, reason and act directly in the real world", with fall detection listed among the applications. The live research direction is the **hybrid**: neural components augmenting classical filtering rather than replacing it. Sources: [specializations landscape](../analysis/2026-09-13-specializations-landscape.md) §§ *Sensor fusion meets foundation models*, *Edge AI and TinyML*.

"Not possible in previous years" is accurate, and it is worth being precise about why: self-supervised pretraining on unlabelled sensor data removes the label bottleneck that made every wearable classifier a data-collection project first.

## What the record already supports

This is the strongest-evidenced candidate on the list that is also genuinely new work:

- **Eight years as the company's positioning subject-matter expert** across GNSS (GPS, GLONASS, Galileo), ECID, Wi-Fi and BLE beacons, including a major upgrade of the positioning infrastructure ([resume][primary]).
- **A sensor-fusion architecture already designed from first principles**: [a low-power sensor cluster and dedicated BLE MCU between the sensors and the application processor, using the sensor's own embedded machine-learning core to classify motion so the AP stays asleep](../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) — selected and justified against motion, fall, stair-transition, heading and gyroscope-precession requirements, with a bench-evaluation programme specified to settle the open questions.
- **Fusion pushed as far down the stack as the silicon allows**: the vendor question set from that period asks which positioning methods the modem can serve alone, what the fused-location path costs, and whether the combo radio can watch for specific beacons and wake the AP only on a change. That is hardware-aware fusion, not library integration.
- **One engine, many sources, with arbitration**: [the modular location engine unifying beacon, GPS and Wi-Fi behind per-provider interfaces with a state layer that arbitrates and falls back](../../raw/brag/2025-11-15-r5-location-engine-design.md).
- **The sensor record itself**: accelerometry, gyroscopes, GNSS, BLE and [PPG](../../raw/brag/2024-09-24-current-health-hospital-at-home-qms.md) — and [fall detection as the product's focused driver, whose next innovation he is driving](../../raw/brag/2026-09-11-fall-detection-product-driver.md).
- **Power as a co-equal constraint** — [battery and power management as a second specialization](../../raw/brag/2021-10-16-battery-power-second-specialization.md) — which is what separates someone who can ship fusion from someone who can only prototype it.
- **Machine learning as a product discipline for seventeen years**, plus neural networks already applied to senior health and safety ([resume][primary]).

## The gap, and the shortest path

**The gap is the learned half, demonstrated.** The architecture, the sensors, the power reasoning and the arbitration are all there. What is missing is a piece of work where *he* trained, adapted or evaluated a model on sensor data and can say what it beat.

Shortest path:

1. **Run the comparison he is uniquely placed to run** — a learned classifier against the classical path, on motion data, evaluated on the metrics that actually matter on a wearable: false-positive rate per day, latency to detection, and milliamps. He has the domain, the data intuition and the power measurement discipline; almost nobody in the foundation-model literature is measuring the third.
2. **Follow the hybrid, not the replacement.** His existing architecture already is a hybrid — the sensor's ML core wakes the chain, classical logic arbitrates. Naming it that way converts a design he shipped into the field's current vocabulary.
3. **Publish or present one result externally.** He has [presented an observability programme to a cross-team community of practice](../../raw/brag/2024-04-18-r5-datadog-community-presentation.md), so the format is not new; the audience would be.

## The vocabulary to foreground

Sensor fusion · multimodal · IMU and inertial · GNSS/Wi-Fi/BLE hybridization · on-device inference · sensor-embedded ML core · activity recognition · self-supervised pretraining · classical filtering with learned augmentation · power-aware perception · false-positive rate per day · edge/cloud escalation.

## Stories to tell for it

- [Positioning as a non-issue in the power budget](../stories/positioning.md) (P2) — the architecture story, told as a fusion story.
- [One engine for every location source](../stories/positioning.md) (P4) — arbitration and fallback.
- Fall detection from the R4 implementation through the sensor-cluster architecture to the innovation he is driving now — the through-line a perception team will care about most.

## How to tell if this is the one

**Ask what the fun part was.** If the answer is the architecture — where each computation belongs, what wakes what, what it costs — this is the one, and it is the same work he already does with better tools. If the answer turns out to be the model itself, that is a different career (research engineer) and needs a different, longer plan than the one above.

## Related

- [Edge AI on constrained wearables](edge-ai-wearables.md) — the deployment half of the same problem, as its own candidate.
- [Resilient and assured PNT](resilient-pnt.md) — the same fusion skill aimed at trust rather than at activity.
- [Dream-job hub](dream-job-hub.md) · [specializations landscape](../analysis/2026-09-13-specializations-landscape.md).

[primary]: ../../../markdown/Oleg.Zhylin.resume.achievements.md "Primary resume (achievements)"
