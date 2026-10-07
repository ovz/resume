---
cluster: about-me
fits: [leadership, principal, observability, operations, defence]
status: draft
runtime: "90 s spoken in full, 40 s without the optional lines"
---

# I presented our monitors and caught a misbehaving device in front of the room

## Why I still care

The owner, 2026-10-02: *"results not communicated don't exist. So my outcomes are always eagerly advertised and I make sure to maximize impact by giving recipients the autonomy credit."* This is the episode where both halves happened in one hour: the monitoring work left the team that built it, proved itself live in front of the people it was meant for, and ended with an invitation for them to own it too.

**The cue:** the spike on the screen, mid-talk, and the moment the monitor narrowed it to one device. *(Owner to confirm or replace with his own image of the room.)*

## Register

Best Buy Health, 2024: ownership and economy, and plain enthusiasm about a thing that worked. The live catch is a fact; it is said flat, never dramatised. See [voice and prominence](../../workflows/voice-and-prominence.md).

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | A talk where the demo did something he had not planned |
| 1 | Hook | Found a misbehaving production device, live, in the middle of the talk |
| 2 | Stakes | Emergency-response wearables; monitoring built for one product, invisible to the teams around it |
| 3 | Complication | The work was inside one team, and the other teams had no way to know about it |
| 4 | Move | Took the programme to the cross-team engineering community; framed dashboards against tuned alerts; investigated a spike live |
| 5 | Punchline | One device, found on the spot — and the talk closed by inviting the other teams to subscribe to the monitors and help tune them |
| 6 | Handover | A question about how their teams share what monitoring finds |

## Narrative — rehearse verbatim

*Agent-drafted from the source entry; the only line in the owner's own words is his rule in beat 3. Replace beat 4's live moment with his own memory of it.*

**0 · Offer**
> I gave a talk in 2024 where the demo did something I hadn't planned.

**1 · Hook**
> Halfway through a presentation about our fleet monitors, I found a misbehaving production device, live, in front of the room.
⟨breathe⟩

**2 · Stakes**
> The devices are emergency-response wearables for seniors. We had built the monitoring for one product, inside one team, and it was already catching problems before customers reported them.
*(optional)* Shortly after launch it had caught a battery-overheating condition early.

**3 · Complication**
> But all of that was inside one team, and the other device teams had no way to know about it. The way I put it to myself is that results not communicated don't exist. So I took the programme to the engineering community of practice, where the other device and platform teams were.
⟨breathe⟩

**4 · Move**
> I framed it around one trade-off. A dashboard only works while somebody is looking at it, so for anything that matters we tuned an alert that keeps watching. I walked through our two fundamental monitors, and the smaller ones we had added as the fleet grew. Then there was a spike on the screen, so I used a monitor to investigate it in front of everyone.
*(optional)* The spike was in alert volume, and the monitor narrowed it to location-service errors.

**5 · Punchline**
> It was one device, generating an abnormal volume of errors, and we found it on the spot. I closed the talk by inviting the other teams to subscribe to the monitors and help us tune them.
⟨breathe⟩

**6 · Handover**
> How do your teams share what their monitoring finds with each other?

## If they follow up

- **"Was the catch staged?"** → No. It was a real production device and a real spike, and I had not seen it before the talk. Say it plainly; it is the most checkable part of the story.
- **"Did the other teams take you up on it?"** → *Owner to answer from memory.* The record shows the invitation, not the adoption; if unsure, say the invitation is what I can vouch for.
- **"How was the monitoring built?"** → Hand over to the production-readiness cluster: agentless device-health telemetry chosen because no agent fit the memory budget, a wide-contract event schema, and anomaly detection tuned from ARIMA/SARIMA first principles.
- **"Why bother presenting? You could have just built it."** → Because a result nobody hears about does not change anything outside the team, and the other teams owned devices with blind spots of their own. The talk was how the work reached them.
- **Defence listener** → This is reporting while acting on the intent: the work was done, and the people who could use it were told and given a part in it. Let them name it.

## Proof

A recorded presentation and an internal write-up for the community-of-practice talk, April 2024. Both are internal; nothing here is public.

## Know it — what stays with me

- The observability platform is Datadog; the talk was to Best Buy's cross-team engineering community of practice. Say "our observability platform" unless the listener names the vendor.
- The spike was in personal-alert volume; the device was producing location-service errors. Do not describe the defect behind it.
- The battery-overheating catch shortly after the 2024 launch is a separate, earlier proactive catch.

## Sources

- [2024-04-18 community presentation and the live catch](../../../raw/brag/2024-04-18-r5-datadog-community-presentation.md)
- [2026-10-02 autonomy and communicated outcomes](../../../raw/brag/2026-10-02-autonomy-and-communicated-outcomes.md) — the practice this story shows.

## Related stories

- [I learned the test framework in two days, so I spent the assignment growing the people around it](the-assignment-i-spent-on-people.md) — the companion: there the result is handed on, here it is made known.
- [Production readiness](../production-readiness.md) PR3, *I retired my own monitor* — the same portfolio, owned as a product.
