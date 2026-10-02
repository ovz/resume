# Device Architecture And Delivery Coverage

> **Doc type:** reference
>
> Portfolio ownership, device features, platforms, medical devices and manufacturer delivery. Audience: brag ingest and resume promotion. [Coverage map](../coverage.md) owns totals, counting rules and shard routing; each claim below has one canonical home.

### ARC — Architecture ownership across the device portfolio

Current scope, and the most senior claim in the corpus. **No brag entry yet** — these claims come from the owner's direct statement of 2026-09-09, with a brag entry to follow. The April 2026 date is the owner's estimate and may be corrected when that entry lands.

**Entries:** *pending capture.*

**Thread coverage: 100%** (5 of 5)

| Claim | Source | Status |
|---|---|---|
| `ARC-1` Owns architecture decisions for the Wearables product line, since April 2026 | owner, 2026-09-09 | **in** |
| `ARC-2` Owns architecture decisions for the Handsets product line, since April 2026 | owner, 2026-09-09 | **in** |
| `ARC-3` Remains hands-on as an engineer across every device of GreatCall lineage still carried in the catalogue | owner, 2026-09-09 | **in** |
| `ARC-4` Uses AI-assisted rapid prototyping to become productive on an unfamiliar platform quickly | owner, 2026-09-09 | **in** |
| `ARC-5` Uses AI-assisted exploration to judge an idea's innovation potential early | owner, 2026-09-09 | **in** |

---

### FALL — Fall detection, the feature the product is chosen for

The owner's product judgement: the Care center is load-bearing, but fall detection is the focused driver. Built on R4, carried into the 2021 sensor architecture (`DEV`), and now the innovation front the owner drives as Wearables architecture owner.

**Entries:** [2026-09-11 fall detection as product driver](../../../raw/brag/2026-09-11-fall-detection-product-driver.md)

**Thread coverage: ≈ 83%** (2.5 of 3)

| Claim | Source | Status |
|---|---|---|
| `FALL-1` Identified fall detection as the product's focused driver, distinct from the load-bearing Care center | 2026-09-11 | **in** |
| `FALL-2` As Wearables architecture owner, driving the next round of fall-detection innovation for active seniors | 2026-09-11 | **in** |
| `FALL-3` Frames fall detection and Home/Away as the care the device gives without the user acting, distinct from a button that reaches a Care agent for any reason | 2026-09-11 | **partial** |

> Promoted at the owner's explicit direction on 2026-09-11, reversing the 2026-09-10 call to hold the innovation direction at T1 as roadmap. The outward wording states the direction only — no feature, sensor, algorithm or date.

---

### INT — Integration across devices, protocols and organizations

The kind of work the owner keeps being drawn to, and now a resume bullet in its own right: two device lines meeting in one care experience, a device programme meeting a contract manufacturer, a regulated culture meeting a consumer one.

**Entries:** [2025-05-18 fall detection and hospital at home](../../../raw/brag/2025-05-18-fall-detection-hospital-at-home-integration.md) · cross-listed: [2025-04-13 BLE SDK](../../../raw/brag/2025-04-13-ble-sdk-breadth-first-white-label.md) (claims under `MED`)

**Thread coverage: ≈ 88%** (3.5 of 4)

| Claim | Source | Status |
|---|---|---|
| `INT-1` Pushed to integrate Lively Mobile 2's fall detection, a PPG wearable and surrounding sensors into one hospital-at-home care experience | 2025-05-18 | **in** |
| `INT-2` Argued that overlapping radios and vitals across two wearables are complementary redundancy in a home, not waste | 2025-05-18 | **in** |
| `INT-3` Grounded it in customer evidence that patients at home accept more devices and more elaborate protocols in exchange for autonomy | 2025-05-18 | partial |
| `INT-4` Names integration across devices, technologies, companies and cultures as a recurring kind of work he is good at | 2025-05-18 | **in** |

> `INT-3` is deliberately `partial`: the resume gives the reasoning ("a home without a nurse in the next room") but not the focus-group finding behind it, which is internal research and stays at T1. Nothing shipped, so no delivery is claimed anywhere.

---

### FW — Embedded platform frameworks

**Entries:** [2024-05-08 component framework](../../../raw/brag/2024-05-08-ccf-capability-framework-lcm-open-source.md) · [2025-08-30 cross-platform SDK modularization](../../../raw/brag/2025-08-30-cross-platform-sdk-modularization-pers-devices.md) · [2025-01-16 phone capability SDK on R5 hardware](../../../raw/brag/2025-01-16-ccfphone-r5-device-lcm-odm-integration.md) · cross-listed: [2026-09-01 beacon FOTA persistence](../../../raw/brag/2026-09-01-r5-beacon-tracking-fota-persistence.md) (claims tracked under POS)

**Thread coverage: ≈ 12%** (4 of 34). `FW-20` to `FW-32` arrived 2026-09-19 from the two governing Confluence design specifications, which the owner supplied after the source study. `FW-33` and `FW-34` arrived 2026-09-21 from the owner-supplied MPERS SDK Confluence draft rendering and are bounded to strategy and requirements rather than adoption.

| Claim | Source | Status |
|---|---|---|
| `FW-1` Led design and delivery of an embedded component framework standardizing how device SKUs declare, configure and bring up features | 2024-05-08 | **in** |
| `FW-2` Implemented dependency injection and hierarchical state machines with predictable lifecycle management in embedded C | 2024-05-08 | **in** |
| `FW-3` Built an aligned structured-logging framework giving consistent logs across all supported devices | 2024-05-08 | **in** |
| `FW-4` Modularized and documented the framework for open-source release and external contribution | 2024-05-08 | **in** |
| `FW-5` Co-authored cross-platform SDK C-library requirements covering ANSI C compatibility, minimal dependencies, predictable memory usage and separation between core SDK and ODM integrations | 2025-08-30 | absent |
| `FW-6` Separated platform-agnostic capabilities from Linux- and MCU-specific adapters so core SDK libraries could be reused across targets | 2025-08-30 | absent |
| `FW-7` Defined stable public C headers and library boundaries for capability and configuration APIs consumed by ODMs and internal teams | 2025-08-30 | absent |
| `FW-8` Organized SDKs as versioned static or dynamic libraries for distribution through existing artifact repositories | 2025-08-30 | absent |
| `FW-9` Aligned the modular SDK architecture with future CCF adoption and identified R5 source areas for extraction into reusable components | 2025-08-30 | absent |
| `FW-10` Built the first capability SDK on the component framework and ran it on production-class R5 hardware | 2025-01-16 | absent |
| `FW-11` Split the system into a company-owned application process and a manufacturer-owned service process, matching the software boundary to the organizational one | 2025-01-16 | absent |
| `FW-12` Used the open-source LCM (Lightweight Communications and Marshalling) publish/subscribe library over three named channels carrying commands, events and the manufacturer service's log records | 2025-01-16 | absent |
| `FW-13` Published the manufacturer-facing C API as a header marked in the source as distributed outside the company | 2025-01-16 | absent |
| `FW-14` Modelled call handling with mobile-originated/terminated direction, a distinct in-service emergency state, a full call-state machine and 3GPP call-end reason codes | 2025-01-16 | absent |
| `FW-15` Separated recoverable from fatal errors so the phone keeps operating when the SDK's own logic fails, with re-initialization documented as recovery | 2025-01-16 | absent |
| `FW-16` Cross-compiled to a Qualcomm MDM9607 ARM target through an OpenEmbedded toolchain with the device sysroot pinned as a submodule | 2025-01-16 | absent |
| `FW-17` Containerized the device build and deployed to hardware over adb, with build-time version provenance stamped from git | 2025-01-16 | absent |
| `FW-18` Covered the real inter-process path with GoogleTest integration tests that subscribe to live channels and publish JSON commands under bounded timeouts | 2025-01-16 | absent |
| `FW-19` Named the submodule-based dependency model as debt in the repository's own README, calling for a package manager instead | 2025-01-16 | absent |
| `FW-20` Framed the SDK strategy as injecting the company's own code into the manufacturer's process, replacing specification documents that cost both sides effort outside their core expertise | 2025-08-30 | absent |
| `FW-21` Set an asymmetric binary policy — manufacturers link dynamic shared objects so SDK behaviour can be upgraded without recompiling their code, while in-house code links static libraries for private-header access | 2025-08-30 | absent |
| `FW-22` Grounded that decision in the Qualcomm/Skyhook integration, where not having to recompile the location service made unplanned fixes deployable | 2025-08-30 | absent |
| `FW-23` Separated public from private headers so manufacturer code is insulated from in-house implementation details | 2025-08-30 | absent |
| `FW-24` Identified reusable location-fix quality comparison as the shared-library core of a capability, so logic previously re-implemented per device could be owned once and varied where needed | 2025-08-30 | absent |
| `FW-25` Set ANSI C as the default with conservative use of newer ISO C, so libraries stay compilable unchanged for restricted MCU targets | 2025-08-30 | absent |
| `FW-26` Required an automated test suite covering all functionality, with unit tests carrying a code-coverage metric | 2025-08-30 | absent |
| `FW-27` Specified a reusable memory pool to satisfy a no-dynamic-allocation constraint, drawing on C++17 polymorphic memory resources for industry-standard patterns | 2024-05-08 | absent |
| `FW-28` Proposed the SDK take over wakelock management, naming manufacturer wakelock misuse as a known defect source and wakelocks as fundamental to location and audio | 2024-05-08 | absent |
| `FW-29` Argued flat state machines grow exponentially with emergency-device scenarios, making hierarchical state machines a requirement rather than a preference | 2024-05-08 | absent |
| `FW-30` Ran a build-versus-buy evaluation against the commercial QP/C real-time embedded framework, pricing its licence plus team learning and a proof of concept, and built the hierarchical state machine in-house instead | 2024-05-08 | absent |
| `FW-31` Made the case for the LCM messaging library over D-Bus marshaling — publish/subscribe, a robotics track record, recordable and replayable messages, portability without UDP — including rewriting existing Boost signal buses while preserving their nomenclature | 2024-05-08 | absent |
| `FW-32` Specified an on-device integration-and-validation test executable so firmware could be validated automatically and manufacturer issues pinpointed | 2024-05-08 | absent |
| `FW-33` Helped define reusable SDK requirements and platform-abstraction concepts intended to support current and future PERS wearable generations, including R6-class planning | 2025-08-30 | absent |
| `FW-34` Framed common embedded services and shared SDK architecture as a way to reduce future platform-migration and maintenance risk rather than optimizing only for one product release | 2025-08-30 | absent |

---

### DEV — Device architecture and sensor research (2021–2022)

The R&D layer under the wearable programme: what the device should be, what it should cost in power, and how it would know where its user was. Captured 2026-09-10 from the owner's own working boards, years after the fact.

**Entries:** [2021-11-15 product architecture and power budget](../../../raw/brag/2021-11-15-r5-product-architecture-power-budget-tradeoffs.md) · [2021-11-22 dead reckoning and sensor cluster](../../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md)

**Thread coverage: 100%** (8 of 8)

| Claim | Source | Status |
|---|---|---|
| `DEV-1` Wrote the dead-reckoning blueprint placing a low-power sensor cluster and dedicated BLE MCU between sensors and application processor, so the AP stays asleep | 2021-11-22 | **in** |
| `DEV-2` Used the machine-learning core embedded in the sensor itself to classify motion, starting the wake-up chain as low in the stack as possible | 2021-11-22 | **in** |
| `DEV-3` Selected and justified the sensor and MCU lineup against motion, fall, stair-transition, heading and gyroscope-precession requirements | 2021-11-22 | **in** |
| `DEV-4` Ran the component-vendor engagement and specified a bench-evaluation programme, turning open architecture questions into measurable experiments | 2021-11-22 | **in** |
| `DEV-5` Argued the battery budget must be decided before the form factor, making it a researchable constraint rather than one inherited from an enclosure | 2021-11-15 | **in** |
| `DEV-6` Made the battery-versus-hardware trade-off structure explicit, including that capable hardware costs power twice — once for the part, once for software that uses it | 2021-11-15 | **in** |
| `DEV-7` Set the design goal that positioning be a non-issue in the power budget, which the sensor architecture was then built to satisfy | 2021-11-15 | **in** |
| `DEV-8` Holds power budgets to the industry standard of care — duty-cycle-weighted average current from the right datasheet rows, component behaviour observed on discovery hardware, estimates confirmed by measurement | 2021-11-15 | **in** |

---

### MED — Regulated medical devices (Current Health)

The mid-career transition from consumer safety-adjacent devices into a regulated medical-device organization. **Partial capture** — the owner has said more material is coming, and supplied a first tranche (`MED-6`–`MED-8`) on 2026-09-10 and a second (`MED-9`–`MED-11`) on 2026-09-11, when the entry was also re-dated to sit inside the public window.

**Entries:** [2024-09-24 Current Health and Hospital at Home](../../../raw/brag/2024-09-24-current-health-hospital-at-home-qms.md)

**Thread coverage: ≈ 96%** (12.5 of 13)

| Claim | Source | Status |
|---|---|---|
| `MED-1` Qualified into a medical-device quality management system, covering design control, CAPA, supplier quality and product release | 2024-09-24 | **in** |
| `MED-2` Works under FDA, EU and Australian regulatory process including mandatory device reporting, vigilance, and advisory notices and recalls | 2024-09-24 | **in** |
| `MED-3` Operates under a full ISO-style information-security policy set — access control, cryptography, patch management, incident response, supplier security | 2024-09-24 | **in** |
| `MED-4` Traced a firmware defect in which a default temperature value reached the telemetry payload and caused the platform to conclude a patient was not wearing the device | 2024-09-24 | **in** |
| `MED-5` Made a domain transition into remote patient monitoring and hospital-at-home mid-career, learning a new observability and cloud stack with it | 2024-09-24 | **in** |
| `MED-6` Mastered Orcanos, the eQMS/ALM the regulated development process runs through, rather than only signing off its documents | 2024-09-24 | **in** |
| `MED-7` Mastered the Gen2 wearable and became familiar with the wider device range | 2024-09-24 | **in** |
| `MED-8` Added working knowledge of PPG (photoplethysmography) to a sensor record already covering accelerometry, gyroscopes, GNSS and BLE | 2024-09-24 | **in** |
| `MED-9` Earned the organization's trust to be given the Hospital at Home work, after asking for it for more than a year | 2024-09-24 | **in** |
| `MED-10` Mastered Orcanos and a PPG wearable in record time, wholly inside the public window of the platform's ownership | 2024-09-24 | **in** |
| `MED-11` Relished the integration across technologies, company cultures and people | 2024-09-24 | **in** |
| `MED-12` Distinguishes breadth-first white-label integration from ground-up device engineering by their exits — replace the vendor, or fix it in-house — and why a hybrid, having neither, destabilizes care provider and vendor alike | 2025-04-13 | **in** |
| `MED-13` Held an observer role on the BLE SDK initiative rather than claiming a model he was watching | 2025-04-13 | partial |

---

### MFG — Manufacturer boundary and firmware delivery

Where the device stops being ours: the specification handed to a contract manufacturer, and what happens when firmware delivery through that boundary fails.

**Entries:** [2022-08-03 ODM specification authoring](../../../raw/brag/2022-08-03-odm-specification-authoring.md) · [2023-09-01 ODM transition](../../../raw/brag/2023-09-01-r5-odm-transition.md) · [2026-09-11 hardware cadence](../../../raw/brag/2026-09-11-hardware-cadence-engineer-to-engineer.md) · [2025-07-18 FOTA vendor escalation](../../../raw/brag/2025-07-18-fota-vendor-escalation-lively-mobile2.md)

**Thread coverage: 100%** (13 of 13)

| Claim | Source | Status |
|---|---|---|
| `MFG-1` Authored the manufacturer-facing specification set — sensor co-processor API, IPC API, device authentication, activation flow, process-supervisor test plan | 2022-08-03 | **in** |
| `MFG-2` Set authoring principles separating hard requirements from recommendations, and wrote for spoken as well as written use across an organizational and language boundary | 2022-08-03 | **in** |
| `MFG-3` Ran a deliberate retrospective on his own specification process after it went wrong, rather than treating documentation quality as unexaminable | 2022-08-03 | **in** |
| `MFG-4` Became the firmware-over-the-air subject-matter expert in record time to change the balance of a vendor negotiation during an inventory crisis | 2025-07-18 | **in** |
| `MFG-5` Drove a resolution adequate to the business while naming its engineering cost — fifty-plus brittle test protocols — as technical debt at the moment it was incurred | 2025-07-18 | **in** |
| `MFG-6` Held a team steady through an all-hands escalation, keeping QA engineers productive and stakeholder confidence intact while the fix was found | 2025-07-18 | **in** |
| `MFG-7` Instrumental in transitioning Lively Mobile 2 to a new contract manufacturer mid-programme | 2023-09-01 | **in** |
| `MFG-8` Observability built for cost-of-operation reasons became the evidence base that made the new build's behaviour verifiable rather than arguable | 2023-09-01 | **in** |
| `MFG-9` Held the conservative engineering call and the customer outcome as one call rather than a trade | 2023-09-01 | **in** |
| `MFG-10` Mastered hardware's rigid cadence — six months or more per new hardware and industrial design, agility in the pre-planning — alongside iterative software | 2026-09-11 | **in** |
| `MFG-11` Got the best results from engineer-to-engineer relationships across manufacturer, silicon and firmware partners | 2026-09-11 | **in** |
| `MFG-12` Treats the Agile Manifesto as the framework that makes engineer-to-engineer practice a transferable skill | 2026-09-11 | **in** |
| `MFG-13` Brought the programme back to a regular hardware/software development lifecycle after the manufacturer transition | 2023-09-01 | **in** |

---

### SHELF — Devices sold off the retail shelf

The product end of the device work: two generations of the owner's devices sold in national retail stores, the display space they earned, and what seeing them there meant to him. Opened 2026-10-01.

**Entries:** [2019-04-23 Lively devices on Best Buy shelves](../../../raw/brag/2019-04-23-lively-devices-on-best-buy-shelves.md)

**Thread coverage: ≈ 79%** (5.5 of 7)

| Claim | Source | Status |
|---|---|---|
| `SHELF-1` Builds software for devices sold as retail products, across two generations (Lively Mobile+ from 2019, Lively Mobile 2 from 2024) | 2019-04-23 | **in** |
| `SHELF-2` Lively Mobile+ was sold in Best Buy and Walmart stores from its 2019 launch (CPSC record) | 2019-04-23 | **in** |
| `SHELF-3` Best Buy gave Lively dedicated display space: two aisle endcaps in 2020, most of a store's main prepaid display by 2021 (Wave7 Research) | 2019-04-23 | **in** |
| `SHELF-4` Part of a service with more than 900,000 paying subscribers at the 2018 acquisition | 2019-04-23 | **in** |
| `SHELF-5` Visited stores, watched customers try the device, and talked about the work with associates and a store general manager | 2019-04-23 | **in** |
| `SHELF-6` The display stood on the store's front line beside Apple, Amazon and Google (owner's observation; resume says "among the major brands") | 2019-04-23 | partial |
| `SHELF-7` Confirmed about a million active lines of service in the enterprise data warehouse (internal figure; tier decision pending) | 2019-04-23 | absent |
