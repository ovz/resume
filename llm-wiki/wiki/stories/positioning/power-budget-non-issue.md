---
cluster: positioning
fits: [embedded, firmware, architecture, principal, product]
status: draft
runtime: "2 min"
---

# We decided the battery before we decided what the device looked like

## Why I still care

This is the one where I got to argue about the *order* of decisions rather than the decisions themselves, and won. I was afraid of the version of this device where industrial design hands you an enclosure and you spend two years apologizing for what fits in it. What I am proud of is that "positioning should be a non-issue in the power budget" is a sentence an engineer can build against — it survived being repeated by people who were not in that room.

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | There is one from the next-generation wearable about the order you make decisions in |
| 1 | Hook | We decided the battery before we decided what the device looked like |
| 2 | Stakes | A senior wears it or leaves it on the dresser; a dead device is not an emergency device |
| 3 | Complication | Battery and hardware oppose each other in both directions at once, and positioning is the biggest single thing that can eat the budget |
| 4 | Move | Made the budget the first-class constraint, wrote the trade-offs out, set positioning's target in budget terms, then designed a wake-up chain that starts at the sensor |
| 5 | Punchline | The application processor sleeps. The sensor decides when anyone else needs to be awake |
| 6 | Handover | Where does the power budget get decided where you are — before the enclosure, or after? |

## Narrative — rehearse verbatim

**0 · Offer**
> There is one from the next-generation wearable I still think about. It is not about a bug. It is about the order you make decisions in.

**1 · Hook**
> We decided the battery before we decided what the device looked like.
⟨breathe⟩

**2 · Stakes**
> This is an emergency-response device for seniors. If the battery does not last, it is on the dresser instead of on the person, and a device on the dresser is not a device.
*(optional)* Charging is the failure mode nobody puts in a spec. You can build everything right and still lose to a charger the user resents.

**3 · Complication**
> Here is what makes it hard. Battery and hardware fight each other in both directions. A bigger battery powers more hardware — and a smaller battery leaves physical room for more hardware. Both are true. So you can argue either side forever, one component at a time.
> And capable hardware costs you twice. Once for the part, and again for the software that finally uses it properly.
⟨breathe⟩

**4 · Move**
> So I stopped arguing components and wrote the trade-off structure down. Battery against hardware. Cost against capability. Which of these is researchable and which is a creative choice. Battery capacity you can go and measure. A form factor is someone's judgement. You do not let the judgement call constrain the measurable one.
> Then I gave positioning a target in the same units. Not "make it efficient." The goal was: **location should be a non-issue in the power budget.** We spend some power to know where the device is, it is never a major line item, and a mistake there cannot sink the battery.
*(optional)* That sentence did more work than the document around it. People who were not in the room repeated it back to me for the next two years.
> Then the architecture is just that sentence made real. The device sleeps by default. A motion sensor with a machine-learning core on the die decides that the user is actually moving. That wakes a small BLE microcontroller, not the application processor. The microcontroller keeps a relative position estimate going. The big processor only wakes when the reckoning fails, or when temperature says we just went outdoors and a satellite fix is finally worth attempting.
*(optional)* Every level you climb multiplies the cost — sensor, microcontroller, modem, application processor. So you start the chain as low as you can get.

**5 · Punchline**
> So the most expensive part of the device spends most of its life asleep, and the cheapest part decides when anyone else needs to wake up.
⟨breathe⟩

**6 · Handover**
> I am curious where that decision sits where you are. Does your power budget get set before the enclosure, or inherited from it?

## If they follow up

- **"Did the microcontroller path ship?"** → Not as designed. Partway through I recorded that backend work and other reasons to run the application processor might mean the MCU never actually reduces the budget — in which case prototyping should be cut short rather than continued for its own sake. That is a negative result I reached and acted on. The framing and the power goal outlived the hardware plan; the positioning work that followed was held to the same constraint.
- **"Where does concurrency come into a power story?"** → Everywhere, because the wake-up chain *is* a concurrency design across two processors. Motion wakes the microcontroller; the microcontroller consumes the sensor's own machine-learning output; the application processor sleeps until it is woken or asks for a position. The protocol between them is where power bugs are born — I corrected the sensor co-processor API specification over whether a call takes or releases a wakelock, because a manufacturer implements that literally. The dedicated-MCU path didn't ship as designed, but the discipline did: concurrency and network programming carry both halves of a device, bare metal and hosted.
- **"How do you know a power claim is true?"** → A power claim without a measurement is an opinion. Engineering build, a handful of devices soaking, a notebook, an answer in days. I would rather have a stated hypothesis and a cheap experiment than an analysis campaign.
- **"What did you argue *down* on battery grounds?"** → A cellular hotspot capability. It would have killed the budget. That is a refusal, not a delivery, but it is the same skill.
- **"Anything you tried that got no traction?"** → I proposed a second positioning timeout so we could measure accuracy against battery instead of arguing it. It landed on deaf ears at the time. I still think it was the cheap version of a question we kept re-litigating.

## Proof

Component-level reasoning anyone in embedded can check: motion classification on the sensor's own ML core, a BLE MCU between sensors and application processor, barometer for stair and fall discrimination, magnetometer for heading and gyro precession, temperature as the outdoors signal. The vendor evaluation was run as a purchase list where each item existed to settle one named experiment.

## Know it — what stays with me

T1: the exact part numbers, the vendor and field-engineer relationships, the internal trade-off cards, the market-segment and competitive reasoning that sat beside the power argument, and the schedule constraint that timeboxed all of it. Component vendors are not named outward.

## Sources

- [2021-11-15 R5 product architecture and power-budget trade-offs](../../../raw/brag/2021-11-15-r5-product-architecture-power-budget-tradeoffs.md)
- [2021-11-22 Dead reckoning and sensor-cluster architecture](../../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md)
- [2021-10-16 Battery and power as a second specialization](../../../raw/brag/2021-10-16-battery-power-second-specialization.md)

## Related stories

- [Every classic pitfall around beacon tracking was survivable alone; together they multiplied](home-away-kept-simple.md) — a later beacon feature on the same device line, assigned in 2023; not an outgrowth of this research.
- [The fault that lost the fix](the-fault-that-lost-the-fix.md) — the same subsystem, seen from the field.
