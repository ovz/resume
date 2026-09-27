---
title: "Concurrency and parallelism as a deliberate specialization: the literature, the industry's attempts to codify it, and the abstractions that finally arrived"
date: "circa 2004 to 2026-09-16"
thread: CONC
domains:
  - "Architecture and API design"
  - "Legacy code and platform migrations"
context: "Cross-career: Salford Systems (Fortran analytics backend, Intel toolchain) and GreatCall / Best Buy Health (Boost.Asio, embedded C++)"
sensitivity: private-repo
resume-worthy: yes
---

# Concurrency and parallelism as a deliberate specialization: the literature, the industry's attempts to codify it, and the abstractions that finally arrived

## What I did

**Low-level concurrency fascinates me.** That is the owner's own opening, and it is the reason this entry exists as a capability record rather than as a line inside a project. The twenty-year thread in this repository is usually told through the bugs — [the daemon](2004-01-01-spm-client-server-tcpip-daemon.md), [the audio artifact](2023-09-26-audio-service-race-condition-diagnosis.md), [the positioning library](2024-05-15-skyhook-positioning-root-cause-diagnostics.md) — but the bugs are where the capability was *spent*. This is where it was *built*: deliberately, by reading, by studying what the industry tried, and by living with the toolchains that made the promises.

### The literature

**"I read pretty much all the pattern books."** The Gang of Four catalogue I did not merely read — during the [2004-2005 client-server project](2004-01-01-spm-client-server-tcpip-daemon.md) I implemented a large share of it as a C++ library and used it as the daemon's skeleton, which is a different relationship with a pattern than recognising its name. That is the documented end of the reading; the rest is a broad, self-reported sweep of the pattern literature over the years that followed, undated and unlisted.

What the reading bought is the thing that is hard to acquire any other way: a **vocabulary for concurrency structures before there were libraries for them**. When a library later shipped the structure, reading its design was recognition rather than learning — which is exactly what happened with Boost.Asio.

### Studying the industry's attempts to codify it

**"I studied Intel TBB and other attempts to codify concurrency and parallelism industry-wide."** The interest was never in one library: it was in the repeated industry attempt to take concurrency away from the person writing the loop and put it in a framework — task graphs, work stealing, parallel algorithm templates, parallel-for over a range — so that correctness came from the shape of the program rather than from the discipline of its author. Following those attempts over two decades is what makes it possible to judge a new one quickly, which is the transferable skill.

The corroborating documented use of an Intel parallel toolchain in this corpus is the **64-bit migration of SPM**, where I ran **Intel Parallel Studio XE** for static and dynamic analysis of the source. Studying a library and shipping with a toolchain are different claims, and both are made here at their own strength.

### Living with the Intel Fortran compiler, and a year to resolution

**SPM's computational backend was Fortran** — it originates from **Jerome Friedman's original source code**, which is the same provenance that made the product what it was — and we used the **Intel Fortran compiler** heavily to build it. Depending on a vendor compiler for the part of the product that does the actual work is a specific kind of exposure, and we found the sharp edge of it.

**We hit nasty compiler bugs that were not fixed for a year of active collaboration.** Intel was responsive — the relationship worked, the engagement was real, they engaged with our reproductions — but **time-to-resolution was highly suboptimal, and it cost our business.** A miscompilation in the analytics backend is not an ordinary defect: the code is correct, the tests that would catch it are testing the wrong layer, and the workaround is either to change source that was right or to pin a toolchain you wanted to move off.

The lesson is about vendor dependency rather than about Intel. **A responsive vendor and an acceptable time-to-resolution are two separate things, and only the second one is on your critical path.** That reading is visible later in the career every time a vendor escalation appears in this record: the question asked is not "will they engage?" but "what does the schedule look like if they engage and it still takes a year?"

### Boost.Asio as the day-to-day abstraction

In the embedded C++ work, **Boost.Asio is the abstraction I live with day to day, and I know first-hand what it buys.** The value is specific and I can name it because I built the hand-rolled version first: in 2004 I wrote the accept loop, the per-job threading, the wire handling and the lifetime rules myself, on three operating systems, and every one of those was a place to be wrong. Asio makes the execution context an explicit object, so *where* a piece of work runs is a decision written in the code rather than an accident of which thread called the function.

The recorded technical work on that boundary is in the [Boost proficiency entry](2026-09-14-boost-library-proficiency.md): analysing the message-bus implementation's `boost::asio` dependency and the need to abstract its executor so the bus could be substituted in off-target tests, and the `boost::asio::signal_set` / SIGTERM analysis where the alternative under discussion would have cost Asio's signal-handler guarantees. Both are reasoning about *what the abstraction guarantees and where the guarantee ends*, which is the only way to use one safely.

### Where C++ coroutines actually landed

**C++ coroutines are a good resolution** to a large part of this — the callback-and-state-machine structure that asynchronous code degenerates into is exactly what a coroutine removes — **but they only became available in recent years.** The owner's instinct, stated 2026-09-16, was that "it might be only C++23 that nailed it". The lookup, done the same day, says that instinct is substantially right:

| Milestone | When | Note |
|---|---|---|
| `co_await`, `co_yield`, `co_return` as language keywords | **C++20** | Merged from the Coroutines TS into the working draft in 2019 (P0912R5); published in C++20 |
| GCC | **10** (2020) | Initially behind `-fcoroutines` |
| MSVC | **19.28** / Visual Studio 2019 16.8 (2020) | Earlier partial support from 19.0 and 19.10 |
| Clang | partial from **8**, still listed partial at **17** (2023) | cppreference's C++20 compiler-support table marks both entries partial |
| A concrete coroutine type in the standard library — `std::generator` | **C++23** | C++20 shipped the *machinery* for writing coroutine types, not a usable one |
| `std::generator` in libstdc++ | **GCC 14** (2024) | `<generator>`, under `-std=c++23` |
| `std::generator` in the MSVC STL | **Visual Studio 2022 17.13** (2025) | |

So: the keyword is C++20, the *usable* out-of-the-box generator is C++23 plus a 2024-or-later toolchain, and libc++ lagged both. **That is why coroutines are not the answer to any of the concurrency work in this record** — not one of the systems in this corpus was on a toolchain that could have used them. The Lively device builds against Boost 1.67.0, a 2018 release. A twenty-year-old problem got a good language-level answer roughly two years ago, on compilers an embedded programme does not get to choose.

### Why these are the embedded fundamentals — bare metal and hosted alike

The owner's position, stated 2026-09-16 when asking for it to reach the resume: concurrency and network programming are **"rather fundamental areas for today's embedded developer"**, and **both halves of a modern device benefit from them — "bare metal like Sensorhub MCU and hosted like R5"**.

The record carries both halves. On the **bare-metal** side: the [sensor-cluster architecture](2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) is a concurrency design across two processors — significant motion wakes the BLE MCU, the MCU consumes the sensor's own machine-learning-core output, and the application processor sleeps until the MCU wakes it or it queries the MCU for a position; the [ODM specification set](2022-08-03-odm-specification-authoring.md) defined the sensor-hub API and the IPC API, down to whether a call acquires or releases a wakelock; and the [Hospital at Home work](2024-09-24-current-health-hospital-at-home-qms.md) traced a firmware defect through FreeRTOS queue and timer primitives. On the **hosted** embedded-Linux side (the R5 device, Lively Mobile 2): the [audio-service race](2023-09-26-audio-service-race-condition-diagnosis.md) and its [manufacturer corrections](2026-04-24-tcl-audio-service-concurrency-corrections.md) in POSIX threads and GLib queues, the [positioning library's listener-thread fault](2024-05-15-skyhook-positioning-root-cause-diagnostics.md), Boost.Asio over D-Bus, and a sync cadence specified [in units of MQTT keep-alive intervals](2021-10-16-battery-power-second-specialization.md).

**The contrast he draws is with backend programming** — Python, Go, .NET, Java — which works "much higher level": the runtime already schedules the work and speaks the protocol, so the engineer rarely touches either. On a device, nothing supplies that layer; the embedded engineer is it.

**Rust, in the owner's words, "helps somewhat, but modern Rust professionals get a 'do it yourself' business mandate."** The example he gave is a silicon vendor — STMicroelectronics, whose STM32WB part is the sensor-hub MCU candidate in the 2021 architecture — not providing Rust libraries of adequate quality: the team then **accepts the risk of building it itself, or of pressing the vendor for it**. He sets that explicitly against the conventional C/C++ posture — *holding the vendor to their claims*, and the "eternal *focus on your own application*" cliché. The mandate only works for a team that commands the layer below, which is exactly where concurrency and network programming live.

### Formal methods as the other direction

In 2026 I worked through **TLA+** as one of the year's study items. It is the formal-methods answer to the same problem from the opposite end: rather than a better abstraction for writing concurrent code, a way to reason about the interleavings instead of hoping to observe one. That pairing — a better abstraction *and* a way to check the thing the abstraction does not cover — is the current state of my answer to "how do you know concurrent code is right?"

## Why it matters

The resume asserts "advanced Concurrency" twice. This entry is the part of the evidence that is not a bug story: a specialization pursued deliberately across twenty years, through the literature, through the industry's successive frameworks, through a vendor toolchain that failed in an instructive way, and into the abstractions that only recently arrived. It is what makes the bug stories credible rather than lucky — and it is the honest basis for a claim of depth rather than familiarity in an area where almost everybody claims both.

The Intel Fortran episode is separately valuable as a **vendor-dependency judgement** with a cost attached, and it is the earliest instance in this record of a pattern the later embedded work repeats constantly.

## Skills demonstrated

Low-level concurrency and parallelism; design patterns implemented rather than cited; evaluating parallelism frameworks and their guarantees; Fortran-backed numerical toolchains; compiler-bug diagnosis and vendor escalation over a long horizon; vendor-dependency risk judgement; Boost.Asio executor and guarantee reasoning; tracking language and toolchain readiness (C++20/23 coroutines) against what a programme can actually adopt; formal methods (TLA+, studied 2026).

## What was blocked, cut short, or wrong

- **The Intel Fortran compiler bugs took a year of active collaboration to resolve**, and that year was paid by the business. The engagement worked; the timeline did not. Recorded as a cost that was absorbed, not a win.
- **C++ coroutines arrived too late to be used on the systems in this record.** That is a negative result about adoption, not about the feature — the toolchain, not the judgement, is the constraint.
- The industry's attempts to codify concurrency are studied here, not adopted: no claim is made that any of these frameworks shipped in a product the owner built.

## Evidence

- The owner's statement of 2026-09-16, captured verbatim in the session scratch scope, is the source for: the fascination with low-level concurrency, the pattern reading, the study of Intel's and others' parallelism frameworks, the Intel Fortran compiler bugs and the year to resolution, Boost.Asio's day-to-day value, and the coroutine assessment.
- The [archived full resume](../archive/Oleg.Zhylin.resume.md) independently records the **Fortran legacy codebase** at Salford ("through acquisition and own development"), and the use of **Intel Parallel Studio XE** for static and dynamic analysis during the 64-bit upgrade.
- The [organizations page](../../wiki/entities/organizations.md) records the Friedman/Breiman/Olshen/Stone provenance of the CART and TreeNet engines that the Fortran backend implements.
- The [Boost proficiency entry](2026-09-14-boost-library-proficiency.md) carries the dated, artifact-backed Boost.Asio work (August 2022 executor analysis; the `signal_set`/SIGTERM note) and establishes Boost 1.67.0 as the vendored release.
- The coroutine dates were looked up on 2026-09-16 from cppreference's C++20 compiler-support table, the GCC 14 release notes and libstdc++ feature list, and Microsoft's C++ team blog announcement of `std::generator` in Visual Studio 2022 17.13.
- TLA+ study in 2026 is recorded in the [audio-service investigation](2023-09-26-audio-service-race-condition-diagnosis.md) § *The wider thread*.

## Evidence limitations

**The Intel Fortran compiler episode is undated.** The owner supplied no year, compiler version, bug identity or product release, and none is inferred — "during the Salford years" is as precise as this record gets. The "year of active collaboration" and "it cost our business" are the owner's own characterisations, without a support case, a ticket, or a cost figure behind them. **This episode deserves its own dated entry once the owner can place it**; it is recorded here rather than lost, not because it belongs inside a capability entry. **Dated since, 2026-09-24:** the mailbox places an Intel Fortran 14 regression — certified December 2013, rolled back January 2014 over internal compiler errors in Release builds, escalated to Intel Premier Support in May 2014, team standardised on a later release in June 2015 — in its own entry, [2013-12-01](2013-12-01-intel-fortran-14-rollback-premier-support-escalation.md). Whether that is the whole of the owner's "year" is still his to confirm. **Settled, 2026-09-25:** the owner ruled the email-grounded record authoritative. The episode is the 2013–2015 regression, and the bug the mail shows is internal compiler errors, not a silent miscompilation; the "miscompilation" above is kept as he first said it and is not told.

**The library is Intel Threading Building Blocks (TBB, now oneTBB).** The owner's first statement said "Intel TPL"; he corrected it on 2026-09-24 — "it is Intel TBB not TPL" — which settles the ambiguity with Microsoft's .NET Task Parallel Library. TBB is also the library debated for SPM's engine in 2012 ([2012-06-01](2012-06-01-spm7-linux-port-tbb-evaluation.md), [2012-12-18](2012-12-18-intel-cpp-compiler-migration-careful-path.md)).

**No list of the pattern books survives**, and "pretty much all" is the owner's own quantifier, retained rather than converted into a number or a bibliography. The only pattern reading with an artifact behind it is the GoF library built in 2004-2005.

**The bare-metal/hosted framing, the backend contrast and the embedded-Rust mandate are the owner's professional position**, grounded in the linked entries for the device work itself. No evaluation of any silicon vendor's Rust support is on record: STMicroelectronics is the example he chose, and it is not a finding. Nothing here claims a production Rust component, and the resume keeps its existing *intermediate Rust* self-assessment.

The coroutine table is a documentation lookup, not the owner's experience: it states when the feature became available, not that he used it. The Clang row reproduces cppreference's own "partial" labelling rather than resolving it. No claim is made that any system in this corpus adopted coroutines, `std::generator`, TBB, or TLA+ in production.

The Boost.Asio value statement is professional judgement grounded in the dated analyses in the Boost entry; it is not a claim to have authored the device's Asio-based infrastructure.

## Related

- [2004-01-01 client-server TCP/IP daemon](2004-01-01-spm-client-server-tcpip-daemon.md) — where the specialization started, and the GoF library that is the documented half of the pattern reading.
- [2026-09-14 Boost proficiency](2026-09-14-boost-library-proficiency.md) — the dated Boost.Asio executor and `signal_set` work this entry's abstraction argument rests on.
- [2023-09-26 audio-service race-condition diagnosis](2023-09-26-audio-service-race-condition-diagnosis.md) — the capability spent on a bug that never reproduced; also the source for the TLA+ study.
- [2026-04-24 manufacturer audio-service concurrency corrections](2026-04-24-tcl-audio-service-concurrency-corrections.md) — the same reading applied to another team's producer-consumer C.
- [2025-07-18 FOTA vendor escalation](2025-07-18-fota-vendor-escalation-lively-mobile2.md) — the later instance of the vendor-dependency judgement the Intel Fortran year taught.
- [2026-05-26 AI adoption and agentic engineering](2026-05-26-ai-adoption-agentic-engineering-choreographer.md) — the present-day answer to the documentation problem that RUP and round-trip engineering could not solve.

## Record history

- 2026-09-16: created from the owner's statement of the same day, with the C++ coroutine availability dates looked up and tabulated at his explicit request, and the Salford-era Fortran and Intel Parallel Studio facts corroborated from the archived full resume. The Intel Fortran compiler episode is flagged for its own dated entry.
- 2026-09-16: updated from the owner's second statement of the same day — concurrency and network programming as embedded fundamentals serving the bare-metal sensor-hub MCU and the hosted R5 processor alike, the contrast with runtime-supplied backend stacks, and embedded Rust's do-it-yourself mandate. The vendor example stays at T1; the public resume names no vendor. Promoted to the resume the same day (`CONC-23`, `CONC-24`).
- 2026-09-24: owner corrected "Intel TPL" to Intel TBB and the paragraph on the ambiguity was rewritten; the Intel Fortran episode now has a dated entry from the mailbox (2013-12-01) and the C++ compiler debate its own (2012-12-18). The owner's undated account above is kept as he gave it.
- 2026-09-25: owner ruled the email-grounded Intel record authoritative; *Evidence limitations* notes that "miscompilation" is superseded by the mail's internal compiler errors.
