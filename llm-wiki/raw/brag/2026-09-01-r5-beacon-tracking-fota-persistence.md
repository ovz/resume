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
  - "positioning/one-engine-for-every-source"
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

## Related

- [2024-01-20-errorsummary-json-schema-datadog-limitation](2024-01-20-errorsummary-json-schema-datadog-limitation.md) — *maintained practice:* the chronic error categorization hardened here is the firmware-side continuation of the error-summary telemetry contract established in 2024.
- [2025-01-14-r5-datadog-monitor-lifecycle-review](2025-01-14-r5-datadog-monitor-lifecycle-review.md) — *refined/stopped practice:* MCU-oriented monitoring superseded an older monitor; the deliberate MCU reboot/fatal handling in this entry is what that monitoring generation observes.
- [2025-05-01-r5-device-specific-failure-investigations](2025-05-01-r5-device-specific-failure-investigations.md) — the operations side of the same loop: device-level investigations there surfaced MCU and firmware-update-related conditions; this entry closes several of them in firmware.
- [2025-11-15-r5-location-engine-design](2025-11-15-r5-location-engine-design.md) — the modular location engine whose beacon provider this entry hardens; the persistence and lifecycle work here builds on that engine's provider interfaces.
- [2024-05-15-skyhook-positioning-root-cause-diagnostics](2024-05-15-skyhook-positioning-root-cause-diagnostics.md) — earlier positioning-reliability work on the same device family (Wi-Fi/GNSS side; this entry is the BLE-beacon side).
- [2026-04-26-ccf-capability-framework-lcm-open-source](2026-04-26-ccf-capability-framework-lcm-open-source.md) — same device programme and period; the lifecycle-management and structured-logging patterns there are the framework-level counterpart of the lifecycle/error-handling patterns applied here (thematic link, not a claimed dependency).

## Record history

- 2026-09-07: created
- 2026-09-08: renamed from `2026-09-07-…` to `2026-09-01-…` so the filename carries the accomplishment's impact date rather than the capture date; merged a second owner write-up of the same accomplishment (corner-case/MCU reboot-fatal fixes, structured impact bullets, second PR in evidence); widened domains; added *Related* cross-links; later the same day added *Related* link to the 2025-11-15 location-engine entry
- 2026-09-13: graduated into story `positioning/one-engine-for-every-source`; `storied` property added, body untouched.
