# Resume Coverage Map

> **Doc type:** reference
>
> How much of the captured brag material is actually reflected in the primary resume, tracked one claim at a time and grouped into threads. This is the page to read and think with **before** a resume pass — it says what is missing, not what to write. Audience: the owner deciding what to promote; agents drafting resume text or ingesting a brag entry.
>
> Live document: every ingest adds claims, every promotion flips a status. Statuses are judgement calls, not measurements — see *How the number is built*.

## Where it stands

| Measure | Coverage |
|---|---|
| All promotable claims | **≈ 63%** — 94 of 150 claims |
| Claims from entries marked `resume-worthy: yes` | **≈ 69%** — 68 of 98 claims |

91 claims are fully reflected. 6 are gestured at generically. 53 are absent. **Two are `held`** — recorded deliberately and never for the resume — and **one is struck** as wrong; all three are excluded from the totals above. Both figures were recounted from the tables on 2026-09-13 and adjusted by delta on 2026-09-14; the `resume-worthy: yes` line had drifted by one claim, which is the kind of drift the *Maintenance* note below expects and says to fix by recounting. The five `ARC` claims come from the owner's direct statement rather than an entry, so they count in the first row and not the second.

> **How the number got here, and what each past pass promoted, is now [coverage history](coverage-history.md)** — including the two earlier occasions when coverage *fell* while nothing was removed from the resume, which is the metric behaving correctly rather than a regression.

**What this number does not mean.** It is not a grade on the resume. The resume carries 25+ years of work, most of it from before the brag file existed and therefore invisible to this page — Salford Systems, Minitab and the pre-2023 Best Buy Health years are all well represented there and score nothing here. What the number measures is narrower: **how much of the recent, captured 2023–2026 material has reached the resume.**

## How the number is built

Each brag entry decomposes into discrete **claims**: one promotable assertion each, small enough to be either in the resume or not. Every claim gets a status:

| Status | Meaning | Weight |
|---|---|---|
| `in` | The resume makes this claim, specifically enough that a reader would take it away. | 1.0 |
| `partial` | The resume gestures at it generically — the theme is present, this specific claim is not. | 0.5 |
| `absent` | Not in the resume in any form. | 0 |

Coverage is the weighted sum over claim count. `partial` at 0.5 is deliberately crude: the point is a direction of travel, not a metric to optimize. When a promotion lands, flip the status here and mark the entry's ledger row — see *Maintenance*.

## Threads

Brag entries cluster into programmes. A thread is the unit worth thinking about during a resume pass, because a thread usually earns one resume bullet, not eight.

---

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

**Entries:** [2026-09-11 fall detection as product driver](../../raw/brag/2026-09-11-fall-detection-product-driver.md)

**Thread coverage: 100%** (2 of 2)

| Claim | Source | Status |
|---|---|---|
| `FALL-1` Identified fall detection as the product's focused driver, distinct from the load-bearing Care center | 2026-09-11 | **in** |
| `FALL-2` As Wearables architecture owner, driving the next round of fall-detection innovation for active seniors | 2026-09-11 | **in** |

> Promoted at the owner's explicit direction on 2026-09-11, reversing the 2026-09-10 call to hold the innovation direction at T1 as roadmap. The outward wording states the direction only — no feature, sensor, algorithm or date.

---

### INT — Integration across devices, protocols and organizations

The kind of work the owner keeps being drawn to, and now a resume bullet in its own right: two device lines meeting in one care experience, a device programme meeting a contract manufacturer, a regulated culture meeting a consumer one.

**Entries:** [2025-05-18 fall detection and hospital at home](../../raw/brag/2025-05-18-fall-detection-hospital-at-home-integration.md) · cross-listed: [2025-04-13 BLE SDK](../../raw/brag/2025-04-13-ble-sdk-breadth-first-white-label.md) (claims under `MED`)

**Thread coverage: ≈ 88%** (3.5 of 4)

| Claim | Source | Status |
|---|---|---|
| `INT-1` Pushed to integrate Lively Mobile 2's fall detection, a PPG wearable and surrounding sensors into one hospital-at-home care experience | 2025-05-18 | **in** |
| `INT-2` Argued that overlapping radios and vitals across two wearables are complementary redundancy in a home, not waste | 2025-05-18 | **in** |
| `INT-3` Grounded it in customer evidence that patients at home accept more devices and more elaborate protocols in exchange for autonomy | 2025-05-18 | partial |
| `INT-4` Names integration across devices, technologies, companies and cultures as a recurring kind of work he is good at | 2025-05-18 | **in** |

> `INT-3` is deliberately `partial`: the resume gives the reasoning ("a home without a nurse in the next room") but not the focus-group finding behind it, which is internal research and stays at T1. Nothing shipped, so no delivery is claimed anywhere.

---

### LEAD — Managing upward and the quarterly cycle

**Entries:** [2025-05-28 bar-raiser practice](../../raw/brag/2025-05-28-bar-raiser-practice.md) · [2021-06-23 quarterly-conversation practice](../../raw/brag/2021-06-23-quarterly-conversation-practice.md) · [2020-07-14 upward feedback](../../raw/brag/2020-07-14-upward-feedback-practice.md) · [2021-06-29 engineering excellency](../../raw/brag/2021-06-29-engineering-excellency-and-meeting-facilitation.md) · [2023-05-02 performance conversation](../../raw/brag/2023-05-02-performance-conversation-and-promotion-context.md) · [2025-04-01 Staff Engineer positioning](../../raw/brag/2025-04-01-staff-engineer-behaviors-principal-positioning.md) · [2025-05-23 mentorship](../../raw/brag/2025-05-23-mentorship-principal-engineer-goal.md)

**Thread coverage: ≈ 25%** (4 of 16 promotable; 2 held)

| Claim | Source | Status |
|---|---|---|
| `LEAD-1` Ran the employer's quarterly conversation cycle as a deliberate, prepared practice for five years unbroken | 2021-06-23 | absent |
| `LEAD-2` Carried commitments forward across quarters so each conversation started from what was agreed rather than from memory | 2021-06-23 | absent |
| `LEAD-3` Used the ritual to move scope and promotion questions rather than to report status | 2021-06-23 | absent |
| `LEAD-4` Sustained a two-way feedback practice with his manager, bringing prepared critical and positive feedback to one-on-ones rather than only responding | 2020-07-14 | absent |
| `LEAD-5` Paired every criticism with a concrete mechanism — kanbanizing a process that was Scrum in name only, naming a decision-maker, asking for an audacious team goal | 2020-07-14 | absent |
| `LEAD-6` Told a manager that self-deprecating framing suppressed rather than invited dissent, and proposed actively canvassing everyone who could contribute | 2020-07-14 | absent |
| `LEAD-7` Initiated a triage meeting and used the queue to force explicit decisions on optional engineering-quality work before it decayed into "too risky" | 2021-06-29 | absent |
| `LEAD-8` Challenged a manager for overruling an agenda in a meeting he was facilitating, arguing the systemic cost to every future meeting rather than the personal slight | 2021-06-29 | absent |
| `LEAD-9` Reframed a performance challenge from individual underperformance to organizational accountability, while conceding the one valid point | 2023-05-02 | **held** |
| `LEAD-10` Raised a contested promotion openly, arguing that promotions are decided rather than deserved and asking leadership to clarify organizational capacity | 2023-05-02 | **held** |
| `LEAD-11` Maintained a multi-year, evidence-backed self-assessment against the enterprise IC job family, including honest gaps | 2025-04-01 | absent |
| `LEAD-12` Rejected the management track on an argued principle about whose values an IC and a manager each carry | 2025-04-01 | absent |
| `LEAD-13` Ran a formal mentorship as a structured working relationship, converting live crises into named practices for confidence, humility and pausing under pressure | 2025-05-23 | absent |
| `LEAD-14` Raises the bar in whatever environment he lands in, as a stated and sustained practice | 2025-05-28 | **in** |
| `LEAD-15` Salford's outsourced Ukrainian team over-performed when the standard rose | 2025-05-28 | **in** |
| `LEAD-16` The Qt team was surprised to be asked to aim higher, then glad of it | 2025-05-28 | **in** |
| `LEAD-17` Reads which environments let a raised bar compound rather than assuming one | 2025-05-28 | **in** |
| `LEAD-18` Recognised his own philosophy in a formal *Bar Raiser* role at Current Health | 2025-05-28 | absent |

> **`LEAD-9` and `LEAD-10` are marked `held`** — deliberately never promotable, at the owner's direction. They record a performance challenge and a contested promotion, and the owner's position is that he cannot document a win against those headwinds in resume form. They stay in the brag file because they are part of the professional record; they are excluded from the coverage denominator because counting claims that will never be promoted would make the metric measure the wrong thing. The organizational context that makes this period explicable is in [Best Buy Health context](../analysis/employers/best-buy-health/2026-09-10-best-buy-health-2024-2026-divestiture-public-record.md), which is where an interview answer should draw from instead.

> Marked `resume-worthy: maybe`, and it is genuinely a judgement call: it evidences the managing-upward habit that senior scope is actually negotiated through, but it describes a practice rather than a delivery and could read as process rather than impact. Worth one clause in a leadership bullet at most.

---

### BLD — Build, packaging and engineering standards

The 2021–2022 platform-and-standards layer under the device programme: where the code lives, how it is built and versioned, and the rules it is written to. Captured 2026-09-09 from the owner's own working boards, years after the fact.

**Entries:** [2021-08-15 GitHub Enterprise migration](../../raw/brag/2021-08-15-github-enterprise-migration-monorepo.md) · [2022-02-18 C++ safety-critical guidelines](../../raw/brag/2022-02-18-cpp-safety-critical-embedded-guidelines.md) · [2022-04-06 Conan and cross-build](../../raw/brag/2022-04-06-conan-package-management-embedded-cross-build.md)

**Thread coverage: 100%** (6 of 6)

| Claim | Source | Status |
|---|---|---|
| `BLD-1` Spearheaded the organization's migration from Atlassian tooling to GitHub Enterprise, personally owning the embedded monorepo case the platform group could not take | 2021-08-15 | **in** |
| `BLD-2` Took ownership of an unowned cross-team change rather than waiting for it to be scheduled, as a deliberate and repeated pattern | 2021-08-15 | **in** |
| `BLD-3` Selected the C++ standard for a safety-critical embedded codebase on what static analysis could actually enforce, comparing MISRA C++, JSF and the Core Guidelines | 2022-02-18 | **in** |
| `BLD-4` Grounded the written guidelines in the existing static-analysis baseline so the rules are checked on every build rather than remembered by reviewers | 2022-02-18 | **in** |
| `BLD-5` Designed a Conan versioning and channel-promotion policy tying version fields to releases and pull requests, with CI-generated unique build identity | 2022-04-06 | **in** |
| `BLD-6` Established cross-compilation to the embedded ARM target, including sysroot packaging strategy and toolchain version pinning | 2022-04-06 | **in** |

---

### OBS — Device-health observability programme

The largest thread by far: eight entries spanning 2023–2025, tracing one arc from "can we even observe this fleet?" through launch monitoring, statistical tuning, and portfolio stewardship.

**Entries:** [2023-12-21 observability architecture](../../raw/brag/2023-12-21-device-health-observability-architecture.md) · [2024-01-20 telemetry schema](../../raw/brag/2024-01-20-errorsummary-json-schema-datadog-limitation.md) · [2024-03-07 monitoring launch](../../raw/brag/2024-03-07-r5-datadog-monitoring-launch.md) · [2024-04-18 community presentation](../../raw/brag/2024-04-18-r5-datadog-community-presentation.md) · [2024-05-05 anomaly tuning](../../raw/brag/2024-05-05-r5-anomaly-detection-arima-tuning.md) · [2025-01-14 lifecycle review](../../raw/brag/2025-01-14-r5-datadog-monitor-lifecycle-review.md) · [2025-05-01 device investigations](../../raw/brag/2025-05-01-r5-device-specific-failure-investigations.md) · [2025-05-29 anomaly validation](../../raw/brag/2025-05-29-r5-anomaly-monitor-validated-against-mcu-alerts.md)

**Thread coverage: ≈ 94%** (17 of 18)

| Claim | Source | Status |
|---|---|---|
| `OBS-1` Co-designed an agentless fleet-wide device-health observability architecture for a resource-constrained embedded fleet | 2023-12-21 | **in** |
| `OBS-2` Drove the vendor feasibility check that ruled out a conventional monitoring agent on RAM budget, closing a dead-end path before investment | 2023-12-21 | **in** |
| `OBS-3` Designed a wide-contract telemetry event so the schema could evolve without a firmware release | 2023-12-21 | **in** |
| `OBS-4` Diagnosed an unqueryable telemetry JSON schema and traced it to specific escaping behaviour the platform's attribute rules reject | 2024-01-20 | **in** |
| `OBS-5` Authored the array-based schema-change proposal that unblocked quantitative monitoring of the primary device health signal | 2024-01-20 | **in** |
| `OBS-6` Designed and shipped a new device's launch monitors and dashboard, becoming the team's automated alerting layer | 2024-03-07 | **in** |
| `OBS-7` Caught device and firmware issues — including a battery-overheating condition — before customer reports | 2024-03-07 | partial |
| `OBS-8` Resolved platform-level blockers directly with the observability vendor's Premier Support engineering | 2024-03-07 | **in** |
| `OBS-9` Presented the observability programme to a cross-team engineering community of practice | 2024-04-18 | **in** |
| `OBS-10` Identified a misbehaving production device live on stage during that session | 2024-04-18 | **in** |
| `OBS-11` Applied ARIMA/SARIMA theory to tune fleet-scale anomaly monitors, reasoning about the statistics rather than treating the feature as a black box | 2024-05-05 | **in** |
| `OBS-12` Established empirically that partitioning the anomaly model by error category sharply cuts false positives, and validated the hypothesis against real incident data | 2024-05-05 | **in** |
| `OBS-13` Initiated a monitor-lifecycle review, securing retirement of a superseded monitor while tying cleanup to its replacement's stability | 2025-01-14 | **in** |
| `OBS-14` Extended ownership from building monitors to stewarding the portfolio's relevance and boundaries | 2025-01-14 | **in** |
| `OBS-15` Converted broad fleet alerts into device-level investigations identifying individual units driving error activity | 2025-05-01 | **in** |
| `OBS-16` Supplied focused evidence for recovery, replacement and defect-classification decisions with firmware partners | 2025-05-01 | **in** |
| `OBS-17` Validated an anomaly monitor's first meaningful firing by correlating it with independent MCU alerts from firmware engineering | 2025-05-29 | **in** |
| `OBS-18` Established an evidence-based observation loop for judging a monitor's ongoing usefulness | 2025-05-29 | partial |

> `OBS-7` is deliberately `partial`: the resume claims the catch but not the battery-overheating specific, which names a safety-adjacent defect in a current employer's product. See *Open sensitivity question* below.

---

### POS — Positioning and location

Four entries, 2023–2026: a feature owned from its inception, field diagnostics, and the architecture.

**Entries:** [2023-11-27 Home/Away beacon tracking](../../raw/brag/2023-11-27-r5-home-away-beacon-tracking.md) · [2024-05-15 positioning root cause](../../raw/brag/2024-05-15-skyhook-positioning-root-cause-diagnostics.md) · [2025-11-15 location engine](../../raw/brag/2025-11-15-r5-location-engine-design.md) · [2026-09-01 beacon FOTA persistence](../../raw/brag/2026-09-01-r5-beacon-tracking-fota-persistence.md)

**Thread coverage: ≈ 54%** (7 of 13)

| Claim | Source | Status |
|---|---|---|
| `POS-1` Root-caused a recurring positioning-library failure — a multithreading fault losing the location fix — via telemetry log correlation | 2024-05-15 | partial |
| `POS-2` Identified the missing service-restart step that left the fallback path unable to fully recover affected devices | 2024-05-15 | absent |
| `POS-3` Reinterpreted an existing error-count signal as a proxy for time-without-fix, changing how the team thresholds it | 2024-05-15 | absent |
| `POS-4` Architected a modular location engine unifying beacon, GPS and Wi-Fi behind per-provider interfaces | 2025-11-15 | **in** |
| `POS-5` Built the state-management layer arbitrating between sources, with fallback when a provider fails | 2025-11-15 | **in** |
| `POS-6` Documented design and interfaces so other teams can extend the engine for new device variants | 2025-11-15 | **in** |
| `POS-7` Designed schema-backed persistence restoring paired beacon state across firmware-over-the-air updates | 2026-09-01 | **in** |
| ~~`POS-8` Kept devices in low-power beacon presence detection after updates instead of high-frequency polling, protecting battery life fleet-wide~~ — never customer-exposed, no fleet outcome | 2026-09-01 | struck 2026-09-14 |
| `POS-9` Hardened beacon/FOTA error categorization and made MCU reboot/fatal handling deliberate rather than incidental | 2026-09-01 | absent |
| `POS-10` Owned BLE beacon tracking from its inception, designing Home/Away as the simplest feature that answers home or away | 2023-11-27 | **in** |
| `POS-11` Drove the contract manufacturer's MCU and cradle BLE firmware to specification against a frozen cradle firmware | 2023-11-27 | **in** |
| `POS-12` Designed for optionality and held scope minimal (YAGNI) while consumers were out of scope, then argued for a location state machine as the next stage once top-down add-ons accreted | 2023-11-27 | partial |
| `POS-13` Named the long-running feature branch as technical debt while it accrued, and paid it down | 2023-11-27 | absent |

> Corrected 2026-09-14: beacon tracking was an assignment owned since 2023 and never customer-exposed, so `POS-8` is struck and the beacon paragraph in *Projects Overview* was rewritten around `POS-10`–`POS-12`. `POS-4`–`POS-6` stay `in`; the engine entry's outcome claims are unconfirmed, see its limitations. `POS-2`/`POS-3` remain interview detail.

---

### FW — Embedded platform frameworks

**Entries:** [2026-04-26 CCF capability framework](../../raw/brag/2026-04-26-ccf-capability-framework-lcm-open-source.md) · cross-listed: [2026-09-01 beacon FOTA persistence](../../raw/brag/2026-09-01-r5-beacon-tracking-fota-persistence.md) (claims tracked under POS)

**Thread coverage: 100%** (4 of 4)

| Claim | Source | Status |
|---|---|---|
| `FW-1` Led design and delivery of a capability and configuration framework standardizing capability management across device SKUs | 2026-04-26 | **in** |
| `FW-2` Implemented dependency injection and hierarchical state machines with predictable lifecycle management in embedded C | 2026-04-26 | **in** |
| `FW-3` Built an aligned structured-logging framework giving consistent logs across all supported devices | 2026-04-26 | **in** |
| `FW-4` Modularized and documented the framework for open-source release and external contribution | 2026-04-26 | **in** |

---

### AI — AI adoption and agentic engineering

**Entries:** [2025-10-29 AI data product](../../raw/brag/2025-10-29-ai-data-product-in-alation.md) · [2026-05-26 agentic engineering](../../raw/brag/2026-05-26-ai-adoption-agentic-engineering-choreographer.md)

**Thread coverage: ≈ 29%** (2 of 7)

| Claim | Source | Status |
|---|---|---|
| `AI-1` Scoped an AI-enabled data product on the enterprise data catalog to test whether warehoused device-event tables earn their storage and cellular cost | 2025-10-29 | absent |
| `AI-2` Combined lineage, query-log usage, glossary metadata and chat-with-your-data exploration into one cost-aware proposal | 2025-10-29 | absent |
| `AI-3` Designed and shipped a multi-agent orchestration layer as an agent plugin, preventing context overflow through delegation | 2026-05-26 | **in** |
| `AI-4` Established a persistent, versioned knowledge base (raw capture → synthesis → index) for the engineering organization | 2026-05-26 | **in** |
| `AI-5` Developed and documented prompt and agent patterns that cut token consumption while holding output quality | 2026-05-26 | absent |
| `AI-6` Integrated agents into code review, documentation and release-note workflows | 2026-05-26 | absent |
| `AI-7` Delivered outcomes at roughly three times the expected rate using AI since 2023 | 2026-05-26 | absent |

> `AI-7` was `in` until 2026-09-09 and was **deliberately retired** from the resume, not lost: an unverifiable productivity multiplier was replaced by what was actually built (`AI-3`, `AI-4`). The claim stays on this page because the underlying fact is still true and the owner may want it back — see *Open questions*.

---

### RSK — Risk, security and process practice

**Entries:** [2023-08-03 risk management analysis](../../raw/brag/2023-08-03-risk-management-practice-early-analysis.md) · [2023-09-30 patch management SOP](../../raw/brag/2023-09-30-security-patch-management-sop-and-vendor-engagement.md) · [2023-12-05 launch readiness](../../raw/brag/2023-12-05-operational-excellence-launch-readiness.md)

**Thread coverage: 100%** (7 of 7)

| Claim | Source | Status |
|---|---|---|
| `RSK-1` Analyzed the Quality organization's risk-management practice and found planning limited to one line of business and largely qualitative | 2023-08-03 | **in** |
| `RSK-2` Proposed risk appetite as the foundation for a unified, quantitatively-informed, org-wide approach | 2023-08-03 | **in** |
| `RSK-3` Drafted a NIST-grounded enterprise patch-management SOP for the fleet's embedded Linux firmware | 2023-09-30 | **in** |
| `RSK-4` Root-caused firmware staleness to an ODM's immediate-patch policy, informing a deliberate risk-based cadence | 2023-09-30 | **in** |
| `RSK-5` Initiated vendor security-feed engagement to formalize vulnerability-patch notification ahead of a device launch | 2023-09-30 | **in** |
| `RSK-6` Challenged a mandated launch-readiness control as the wrong instrument for the device, arguing from system coupling and existing test coverage rather than effort | 2023-12-05 | **in** |
| `RSK-7` Substituted better controls — chaos-style testing where failures actually live, escalation-path membership, and the one device-specific scenario worth rehearsing | 2023-12-05 | **in** |

---

### DEV — Device architecture and sensor research (2021–2022)

The R&D layer under the wearable programme: what the device should be, what it should cost in power, and how it would know where its user was. Captured 2026-09-10 from the owner's own working boards, years after the fact.

**Entries:** [2021-11-15 product architecture and power budget](../../raw/brag/2021-11-15-r5-product-architecture-power-budget-tradeoffs.md) · [2021-11-22 dead reckoning and sensor cluster](../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md)

**Thread coverage: 100%** (7 of 7)

| Claim | Source | Status |
|---|---|---|
| `DEV-1` Wrote the dead-reckoning blueprint placing a low-power sensor cluster and dedicated BLE MCU between sensors and application processor, so the AP stays asleep | 2021-11-22 | **in** |
| `DEV-2` Used the machine-learning core embedded in the sensor itself to classify motion, starting the wake-up chain as low in the stack as possible | 2021-11-22 | **in** |
| `DEV-3` Selected and justified the sensor and MCU lineup against motion, fall, stair-transition, heading and gyroscope-precession requirements | 2021-11-22 | **in** |
| `DEV-4` Ran the component-vendor engagement and specified a bench-evaluation programme, turning open architecture questions into measurable experiments | 2021-11-22 | **in** |
| `DEV-5` Argued the battery budget must be decided before the form factor, making it a researchable constraint rather than one inherited from an enclosure | 2021-11-15 | **in** |
| `DEV-6` Made the battery-versus-hardware trade-off structure explicit, including that capable hardware costs power twice — once for the part, once for software that uses it | 2021-11-15 | **in** |
| `DEV-7` Set the design goal that positioning be a non-issue in the power budget, which the sensor architecture was then built to satisfy | 2021-11-15 | **in** |

---

### CRISIS — The August 2019 CPSC recall and relaunch

The formative event of the GreatCall years, captured 2026-09-10 from the owner's direct statement, seven years after the fact, and grounded the same day in the public CPSC record.

**Entries:** [2019-08-30 CPSC recall and relaunch](../../raw/brag/2019-08-30-r4-cpsc-recall-and-relaunch.md)

**Thread coverage: 100%** (4 of 4)

| Claim | Source | Status |
|---|---|---|
| `CRISIS-1` Instrumental in getting a safety-critical device through the August 2019 CPSC recall (19-775) and its relaunch | 2019-08-30 | **in** |
| `CRISIS-2` Made the fleet answerable with telemetry when existing tooling could not say which devices were affected or whether a fix had taken | 2019-08-30 | **in** |
| `CRISIS-3` Built analysis that outlived the crisis and changed how the product was maintained afterwards | 2019-08-30 | **in** |
| `CRISIS-4` Learned, first-hand, how an entire organization coordinates such an event at every level | 2019-08-30 | **in** |

> **Settled 2026-09-10.** The owner confirmed the recall is public and supplied the CPSC notice, so the resume names it and links a pinned snapshot of the notice. What stays out is everything not in the public record — root cause and internal decision-making.

---

### MFG — Manufacturer boundary and firmware delivery

Where the device stops being ours: the specification handed to a contract manufacturer, and what happens when firmware delivery through that boundary fails.

**Entries:** [2022-08-03 ODM specification authoring](../../raw/brag/2022-08-03-odm-specification-authoring.md) · [2023-09-01 ODM transition](../../raw/brag/2023-09-01-r5-odm-transition.md) · [2026-09-11 hardware cadence](../../raw/brag/2026-09-11-hardware-cadence-engineer-to-engineer.md) · [2025-07-18 FOTA vendor escalation](../../raw/brag/2025-07-18-fota-vendor-escalation-lively-mobile2.md)

**Thread coverage: 100%** (13 of 13)

| Claim | Source | Status |
|---|---|---|
| `MFG-1` Authored the manufacturer-facing specification set — sensor-hub API, IPC API, device authentication, activation flow, system-monitor test plan | 2022-08-03 | **in** |
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

### QA — Test automation and environment diagnosis

**Entries:** [2024-12-31 device test automation](../../raw/brag/2024-12-31-device-test-automation-robot-framework.md)

**Thread coverage: 0%** (0 of 7)

| Claim | Source | Status |
|---|---|---|
| `QA-1` Distinguished broken tests from broken environments across message-broker, staging and provisioning failures, preventing an untrustworthy suite | 2024-12-31 | absent |
| `QA-2` Ran a protocol-level OAuth bearer-token investigation to unblock a whole class of automated tests | 2024-12-31 | absent |
| `QA-3` Configured CI so an AI coding agent could open pull requests against the automation repository, treating the agent as a contributor | 2024-12-31 | absent |
| `QA-4` Converted a top-down test-automation mandate into a mentorship practice for junior and QA engineers, deciding deliberately what to build himself and what to guide others through | 2024-12-31 | absent |
| `QA-5` Introduced pull-request discipline to the engineers he mentored — a practice that outlives the framework it arrived with | 2024-12-31 | absent |
| `QA-6` Pushed back on making unit-test coverage an externally observed metric, on the ground that it removes unit tests from an engineer's own toolbox | 2024-12-31 | absent |
| `QA-7` Names the limit of AI-assisted mentorship: prompt engineering is easy to learn and easy to master, while building good software is multi-dimensional | 2024-12-31 | absent |

> **Re-ingested 2026-09-13 after the owner reframed the entry.** The framework was mastered in days and was never the accomplishment; the mentorship under a mandate is. `QA-4` and `QA-6` are the principal-level claims here and belong with `LEAD` in any promotion pass — `QA-6` in particular is a refusal argued on engineering grounds, which is the same behaviour as the launch-readiness challenge in `RSK`. The entry stays `resume-worthy: maybe`; that judgement is the owner's and the reframing may change it.

---

### DATA — Data engineering and governance

**Entries:** [2022-05-18 Snowflake device telemetry](../../raw/brag/2022-05-18-snowflake-edw-device-telemetry.md) · cross-listed: [2025-10-29 AI data product](../../raw/brag/2025-10-29-ai-data-product-in-alation.md) (claims tracked under `AI`)

**Thread coverage: 0%** (0 of 2)

| Claim | Source | Status |
|---|---|---|
| `DATA-1` Learned the enterprise data warehouse to interrogate device telemetry directly, removing the device team's dependency on requested reports | 2022-05-18 | absent |
| `DATA-2` Argued data-mesh and data-product ownership for the device domain years before taking on the data-governance stewardship that realized it | 2022-05-18 | absent |

---

### MED — Regulated medical devices (Current Health)

The mid-career transition from consumer safety-adjacent devices into a regulated medical-device organization. **Partial capture** — the owner has said more material is coming, and supplied a first tranche (`MED-6`–`MED-8`) on 2026-09-10 and a second (`MED-9`–`MED-11`) on 2026-09-11, when the entry was also re-dated to sit inside the public window.

**Entries:** [2024-09-24 Current Health and Hospital at Home](../../raw/brag/2024-09-24-current-health-hospital-at-home-qms.md)

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
| `MED-12` Distinguishes breadth-first white-label integration from ground-up device engineering, and why a hybrid inherits the costs of both | 2025-04-13 | **in** |
| `MED-13` Held an observer role on the BLE SDK initiative rather than claiming a model he was watching | 2025-04-13 | partial |

---

---

### PWR — Battery and power as a standing specialization

The owner's second major, and the same subject as `POS` seen from the power side. `DEV` holds the 2021 argument that started it; this thread holds the standing expertise and the judgement calls it enabled, through 2026.

**Entries:** [2021-10-16 battery and power as a second specialization](../../raw/brag/2021-10-16-battery-power-second-specialization.md) · cross-listed: [2021-11-15 power budget](../../raw/brag/2021-11-15-r5-product-architecture-power-budget-tradeoffs.md) and [2021-11-22 sensor cluster](../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) (claims under `DEV`)

**Thread coverage: 0%** (0 of 7)

| Claim | Source | Status |
|---|---|---|
| `PWR-1` Carries battery and power management as a second specialization alongside positioning, on a cellular wearable | 2021-10-16 | absent |
| `PWR-2` Established the mechanical interlock between the two: the fallback breadcrumbing interval specified in units of MQTT keep-alive intervals, so a location report rides an existing network wake-up | 2021-10-16 | absent |
| `PWR-3` Holds a platform-level intuition for power on Qualcomm MDM-class SoCs — modem-versus-AP positioning, combo-radio beacon scanning, wakelocks, cellular power-saving modes | 2021-10-16 | absent |
| `PWR-4` Reduced battery questions from analysis campaigns to a stated hypothesis plus a cheap experiment, and has been consistently right in recent years | 2021-10-16 | absent |
| `PWR-5` Delivered the 2026 keep-alive production configuration, with a notebook from the engineering build and device soak testing to confirm the battery effect | 2021-10-16 | absent |
| `PWR-6` Advises product management and business partners on what will and will not move battery life before a quarter is spent finding out | 2021-10-16 | absent |
| `PWR-7` Cut a prototyping path short on his own finding that MCU-based positioning might not reduce the power budget — a negative result reached and acted on | 2021-10-16 | absent |

> `PWR-4` and `PWR-6` are the claims to watch: both are genuinely principal-level and both currently rest on the owner's own assessment, with no measured before/after committed. Promote them narrowly, or promote `PWR-2` and `PWR-5` instead, which are documented. See [voice and prominence](../workflows/voice-and-prominence.md) § *Prominence follows evidence*.

---

### COST — Cost of operation: cellular data and the devices that waste it

Where observability stops being about reliability and starts being about money. The company is its own MVNO, so cellular data is a direct per-device cost.

**Entries:** [2024-01-04 cellular cost and rogue-device detection](../../raw/brag/2024-01-04-cellular-cost-rogue-device-detection.md) · cross-listed: [2025-10-29 AI data product](../../raw/brag/2025-10-29-ai-data-product-in-alation.md) (claims under `AI`)

**Thread coverage: 0%** (0 of 6)

| Claim | Source | Status |
|---|---|---|
| `COST-1` Joined carrier cellular-operations data, device telemetry and warehouse event tables on device identity to find devices consuming far outside any plausible pattern | 2024-01-04 | absent |
| `COST-2` Built a rogue-device emulation script to validate the detection path against a device known to be misbehaving, and got the threshold agreed before an incident rather than during one | 2024-01-04 | absent |
| `COST-3` Published a rogue-device runbook and fed the scenario into the launch tabletop exercise | 2024-01-04 | absent |
| `COST-4` The work revealed a real misbehaving unit at roughly a gigabyte a day, investigated quickly because detection and runbook were already in place | 2024-01-04 | absent |
| `COST-5` Made replacement plus root cause the routine response, so each bad device produced a root cause rather than only a swap | 2024-01-04 | absent |
| `COST-6` Submitted five ideas to the organization's cost-reduction programme | 2024-01-04 | absent |

> `COST-6` is deliberately weak and should stay low-prominence or be dropped outward: submitted is not adopted, and the record shows no outcome. The dollar figure behind `COST-1` is the owner's own and is not in the archive — an outward claim should say "devices costing real money" and let a follow-up question carry the number.

---

### STAT — The statistical bar, and the Data Science partnership

The practice underneath the `OBS` thread's credibility: knowing when a question needs statistics and when it needs one decisive experiment, and keeping a specialist team engaged across an organizational boundary.

**Entries:** [2026-05-17 statistical bar and the Data Science partnership](../../raw/brag/2026-05-17-statistical-bar-and-data-science-partnership.md) · cross-listed: [2024-05-05 anomaly tuning](../../raw/brag/2024-05-05-r5-anomaly-detection-arima-tuning.md) and [2025-05-29 anomaly validation](../../raw/brag/2025-05-29-r5-anomaly-monitor-validated-against-mcu-alerts.md) (claims under `OBS`)

**Thread coverage: 0%** (0 of 5)

| Claim | Source | Status |
|---|---|---|
| `STAT-1` Argued for statistical reasoning where statistics is the right tool, including engaging real statisticians rather than approximating them | 2026-05-17 | absent |
| `STAT-2` Replaced brute-force analysis with a stated hypothesis and the smallest experiment that could settle it | 2026-05-17 | absent |
| `STAT-3` Replaced hand-built spreadsheets with re-runnable notebooks going directly at the warehouse | 2026-05-17 | absent |
| `STAT-4` Presented the anomaly monitors to the extended Data Science organization | 2026-05-17 | absent |
| `STAT-5` Sustained a working partnership with a specialist team that had its own priorities, including a named tactic for getting device work prioritized | 2026-05-17 | absent |

> **The weakest-supported thread in the corpus, and the entry says so itself.** `STAT-1` and `STAT-3` rest largely on the owner's statement; `STAT-2` and `STAT-4` are corroborated. Any outward claim should be drawn at the line the `OBS` entries already reach.

---

### CONC — Concurrency, and the bugs that vanish when observed

A failure class the owner has pursued for twenty years, with one fully documented investigation at its centre.

**Entries:** [2023-09-26 audio-service race condition](../../raw/brag/2023-09-26-audio-service-race-condition-diagnosis.md) · cross-listed: [2024-05-15 positioning root cause](../../raw/brag/2024-05-15-skyhook-positioning-root-cause-diagnostics.md) (claims under `POS`)

**Thread coverage: 0%** (0 of 5)

| Claim | Source | Status |
|---|---|---|
| `CONC-1` Diagnosed an intermittent audio artifact as a race condition without ever reproducing it, from correlated logs showing the playback thread created twice and the audio wakelock acquired twice before a forced reboot | 2023-09-26 | absent |
| `CONC-2` Corroborated the reboot story from an independent subsystem's own counter | 2023-09-26 | absent |
| `CONC-3` Designed instrumentation and fault injection instead of repeating a manual test, including a negative experiment that separated two failure modes | 2023-09-26 | absent |
| `CONC-4` Separated a defect that was being debugged as part of another, wrote a reproduction others could follow, and framed it as a risk rather than a bug report | 2023-09-26 | absent |
| `CONC-5` Treats concurrency as a specialization spanning a 2004 TCP/IP daemon, a 2024 positioning multithreading fault, and TLA+ study in 2026 | 2023-09-26 | absent |

> The resume already says "advanced Concurrency" twice without evidence behind it; this thread is the evidence. `CONC-1` is the strongest single debugging story in the corpus for a systems audience, and the honest ending — mechanism established, fix not attributable to him alone — is what makes it credible rather than weaker.

## What this says right now

1. **The absent 51 claims now sit in nine threads, and the four largest are new or leadership.** `LEAD` has 12 absent of 16 — still no evidence on the resume of managing upward, mentoring, or process discipline, the behaviours that separate a principal candidate from a senior one. Then `PWR` (7), `COST` (6), `STAT` (5) and `CONC` (5), all opened on 2026-09-13 and none promoted. The statement that "everything technical the brag file knows about has landed" was true on 2026-09-11 and is no longer: battery and power, cost of operation, and concurrency are all technical, all current, and all absent.
2. **Three of the four new threads are strong, and one is not.** `PWR`, `COST` and `CONC` each rest on documented work, and `CONC-1` is arguably the best debugging story in the corpus. `STAT` rests largely on the owner's own account. That asymmetry is exactly what the [prominence rule](../workflows/voice-and-prominence.md) exists for: promote `PWR-2`, `PWR-5`, `COST-2`, `COST-4` and `CONC-1` before anything from `STAT`.
3. **`QA` is no longer small.** Reframed on 2026-09-13 around the mentorship it actually was, it now carries seven claims — including the refusal to let unit-test coverage become an externally watched metric, and pull-request discipline taught to QA engineers under a compliance mandate. Read it alongside `LEAD`: between them they are 19 of the 51 absent claims, and they are the same argument about how this person operates. `DATA` remains the genuine small zero, at two.
4. **The binding constraint has changed.** Before the 2026-09-10 budget pass the question was *what is worth promoting*; the pool was rich and the document had room. It is now *what fits*: the About section and every Experience entry are marked with LinkedIn's character budgets and the build fails when one is exceeded. The Best Buy Health entry has 31 characters of headroom. The next promotion into it has to displace something, and that is a real editorial decision rather than an oversight.
5. **`ARC` is still promoted but uncaptured**, which inverts the normal direction of the pipeline. The resume asserts something the knowledge layer cannot source. The brag entry remains genuinely owed.
6. **Depth now lives in *Projects Overview*.** Eight new sections carry the Best Buy Health era, which had none before. That is where a future promotion should land first; the C2 bullets and the LinkedIn-budgeted sections above them are for claims that change what a reader should know in the first two pages.

## Open questions

- **`OBS-7`, battery overheating.** The brag entry records catching a battery-overheating condition before customers reported it. The resume claims the catch generically instead, because naming a safety-adjacent defect in a current employer's product is arguably unfair disclosure under [sensitivity tiers](../workflows/sensitivity-tiers.md) § *T2*. Applying the conservative reading was an agent's call; the owner may overrule it, and either way the tier page should say explicitly how to treat a defect one caught oneself.
- **`AI-7`, the productivity multiplier.** Retired from the resume in favour of capability claims. Restorable if the owner wants a quantified line back.
- **What gets displaced next.** The Best Buy Health Experience entry is at 1,969 of 2,000 characters. Promoting anything further into it means removing something already there, and the choice of what to remove is the owner's rather than an agent's. The alternative — splitting the 2018-present tenure into two LinkedIn positions at the GreatCall/Best Buy Health boundary — would roughly double the available room, and is a profile-structure decision, not a resume one.
- **How much of the leadership material is promotable at all.** `LEAD-9` and `LEAD-10` describe a performance challenge and a contested promotion. They are real evidence of how the owner handles adversity, and they are recorded deliberately — but a resume states outcomes, not the conversations behind them. The likely answer is that they inform an interview narrative rather than a bullet, and the coverage number should not be read as demanding their promotion.

## Maintenance

- **On ingest:** add the entry's claims to its thread, or open a thread if it starts one. New claims default to `absent`. Assign the entry to exactly one primary thread; cross-list it under others without duplicating its claims.
- **Statuses:** `in` (fully reflected), `partial` (gestured at generically), `absent` (not there yet), `held` (deliberately never for the resume — the owner's call, not an agent's). `held` claims stay in the tables so the record is complete, and are excluded from every total.
- **On promotion:** when resume text lands, flip the affected claims to `in` or `partial` in the same edit, and set the entry's ledger promotion status. Recompute the thread and headline numbers.
- **Recompute:** counts are maintained by hand and are meant to be approximate. If they drift, recount from the tables — the tables are the source of truth, the headline figures are derived.
- Claim IDs are stable and never reused. A claim that turns out to be wrong is struck, not deleted, so anything citing it still resolves. A claim retired from the resume returns to `absent` rather than being removed.

## Related

- [Update the outward-facing resume](update-workflow.md) — the pass this page feeds.
- [Primary resume — structure and cut points](primary-resume.md) — where a promoted claim has to fit.
- [Accomplishments by domain](../concepts/accomplishments-by-domain.md) — the same material organized for drafting rather than for gap-spotting.
- [Coverage history](coverage-history.md) — how the figure moved, and what each past pass promoted.
- [Brag ledger](../sources/brag-ledger.md) — ingest and promotion state per entry.
- [Brag file workflow](../workflows/brag-file.md) — capture and ingest.
- [Voice and prominence](../workflows/voice-and-prominence.md) — how a claim's support here decides how loudly it may be made outward.
