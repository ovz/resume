---
title: "Instrumental in transitioning Lively Mobile 2 to a new contract manufacturer"
date: "2023-2024 (start date approximate — owner to correct)"
thread: MFG
domains:
  - "embedded and safety-critical devices"
  - "operational excellence and observability"
  - "risk management and compliance"
  - "architecture and API design"
context: "Best Buy Health, Lively Mobile 2 (R5)"
sensitivity: private-repo
resume-worthy: yes
---

# Instrumental in transitioning Lively Mobile 2 to a new contract manufacturer

> **Captured 2026-09-10 from the owner's direct statement.** Dates approximate.

## What I did

Lively Mobile 2 (R5) had to change ODM mid-programme: the original manufacturing arrangement, entered by a department outside engineering, did not work out, and the build moved from **Wistron** to **TCL**. The owner was **instrumental in making that transition succeed**.

**The operational-excellence work paid for itself here.** The observability programme built through 2023–2024 — the agentless device-health architecture ([2023-12-21](2023-12-21-device-health-observability-architecture.md)), the telemetry schema that made the primary health signal queryable ([2024-01-20](2024-01-20-errorsummary-json-schema-datadog-limitation.md)), the launch monitors and dashboard ([2024-03-07](2024-03-07-r5-datadog-monitoring-launch.md)), and the anomaly detection tuned from first principles ([2024-05-05](2024-05-05-r5-anomaly-detection-arima-tuning.md)) — turned out to be exactly the instrumentation a manufacturer transition needs. Hardware built by a different partner can differ in ways a specification does not capture; having fleet-level evidence already in place meant the question "is the new build behaving?" was answerable with data rather than argument.

That is the shape of the achievement worth carrying outward: **the investment was not made for the transition, and it is what made the transition verifiable.**

**Played it safe and served the customer at the same time.** The owner's framing: the conservative engineering call and the customer-outcome call were not in tension, and holding both is what the role required.

**Back to a regular hardware/software development lifecycle.** The transition's real finish line was not the first good build but the programme returning to a normal development lifecycle — which, for a device with new hardware and industrial design, means a cadence of six months or more. Anyone who has run one reads that as the hard part.

**Continuity of the device programme.** Fall detection — the product's killer feature — and the wider set of active-senior needs remain the direction of travel; see [2026-09-11](2026-09-11-fall-detection-product-driver.md).

*(To supply: the owner's specific deliverables in the transition; qualification and bring-up work on the new build; what was found; timeline.)*

## Why it matters

- **A mid-programme ODM change is a serious test** of specification quality, test coverage and fleet instrumentation all at once. Coming through one is strong evidence for a principal-level manufacturing-facing engineer.
- **It closes a loop with the specification work** of [2022-08-03](2022-08-03-odm-specification-authoring.md): specs written to be usable across an organizational and language boundary are what make a partner change survivable.
- **It is the clearest instance of infrastructure paying off later.** Observability built for cost-of-operation reasons became the transition's evidence base.

## Sensitivity

**The ODM identities and the origin of the change never leave T1.** Naming Wistron and TCL, and characterizing the original arrangement as a poor one, is commercially sensitive and unfair to a current employer and its partners outward — see [sensitivity tiers](../../wiki/workflows/sensitivity-tiers.md). The T0 rendering says only that the owner was instrumental in transitioning the product to a new contract manufacturer, and that the observability practice is what made it verifiable. That claim is entirely his own and stands on its own.

## Related

- [2022-08-03 ODM specification authoring](2022-08-03-odm-specification-authoring.md) — the manufacturer-facing specification set.
- [2025-07-18 FOTA vendor escalation](2025-07-18-fota-vendor-escalation-lively-mobile2.md) — the later delivery-boundary crisis on the same product.
- [Best Buy Health context](../../wiki/analysis/best-buy-health-context.md).

## Record history

- 2026-09-10: created from the owner's direct statement during the LinkedIn content pass. Dates approximate; deliverables owed.
- 2026-09-11: owner added the return to a regular hardware/software development lifecycle; confirmed that dates may stay out of outward text.
