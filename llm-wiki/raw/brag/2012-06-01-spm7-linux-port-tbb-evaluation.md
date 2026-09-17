---
title: "SPM 7.x Linux port and an Intel TBB threading-library evaluation that reached a documented negative conclusion"
date: "2012"
thread: CONC
domains:
  - "Legacy code and platform migrations"
  - "Architecture and API design"
context: "Salford Systems — SPM 7.1/7.2 cross-platform engine (CentOS 5, Solaris)"
sensitivity: private-repo
resume-worthy: maybe
---

# SPM 7.x Linux port and an Intel TBB threading-library evaluation that reached a documented negative conclusion

## What I did

Technical participant in porting **SPM 7.x** to Linux (CentOS 5) and evaluating **Intel Threading Building Blocks (TBB)** for the engine's threading needs, alongside the existing Solaris port. A colleague, **Ken Bernstein**, flatly concluded that "porting TBB was doomed to fail" for low-level platform reasons — a concrete, technically specific cross-platform/concurrency data point.

## Why it matters

This directly extends the concurrency thread the [2004-2005 client-server daemon](2004-01-01-spm-client-server-tcpip-daemon.md) started, into the SPM 7 era eight years later, and adds a rarer kind of evidence: a **documented negative result** on a concurrency-library choice, reached collaboratively rather than unilaterally. The corpus already records the assertion that "a responsive vendor and an acceptable time-to-resolution are separate things" about the Fortran/Intel compiler dependency in the same codebase family ([2026-09-16 concurrency specialization entry](2026-09-16-concurrency-parallelism-specialization.md)); this is the sibling case where the vendor library itself was rejected outright.

## Skills demonstrated

Cross-platform C++ porting (Linux, Solaris); threading-library evaluation (Intel TBB) against a legacy statistical engine's concurrency needs; reaching and accepting a negative technical conclusion rather than forcing an adoption.

## Evidence

A 2026-09-16 breadth-first Gmail survey identified the thread by keyword (SPM 7.1/7.2, Linux port, Intel TBB, CentOS 5, Solaris) and the verbatim "doomed to fail" characterization attributed to Ken Bernstein.

## Evidence limitations

**Breadth-first candidate, not a deep-dive.** The survey preserved the "doomed to fail" characterization and the named colleague but not the specific low-level platform reasons cited, nor what threading approach (if any) replaced TBB in the port. No completion date for the Linux port itself is recorded.

**More detail could be mined from Gmail via the Gmail connector available to Claude**, specifically the full thread with Ken Bernstein for the technical reasoning behind the TBB rejection and what the port used instead. Deferred to a later session (this desktop or a Claude web chat), not performed here.

## Related

- [2004-01-01 client-server TCP/IP daemon](2004-01-01-spm-client-server-tcpip-daemon.md) — the concurrency origin.
- [2010-01-01 SPM engine debugging — CART/TreeNet/MARS internals](2010-01-01-spm-engine-debugging-cart-treenet-mars.md) — the same-era engine work.
- [2026-09-16 concurrency and parallelism specialization](2026-09-16-concurrency-parallelism-specialization.md) — the Fortran/Intel compiler vendor-dependency sibling case.

## Record history

- 2026-09-16: created, ingested from inbox note "gmail-brag-file-candidates.md" (candidate 4).
