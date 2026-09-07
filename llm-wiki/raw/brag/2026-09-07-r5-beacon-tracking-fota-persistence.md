# Beacon tracking reliability, location accuracy, and battery optimization for R5 devices

- date: 2026-07 to 2026-09
- context: Best Buy Health, wearables-em-r5-core (R5 senior-care wearable), firmware/systems
- domains: positioning, reliability, observability, battery/power
- sensitivity: private-repo
- resume-worthy: maybe

## What I did

Contributed to firmware and system design for the R5 wearable's Bluetooth beacon tracking, which the device relies on for in-home location awareness. Previously, paired beacon state could be lost across firmware-over-the-air (FOTA) updates, degrading location tracking and forcing the device into higher-power fallback polling.

- Designed and implemented a schema-backed mechanism to serialize and restore paired beacon state via a persistent FOTA handoff file (`fota_info.json`).
- Ensured restoration logic runs before the location subsystem starts, so beacon state carries over seamlessly across updates.
- Hardened error categorization and chronic error reporting for beacon/FOTA interactions to speed root-cause analysis.
- Updated internal design docs and code comments to reflect the new lifecycle and error-handling patterns.

## Why it matters

Devices now retain their paired beacon configuration through firmware updates, keeping in-home positioning accurate and reducing false "away"/"unknown" states. Because beacon state is reliably available post-update, the device stays in its low-power beacon-based presence detection mode instead of falling back to high-frequency polling, extending battery life. Reduces silent tracking failures and the need for manual re-pairing or support intervention after updates; improved error reporting speeds detection and resolution of beacon/FOTA issues.

Operational metrics (support ticket reduction, measured battery life improvement) are pending post-release data.

## Skills demonstrated

Firmware/embedded systems design, state persistence across OTA update boundaries, schema design, error handling and diagnostics, battery/power optimization, technical documentation.

## Evidence

Jira ticket describing the beacon-tracking FOTA migration; a merged pull request implementing the persistence and restoration logic; supporting internal design docs; hardened error handling and chronic error categorization visible in code and test updates.

## Record history

- 2026-09-07: created
