---
title: "Root-caused a recurring positioning-library failure via telemetry log correlation"
date: "2024-01-25 to 2024-05-15"
thread: POS
domains:
  - "positioning and location"
  - "operational excellence and observability"
context: "Best Buy Health, embedded device positioning subsystem (third-party GNSS/Wi-Fi positioning library)"
sensitivity: private-repo
resume-worthy: maybe
---

# Root-caused a recurring positioning-library failure via telemetry log correlation

## What I did

Used observability-platform log correlation to diagnose a recurring positioning-library failure mode on the device: a third-party positioning SDK losing the ability to obtain a location fix, traced to a multithreading fault while creating a listener thread. Investigated why the device's existing fallback-to-native-positioning path was not fully recovering affected devices and identified that a service restart was the missing recovery step. Derived and documented an operational reinterpretation of an existing telemetry signal: the device's "total errors" counter, which incremented on a fixed interval while the fault persisted, was better read as a proxy for *how long* devices went without a position fix than as a simple occurrence count — changing how the team should threshold and interpret that signal going forward.

## Why it matters

Converted an ambiguous, hard-to-reproduce field issue into a root-caused defect with a concrete fix path (service restart on fallback) and a corrected interpretation of an existing monitoring signal, feeding directly back into the reliability of a safety-critical positioning feature on an emergency-response device.

## Skills demonstrated

Log-driven root-cause analysis, third-party SDK/library troubleshooting, positioning/location subsystem expertise, translating raw telemetry into an operational interpretation.

## Evidence

Internal chat threads and observability-platform log queries (January and May 2024) documenting the diagnosis.

## Related

- [2025-11-15-r5-location-engine-design](2025-11-15-r5-location-engine-design.md) — the later modular location engine that consolidates the fragmented positioning logic this investigation exposed.

## Record history

- 2026-09-07: created
- 2026-09-08: added *Related* link to the 2025-11-15 location-engine entry
