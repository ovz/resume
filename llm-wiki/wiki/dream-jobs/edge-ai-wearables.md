---
title: "Edge AI on constrained wearables"
dream-job: DJ-9
origin: suggested
specialization: emerging
evidence: moderate
horizon: build
fits: [embedded, ai, sensors, power, architecture]
status: candidate
---

# ○ Edge AI on constrained wearables

> **Doc type:** reference · **origin: suggested** — proposed by an agent on 2026-09-13 as the deployment-side counterpart to [AI sensor fusion](ai-sensor-fusion.md). Not the owner's idea.

## The job

Getting inference to run *on* a device that has milliamps and kilobytes rather than GPUs: model and memory budgets, quantization, which tier of silicon each computation belongs to, when to escalate a hard case off-device, and how to keep the whole thing inside a battery target the product was sold on. Where [sensor fusion](ai-sensor-fusion.md) is the algorithm question, this is the platform question — and the two are usually the same team.

## Under the Value and Impact tests

**Product line.** On-device inference is experienced by the customer directly — what the device notices, how fast, and how long it lasts between charges are the three things a wearable is judged on, and this work moves all three. The differential is measurable in the same units the business already uses.

## Why it is a real field

Market framing (aggregator summaries): a TinyML market around **$1.36B in 2026 heading toward ~$6.1B by 2035**, with **healthcare the largest single share (~36%)**, and a forecast of 2.5B TinyML-capable devices shipping by 2030. The pattern the field settled on in 2026 is **hybrid** — local models handle the routine, latency- and privacy-sensitive cases, and rare or hard cases escalate to larger models elsewhere. The practitioner skills are embedded skills applied to inference. Sources: [specializations landscape](../analysis/2026-09-13-specializations-landscape.md) § *Edge AI and TinyML*.

## What the record already supports

He has been doing the discipline's central move since 2021, for power reasons rather than AI reasons:

- **Inference below the application processor, deliberately**: [the sensor-cluster architecture uses the machine-learning core embedded in the sensor itself to classify motion, starting the wake-up chain as low in the stack as possible so the AP stays asleep](../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md). That is the edge-AI tiering decision, made correctly, before the term was current here.
- **The budget discipline the field keeps rediscovering**: [capable hardware costs power twice — once for the part, once for the software that uses it](../../raw/brag/2021-11-15-r5-product-architecture-power-budget-tradeoffs.md), and [an intuition for what actually eats battery on this class of SoC](../../raw/brag/2021-10-16-battery-power-second-specialization.md).
- **A memory-budget decision already made against a vendor's product**: [driving the feasibility check that ruled out a conventional monitoring agent because it did not fit the device's RAM](../../raw/brag/2023-12-21-device-health-observability-architecture.md). The same arithmetic decides whether a model fits.
- **A shipped on-device classifier in the same problem family**: [fully automated fall detection — MCU signal filtering, subsystem coordination, persistence across reboot](../../raw/brag/2026-09-11-fall-detection-product-driver.md) — plus neural networks applied to senior health and safety ([resume][primary]).
- **Component-vendor evaluation as a practice**: sensor and MCU lineups selected against stated requirements, with a bench-evaluation programme specified to settle open questions.
- **Seventeen years of ML product engineering**, so the model side is familiar ground in a different form factor.

## The gap, and the shortest path

**The gap is the modern toolchain.** Quantization-aware training, the embedded inference runtimes, and per-layer profiling on target hardware are named in no entry. He has architected *where* inference belongs; he has not personally shipped a quantized model into a constrained target.

Shortest path: take one classifier in a domain he knows cold — motion, fall, activity — and carry it end to end on real hardware, reporting the three numbers this field runs on: accuracy, latency, and current draw. He is one of few people who would instinctively report the third, which is the differentiator. The [fall-detection lineage](../../raw/brag/2026-09-11-fall-detection-product-driver.md) is the natural subject, and the innovation direction he already owns is the natural excuse.

## The vocabulary to foreground

On-device inference · TinyML and tiny deep learning · quantization · model and memory budget · inference tiering (sensor → MCU → AP) · duty cycling and wake-up chains · current draw per inference · hybrid local/cloud escalation · activity and fall classification · sensor-embedded ML core.

## Stories to tell for it

- The sensor's own ML core waking the chain — a power story that is really an edge-AI architecture story.
- [The monitoring agent that did not fit the RAM budget](../../raw/brag/2023-12-21-device-health-observability-architecture.md) — how he decides what a constrained device can host.
- Fall detection, from the original implementation to the next innovation — the product-level reason any of it matters.

## How to tell if this is the one

**Run the end-to-end exercise above and check which number you chased.** If it was current draw, this candidate is a natural extension of what he already is. If it was accuracy, [AI sensor fusion](ai-sensor-fusion.md) is the better-aimed version of the same ambition, and this page is its implementation detail rather than a separate job.

## Related

- [Next-generation AI sensor fusion](ai-sensor-fusion.md) — the algorithm side; the owner's own candidate.
- [Dream-job hub](dream-job-hub.md) · [specializations landscape](../analysis/2026-09-13-specializations-landscape.md).

[primary]: ../../../markdown/Oleg.Zhylin.resume.achievements.md "Primary resume (achievements)"
