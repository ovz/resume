---
title: "Regulated medical device software"
dream-job: DJ-6
origin: suggested
specialization: established
evidence: strong
horizon: now
fits: [regulated, embedded, medical, architecture, integration]
status: candidate
---

# ○ Regulated medical device software

> **Doc type:** reference · **origin: suggested** — proposed by an agent on 2026-09-13 from this repository's Current Health record. Not the owner's idea, though it is the direction he asked for internally and got.

## The job

Software on devices that make clinical claims: firmware or platform engineering inside a quality management system, under design control, with risk management, verification evidence and regulatory submissions as part of the definition of done. Employers are medical-device manufacturers, remote-patient-monitoring and hospital-at-home platforms, and the growing set of companies discovering that their wellness product has become a regulated one.

## Under the Value and Impact tests

**Product if the role is the device; enabler sliding to cost centre if the role is the process.** The QMS fluency is what makes him hireable here and it is also the half that reads as overhead — compliance is a cost of doing business, and a career spent on it is funded by pragmatic reasoning. The version that passes is the one where the regulated constraint sits *around* a hard technical problem he owns: a sensor, a real-time path, an algorithm making a clinical claim. Screen postings on that, not on the standards list.

## Why it is a real field

Aggregator summaries put software-as-a-medical-device near **$47B by the end of 2026 at roughly 24% CAGR**, and describe the constraint that matters here: software engineers are plentiful, but those with **five or more years in Class II/III FDA-regulated environments are scarce**, with IEC 62304 and ISO 14971 the expected stack. The same regulatory weight is what makes the role comparatively durable — the lifecycle obligations do not go away when code generation gets cheap. Sources: [specializations landscape](../analysis/2026-09-13-specializations-landscape.md) § *Regulated medical device software / SaMD*.

## What the record already supports

He holds the scarce half of that market, and recently:

- **Qualified into a medical-device QMS**, working through roughly a hundred controlled documents: design control and change control, significant-change assessment, product release, CAPA and non-conformance, supplier quality, and a full ISO-style information-security policy set — under **FDA, EU and Australian** regulatory process including mandatory device reporting, vigilance, and advisory notices and recalls ([2024-09-24](../../raw/brag/2024-09-24-current-health-hospital-at-home-qms.md)).
- **Fluency in the system the process actually runs through** — he mastered the eQMS/ALM in record time, which is the difference between being qualified on paper and being able to move a change through a regulated process ([same entry](../../raw/brag/2024-09-24-current-health-hospital-at-home-qms.md)).
- **A clinically meaningful defect traced end to end**: a default temperature value reaching the telemetry payload and making the platform conclude a patient was not wearing the device — followed from the data-gathering thread down through the payload path and RTOS primitives, and back through the previous generation to establish what was inherited ([same entry](../../raw/brag/2024-09-24-current-health-hospital-at-home-qms.md)).
- **Clinical-grade sensing**: PPG added to a sensor record already covering accelerometry, gyroscopes, GNSS and BLE.
- **Safety-critical engineering habits that predate the regulated work**: [a C++ standard chosen on what static analysis can enforce](../../raw/brag/2022-02-18-cpp-safety-critical-embedded-guidelines.md), [a NIST-grounded patch-management SOP for embedded Linux firmware](../../raw/brag/2023-09-30-security-patch-management-sop-and-vendor-engagement.md), and [risk-appetite reasoning proposed to a quality organization](../../raw/brag/2023-08-03-risk-management-practice-early-analysis.md).
- **He asked for this work for more than a year before being given it** — which is the most persuasive thing on the page, because it shows the motivation is not retrospective.

## The gap, and the shortest path

**The gaps are specific and nameable.** He has not owned a submission; the QMS experience is one organization's; and the depth is on the device and platform side rather than on verification-and-validation evidence generation, which is where much regulated hiring actually sits. IEC 62304 and ISO 14971 are the *frameworks behind* what he did, but the record shows the practice, not the standards by number.

Shortest path: name the standards explicitly wherever the practice matches them, since employers screen on the numbers; and treat the platform-integration work he pushed for — [fall detection plus a PPG wearable in one hospital-at-home experience](../../raw/brag/2025-05-18-fall-detection-hospital-at-home-integration.md) — as the architectural story, since it is the part that is his rather than the platform's.

## The vocabulary to foreground

IEC 62304 · ISO 14971 · ISO 13485 · design control and change control · CAPA and non-conformance · supplier quality · significant-change assessment · verification and validation evidence · MDR/vigilance · eQMS/ALM · RTOS firmware · remote patient monitoring · hospital at home.

## Stories to tell for it

- Earning the tour of duty by asking for a year, then qualifying into the QMS and mastering the eQMS — a story about how he enters an unfamiliar discipline.
- The default temperature value that made a platform conclude a patient was unmonitored — a debugging story with a clinical consequence, which is the exact combination this audience wants.
- [Integration as the recurring work](../../raw/brag/2025-05-18-fall-detection-hospital-at-home-integration.md), including the honest ending: proposed, worked, then slowed; nothing shipped.

## How to tell if this is the one

**Ask whether the process is interesting or merely tolerable.** He treats the QMS as a system to master rather than a tax, which is rare and is exactly what regulated employers look for. If a role promises the regulation *and* a hard technical problem — a sensor, a real-time constraint, an algorithm making a clinical claim — it passes. If the regulation is the whole job, the Innovation test fails it.

## Related

- [Rust in safety-critical embedded](rust-safety-critical.md) — the same regulatory world, aimed at where it is going rather than where it is.
- [Next-generation AI sensor fusion](ai-sensor-fusion.md) — the clinical-algorithm version of that hard problem.
- [Dream-job hub](dream-job-hub.md) · [specializations landscape](../analysis/2026-09-13-specializations-landscape.md).
