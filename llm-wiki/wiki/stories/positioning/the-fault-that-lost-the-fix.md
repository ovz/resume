---
cluster: positioning
fits: [debugging, embedded, firmware, vendor, crisis]
status: draft
runtime: "2 min"
---

# The counter was not counting errors — it was counting time without a fix

## Why I still care

I never had the device in my hand. Everything I knew came off a fleet, through telemetry, about a library I could not read. What I am proud of is not the root cause — it is that I stopped trusting the number everyone else was reading and asked what it was actually measuring. What I was afraid of is the quiet version of this failure: a device that looks healthy right up to the moment somebody needs it to know where they are.

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | There is one where the hardest part was not the bug, it was the dashboard |
| 1 | Hook | Devices stopped knowing where they were. No crash, no reboot, nothing anyone could reproduce |
| 2 | Stakes | The device calls for help by itself when it detects a fall; on an emergency-response device, location is not a feature, it is the product |
| 3 | Complication | Third-party positioning library, no reproduction, and a fallback path that looked like it was working |
| 4 | Move | Correlated the logs across the fleet, found a multithreading fault creating a listener thread, then found the fallback never actually restored the library |
| 5 | Punchline | The error counter was not counting errors. It was counting how long a device had gone without knowing where it was |
| 6 | Handover | Ask me what we did to the monitor after that |

## Narrative — rehearse verbatim

**0 · Offer**
> There is one from the positioning work where the hardest part was not the bug. It was the dashboard.

**1 · Hook**
> Devices in the field would just stop knowing where they were. No crash. No reboot. Nothing you could reproduce on a bench.
⟨breathe⟩

**2 · Stakes**
> This is a device that calls for help, very often by itself — it detects a fall when the person cannot press anything. Location is not a feature on it. Location is the product.

**3 · Complication**
> Three things made it hard. The positioning library was a third party's, so I could not read it. It never reproduced on demand. And we already had a fallback — when the library could not get a fix, the device fell back to the modem's own positioning. So on paper the device recovered. In the field, some of them never came back.
⟨breathe⟩

**4 · Move**
> All I had was telemetry. So I stopped looking at single devices and started correlating logs across the fleet — which devices, in what order, what else was happening on them at the time.
> The library was failing while creating a listener thread. A multithreading fault, on startup of the thing that was supposed to hand us positions.
*(optional)* Once you can name the moment it breaks, "not reproducible" turns into "not reproducible *yet*", which is a completely different conversation to have with a vendor.
> Then the second half. The fallback worked, but it only covered for the library — it never put the library back. The missing step was restarting the service. Until that happened, the device was running on a backup it was never meant to live on.

**5 · Punchline**
> And then the part I still like. There was a total-errors counter on the device that everyone read as "how many times did this go wrong." But while the fault persisted, it ticked up on a fixed interval. It was not counting errors. It was counting how long that device had gone without knowing where it was.
⟨breathe⟩

**6 · Handover**
> Which changes what you do with it entirely. Ask me what we did to that monitor afterwards.

## If they follow up

- **"What did you do to the monitor?"** → Thresholded it as a duration rather than a count, and documented the reinterpretation so the next person reading the signal inherits the right meaning instead of rediscovering it. A telemetry signal is a contract; when you learn what it really measures, you write that down.
- **"How do you debug a library you cannot read?"** → You debug the boundary. What goes in, what comes out, when it stops, what else was true on that device at that second. Fleet telemetry is a debugger with terrible ergonomics and an enormous sample size.
- **"Did this change anything structural?"** → Yes. The fragmentation this exposed — positioning logic scattered across the system with each source recovering in its own way — is a large part of what the later location engine consolidated behind one arbitration layer.
- **"Was this the same library that leaked file descriptors?"** → Same library, same months — I reproduced a descriptor leak in it for the vendor that spring. I have not proved the two are connected, and I would not claim it; a thread that fails to start is one of the symptoms you would expect. That is its own story.
- **"Isn't the button the main thing?"** → The button reaches a Care agent for any reason at all — loneliness, a ride, a question — and we deliberately do not ration that time. Fall detection and Home/Away are what the device does without being asked. The fall where nobody can press anything is the one that matters most.
- **"How did the vendor take it?"** → Concrete findings travel better than escalations. A named failure point and correlated evidence is a different artifact from "our devices sometimes lose positioning."

## Proof

The diagnosis ran January to May 2024 across internal chat threads and observability-platform log queries. The recovery gap and the reinterpreted counter both fed the fleet-monitoring practice already in place on that device line.

## Know it — what stays with me

T1: the vendor and library identity, the specific telemetry field names, the monitor configuration, and which devices exhibited it. The positioning vendor is not named outward; the failure shape is mine to tell.

## Sources

- [2024-05-15 Skyhook positioning root-cause diagnostics](../../../raw/brag/2024-05-15-skyhook-positioning-root-cause-diagnostics.md)

## Related stories

- [Every classic pitfall around beacon tracking was survivable alone; together they multiplied](home-away-kept-simple.md) — the beacon side of the same positioning subsystem.
- [We decided the battery before we decided what the device looked like](power-budget-non-issue.md) — the same subsystem, five years earlier, before it had users.
