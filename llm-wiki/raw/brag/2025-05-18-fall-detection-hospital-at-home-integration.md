---
title: "Integrating fall detection and the hospital-at-home platform into one care experience"
date: "2025 (proposed and worked during the Current Health engagement; slowed 2025-05-18)"
thread: INT
domains:
  - "embedded and safety-critical devices"
  - "architecture and API design"
context: "Best Buy Health: Lively Mobile 2 (R5) fall detection and Current Health's Hospital at Home platform"
sensitivity: private-repo
resume-worthy: yes
---

# Integrating fall detection and the hospital-at-home platform into one care experience

## What I did

Two device lines sat in the same company without meeting: the consumer emergency-response wearable with **fully automated fall detection**, and the **hospital-at-home** platform with its **PPG** wearable and its own sensing, networking and alerting. The owner pushed to integrate them — Lively Mobile's fall detection, the PPG device, and the other sensors — into a single care experience.

**The duplication is the point, not the waste.** Read as a bill of materials, two wearables with overlapping radios and overlapping vitals look like redundancy to remove. Read as a care experience, the overlap is **complementary**: a second independent path to the same fact, a second radio when the first cannot reach, and a fall detected by a device the patient already wears for another reason. In a home, where there is no nurse three metres away, redundancy is the safety margin.

**The customer evidence pointed the same way.** Focus groups and other internal research showed hospital-at-home patients are *open* to a wide assortment of devices and to more elaborate protocols — the opposite of the intuition that patients want fewer things attached to them. The reason is what the setting means to them: people value recovering at their own pace, in a place they genuinely feel at home, with their authority over their own health unchallenged. A hospital's rules are restrictive for good institutional reasons; at home, the patient is willing to trade a little more equipment and a little more protocol for that autonomy.

**Status: proposed and in progress, then slowed.** On 2025-05-18 the owner's own note records: "We slowed down Fall Detection work and integration of R5 FD into Hospital at Home." It was a resource decision in a contracting organization, not a technical verdict. **Nothing shipped, so nothing about delivery is claimed** — what is claimed is the idea, the reasoning and the work.

## Why it matters

- **It is product judgement, not just engineering.** Recognising that two overlapping devices are complementary in the home and redundant in the hospital is a claim about the customer, defended with customer evidence.
- **It is the clearest example of the owner's integration instinct**, which runs through the record: GreatCall and Current Health ecosystems, manufacturer and silicon partners, regulated and consumer engineering cultures.
- **The public evidence supports the direction.** Hospital-at-home care is associated with lower mortality, lower readmissions and complications, and higher patient and caregiver satisfaction than inpatient care — see *Evidence*. The owner's argument rests on why patients accept the setting, and that is publicly documented.

## Skills demonstrated

Cross-product architecture; sensor and radio redundancy reasoning; customer research read into design decisions; remote patient monitoring domain; knowing when not to claim a result.

## Evidence

Internal: the owner's board note of 2025-05-18, and the focus-group findings — **T1, never quoted outward**; the resume rests on the public record instead.

Public, for the direction of travel:

- CMS, *Report on the Study of the Acute Hospital Care at Home Initiative* (30 Sep 2024) — <https://www.cms.gov/newsroom/fact-sheets/fact-sheet-report-study-acute-hospital-care-home-initiative>
- AHRQ PSNet — Hospital at Home reduces costs, readmissions and complications and enhances satisfaction for elderly patients — <https://psnet.ahrq.gov/innovation/hospital-homesm-care-reduces-costs-readmissions-and-complications-and-enhances>
- American Medical Association on the CMS report — <https://www.ama-assn.org/public-health/population-health/hospital-home-saves-lives-and-money-cms-report>

## Related

- [2026-09-11 Fall detection as the product's driver](2026-09-11-fall-detection-product-driver.md)
- [2024-09-24 Current Health and Hospital at Home](2024-09-24-current-health-hospital-at-home-qms.md)
- [2025-04-13 BLE SDK: breadth-first white label](2025-04-13-ble-sdk-breadth-first-white-label.md) — the other integration model, and why the two do not blend.

## Record history

- 2026-09-11: created from the owner's direct statement, with the board note and public hospital-at-home evidence.
