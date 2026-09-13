---
title: "Moved into regulated medical-device engineering on Current Health's Hospital at Home platform"
date: "2024-09 to 2025-06 (hands-on from late January 2025; ended with the 24 June 2025 [divestiture](../../wiki/analysis/executive-language-glossary.md))"
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

> **Partial entry — more material expected.** Written 2026-09-10 from the Trello device-programme board only. The owner has said he will supply further material; this entry is the frame to enrich, not the finished record. Gaps are marked *(to supply)*. Enriched 2026-09-11 from both boards and the owner's statements.

## How the work came to me — earned, not assigned

The owner asked for this work for more than a year before it arrived:

- **Oct 2023** — asked for a *tour of duty to Current Health*: "still top of my mind".
- **Apr 2024** — "I grabbed a chance to put myself forward to learn current health technology."
- **Sep 2024** — the move "was promised by Mark Kauffman and Robert Smith explicitly during the last all hands"; the first Hospital at Home card on the board is dated 24 Sep 2024.
- **Nov 2024** — "I understand that we are taking over current health development": the platform's engineering was moving to Best Buy Health, and the owner was among the engineers it was trusted to.
- **Late Jan 2025** — access to the platform's source; the quarter's reflection records "a great deal of autonomy at the beginning of CurrentHealth learning paths".

That sequence is what the resume's *earned the organization's trust* rests on: a year of asking, a public commitment, then the work.

## Inside the public window

Best Buy announced the acquisition in October 2021 and sold Current Health back to its co-founder on **24 June 2025** — see [Best Buy Health context](../../wiki/analysis/employers/best-buy-health/2026-09-10-best-buy-health-2024-2026-divestiture-public-record.md). This work sits wholly inside that window, beginning nearly three years after the acquisition:

| When | What the boards record |
|---|---|
| 24 Sep 2024 | First Hospital at Home card |
| 30 Jan 2025 | Access to the platform's source |
| From 31 Jan 2025 | Orcanos Academy and trainings; "Finish Orcanos and study BLE Simulator" by late February |
| 8 Apr 2025 | Gen2 negative-temperature investigation starts |
| May 2025 | Working in the platform's design reviews; key people met across Current Health and the data team |
| 12 Jun 2025 | Gen2 kit in hand |
| 23–30 Jun 2025 | The separation: "Up to this Monday things were looking up so much!" (24 Jun); "quite a Disney ride with the Current Health separation this week" (30 Jun) |

**Record time.** Orcanos mastered inside roughly the first month, and a defect investigation on the Gen2 firmware about ten weeks after access. The resume says *record time* and states no duration.

**On when the separation was announced internally.** The owner recalls an internal announcement three to six months before the public disclosure. The boards do not show one: the note of 24 June reads as news that week. What they do show earlier is the contraction around it — the March 2025 impairment, the 9 May reorganization, and on 18 May, "We slowed down Fall Detection work and integration of R5 FD into Hospital at Home". The recollection may be of those. *(Open for the owner.)* Either way it is T1 and never goes outward.

## Integration — the part the owner relished

In the owner's words: he **"relished integration across technologies, company cultures, people cultures."** The boards bear it out:

- "Current Health and GreatCall integration is on the forefront. This will be an achievement." (Oct 2024)
- "mastering and developing joint current health and GreatCall wearables" as the route to Principal (Nov 2024); "becoming Subject Matter expert for both Current Health and GreatCall technologies" (Feb 2025).
- Moved into the platform's own Slack to reach its engineers (Mar 2025); "people are friendly" (May 2025); met key people across Current Health and the Best Buy Health data team (May 2025).
- Adopted the platform team's *bar raiser* role as his own after meeting one of its engineers who held it (May 2025).
- Integrating Lively Mobile 2's fall detection into Hospital at Home was in progress before it was slowed in May 2025 — planned, not shipped, so not claimed.

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
- **It happened during the organization's hardest period, and wholly inside the public window.** The platform was sold back to its founder on 24 June 2025 and the owner's engagement ended with it; every claim here predates that date. See [Best Buy Health context](../../wiki/analysis/employers/best-buy-health/2026-09-10-best-buy-health-2024-2026-divestiture-public-record.md).

## Skills demonstrated

Medical-device quality management systems; **Orcanos eQMS/ALM**; ISO-style design control and CAPA; FDA, EU and Australian regulatory process; supplier quality management; information-security policy frameworks; embedded firmware debugging (FreeRTOS queues, timers, telemetry payload paths); **Gen2 wearable platform depth**; **PPG (photoplethysmography)** working knowledge; remote patient monitoring and hospital-at-home domain knowledge; Grafana and cloud-backend observability; BLE SDK evaluation; AI-assisted code critique; cross-organizational relationship building.

## Evidence

Trello device-programme board — *Hospital at Home*, *Current Health Opportunities*, and the Current Health trailing list, 2024-09 onward — including the QMS training sign-off checklist, the Gen2 temperature investigation, and the hub opportunity work. Controlled-document identifiers, the QMS tool's URLs, internal presentation links and colleague usernames remain in the board archive; the document *titles* above are generic quality-system names, not proprietary content.

## Related

- [Best Buy Health: the public record behind the private one](../../wiki/analysis/employers/best-buy-health/2026-09-10-best-buy-health-2024-2026-divestiture-public-record.md) — what happened to this business, and how to speak about it.
- [2023-09-30 Security patch management SOP](2023-09-30-security-patch-management-sop-and-vendor-engagement.md) — the earlier, self-initiated version of the patch-management discipline formalized here.
- [2023-08-03 Risk-management practice](2023-08-03-risk-management-practice-early-analysis.md) — risk-appetite thinking that a formal QMS makes mandatory.
- [2025-05-01 R5 device-specific failure investigations](2025-05-01-r5-device-specific-failure-investigations.md) — the same defect-tracing method on the consumer line.
- [2025-05-23 Mentorship toward Principal Engineer](2025-05-23-mentorship-principal-engineer-goal.md) — where this platform is named as the stretch goal and the intended path to Principal.

## Record history

- 2026-09-10: created from the Trello device-programme board during the full board ingest. Marked partial pending further material from the owner.
- 2026-09-10: added Orcanos mastery, Gen2 device mastery and familiarity with the wider device range, and PPG working knowledge, supplied directly by the owner. Still partial — the owner has said more is coming.
- 2026-09-11: renamed from `2026-06-15-…`. That date came from a mistyped board card (titled "2026-06-15 - 5G010K firmware", created 12 Jun 2025) and placed the work a year after the divestiture. Re-dated to the first Hospital at Home card, 24 Sep 2024; period corrected to end June 2025. Added the trust arc, the public-window timeline, record-time evidence and the integration notes, from both boards and the owner's statements.
