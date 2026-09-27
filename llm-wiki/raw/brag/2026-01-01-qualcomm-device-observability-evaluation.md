---
title: "Evaluated Qualcomm Device Observability as a fleet-scale telemetry platform"
date: "2026-01"
thread: OBS
domains:
  - "architecture and API design"
  - "data engineering"
  - "embedded and safety-critical devices"
  - "operational excellence and observability"
context: "Best Buy Health, Lively device fleet and Qualcomm/Skyhook Device Observability evaluation"
sensitivity: private-repo
resume-worthy: yes
---

# Evaluated Qualcomm Device Observability as a fleet-scale telemetry platform

## What I did

Served as the technical evaluator and internal subject-matter expert for Qualcomm/Skyhook Device Observability, performing the engineering due diligence needed to determine whether the platform could become a viable fleet-scale telemetry and diagnostics solution for Lively devices. Evaluated it as a production observability architecture decision rather than as a vendor feature request, covering device telemetry collection, fleet monitoring, network and cellular utilization, Datadog integration, OEM implementation requirements, vendor lock-in risk and long-term operational costs.

The platform continuously harvested device-health information and uploaded it through Qualcomm infrastructure into cloud-hosted storage for later analysis. Available telemetry included cellular signal, battery, storage, data usage, device-health and location-related observability data, with periodic cloud uploads and reporting. I investigated what telemetry was actually produced, whether individual metrics were trustworthy, whether they could be operationalized, how they compared with existing Datadog capabilities and whether downstream ingestion would create practical value.

Performed hands-on validation of observed telemetry. Identified battery values that appeared outside expected ranges, uncertainty about CPU-utilization reporting and ambiguity in the operational meaning of some metrics. Pursued clarification from Qualcomm and reviewed available documentation before drawing conclusions about deployment suitability.

Acted as the technical bridge between Qualcomm/Skyhook, TCL, Best Buy Health engineering, Operations and Product stakeholders. Determined that additional TCL participation would be required before several observability fields could become operationally useful, making vendor, ODM and operational readiness part of the decision. Obtained Qualcomm pricing and translated the technical findings into a fleet-scale cost and operational-impact discussion for leadership.

## Why it matters

This was a build-versus-buy and adoption decision about a telemetry pipeline, not merely a feature evaluation. The analysis tested whether Qualcomm-provided data would supplement or duplicate Datadog monitoring, improve coverage, reduce custom device reporting and potentially reduce cellular reporting costs, while making the new dependency on Qualcomm/Skyhook infrastructure explicit.

## Skills demonstrated

Embedded telemetry analysis, native SDK evaluation, fleet observability architecture, cellular reporting analysis, data-quality validation, metric semantics, Datadog integration strategy, vendor and ODM coordination, vendor-risk assessment, cost-benefit analysis and technology-adoption recommendations.

## Evidence

Firmware correspondence titled *Skyhook - Device Observability - Check In* and an email thread titled *[Skyhook/TCL/BBYH] LVR52 R5.5 OEM name indication*, both dated around the January 2026 evaluation. The correspondence contains the telemetry discussion, implementation dependencies and Qualcomm pricing exchange.

## Evidence limitations

The supplied record supports technical evaluation, telemetry validation, stakeholder coordination, pricing analysis and a recommendation prepared for leadership. It does not establish that Qualcomm Device Observability was deployed fleet-wide, that a final adoption decision was made, or that cellular costs or Datadog coverage improved in production. The telemetry-quality concerns are observations and interpretation questions requiring vendor clarification, not proof that the platform's underlying measurements were universally incorrect.

## What was blocked, cut short, or wrong

Several fields could not become operationally useful without additional TCL implementation work. The evaluation also surfaced architectural dependency and data-quality risks that limited a straightforward adoption case. No realized fleet outcome is claimed here because the available evidence ends at the technical and commercial recommendation.

## Related

- [2023-12-21-device-health-observability-architecture](2023-12-21-device-health-observability-architecture.md) — earlier architecture work establishing an agentless device-health telemetry approach under embedded resource constraints.
- [2024-03-07-r5-datadog-monitoring-launch](2024-03-07-r5-datadog-monitoring-launch.md) — existing Datadog monitoring and vendor-support foundation against which this platform was evaluated.
- [2024-01-04-cellular-cost-rogue-device-detection](2024-01-04-cellular-cost-rogue-device-detection.md) — related analysis of cellular operating cost using device and carrier data.
- [2025-05-01-qualcomm-skyhook-device-identity](2025-05-01-qualcomm-skyhook-device-identity.md) — earlier cross-company work establishing the device-identity prerequisite for Qualcomm/Skyhook observability and telemetry.
- [2025-12-01-qualcomm-ces-aware-showcase](2025-12-01-qualcomm-ces-aware-showcase.md) — shared observability context, applied to Qualcomm's intended CES use of production Lively devices before this later fleet-platform evaluation.
- [2022-09-16 buying positioning and calendar time](2022-09-16-skyhook-license-buy-calendar-time.md) — the positioning decision and the direct vendor relationship behind this evaluation.

## Record history

- 2026-09-19: created from owner-supplied January 2026 accomplishment note
- 2026-09-19: added *Related* forward link to the December 2025 Qualcomm CES showcase entry
- 2026-09-24: reciprocal *Related* link to an entry created the same day.
