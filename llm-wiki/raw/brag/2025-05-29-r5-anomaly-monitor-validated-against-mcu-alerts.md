# Validated an anomaly-based device error monitor against independent firmware alerts

- date: 2025-05-29
- context: Best Buy Health, Lively Mobile 2 (R5) production reliability — Datadog anomaly monitoring of device self-reported error telemetry
- domains: operational excellence and observability, embedded and safety-critical devices
- sensitivity: private-repo
- resume-worthy: maybe
- collaborator: Shiping Wang (MCU firmware owner)

## What I did

One of the per-error-category anomaly monitors set up during the 2024 tuning work ([2024-05-05-r5-anomaly-detection-arima-tuning](2024-05-05-r5-anomaly-detection-arima-tuning.md)) fired on the error stream of a specific firmware subsystem: 63.6% of the evaluation window's values fell outside the model's predicted band against a 0.6 alert threshold, evaluated over the preceding hour. Rather than treat the trigger as either noise or a confirmed problem, I framed the engineering question as whether the statistical anomaly corresponded to device behaviour a firmware engineer would consider real and actionable. I took the monitor event to Shiping Wang, the MCU firmware owner, for interpretation; his analysis correlated the window with multiple independent MCU error-monitor alerts he had received over the same period, giving two separate detection mechanisms agreeing on one underlying device condition. I recorded the outcome and set continued observation as the explicit next step, so the monitor's usefulness would be judged on accumulated evidence rather than on a single firing.

## Why it matters

Showed that the anomaly-detection layer could surface a genuine device-health pattern that a fixed-volume threshold would not have isolated, and did so by cross-checking one monitoring mechanism against another rather than assuming a configured alert is automatically useful. Established a small evidence-based feedback loop — production behaviour informs whether a monitor stays, is retuned, or is retired — and reinforced the production-telemetry ↔ firmware-expertise collaboration that the team's device-health work depends on.

Scope limitation, stated in the source: the thread establishes the correlation and the decision to keep observing. It does not record a downstream outcome (incidents prevented, devices replaced, alert-noise reduction), so none is claimed.

## Skills demonstrated

Alert validation and monitoring hygiene, statistical anomaly detection applied to fleet telemetry, cross-functional troubleshooting with firmware engineering, evidence-based operational decision-making, responsible alert lifecycle management.

## Evidence

Email thread on the triggered Datadog anomaly monitor for R5 total errors by description (May 29, 2025), in which the monitor event was shared, Shiping Wang correlated it with MCU alerts, and continued observation was recorded as the decision. The monitor's exact query is not reproduced here.

## Record history

- 2026-09-07: created from an owner-supplied write-up of the May 2025 email thread
- 2026-09-07: restored collaborator's name after the owner ruled colleague names acceptable at private-repo tier
