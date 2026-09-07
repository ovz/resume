# Diagnosed and proposed a fix for an unqueryable device-telemetry JSON schema

- date: 2024-01-20
- context: Best Buy Health, device self-reported error telemetry ingested into Datadog
- domains: data engineering, operational excellence and observability
- sensitivity: private-repo
- resume-worthy: maybe

## What I did

Identified a structural limitation in the device's self-reported error telemetry: a JSON sub-object whose keys were themselves JSON-encoded strings containing quote characters, which the observability platform's attribute-naming rules could not accept (quote and colon characters are disallowed in attribute names) — making the field impossible to query, aggregate, or facet on directly. Traced the root cause to the specific escaping behavior, evaluated and ruled out the platform's available log-processing options (arithmetic processor, string-builder processor, log-message remapper) as insufficient for the case, and authored a solution proposal to restructure the sub-object into an array of name/count records plus a pre-computed total, weighing the proposal against the cost of a cross-team schema change. Escalated the specific query limitation directly to the platform vendor's support organization with a reproducible example.

## Why it matters

Unblocked quantitative monitoring of the device's most important self-reported health signal, which had been an unreliable manual workaround until this point, and the proposed schema change became the basis for a tracked firmware/schema change request with the platform team.

## Skills demonstrated

JSON/telemetry schema design, root-cause diagnosis of a third-party platform limitation, cross-team technical proposal writing, vendor support escalation.

## Evidence

Internal ticket drafts and vendor support correspondence (January 2024).

## Record history

- 2026-09-07: created
