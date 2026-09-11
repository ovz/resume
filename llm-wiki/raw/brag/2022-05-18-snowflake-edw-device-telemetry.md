---
title: "Learned the enterprise data warehouse to get at device telemetry directly, and pushed data-mesh thinking into the device team"
date: "2022-05-18 onward"
thread: DATA
domains:
  - "data engineering"
  - "positioning and location"
  - "embedded and safety-critical devices"
context: "Best Buy Health, R5 wearable programme, device telemetry and analytics"
sensitivity: private-repo
resume-worthy: maybe
---

# Learned the enterprise data warehouse to get at device telemetry directly, and pushed data-mesh thinking into the device team

## What I did

Device stability reporting depended on the enterprise data warehouse, and the device team consumed those reports without being able to interrogate the underlying data. I closed that gap for myself and then argued for closing it structurally.

**Went to the source.** I worked out exactly which warehouse tables the stability reports were built from — device event detail and its event-code dimension, carrier data-transport records, line-of-service, GPS fix records, and network statistics — so that a question about device behaviour could be answered against the data rather than by requesting a report and waiting.

**Learned the platform properly rather than by cargo-cult query.** I worked through the vendor's key-concepts material systematically, and established the practical detail that mattered for our data: telemetry was stored as JSON in a record-content column, which determines how every query against it has to be written.

**Solved the access friction.** Authentication ran through the enterprise identity provider and forced an in-browser flow, which is workable interactively and useless for anything repeatable. I identified avoiding in-browser authentication as the blocker to automating any of this, and looked at a notebook-based environment as the way around it — the difference between ad-hoc lookups and reproducible analysis.

**Went to the people, not just the docs.** I identified the engineer who owned the stability reporting and worked directly with him on which tables were used and how, rather than reverse-engineering it alone.

**Connected it to the location work.** I specifically tracked the previous generation's location data in the warehouse, tying warehouse telemetry to the positioning problems I was working on — which is what made this data engineering in service of a device question rather than a detour.

**Pushed the structural argument.** I raised data products, self-service platform and data-mesh ideas for the device domain — the position being that a device team should own and publish its telemetry as a product other teams can consume, rather than every question routing through a central reporting function. That framing is the direct ancestor of the data-governance and catalog work I took on years later.

## Why it matters

- **It removed a dependency.** A device engineer who can query the warehouse directly can answer stability and positioning questions in hours instead of negotiating a report request.
- **It is deliberate breadth into an adjacent discipline** — an embedded engineer learning warehouse modelling, semi-structured storage and enterprise authentication because the device questions lived there.
- **The data-mesh argument was early and correct for the context**, and prefigured the data-governance stewardship and catalog work later taken on as a stretch assignment.
- The in-browser-authentication finding is the kind of specific, practical blocker that separates analysis someone can repeat from analysis they did once.

## Skills demonstrated

Snowflake and enterprise data warehousing; semi-structured/JSON data in analytical stores; telemetry data modelling; enterprise SSO and non-interactive authentication; notebook-based analysis; data mesh and data-product thinking; cross-team collaboration with data owners; self-directed learning into an adjacent domain.

## Evidence

Trello device-programme board, *Snowflake Based EDW* list (4 cards), from 2022-05-18. Table names are internal schema identifiers and are described generically here; the warehouse portal URL, environment names and colleague usernames remain in the board archive.

## Related

- [2025-10-29 AI data product in Alation](2025-10-29-ai-data-product-in-alation.md) — the data-governance and catalog work this thinking led to.
- [2024-05-15 Skyhook positioning root-cause diagnostics](2024-05-15-skyhook-positioning-root-cause-diagnostics.md) — later positioning diagnosis using fleet data.
- [2023-12-21 Device-health observability architecture](2023-12-21-device-health-observability-architecture.md) — the observability programme that gave device telemetry a first-class home.

## Record history

- 2026-09-10: created from the Trello device-programme board during the full board ingest.
