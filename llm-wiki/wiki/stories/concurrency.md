---
cluster: concurrency
aliases:
  - "Concurrency stories"
  - "Parallelism stories"
  - "Race condition stories"
---

# Concurrency, and the bugs that vanish when observed — story cluster

> **Doc type:** reference
>
> Hub for the concurrency cluster: the through-line, the stories planned and written, and the entries each draws on. Open this note's local graph to see the cluster as a sub-graph. Audience: the owner preparing to talk about low-level concurrency; agents writing these stories.

## The through-line

**Twenty years, one skill, spent twice.** In 2004-2005 he built a cross-platform TCP/IP daemon alone — every thread, every lifetime, the wire protocol, on three operating systems, before the standard library had threads. That is where the reflexes were bought. Everything after it is those reflexes spent on code somebody else wrote: an audio artifact diagnosed from doubled log lines without ever being witnessed, a positioning library's listener-thread fault found from fleet telemetry, and a manufacturer's producer-consumer C read closely enough to name each race as an actionable correction.

The arc has a second half that is not about bugs at all: **the abstractions**. The pattern literature, the industry's successive attempts to codify parallelism, a vendor compiler that miscompiled the analytics backend for a year, Boost.Asio as the day-to-day abstraction whose value he can state precisely *because* he built the hand-rolled version first, and C++ coroutines — the right answer, arriving about two years ago, on toolchains an embedded programme does not get to choose.

## Stories

| # | Working title | The claim | Draws on | Status |
|---|---|---|---|---|
| C1 | [I built the hand-rolled version in 2005, so twenty years later I could read someone else's and see it](concurrency/lowest-level-reflexes.md) | The 2005 daemon bought the reflexes; the 2026 audio-service audit spent them — named the races in another company's C precisely enough to be implemented, reviewed every round, and QA reported the service running smoothly afterwards. Boost.Asio and coroutines are the follow-up depth | [2004-01-01 TCP/IP daemon](../../raw/brag/2004-01-01-spm-client-server-tcpip-daemon.md) · [2026-04-24 manufacturer corrections](../../raw/brag/2026-04-24-tcl-audio-service-concurrency-corrections.md) · cited not graduated: [2026-09-16 specialization](../../raw/brag/2026-09-16-concurrency-parallelism-specialization.md), [2026-09-14 Boost](../../raw/brag/2026-09-14-boost-library-proficiency.md) | **draft written** |
| C2 | [I never heard the bug once, and I still know what it was](concurrency/the-bug-i-never-saw.md) | Stopped trying to reproduce an intermittent audio artifact and made the evidence dense instead: correlated logs showing the playback thread created twice and the wakelock taken twice before a forced-reboot gap, a second subsystem's counter agreeing, fault injection, and a negative experiment that separated two failure modes | [2023-09-26 audio-service race-condition diagnosis](../../raw/brag/2023-09-26-audio-service-race-condition-diagnosis.md) | **draft written** |
| C3 | The compiler was wrong, and it took a year | The Intel Fortran compiler miscompiled the Fortran analytics backend; Intel engaged and stayed responsive, and resolution still took a year the business paid for. A responsive vendor and an acceptable time-to-resolution are two different things, and only the second is on your critical path | [2026-09-16 specialization](../../raw/brag/2026-09-16-concurrency-parallelism-specialization.md) § *Living with the Intel Fortran compiler* | **needs dating** — the episode has no year, compiler version or bug identity; owner item |

## Reach for these when

- **"Tell me about your hardest bug"** — C2, then [the fault that lost the fix](positioning/the-fault-that-lost-the-fix.md) if they want a second.
- **Embedded, firmware or systems roles where concurrency is the actual job** — C1. It is the only story in the corpus that shows both halves: building the low-level thing and reading someone else's.
- **Principal or architecture conversations** — C1, because the value in its second half is entirely judgement and influence, with no code written.
- **Working with vendors, manufacturers or silicon partners** — C1's review technique, then C3 once it is dated.
- **"What do you read / how do you keep sharp?"** — C1's follow-ups: the pattern literature, Boost.Asio's guarantees, the coroutine timeline, TLA+ in 2026.
- **"Why do embedded engineers need this?", bare metal versus hosted, or Rust** — C1's follow-ups on the backend contrast and embedded Rust's do-it-yourself mandate, then [the power-budget story](positioning/power-budget-non-issue.md)'s concurrency follow-up for the two-processor wake-up chain. This is the framing the public resume now leads its concurrency achievement with (2026-09-16).
- **Modernization and toolchain judgement** — C1's coroutine follow-up. It is the clearest example in the corpus of separating "the right answer exists" from "we can adopt it".

## Related, not conflated

- **The audio subsystem appears in both C1 and C2, and they are different stories.** C2 is the 2023 *diagnosis* — finding a mechanism for a failure nobody ever witnessed. C1's second half is the 2026 *correction* — reading another company's implementation and driving it round by round to a QA-observed result. Told together they sound like one long saga; told apart, each has its own punchline. If a listener wants both, tell C2 first and let C1 pick it up.
- **[The fault that lost the fix](positioning/the-fault-that-lost-the-fix.md) belongs to [positioning](positioning.md)**, not here, because its payoff is about a misread telemetry signal. It is cross-listed as concurrency evidence and is the right second story when the first one lands well.
- **Two entries are cited but not graduated.** The [Boost entry](../../raw/brag/2026-09-14-boost-library-proficiency.md) supplies C1's Asio material while its Boost.MSM substance belongs to [state machines](state-machines.md); the [specialization entry](../../raw/brag/2026-09-16-concurrency-parallelism-specialization.md) supplies C1's follow-up depth while its Intel Fortran half is C3, unwritten. Neither is marked `storied:` — half-told entries stay in the working graph, because the filter `-[storied]` would otherwise hide material that still needs a story.

## Status

C1 and C2 are written as drafts (2026-09-16) and are ready to **rehearse** — read each aloud once, then set `status: rehearsed` in its frontmatter. C1 is the longer telling at about three minutes and carries the richest follow-up set in the corpus; it is the one to rehearse first.

C3 is blocked on dating, not on writing. The Intel Fortran episode is recorded in full in the specialization entry, but a story needs a year, and inventing one would be the exact failure [voice and prominence](../workflows/voice-and-prominence.md) exists to prevent.

## Before writing more

Two gaps in the record, both cheap to close:

- **The Intel Fortran episode has no date, no compiler version and no bug identity.** It is the whole of C3.
- **"Intel TPL" is ambiguous** — Intel's threading library is TBB (now oneTBB); TPL is Microsoft's .NET Task Parallel Library. The specialization entry preserves the owner's wording and does not pick one.

## Related

- [Story map](story-map.md) — every cluster.
- [Reliability and operations coverage](../resume/coverage/reliability.md) § *CONC* — the claims behind these stories, and which have reached the resume.
- [Voice and prominence](../workflows/voice-and-prominence.md) — C1 deliberately switches register mid-story; that page is why.
