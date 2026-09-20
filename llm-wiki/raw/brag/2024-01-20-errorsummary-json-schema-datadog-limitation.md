---
title: "Diagnosed and proposed a fix for an unqueryable device-telemetry JSON schema"
date: "2024-01-20"
thread: OBS
domains:
  - "data engineering"
  - "operational excellence and observability"
context: "Best Buy Health, device self-reported error telemetry ingested into Datadog"
sensitivity: private-repo
resume-worthy: maybe
---

# Diagnosed and proposed a fix for an unqueryable device-telemetry JSON schema

## What I did

Identified a structural limitation in the device's self-reported error telemetry: a JSON sub-object whose keys were themselves JSON-encoded strings containing quote characters, which the observability platform's attribute-naming rules could not accept (quote and colon characters are disallowed in attribute names) — making the field impossible to query, aggregate, or facet on directly. Traced the root cause to the specific escaping behavior, evaluated and ruled out the platform's available log-processing options (arithmetic processor, string-builder processor, log-message remapper) as insufficient for the case, and authored a solution proposal to restructure the sub-object into an array of name/count records plus a pre-computed total, weighing the proposal against the cost of a cross-team schema change. Escalated the specific query limitation directly to the platform vendor's support organization with a reproducible example.

## Why it matters

Unblocked quantitative monitoring of the device's most important self-reported health signal, which had been an unreliable manual workaround until this point, and the proposed schema change became the basis for a tracked firmware/schema change request with the platform team.

## Skills demonstrated

JSON/telemetry schema design, root-cause diagnosis of a third-party platform limitation, cross-team technical proposal writing, vendor support escalation.

## Evidence

Internal ticket drafts and vendor support correspondence (January 2024).

## Related

- [2026-09-01-r5-beacon-tracking-fota-persistence](2026-09-01-r5-beacon-tracking-fota-persistence.md) — *practice maintained:* hardened chronic error categorization for beacon/FOTA interactions continues the error-summary contract established here (2026).
- [2024-05-08-ccf-capability-framework-lcm-open-source](2024-05-08-ccf-capability-framework-lcm-open-source.md) — the CCF structured-logging framework applies the consumer-shaped-telemetry lesson learned here (2024-2025).

## Record history

- 2026-09-07: created
- 2026-09-08: added *Related* forward links to the 2026-09-01 beacon-tracking and 2026-04-26 CCF entries
