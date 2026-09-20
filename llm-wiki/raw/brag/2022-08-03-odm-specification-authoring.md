---
title: "Authored the ODM-facing specifications for the wearable, and ran the retrospective when the process went wrong"
date: "2022-06 to 2022-08-03"
thread: MFG
domains:
  - "architecture and API design"
  - "embedded and safety-critical devices"
  - "quality and test automation"
context: "Best Buy Health, R5 wearable, contract-manufacturer (ODM) engagement"
sensitivity: private-repo
resume-worthy: maybe
---

# Authored the ODM-facing specifications for the wearable, and ran the retrospective when the process went wrong

## What I did

The wearable was built by an outside manufacturer, which makes the specification handed to them the actual product boundary: anything not written down is either not built or built wrong, and discovered late.

**Wrote the ODM-facing specification set**, covering the sensor-hub API and architecture, the inter-process communication API the device software exposes, certificate-based device authentication, the activation flow, and the system-monitor test plan — the interfaces an outside team needs to implement against without access to our reasoning.

**Set explicit authoring principles for the documents**, which is the part that usually goes unwritten:

- **As simple as it could be**, and in *both* registers — written and spoken. A specification handed across an organizational and language boundary gets discussed verbally as much as read, and I wrote for both.
- **Distinguish hard requirements from recommendations.** Without that distinction an ODM either treats advice as binding and over-builds, or treats a requirement as advice and misses it. Making the modality explicit is the single highest-value thing in a document of this kind.

**Kept the specification honest at the level of individual words.** I corrected API documentation where the described behaviour was ambiguous about whether a call acquires or releases a wake-lock — precisely the class of detail that a manufacturer implements literally and that produces a power bug nobody can find later.

**Maintained the specification as a live artifact**, cross-referencing it against the ticket system to strike out what had already been completed, keeping the architecture board and the written specification in sync, and directing new material into a single agreed home so the ODM had one place to look.

**Ran the retrospective when it went wrong.** After the specification effort, I opened a deliberate retrospection on what had gone wrong with the ODM specification — going back through the work log and brainstorming causes rather than moving on. Making the post-mortem of one's own documentation process a scheduled item, rather than an informal grumble, is what turns a bad experience into a transferable lesson.

**Documented the working relationship itself**, not just the interfaces — how the two organizations were to work together, alongside the technical content.

**Outward alias.** The "sensor-hub API" is named after the internal "sensorhub"; outward it is the **sensor co-processor API** — see [sensitivity tiers](../../wiki/workflows/sensitivity-tiers.md) § *Public aliases for internal names*.

## Why it matters

- **The specification *is* the product when an ODM builds the device.** Ambiguity does not produce a discussion; it produces hardware that behaves differently from what was intended, found at integration.
- **Separating hard requirements from recommendations** is a small convention with an outsized effect on what an outside team actually builds.
- **Writing for speech as well as reading** is an unusual and correct instinct for cross-organizational, cross-language technical communication.
- **Retrospecting on one's own specification process** is rare; most teams retrospect on delivery and leave documentation quality unexamined.
- The wake-lock ambiguity is a concrete example of the failure mode the whole discipline exists to prevent.

## Skills demonstrated

Technical specification authoring; API and interface design documentation; ODM and contract-manufacturer engagement; requirements modality discipline; cross-organizational and cross-cultural technical communication; documentation lifecycle maintenance; retrospective facilitation; device authentication and activation flows.

## Evidence

Trello device-programme board, *ODM Documentation for R5* list (16 cards) and the related manufacturer list; the retrospective is captured on the leadership board as a dated one-on-one list from 2022-08-03 calling for a review of the work log to establish what went wrong. Document links, the manufacturer's identity, internal wiki and file-share URLs, and ticket identifiers remain in the board archive.

## Related

- [2022-02-18 C++ safety-critical embedded guidelines](2022-02-18-cpp-safety-critical-embedded-guidelines.md) — the internal engineering standards written in the same period.
- [2021-11-22 Dead reckoning and sensor-cluster architecture](2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) — the sensor architecture whose API is specified here.
- [2023-09-30 Security patch management SOP and vendor engagement](2023-09-30-security-patch-management-sop-and-vendor-engagement.md) — later work on the same vendor boundary.
- [2025-07-18 FOTA vendor escalation](2025-07-18-fota-vendor-escalation-lively-mobile2.md) — what happens when the manufacturer boundary fails under pressure.
- [2025-08-30 cross-platform SDK modularization](2025-08-30-cross-platform-sdk-modularization-pers-devices.md) — later SDK boundary work that extends the earlier manufacturer-facing API specification into reusable cross-platform libraries.

## Record history

- 2026-09-10: created from the Trello device-programme and leadership boards during the full board ingest.
- 2026-09-16: added *Outward alias* for the "sensorhub" name.
- 2026-09-19: linked the later cross-platform SDK modularization entry.
