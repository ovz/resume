---
cluster: positioning
fits: [embedded, architecture, principal, product, vendor]
status: draft
runtime: "2 min"
---

# I argued to buy our positioning per device instead of building it, because calendar time is the one resource you cannot buy back

## Why I still care

Building our own location fusion would have been the fun option, and I am exactly the engineer who would have enjoyed it. Arguing against my own favourite project, because I could see who would pay for the delay, is the decision I am proudest of in the positioning work. And the people who wrote the library I argued for now know me by name.

**Cue:** my notes on the vendor's SDK preview in September 2022 — *"we are getting a Location Fix out of the box. No need to fuse positioning inputs from different sources."*

## Register

**2020-2026, Best Buy Health** — ownership and economy; willing to say "I argued" and equally willing to say what was not measured. Vendors are not named. Lines lifted from the owner's dictation of 2026-09-14 and 2026-09-24 per [spoken drafts](../../workflows/spoken-drafts.md).

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | One about the most interesting thing I argued for, which was not to build something |
| 1 | Hook | We could have built our own location fusion; I argued to license it per device |
| 2 | Stakes | Commercial customers: one assisted-living operator is hundreds of lines, and a resident nobody can find is a reputation problem that spreads |
| 3 | Complication | Building it was possible, interesting and fun — and it costs calendar time |
| 4 | Move | Evaluated the SDK against the previous generation as the baseline; argued for the per-device licence; built a direct relationship with its engineers |
| 5 | Punchline | The device positions well, and I talk to the people who wrote the library directly |
| 6 | Handover | Where do you draw the build-or-buy line? |

## Narrative — rehearse verbatim

**0 · Offer**
> There's one from the positioning work about the most interesting thing I argued for, which was not to build something.

**1 · Hook**
> For the new wearable we could have built our own location fusion — dead reckoning, sensors, Wi-Fi, all of it. I argued that we should license a commercial positioning service instead, per device.
⟨breathe⟩

**2 · Stakes**
> The reason is our commercial customers. One assisted-living operator is easily hundreds of lines of service. The last thing we want is staff there having trouble locating a resident who is wearing our device. And everyone in that industry talks to everyone, so that is a reputation problem you cannot fix quickly.

**3 · Complication**
> Building it ourselves was possible. It had real innovation potential, and honestly it is fun for engineers like me. But it takes resources, and one of those resources is calendar time. There is no way around that one.
⟨breathe⟩

**4 · Move**
> So I evaluated what we would be buying against what we already had. The vendor's preview described what the previous device was already getting, in a new form, so I could use the old device as the baseline and expect the same quality or better. We would be getting a location fix out of the box, with no need to fuse the inputs ourselves.
> I strongly supported the per-device licence on that basis.
*(optional)* Then I built a direct working relationship with the library's engineers. Chip-vendor questions normally go through the manufacturer, and every hop costs weeks. These people know me, and we work well together.

**5 · Punchline**
> The device we ship today positions well. And when something goes wrong in that library, I can talk to the people who wrote it.
⟨breathe⟩

**6 · Handover**
> I'm curious where you draw that line — what do you build, and what do you buy?

## If they follow up

- **"Weren't you worried about shipping a version 1.0?"** → Consumers will tolerate some variability; a version-one blunder might raise churn a little, but it is rarely the single thing that kills a product. Commercial customers are different — they do not appreciate version-one technology. The way I put it to myself is that no product means no churn. Getting something good into the field is progress; waiting for the perfect home-made version is not.
- **"Was battery part of it?"** → Among other things, yes. My read is that the new path is much kinder to the battery than the previous generation's positioning, but I don't have a controlled comparison I could quote, so I don't. We did not buy it for battery.
- **"How did you become the positioning person?"** → On the previous device, location quality started to degrade and nobody knew why. Cellular and satellite positioning were new to me, so I built myself a curriculum and worked it out engineer to engineer with the manufacturer's team — it took about half a year of experiments, and the chip vendor later confirmed what I had suspected early. After that I was introduced to them as the company's positioning expert.
- **"Did the bought library ever let you down?"** → Yes, and that is two more stories: a recovery gap where the fallback never restored it, and two file-descriptor leaks — one they fixed fast, one that takes five days to show and that I narrowed down to our own side. Buying is not the same as not owning.

## Proof

The September 2022 evaluation notes are in the committed device-board snapshot; the later incidents with the same library are their own entries. The chip vendor's acquisition of the positioning vendor in May 2022 is public.

## Know it — what stays with me

T1: the library is **Skyhook**'s, now part of **Qualcomm**; the previous generation used Qualcomm's **IZat** positioning on the modem; the manufacturers were **Borqs** (the earlier device's team in India) and later **TCL**, through whom chip-vendor questions route. The battery comparison is my statement only. Who approved the licence, and when exactly, is not in the record.

## Sources

- [2022-09-16 Buying positioning and calendar time](../../../raw/brag/2022-09-16-skyhook-license-buy-calendar-time.md)
- [2020-01-01 R4 location fix, engineer to engineer](../../../raw/brag/2020-01-01-r4-location-fix-engineer-to-engineer-borqs.md)

## Related stories

- [The fault that lost the fix](the-fault-that-lost-the-fix.md) and [The positioning library leaked twice](../concurrency/the-guard-that-counted-descriptors.md) — living with the library we bought.
- [Every number in the power budget was observed on the bench](power-budget-non-issue.md) — the power side of the same device.
