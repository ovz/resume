# Skills Matrix

> **Doc type:** reference
>
> The owner's skill inventory with years of use. **Baseline** rows are carried from the [archived skills document][skills], whose values date to about 2020 (C++ = 24 years from 1996). They have **not** been re-aged; treat "years" as *as of ~2020* until the owner refreshes them. The **Delta** section lists skills evidenced by the [primary resume][primary] that the baseline lacks. Audience: resume edit passes (keyword coverage) and brag ingest (new capability check).

## Baseline (as of ~2020, from the archived skills document)

| Skill | Years | Comment (source wording, lightly trimmed) |
|---|---|---|
| C++ | 24 | Main language for professional software engineering |
| Data Science / Machine Learning / AI | 18 | Commercializing binary trees in predictive analytics since 2000 |
| Software Architecture | 17 | Strong knowledge of design principles and patterns |
| Desktop User Interface | 15 | Mostly Windows |
| Boost/C++ | 15 | |
| Team Lead | 12 | |
| TDD | 10 | |
| CMake | 10 | |
| CI/CD | 10 | Continuous integration and delivery for everything important |
| TCP/IP | 10 | Strong understanding of networking with multiple protocols |
| Agile/Scrum | 10 | |
| Source Code Version Control | 20 | Strong practice since 2000 (Visual SourceSafe onward); "if something is still in Git I can recover it" |
| SQL | 7 | "I happen to love relational algebra" |
| Data Security, Risk/Threat Analysis, License Management | 7 | |
| AWS Cloud | 6 | Every cloud project converged to AWS; familiar with Azure |
| API Design | 6 | Building reusable code to run everywhere |
| Python | 5 | Tool of preference for data engineering |
| MS SQL Server | 5 | Query optimization |
| Data Engineering | 5 | ETL databases up to 1 TB; preparing data for ML |
| Big Data | 5 | Binary trees for ML over peta-scale databases |
| Concurrency/Parallelism | 5 | |
| Static and dynamic source analysis | 5 | |
| Google Test | 5 | |
| Legacy code | 5 | |
| Cryptography | 5 | |
| Management | 5 | |
| C#/.NET | 4 | Multiple projects over 7 years |
| Pandas | 4 | Data wrangling in Python |
| Conda | 3 | Python package manager |
| Autoconf/Autotools | 3 | |
| JavaScript | 3 | |
| Recruiting, Technical Interviewing | 3 | |
| MacOS | 3 | |
| Embedded C++ | 2 | |
| Cellular Mobile Technologies | 2 | |
| MQTT | 2 | Message broker for IoT/mobile |
| Boost Test | 2 | |
| Model Driven Development | 2 | Round-trip engineering with Rational Rose |
| WWF/.NET | 1 | "Best workflow engine I worked with" |
| Qt/C++ | 1 | Product owner and leader of the flagship GUI rewrite |
| MongoDB | 1 | |
| SAS | 1 | |
| Rust | 0 | Learning, looking for a project |
| Windows | 25 | |
| Linux | 15 | |

## Delta — evidenced since the baseline (from the primary resume)

| Skill | Evidence | Suggested treatment |
|---|---|---|
| Rust | summary now says "Intermediate Rust"; studied again in 2026, and now a stated *direction* as well as a skill — see the [dream-job hub](../dream-jobs/dream-job-hub.md) | baseline row (0 years) is stale twice over; owner to supply years |
| Embedded C++ / cellular / positioning | six more years of Lively Mobile+ and Lively Mobile 2 work | re-age Embedded C++ and Cellular; add **GNSS/positioning (GPS, GLONASS, Galileo, ECID, Wi-Fi, BLE)** and **Qualcomm Linux Enablement / Skyhook** |
| Observability / Datadog | OKR-level operational excellence; monitor/dashboard design, ARIMA/SARIMA-based anomaly tuning, vendor Premier Support collaboration ([brag entries, 2023-12 to 2024-05](../../raw/brag/)) | add **Datadog**, **incident management, runbooks, post-mortems**, **applied time-series anomaly detection** |
| Neural networks | "successfully used neural networks" for senior health & safety | add under ML/AI; detail wanted (brag candidate) |
| AI-assisted engineering | "leveraging AI since 2023" | add row; owner to name tools/practices at the public tier |
| On-device test automation | architecture and implementation | strengthen TDD/testing rows |
| Hiring | interview challenges, hiring process | re-age Recruiting |
| SQL | summary says "advanced knowledge of SQL" | re-age |
| Distributed systems | "Distributed System Design" applied at Best Buy Health | add or fold into Architecture |
| **Embedded power management / power budgeting** | battery and power carried as a second specialization interlocked with positioning: sync-cadence design against MQTT keep-alive, wakelock discipline, soak-test and engineering-build measurement ([2021-10-16 entry](../../raw/brag/2021-10-16-battery-power-second-specialization.md)) | add **embedded power management**, and **Qualcomm MDM-class modem/AP platform behaviour** under cellular |
| Concurrency/Parallelism | baseline of 5 years is badly stale: evidence runs 2004 (cross-platform TCP/IP daemon) → 2024 (positioning multithreading fault) → 2023-2026 ([a race condition diagnosed without ever reproducing it](../../raw/brag/2023-09-26-audio-service-race-condition-diagnosis.md)), plus TLA+ studied in 2026 | re-age substantially; add **race-condition diagnosis from correlated telemetry** and **formal methods (TLA+, studied 2026 — owner to state depth)** |
| Vendor corrective engineering / concurrency review | concrete manufacturer-facing requirements and repeated source reviews covering POSIX synchronization, GLib ownership and ALSA lifetimes; later smooth QA retest reported by the owner ([2026-04-24 entry](../../raw/brag/2026-04-24-tcl-audio-service-concurrency-corrections.md)) | add **supplier technical assurance**, **source-level concurrency review**, and **acceptance-criteria design**; do not imply the proposed sanitizer or soak runs were executed |
| Applied statistics and experiment design | hypothesis-first practice, ARIMA/SARIMA reasoning, validation against an independent signal, notebooks replacing spreadsheets ([2026-05-17 entry](../../raw/brag/2026-05-17-statistical-bar-and-data-science-partnership.md)) | strengthen the Data Science row; add **experiment design** and **Jupyter** |
| Cellular operations and cost analysis | carrier cellular-operations data joined with device telemetry and warehouse events on device identity; outlier detection on operating cost ([2024-01-04 entry](../../raw/brag/2024-01-04-cellular-cost-rogue-device-detection.md)) | add row; also strengthens **Cellular Mobile Technologies** and **Data Engineering** |

## Maintenance

- A skill that has become a *direction* as well as a capability is also recorded in the [dream-job hub](../dream-jobs/dream-job-hub.md), which grades how much of this matrix supports it.
- Refreshing years is an owner task; agents should not invent values. When refreshed, replace the baseline heading's "as of ~2020" with the new date and fold the delta rows into the table.
- A brag ingest that evidences a skill absent from both tables adds a delta row citing the entry.

[skills]: ../../raw/archive/Oleg.Zhylin.skills_and_responsibilities.md "Archived skills and responsibilities"
[primary]: ../../../markdown/Oleg.Zhylin.resume.achievements.md "Primary resume (achievements)"
