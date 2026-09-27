---
title: "Root-caused a file-descriptor leak into the chip vendor's QMI routing code by reading it and experimenting by hand, and chose mitigation because the fix was out of reach"
date: "2021-05 (owner's briefing card; the investigation preceded it)"
thread: CONC
domains:
  - "Embedded and safety-critical devices"
  - "Legacy code and platform migrations"
context: "GreatCall / Best Buy Health — Lively Mobile+ (R4), embedded Linux on a Qualcomm modem SoC"
sensitivity: private-repo
resume-worthy: maybe
storied:
  - "concurrency/the-alternator"
---

# Root-caused a file-descriptor leak into the chip vendor's QMI routing code by reading it and experimenting by hand, and chose mitigation because the fix was out of reach

## What I did — the owner's account (2026-09-24, verbatim)

> There is also related story that Skyhook, and even Qualcomm QMI in separate scenarios badly leaked file descriptors. QMI incident is where I read a ton of Qualcomm code and did a number of experiments pre-AI by hand. skyhook is where FD guarding condition saved the day and pointed at a problem. This is at least 2 stories, maybe even more than that because discourse of wathing out for File Descriptors on Linux where everything is a file makes a good conversation. Process that leaks file descriptors is subject to OOM killer. in practice, though, OOM might arrive late or even never on an Yocto embedded system and process with file descriptor failures at random places is like alternator broken on a car. Because alternator give electricity to every piece of modern car the failure modes and funny behaviours are abundant

This entry is the QMI half; the Skyhook half is [2024-04-03](2024-04-03-skyhook-file-descriptor-leak-reproduction.md).

## What the record shows

A card in the owner's one-on-one agenda, created in May 2021: *"I would like to brief you on root causing File Descriptors. As expressed before in my opinion the conditions for this are complex and mitigation is the only realistic way to address it for R4. This is because we cannot engage Qualcomm's help to fix QMI routing code."*

QMI is the Qualcomm MSM Interface, the message protocol between the application processor's services and the modem. A leak there sits under every service that talks to the modem, which on a cellular emergency device is most of them.

## Why it matters

- **He went to the vendor's code rather than stopping at the symptom.** Without AI assistance, reading a large body of unfamiliar vendor code and designing experiments to isolate which path leaked is slow, unglamorous work.
- **He made the engineering call the constraints allowed.** With the vendor unreachable for a fix, the right answer was a mitigation the team could own, stated plainly to his manager as a decision with its reason.
- **The failure mode is worth explaining to any listener.** On Linux everything is a file — sockets, pipes, device nodes, timers — so a process that leaks descriptors eventually fails at `open`, `socket` or `accept` with a per-process limit error, at whatever call happens to come next. Descriptors cost little memory, so the out-of-memory killer may arrive late or never on a small embedded Linux system. The owner's comparison is a broken alternator in a car: it feeds everything, so the symptoms turn up everywhere and all look different.

## Skills demonstrated

Linux resource-lifetime debugging; reading and experimenting against third-party vendor code; embedded Linux (Yocto-class) failure modes; choosing mitigation over a fix when the fix is not available, and saying so.

## What was blocked, cut short, or wrong

- **The root cause stayed unfixed at the source.** The chip vendor could not be engaged to fix the QMI routing code for R4. What shipped was a mitigation.
- **The mitigation itself is not described in the record** — the owner's account and the one agenda card are all that is retained.

## Evidence

Leadership board (committed Trello snapshot): the agenda card created 2021-05-19. The owner's statement above. Error semantics: `open(2)`, EMFILE — "The per-process limit on the number of open file descriptors has been reached" ([man7.org](https://man7.org/linux/man-pages/man2/open.2.html), fetched 2026-09-24).

## Evidence limitations

The experiments, the leaking path and the mitigation are the owner's recollection; no code, ticket or test log is retained. Outward, the claim is the technique and the judgement, not a specific defect in a vendor's product — the chip vendor is not named.

## Related

- [2024-04-03 Skyhook file-descriptor leak reproduction](2024-04-03-skyhook-file-descriptor-leak-reproduction.md) — the second leak, on the next device.
- [2023-09-26 audio-service race-condition diagnosis](2023-09-26-audio-service-race-condition-diagnosis.md) — another failure that had to be found without being reproduced on demand.
- [2026-09-16 concurrency and parallelism specialization](2026-09-16-concurrency-parallelism-specialization.md) — lifetimes are half of what that specialization is about.

## Record history

- 2026-09-24: created from the owner's TODO note of 2026-09-24 (verbatim above), dated by the committed leadership-board snapshot.
- 2026-09-24: graduated into story `concurrency/the-alternator`; `storied` property added, body untouched.
