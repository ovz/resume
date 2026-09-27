---
title: "Caught a positioning library leaking file descriptors, reproduced it for the vendor in five days, and drove the vendor's experiments to a better library build"
date: "2023-10 to 2026-03"
thread: POS
domains:
  - "Positioning and location"
  - "Embedded and safety-critical devices"
  - "Operational excellence and observability"
context: "Best Buy Health — Lively Mobile 2 (R5), embedded Linux; third-party Wi-Fi/cell positioning library and its vendor's engineers"
sensitivity: private-repo
resume-worthy: maybe
storied:
  - "concurrency/the-guard-that-counted-descriptors"
---

# Caught a positioning library leaking file descriptors, reproduced it for the vendor in five days, and drove the vendor's experiments to a better library build

## What I did

The owner's account (2026-09-24) is preserved verbatim in [2021-05-19](2021-05-19-r4-qmi-file-descriptor-leak-mitigation.md); for this half: *"skyhook is where FD guarding condition saved the day and pointed at a problem."*

- **October 2023 — the first sign.** Investigating a device's logs he flagged a possible file-descriptor issue: the core service failing to collect logs with "Cannot allocate memory", the location manager publishing a location error at the same second, a location sync timing out, and a gap in another service's log. A descriptor guard in the device software is what surfaced it, in the owner's account.
- **April 2024 — reproduced it.** Ticket: *reproduce the Skyhook file-descriptor issue with the vendor's library for the device's modem platform*. "It took 5 days to reproduce." The next experiment he specified needed a custom build with the core and cloud-connection processes disabled in the device's process supervisor, or a core that did no MQTT and requested a location every second — isolating the library from everything else.
- **May–June 2024 — worked the vendor.** Followed up the vendor's engineers when promised updates slipped; the vendor suspected the device's own location service of leaking memory, which he read as possibly "a euphemism for 'we don't know how in the world this thing still fails after we fixed it'", and answered with the next logical experiment: comparing memory use between the device's location service and the vendor's own test program running the same library, then testing a newer library version supplied for the purpose.
- **July 2024 — got the update through.** When the library update stalled inside the team, he escalated it, reminding everyone the update had been wanted since launch and could not be planned during the manufacturer transition; he "went all the way through to arrive at the best version of the library executable" and offered to show how customer impact could be observed.

### Follow-up, 2026-09-25 — two leaks, not one (the owner's account, verbatim)

> There was one skyhook leak that was an easy fix. We had updated library promptly but couldn't put it into firmware for almost a year because TCL FOTA mess up (they only started talking to redbend when they broke something; before then TCL seemed to rely on Wistron code and their own reasoning). So in brag files there is initial leak discovery, relatively low hanging fix, and another leak that manifests 5 days with no reboot, and that one still stands because TCL is needed to debug that one further. Sergey Galat and I worked diligently to rule out what skyhook code does wrong and next step is to audit locmgr-service client code which would put TCL in the loop and we didn't have calendar time to add this to workload.

How the dated record above maps onto his account:

- **Leak 1 — found, fixed quickly, delivered late.** The October 2023 log analysis is the discovery. The vendor's library fix came promptly and the team took the updated library promptly; getting it *into firmware* took almost a year, because the contract manufacturer's firmware-over-the-air process broke down. It engaged the FOTA platform vendor (Redbend) only once something had broken, and until then had relied on the previous manufacturer's (Wistron's) code and its own reasoning. The July 2024 escalation — "wanted since launch", held up by the manufacturer transition — is that delivery.
- **Leak 2 — manifests after five days without a reboot, and still stands.** The April 2024 ticket's "it took 5 days to reproduce" is this leak's signature: it needs five days of uptime to show. With **Sergey Galat** he worked to rule out the vendor library as the cause — the stripped-down build and the side-by-side memory comparison against the vendor's own test program are that work. The next step is an audit of the device's own location-service client code (`locmgr-service`), which is the manufacturer's code and would put it in the loop; there was no calendar time to add that to the workload. The 2026-03 "file descriptor ticket in review" note belongs to this thread.

## Why it matters

A descriptor leak in a positioning library is a slow failure of the device's most important function, and it shows up everywhere except where it starts. A guard that counts what should not grow, a reproduction the vendor could not dismiss, and a sequence of experiments that separated "their library" from "our service" turned an argument into evidence. It is also the same library and the same months as [the fault that lost the fix](2024-05-15-skyhook-positioning-root-cause-diagnostics.md).

## Skills demonstrated

Resource-leak detection and reproduction on embedded Linux; experiment design to isolate a third-party library; vendor engineering engagement and follow-through; escalation with a stated reason; linking a low-level fault to customer impact.

## What was blocked, cut short, or wrong

- **The fix lived on the vendor's clock.** His own note: tickets to fix the leak "live on Qualcomm time, not necessarily aligned with our sprint".
- **The library update was delayed by the manufacturer transition** before he pushed it through.
- **The second leak is not fixed.** The library was ruled out; the remaining suspect is the device's own location-service client, which is the contract manufacturer's code, and the audit that would settle it was never scheduled for lack of calendar time. This is told as it stands.
- **The first fix sat outside firmware for almost a year** because of the manufacturer's over-the-air update process — a delivery problem, not an engineering one.
- **The vendor's suspicion of the location service may have been partly right** for the second leak. The owner's contemporaneous "euphemism" reading was about the vendor's evasiveness at the time; it is never said outward, and it is not the conclusion.
- **The guard itself is not in the record.** Which check counted descriptors, and where, is the owner's statement only; his 2026-09-25 account does not name it.

## Evidence

Device-programme board (committed Trello snapshot): the log-analysis card of 2023-10-12; the reproduction ticket card (2024-04-03) and stand-up notes of 2024-04-16, 2024-05-16, 2024-05-27, 2024-05-28, 2024-06-05 and 2024-06-12; the memory-comparison card (2024-06-06). Leadership board: the escalation card of 2024-07-26, and a 2026-03 note that "file descriptor ticket" was in review.

## Evidence limitations

- **The vendor-side outcome is not recorded** — no release note says the leak was fixed in the later library build.
- **Possible link, inference only (not addressed in the owner's 2026-09-25 account):** the listener-thread creation fault in [2024-05-15](2024-05-15-skyhook-positioning-root-cause-diagnostics.md) is the same library in the same months, and failing to create a thread is a plausible downstream symptom of descriptor or memory exhaustion. Nothing in the record connects them; the owner may.
- Vendor and internal service names stay at T1; outward this is "a third-party positioning library".

## Related

- [2021-05-19 QMI file-descriptor leak](2021-05-19-r4-qmi-file-descriptor-leak-mitigation.md) — the first leak, on the previous device, and the full note.
- [2024-05-15 positioning root cause](2024-05-15-skyhook-positioning-root-cause-diagnostics.md) — the same library's recovery gap.
- [2022-09-16 buying positioning and calendar time](2022-09-16-skyhook-license-buy-calendar-time.md) — why this library is on the device at all.

## Record history

- 2026-09-24: created from the owner's TODO note of 2026-09-24, grounded in the committed Trello snapshots.
- 2026-09-24: graduated into story `concurrency/the-guard-that-counted-descriptors`; `storied` property added, body untouched.
- 2026-09-25: owner's account added as a follow-up — two leaks, the first fixed quickly but delivered late by the manufacturer's FOTA process, the second still open pending an audit of the device's location-service client; Sergey Galat recorded; `date:` widened to 2026-03 because the second-leak work continued; *What was blocked* extended.
