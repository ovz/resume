---
cluster: positioning
fits: [embedded, firmware, architecture, principal, product]
status: draft
runtime: "2 min"
---

# Every number in the power budget was observed on the bench, and added the way anyone in the industry would add it

## Why I still care

The trade-off itself was never the interesting part — everybody knows battery and hardware fight each other. What I cared about was refusing the shortcut: taking a feature list at its word, or adding numbers that do not belong together, and then building a product on the result. What I am proud of is that anybody in embedded could have checked that budget line by line, and the goal we set on top of it — positioning should be a non-issue in the power budget — survived being repeated by people who were never in the room.

**Cue:** the purchase list for the evaluation — discovery kits, a sensor tile for free-fall tests, and a programmable supply that measures current — where every item existed to settle one named experiment.

## Register

**2020-2026, Best Buy Health**, looking back at 2021. Ownership and economy. The owner's correction of 2026-09-24 is the spine: the trade-off is obvious even to juniors and executives; *the story is about not cutting corners on the estimate*, with a method that matches the industry's standard of care. Lines lifted from that dictation per [spoken drafts](../../workflows/spoken-drafts.md). Replaces the 2026-09-13 telling, which led with the order of decisions.

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | One about the power budget, and not the part people expect |
| 1 | Hook | Everyone knows battery and hardware trade off; the hard part is the estimate |
| 2 | Stakes | A senior wears it or leaves it on the dresser; the budget decides which |
| 3 | Complication | The shortcuts: feature lists taken at their word, headline figures, numbers added wrong |
| 4 | Move | Observed each feature on discovery hardware; took the right datasheet rows; added them the standard way; measured |
| 5 | Punchline | Every number under "positioning is a non-issue in the budget" had been seen on a bench |
| 6 | Handover | How do you check a power number before you believe it? |

## Narrative — rehearse verbatim

**0 · Offer**
> There's one from the next-generation wearable about the power budget, and it is not the part people usually expect.

**1 · Hook**
> Everybody knows that battery and hardware trade off against each other. Juniors know it, executives know it. The hard part is the estimate, and that is where corners get cut.
⟨breathe⟩

**2 · Stakes**
> This is an emergency device for seniors. If the battery does not last, it sits on the dresser instead of on the person, and then it cannot call for help when they fall.

**3 · Complication**
> The shortcuts are very tempting. A vendor's feature list says significant-motion detection, a machine-learning core on the sensor, dead reckoning — and it is easy to treat that as a keyword match instead of evidence. Then you take the headline current from a datasheet, add it to numbers that describe a different mode, and you have a budget that looks precise and isn't.
⟨breathe⟩

**4 · Move**
> So we bought the discovery hardware and watched each feature actually do what it claimed, before anything was designed around it. Significant motion had to wake things up on a real bench. The machine-learning core had to classify real movement.
> Then the numbers. I found the right rows in the datasheets for the modes we would really run, and added them the way the industry does — each state's current times the fraction of time spent in it — and then checked the estimate with a supply that measures current.
*(optional)* In medicine there is the idea of a standard of care — the method any competent practitioner would use. A battery budget should be like that. Nobody wants a revolutionary battery estimate.
> Only then did we set the goal in the same units: positioning should be a non-issue in the power budget. The device sleeps by default, the motion sensor decides the user is moving, a small microcontroller keeps a relative position, and the big processor wakes only when it has to.

**5 · Punchline**
> So when we said positioning would be a non-issue in the budget, every number underneath that sentence had been seen on a bench and added the way anyone in the industry would add it.
⟨breathe⟩

**6 · Handover**
> I'm curious how you check a power number before you believe it.

## If they follow up

- **"Isn't that just the textbook method?"** → Yes, on purpose. The method should be the industry's standard of care, not something that raises eyebrows. Where I think for myself is in what goes into it and whether I believe it. It is a bit like Russ White on the OSI model — you should know the standard well enough to say plainly where it is wrong, and use it everywhere it is right.
- **"How would you do that experiment today?"** → With an AI coding agent, the experiment costs calendar time, not project time. A set of scripts configures any number of devices, the test procedure is something I enjoy running, and the notebook analysis that would have been a data scientist's week is on my machine the same day. It is a very good fit for that kind of code: straightforward, no cleverness allowed, and anything irrelevant is easy to spot in review.
- **"Did the microcontroller path ship?"** → Not as designed. Partway through I recorded that other reasons to run the application processor might mean the microcontroller never actually reduced the budget, and that prototyping should be cut short rather than continued for its own sake. That is a negative result I reached and acted on. The measured, standard-method budget and the positioning goal outlived the hardware plan.
- **"Where does concurrency come into a power story?"** → Everywhere, because the wake-up chain is a concurrency design across two processors. The protocol between them is where power bugs are born — I corrected the co-processor API specification over whether a call takes or releases a wakelock, because a manufacturer implements that literally.
- **"What did you argue *down* on battery grounds?"** → A cellular hotspot capability. It would have killed the budget. That is a refusal, not a delivery, but it is the same skill.
- **"Anything that got no traction?"** → I proposed a second positioning timeout so we could measure accuracy against battery instead of arguing about it. It landed on deaf ears at the time. I still think it was the cheap version of a question we kept re-litigating.

## Proof

Component-level reasoning anyone in embedded can check: motion classification on the sensor's own ML core, a BLE microcontroller between the sensors and the application processor, barometer for stairs and fall discrimination, magnetometer for heading, temperature as the outdoors signal. The evaluation was run as a purchase list where each item settled one named experiment, including a programmable supply with current measurement. The averaging method is the ordinary one: battery life is a function of average current, dominated by duty cycle, and trusted only once measured ([Embedded.com](https://www.embedded.com/low-power-embedded-design-are-you-optimizing-the-wrong-thing/)).

## Know it — what stays with me

T1: the part numbers (LSM6DSOX, STM32WB family, LPS22HH, LIS2MDL), the STMicroelectronics discovery kits and field engineers, the internal trade-off cards, the market reasoning beside the power argument, and the schedule that timeboxed it. Component vendors are not named outward. The AI-era experiment is the 2026 keep-alive soak.

## Sources

- [2021-11-15 R5 product architecture and power-budget trade-offs](../../../raw/brag/2021-11-15-r5-product-architecture-power-budget-tradeoffs.md) — including the owner's 2026-09-24 correction of emphasis
- [2021-11-22 Dead reckoning and sensor-cluster architecture](../../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md)
- [2021-10-16 Battery and power as a second specialization](../../../raw/brag/2021-10-16-battery-power-second-specialization.md)
- Cited, not graduated: [2026-07-28 AI-assisted device experiments](../../../raw/brag/2026-07-28-ai-assisted-device-experiments.md)

## Related stories

- [I argued to buy our positioning per device](buying-calendar-time.md) — the positioning decision on the same device.
- [Every classic pitfall around beacon tracking was survivable alone; together they multiplied](home-away-kept-simple.md) — a later beacon feature on the same device line, assigned in 2023; not an outgrowth of this research.
- [The fault that lost the fix](the-fault-that-lost-the-fix.md) — the same subsystem, seen from the field.
