---
title: "R5 Datadog Monitoring shipped for device production launch"
date: "2024-03-07"
thread: OBS
domains:
  - "operational excellence and observability"
  - "embedded and safety-critical devices"
context: "Best Buy Health, embedded emergency-response device (Lively Mobile 2 generation) production launch"
sensitivity: private-repo
resume-worthy: yes
---

# R5 Datadog Monitoring shipped for device production launch

## What I did

Owned the operational-excellence/observability effort for a new embedded device's production launch. Designed and implemented two production Datadog Monitors: one summed self-reported error counts by category to size overall error volume, the other counted distinct devices reporting each error category and served as a bridge metric until firmware could publish the primary error-volume field. Built a companion dashboard covering error trends, device-level breakdowns, a thermal-safety-warning panel, and a set of "expected, ignore" patterns tied to firmware-update events, then iterated on the dashboard's naming and layout with a program stakeholder to make it legible to non-specialist viewers. Collaborated directly with Datadog's Premier Support engineering team to solve platform-level blockers: how to define a custom numeric "measure" on a JSON telemetry field so it could be summed, how to structure multi-alert grouping so one notification carried enough context to start troubleshooting, and a misconfigured required tag that had been silently affecting alert routing.

## Why it matters

These monitors and the dashboard became the team's fundamental automated-alerting layer for the launch, replacing a purely manual, dashboard-watching approach with alerting tuned for a sensitivity/specificity tradeoff. The effort caught device and firmware issues — including a battery-overheating condition — before customers reported them, directly supporting the reliability bar expected of a safety-adjacent medical-alert device.

## Skills demonstrated

Observability/monitoring architecture (Datadog), incident-detection design, cross-vendor technical-support collaboration, dashboard design for operational stakeholders, statistical framing of alert tuning (sensitivity vs. specificity), embedded-device telemetry design.

## Evidence

Internal Confluence narrative and a recorded team walkthrough of the device Datadog Monitor deliverables (March 2024); Datadog Premier Support correspondence.

Related later lifecycle review: [2025-01-14-r5-datadog-monitor-lifecycle-review](2025-01-14-r5-datadog-monitor-lifecycle-review.md).

## Record history

- 2026-09-07: created
- 2026-09-08: added link to the later R5 Datadog monitor lifecycle review
