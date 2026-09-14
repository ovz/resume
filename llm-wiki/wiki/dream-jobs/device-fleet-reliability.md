---
title: "Connected-device fleet reliability and cost"
dream-job: DJ-5
origin: suggested
specialization: established
evidence: strong
horizon: now
fits: [embedded, data, observability, crisis, product]
status: candidate
---

# ○ Connected-device fleet reliability and cost

> **Doc type:** reference · **origin: suggested** — proposed by an agent on 2026-09-13 from this repository's observability and cost record. Not the owner's idea.

## The job

Owning whether a fleet of shipped devices behaves, and what it costs to run: telemetry design, monitors and anomaly detection, incident response and runbooks, firmware-update health, and the operating cost of connectivity and storage. Titles vary — device reliability engineer, IoT SRE, fleet platform lead, operational-excellence owner — and the work is recognisably SRE with the constraint that you cannot ssh into the thing.

## Under the Value and Impact tests

**Cost centre — and this is where the corrected test bites hardest.** Reliability and cost-of-operation work is funded by austerity reasoning, which is precisely the pragmatic reasoning the [Innovation test](dream-job-hub.md) screens out; the owner's own note from inside the job says the same thing, that a path to profitability framed as austerity is not where future margin comes from. **As stated, this candidate fails Impact** despite having the strongest evidence in the hub.

The exception is real and worth hunting for: at a company whose **fleet is the product** — where reliability drives renewal, churn and warranty rather than an internal budget line — the same work is product-adjacent, and this portfolio is then exceptional rather than merely strong.

## Why it is a real field

Field guidance for 2026 describes the signal set plainly — "crash dumps (or core dumps), reboot reasons, connectivity state transitions, memory usage, performance metrics, and any custom device behavior signals" — collected inside "limited RAM and flash memory, intermittent connectivity, constrained power budgets, and sometimes … extremely low-bandwidth networks". Industry commentary notes teams leaning on specialists "who understand modem behavior, radio conditions, power optimization, firmware idiosyncrasies, and complex debugging". That is a role defined by its constraints, which is why it is hard to hire. Sources: [specializations landscape](../analysis/2026-09-13-specializations-landscape.md) § *Connected-device fleet reliability*.

## What the record already supports

This is the most completely evidenced candidate in the hub — eighteen coverage claims and eight brag entries in one thread, plus the cost work:

- **The architecture decision at the start**: [agentless device-health observability, chosen after personally driving the feasibility check that ruled out a monitoring agent on RAM budget](../../raw/brag/2023-12-21-device-health-observability-architecture.md), with a wide-contract telemetry event so the schema could evolve without a firmware release.
- **The unglamorous blocker nobody else found**: [the primary health signal was unqueryable because of the schema's quote-bearing keys; he diagnosed it and authored the array-based replacement](../../raw/brag/2024-01-20-errorsummary-json-schema-datadog-limitation.md).
- **Monitors that caught real defects before customers did**, including a battery-overheating condition, with platform blockers resolved directly with the vendor's Premier Support ([2024-03-07](../../raw/brag/2024-03-07-r5-datadog-monitoring-launch.md)).
- **Statistics done properly**: [ARIMA/SARIMA reasoning and an empirically validated per-category partition that cut false positives](../../raw/brag/2024-05-05-r5-anomaly-detection-arima-tuning.md), then [validated against independent MCU alerts](../../raw/brag/2025-05-29-r5-anomaly-monitor-validated-against-mcu-alerts.md).
- **Portfolio stewardship, not just construction**: [a monitor-lifecycle review retiring a superseded monitor while tying cleanup to its replacement's stability](../../raw/brag/2025-01-14-r5-datadog-monitor-lifecycle-review.md).
- **From fleet signal to individual unit**: [identifying the devices that disproportionately drove error activity and giving firmware partners focused questions](../../raw/brag/2025-05-01-r5-device-specific-failure-investigations.md).
- **Cost, in money**: [finding devices burning cellular data, agreeing the rogue threshold in advance, writing the runbook, and making replacement-plus-root-cause routine](../../raw/brag/2024-01-04-cellular-cost-rogue-device-detection.md).
- **Crisis credentials**: [the 2019 recall, where telemetry is what turned "which devices are affected?" from argument into measurement](../../raw/brag/2019-08-30-r4-cpsc-recall-and-relaunch.md), and [the FOTA escalation under an inventory crisis](../../raw/brag/2025-07-18-fota-vendor-escalation-lively-mobile2.md).
- **Readiness argued from first principles**: [challenging a mandated launch-readiness control and substituting chaos-style testing where the failures actually live](../../raw/brag/2023-12-05-operational-excellence-launch-readiness.md).

## The gap, and the shortest path

**No gap in capability.** The honest gaps are: the tooling is one vendor's (a platform migration would be learning, not a leap); the fleet is tens of thousands of devices rather than millions; and — the real one — **this is the candidate closest to what he already does**, so it scores lowest on the hub's *Innovation* test.

Shortest path: none needed. The question is not whether he could get such a role; it is whether it would be a dream job or a lateral move. It becomes a dream job at a company where the fleet is the product and the scale is an order of magnitude larger, or where the role is to *build* the practice rather than to run one that exists.

## The vocabulary to foreground

Fleet observability · agentless telemetry · wide-contract events · anomaly detection and false-positive control · monitor lifecycle · runbooks and incident response · tabletop exercises · FOTA health · cost of operation · device-level root cause.

## Stories to tell for it

- The observability arc end to end: RAM budget → unqueryable schema → launch monitors → tuned anomaly detection → portfolio stewardship. One story with five scenes.
- [The rogue device at a gigabyte a day](../../raw/brag/2024-01-04-cellular-cost-rogue-device-detection.md) — observability that paid for itself in money.
- [The device caught misbehaving live on stage](../../raw/brag/2024-04-18-r5-datadog-community-presentation.md) — the story that makes everything else believable.
- [The recall](../../raw/brag/2019-08-30-r4-cpsc-recall-and-relaunch.md) — for any interviewer who wants to know how he behaves under a hard deadline.

## How to tell if this is the one

**Ask whether the next thing would be new.** If a role offers the same practice at ten times the scale, or a greenfield practice at a company that has none, it passes the Innovation test. If it offers a mature practice to maintain, it fails — and the failure is the point of grading this candidate rather than assuming its strong evidence makes it best.

## Related

- [Telemetry and time-series engine internals](telemetry-engines.md) — the same domain one layer down, for when the interesting part is the data plane.
- [Dream-job hub](dream-job-hub.md) · [specializations landscape](../analysis/2026-09-13-specializations-landscape.md).
