---
title: "Named the lesson of a contractor-built framework frozen without a build-and-run check: a frozen project must still build, and its tests must still run"
date: "2023-01-30 (the observation; the freeze was earlier, during the R5 delays)"
thread: STEW
domains:
  - "Quality and test automation"
  - "Legacy code and platform migrations"
  - "Leadership, management, hiring"
context: "Best Buy Health — Lively Mobile 2 (R5) device software; frameworks built by an outside consultancy"
sensitivity: private-repo
resume-worthy: no
storied:
  - "stewardship/records-nobody-asked-for"
---

# Named the lesson of a contractor-built framework frozen without a build-and-run check: a frozen project must still build, and its tests must still run

## What I did — the owner's account (2026-09-24, verbatim)

> Can be augmented with system-monitor story from best buy era. A contractor team lead by C++ superstar Michael Casey created a system-monitor process to manager lifecycle of r5 device (there is a detailed record of design specs in confluence). The project was fully unit tested. Because of r5 delays we had to defer putting system monitor on actual device. When it was time to resurrect the project unit tests didn't work. If I was in charge of the freeze, I would make sure everything builds and runs. But it was CVK who worked with contractors, and he just took their word for it and never tested himself. system-monitor is still in production with no unit test security harness as no one has time to figure out how to run them. xpmf (extensibe portable mobile framework) is another creation of Michael Casey consulting. It does MQTT handling and has beautiful design, but it relies on niche tool called Genie for interface definitions. No one knows how to build xpmf to this day.

**Names, for the record.** The consultancy is Ciere Consulting and its lead is **Michael Caisse** — the spelling the committed record already uses ([2024-05-08](2024-05-08-ccf-capability-framework-lcm-open-source.md)); "Casey" in the note is phonetic. "CVK" is Christopher VanKirk, the colleague who managed the contractor relationship and wrote its statements of work.

## What the record shows

- **January 2023, contemporaneous:** in a one-on-one agenda, arguing that a new hardware deliverable should be tested as soon as it arrives, the owner wrote: *"The blast from the past is System Monitor from Cierre consulting that we put on hold but didn't go through steps to make sure e.g. unit tests run as expected."*
- **The process supervisor is in production on R5.** It appears in 2022 location work (a way to restart the location service with a logging environment) and in the 2025 security-scan planning.
- **XPMF.** The owner's own May 2024 presentation named the framework as the cautionary precedent for the capability SDKs: brilliant, still in production, and not rebuildable because the toolset that produced it is practically unrecoverable ([2024-05-08](2024-05-08-ccf-capability-framework-lcm-open-source.md)). In May 2024 he and a colleague also discussed whether the SDKs could be a collaboration point with the hospital-at-home engineers, and named "the fate of XPMF" as the main pitfall.

## Why it matters

It is the counterexample to the freeze the owner did run: at the Salford acquisition every stopped project was documented so a stranger could restart it ([2026-09-16 stewardship](2026-09-16-stewardship-first-principle.md)). Here a fully unit-tested project was paused on the contractor's word, nobody built it or ran its tests at the pause, and when it came back the tests did not run. The component shipped anyway, and it still has no working test harness. The rule the owner takes from it is short: a freeze is only a freeze if on the day you stop, someone who is not the author builds it and runs its tests, and writes down how.

## Skills demonstrated

Recognising a stewardship failure mode and turning it into a rule; due diligence on third-party deliverables; build reproducibility as part of custody.

## What was blocked, cut short, or wrong

- **The owner did not run the freeze and could not fix it after.** The resurrected component went to production without its tests running, and "no one has time to figure out how to run them".
- **XPMF's build toolchain remains unrecoverable** in the owner's account.

## Evidence

Leadership board (committed Trello snapshot): the agenda card of 2023-01-30 quoted above; the statement-of-work cards of 2021-12-28 and 2022-01-25. Device-programme board: the positioning-logging card of 2022-09-29 and the stand-up notes of 2024-05-29. The design specification the owner mentions is on the employer's wiki and is not reproduced.

## Evidence limitations

The unit tests' state at the pause, and who decided what, are the owner's account plus the one contemporaneous card. The telling is about what a freeze needs, not about a colleague; per [voice and prominence](../../wiki/workflows/voice-and-prominence.md) § *Humility, respect and trust*, no telling assigns blame, and the colleague and the consultancy are not named outward. Internal component names have public aliases in [sensitivity tiers](../../wiki/workflows/sensitivity-tiers.md).

## Related

- [2026-09-16 stewardship as a first principle](2026-09-16-stewardship-first-principle.md) — the freeze done right.
- [2024-05-08 component framework](2024-05-08-ccf-capability-framework-lcm-open-source.md) — where XPMF is named as the precedent to avoid.
- [2026-05-02 device unit-testing practice](2026-05-02-device-unit-testing-practice-across-repositories.md) — the test discipline this lacked.

## Record history

- 2026-09-24: created from the owner's TODO note of 2026-09-24 (verbatim above), grounded in the committed Trello snapshots; consultancy and lead spellings corrected to the committed record.
- 2026-09-24: graduated into story `stewardship/records-nobody-asked-for`; `storied` property added, body untouched.
