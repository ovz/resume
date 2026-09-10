# Resume Coverage Map

> **Doc type:** reference
>
> How much of the captured brag material is actually reflected in the primary resume, tracked one claim at a time and grouped into threads. This is the page to read and think with **before** a resume pass — it says what is missing, not what to write. Audience: the owner deciding what to promote; agents drafting resume text or ingesting a brag entry.
>
> Live document: every ingest adds claims, every promotion flips a status. Statuses are judgement calls, not measurements — see *How the number is built*.

## Where it stands

| Measure | Coverage |
|---|---|
| All captured claims | **≈ 40%** — 19 of 48 claims |
| Claims from entries marked `resume-worthy: yes` | **50%** — 10 of 20 claims |

Seventeen claims are fully reflected. Four are gestured at generically. Twenty-seven are absent.

> **Last pass: 2026-09-09.** Added an observability bullet, an architecture-ownership bullet, and a rewritten AI line to the resume; overall coverage moved from ≈ 6% to ≈ 40%. The observability thread went from ≈ 6% to ≈ 64% in a single pass, because one well-built bullet can carry many claims at once when they belong to the same story.

**What this number does not mean.** It is not a grade on the resume. The resume carries 25+ years of work, most of it from before the brag file existed and therefore invisible to this page — Salford Systems, Minitab and the pre-2023 Best Buy Health years are all well represented there and score nothing here. What the number measures is narrower: **how much of the recent, captured 2023–2026 material has reached the resume.**

## How the number is built

Each brag entry decomposes into discrete **claims**: one promotable assertion each, small enough to be either in the resume or not. Every claim gets a status:

| Status | Meaning | Weight |
|---|---|---|
| `in` | The resume makes this claim, specifically enough that a reader would take it away. | 1.0 |
| `partial` | The resume gestures at it generically — the theme is present, this specific claim is not. | 0.5 |
| `absent` | Not in the resume in any form. | 0 |

Coverage is the weighted sum over claim count. `partial` at 0.5 is deliberately crude: the point is a direction of travel, not a metric to optimize. When a promotion lands, flip the status here and mark the entry's ledger row — see *Maintenance*.

## Threads

Brag entries cluster into programmes. A thread is the unit worth thinking about during a resume pass, because a thread usually earns one resume bullet, not eight.

---

### ARC — Architecture ownership across the device portfolio

Current scope, and the most senior claim in the corpus. **No brag entry yet** — these claims come from the owner's direct statement of 2026-09-09, with a brag entry to follow. The April 2026 date is the owner's estimate and may be corrected when that entry lands.

**Entries:** *pending capture.*

**Thread coverage: 100%** (5 of 5) — promoted ahead of capture, which is the reverse of the normal direction and is why the entry is still owed.

| Claim | Source | Status |
|---|---|---|
| `ARC-1` Owns architecture decisions for the Wearables product line, since April 2026 | owner, 2026-09-09 | **in** |
| `ARC-2` Owns architecture decisions for the Handsets product line, since April 2026 | owner, 2026-09-09 | **in** |
| `ARC-3` Remains hands-on as an engineer across every device of GreatCall lineage still carried in the catalogue | owner, 2026-09-09 | **in** |
| `ARC-4` Uses AI-assisted rapid prototyping to become productive on an unfamiliar platform quickly | owner, 2026-09-09 | **in** |
| `ARC-5` Uses AI-assisted exploration to judge an idea's innovation potential early | owner, 2026-09-09 | **in** |

---

### OBS — Device-health observability programme

The largest thread by far: eight entries spanning 2023–2025, tracing one arc from "can we even observe this fleet?" through launch monitoring, statistical tuning, and portfolio stewardship.

**Entries:** [2023-12-21 observability architecture](../../raw/brag/2023-12-21-device-health-observability-architecture.md) · [2024-01-20 telemetry schema](../../raw/brag/2024-01-20-errorsummary-json-schema-datadog-limitation.md) · [2024-03-07 monitoring launch](../../raw/brag/2024-03-07-r5-datadog-monitoring-launch.md) · [2024-04-18 community presentation](../../raw/brag/2024-04-18-r5-datadog-community-presentation.md) · [2024-05-05 anomaly tuning](../../raw/brag/2024-05-05-r5-anomaly-detection-arima-tuning.md) · [2025-01-14 lifecycle review](../../raw/brag/2025-01-14-r5-datadog-monitor-lifecycle-review.md) · [2025-05-01 device investigations](../../raw/brag/2025-05-01-r5-device-specific-failure-investigations.md) · [2025-05-29 anomaly validation](../../raw/brag/2025-05-29-r5-anomaly-monitor-validated-against-mcu-alerts.md)

**Thread coverage: ≈ 64%** (11.5 of 18)

| Claim | Source | Status |
|---|---|---|
| `OBS-1` Co-designed an agentless fleet-wide device-health observability architecture for a resource-constrained embedded fleet | 2023-12-21 | **in** |
| `OBS-2` Drove the vendor feasibility check that ruled out a conventional monitoring agent on RAM budget, closing a dead-end path before investment | 2023-12-21 | **in** |
| `OBS-3` Designed a wide-contract telemetry event so the schema could evolve without a firmware release | 2023-12-21 | absent |
| `OBS-4` Diagnosed an unqueryable telemetry JSON schema and traced it to specific escaping behaviour the platform's attribute rules reject | 2024-01-20 | absent |
| `OBS-5` Authored the array-based schema-change proposal that unblocked quantitative monitoring of the primary device health signal | 2024-01-20 | absent |
| `OBS-6` Designed and shipped a new device's launch monitors and dashboard, becoming the team's automated alerting layer | 2024-03-07 | **in** |
| `OBS-7` Caught device and firmware issues — including a battery-overheating condition — before customer reports | 2024-03-07 | partial |
| `OBS-8` Resolved platform-level blockers directly with the observability vendor's Premier Support engineering | 2024-03-07 | absent |
| `OBS-9` Presented the observability programme to a cross-team engineering community of practice | 2024-04-18 | **in** |
| `OBS-10` Identified a misbehaving production device live on stage during that session | 2024-04-18 | absent |
| `OBS-11` Applied ARIMA/SARIMA theory to tune fleet-scale anomaly monitors, reasoning about the statistics rather than treating the feature as a black box | 2024-05-05 | **in** |
| `OBS-12` Established empirically that partitioning the anomaly model by error category sharply cuts false positives, and validated the hypothesis against real incident data | 2024-05-05 | **in** |
| `OBS-13` Initiated a monitor-lifecycle review, securing retirement of a superseded monitor while tying cleanup to its replacement's stability | 2025-01-14 | **in** |
| `OBS-14` Extended ownership from building monitors to stewarding the portfolio's relevance and boundaries | 2025-01-14 | **in** |
| `OBS-15` Converted broad fleet alerts into device-level investigations identifying individual units driving error activity | 2025-05-01 | **in** |
| `OBS-16` Supplied focused evidence for recovery, replacement and defect-classification decisions with firmware partners | 2025-05-01 | partial |
| `OBS-17` Validated an anomaly monitor's first meaningful firing by correlating it with independent MCU alerts from firmware engineering | 2025-05-29 | **in** |
| `OBS-18` Established an evidence-based observation loop for judging a monitor's ongoing usefulness | 2025-05-29 | partial |

> `OBS-7` is deliberately `partial`: the resume claims the catch but not the battery-overheating specific, which names a safety-adjacent defect in a current employer's product. See *Open sensitivity question* below.

---

### POS — Positioning and location

Three entries, 2024–2026, moving from field diagnostics to owning the architecture.

**Entries:** [2024-05-15 positioning root cause](../../raw/brag/2024-05-15-skyhook-positioning-root-cause-diagnostics.md) · [2025-11-15 location engine](../../raw/brag/2025-11-15-r5-location-engine-design.md) · [2026-09-01 beacon FOTA persistence](../../raw/brag/2026-09-01-r5-beacon-tracking-fota-persistence.md)

**Thread coverage: ≈ 6%** (0.5 of 9)

| Claim | Source | Status |
|---|---|---|
| `POS-1` Root-caused a recurring positioning-library failure — a multithreading fault losing the location fix — via telemetry log correlation | 2024-05-15 | partial |
| `POS-2` Identified the missing service-restart step that left the fallback path unable to fully recover affected devices | 2024-05-15 | absent |
| `POS-3` Reinterpreted an existing error-count signal as a proxy for time-without-fix, changing how the team thresholds it | 2024-05-15 | absent |
| `POS-4` Architected a modular location engine unifying beacon, GPS and Wi-Fi behind per-provider interfaces | 2025-11-15 | absent |
| `POS-5` Built the state-management layer arbitrating between sources, with fallback when a provider fails | 2025-11-15 | absent |
| `POS-6` Documented design and interfaces so other teams can extend the engine for new device variants | 2025-11-15 | absent |
| `POS-7` Designed schema-backed persistence restoring paired beacon state across firmware-over-the-air updates | 2026-09-01 | absent |
| `POS-8` Kept devices in low-power beacon presence detection after updates instead of high-frequency polling, protecting battery life fleet-wide | 2026-09-01 | absent |
| `POS-9` Hardened beacon/FOTA error categorization and made MCU reboot/fatal handling deliberate rather than incidental | 2026-09-01 | absent |

> Now the weakest thread relative to its weight. The resume's positioning bullet still describes the 2024 Qualcomm/Skyhook infrastructure upgrade; the 2025 engine architecture and the 2026 beacon work remain absent.

---

### FW — Embedded platform frameworks

**Entries:** [2026-04-26 CCF capability framework](../../raw/brag/2026-04-26-ccf-capability-framework-lcm-open-source.md) · cross-listed: [2026-09-01 beacon FOTA persistence](../../raw/brag/2026-09-01-r5-beacon-tracking-fota-persistence.md) (claims tracked under POS)

**Thread coverage: 0%** (0 of 4)

| Claim | Source | Status |
|---|---|---|
| `FW-1` Led design and delivery of a capability and configuration framework standardizing capability management across device SKUs | 2026-04-26 | absent |
| `FW-2` Implemented dependency injection and hierarchical state machines with predictable lifecycle management in embedded C | 2026-04-26 | absent |
| `FW-3` Built an aligned structured-logging framework giving consistent logs across all supported devices | 2026-04-26 | absent |
| `FW-4` Modularized and documented the framework for open-source release and external contribution | 2026-04-26 | absent |

> Still entirely unrepresented, and the only open-source-facing work in the corpus.

---

### AI — AI adoption and agentic engineering

**Entries:** [2025-10-29 AI data product](../../raw/brag/2025-10-29-ai-data-product-in-alation.md) · [2026-05-26 agentic engineering](../../raw/brag/2026-05-26-ai-adoption-agentic-engineering-choreographer.md)

**Thread coverage: ≈ 29%** (2 of 7)

| Claim | Source | Status |
|---|---|---|
| `AI-1` Scoped an AI-enabled data product on the enterprise data catalog to test whether warehoused device-event tables earn their storage and cellular cost | 2025-10-29 | absent |
| `AI-2` Combined lineage, query-log usage, glossary metadata and chat-with-your-data exploration into one cost-aware proposal | 2025-10-29 | absent |
| `AI-3` Designed and shipped a multi-agent orchestration layer as an agent plugin, preventing context overflow through delegation | 2026-05-26 | **in** |
| `AI-4` Established a persistent, versioned knowledge base (raw capture → synthesis → index) for the engineering organization | 2026-05-26 | **in** |
| `AI-5` Developed and documented prompt and agent patterns that cut token consumption while holding output quality | 2026-05-26 | absent |
| `AI-6` Integrated agents into code review, documentation and release-note workflows | 2026-05-26 | absent |
| `AI-7` Delivered outcomes at roughly three times the expected rate using AI since 2023 | 2026-05-26 | absent |

> `AI-7` was `in` until 2026-09-09 and was **deliberately retired** from the resume, not lost: an unverifiable productivity multiplier was replaced by what was actually built (`AI-3`, `AI-4`). The claim stays on this page because the underlying fact is still true and the owner may want it back — see *Open questions*.

---

### RSK — Risk, security and process practice

**Entries:** [2023-08-03 risk management analysis](../../raw/brag/2023-08-03-risk-management-practice-early-analysis.md) · [2023-09-30 patch management SOP](../../raw/brag/2023-09-30-security-patch-management-sop-and-vendor-engagement.md)

**Thread coverage: 0%** (0 of 5)

| Claim | Source | Status |
|---|---|---|
| `RSK-1` Analyzed the Quality organization's risk-management practice and found planning limited to one line of business and largely qualitative | 2023-08-03 | absent |
| `RSK-2` Proposed risk appetite as the foundation for a unified, quantitatively-informed, org-wide approach | 2023-08-03 | absent |
| `RSK-3` Drafted a NIST-grounded enterprise patch-management SOP for the fleet's embedded Linux firmware | 2023-09-30 | absent |
| `RSK-4` Root-caused firmware staleness to an ODM's immediate-patch policy, informing a deliberate risk-based cadence | 2023-09-30 | absent |
| `RSK-5` Initiated vendor security-feed engagement to formalize vulnerability-patch notification ahead of a device launch | 2023-09-30 | absent |

> The resume's security material is all from the 1996–2000 cryptography era. This thread is the only evidence of *current* security and risk practice, and it is invisible.

---

## What this says right now

1. **The gap moved.** Observability and current architecture scope are now represented. The remaining concentration is **positioning and firmware architecture** — `POS-4` through `POS-9` and all of `FW` are nine absent claims describing the most recent hands-on engineering in the corpus.
2. **`FW` and `RSK` are still at zero.** Between them they hold the only open-source-facing work and the only current security-practice evidence.
3. **`ARC` is promoted but uncaptured**, which inverts the normal direction of the pipeline. The resume now asserts something the knowledge layer cannot source. That is acceptable briefly — the owner is the authority on their own scope — but the brag entry is genuinely owed.
4. **Five entries remain un-ingested**, so `OBS-13`, `OBS-14`, `AI-3` and `AI-4` are marked promoted here while carrying no ledger row at all — see [brag-ledger.md](../sources/brag-ledger.md).

## Open questions

- **`OBS-7`, battery overheating.** The brag entry records catching a battery-overheating condition before customers reported it. The resume claims the catch generically instead, because naming a safety-adjacent defect in a current employer's product is arguably unfair disclosure under [sensitivity tiers](../workflows/sensitivity-tiers.md) § *T2*. Applying the conservative reading was an agent's call; the owner may overrule it, and either way the tier page should say explicitly how to treat a defect one caught oneself.
- **`AI-7`, the productivity multiplier.** Retired from the resume in favour of capability claims. Restorable if the owner wants a quantified line back.

## Maintenance

- **On ingest:** add the entry's claims to its thread, or open a thread if it starts one. New claims default to `absent`. Assign the entry to exactly one primary thread; cross-list it under others without duplicating its claims.
- **On promotion:** when resume text lands, flip the affected claims to `in` or `partial` in the same edit, and set the entry's ledger promotion status. Recompute the thread and headline numbers.
- **Recompute:** counts are maintained by hand and are meant to be approximate. If they drift, recount from the tables — the tables are the source of truth, the headline figures are derived.
- Claim IDs are stable and never reused. A claim that turns out to be wrong is struck, not deleted, so anything citing it still resolves. A claim retired from the resume returns to `absent` rather than being removed.

## Related

- [Update the outward-facing resume](update-workflow.md) — the pass this page feeds.
- [Primary resume — structure and cut points](primary-resume.md) — where a promoted claim has to fit.
- [Accomplishments by domain](../concepts/accomplishments-by-domain.md) — the same material organized for drafting rather than for gap-spotting.
- [Brag ledger](../sources/brag-ledger.md) — ingest and promotion state per entry.
- [Brag file workflow](../workflows/brag-file.md) — capture and ingest.
