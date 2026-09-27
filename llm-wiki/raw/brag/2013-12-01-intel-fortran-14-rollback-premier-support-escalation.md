---
title: "Owned the Intel Fortran toolchain for SPM through a compiler regression: certified, rolled back, escalated to Intel, and standardised the team"
date: "2013-05 to 2015-06"
thread: CONC
domains:
  - "Build, release, CI/CD"
  - "Legacy code and platform migrations"
context: "Salford Systems — SPM's Fortran computational backend, Intel Visual Fortran / Parallel Studio on Windows and Linux, team in the U.S. and Ukraine"
sensitivity: private-repo
resume-worthy: maybe
storied:
  - "concurrency/the-compiler-was-wrong"
---

# Owned the Intel Fortran toolchain for SPM through a compiler regression: certified, rolled back, escalated to Intel, and standardised the team

## What I did

This is the dated record of the episode the [2026-09-16 specialization entry](2026-09-16-concurrency-parallelism-specialization.md) describes as "nasty compiler bugs that were not fixed for a year of active collaboration" — SPM's numerical backend is Fortran, derived from Jerome Friedman's original code, and it was built with Intel's compiler.

- **May to November 2013 — a first Intel Premier Support case.** A defect in the Visual Studio integration of Intel's Fortran debugger ("Fee.dll terribly slows down the debugger") ran as a Premier Support issue for six months of updates. Salford held Premier Support through the owner's account.
- **December 2013 — certified the upgrade.** He confirmed Intel Visual Fortran XE 14.0.1 "stable enough", asked the team to upgrade, and moved the build server to Parallel Studio with project configuration set to always use Fortran 14.
- **January 2014 — rolled it back.** Six weeks later: *"Given a number of issues we are having with Intel Fortran 14 we stick with Fortran 13 for the time being"* — precise instructions to the Ukrainian and U.S. developers to pin the 2013 compiler for both 32- and 64-bit, and to take core libraries only from the build server configured that way. The issues were a linker problem, a CART crash, and **internal compiler errors in Release builds at full optimisation**, which he was working with Intel support. He also checked the Unix side: a colleague building at `-O2` was not hitting them, "which might explain why you're not running into compilation issues".
- **May 2014 — escalated.** He re-opened Premier Support issue 6000037617 and asked Intel to escalate it: *"I did not receive adequate help from the person who was helping me. I would like to escalate issue."* He then wrote directly to Intel's Fortran support lead about the internal compiler error.
- **June 2015 — standardised.** The team moved together to Parallel Studio XE 2015 Update 4, build server first, because *"best is to have everyone running the same version of the compiler"*.

## Why it matters

The numerical core of a machine-learning product depended on one vendor's optimising compiler, and the owner was the person who decided which compiler the whole team — two continents, several build hosts — was allowed to use. The sequence is a toolchain-stewardship pattern that still applies: certify on the build server, pin every workstation to the same version, roll back quickly when release builds break, escalate when first-line support stalls, and move again only together. It is also why, a year earlier, he had argued for care before moving the C++ codebase onto Intel's compiler ([2012-12-18](2012-12-18-intel-cpp-compiler-migration-careful-path.md)).

## Skills demonstrated

Toolchain ownership across a distributed team; compiler-regression triage (optimisation-level differences, internal compiler errors); vendor escalation; release-build stability; reproducible developer environments before containers made them easy.

## What was blocked, cut short, or wrong

- **The lesson the owner draws, in his words (2026-09-16):** "Intel was responsive, but it costed our business that time to resolution was highly suboptimal." A responsive vendor and an acceptable time-to-resolution are two different things.
- **Pinning an old compiler is itself a cost** — it delays whatever the new one would have brought, and it was carried for about a year and a half.

## Evidence

Mailbox threads, Salford Systems work account: Intel Premier Support issue 696480 updates (May–November 2013); "Development tools upgrade" (2013-12-01/06); "Fortran compiler setting, v13 versus v14" and "Sticking with Fortran 13 for now" (2014-01-13 to 01-23); "Escalate issue 6000037617" (2014-05-05); "Compiler Internal Error" (2014-05-22, auto-reply from Intel's Fortran support lead); "Intel Parallel Studio Update 4" (2015-06-06/08).

## Evidence limitations

- **The fix is not in the record read.** No closure of issue 6000037617 or release note naming a fix was found; "a year of active collaboration" is consistent with December 2013 to late 2014 or 2015 but is not proven by a closing message.
- **What the bug was — settled by the mailbox (owner's ruling, 2026-09-25: "Use the information grounded in emails as authoritative").** The record shows internal compiler errors in full-optimisation Release builds, a linker problem and a CART crash. It does not show a silent miscompilation, so tellings say "internal compiler errors" and not "miscompilation". This episode is also the *later* one: the C++ compiler argument ([2012-12-18](2012-12-18-intel-cpp-compiler-migration-careful-path.md)) came a year before it, not after.

## Related

- [2012-12-18 Intel C++ compiler migration pushback](2012-12-18-intel-cpp-compiler-migration-careful-path.md) — the earlier argument for care.
- [2026-09-16 concurrency and parallelism specialization](2026-09-16-concurrency-parallelism-specialization.md) — the undated account this entry dates.
- [2010-01-01 SPM engine debugging](2010-01-01-spm-engine-debugging-cart-treenet-mars.md) — the same Fortran engines, debugged at their numerical core.

## Record history

- 2026-09-24: created from the Salford mailbox on the owner's instruction to mine it for the Intel communication (TODO note of 2026-09-24).
- 2026-09-24: graduated into story `concurrency/the-compiler-was-wrong`; `storied` property added, body untouched.
- 2026-09-25: owner ruled the email-grounded record authoritative; the "miscompilation" question in *Evidence limitations* is settled as internal compiler errors.
