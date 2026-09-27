---
cluster: concurrency
fits: [embedded, debugging, vendor]
status: draft
runtime: "90 s"
---

# The positioning library leaked twice: the first leak was an easy fix that took a year to ship, and the second one I narrowed down but could not close

## Why I still care

The first time, on the older device, I found a leak by reading code. On the new device there were two, and they taught me different things. The first one was an easy fix — the vendor fixed their library promptly and we took it promptly — and it still took almost a year to reach devices, because the manufacturer's over-the-air update process was broken. The second one only shows after five days without a reboot. A colleague and I worked diligently to rule out the vendor's library, and we did, and the next step needed the manufacturer in the loop and calendar time we did not have. I would rather tell that honestly than pretend it closed.

**Cue:** a device log from October 2023 — the core service failing to collect logs with *"Cannot allocate memory"*, and the location manager publishing a location error in the same second.

## Register

**2020-2026, Best Buy Health.** Ownership and economy. The vendor is "the positioning vendor", the manufacturer is "the manufacturer"; no names. Blocked work told per [voice and prominence](../../workflows/voice-and-prominence.md): what was done, what stands, no blame. Lines per [spoken drafts](../../workflows/spoken-drafts.md), lifted from the owner's account of 2026-09-25.

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | A second descriptor story, on the next device — two leaks this time |
| 1 | Hook | Our software flagged descriptors running out, and it pointed at the positioning library we had bought |
| 2 | Stakes | Location is the product |
| 3 | Complication | The first fix was easy and still took a year to ship; the second leak needs five days of uptime to show |
| 4 | Move | Reproduced it; stripped everything else away; ran the vendor's own test program beside our service — and ruled their library out |
| 5 | Punchline | Narrowed a five-day leak to one place, and got the first fix onto devices |
| 6 | Handover | Where does a fix go to wait in your organisation? |

## Narrative — rehearse verbatim

**0 · Offer**
> There's a second file-descriptor story, on the next device — and this time there were two leaks, not one.

**1 · Hook**
> Our own software noticed descriptors running out, and it pointed at the positioning library we had bought.
⟨breathe⟩

**2 · Stakes**
> On an emergency device, location is the product. A slow leak there is a slow failure of the one thing that has to work.

**3 · Complication**
> The first leak was an easy fix. The vendor fixed their library promptly and we took it promptly, but it took almost a year to get it into firmware, because the manufacturer's over-the-air update process was a mess at the time.
> The second one was harder, because it only shows after five days without a reboot.
⟨breathe⟩

**4 · Move**
> So I built the reproduction and waited the five days. Then, with a colleague, I took everything else away — a build with our other processes turned off, asking for a location every second — and ran the vendor's own test program with the same library, side by side with our service. We worked diligently to rule out the vendor's code, and we did.

**5 · Punchline**
> That narrowed a five-day leak down to one place: our own location client, which the manufacturer wrote. And the first fix did reach the devices, once I pushed it through.
⟨breathe⟩

**6 · Handover**
> I'm curious where a finished fix goes to wait in your organisation.

## If they follow up

- **"So is the second leak fixed?"** → No. The next step is an audit of the location client, and that is the manufacturer's code, so it puts them in the loop. We didn't have the calendar time to add it to the workload. I would rather say that than claim it closed.
- **"Why did the first fix take a year?"** → Not engineering. The manufacturer's over-the-air update process was broken, and they only started working with the update platform's vendor after something broke. Until then the fix sat ready and waiting.
- **"The vendor blamed your service at first — were they right?"** → For the second leak, possibly. That's exactly where we narrowed it to. The difference is that now it's a measurement, not an opinion.
- **"What exactly was the guard?"** → *(owner to confirm: which check counted descriptors, and where it runs — not in the record)*.
- **"Is this related to the location recovery bug?"** → Same library, same months. I have not proved a connection, and I would not claim one.

## Proof

The October 2023 log analysis (the first leak), the reproduction ticket and its stand-up notes (April to June 2024) and the memory comparison (the second leak), and the July 2024 escalation (delivering the first fix) are in the committed board snapshots. The two-leak account itself is the owner's, 2026-09-25.

## Know it — what stays with me

T1: the library is **Skyhook**'s precision-location library for the device's modem platform; the ticket was *reproduce the Skyhook file descriptor issue*; the vendor engineers were Tim Robinson and Preston; the vendor suspected our `locmgr-service` of leaking memory, which I read at the time as possibly *"a euphemism for 'we don't know how in the world this thing still fails after we fixed it'"* — never said outward. The update had been wanted since launch and was held up by the manufacturer transition. The manufacturer is **TCL**; its FOTA process engaged **Redbend** only once something broke, and before that relied on the previous manufacturer **Wistron**'s code. The colleague who ruled out the library with me is **Sergey Galat**. The location client to audit next is `locmgr-service`. The "euphemism" line was about the vendor's evasiveness at the time, and the vendor's suspicion may have been partly right for the second leak — never tell the euphemism.

## Sources

- [2024-04-03 Positioning-library file-descriptor leak reproduction](../../../raw/brag/2024-04-03-skyhook-file-descriptor-leak-reproduction.md)

## Related stories

- [A process leaking file descriptors is like a car with a broken alternator](the-alternator.md) — the first leak.
- [The fault that lost the fix](../positioning/the-fault-that-lost-the-fix.md) — the same library's recovery gap.
- [I argued to buy our positioning per device](../positioning/buying-calendar-time.md) — why the library is there.
