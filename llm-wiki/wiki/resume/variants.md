# Tailored resume variants — inventory, priority and what feeds each

> **Doc type:** reference
>
> One page per question "which resume do I send, and what does each one draw on". It lists the variants that exist, the ones planned in priority order, and for each the coverage threads, brag entries, story clusters and dream-job candidates that supply it — so authoring or refreshing a variant loads **this page plus the named shards** and never re-summarizes the career from scratch. Audience: the owner choosing a document; an agent drafting or refreshing a variant. Tier **T1**; every variant itself is **T0 public**.
>
> Procedure for making or editing a variant, the shared `_parts/` fragments and the build: [update workflow](update-workflow.md) § *Tailored variants*. Depth and cut rules every variant inherits: [primary resume](primary-resume.md).

## The tiering behind this page

On 2026-09-19 the owner ran Microsoft Copilot over his Best Buy work mailbox and asked it to tier the record into resume tracks. Its answer — four tiers, each with the brag-file themes and keywords it saw recurring — is preserved verbatim in the maintainer's session scratch and is the external assessment this page reconciles against the wiki's own evidence. The tiers and the wiki agree on the shape; where they differ is noted per variant below.

| Tier | Track | Copilot's verdict | This repository's position |
|---|---|---|---|
| 1 | Embedded Systems / Device Software Engineer | "your strongest body of evidence" | Agrees. Already the [embedded variant](../../../markdown/Oleg.Zhylin.resume.embedded.md); [devices shard](coverage/devices.md) is 47/48 covered. |
| 2 | Network Software Product Engineer | "probably your most marketable secondary specialization" — strongest when about production telemetry, field devices, communication paths, **not** datacenter networking | Agrees, with a correction: the record also holds a **client/server network-programming** root (the 2004–2005 TCP/IP daemon, `CONC`) that a mailbox survey cannot see, so the variant is *network software engineer* with both the transport-programming and the fleet-telemetry legs. **Live since 2026-09-20.** |
| 3 | Data Engineer for AI | "the corrected category" — not "Data Engineer", "definitely not Observability Engineer"; the recurring role is making data *exist, be trustworthy, be collected correctly and be consumable* for Data Science | Agrees with the framing and the exclusion. The wiki adds the Salford/Minitab ML-product decade (`SALF`, big-data R&D) as a second leg the mailbox cannot see. **Planned next.** |
| 4 | Operational Excellence / Reliability Engineering | "not a primary resume track, but a useful supporting theme" | Agrees. `OBS`, `COST`, `CRISIS` become bullets inside tiers 1–3 — the shared [`bullet-operational-excellence.md`](../../../markdown/_parts/bullet-operational-excellence.md) fragment is exactly this. Never a standalone variant. |

The assessment is an input, not a source of claims: nothing on it enters a resume unless a brag entry and its coverage row support it.

## Inventory

| Priority | File | Audience | Status |
|---|---|---|---|
| — | `Oleg.Zhylin.resume.achievements.md` | General — the primary, mirrored to LinkedIn | live |
| — | [`Oleg.Zhylin.resume.compact.md`](../../../markdown/Oleg.Zhylin.resume.compact.md) | Any submission with a page limit — the primary under a 7-page budget, not an audience | live, 2026-10-07 |
| — | `Oleg.Zhylin.resume.embedded.md` | Principal Engineer, C++/Rust, embedded, owning operational excellence | live (Tier 1) |
| — | [`Oleg.Zhylin.resume.networking.md`](../../../markdown/Oleg.Zhylin.resume.networking.md) | Network software engineer — device-side transport, cellular, fleet telemetry | live (Tier 2), 2026-09-20 |
| **1** | `Oleg.Zhylin.resume.data-ai.md` | Data Engineer for AI / ML / Data Science enablement | planned (Tier 3) |
| Owner-requested | [`Oleg.Zhylin.resume.engineering-manager.md`](../../../markdown/Oleg.Zhylin.resume.engineering-manager.md) | Engineering Manager with hands-on technical depth and risk-informed delivery | live; one management variant |

A variant that is retired leaves this table for [archive-source](../workflows/archive-source.md). The primary is always the safe default when a posting's centre of gravity is unclear, and its compact edition when the submission caps the length ([choosing a variant](update-workflow.md#choosing-a-variant-to-submit)).

## How variants relate to each other

- **The primary is the union; a variant is a re-weighting.** Every claim a variant makes is also true of the primary's subject and traces to the same brag entry. A variant may say less or reorder; it never says something the record does not support just because the audience would like it.
- **One fact, one home.** Text that must read identically everywhere lives in `markdown/_parts/`; text a variant should be free to phrase differently is inlined. The test and the fragment list: [update workflow](update-workflow.md#keeping-variants-from-drifting).
- **What also appears on LinkedIn is shared by default, and tailoring overrides it.** This is the owner's rule, stated 2026-10-07. The best and most effective employers take what they need from the LinkedIn profile, and a resume file is mostly a formality, the copy on record in case the profile's content ever goes away. So the LinkedIn text (*My Story* and the Experience sections) and the common plugs (the shared achievement bullets) are shared as fragments with every variant that can carry them unchanged. A better-tailored resume still matters more than a lower maintenance cost, so a variant tailored to an audience inlines its own version wherever its audience needs a different one. The [compact variant](#compact-page-limited-submissions--live) is the third case: it serves a constraint rather than an audience, so it shares everything the constraint allows. LinkedIn's own limits are not negotiable either way, because the profile generates leads and application systems such as Workday import from it.
- **Coverage measures the primary.** A claim promoted only into a variant does **not** flip its status in the [coverage map](coverage.md); it is recorded in the variant's *draws on* list below and in the entry's ledger row. Otherwise the coverage number stops meaning "reached the public resume".
- **No variant contradicts another.** Dates, team sizes, titles and the role of each era are the same words or the same facts in different words. A discrepancy found in one variant is fixed in the source of truth — the brag entry or the primary — and then in every variant.
- **Adding a variant does not touch the existing ones.** The embedded variant and the primary are not rebalanced to make room for the networking one; each is judged against its own audience.

## Variant briefs

Each brief is the loading list for one variant. When drafting, open this section, then only the shards and pages it names.

### Embedded Systems / Device Software Engineer — live

- **Centre of gravity:** Principal-level ownership of a connected medical-alert device portfolio; C++ on embedded Linux; safety-critical discipline; manufacturer boundary.
- **Coverage threads:** `ARC`, `FALL`, `INT`, `FW`, `DEV`, `MED`, `MFG` ([devices](coverage/devices.md)); `POS`, `PWR` ([positioning-power](coverage/positioning-power.md)); `BOOST`, `BLD` ([engineering](coverage/engineering.md)); `CONC` ([reliability](coverage/reliability.md)).
- **Domain synthesis:** [accomplishments by domain](../concepts/accomplishments-by-domain.md) §§ *Embedded and safety-critical devices*, *Positioning and location*, *Battery, power and cost of operation*, *Build, release, CI/CD*.
- **Stories:** [positioning](../stories/positioning.md), [concurrency](../stories/concurrency.md), [state machines](../stories/state-machines.md).
- **Dream-job candidates it serves:** `DJ-2`, `DJ-3`, `DJ-6`, `DJ-8`, `DJ-9` in the [hub](../dream-jobs/dream-job-hub.md).
- **Keywords the assessment saw recurring:** Embedded Linux, Location Services, Qualcomm SDK, GNSS, Device Telemetry, Production Debugging, Firmware Validation, Root Cause Analysis, OEM Integration.
- **What it must not become:** a list of every Best Buy Health project. It already cuts *Projects Overview* to *Selected Projects*; keep it there.

### Network software engineer — live

- **Centre of gravity:** two legs, told as one arc. **Transport programming:** the cross-platform TCP/IP predictive-analytics daemon (2004–2005), HTTP transfer callback ownership, cellular MQTT traffic scheduling, fire-and-forget HTTPS reporting with SMS as the degraded-mode path. **Fleet telemetry over cellular:** radio-quality indication, cellular cost and rogue-device detection, device-health observability, the Qualcomm/Skyhook Device Observability evaluation. Location services (`POS`) are the domain the transport serves.
- **Coverage threads:** `CONC`, `OBS`, `COST` ([reliability](coverage/reliability.md)); `POS`, `PWR` ([positioning-power](coverage/positioning-power.md)); `INT` ([devices](coverage/devices.md)).
- **Brag entries to draw on:** [2004-01-01 TCP/IP daemon](../../raw/brag/2004-01-01-spm-client-server-tcpip-daemon.md), [2023-04-06 cellular radio quality](../../raw/brag/2023-04-06-cellular-radio-quality-service-indication.md), [2023-12-21 observability architecture](../../raw/brag/2023-12-21-device-health-observability-architecture.md), [2024-01-04 cellular cost and rogue devices](../../raw/brag/2024-01-04-cellular-cost-rogue-device-detection.md), [2025-12-07 HTTP transfer callback ownership](../../raw/brag/2025-12-07-http-transfer-callback-ownership.md), [2026-01-01 Qualcomm Device Observability evaluation](../../raw/brag/2026-01-01-qualcomm-device-observability-evaluation.md), [2026-07-29 cellular MQTT scheduling](../../raw/brag/2026-07-29-cellular-mqtt-traffic-scheduling.md), [2026-09-01 beacon tracking and FOTA persistence](../../raw/brag/2026-09-01-r5-beacon-tracking-fota-persistence.md), [2026-09-20 network programming foundations and mentors](../../raw/brag/2026-09-20-network-programming-foundations-and-mentors.md), [2025-01-16 phone capability SDK over LCM](../../raw/brag/2025-01-16-ccfphone-r5-device-lcm-odm-integration.md), [2024-05-08 component framework and the LCM case](../../raw/brag/2024-05-08-ccf-capability-framework-lcm-open-source.md).
- **Domain synthesis:** [accomplishments by domain](../concepts/accomplishments-by-domain.md) § *Networking and transport* — created 2026-09-20 for exactly this reason, because the record had been spread across four half-views and a variant cannot be drafted from those. Then §§ *Operational excellence and observability*, *Battery, power and cost of operation*, *Positioning and location*.
- **Problem-space read:** [four problems, four solutions](../concepts/four-problems.md) § *Networking* — Russ White's model with this record's answer to each. The rehearsal aid for an interview in this domain, and the place the routing gap is named.
- **Stories:** [concurrency](../stories/concurrency.md) (the daemon), [positioning](../stories/positioning.md).
- **Dream-job candidates it serves:** `DJ-5` first, then `DJ-3` and `DJ-7`.
- **Keywords the assessment saw recurring:** Network Software Engineer, Telemetry Architecture, Reliability Engineering, Location Services, Fleet Monitoring, Distributed Systems, Cellular Communications.
- **Framing the assessment got right and the variant must keep:** device-side and fleet-side networking under real constraints — power, cost per byte, intermittent radio — not datacenter or campus networking.
- **The foundations are now captured**, which is what unblocked the draft: Stevens for the programming, Russ White for the engineering read, and a mentor on the enterprise networking side. Per [sensitivity tiers](../workflows/sensitivity-tiers.md) rule 1, the published authors are named in the variant and **the colleagues are not** — the book arrives via "a colleague", the mentor does not appear at all.
- **The gap is stated in the document itself.** The variant says outright that there is no routing-protocol or switch-configuration practice, and turns never having specialized into the positioning argument the owner actually makes: arriving from the programming side, with White's problem-first framing, means arriving without the received practice. That sentence is load-bearing — do not soften it into a hedge or delete it as a weakness.
- **What it must not become:** a network-*administration* resume. No routing-protocol or switch-configuration claims exist in the record.

### Data Engineer for AI — planned, priority 2

- **Centre of gravity:** making data exist, be trustworthy, be collected correctly and be consumable by Data Science and analytics — from device telemetry instrumentation and schema design through warehouse access and governance to the ML-product decade at Salford Systems where the owner built the tools data scientists used.
- **Coverage threads:** `DATA`, `STAT` ([data](coverage/data.md)); `STEW` ([leadership](coverage/leadership.md)); `OBS` as data collection rather than operations ([reliability](coverage/reliability.md)); `SALF` ([engineering](coverage/engineering.md)).
- **Brag entries to draw on:** [2010-05-01 NCS-R data preparation](../../raw/brag/2010-05-01-ncs-r-sas-data-preparation-pharma-client.md), [2013-01-01 Carrefour promotion optimization](../../raw/brag/2013-01-01-carrefour-c4-promotion-optimization-brazil.md), [2014-01-01 CloudSML big-data R&D](../../raw/brag/2014-01-01-cloudsml-cloudspm-bigisle-big-data-rd.md), [2022-05-18 Snowflake EDW and device telemetry](../../raw/brag/2022-05-18-snowflake-edw-device-telemetry.md), [2024-01-20 ErrorSummary JSON schema](../../raw/brag/2024-01-20-errorsummary-json-schema-datadog-limitation.md), [2024-05-05 anomaly detection tuning](../../raw/brag/2024-05-05-r5-anomaly-detection-arima-tuning.md), [2025-01-01 Data Steward](../../raw/brag/2025-01-01-data-steward-enterprise-data-catalog.md), [2025-10-29 AI data product in Alation](../../raw/brag/2025-10-29-ai-data-product-in-alation.md), [2026-05-17 statistical bar and Data Science partnership](../../raw/brag/2026-05-17-statistical-bar-and-data-science-partnership.md).
- **Domain synthesis:** [accomplishments by domain](../concepts/accomplishments-by-domain.md) §§ *Data engineering*, *ML products and GUIs*, *Big data and distributed ML*, *Operational excellence and observability*.
- **Stories:** [salford](../stories/salford.md), [stewardship](../stories/stewardship.md).
- **Dream-job candidates it serves:** `DJ-7` first, then `DJ-4`.
- **Keywords the assessment saw recurring:** Data Engineering, Telemetry Pipelines, Data Quality, Instrumentation, Analytics Infrastructure, AI Enablement.
- **Framing the assessment got right and the variant must keep:** the owner is usually *not* the data scientist; he is the engineer the data scientist depends on. Say so plainly — it is the honest and the more marketable claim.
- **What it must not become:** "Observability Engineer" (the assessment's explicit exclusion) or a generic "Data Engineer" with a Spark/Airflow keyword list the record does not support. The [data shard](coverage/data.md) is 3/16 covered on the primary; expect this variant to promote more new claims than the networking one.

### Engineering Manager - Live

- **Document and provenance:** [management resume](../../../markdown/Oleg.Zhylin.resume.engineering-manager.md), [source and claim map](../sources/resume-engineering-manager.md). Variant-only promotions do not change primary coverage.
- **Centre of gravity:** distributed-team delivery, coaching and quality, architecture judgement and cross-functional risk decisions. Retain the hands-on security-trained engineer; do not turn the voice into a generic management profile.
- **Owner's direction, 2026-09-22:** one Engineering Manager variant is sufficient across prospective career directions. Risk Engineer is a capability track, explicitly not a dream job. This does not change the existing Data Engineer for AI priority or create a Risk Engineer resume.
- **Loading list:** [risk-engineering track record](../concepts/risk-engineering-track-record.md); [domain synthesis](../concepts/accomplishments-by-domain.md) sections *Leadership, management, hiring*, *Risk management and compliance*, *Quality and test automation*, *Security, cryptography, licensing*; `LEAD`, `QA`, `RSK`, `STEW` in [leadership coverage](coverage/leadership.md). Established delivery and team scale come from the [primary resume](../../../markdown/Oleg.Zhylin.resume.achievements.md).
- **Draws on:** [2023 risk-practice analysis](../../raw/brag/2023-08-03-risk-management-practice-early-analysis.md), [patch SOP](../../raw/brag/2023-09-30-security-patch-management-sop-and-vendor-engagement.md), [readiness challenge](../../raw/brag/2023-12-05-operational-excellence-launch-readiness.md), [test-automation mentorship](../../raw/brag/2024-12-31-device-test-automation-robot-framework.md), [quality-work triage](../../raw/brag/2021-06-29-engineering-excellency-and-meeting-facilitation.md), [data-governance framework](../../raw/brag/2025-11-13-column-mapping-framework-alation-data-governance.md), [firmware escalation](../../raw/brag/2025-07-18-fota-vendor-escalation-lively-mobile2.md).
- **Boundaries:** historical titles unchanged; teams up to 15 is not a claim of 15 direct reports. No invented budget, hiring volume, performance-review authority, current formal manager role or enterprise risk ownership. The report's retail experiments, data migration and recovery-plan claims stay out pending attribution. No "process wars" language outward.
- **Career continuity:** the earlier [Staff Engineer positioning](../../raw/brag/2025-04-01-staff-engineer-behaviors-principal-positioning.md) records reservations about a management track. Preserve that historical view; the owner's newer request authorizes a management variant, not a rewrite claiming management was always the goal.

### Compact (page-limited submissions) — live

- **Document and provenance:** [compact resume](../../../markdown/Oleg.Zhylin.resume.compact.md), [source and claim map](../sources/resume-compact.md). The map carries the page-budget measurement and a row per bullet naming the primary text it condenses.
- **Centre of gravity:** none of its own. It is the primary under a page budget, for any submission whose system caps the length. The first case was a recruiter's ten-page limit, most likely applied to the DOCX as their system renders it, and the primary renders at about eighteen pages.
- **Budget:** at most **7 pages as a DOCX opened in LibreOffice**, which leaves about 30% headroom under a 10-page cap for Word, an ATS conversion or A4 paper. Re-measure after any change to its text or to a fragment it includes; the method is on the claim map.
- **Shape:** *My Story* is the shared fragment, word for word the LinkedIn About. The achievements are condensed to sixteen bullets in three groups, and the employment history is one short paragraph per period that names the period's threads and leaves the elaboration to the achievements. *Projects Overview* is omitted, and an invitation line offers its stories and the full edition.
- **Draws on:** the primary only. It promotes nothing, so coverage and the brag ledger do not change when it does.
- **Maintenance:** a change lands in the primary first. The claim map then shows which compact bullet condenses the changed section, if any. *My Story* and the shared bullets arrive on their own, which is why the page count is re-measured after any fragment changes.
- **What it must not become:** a variant with claims or a voice of its own, or the place where new material lands first. If an audience-specific short resume is ever needed, that is a tailored variant with its own brief.

## Maintenance

- **New brag entry:** if it clearly serves a planned or live variant, add it to that brief's *draws on* list in the same ingest edit — this is the cheap step that keeps variant work from re-surveying the brag file.
- **New variant:** add the inventory row and a brief here **before** drafting the file, so the loading list exists when the drafting agent needs it. Register the file in [sources.md](../sources.md) and give it a `wiki/sources/` summary page when it goes live.
- **Re-tiering:** a later external assessment (another mailbox pass, a recruiter's read) is appended as a dated row to *The tiering behind this page*, not substituted; the priority column in *Inventory* is the owner's call.
- **Size:** if a brief outgrows a screen, move it to `variants/<audience>.md` and leave a row here — the same rule the coverage map applies to shards.

## Related

- [Update the outward-facing resume](update-workflow.md) — how a variant is made, shared fragments, choosing one to submit.
- [Primary resume — structure and cut points](primary-resume.md) — the depth rules every variant inherits.
- [Resume coverage map](coverage.md) — the claim tables each brief points into.
- [Dream-job hub](../dream-jobs/dream-job-hub.md) — the directions each variant is meant to open.
- [Voice and prominence](../workflows/voice-and-prominence.md) — one voice across every variant.
