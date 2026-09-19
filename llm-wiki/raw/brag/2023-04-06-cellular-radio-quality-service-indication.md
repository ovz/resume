---
title: "Translated cellular radio quality and service state into tested device behavior"
date: "2023-04-06 to 2023-04-07"
thread: DEV
domains:
  - "Embedded and safety-critical devices"
  - "Quality and test automation"
context: "Best Buy Health, Lively Mobile 2 cellular radio-status integration"
sensitivity: private-repo
resume-worthy: maybe
---

# Translated cellular radio quality and service state into tested device behavior

## Scope: radio technology, kept separate from TCP/IP

This record concerns **cellular radio measurements and service indication**, not TCP/IP transport or MQTT delivery. It is separate because the owner explicitly requested that radio experience not be conflated with the networking-product career story.

## What I did

In April 2023 I implemented the device's low-signal indication using the radio-quality information available through its platform interface. The source changes are attributed to me on April 6 and 7.

The behavior distinguishes **no service** from **service available but poor radio conditions**. Within the service state, it compares several reported measurements against their respective thresholds rather than assuming that registration alone means acceptable conditions. If any monitored quality measure is below its threshold, the device displays the low-signal indication; otherwise it uses the normal service behavior.

The measurements are related but not interchangeable:

- **RSRP:** reference-signal received power, a measure of reference-signal strength.
- **RSSI:** received signal strength, including more than just the desired reference signal.
- **RSRQ:** reference-signal received quality, distinct from received power alone.
- **SNR:** signal-to-noise ratio, another aspect of whether a received signal is usable.

My implementation handled those distinct inputs in application logic. This does not imply I designed their measurement in the modem or calibrated the radio thresholds experimentally.

### Make the indication respond to new information

The follow-up change wired both device-information and network-information responses into the service-indication update path. A correct classification is not useful if the UI never recomputes it when the underlying state changes. The code chooses the service/no-service state from the platform's voice-service status, then applies the relevant display behavior.

That is a deliberate boundary: **the indication is not an end-to-end Internet reachability test**. Voice-service status, cellular packet-data availability, TCP connectivity, TLS authentication and MQTT session health are different observations. A low-signal indicator must not later be described as proving that all of those layers work.

### Test the combinations, not just the nominal state

The change includes test work for combinations of reported device information. The available tests exercise a poor value in each quality dimension while keeping the others at their comparison boundaries, along with the no-service behavior. The tests also account for the platform representation of SNR when constructing input data; comparing raw fields without respecting their units or scale would test the wrong condition.

The April 7 update adds the event-driven refresh path. The current suite contains cases for both network-information and device-information updates. This capture records test definitions and source authorship, not a new test execution or a measured improvement in RF performance.

## Why it matters

A cellular device can be registered while operating in weak or noisy conditions. Translating that distinction into behavior requires understanding what the modem reports, which service is being observed, how measurements are represented, and when the UI should refresh. My contribution connected those layers and made the classification testable.

This is useful adjacent experience for connected-device engineering. It is not substituted for the stronger networking evidence in asynchronous HTTP, MQTT traffic scheduling and cellular data-cost investigation.

## Skills demonstrated

Cellular radio telemetry interpretation; RSRP/RSSI/RSRQ/SNR distinctions; voice-service versus data-path reasoning; event-driven C++; platform-to-UI integration; threshold and parameter-combination testing; measurement representation awareness.

## Evidence

- Two owner-authored device-software changes dated April 6 and April 7, 2023, covering low-signal classification and service-indicator refresh on device/network reports.
- Associated UI, platform-data and unit-test changes; current test definitions for low-signal combinations and report-driven state changes. Exact internal revision and source references are retained offline.
- Existing broader radio-adjacent experience remains in the [sensor-cluster and BLE architecture record](2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) and [power-specialization record](2021-10-16-battery-power-second-specialization.md); those are distinct work, not additional outcomes of this change.

## Evidence limitations

No antenna design, RF propagation modeling, modem/baseband implementation, carrier-network planning, measured coverage gain, certification result or reduction in dropped calls is established. The source does not establish who originally selected the product's thresholds. No new device or RF test was performed for this capture.

## Related

- [Cellular MQTT traffic scheduling](2026-07-29-cellular-mqtt-traffic-scheduling.md): application/network behavior kept separate from radio-quality work.
- [HTTP callback ownership](2025-12-07-http-transfer-callback-ownership.md): TCP/HTTP transport and asynchronous lifetime handling, not RF engineering.

## Record history

- 2026-09-19: Created from authored source history and nearby test definitions during the requested networking capture. Filed separately as radio technology; no synthesis, coverage or public resume promotion.