---
title: "Core-engine debugging in CART/TreeNet/MARS, and an assertions-as-watchdogs debugging philosophy"
date: "2009 to 2012"
thread: CONC
domains:
  - "ML products and GUIs"
  - "Legacy code and platform migrations"
context: "Salford Systems — SPM statistical/predictive-modeling engine (CART, TreeNet, MARS)"
sensitivity: private-repo
resume-worthy: maybe
---

# Core-engine debugging in CART/TreeNet/MARS, and an assertions-as-watchdogs debugging philosophy

## What I did

Sustained low-level C/C++ debugging inside the statistical engine itself, not the GUI layer around it: chasing assertion failures tied to **MARS model/grove pointer lifetime**, fixing **R-squared computation paths shared between the `SCORE` command and TSLS**, and reasoning through **partial-dependency plot semantics** in direct technical dialogue with the engine's own author, Dan Steinberg.

The standout artifact is a verbatim, quotable statement of engineering philosophy from these threads: *"I prefer to treat assertions as watchdogs which only get activated if the abnormal situation..."* — a debugging-discipline quote worth keeping intact rather than paraphrasing.

## Why it matters

This is evidence of engine-level (not application-level) C/C++ debugging, plus direct technical collaboration with the algorithm's inventor — a different kind of credibility than the GUI/release-engineering side of the same era. It also gives the owner's twenty-year concurrency and reliability narrative (see the [2004 client-server daemon](2004-01-01-spm-client-server-tcpip-daemon.md) and later [audio-service diagnoses](2023-09-26-audio-service-race-condition-diagnosis.md)) an intermediate data point: assertion-driven, watchdog-style defensive engineering practiced consistently across a career, not adopted late.

## Skills demonstrated

C/C++ debugging in a numerical/statistical engine; assertion-based defensive design ("assertions as watchdogs"); shared-code-path bug isolation (`SCORE`/TSLS); direct technical dialogue with an algorithm's original author on model semantics.

## Evidence

A 2026-09-16 breadth-first Gmail survey identified this thread from correspondence with Dan Steinberg and others, including the verbatim assertions-as-watchdogs quote. The survey worked from snippets, not full threads.

## Evidence limitations

**Breadth-first candidate, not a deep-dive.** The survey preserved one strong verbatim quote and named the technical areas (grove-pointer lifetime, R-squared/TSLS, partial dependency) but did not extract specific bug identifiers, fix dates, or the full context of the assertions-as-watchdogs statement. The philosophy quote is recorded here exactly as surfaced; it should be re-verified against the full email before it is used outward as a direct quotation.

**More detail could be mined from Gmail via the Gmail connector available to Claude** — reading the full thread(s) with Dan Steinberg to get the complete quote, dates, and surrounding technical context. That mining is deferred to a later session (this desktop or a Claude web chat), not performed here.

## Related

- [2009-06-01 SPM release engineering and Japanese localization](2009-06-01-spm-release-engineering-japanese-localization.md) — the same build era's release-process side.
- [2004-01-01 client-server TCP/IP daemon](2004-01-01-spm-client-server-tcpip-daemon.md) — the concurrency origin this entry's defensive-coding discipline extends.
- [2012-06-01 SPM 7.x Linux port and TBB evaluation](2012-06-01-spm7-linux-port-tbb-evaluation.md) — later cross-platform engine work in the same codebase.

## Record history

- 2026-09-16: created, ingested from inbox note "gmail-brag-file-candidates.md" (candidate 2).
