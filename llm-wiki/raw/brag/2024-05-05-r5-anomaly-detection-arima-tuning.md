---
title: "Applied ARIMA/SARIMA anomaly-detection theory to tune fleet-scale error monitors"
date: "2024-04-05 to 2024-05-05"
thread: OBS
domains:
  - "operational excellence and observability"
  - "data engineering"
context: "Best Buy Health, device error-telemetry anomaly detection on a fast-growing device fleet"
sensitivity: private-repo
resume-worthy: yes
---

# Applied ARIMA/SARIMA anomaly-detection theory to tune fleet-scale error monitors

## What I did

Went beyond static-threshold alerting to evaluate Datadog's anomaly-detection monitor type, which is built on a SARIMA-family algorithm, for the device error-telemetry stream. Independently researched the statistical foundations — ARIMA/SARIMA structure, the stationarity assumption, the residual-normality assumption behind forecast confidence intervals, and the tradeoffs between the vendor's Basic/Agile/Robust algorithm variants — well enough to reason about why a given tuning choice worked or failed rather than treating the feature as a black box. Discovered empirically that partitioning the anomaly model by error-description category, instead of a single aggregate "total errors" stream, sharply cut false positives, because the aggregate stream mixed together unrelated error types in ways that violate a univariate model's independence assumptions; validated the hypothesis by isolating a known noisy error source and showing it explained a specific false-positive spike in the aggregate model. Selected the "Agile" SARIMA variant to match a fast-growing, non-stationary device population. Wrote up the reasoning and results for the team and prepared a targeted question set for the vendor's support organization to validate the statistical approach.

## Why it matters

Turned a generic vendor feature into a fleet-scale-aware, statistically grounded anomaly-detection capability that adapts automatically as the device population grows, avoiding indefinite manual re-tuning of fixed thresholds. The approach and findings were positioned as reusable guidance for other teams using the same vendor's anomaly monitors.

## Skills demonstrated

Applied time-series statistics (ARIMA/SARIMA), independent/self-directed technical research, hypothesis-driven empirical validation, translating vendor black-box behavior into engineering guidance, technical writing for a broad audience.

## Evidence

Internal Confluence drafts and dated research notes on anomaly-monitor tuning (April–May 2024).

## Related

- [2025-05-29-r5-anomaly-monitor-validated-against-mcu-alerts](2025-05-29-r5-anomaly-monitor-validated-against-mcu-alerts.md) — a year later, one of the per-category anomaly monitors produced by this tuning fired on a real device condition and was validated against independent firmware-level alerts.
- [2022-11-10 percentiles over averages](2022-11-10-percentiles-over-averages-location-statistics.md) — the distribution-aware reasoning taught to colleagues.

## Record history

- 2026-09-07: created
- 2026-09-07: added *Related* forward link to the 2025-05-29 validation entry
- 2026-09-24: reciprocal *Related* link to an entry created the same day.
