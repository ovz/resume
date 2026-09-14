# Emerging and established specializations, as of September 2026

> **Doc type:** explanation
>
> External evidence that the specializations named in the [dream-job hub](../dream-jobs/dream-job-hub.md) are real markets rather than plausible-sounding ideas. Audience: the owner or an agent weighing a direction; anyone re-checking whether a candidate has aged well. Tier **T1**.
>
> **Read on 2026-09-13.** Five sources were opened and read directly; the rest are search-result summaries and are marked as such in the ledger. Nothing here is a salary recommendation — see *What this page deliberately does not say*.

## Why this page is separate from the hub

The hub answers "would this be a good job for this person", which is a judgement about a career and changes slowly. This page answers "is anyone actually doing this in 2026", which is a fact about a market and **goes stale within a year**. Keeping them apart means the hub can be re-read without re-litigating the market, and the market can be refreshed without rewriting the hub. It is dated in its filename for the same reason employer research is.

## The specializations

### Database and query-engine internals — established, and mid-rewrite

The discipline is old; what is new is that a visible share of new engines are being written in **Rust**, which reopens the field to systems engineers who never worked at a database vendor. A representative 2026 posting asks for "meaningful experience working on databases, query engines, storage engines, indexing systems, or similarly complex infrastructure software", names **Rust** as the primary language with C/C++/Zig accepted as evidence of systems ability, and scopes the work as storage, indexing, query planning and execution — with contribution to open-source engine components treated as part of the job. The generic shape of these roles is **depth in one area of the engine spine**: front end, planner/optimizer, operators, storage engine, transactions and recovery, or scale-out. Notable Rust-based engines named across the ecosystem in 2026 include InfluxDB 3 (Arrow, DataFusion, Parquet), Turso's SQLite reimplementation, Materialize, Databend, Quickwit and ParadeDB.

**Why it is reachable without a database CV:** the entry path is a component, not a product — an index type, an operator, a WAL, a storage format — and open-source engines accept that work from outside.

### Time-series and telemetry engines — the IoT-shaped corner of the same field

The same discipline, aimed at the data shape this career already produces: device events, carrier statistics, fixes, error counts. The 2026 comparisons place **QuestDB** as the time-series/IoT option, **ClickHouse** for large-scale analytical workloads and **DuckDB** for embedded and local analytics, and **InfluxDB 3** is the Rust rewrite of the category's best-known name. Domain knowledge of what device telemetry actually looks like is a genuine asset here rather than a neutral.

### Sensor fusion meets foundation models — emerging, and moving fast

The classical discipline (Kalman-family filters, multi-source arbitration) is now being met by a foundation-model wave aimed at exactly the signals a wearable produces. An April 2026 survey of foundation models for sensor-based human activity recognition describes the field's own problem in terms that will be familiar to anyone who has shipped a wearable — "scarce labels, sensor heterogeneity, and poor generalization across users and contexts" — and argues that foundation models "offer a unifying paradigm to address these challenges by learning reusable, adaptable representations for activity understanding", with open problems in "data curation, multimodal alignment, personalization, privacy, and responsible deployment". A parallel industrial framing calls the combination of IMU fusion with on-device inference the basis of **"physical AI systems that can perceive, reason and act directly in the real world"**, with the signals "fused, filtered and interpreted locally" rather than in the cloud, naming wearables and fall detection among the applications.

**The hybrid, not the replacement, is the live research direction:** neural components augmenting classical filtering, keeping the interpretability and cost of the filter and adding the adaptability of the learned model.

### Edge AI and TinyML — crossing from emerging to established

Market framing (aggregator summaries, not read directly): a TinyML market of roughly **$1.36B in 2026 growing toward ~$6.1B by 2035**, with **healthcare the largest single share at about 36%**, and an industry forecast of 2.5B TinyML-capable device shipments by 2030. The engineering pattern the field settled on in 2026 is **hybrid**: local models handle routine, latency- and privacy-sensitive work, and rare or hard cases escalate to larger models elsewhere. The practitioner skills are recognisably embedded skills — model and memory budgets, quantization, power-versus-latency trade-offs — applied to inference.

### Resilient and assured PNT — established in defence, spreading to civil

Position, navigation and timing has become a resilience discipline because GNSS can no longer be assumed. "Cheap one-watt jammers, though illegal in most countries, are readily available on the internet" and can "defeat GNSS reception for several kilometers around their radiation pattern"; the countermeasures are an architecture rather than a product — controlled-reception-pattern antennas offering "20 – 50 dB of jamming protection", inertial systems disciplined by GNSS while it is trusted and carrying the solution when it is not, multi-constellation receivers, and atomic-clock holdover for timing. A widely-quoted figure of roughly 700 GNSS interference events per day appears in secondary sources; treat it as indicative only, since it was not read at its origin.

**Why it is adjacent to this career rather than a leap:** arbitration between positioning sources with fallback when one fails, and a power budget that decides how often each source may be used, is precisely the resilient-PNT problem in miniature.

### Rust in safety-critical embedded — emerging, and 2026 is the inflection

2026 is the year this stopped being a hobbyist argument. From the Rust Project's own safety-critical write-up (14 January 2026): a medical-device firm reports "All of the product code that we deploy to end users and customers is currently in Rust" for IEC 62304 Class B software in intensive-care use, and a robotics engineer working to IEC 61508 SIL 2 reports "Roughly 90% of what we used to check with external tools is built into Rust's compiler". The same source is candid about the limit — "once you move beyond prototyping into the higher-criticality parts of a system, the ecosystem support thins out fast" — and about MC/DC coverage support having stalled for want of industry involvement, now being revived through the Safety-Critical Rust Consortium. Automotive is leading adoption, and regulatory pressure (EU Cyber Resilience Act, FDA premarket cybersecurity expectations, UNECE WP.29 / ISO 21434) is part of why.

**The rare combination this rewards:** someone who has chosen a C++ standard on enforceability grounds, worked inside a medical-device QMS, and can write embedded Rust. Very few people have all three.

### Agentic AI and AI platform engineering — emerging, titles still forming

The role names are less than a year old and already appear in postings: **Agent Engineer** (described as formalised in late 2025 alongside the Claude Agent SDK, Google's ADK and LangGraph), **Agent Systems Engineer**, **Agentic AI Engineer**, and at the leadership end an AI platform role whose most-cited responsibility is **"multi-agent orchestration, model routing, and runtime controls for non-deterministic systems"** used across an engineering organization. Context engineering is named repeatedly as where the interesting problems are and as early enough that depth now compounds.

**Caution proportional to the hype:** titles this new are unstable, and a role's substance varies wildly between "prompt plumbing" and genuine platform engineering. The distinguishing question for any posting is whether the work has *users inside the engineering organization* and a reliability budget.

### Regulated medical device software / SaMD — established, and structurally protected

Aggregator summaries put the SaMD market near **$47B by the end of 2026 at a ~24% CAGR**, and describe the scarcity plainly: software engineers are plentiful, but those with **5+ years in Class II/III FDA-regulated environments are not**, with IEC 62304 and ISO 14971 named as the expected compliance stack. The same summaries argue the regulatory framework makes the role comparatively resistant to AI-driven displacement, because the lifecycle obligations do not disappear when code generation gets cheaper.

### Connected-device fleet reliability — an established practice specializing into a role

Field guidance for 2026 describes fleet observability as collecting "crash dumps (or core dumps), reboot reasons, connectivity state transitions, memory usage, performance metrics, and any custom device behavior signals" while living inside "limited RAM and flash memory, intermittent connectivity, constrained power budgets, and sometimes connect via extremely low-bandwidth networks" — and industry commentary notes that teams increasingly lean on specialists "who understand modem behavior, radio conditions, power optimization, firmware idiosyncrasies, and complex debugging". That is a job description assembled from constraints, which is why it is hard to hire for.

## Source ledger

| # | Source | Read how | URL |
|---|---|---|---|
| 1 | Rust Project — *What does it take to ship Rust in safety-critical?*, 14 Jan 2026, Pete LeVasseur for the Vision Doc group | **read directly** | https://blog.rust-lang.org/2026/01/14/what-does-it-take-to-ship-rust-in-safety-critical/ |
| 2 | Bian, Liu, Ray, Zhou, Guo, Yu, Ploetz, Lukowicz, Yuan, Fortes Rey — *Foundation Models Defining A New Era In Sensor-based Human Activity Recognition: A Survey And Outlook*, arXiv, submitted 3 Apr 2026, rev. 8 Apr 2026 | **read directly** (abstract and structure) | https://arxiv.org/abs/2604.02711 |
| 3 | Safran Navigation & Timing — *Resiliency in PNT: GPS/GNSS Jamming and Spoofing* | **read directly** | https://safran-navigation-timing.com/resiliency-in-pnt-gps-gnss-jamming-and-spoofing/ |
| 4 | ParadeDB — *Database Engineer — Storage & Query Execution* (job posting, via Y Combinator) | **read directly** | https://www.ycombinator.com/companies/paradedb/jobs/GCpYraM-database-engineer-storage-query-execution |
| 5 | Memfault — *The 2026 Guide to Monitoring IoT Devices in the Field* | **read directly** | https://memfault.com/blog/the-2026-guide-to-monitoring-iot-devices-in-the-field/ |
| 6 | 221e — *Edge AI & IMU Sensor Fusion: Powering Physical AI for Motion Intelligence* | **read directly** | https://www.221e.com/blog/edge-ai/edge-ai-imu-sensor-fusion-powering-physical-ai-for-motion-intelligence |
| 7 | Electronic Design / AdaCore — Rust in safety-critical predictions for 2026 | search summary only | https://www.electronicdesign.com/technologies/embedded/software/article/55356147/adacore-rust-in-safety-critical-systems-predictions-for-2026 |
| 8 | Augment Code — *Hiring an AI Platform Engineering Leader: A 2026 Job Spec* | search summary only | https://www.augmentcode.com/guides/ai-platform-engineering-leader-job-spec |
| 9 | Code Labs Academy — *7 Emerging AI-Native Tech Roles to Watch in 2026* | search summary only | https://codelabsacademy.com/en/blog/ai-native-jobs-emerging-tech-roles-2026/ |
| 10 | TinyML market summaries (Global Market Statistics; Roots Analysis; Derek Molloy, *From TinyML to Tiny Language Models: the State of Edge AI in 2026*) | search summary only | https://derekmolloy.ie/from-tinyml-to-tiny-language-models-the-state-of-edge-ai-in-2026/ |
| 11 | SaMD / IEC 62304 hiring summaries (KiTalent; ZipRecruiter aggregates) | search summary only | https://kitalent.com/healthcare-and-life-sciences-recruitment/medtech-and-diagnostics-recruitment/software-as-a-medical-device-samd-recruitment |
| 12 | Time-series and embedded-database comparisons, 2026 (Kestra; Basekick Labs; PkgPulse) | search summary only | https://kestra.io/blogs/embedded-databases |
| 13 | Database-internals role aggregates (ZipRecruiter: ~$122k average, ~$99.5k-$140k band, July 2026) | search summary only | https://www.ziprecruiter.com/Jobs/Database-Internals-Engineer |
| 14 | 1NCE — *IoT Trends in 2026* (the "specialized IoT engineers" observation) | search summary only | https://www.1nce.com/en-ap/resources/news/blog/iot-trends-2026 |

**No Wayback snapshots were pinned for these.** The repo's [link conventions](../resume/link-conventions.md) require archived links in *outward-facing* documents; this is an internal research page, and the durable record here is the **quotations**, which are committed. Row 2 needs no snapshot — an arXiv identifier is already an immutable citation. If any of this material is ever promoted into `markdown/`, the citation must be re-sourced and pinned at that point.

## What this page deliberately does not say

- **It does not recommend a job by salary.** Rows 11 and 13 carry job-board averages because they were in the search results; job-board aggregates mix titles, seniorities and geographies and are the weakest evidence on this page. They are not a reason to prefer one direction over another.
- **It does not rank the specializations.** Ranking depends on fit, and fit is the hub's job.
- **It does not claim completeness.** These are the nine areas the repository's own material pointed at. A specialization nobody in this career has touched would not have surfaced in this search, which is a real limitation of research that starts from a résumé.

## Refreshing this page

Re-run when a hub candidate is being seriously pursued, or annually, whichever comes first. Write a **new dated page** rather than editing this one where the conclusions change materially — a hub candidate that was graded on a 2026 market should still be traceable to the 2026 evidence. Small corrections (a dead link, a mis-attributed quote) are fixed in place.

## Related

- [Dream-job hub](../dream-jobs/dream-job-hub.md) — where this evidence is turned into candidates, with fit and gaps.
- [Skills matrix](../concepts/skills-matrix.md) — the inventory any gap is measured against.
- [Voice and prominence](../workflows/voice-and-prominence.md) — the evidence discipline this page exists to satisfy.
