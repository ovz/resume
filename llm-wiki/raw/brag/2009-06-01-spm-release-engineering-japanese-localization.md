---
title: "Release engineering across three parallel SPM 6.6 build tracks, and a full Japanese resource-table localization"
date: "2009 to 2010"
thread: SALF
domains:
  - "Build, release, CI/CD"
  - "Internationalization"
context: "Salford Systems — Salford Predictive Modeler (SPM) 6.6"
sensitivity: private-repo
resume-worthy: maybe
---

# Release engineering across three parallel SPM 6.6 build tracks, and a full Japanese resource-table localization

## What I did

Ran the daily-to-weekly build/release cycle for **Salford Predictive Modeler (SPM) 6.6** across three parallel build tracks — English (`SPM_En`), Japanese (`SPM_Jp`), and license-protected (`SPM_protected`) — acting as the central reviewer and triager of Mantis bug reports spanning the GUI and the CART/TreeNet engine underneath it.

The largest single piece of it was a **full literal-string-to-resource-table localization effort** for the Japanese build (`SPM_Jp`, ILOC-based string replacement) — a genuine internationalization project restructuring how the codebase held text, not a pass of one-off string fixes. Alongside it, I made **platform-support-floor calls** — dropping Windows 2000 support and setting Windows XP as the minimum — weighing customer impact against the engineering cost of continuing to support an aging platform.

Correspondents on the Gmail threads this is drawn from: Jeffrey Powers, Phillip Colla, Bernie Bernstein, Igor Goncharov, Borys Tysik.

## Why it matters

This is release-engineering and internationalization ownership predating the resume's existing i18n entries (Unicode SPM is dated 2011 in the corpus; this pushes the effort's start back to 2009-2010) and predating the GitHub/monorepo-era build discipline captured from 2021 onward. It shows the same "own the release process end to end" pattern a decade before the later, better-evidenced instances.

## Skills demonstrated

Multi-track release management; cross-cutting bug triage across GUI and engine layers; internationalization architecture (resource tables vs. literal strings); platform-support-floor decision-making balancing customer and engineering cost.

## Evidence

A 2026-09-16 breadth-first Gmail survey (`oleg.zhylin@gmail.com`) identified this as a distinct thread, reached via CC'd/forwarded mail to `ovz@salford-systems.com`. The survey read snippets only, not full threads, and did not attempt to date individual releases or extract specific Mantis ticket counts.

## Evidence limitations

**This entry is a breadth-first candidate, not a deep-dive.** It rests on a single-pass Gmail survey that named the participants, the three build tracks, and the localization/platform-floor decisions, but did not read full threads, pull specific dates, quantify the Mantis backlog, or confirm exact ILOC mechanics. No resume-worthy numbers (release cadence, bug counts, localization string count) are recorded because none were extracted.

**More detail could be mined from Gmail via the Gmail connector available to Claude.** That follow-up mining is deferred — to be done in a later session, either on this desktop or in a Claude web chat similar to the one that produced the source survey — not performed as part of this ingest pass.

## Related

- [2010-01-01 SPM engine debugging — CART/TreeNet/MARS internals](2010-01-01-spm-engine-debugging-cart-treenet-mars.md) — the same build era's lower-level engine work.
- [2009-02-01 SPM_protected / Wibu-Systems CodeMeter integration](2009-02-01-spm-protected-wibu-codemeter-license-integration.md) — the third build track this entry names.

## Record history

- 2026-09-16: created, ingested from inbox note "gmail-brag-file-candidates.md" (candidate 1).
