---
title: "Writing database code in C++ or Rust"
dream-job: DJ-1
origin: owner
specialization: established
evidence: thin
horizon: stretch
fits: [systems, data, cpp, rust, concurrency]
status: candidate
---

# ★ Writing database code in C++ or Rust

> **Doc type:** reference · **origin: owner** — the owner's own statement, 2026-09-13: *"Databases is much more prominent in my professional experience and interest and writing database code in C++ or Rust is one of the possible dream jobs."*

## The job

Engine internals, not application development on top of a database: storage engines, indexes, query planning and execution, transactions and recovery. The employer is a database company or an open-source engine, the language is Rust or modern C++, and the unit of work is a component of the engine spine rather than a feature of a product.

## Under the Value and Impact tests

**Product line — the cleanest alignment in the hub.** At a database company the engine *is* the revenue, so technical power and money power cannot point in different directions; that structural agreement is exactly what the [hub's test](dream-job-hub.md) is built to find. The catch is entirely on the other axis: perfect alignment, thin record. That is what makes this an ambition worth a plan rather than a whim.

## Why it is a real field

Old discipline, new opening: a visible share of 2026's engines are being written in Rust, and postings ask for "meaningful experience working on … databases, query engines, storage engines, indexing systems, or similarly complex infrastructure software" — an *area of the spine*, not a vendor pedigree — with open-source contribution treated as part of the job. Evidence and sources: [specializations landscape](../analysis/2026-09-13-specializations-landscape.md) § *Database and query-engine internals*.

## What the record already supports

Real, and mostly one layer above the engine:

- **C++ since 1996**, concurrency and parallelism from a cross-platform TCP/IP daemon built singlehandedly, and a GoF-pattern C++ library written to learn the patterns properly ([resume][primary]).
- **Systems discipline that engine work assumes**: a [64-bit migration](../concepts/accomplishments-by-domain.md) done by methodically revisiting every address and size; Unicode hardening with static and dynamic analysis; [Conan packaging and ARM cross-compilation](../../raw/brag/2022-04-06-conan-package-management-embedded-cross-build.md); a [C++ standard chosen on what static analysis can enforce](../../raw/brag/2022-02-18-cpp-safety-critical-embedded-guidelines.md).
- **The closest existing thing to database code**: the 2015 Hive scoring utility, which pushed hundreds of models over billions of rows through `SELECT TRANSFORM` by shipping a Tiny C Compiler to every node and compiling the model *on the fly per invocation* ([resume][primary]). That is query-engine thinking — code generation at execution time — arrived at independently.
- **Data-plane experience**: 1 TB ETL into MS SQL with query optimization and CLR stored procedures; distributed execution research across Hadoop, Spark/PySpark (with pieces re-implemented in Scala) and Dask; [the enterprise warehouse learned well enough to interrogate device telemetry directly](../../raw/brag/2022-05-18-snowflake-edw-device-telemetry.md).
- **Schema judgement under a real constraint**: [diagnosing an unqueryable telemetry JSON schema and authoring the array-based replacement](../../raw/brag/2024-01-20-errorsummary-json-schema-datadog-limitation.md).
- **Deliberate preparation, 2026**: Rust, C++, *Future Database architecture* and **TLA+** worked through as that year's study items, recorded in his own quarterly record — plus "I happen to love relational algebra" from the skills document, which is the giveaway that the interest predates the ambition.

## The gap, and the shortest path

**The gap is one artifact: engine code that someone else runs.** Everything above says "this person could do it"; nothing says "this person has done it". Postings in this field screen on demonstrated depth in one area of the spine, and that is exactly the evidence missing.

Shortest path, in order of cost:

1. **Land one component in an open-source engine** — an index type, an operator, a storage-format detail, a recovery-path fix. Rust-based projects with public issue trackers are the obvious target; prefer one whose data shape he already understands (see the [telemetry-engine candidate](telemetry-engines.md), which is the same move with a domain advantage).
2. **Build a small storage engine and make the concurrency argument the differentiator** — a B+tree or LSM with a written invariant, a TLA+ specification of the concurrent parts, and deterministic simulation tests. That combination turns the thin CV into an unusual one, because most applicants can write the tree and cannot reason about the interleavings. His [concurrency record](../../raw/brag/2023-09-26-audio-service-race-condition-diagnosis.md) makes this authentic rather than academic.
3. **Write up the Hive/TCC utility properly** as the prior art it is. It is currently one resume line for work that would interest an execution-engine team.

## The vocabulary to foreground

Storage engine · B+tree and LSM · query execution and operators · code generation at execution time · transactions and recovery · relational algebra · Rust and modern C++ · memory-safety discipline · concurrency correctness · deterministic simulation testing · TLA+ · columnar and analytical processing.

## Stories to tell for it

- The cross-platform TCP/IP daemon — concurrency learned by building the thing, not by reading about it (no entry yet; resume-sourced, and a [capture gap](../resume/coverage.md)).
- [The race condition never reproduced on demand](../../raw/brag/2023-09-26-audio-service-race-condition-diagnosis.md) — the concurrency story an engine team will actually respond to.
- The Hive scoring utility — on-the-fly compilation, in production for over a year.

## How to tell if this is the one

Spend one weekend on a real issue in a real engine. **If the satisfaction comes from the invariant holding and the benchmark moving — rather than from the feature being usable — this is the one**, and the next step is item 1 above. If the pleasure turns out to be in what the data *means* rather than in how it is stored, the honest answer is [telemetry engines](telemetry-engines.md) or [fleet reliability](device-fleet-reliability.md), which keep the domain and drop the internals.

## Related

- [Telemetry and time-series engine internals](telemetry-engines.md) — the bridge: same discipline, his domain, far shorter path.
- [Dream-job hub](dream-job-hub.md) · [specializations landscape](../analysis/2026-09-13-specializations-landscape.md).

[primary]: ../../../markdown/Oleg.Zhylin.resume.achievements.md "Primary resume (achievements)"
