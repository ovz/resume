---
title: "Beacon tracking reliability, location accuracy, and battery optimization for R5 devices"
date: "2026-07 to 2026-09-01"
thread: POS
domains:
  - "positioning and location"
  - "embedded and safety-critical devices"
  - "operational excellence and observability"
  - "battery/power"
context: "Best Buy Health, wearables-em-r5-core (R5 senior-care wearable), firmware/systems"
sensitivity: private-repo
resume-worthy: maybe
storied:
  - "positioning/home-away-kept-simple"
---

# Beacon tracking reliability, location accuracy, and battery optimization for R5 devices

## What I did

Contributed to firmware and system design for the R5 wearable's Bluetooth beacon tracking, which the device relies on for in-home location awareness. Previously, paired beacon state could be lost across firmware-over-the-air (FOTA) updates, degrading location tracking and forcing the device into higher-power fallback polling.

- Designed and implemented a schema-backed mechanism to serialize and restore paired beacon state via a persistent FOTA handoff file (`fota_info.json`).
- Ensured restoration logic runs before the location subsystem starts, so beacon state carries over seamlessly across updates.
- Hardened error categorization and chronic error reporting for beacon/FOTA interactions to speed root-cause analysis. Silent failures in beacon tracking had been hard to diagnose, risking undetected service degradation and a higher support burden.
- Addressed beacon-tracking corner cases by fixing real-world defects and making MCU reboot/fatal handling deliberate rather than incidental, so tracking stays robust at the edges.
- Updated internal design docs and code comments to reflect the new lifecycle and error-handling patterns, supporting maintainability and future enhancements.

## Why it matters

- **Location accuracy:** devices now retain their paired beacon configuration through firmware updates, keeping in-home positioning accurate and reducing false "away"/"unknown" states.
- **Battery life:** because beacon state is reliably available post-update, the device stays in its low-power beacon-based presence detection mode instead of falling back to high-frequency polling, extending battery life for every device that takes an update.
- **Reliability and support:** fewer silent tracking failures and less need for manual re-pairing or support intervention after updates.
- **Operational diagnosability:** the sharper error categorization feeds the fleet telemetry that the observability practice already monitors (see *Related*), so beacon/FOTA issues are detected and resolved faster.

Operational metrics (support ticket reduction, measured battery life improvement) are pending post-release data.

## Skills demonstrated

Firmware/embedded systems design, state persistence across OTA update boundaries, schema design, error handling and diagnostics, defensive handling of reboot/fatal paths, battery/power optimization, technical documentation.

## Evidence

Jira story describing the beacon-tracking FOTA migration; a merged pull request implementing the persistence and restoration logic; a second merged pull request with the corner-case and MCU reboot/fatal-handling fixes and related Jira stories; supporting internal design docs; hardened error handling and chronic error categorization visible in code and test updates.

## Correction and context, 2026-09-14

The owner corrected this entry on 2026-09-14, in two rounds. The text above is left in place so the record shows what was believed before; these points supersede or reframe it:

1. **Beacon tracking was never exposed to customers.** The persistence work belongs to a release candidate created in August 2026. *Why it matters* describes what the design is for, not a delivered outcome: "every device that takes an update", fewer support interventions and fleet battery life are design intent, with no fleet behind them.
2. **The state-machine argument is about accreted add-ons, not about the 2023 design.** In July–August 2026 the owner argued that "Beacon Tracking as an add on falls apart quickly" and asked for a green light on a location state-machine refactor for a later maintenance release. His clarification, 2026-09-14: *"With LocationFSM the point is the Home/Away from 2023 didn't need a state machine and other complexity. But because quite a number top down mandated add ons were stuffed into what we have in August 2026 the codebase becomes messy. I strongly advocate that Location FSM must be the next stage rather than trying to add one little thing."* The add-ons on the board, 2025–2026: location-fix freshness on beacon exit; beacon location freshness; inside-home major sync; skipping location-fix requests on major syncs; an inside-home location-fix interval; a test call on cradle linking — with the keep-alive production refactoring underneath. His reading of what they did together, that classic pitfalls multiply rather than add, is told in the story `positioning/home-away-kept-simple`.
3. **The feature has been his since its 2023 inception**, as an assignment — [2023-11-27 Home/Away beacon tracking](2023-11-27-r5-home-away-beacon-tracking.md). This entry is its late chapter.

**Why FOTA durability was a gap.** Surviving a firmware update was not in the 2023 design documents, because firmware update worked differently then. In the owner's words: *"AI spotted that this is a gap, even without updated firmware docs being part of the knowledge. This also confirmed my early intuition since I started doing agentic coding that the strength of AI coding agent is that it will read all the inputs and not forget about any important piece of 1000 pages manual."* His position on what that means for engineering practice is recorded with the AI work — [2026-05-26 AI adoption](2026-05-26-ai-adoption-agentic-engineering-choreographer.md) § *Follow-up*.

The FOTA handoff file was, by his own account, added "rather opportunistically": *"As I predicted, FOTA related scenarios are never easy… Quite a few corner cases remain. I am finishing validating FOTA scenarios to make sure beacons are restored during all the relevant execution flows"* (late August 2026), and, planning the pull request before his September leave, *"I don't want to be the one who broke FOTA so I am researching all the scenarios and corner cases for beacon save and restore."*

### How the 2023 design aged, 2025–2026

- **2025-01, then 2025-12 to 2026-01** — location-fix freshness for the beacon *exit* event.
- **2025-07** — published a beacon tracking MVP status report for team review.
- **2025-09 retrospective** — *"MCU error is tech debt just like beacon tracking. The more time passes the more interest we end up paying on it."*
- **2026-01** — *"I am happy with what we have for Beacon Tracking for MR5. We can call the upcoming PR a release candidate."* He argued against getting clever about microcontroller reboots and every edge case — it overloads a limited QA resource and risks a flaky customer experience — and put the Home/Away release-candidate pull request up for review. In February he asked who to talk to about downstream consumption, and whether beacon tracking could be merged into the main development branch so product-development testing was not wasted.
- **2026-04** — a "test call" on the cradle's checkmark button turned out to be the home-cradle-linked call; Device Communications (JR, Shannon) had written their own pages instead of reading his. *"Because Home Away is so straightforward it will be easy to plug test call on Cradle linking as one of the side effects."* He designed the cradle-linked data-analytics event as an MQTT contract in that team's AsyncAPI format: *"So there will be a co-design this time, and this how it should be."*
- **2026-05 to 2026-06** — the beacon location-freshness pull request; AI-assisted research on the audio service, FOTA and beacons completed — *"research is a killer feature of ai."*
- **2026-06** — inside-home major sync behaviour pull-requested.
- **2026-07-20** — *"It quickly becomes necessary to make Beacon Tracking a first class FSM. Beacon Tracking as an add on falls apart quickly. This confirms my years of advocating to make simple Home/Away feature to work for everyone."*
- **2026-07-22** — a development meeting on microcontroller cradle functionality, "a welcome change of plans".
- **2026-07-28** — the keep-alive production refactoring broke beacon tracking. *"I am glad that I strongly advocated to keep beacon tracking simple. I could only imagine maintenance cost of a more sophisticated solution that no one but me fully understands."*
- **2026-08-07**, to a mentor — the team "finally received green light to properly scrutinize BLE based beacon tracking… I was in charge of this feature since the original inception 3 years ago."
- **2026-08** — corner cases from Shiping Wang's material and his own testing; an inside-home location-fix interval as the example of complexity rippling ("we step up the complexity and all kinds of corner cases will proliferate"); microcontroller fatal UI found to disable beacon tracking; a ticket closed without a pull request because "we have enough complexity to stop throw items ad hoc"; the release-candidate code review; FOTA preservation judged "additive… Best platform, of course would be Location FSM". QA deferred.

## What was blocked, cut short, or wrong

- **Customer exposure** was out of scope throughout.
- **The location state-machine refactor** he asked for is not green-lit as of this entry.
- **On-device testing and QA** were deferred; the FOTA pull request was planned for before 2026-09-08.
- **The original write-up above overclaimed** fleet outcomes for an unreleased feature.

## Evidence limitations

- **"AI spotted the gap"** rests on the owner's statement. The board corroborates AI-assisted research on FOTA and beacons (2026-06) but not that specific finding.
- **The two merged pull requests** under *Evidence* are not confirmed by the board, which as of 2026-09-01 shows the FOTA pull request still being prepared. Owner to confirm what is merged.
- **No operational metric exists**, and none can until the feature reaches customers.
- **"Top down mandated"** is the owner's characterization; the board shows the add-ons as tickets and sprint work, not who required them.

## Related

- [2023-11-27-r5-home-away-beacon-tracking](2023-11-27-r5-home-away-beacon-tracking.md) — the origin of this feature: the 2023 assignment, the Home/Away design, the manufacturer cradle work.
- [2024-01-20-errorsummary-json-schema-datadog-limitation](2024-01-20-errorsummary-json-schema-datadog-limitation.md) — *maintained practice:* the chronic error categorization hardened here is the firmware-side continuation of the error-summary telemetry contract established in 2024.
- [2025-01-14-r5-datadog-monitor-lifecycle-review](2025-01-14-r5-datadog-monitor-lifecycle-review.md) — *refined/stopped practice:* MCU-oriented monitoring superseded an older monitor; the deliberate MCU reboot/fatal handling in this entry is what that monitoring generation observes.
- [2025-05-01-r5-device-specific-failure-investigations](2025-05-01-r5-device-specific-failure-investigations.md) — the operations side of the same loop: device-level investigations there surfaced MCU and firmware-update-related conditions; this entry closes several of them in firmware.
- [2025-11-15-r5-location-engine-design](2025-11-15-r5-location-engine-design.md) — the modular location engine whose beacon provider this entry hardens; the persistence and lifecycle work here builds on that engine's provider interfaces.
- [2024-05-15-skyhook-positioning-root-cause-diagnostics](2024-05-15-skyhook-positioning-root-cause-diagnostics.md) — earlier positioning-reliability work on the same device family (Wi-Fi/GNSS side; this entry is the BLE-beacon side).
- [2024-05-08-ccf-capability-framework-lcm-open-source](2024-05-08-ccf-capability-framework-lcm-open-source.md) — same device programme; the lifecycle-management and structured-logging patterns there are the framework-level counterpart of the lifecycle/error-handling patterns applied here (thematic link, not a claimed dependency).

## Record history

- 2026-09-07: created
- 2026-09-08: renamed from `2026-09-07-…` to `2026-09-01-…` so the filename carries the accomplishment's impact date rather than the capture date; merged a second owner write-up of the same accomplishment (corner-case/MCU reboot-fatal fixes, structured impact bullets, second PR in evidence); widened domains; added *Related* cross-links; later the same day added *Related* link to the 2025-11-15 location-engine entry
- 2026-09-13: graduated into story `positioning/one-engine-for-every-source`; `storied` property added, body untouched.
- 2026-09-14: owner correction appended as *Correction and context* (never customer-exposed, August 2026 release candidate, FOTA gap found through AI-assisted research, 2025–2026 timeline from the board), plus *What was blocked* and *Evidence limitations*; original body left unedited; `storied` moved from the retired `positioning/one-engine-for-every-source` to `positioning/home-away-kept-simple`; *Related* link to the 2023-11-27 entry.
- 2026-09-14 (second round): correction point 2 reframed on the owner's clarification — the location state-machine argument is about top-down add-ons accreted by August 2026, not a need of the 2023 design and not evidence against the location engine; add-on list and a 2026-06 timeline line added; limitation on "top down mandated" added.
