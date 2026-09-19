---
title: "Owned beacon tracking from its inception, and designed Home/Away as the simplest thing that could work"
date: "2022-10 to 2024-05 (simplified design confirmed and implemented 2023-10 to 2023-11-27)"
thread: POS
domains:
  - "positioning and location"
  - "embedded and safety-critical devices"
  - "architecture and API design"
  - "leadership"
context: "Best Buy Health, R5 senior-care wearable (Lively Mobile 2) and its BLE charging cradle; the contract-manufacturer (ODM) boundary; downstream care-centre, caregiver-app and device-communication teams"
sensitivity: private-repo
resume-worthy: yes
storied:
  - "positioning/home-away-kept-simple"
---

# Owned beacon tracking from its inception, and designed Home/Away as the simplest thing that could work

## In the owner's words

Stated 2026-09-14, correcting a story that had framed this work as sensor fusion he had lobbied for (spelling corrected, otherwise verbatim):

> I did not lobby sensor fusion for beacon tracking. Per brag files especially coming from r5-jira I received beacon tracking as an assignment. I saw immediately there was not that much work on device to implement it. A lot of work with ODM to get MCU and BLE part right both on Lively Mobile device and in its cradle. There was a complication that senior management decided we want never update firmware on cradle. Cradle firmware upgrade would actually be an interesting technical challenge and also a healthy practice. This resulted in the need to get beacon tracking working end to end so that to validate cradle behavior, but exposing beacon tracking to customers was out of scope. I immediately saw that device side is not a challenge. I am experienced enough to know what YAGNI means. The biggest risk was collaboration with cloud services that support care center, caregivers (people who take care of active seniors and often ones who pay for the subscription), and caregiver facing phone apps and web sites. Unfortunately talking to downstream consumer teams was out of scope too. I did touch base and established relationships but the scope was limited.
>
> I worked very hard to design simplest possible beacon tracking solution. It even got a name Home/Away. Because of the circumstances I prepared most diligent design documentation and my design was solid foundation with maximal optionality. As I suspected my results back in 2023 were skimmed over, everyone was silently in agreement without thinking much.
>
> As I correctly evaluated, the risk of this becoming a tech debt materialized.

How that risk materialized, 2025–2026, is recorded in [2026-09-01 beacon tracking and FOTA persistence](2026-09-01-r5-beacon-tracking-fota-persistence.md) § *Correction and context*.

## What I did

### It arrived as an assignment

Beacon tracking on the R5 was assigned, not pitched. The 2021 BLE-beaconing research in [the sensor-cluster entry](2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) was exploratory device-architecture work on a different question; the feature itself reached him through sprint planning in April 2023, when he planned the cradle-tracking MVP epic "to the best of my ability so that other team members could contribute" — and then found the team's working assumption was that he would implement all of it.

The design groundwork predates the assignment. In October–November 2022 he wrote the device-side cradle-tracking design, reconciling an earlier colleague's cradle beacon tracking design with the BLE design document and bridging the gaps in the BLE section of the D-Bus API specification handed to the ODM. Two decisions from that review are worth keeping: he treated the D-Bus API and the cradle API as **separate, non-transparent layers** rather than one design encapsulated in another, and he proposed widening the BLE feature code in the device configuration to cover all future BLE functionality rather than beacon tracking alone. Beacon enter and exit counts were specified as 16-bit ring counters sent as diagnostics, because not every event is transmitted — a throttling choice that still lets abnormal behaviour be detected.

### The device side was never the challenge

He saw early that the code on the wearable was the small part, and built it so that others could fill gaps once the microcontroller side worked end to end ("I have everything figured out in my mind"). April–June 2023:

- The skeleton and configuration for beacon tracking, with schema validation that fails until the BLE tracking fields are introduced.
- A beacon dictionary persisted as JSON objects in shared preferences, with a database migration script for the new schema, so paired cradles survive a reboot.
- D-Bus signals and console commands to exercise the microcontroller's BLE tracking — and, before the ODM's microcontroller firmware existed, a D-Bus spoofer to simulate cradle information, so the device logic could be verified without it.
- Home-cradle linking: handlers for the BLE alert messages, synchronizing the cradle list with the microcontroller at startup, a `modified` timestamp on each beacon record, and a cap of sixteen stored cradles tested at 0, 1, 8, 16, 17 and 18 (the oldest dropped). His own note on the cap is the YAGNI instinct in one line: *"If I maintain a single home cradle this will take care of beacon list growth. We can revisit this while non-home cradle tracking will be implemented."*

He did this while moving across the country in May 2023, deliberately building to a state "I am confident team can pick up and polish while I am moving", while the cradle requirements were being re-litigated at the same time. Multi-cradle tracking was descoped on a call with the ODM on 2023-05-15.

### The work was at the manufacturer boundary

The BLE implementation on the wearable's microcontroller and in the cradle belonged to the ODM, Wistron, and most of the effort went there. July–September 2023 he re-tested cradle linking on each new device and cradle build, documented defects as ODM tickets, upgraded the spoofer so the team could exercise device behaviour while cradle firmware was unstable, wrote testing instructions elaborate enough to cover activation, and read the ODM's cradle state-and-transition test reports line by line. His conclusion from one report: *"Cradle firmware implements linking, but MCU firmware on device messes up."* He found on his own a defect where, after a microcontroller reset, the linked cradle was recovered with incorrect information, and on 2023-09-20 confirmed that all cradle-linking functionality finally worked from the device software's standpoint. Shiping Wang and Rob Gonsiewski carried the microcontroller and low-level cradle testing alongside him.

### Cradle firmware set in stone

Senior management decided the cradle's firmware would not be updated — fixed "in stone" along with the September 2023 code freeze. He recorded it at the time as a dubious decision, and noted that the team's attention had turned to cradle issues too late. His own view is that cradle firmware update would have been an interesting technical challenge and a healthy practice. His August 2023 requirements list had already asked to exercise cradle firmware early "so to reduce the chance of different cradle versions in mass production".

The consequence shaped everything after: whatever the cradle did at launch it would do permanently, so beacon tracking had to work **end to end** to validate cradle behaviour — while exposing beacon tracking to customers remained out of scope.

### The real risk was downstream, and that was out of scope too

The consumers of home/away information were the cloud services behind the care centre, caregivers — often the person paying for the subscription — and the caregiver-facing phone apps and websites. Designing with those teams was not in his scope. He touched base anyway and built the relationships:

- The Link app team (Jeremy Moore; Philippe Darvish), Device Management and Device Communications, starting September 2023. A meeting with Link and Device Communications in late October 2023 produced a soft commitment from the Link team on Home/Away, and Joel Stair wrote a Link compatibility page capturing the solution.
- Device Communications was at capacity for the quarter, so validation used MQTT snapshots on the device and a lower-environment broker rather than their pipeline.
- In December 2023, when beacon tracking came up in a cross-team sync, he offered the Link team a concrete ask: an implementation that had passed the embedded team's code review, needing one developer and one QA to include.
- March 2024: a device build for the Link team with beacon events, and an April 2024 demo showing a beacon *enter* event arriving in Link.
- November–December 2024: following up on caregiver app support with Jordan Alhadoff and Nathan Hall, after learning nobody was working on Link beyond critical fixes.

### Home/Away: the simplest possible design

His August 2023 requirements card framed the first maintenance release's goal as *prototype and justify that beacon tracking is useful to determine whether the user is home or away*: minimize false positives that the user is away, confirm beacon tracking does not compromise battery life, identify the other items for a cost/benefit analysis, write the design, gather feedback from Link and Device Communications, and work in a feature branch because the main branch belonged to code freeze.

In October 2023 he refined the Home/Away (cradle tracking) design and cut it down to **linked cradle only**: every review comment resolved, the design confirmed, then implemented in November. The device reports three things — cradle linked, beacon enter, beacon exit — and sends `linked_cradle_enter` / `linked_cradle_exit` data-analytics events at a configurable proximity report interval, five minutes by default, with the last state winning inside an interval. He got the green light to send those events, and wrote the step-by-step on-device test instructions.

Keeping it that small took deliberate effort. His note to his manager in October 2023: *"We made the trade off to focus on simple Home/Away, rather than building a solution with more capabilities but also more risks, given the circumstance."* A colleague, CVK, repeatedly pushed for a more capable and more coupled solution — premature optimization, in the owner's reading — and the rest of the team tended not to argue; the owner asked for his manager's help to prune scope aggressively instead.

### Documentation as the hedge

With the consumers out of reach, the design document was the only way to leave them room. He wrote the most diligent design documentation he could, aiming for a foundation with maximal optionality. He expected it to be skimmed, and in his reading it was: everyone was silently in agreement. He had seen the failure mode earlier — a May 2023 retrospective recorded that the cradle tracking design document "remained rotting when the decision was made that Find Me is in scope", and argued for a single source of truth.

### The feature branch as debt

He named the long-running feature branch as technical debt while it was accruing, and paid it down: his April 2024 quarterly conversation records *"Beacon Tracking technical debt was successfully paid off. Long-running feature branch keeps this debt open to accumulation."* In May 2024 he updated the implementation for the core feature identifier — a time-boxed task he described as approaching strategic, given how much the Link collaboration mattered.

## Why it matters

- **It locates the risk correctly.** The device code was small; the risk sat in firmware owned by a manufacturer and in consumers he was not allowed to design with. The effort went where the risk was.
- **YAGNI held under pressure, and paid for itself later.** When a keep-alive refactoring broke beacon tracking in July 2026, it was cheap to fix because there was so little of it — see [battery and power](2021-10-16-battery-power-second-specialization.md).
- **Design for optionality when the customer of the design cannot be consulted.** A deliberately small feature plus a thorough document is the hedge available to an engineer whose scope stops at the device.
- **The debt call was right.** He predicted the feature would turn into technical debt; scope shifted for three years and the release candidate arrived in August 2026.
- **It is an honest record of unshipped work.** Built, validated end to end against the cradle, and never exposed to customers.

## Skills demonstrated

Risk identification across organizational boundaries; minimal design and scope discipline (YAGNI); layered API design across the device/ODM boundary; embedded state persistence and schema migration; test doubles for hardware that does not exist yet; ODM defect management and test-report review; cross-team relationship building without formal scope; design documentation for optionality; naming technical debt as it accrues.

## What was blocked, cut short, or wrong

- **Customer exposure was never in scope**, and neither was co-design with downstream consumers. Link had no capacity beyond critical work; Device Communications was oversubscribed.
- **Cradle firmware was frozen** at the 2023 code freeze, removing the option to fix cradle behaviour after launch.
- **Product appetite fell.** In September 2023 the product manager reduced the likelihood the team would do beacon tracking at all; multi-cradle tracking had already been descoped in May.
- **The design was agreed without being engaged with**, in the owner's reading.
- **Visibility.** In October 2023 he wrote that he felt "tricked, trapped into beacon tracking" if its outcomes would not count while a stressful launch schedule was being retrospected — the same period as the [performance conversation](2023-05-02-performance-conversation-and-promotion-context.md), where he noted he could have written much more beacon tracking code against a mature, reviewed design.
- **The lesson he takes:** when co-design with consumers is out of scope, keep the feature small and the document thorough — and keep pushing for co-design anyway. It finally happened in 2026, on the cradle-linked event.

## Evidence

Device-programme board, 2022-10 to 2024-12: the *Beacon Tracking Implementation*, *R5 Location* and *R5 MVP Locations* lists and the sprint-by-sprint standup cards, carrying the requirements card, pull-request descriptions for the skeleton and configuration, the microcontroller BLE exercise, cradle linking and the simplified linked-cradle-only implementation, the on-device test instructions, and the ODM cradle ticket and test-report reviews. Leadership board one-on-one lists, 2023-04 to 2024-01, for the scope trade-off, the cradle firmware decision and the cross-team work. Internal design pages for cradle tracking and Link compatibility exist and are not linked here. The April 2024 quarterly conversation text records the feature-branch debt being paid off.

## Evidence limitations

- **"Never update firmware on the cradle"** — the board records the decision as setting cradle firmware "in stone" with the September 2023 code freeze; that it is permanent rests on the owner's statement.
- **"Skimmed over, silently in agreement"** is the owner's reading. The board shows the design confirmed with every comment resolved and no substantive objection, which is consistent with it but does not prove it.
- **No customer, battery or support outcome exists** to cite; the feature was never exposed to customers.
- **Where the code lived** is not fully clear from the board: the debt was recorded as paid off in April 2024, yet in February 2026 he was still asking whether beacon tracking could be merged into the main development branch. Owner to confirm.

## Related

- [2026-09-01 beacon tracking and FOTA persistence](2026-09-01-r5-beacon-tracking-fota-persistence.md) — the same feature three years on: the release candidate, its FOTA persistence, and how the design aged.
- [2021-11-22 dead reckoning and sensor cluster](2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) — earlier BLE-beaconing research on a different question; not the origin of this assignment.
- [2022-08-03 ODM specification authoring](2022-08-03-odm-specification-authoring.md) — the specification discipline at the same manufacturer boundary this work ran across.
- [2023-09-01 R5 ODM transition](2023-09-01-r5-odm-transition.md) — the manufacturer relationship whose cradle and microcontroller firmware this work depended on.
- [2021-10-16 battery and power](2021-10-16-battery-power-second-specialization.md) — the 2026 keep-alive refactoring that broke beacon tracking, and why its simplicity kept the fix cheap.
- [2023-05-02 performance conversation](2023-05-02-performance-conversation-and-promotion-context.md) — beacon tracking as the example of work slowed by re-litigated decisions.
- [2025-04-01 Staff Engineer behaviours](2025-04-01-staff-engineer-behaviors-principal-positioning.md) — beacon tracking named as delivered on his own initiative.

## Record history

- 2026-09-14: created from the owner's correction of 2026-09-14, grounded the same day in the committed device-programme and leadership board snapshots. Replaces the framing of the retired story `positioning/one-engine-for-every-source`; graduated at creation into story `positioning/home-away-kept-simple`.
