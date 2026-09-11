---
title: "Moved into regulated medical-device engineering on Current Health's Hospital at Home platform"
date: "2024-09 to 2026 (ongoing)"
thread: MED
domains:
  - "embedded and safety-critical devices"
  - "risk management and compliance"
  - "operational excellence and observability"
  - "architecture and API design"
context: "Best Buy Health → Current Health, Hospital at Home / remote patient monitoring, Gen2 wearable"
sensitivity: private-repo
resume-worthy: yes
---

# Moved into regulated medical-device engineering on Current Health's Hospital at Home platform

> **Partial entry — more material expected.** Written 2026-09-10 from the Trello device-programme board only. The owner has said he will supply further material; this entry is the frame to enrich, not the finished record. Gaps are marked *(to supply)*.

## What I did

Best Buy Health's clinical arm was a different kind of engineering organization from the consumer wearable line — a regulated medical-device company operating under a formal quality management system, with FDA and international regulatory obligations attached to the software. Moving into it meant re-learning how to ship.

**Qualified into the quality management system.** Read, understood and signed off roughly a hundred controlled documents in the company's electronic QMS, spanning:

- **Design and change control** — control of documents and records, change control orders and their work instructions, software change control, product development significant-change assessment, implementation and release of new software features, product release.
- **Regulatory** — managing regulatory requirements for the USA, EU and Australia; FDA mandatory device reporting; vigilance reporting; advisory notices and recalls; regulatory impact assessment.
- **Quality operations** — CAPA raising and management, non-conformance handling, control of non-conforming product and concessions, material review board, complaint handling, returns, first-article inspection, receiving-goods inspection, process validation, equipment calibration.
- **Supplier and manufacturing** — supplier selection, approval, evaluation and management; supplier issue management; certificates of conformity; supplier self-assessment; distributor evaluation; supplier change documents; device master records for the Gen2 wearable; control of labelling; plastic-moulding acceptance criteria.
- **Information security** — a full policy set: information security, access control, information transfer, mobile device, patch management, information classification, change management, cryptography, physical and environmental security, secure disposal, remote access, incident management, supplier information security, and risk assessment and treatment methodology.
- **Operational work instructions** — mesh network configuration, Wi-Fi signal analysis and site survey, home-hub access-point configuration, authentication failover, incident management process, ship-mode tooling.

Also completed eleven **critical incident reviews**.

This is not a box-ticking exercise to record for its own sake: it is the difference between an engineer who has worked on consumer devices and one who can work on a regulated one, and it is directly relevant to any future medical, automotive or safety-critical role.

**Decomposed the product domain deliberately.** Framed Hospital at Home as three questions — the sensors, the alerts, and *everything that is neither sensors nor alarms nor the glue between them* — and worked each. That third category is where the unexamined complexity in a monitoring platform usually lives.

**Investigated a Gen2 firmware defect end to end.** Chased a negative-temperature condition in which a default of roughly −7 °C reached the telemetry payload and caused the platform to conclude the device was off-patient. The investigation ran from the data-gathering thread down through the payload path, examined FreeRTOS queue and timer primitives and a 510 ms timeout, and worked out whether the behaviour was inherited from the previous generation by reading the history. Pulled evidence from the observability stack and the software design specification rather than from the code alone, and used AI assistants deliberately to critique the timer and queue design across the whole path.

**Learned a new observability and cloud stack** — a different monitoring platform and cloud backend from the one used on the consumer line — including how the Gen2 device surfaces there, and used it as the evidence base for the defect work.

**Researched a BLE SDK** for the platform, continuing the Bluetooth work that runs through the whole career record.

**Brought a hardware opportunity forward.** Worked the Lively Hub opportunity into concrete proposals, including battery testing and how a collaboration with an external test lab would work.

**Built the relationships deliberately**, using shared technical documents as the occasion — the approach recorded elsewhere as phrasing collaboration opportunities as deliverables.

**Mastered Orcanos.** Became fluent in the electronic quality management and ALM system the organization runs its regulated development through — the tool where design control, requirements, change control and CAPA actually live. Knowing the QMS as a *system of record you can work in*, rather than as a set of documents you have signed, is what separates being qualified on paper from being able to move a change through a regulated process.

**Mastered the Gen2 device**, and became familiar with the rest of the platform's device range. Gen2 is where the temperature investigation above was carried out, and the depth came from that kind of end-to-end work rather than from onboarding material.

**Working knowledge of PPG** (photoplethysmography) — the optical sensing behind heart-rate and related vitals on a wearable monitor. This extends the sensor-domain record that already runs through accelerometry, gyroscopes, GNSS and BLE into clinical-grade optical measurement.

*(To supply: specific design ownership and shipped outcomes on this platform; regulatory submissions or audits participated in; the Gen2 temperature defect's resolution and its measured impact. The owner has said further material is coming, and it is expected to reinforce rather than revise the above.)*

## Why it matters

- **It is a genuine domain transition**, from consumer safety-adjacent devices into regulated medical devices, made mid-career and mid-programme. Few embedded engineers make it in that direction.
- **The QMS qualification is transferable and scarce.** Design control, CAPA, supplier management, FDA and EU regulatory process, and a full ISO-style information-security policy set are exactly what medical, automotive and industrial safety-critical employers screen for, and they are slow to acquire.
- **The negative-temperature investigation is characteristic** of the owner's strongest work: a plausible-looking default value producing a clinically meaningful wrong conclusion — that a patient is not wearing the device — traced from thread to payload rather than patched at the symptom.
- **It happened during the organization's hardest period.** This platform was divested in June 2025 and its team reduced; the work continued through it. See [Best Buy Health context](../../wiki/analysis/best-buy-health-context.md).

## Skills demonstrated

Medical-device quality management systems; **Orcanos eQMS/ALM**; ISO-style design control and CAPA; FDA, EU and Australian regulatory process; supplier quality management; information-security policy frameworks; embedded firmware debugging (FreeRTOS queues, timers, telemetry payload paths); **Gen2 wearable platform depth**; **PPG (photoplethysmography)** working knowledge; remote patient monitoring and hospital-at-home domain knowledge; Grafana and cloud-backend observability; BLE SDK evaluation; AI-assisted code critique; cross-organizational relationship building.

## Evidence

Trello device-programme board — *Hospital at Home*, *Current Health Opportunities*, and the Current Health trailing list, 2024-09 onward — including the QMS training sign-off checklist, the Gen2 temperature investigation, and the hub opportunity work. Controlled-document identifiers, the QMS tool's URLs, internal presentation links and colleague usernames remain in the board archive; the document *titles* above are generic quality-system names, not proprietary content.

## Related

- [Best Buy Health: the public record behind the private one](../../wiki/analysis/best-buy-health-context.md) — what happened to this business, and how to speak about it.
- [2023-09-30 Security patch management SOP](2023-09-30-security-patch-management-sop-and-vendor-engagement.md) — the earlier, self-initiated version of the patch-management discipline formalized here.
- [2023-08-03 Risk-management practice](2023-08-03-risk-management-practice-early-analysis.md) — risk-appetite thinking that a formal QMS makes mandatory.
- [2025-05-01 R5 device-specific failure investigations](2025-05-01-r5-device-specific-failure-investigations.md) — the same defect-tracing method on the consumer line.
- [2025-05-23 Mentorship toward Principal Engineer](2025-05-23-mentorship-principal-engineer-goal.md) — where this platform is named as the stretch goal and the intended path to Principal.

## Record history

- 2026-09-10: created from the Trello device-programme board during the full board ingest. Marked partial pending further material from the owner.
- 2026-09-10: added Orcanos mastery, Gen2 device mastery and familiarity with the wider device range, and PPG working knowledge, supplied directly by the owner. Still partial — the owner has said more is coming.
