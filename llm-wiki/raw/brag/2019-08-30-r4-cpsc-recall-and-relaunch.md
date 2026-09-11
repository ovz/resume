---
title: "Instrumental in getting Lively Mobile+ through the August 2019 CPSC recall and relaunch"
date: "2019-08-30 (CPSC recall date; the response ran through 2019)"
thread: CRISIS
domains:
  - "embedded and safety-critical devices"
  - "data engineering"
  - "quality and test automation"
  - "leadership, management, hiring"
context: "GreatCall, Lively Mobile+ (R4, public model number GCR4)"
sensitivity: private-repo
resume-worthy: yes
---

# Instrumental in getting Lively Mobile+ through the August 2019 CPSC recall and relaunch

## What I did

In the owner's words: **"I was instrumental in getting through this recall."** It was a crunch, and the formative event of the GreatCall years.

On August 30, 2019 the U.S. Consumer Product Safety Commission announced a recall of the Lively Mobile+ emergency-response device (see *The public record* below). Product quality stopped being a workstream and became the business, on a device whose whole purpose is to work when someone's life depends on it.

**Made the response tractable with data.** Existing tooling could not answer, at fleet scale, which devices were affected or whether a fix had taken. The owner's **data engineering** on device and server-side telemetry turned that from argument into measurement — and the analysis outlived the recall, changing how the product was maintained through the relaunch and the adoption phase that followed.

**Learned how an event like this is actually handled, at every level.** The lasting value the owner calls out is not the fix but having seen a whole company — engineering, quality, operations, supply chain, customer care and executives — coordinate under a hard deadline with customer safety at stake. It is a template he has drawn on since, including on the later manufacturer transition for Lively Mobile 2.

**GreatCall's C-suite was notably transparent throughout**, which is what made that learning possible: the reasoning behind decisions was visible to engineers rather than arriving as instructions. Worth recording as a contrast case — an organization behaving well under pressure, and what that buys.

*(To supply: the owner's specific scope and deliverables in the response; who else carried it.)*

## The public record

Read 2026-09-10 from CPSC's recalls API and from the Wayback copy of the notice; both agree.

| Field | CPSC record |
|---|---|
| Recall number | 19-775 (*Fast Track Recall*; listed as a *Recall Alert*) |
| Recall date | August 30, 2019 |
| Product | Lively Mobile Plus Emergency Alert Devices, model GCR4, manufactured January–April 2019 |
| Hazard | "The call button can fail when pushed by the consumer in an emergency." |
| Units | About 44,300 |
| Incidents/injuries | None reported |
| Remedy | "Consumers should immediately stop using Lively Mobile Plus and contact GreatCall to receive a full refund. GreatCall is contacting all known purchasers directly." |
| Sold | Best Buy and Walmart stores and online, April–May 2019 |
| Importer | GreatCall Inc., of San Diego, California; manufactured in China |

*Fast Track* is CPSC's programme for a firm that reports a hazard and commits to a remedy quickly — the public record of a response that moved fast, which is the context the owner's role sits in.

## Why it matters

- **Crisis experience on a safety-critical device, on the public record.** Scarce, and exactly what a hiring manager for a regulated or safety-adjacent role wants evidence of — and verifiable by anyone, because the notice is public.
- **The origin of the data-engineering position** the owner held for years afterwards: telemetry-driven maintenance became normal on that product because of this work.
- **It anticipates the later observability programme** — the same instinct, making the fleet answerable to a question, at much greater scale in 2023–2025.

## Sensitivity

**The recall itself is public** (confirmed by the owner, 2026-09-10, with the CPSC notice) and may be named at T0, linked to a pinned snapshot of the notice. What stays out of every outward document: root cause, internal decision-making, and anything not in the CPSC record. The claim that goes outward is the owner's role, not a narrative of the defect.

## Evidence

- CPSC notice — live: <https://www.cpsc.gov/Recalls/2019/GreatCall-Recalls-Lively-Mobile-Plus-Emergency-Alert-Device-Due-to-Risk-of-Call-Button-Failing-in-an-Emergency-Recall-Alert>
- CPSC notice — Wayback snapshot, pinned: <https://web.archive.org/web/20260517183859/https://www.cpsc.gov/Recalls/2019/GreatCall-Recalls-Lively-Mobile-Plus-Emergency-Alert-Device-Due-to-Risk-of-Call-Button-Failing-in-an-Emergency-Recall-Alert>
- CPSC recalls API query that returned the record: <https://www.saferproducts.gov/RestWebServices/Recall?format=json&RecallTitle=GreatCall>

No Wayback capture from 2019 exists; the 2026-05-17 snapshot is the earliest available and is recorded per the repo's link conventions, which prefer a recent pinned capture to a live URL.

## Related

- [2023-12-21 Device-health observability architecture](2023-12-21-device-health-observability-architecture.md) — the same instinct at fleet scale, four years later.
- [2023-09-01 Lively Mobile 2 manufacturer transition](2023-09-01-r5-odm-transition.md) — the next time the whole-company template was needed.
- [Best Buy Health context](../../wiki/analysis/best-buy-health-context.md) — the organizational arc this sits at the start of.

## Record history

- 2026-09-10: created from the owner's direct statement as `2019-06-01-r4-quality-crisis-and-relaunch`, date approximate and the recall's public status unconfirmed.
- 2026-09-10: owner confirmed the recall is public and supplied the CPSC notice. Re-dated to the recall date and renamed; public record read from CPSC's API and the Wayback copy and tabulated; sensitivity settled.
