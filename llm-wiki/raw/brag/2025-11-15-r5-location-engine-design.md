---
title: "Designed and implemented the modular R5 location engine unifying beacon, GPS, and Wi-Fi positioning"
date: "2025-09 to 2025-11-15"
thread: POS
domains:
  - "positioning and location"
  - "embedded and safety-critical devices"
  - "architecture and API design"
context: "Best Buy Health, R5 senior-care wearable, firmware/systems"
sensitivity: private-repo
resume-worthy: maybe
storied:
  - "positioning/one-engine-for-every-source"
---

# Designed and implemented the modular R5 location engine unifying beacon, GPS, and Wi-Fi positioning

## What I did

The R5 wearable needed a robust, extensible location engine for accurate in-home and out-of-home positioning across multiple, independently evolving sources — Bluetooth beacons, GPS, and Wi-Fi. Before this work, location logic was fragmented, making enhancements and maintenance difficult.

- **Architected a modular location engine** with clear interfaces per provider (beacon, GPS, Wi-Fi), enabling plug-and-play extensibility.
- **Established a state-management layer** that arbitrates between sources and provides the most reliable location estimate at any time.
- **Unified the location data flow:** standardized data formats and update mechanisms so location events are handled consistently across the system; integrated error handling and fallback logic so service continues if a provider fails or becomes unavailable.
- **Documented the design and interfaces** — diagrams, interface definitions, and usage examples — for future maintainers and developers.
- **Built for future enhancements:** the engine allows rapid integration of new technologies (e.g. future BLE protocols, Wi-Fi RTT) with minimal disruption to existing code.

## Why it matters

- **Positioning accuracy:** a unified engine that selects the best available source yields more accurate and reliable in-home and out-of-home detection — the device's safety features and user experience depend on precise, timely location, especially in-home presence detection.
- **Extensibility:** reduced the time and effort to add or update location providers, supporting faster adaptation to new requirements.
- **Maintainability:** consolidated location logic simplified the codebase and reduced technical debt.
- **Cross-team enablement:** clear documentation and modular interfaces let other teams build on the engine for new features and device variants.

Operational metrics (measured accuracy improvement, time-to-integrate new providers) are pending post-deployment data.

## Skills demonstrated

Embedded systems architecture, modular/provider-based interface design, state management and source arbitration, fault tolerance and fallback design, technical design documentation, cross-team enablement.

## Evidence

Internal design document (Confluence, "R5 Location Design") with diagrams, interface definitions, and usage examples; modular architecture and provider interfaces visible in the code repositories and interface specifications.

## Related

- [2024-05-15-skyhook-positioning-root-cause-diagnostics](2024-05-15-skyhook-positioning-root-cause-diagnostics.md) — earlier positioning-reliability work on the Wi-Fi/GNSS side of the same device family; the fragmentation diagnosed there is part of what this engine consolidates.
- [2026-09-01-r5-beacon-tracking-fota-persistence](2026-09-01-r5-beacon-tracking-fota-persistence.md) — later work on the beacon provider of this engine: persisting paired beacon state across FOTA updates and hardening the beacon lifecycle/error handling.

## Record history

- 2026-09-08: created from an owner write-up (accomplishment dated 2025-09 to 2025-11-15); internal design-doc URL replaced with a generic description per the brag-file rules
- 2026-09-13: graduated into story `positioning/one-engine-for-every-source`; `storied` property added, body untouched.
