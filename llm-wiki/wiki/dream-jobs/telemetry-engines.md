---
title: "Telemetry and time-series engine internals"
dream-job: DJ-7
origin: suggested
specialization: established
evidence: moderate
horizon: build
fits: [systems, data, rust, cpp, observability]
status: candidate
---

# ○ Telemetry and time-series engine internals — the bridge candidate

> **Doc type:** reference · **origin: suggested** — proposed by an agent on 2026-09-13 as the shortest honest route from the record the owner has to [the database work he says he wants](database-internals.md). Not the owner's idea.

## The job

The same discipline as [database internals](database-internals.md), aimed at the data shape this career already produces: device events, carrier statistics, location fixes, error counts, firmware versions. Storage formats and compression for time-ordered data, ingest paths that survive bursty and out-of-order arrival, retention and downsampling, query execution over columnar layouts. Employers are time-series and observability vendors and the analytics-engine projects underneath them.

## Under the Value and Impact tests

**Product line, and the shortest route to another one.** At a time-series or observability vendor the engine is what customers pay for, so this scores where [database internals](database-internals.md) scores — while asking for one component rather than a career change. That is the whole argument for the bridge: same revenue line, a fraction of the distance.

## Why this is the bridge, and not a consolation prize

The database-internals candidate is graded `thin` for one reason: no engine artifact. Every other requirement — C++, concurrency, systems discipline, execution-time code generation, schema judgement — is already there. **This candidate closes that gap using domain knowledge as the lever rather than asking him to compete on engine pedigree alone.** He does not just know what device telemetry looks like; he has designed the schema, hit the query limitations, paid the storage bill, and asked whether the tables earn their cost. Very few engine engineers have ever been the customer.

The field is real and mid-rewrite: **InfluxDB 3** is the Rust rewrite of the category's best-known name, built on Arrow, DataFusion and Parquet; **QuestDB** is the time-series/IoT option; ClickHouse and DuckDB hold the analytical and embedded corners. Sources: [specializations landscape](../analysis/2026-09-13-specializations-landscape.md) §§ *Time-series and telemetry engines*, *Database and query-engine internals*.

## What the record already supports

- **Schema design for telemetry, under a real engine's constraints**: [diagnosing why the primary device-health signal was unqueryable — quote-bearing JSON keys the platform's attribute rules reject — and authoring the array-based schema change that unblocked quantitative monitoring](../../raw/brag/2024-01-20-errorsummary-json-schema-datadog-limitation.md). That is a bug report an engine team would read with interest.
- **Wide-contract event design** so a schema could evolve without a firmware release ([2023-12-21](../../raw/brag/2023-12-21-device-health-observability-architecture.md)). Schema evolution under a client you cannot redeploy on demand is a database problem wearing firmware clothes.
- **Time-series statistics at the query layer**: [ARIMA/SARIMA-based anomaly detection tuned by partition](../../raw/brag/2024-05-05-r5-anomaly-detection-arima-tuning.md) — he has reasoned about what the engine's own time-series functions are doing.
- **Warehouse depth**: [learning the enterprise warehouse well enough to interrogate device telemetry directly, and arguing data-product ownership for the device domain](../../raw/brag/2022-05-18-snowflake-edw-device-telemetry.md); JSON-stored event detail, carrier transport, GPS fix and network statistics.
- **Storage cost as a first-class question**: [do warehoused device-event tables earn their storage and cellular cost?](../../raw/brag/2025-10-29-ai-data-product-in-alation.md) — retention and downsampling policy, asked from the paying side.
- **Execution-time code generation, already done once**: the Hive scoring utility compiling model code per invocation on every node ([resume][primary]).
- **Systems credentials**: C++ since 1996, concurrency depth, cross-compilation and packaging, a 64-bit migration done address by address.

## The gap, and the shortest path

**The gap is the same single artifact**, and this is where it is cheapest to produce: a component in a time-series or analytics engine, in a part of the system whose requirements he can state from experience.

1. **Pick an engine in this niche and fix something real** — an ingest-path edge case with out-of-order or duplicate device events, a compression or encoding improvement for a column type telemetry actually produces, a retention/downsampling behaviour. Arrow/DataFusion-based projects make operator-level contributions unusually approachable.
2. **Write the telemetry-schema war story publicly.** The unqueryable-key diagnosis is exactly the content engine teams circulate, and it demonstrates engine-adjacent judgement without needing a commit.
3. **Then re-grade [database internals](database-internals.md).** One landed component moves that candidate from `thin` to `moderate`, which is the whole point of taking this route.

## The vocabulary to foreground

Time-series storage · columnar formats and Parquet · Arrow and DataFusion · ingest path and out-of-order arrival · schema evolution · retention and downsampling · compression and encodings · query execution over telemetry · wide events · storage cost per signal.

## Stories to tell for it

- The unqueryable health signal — the escaping rule, the diagnosis, the schema change that unblocked monitoring.
- The wide-contract event — schema evolution designed for a client that cannot be redeployed on demand.
- The Hive scoring utility — hundreds of models over billions of rows, compiled on the fly per invocation.

## How to tell if this is the one

**This candidate is a means as much as an end.** If, after landing one engine component, the interesting part was the engine, pursue [database internals](database-internals.md) properly. If the interesting part was the telemetry, then [fleet reliability](device-fleet-reliability.md) at larger scale is the truer direction and this was a productive detour. Either answer is worth the price of one component.

## Related

- [Database internals in C++ or Rust](database-internals.md) — the owner-originated candidate this one exists to reach.
- [Connected-device fleet reliability and cost](device-fleet-reliability.md) — the same domain, one layer up.
- [Dream-job hub](dream-job-hub.md) · [specializations landscape](../analysis/2026-09-13-specializations-landscape.md).

[primary]: ../../../markdown/Oleg.Zhylin.resume.achievements.md "Primary resume (achievements)"
