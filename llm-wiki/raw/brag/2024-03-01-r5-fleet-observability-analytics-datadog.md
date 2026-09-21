---
title: "Built the R5 fleet observability and analytics platform using Datadog"
date: "2024-03 to 2025-01"
thread: OBS
domains:
  - "network software product engineering"
  - "data engineering"
  - "operational excellence and observability"
context: "Best Buy Health, R5 connected-device fleet production launch and post-launch operations"
sensitivity: private-repo
resume-worthy: yes
---

# Built the R5 fleet observability and analytics platform using Datadog

## What I did

Led the design and implementation of the observability, telemetry analytics, and automated monitoring framework used to support R5 production launch and post-launch operations. The work went beyond dashboards: worked through Datadog platform limitations, collaborated with Datadog technical resources, designed telemetry representations suitable for large-scale analytics, enabled anomaly and outlier detection capabilities, built automated monitors, established production alerting strategy, and developed the operational visibility needed to manage a large connected-device fleet.

The platform moved R5 observability from manual inspection toward a structured telemetry and alerting system capable of identifying production issues, anomalous device populations, emerging fleet patterns, and operational incidents. The strategy covered monitor selection, alerting, dashboard architecture, monitor tuning, incident workflows, production readiness, troubleshooting, operational reviews, launch-readiness validation and tabletop exercises.

The telemetry and monitoring work addressed location-service issues, dropped calls, battery-temperature conditions, accelerometer-related failures, firmware-update behaviour and device self-reported errors. Rather than treating errors only as individual events, the approach represented fleet behaviour quantitatively for population-level monitoring, trend analysis, anomaly detection, outlier identification and device clustering around failure modes.

## Why it matters

Traditional dashboard-only approaches did not scale to a deployed connected-device fleet: human review could miss emerging issues, device populations could conceal abnormal behaviour, and complex error structures were difficult to consume in analytics tools. The resulting monitoring and analytics foundation supported R5 operational readiness and production monitoring, helping the organisation move from isolated-incident reaction toward understanding patterns across the fleet.

The strongest data-engineering element was designing telemetry representations and quantitative metrics that downstream analytics systems could query and use, rather than simply generating more telemetry. This made the work a telemetry data-engineering accomplishment as well as an observability and operational-excellence accomplishment.

## Skills demonstrated

- Telemetry architecture for connected devices
- Fleet-scale monitoring and distributed-system visibility
- Datadog monitor and alerting strategy
- Quantitative error aggregation and analytics representation
- Anomaly and outlier monitoring
- Production readiness, incident workflows and operational troubleshooting
- Cross-vendor technical collaboration
- Service reliability engineering

## Evidence

Owner-supplied accomplishment synthesis received 2026-09-21, supported by the component records for the R5 monitoring launch, telemetry schema limitation, anomaly-monitor tuning, community presentation, self-reported-error runbook and monitor-lifecycle review. The component records describe the dated implementation episodes and their evidence sources, including internal Confluence material, recorded walkthroughs, vendor correspondence and operational-runbook records.

## Evidence limitations

This umbrella entry is a synthesis of the component records and the owner's account, not an independent platform inventory. The supplied material does not establish exact fleet size, quantitative reductions in incident time or operating cost, a complete monitor list, measured adoption of every analytics capability, or a single artifact proving that every named device behaviour was covered by a production monitor. Detailed claims should therefore be grounded in the dated component entries rather than this umbrella description alone.

## What was blocked, cut short, or wrong

Datadog's handling of nested telemetry and complex JSON payloads was a real platform constraint. The response was to redesign representations, simplify error aggregation and improve queryability; the limitation was not solved by relying on raw device errors or by adding dashboards alone. The entry does not claim that every proposed anomaly, outlier or forecast scenario shipped, only that the metric strategy enabled those advanced monitoring approaches and that the related component records document the implemented episodes.

## Concise brag-file version

Led development of the R5 Datadog observability platform, creating the telemetry architecture, anomaly-monitoring strategy, fleet analytics framework and automated alerting capabilities used to support production launch and post-launch operations. Solved Datadog telemetry-ingestion and analytics challenges, enabled anomaly and outlier detection, and established the operational visibility needed to identify fleet-wide issues and emerging device failure patterns.

## Regenerated candidate queue

The supplied note also regenerated a higher-level engineering queue after the Skyhook and Datadog work: Hybrid Skyhook / GNSS / Cellular Location Architecture; Diagnostic Telemetry and Logging Architecture; R5 Fleet Analytics & Device Population Modeling; Puffin Recovery Architecture and Recovery Validation; Device-Fleet Defect Discovery Program; and Location Reliability Program. This is preserved as planning context, not treated as additional accomplishment evidence. The note identifies Hybrid Skyhook / GNSS / Cellular Location Architecture as the strongest remaining network-first candidate because it is closest to protocol, location-service and distributed-system design.

## Related

- [2024-01-20-errorsummary-json-schema-datadog-limitation](2024-01-20-errorsummary-json-schema-datadog-limitation.md) — the telemetry-schema constraint and array-based representation proposal.
- [2024-03-07-r5-datadog-monitoring-launch](2024-03-07-r5-datadog-monitoring-launch.md) — the launch monitors and dashboard that formed the automated alerting foundation.
- [2024-04-18-r5-datadog-community-presentation](2024-04-18-r5-datadog-community-presentation.md) — cross-team presentation and live production-device investigation.
- [2024-05-05-r5-anomaly-detection-arima-tuning](2024-05-05-r5-anomaly-detection-arima-tuning.md) — statistical tuning of fleet-scale anomaly monitors.
- [2025-01-09-r5-self-reported-error-operational-runbook](2025-01-09-r5-self-reported-error-operational-runbook.md) — operational response guidance built from device-health telemetry.
- [2025-01-14-r5-datadog-monitor-lifecycle-review](2025-01-14-r5-datadog-monitor-lifecycle-review.md) — later portfolio stewardship and monitor rationalization.

## Record history

- 2026-09-21: created from the owner's supplied platform-level synthesis; preserved verbatim in the session-wiki raw capture.
