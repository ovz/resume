# Reliability And Operations Coverage

> **Doc type:** reference
>
> Observability, recall response, concurrency and cellular operating cost. Audience: brag ingest and resume promotion. [Coverage map](../coverage.md) owns totals, counting rules and shard routing; each claim below has one canonical home.

### OBS — Device-health observability programme

The largest thread by far: ten entries spanning 2023–2026, tracing one arc from "can we even observe this fleet?" through launch monitoring, operational response, statistical tuning, portfolio stewardship and vendor-platform due diligence.

**Entries:** [2023-12-21 observability architecture](../../../raw/brag/2023-12-21-device-health-observability-architecture.md) · [2024-01-20 telemetry schema](../../../raw/brag/2024-01-20-errorsummary-json-schema-datadog-limitation.md) · [2024-03-07 monitoring launch](../../../raw/brag/2024-03-07-r5-datadog-monitoring-launch.md) · [2024-04-18 community presentation](../../../raw/brag/2024-04-18-r5-datadog-community-presentation.md) · [2024-05-05 anomaly tuning](../../../raw/brag/2024-05-05-r5-anomaly-detection-arima-tuning.md) · [2025-01-09 operational runbook](../../../raw/brag/2025-01-09-r5-self-reported-error-operational-runbook.md) · [2025-01-14 lifecycle review](../../../raw/brag/2025-01-14-r5-datadog-monitor-lifecycle-review.md) · [2025-05-01 device investigations](../../../raw/brag/2025-05-01-r5-device-specific-failure-investigations.md) · [2025-05-29 anomaly validation](../../../raw/brag/2025-05-29-r5-anomaly-monitor-validated-against-mcu-alerts.md) · [2026-01-01 Qualcomm observability evaluation](../../../raw/brag/2026-01-01-qualcomm-device-observability-evaluation.md)

**Thread coverage: ≈ 56%** (18 of 32)

| Claim | Source | Status |
|---|---|---|
| `OBS-1` Co-designed an agentless fleet-wide device-health observability architecture for a resource-constrained embedded fleet | 2023-12-21 | **in** |
| `OBS-2` Drove the vendor feasibility check that ruled out a conventional monitoring agent on RAM budget, closing a dead-end path before investment | 2023-12-21 | **in** |
| `OBS-3` Designed a wide-contract telemetry event so the schema could evolve without a firmware release | 2023-12-21 | **in** |
| `OBS-4` Diagnosed an unqueryable telemetry JSON schema and traced it to specific escaping behaviour the platform's attribute rules reject | 2024-01-20 | **in** |
| `OBS-5` Authored the array-based schema-change proposal that unblocked quantitative monitoring of the primary device health signal | 2024-01-20 | **in** |
| `OBS-6` Designed and shipped a new device's launch monitors and dashboard, becoming the team's automated alerting layer | 2024-03-07 | **in** |
| `OBS-7` Caught device and firmware issues — including a battery-overheating condition — before customer reports | 2024-03-07 | partial |
| `OBS-8` Resolved platform-level blockers directly with the observability vendor's Premier Support engineering | 2024-03-07 | **in** |
| `OBS-9` Presented the observability programme to a cross-team engineering community of practice | 2024-04-18 | **in** |
| `OBS-10` Identified a misbehaving production device live on stage during that session | 2024-04-18 | **in** |
| `OBS-11` Applied ARIMA/SARIMA theory to tune fleet-scale anomaly monitors, reasoning about the statistics rather than treating the feature as a black box | 2024-05-05 | **in** |
| `OBS-12` Established empirically that partitioning the anomaly model by error category sharply cuts false positives, and validated the hypothesis against real incident data | 2024-05-05 | **in** |
| `OBS-13` Initiated a monitor-lifecycle review, securing retirement of a superseded monitor while tying cleanup to its replacement's stability | 2025-01-14 | **in** |
| `OBS-14` Extended ownership from building monitors to stewarding the portfolio's relevance and boundaries | 2025-01-14 | **in** |
| `OBS-15` Converted broad fleet alerts into device-level investigations identifying individual units driving error activity | 2025-05-01 | **in** |
| `OBS-16` Supplied focused evidence for recovery, replacement and defect-classification decisions with firmware partners | 2025-05-01 | **in** |
| `OBS-17` Validated an anomaly monitor's first meaningful firing by correlating it with independent MCU alerts from firmware engineering | 2025-05-29 | **in** |
| `OBS-18` Established an evidence-based observation loop for judging a monitor's ongoing usefulness | 2025-05-29 | partial |
| `OBS-19` Co-authored the R5 self-reported-error runbook, translating device telemetry and syslog evidence into actionable operational guidance | 2025-01-09 | absent |
| `OBS-20` Recognized that threshold detection alone could not diagnose some device conditions, routing them to device-specific engineering interpretation and recovery assessment | 2025-01-09 | partial |
| `OBS-21` Prioritized physical-device recovery by customer-care urgency and diagnostic value, accounting for recovery cost | 2025-01-09 | partial |
| `OBS-22` Ensured the detailed diagnostic guide was reviewed and published alongside the main runbook's recurring review | 2025-01-09 | absent |
| `OBS-23` Evaluated Qualcomm/Skyhook Device Observability as a potential fleet-scale telemetry and diagnostics platform rather than as an isolated vendor feature | 2026-01-01 | absent |
| `OBS-24` Validated the telemetry actually produced, including cellular, battery, storage, data-usage, device-health and location-related fields | 2026-01-01 | absent |
| `OBS-25` Identified battery-range, CPU-utilization and metric-semantics questions and pursued vendor clarification before judging deployment suitability | 2026-01-01 | absent |
| `OBS-26` Compared vendor telemetry with existing Datadog monitoring to assess overlap, coverage and custom-reporting implications | 2026-01-01 | absent |
| `OBS-27` Assessed the potential effect of telemetry reporting on cellular utilization and operating cost without claiming realized savings | 2026-01-01 | absent |
| `OBS-28` Identified Qualcomm/Skyhook infrastructure dependency and vendor lock-in as architecture risks for adoption | 2026-01-01 | absent |
| `OBS-29` Determined that additional TCL participation was required before several observability fields could become operationally useful | 2026-01-01 | absent |
| `OBS-30` Coordinated the evaluation across Qualcomm/Skyhook, TCL, Best Buy Health engineering, Operations and Product stakeholders | 2026-01-01 | absent |
| `OBS-31` Obtained vendor pricing and translated technical findings into a fleet-scale cost and operational-impact discussion for leadership | 2026-01-01 | absent |
| `OBS-32` Built an engineering and business recommendation while explicitly accounting for data quality, vendor readiness and operational readiness | 2026-01-01 | absent |

> `OBS-7` is deliberately `partial`: the resume claims the catch but not the battery-overheating specific, which names a safety-adjacent defect in a current employer's product. See [editorial questions](editorial.md#open-questions).

---

### CRISIS — The August 2019 CPSC recall and relaunch

The formative event of the GreatCall years, captured 2026-09-10 from the owner's direct statement, seven years after the fact, and grounded the same day in the public CPSC record.

**Entries:** [2019-08-30 CPSC recall and relaunch](../../../raw/brag/2019-08-30-r4-cpsc-recall-and-relaunch.md)

**Thread coverage: 100%** (4 of 4)

| Claim | Source | Status |
|---|---|---|
| `CRISIS-1` Instrumental in getting a safety-critical device through the August 2019 CPSC recall (19-775) and its relaunch | 2019-08-30 | **in** |
| `CRISIS-2` Made the fleet answerable with telemetry when existing tooling could not say which devices were affected or whether a fix had taken | 2019-08-30 | **in** |
| `CRISIS-3` Built analysis that outlived the crisis and changed how the product was maintained afterwards | 2019-08-30 | **in** |
| `CRISIS-4` Learned, first-hand, how an entire organization coordinates such an event at every level | 2019-08-30 | **in** |

> **Settled 2026-09-10.** The owner confirmed the recall is public and supplied the CPSC notice, so the resume names it and links a pinned snapshot of the notice. What stays out is everything not in the public record — root cause and internal decision-making.

---

### CONC — Concurrency, and the bugs that vanish when observed

A failure class the owner has pursued for twenty years: evidence-led diagnosis, followed by vendor corrective engineering and a later owner-reported QA improvement in the same audio subsystem. Owner's concurrency chops acquired early in the career continue to bring value. 

**Entries:** [2004-01-01 client-server TCP/IP daemon](../../../raw/brag/2004-01-01-spm-client-server-tcpip-daemon.md) · [2023-09-26 audio-service race condition](../../../raw/brag/2023-09-26-audio-service-race-condition-diagnosis.md) · [2026-04-24 manufacturer audio-service corrections](../../../raw/brag/2026-04-24-tcl-audio-service-concurrency-corrections.md) · [2026-09-16 concurrency and parallelism specialization](../../../raw/brag/2026-09-16-concurrency-parallelism-specialization.md) · [2010-01-01 SPM engine debugging](../../../raw/brag/2010-01-01-spm-engine-debugging-cart-treenet-mars.md) · [2012-06-01 SPM 7.x Linux port and TBB evaluation](../../../raw/brag/2012-06-01-spm7-linux-port-tbb-evaluation.md) · cross-listed: [2024-05-15 positioning root cause](../../../raw/brag/2024-05-15-skyhook-positioning-root-cause-diagnostics.md) (claims under `POS`)

**Thread coverage: ≈ 69%** (16.5 of 24). `CONC-21` became `partial` on 2026-09-16: the resume now features engine-level debugging of the classic ML implementations at their Fortran and C/C++ core, without the specific grove-pointer and R-squared defects.

| Claim | Source | Status |
|---|---|---|
| `CONC-1` Diagnosed an intermittent audio artifact as a race condition without ever reproducing it, from correlated logs showing the playback thread created twice and the audio wakelock acquired twice before a forced reboot | 2023-09-26 | **in** |
| `CONC-2` Corroborated the reboot story from an independent subsystem's own counter | 2023-09-26 | **in** |
| `CONC-3` Designed instrumentation and fault injection instead of repeating a manual test, including a negative experiment that separated two failure modes | 2023-09-26 | **in** |
| `CONC-4` Separated a defect that was being debugged as part of another, wrote a reproduction others could follow, and framed it as a risk rather than a bug report | 2023-09-26 | **in** |
| `CONC-5` Treats concurrency as a specialization spanning a 2004 TCP/IP daemon, a 2024 positioning multithreading fault, and TLA+ study in 2026 | 2023-09-26 | partial |
| `CONC-6` Drove the manufacturer's audio-service corrections through successive concrete requests and source reviews, with the vendor owning implementation | 2026-04-24 | **in** |
| `CONC-7` Directed corrections to producer-consumer synchronization, queue-pointer ownership and shared-state locking | 2026-04-24 | **in** |
| `CONC-8` Extended corrective review to C/ALSA resource lifetimes and worker shutdown sequencing | 2026-04-24 | **in** |
| `CONC-9` Defined structural acceptance criteria and runtime test requirements so known unsafe code did not masquerade as meaningful stress-test evidence | 2026-04-24 | **in** |
| `CONC-10` After the team's fixes, QA reported smooth audio-service operation with no observed behaviours attributable to lingering concurrency issues; owner-reported, bounded by the retest | 2026-04-24 | **in** |
| `CONC-11` The resulting audio service also received a subjective user-experience improvement assessment in QA; qualitative, not a measured performance gain | 2026-04-24 | absent |
| `CONC-12` Designed and singlehandedly built a cross-platform TCP/IP daemon that ran concurrent predictive-analytics jobs for remote users, before the standard library had threads | 2004-01-01 | **in** |
| `CONC-13` Handed two client-side developers a framework of components and guidance rather than a specification — architect behaviour four years into the career | 2004-01-01 | **in** |
| `CONC-14` Delivered it on Windows, Linux and Solaris with native `.RPM`, `.DEB` and `.PKG` installers, structuring the code so one set of sources built both client and server | 2004-01-01 | **in** |
| `CONC-15` Implemented a large share of the Gang of Four catalogue as a C++ library and used it as the daemon's skeleton | 2004-01-01 | **in** |
| `CONC-16` Modelled the system in Rational Rose with round-trip engineering, and holds a considered account of why the model/code pairing decayed and what now supplies what RUP promised | 2004-01-01 | absent |
| `CONC-17` Pursued concurrency and parallelism as a deliberate specialization — the pattern literature, the industry's successive parallelism frameworks, and formal methods (TLA+, studied 2026) | 2026-09-16 | absent |
| `CONC-18` Carried a vendor-compiler dependency for the Fortran analytics backend through nasty compiler bugs and a year of active collaboration; a responsive vendor and an acceptable time-to-resolution are separate things | 2026-09-16 | absent |
| `CONC-19` Can state what an asynchronous abstraction buys and where its guarantees stop, from having built the hand-rolled equivalent first | 2026-09-16 | partial |
| `CONC-20` Tracks language and toolchain readiness against what a programme can adopt: `co_yield` is C++20, the first usable standard coroutine type is C++23's `std::generator`, so coroutines arrived too late for the systems in this record | 2026-09-16 | absent |
| `CONC-21` Chased assertion failures tied to model/grove-pointer lifetime and fixed an R-squared computation path shared between two commands in a C/C++ statistical engine, reasoning through algorithm semantics directly with the engine's original author | 2010-01-01 | partial |
| `CONC-22` Technical participant in porting a C++ analytics engine to Linux and evaluating Intel TBB for its threading needs, reaching a documented negative conclusion on TBB for low-level platform reasons | 2012-06-01 | absent |
| `CONC-23` Treats concurrency and network programming as the fundamentals of embedded work, serving both the bare-metal sensor co-processor MCU and the hosted embedded-Linux processor, where a backend engineer's runtime would otherwise supply them | 2026-09-16 | **in** |
| `CONC-24` Frames embedded Rust as carrying a do-it-yourself mandate — owning the layer below where silicon-vendor support falls short — which those fundamentals make viable | 2026-09-16 | **in** |

> **Promoted 2026-09-16.** The resume now carries a dedicated *Concurrency and Network Programming* achievement, a clause in *My Story* and in the Best Buy Health block, a 2023-2026 concurrency project section, and a fuller 2004-2005 section — so the diagnosis (`CONC-1`–`CONC-4`), the manufacturer corrections (`CONC-6`–`CONC-10`), the platforms and installers (`CONC-14`) and the owner's bare-metal/hosted and embedded-Rust framing (`CONC-23`, `CONC-24`) are `in`. `CONC-5` and `CONC-19` are `partial`: TLA+ and the guarantee-boundary half of the Asio point are not on the resume. `CONC-11`, the subjective UX remark, stays out by choice — qualitative, and weaker than the smooth-QA claim beside it. The public wording names no device, no manufacturer and no silicon vendor; the vendor example in the owner's own statement stays at T1.
>
> Before this pass the resume said "advanced Concurrency" twice without evidence behind it; this thread is the evidence. `CONC-12` through `CONC-16` are the 2004-2005 origin — the first four are already on the resume's project section, which is why this thread is no longer at zero; `CONC-14` is `partial` because the resume says "fully cross-platform" without naming the three platforms or the installers. `CONC-17` through `CONC-20` are the craft behind the bug stories, and rest on the owner's own account: `CONC-18` is undated and wants its own entry. `CONC-1` supplies the diagnosis; `CONC-6` through `CONC-11` add a distinct correction-and-outcome story. `CONC-21` and `CONC-22` are 2009-2012 Salford-era engine debugging and platform-work, captured 2026-09-16 from a breadth-first Gmail survey and not yet deep-dived — see each entry's own *Evidence limitations*. The last retained static review still had open findings; the later QA result is owner-reported, with no exact retest date, final build, full closure ledger, or proof of race freedom. Test plans are not executed tests, and the vendor identity stays private.

---

### COST — Cost of operation: cellular data and the devices that waste it

Where observability stops being about reliability and starts being about money. The company is its own MVNO, so cellular data is a direct per-device cost.

**Entries:** [2024-01-04 cellular cost and rogue-device detection](../../../raw/brag/2024-01-04-cellular-cost-rogue-device-detection.md) · cross-listed: [2025-10-29 AI data product](../../../raw/brag/2025-10-29-ai-data-product-in-alation.md) (claims under `AI`)

**Thread coverage: 0%** (0 of 6)

| Claim | Source | Status |
|---|---|---|
| `COST-1` Joined carrier cellular-operations data, device telemetry and warehouse event tables on device identity to find devices consuming far outside any plausible pattern | 2024-01-04 | absent |
| `COST-2` Built a rogue-device emulation script to validate the detection path against a device known to be misbehaving, and got the threshold agreed before an incident rather than during one | 2024-01-04 | absent |
| `COST-3` Published a rogue-device runbook and fed the scenario into the launch tabletop exercise | 2024-01-04 | absent |
| `COST-4` The work revealed a real misbehaving unit at roughly a gigabyte a day, investigated quickly because detection and runbook were already in place | 2024-01-04 | absent |
| `COST-5` Made replacement plus root cause the routine response, so each bad device produced a root cause rather than only a swap | 2024-01-04 | absent |
| `COST-6` Submitted five ideas to the organization's cost-reduction programme | 2024-01-04 | absent |

> `COST-6` is deliberately weak and should stay low-prominence or be dropped outward: submitted is not adopted, and the record shows no outcome. The dollar figure behind `COST-1` is the owner's own and is not in the archive — an outward claim should say "devices costing real money" and let a follow-up question carry the number.
