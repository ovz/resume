---
title: "Designed and singlehandedly built a cross-platform TCP/IP predictive-analytics daemon — the project that taught me concurrency"
date: "2004 to 2005"
thread: CONC
domains:
  - "Architecture and API design"
  - "ML products and GUIs"
  - "Build, release, CI/CD"
context: "Salford Systems — Client-Server predictive analytics for CART/SPM; contractor from Ukraine, remote"
sensitivity: public-friendly
resume-worthy: yes
storied: [concurrency/lowest-level-reflexes]
---

# Designed and singlehandedly built a cross-platform TCP/IP predictive-analytics daemon — the project that taught me concurrency

## What I did

**One of the company's strategic projects, and the largest software system I have ever developed singlehandedly from the ground up**: a client-server solution that ran predictive-analytics algorithms on remote servers while analysts kept working in the SPM GUI they already knew.

Two business cases drove it, and they were different arguments made by different people. **Performance**: a remote server has hardware an analyst's desktop does not, so the model that will not finish overnight on a laptop finishes on the server. **Security**: customers wanted the data to stay on the central server rather than be copied to every analyst's machine. The second reason is the one that aged best — it is the same argument every managed analytics platform makes today, twenty years later.

**I designed the entire system and implemented the TCP/IP daemon.** It ran multiple data-mining jobs concurrently on behalf of end users, each of whom saw the familiar SPM front end rather than a new tool. For the client side I did not write the GUI: I provided *guidance* and a *framework of components* to two developers who did, which is the earliest recorded instance of the pattern that runs through the rest of the career — build the substrate, then make other people fast on it.

### What made it a concurrency project rather than a networking one

This was **my major introduction to concurrency, parallelism, network programming and network-protocol design**, and I did all four at once with nobody to ask. The daemon had to accept connections, authenticate them, run long analytics jobs on their behalf, keep those jobs isolated from one another, report progress back over the wire, and survive a client disappearing mid-job. There was no framework underneath doing any of that: this is 2004, before `std::thread`, before Boost.Asio was something you reached for by default, on three operating systems with three different threading and socket personalities.

**I still understand networking and multithreading intimately because of this project**, and the understanding is at the level the wire and the scheduler actually work at, not at the level a library describes them. That is the thing I mean by *reflexes*: twenty years later, reading someone else's producer-consumer code, I can see the missing critical section the way you see a misspelled word — without deriving it.

### Cross-platform meant three platforms, properly

The daemon was deployed on **Windows, Linux and Sun Solaris**. I authored the native installers myself — **`.RPM`, `.DEB` and `.PKG`** packages — so that the thing could actually be delivered to a customer's operations team rather than handed over as a tarball and an apology.

I organized the code so that **a large proportion of the same source files built both the client and the server**. That was a deliberate structural decision, not a convenience: one protocol definition, one serialization path, one set of shared types, compiled into both ends. The classic failure of a hand-rolled protocol is that the two ends drift; sharing the sources removes the opportunity.

### The GoF pattern library

I developed a C++ library implementing a large share of the **Gang of Four** patterns and used it as the daemon's skeleton. Two things came out of that, and only one of them was the library. **It gave me intimate knowledge of the patterns** — not the catalogue-recognition kind, the kind where you have paid the cost of each one — **and it took my understanding of idiomatic C++ to the next level.** The patterns were the vocabulary I had at the time for the problems that concurrency libraries later solved directly; reading Asio's design years afterwards was recognition, not learning.

### Round-trip engineering with Rational Rose

The system was modelled in **Rational Rose**, with **round-trip engineering** — model to code, code back to model — which was the state of the art then and part of what the Rational Unified Process promised.

**The owner's reflection, stated 2026-09-16:** *RUP never caught up.* The round trip worked in the demo and degraded in the real project, for the reason it always degrades: keeping a model and a codebase in agreement is continuous work that no one is funded to do, so the model goes stale and then gets ignored, and the discipline collapses into documentation theatre. **Today AI is finally the way to comprehensive, up-to-date documentation** — it reads the code that exists rather than a model of the code that was intended, and it can be re-run, which is the property Rose never had. **UML itself is unlikely to revive.** That judgement matters for how this repository works: the knowledge layer is regenerated from sources rather than maintained as a parallel artifact, which is the same lesson applied twenty years later.

## Why it matters

The claim this entry supports is **not** "shipped a client-server product in 2005" — it is that the concurrency capability the resume asserts twice has a twenty-year origin with an artifact behind it. A cross-platform daemon running concurrent analytics jobs, a hand-designed wire protocol, three operating systems and native packaging, all built alone, is the strongest possible answer to "where did you learn concurrency?" Everything later in this thread — the positioning library's listener-thread fault, the audio service's doubled thread creation, the producer-consumer corrections sent to a manufacturer — is the same reading skill applied to someone else's code.

It also dates the **architect** behaviour earlier than the title does. Designing the whole system, then handing two developers a component framework instead of a specification, is architecture in 2004, four years into the career.

## Skills demonstrated

Systems design from a blank page; TCP/IP network-protocol design; multithreaded server design; job isolation and lifecycle on a shared server; cross-platform C++ across Windows, Linux and Solaris; native packaging (`.RPM`, `.DEB`, `.PKG`); shared-source client/server structuring; GoF design patterns implemented rather than cited; idiomatic C++; providing a component framework to other developers; UML modelling and round-trip engineering with Rational Rose; connecting a technical design to two separate business cases (performance and data residency).

## What was blocked, cut short, or wrong

- **The round-trip-engineering discipline did not hold.** That is recorded as a lesson, not a defeat: the model-and-code pairing decays unless something regenerates it, and nothing then could.
- The record does not carry adoption figures, customer names, or how long the product line lived. It is a capability and craft entry; treat the impact claim as bounded by that.

## Evidence

- The [archived full resume](../archive/Oleg.Zhylin.resume.md) § *2004-2005. Client-Server predictive analytics application* — the contemporaneous long-form account: singlehanded development, the daemon, the two client-side developers, the three platforms, the native installers, the shared client/server sources, the GoF library, and the concurrency/parallelism/protocol-design framing.
- The [primary resume](../../../markdown/Oleg.Zhylin.resume.achievements.md) carries the same project in condensed form in both the Salford summary and the 2004-2005 project section, so the substance is already public.
- The owner's statement of 2026-09-16 supplies the Rational Rose round-trip-engineering fact and the RUP/UML/AI reflection, neither of which appears in any earlier document.
- The earlier [audio-service investigation](2023-09-26-audio-service-race-condition-diagnosis.md) § *The wider thread* already cited this project as the origin of the concurrency specialization; this entry is the record that citation pointed at.

## Evidence limitations

**The filename date `2004-01-01` is a placeholder for an undated range.** Only the years 2004-2005 are established, from the archived resume's own section heading; no month, milestone date or release date is recorded anywhere in the corpus. Do not quote a start or ship date from the filename.

Everything technical here comes from the owner's own contemporaneous long-form resume rather than from code, tickets or a release record — that source is detailed and was written far closer to the events than today, but it is one source and it is self-authored. No customer, revenue, concurrency-level, throughput or uptime figure is recorded, and none is invented. The Rational Rose detail rests on the owner's 2026 recollection alone; the RUP, UML and AI-documentation statements are his stated opinion, labelled as such, not findings.

"Large proportion of the same source files" and "large share of the GoF patterns" preserve the source's own imprecision deliberately; earlier and later renderings say "quite a number" and "a large percentage" of the patterns, and no list survives.

## Related

- [2026-09-16 concurrency and parallelism as a deliberate specialization](2026-09-16-concurrency-parallelism-specialization.md) — the craft this project started: the pattern literature, the industry's attempts to codify parallelism, the Intel Fortran toolchain, Boost.Asio as the day-to-day abstraction, and where C++ coroutines finally landed.
- [2023-09-26 audio-service race-condition diagnosis](2023-09-26-audio-service-race-condition-diagnosis.md) — the same reading skill twenty years on, applied to a bug that never reproduced.
- [2026-04-24 manufacturer audio-service concurrency corrections](2026-04-24-tcl-audio-service-concurrency-corrections.md) — producer-consumer, queue ownership and lock discipline reviewed in someone else's C; the direct descendant of this project's reflexes.
- [2024-05-15 positioning root-cause diagnostics](2024-05-15-skyhook-positioning-root-cause-diagnostics.md) — a multithreading fault in a third-party library, found from telemetry.
- [2026-09-14 Boost proficiency](2026-09-14-boost-library-proficiency.md) — Boost.Asio and Boost.MSM, the libraries that now do what this daemon did by hand.

## Record history

- 2026-09-16: created during the concurrency story pass, from the archived full resume plus the owner's statement of the same day. The project had been cited in two other entries and in `accomplishments-by-domain.md` for a week without an entry of its own; this closes that gap. The Rational Rose round-trip-engineering fact and the RUP/UML/AI reflection are new to the corpus.
- 2026-09-16: graduated into [concurrency/lowest-level-reflexes](../../wiki/stories/concurrency/lowest-level-reflexes.md).
