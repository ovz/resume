---
title: "Tracked an audio artifact to a race condition I could never make happen on demand"
date: "2023-09 to 2026-05"
thread: CONC
domains:
  - "embedded and safety-critical devices"
  - "quality and test automation"
  - "operational excellence and observability"
context: "Best Buy Health — Lively Mobile 2 device firmware, audio service on an embedded Linux Qualcomm MDM platform"
sensitivity: private-repo
resume-worthy: yes
storied: [concurrency/the-bug-i-never-saw]
---

# Tracked an audio artifact to a race condition I could never make happen on demand

## What I did

The device would occasionally emit a **single-pitch beep instead of the audio prompt it was supposed to play** — uncomfortable and confusing for a senior using an emergency-response device, and sometimes accompanied by a reboot. It was reported, it was intermittent, and it was the kind of defect that gets closed as unreproducible.

**I never once observed it happen in front of me, despite creative attempts.** So I stopped trying to catch it live and went after it through evidence instead.

**The log correlation.** Across collected device logs I established that audio playback was consistently in progress at the moment a chain reboot occurred — which explained why people mostly reported hearing the artifact during the power-on prompt. Then the smoking gun: in the same second, the audio play-request handler logged **creating its playback thread twice**, and the audio **wakelock was acquired twice**, immediately before a twenty-to-thirty-second gap in the log that marks an externally-forced reboot. That is the shape of a race in the request handler, and it gave a mechanism for both symptoms at once: the same double-entry either produces a corrupted sound or leaves the service unhealthy enough that the platform watchdog takes the device down.

**The second, independent signal.** The device's own reboot counter read 11 against a platform threshold that puts the device into a fatal-UI state at 10 — so the reboot count corroborated the crash story from a completely different subsystem, and told me how far the device had already gone down that path.

**Instrumentation, not repetition.** Rather than run the same manual test more times, I set up to capture the failure if it chose to happen: sessions left running with the modem diagnostic monitor and the power-analysis tool attached so a spontaneous crash would leave a RAM dump; a reboot-counter reset and log-clearing procedure so each attempt started from a known state; a dedicated laptop procured specifically to capture defective audio logs where the tooling demanded it. I designed fault injection instead of waiting — killing the audio service at arbitrary moments to provoke the same window — and ran a shutdown-during-playback experiment, which reliably broke audio *without* producing the artifact, which is itself a useful negative: it separated "audio dies on shutdown" from "audio is corrupted by a race".

**What I made of it.** I found a deterministic reproduction for the related single-pitch beep and wrote it up as steps, so QA and the manufacturer could see the thing rather than take my word for it. I established that this defect was **separate** from another ticket it had been folded into, which stopped two different problems being debugged as one. I submitted it into risk assessment rather than leaving it as an open bug report, and supplied the logs to the manufacturer. Audio-service work continued through later releases, and in 2026 an audio-service change of mine was approved into the firmware.

## The wider thread: concurrency, and the bugs that vanish when observed

This is one instance of a pattern that has run through my whole career, and the reason I treat concurrency as a specialization rather than a skill I happen to have.

- **2004-2005** — I designed and singlehandedly built a cross-platform TCP/IP daemon serving predictive-analytics jobs. That was my introduction to concurrency, parallelism and network protocol design, and it is where the intuition was formed. I still understand networking and multithreading intimately, and would be able to pick up routing and other network-engineering work if a role needed it.
- **2024** — a third-party positioning library lost the ability to obtain a location fix through a **multithreading fault while creating a listener thread**; root-caused from telemetry correlation, with the same method as here: the bug is not reproducible, so make the evidence reproducible instead.
- **This entry, 2023-2026** — the same failure class on a power-managed SoC, where threads, wakelocks and sleep interact and a race can express itself as a *sound* or as a *reboot* rather than as a crash in the code that is wrong.
- **2026** — I worked through TLA+ as one of the year's study items, which is the formal-methods answer to exactly this problem: reason about the interleavings rather than hope to observe them.

The transferable part is the method. A race condition that reproduces is an ordinary bug. The interesting ones do not reproduce, and the only way in is to make the *evidence* dense enough that the mechanism has nowhere left to hide: correlate independent subsystems, look for the same operation happening twice, treat a negative experiment as information, and instrument so that the one occurrence you cannot schedule leaves a trace worth having.

## Why it matters

On an emergency-response device, an audio prompt is not decoration: it is how the wearer knows the device heard them. An intermittent wrong sound plus an unexplained reboot is a trust problem and a safety-adjacent one, and it was heading for "cannot reproduce". Turning it into a named mechanism, a separated defect, a written reproduction and an assessed risk is what made it actionable — and it did so without my ever having witnessed the symptom.

## Skills demonstrated

Concurrency and race-condition diagnosis; embedded Linux and Qualcomm-platform debugging (modem diagnostic monitor, power-analysis tooling, RAM dumps); log correlation across independent subsystems; wakelock and power-state interaction with threading; fault injection; designing a negative experiment; separating conflated defects; writing a reproduction others can follow; risk-assessment framing; working a defect across the manufacturer boundary.

## What was blocked, cut short, or wrong

- **I never reproduced the primary artifact on demand**, and the mechanism remains a strongly-evidenced hypothesis rather than a proven root cause with a failing test.
- The record does not let me claim I shipped *the* fix for it. Audio-service work continued across releases and a change of mine reached the firmware in 2026; the honest statement is that I made the defect tractable and contributed to the work, not that I closed it single-handed.
- Early on, this defect was **being debugged as part of a different ticket**, which cost time before I separated them.

## Evidence

The owner's device-programme board carries the investigation in detail: the quoted device-log excerpts showing the doubled thread creation and doubled wakelock acquisition either side of the reboot gap, the defect-triage notes with the reboot-counter observation and the RAM-dump setup, the reproduction steps, the shutdown-experiment result, the fault-injection idea, and the later sprint records of continued audio-service work. That board is one of the committed Trello snapshots. The internal analysis notes of 27 September 2023 and the manufacturer log submissions are internal artifacts.

## Evidence limitations

Everything above is documented in the owner's own contemporaneous notes; what is absent is the defect's eventual disposition in the employer's tracker. Treat the outcome claim conservatively, as this entry does.

The [later manufacturer-correction effort](2026-04-24-tcl-audio-service-concurrency-corrections.md) now records the owner's report of smooth QA retesting and a subjective user-experience improvement after the team's fixes. That is a distinct, positive outcome in the same subsystem; it does not establish sole closure or a proven one-to-one cause for the original intermittent symptom.

## Related

- [2026-04-24 TCL audio-service concurrency corrections](2026-04-24-tcl-audio-service-concurrency-corrections.md) — the later vendor-facing corrective effort and QA outcome, extending the thread beyond diagnosis.
- [2024-05-15-skyhook-positioning-root-cause-diagnostics](2024-05-15-skyhook-positioning-root-cause-diagnostics.md) — the same failure class and the same method, one subsystem over: a multithreading fault found from telemetry alone.
- [2021-10-16-battery-power-second-specialization](2021-10-16-battery-power-second-specialization.md) — wakelocks and sleep as the power mechanism that this race expressed itself through.
- [2024-12-31-device-test-automation-robot-framework](2024-12-31-device-test-automation-robot-framework.md) — distinguishing broken tests from broken environments; the same refusal to accept "it is flaky" as an explanation.
- [2023-12-05-operational-excellence-launch-readiness](2023-12-05-operational-excellence-launch-readiness.md) — the argument for chaos-style testing where the failures actually live, which is what fault injection is.

## Record history

- 2026-09-13: created from the committed Trello snapshots, prompted by the owner's statement of 2026-09-13 that concurrency and the heisenbugs it brings is a repeating story. Closes the repository's standing note to capture the audio-service troubleshooting as an entry.
- 2026-09-14: linked the distinct April-May 2026 TCL correction effort and later owner-reported QA outcome, retaining the original investigation's attribution and root-cause limits.
- 2026-09-16: graduated into [concurrency/the-bug-i-never-saw](../../wiki/stories/concurrency/the-bug-i-never-saw.md). Body untouched; `storied:` added.
