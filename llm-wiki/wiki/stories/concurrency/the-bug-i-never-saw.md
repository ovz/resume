---
cluster: concurrency
fits: [debugging, embedded, firmware, vendor]
status: draft
runtime: "2 min"
---

# I never heard the bug once, and I still know what it was

## Why I still care

Everybody has a bug they couldn't reproduce. What I like about this one is the moment I stopped trying. I had been chasing it the ordinary way — run it again, run it differently, run it forty times — and the honest read was that I was going to lose. So I changed what I was doing: instead of making the *bug* reproducible, make the *evidence* reproducible. What I was afraid of is the ending this defect was heading for, which is "cannot reproduce, closed" on a device somebody's mother wears.

## Register

**2020-2026, Best Buy Health.** Ownership and economy — short declaratives, bare numbers, no adjectives, and willing to say out loud what is still only a hypothesis. The stakes do the work; do not help them. See [voice and prominence](../../workflows/voice-and-prominence.md) § *The registers, era by era*.

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | I have one where I never once saw the bug happen |
| 1 | Hook | The device would beep instead of speaking. Sometimes it rebooted afterwards. I never caught it once |
| 2 | Stakes | The prompt is how the wearer knows the device heard them. An intermittent wrong sound plus a reboot is a trust problem |
| 3 | Complication | It never reproduced, and it was being debugged as part of a different ticket |
| 4 | Move | Stopped chasing the bug and went after the evidence: correlated logs, a second independent subsystem, fault injection, and a negative experiment |
| 5 | Punchline | In the same second, the handler created its playback thread twice and took the wakelock twice — then thirty seconds of nothing, which is what a forced reboot looks like in a log |
| 6 | Handover | Ask me about the experiment that failed, because it was the useful one |

## Narrative — rehearse verbatim

**0 · Offer**
> I've got one where I never saw the bug happen. Not once.

**1 · Hook**
> The device would occasionally play a single flat beep instead of the voice prompt it was supposed to play. Sometimes it rebooted right after. Intermittent, and nobody could make it happen.
⟨breathe⟩

**2 · Stakes**
> That prompt is how a person wearing an emergency-response device knows it heard them. A wrong sound and an unexplained restart is a trust problem, and it was heading straight for "cannot reproduce, closed."

**3 · Complication**
> Two things made it hard. It never reproduced — I tried, creatively, and I never once got it in front of me. And it had been folded into a different ticket, so two separate problems were being debugged as one.
⟨breathe⟩

**4 · Move**
> So I stopped trying to catch it, and went after the evidence instead.
> First, correlation. Across the logs we collected from the field, audio playback was in progress every time one of those reboots happened — which is exactly why people mostly reported hearing it during the power-on prompt.
> Then I set the device up to incriminate itself. Sessions left running with the diagnostic monitor and the power tool attached, so if it crashed on its own it would leave me a RAM dump. A procedure to reset the reboot counter and clear the logs, so every attempt started from a known state.
*(optional)* I bought a laptop specifically to collect defective audio logs, because the tooling demanded a dedicated machine. That's the unglamorous half of this kind of work.
> And I designed the failure instead of waiting for it. Killed the audio service at arbitrary moments to try to force the same window open.

**5 · Punchline**
> Here's what the logs gave me. In the same second, the audio request handler logged creating its playback thread — twice. And the audio wakelock was acquired — twice. Then a gap. Twenty to thirty seconds of nothing, which is what an externally forced reboot looks like in a log.
⟨breathe⟩
> That's a race in the request handler, and it explains both symptoms with one mechanism: the same double entry either corrupts the sound or leaves the service unhealthy enough that the watchdog takes the whole device down.
*(optional)* And the device agreed from a completely different direction. Its own reboot counter read eleven, against a platform threshold of ten that puts it into a fatal state. Two subsystems that don't know about each other telling me the same story.

**6 · Handover**
> Ask me about the experiment that failed, because that was the useful one.

## If they follow up

- **"The experiment that failed?"** → I ran a shutdown during playback, expecting the artifact. It reliably broke audio and it never once produced the beep. That's a negative result and it's worth as much as a positive one: it separated "audio dies on shutdown" from "audio is corrupted by a race". Two failure modes that looked identical in a bug report.
- **"So did you fix it?"** → No, and I won't claim it. What I had was a strongly-evidenced mechanism, not a proven root cause with a failing test. What I did was make it actionable: I found a deterministic reproduction for the related single-pitch beep and wrote it up as steps, so QA and the manufacturer could see it rather than take my word for it. I separated it from the ticket it had been buried in. And I put it into risk assessment rather than leaving it as a bug report, because a bug report is a request and a risk is a decision somebody has to make. Audio-service work carried on across later releases, and a change of mine reached the firmware in 2026.
- **"Why risk assessment instead of a defect?"** → Because "intermittent, not reproducible, safety-adjacent" is exactly the shape of thing a defect queue loses. Risk assessment is where something gets weighed instead of triaged.
- **"What's the transferable part?"** → A race that reproduces is an ordinary bug. The interesting ones don't. So make the evidence dense enough that the mechanism has nowhere left to hide — correlate independent subsystems, look for the same operation happening twice, treat a negative experiment as information, and instrument so the one occurrence you can't schedule leaves a trace worth having.
- **"Is this just a Linux problem?"** → No. This one lived on the hosted side — threads, a wakelock, a watchdog. The bare-metal side has the same shapes in different clothes: RTOS queues and timers, and a wake-up chain between two processors. On a medical wearable I traced a firmware defect through exactly those FreeRTOS primitives. Concurrency is the embedded fundamental on both halves of the device, not a Linux specialty.
- **"Has this happened to you before?"** → It's most of my career. A third-party positioning library that lost its ability to get a fix, through a multithreading fault while creating a listener thread — root-caused the same way, from telemetry, never reproduced on a bench. And it goes back to 2005, when I built a cross-platform server and hand-wrote every thread in it. That's a separate story if you want it.

## Proof

The investigation is documented in the owner's contemporaneous device-programme board, preserved as a committed export: the quoted device-log excerpts showing the doubled thread creation and doubled wakelock acquisition either side of the reboot gap, the triage notes with the reboot-counter observation and the RAM-dump setup, the written reproduction steps, the shutdown-experiment result, and the fault-injection design. Internal analysis notes dated 27 September 2023 and the log submissions to the manufacturer are internal artifacts.

What the record does *not* contain is the defect's eventual disposition in the employer's tracker. The mechanism is a hypothesis with unusually good evidence, and it is told that way.

## Know it — what stays with me

T1: the manufacturer's identity, the platform and silicon vendor, the diagnostic and power tooling by name, the log field names, the ticket the defect had been folded into, and the specific service and handler. Outward, the manufacturer is "the contract manufacturer" and the platform is "an embedded Linux device". The failure shape and the method are mine to tell.

## Sources

- [2023-09-26 audio-service race-condition diagnosis](../../../raw/brag/2023-09-26-audio-service-race-condition-diagnosis.md)

## Related stories

- [I built the hand-rolled version in 2005](lowest-level-reflexes.md) — the same subsystem three years later, from the other side: reading another team's code and naming the races precisely enough to be fixed.
- [The fault that lost the fix](../positioning/the-fault-that-lost-the-fix.md) — the same method one subsystem over, and the story to tell if the listener wants the telemetry version rather than the log version.
