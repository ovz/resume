---
title: "Argued to license a commercial positioning service per device rather than build our own, because reliable location is what commercial customers buy and calendar time cannot be bought back"
date: "2022-09 to 2026 (decision 2022; direct vendor relationship ongoing)"
thread: POS
domains:
  - "Positioning and location"
  - "Battery, power and cost of operation"
  - "Architecture and API design"
context: "Best Buy Health — Lively Mobile 2 (R5) positioning; commercial (assisted-living) and consumer customers; the positioning vendor, later part of the chip vendor"
sensitivity: private-repo
resume-worthy: yes
storied:
  - "positioning/buying-calendar-time"
---

# Argued to license a commercial positioning service per device rather than build our own, because reliable location is what commercial customers buy and calendar time cannot be bought back

## What I did — the owner's account, verbatim

**2026-09-14** (filed as a brag-inbox note the same day):

> Make them related but not conflated story lines. Positioning is mostly a success, things done right, I fixed locations by working with Borqs India in proper engineer to engineer collaboration. Current r5 device does positioning well. Leveraging skyhook was a brilliant idea. I strongly supported to by skyhook per device license because reliable positioning is vital for commercial cutomers of lively mobile. We did our home grown dead reconing etc and such home growth is possible and nice innovation potential, and fun for engineers like me, but they take resources, critically, there is no way around calendar time being one of the resources. For commercial customers who are life line for profitabiity as every assisted living is easily hundreds of lines of services last thing we want people having trouble locating a customer wearing a device. And since everyone talks to everyone that's a reputation risk that cannot be dealt with without, again, calendar time. I also researched skyhook / qualcomm all products promoted observabiity  that could augment or even replace Data Dog and with help from AI quickly identified the state and the potential and communicated properly inside Best Buy and with Skyhook. Skyhook is part of Qualcomm and we are fortunate we can talk to them directly. The standing rule all communication with Qualcomm as chip vendor goes through ODM (TCL) and that's again calendar time and all the obviuous other downside including sub-optimal engineering collaboration. In contrast, skyhook people know me and we work together well.

**2026-09-24:**

> Another related fact is that SKyhook was decided for positioning. Among other things r5 skyhook powered location fix is much more effective on battery as compared to iZat qualcomm (lookup exact names) previous generation positioning. Qualcomm did a good call purchasing skyhook. We didn't get skyhook just for battery. As I tell in another story, commercial customers e.g. assisted living don't appreciate 1.0 technology. Consumers might tolerate some variability and 1.0 kinds of blunder might drive the churn up somewhat, but rarely be single signficant factor that hikes the churn and kills the product. one of those cases when "no product" means no churn, otherwise getting something in the field is progress, perfectionism is stagnation and failure.

The R4 location fix with the manufacturer's engineers in India is its own entry, [2020-01-01](2020-01-01-r4-location-fix-engineer-to-engineer-borqs.md).

## What the record shows

- **September 2022 — the evaluation.** The owner's notes on the chip vendor's *terrestrial positioning* SDK preview: it "pretty much describes what we are getting on R4, but it is Skyhook's solution now", which "opens an avenue to utilize R4 device alongside R5 hardware and confirm R5 performs similarly or better"; since hybridisation and fusion are provided, "we are getting a Location Fix out of the box. No need to fuse positioning inputs from different sources." Draft conclusion: "we have a reason to expect same or better quality as R4." In the same weeks he worked out the licence string and the library's logging.
- **The names.** The previous generation positioned with Qualcomm's **IZat** location platform on the modem (GNSS with its XTRA assistance data, plus Wi-Fi and cell). The current device uses **Skyhook**'s precision-location library (Wi-Fi, cell and GNSS hybrid). Qualcomm completed its acquisition of Skyhook in May 2022 ([Location Business News, 2022-05-18](https://locationbusinessnews.com/qualcomm-completes-skyhook-acquisition)).
- **The relationship.** The library's engineers became direct contacts — the 2024 descriptor-leak reproduction ([2024-04-03](2024-04-03-skyhook-file-descriptor-leak-reproduction.md)), the 2025 device-identity work ([2025-05-01](2025-05-01-qualcomm-skyhook-device-identity.md)) and the 2026 observability evaluation ([2026-01-01](2026-01-01-qualcomm-device-observability-evaluation.md)) — while chip-vendor questions otherwise route through the manufacturer.

## Why it matters

The buy-versus-build call is the product judgement: home-grown dead reckoning and fusion were possible and interesting, and they would have cost the one resource nobody can buy back. **Commercial customers set the bar** — one assisted-living operator is hundreds of lines of service, and a facility that cannot find a resident is a reputation problem that spreads, because "everyone talks to everyone". Consumers tolerate some version-1.0 roughness; a commercial buyer does not. **And the counterweight, in his words: "no product" means no churn** — shipping a good bought solution beats perfecting a home-made one.

## Skills demonstrated

Buy-versus-build analysis; product and customer-segment reasoning; vendor evaluation against the previous generation as a baseline; direct engineering relationships with a platform vendor; positioning and power as one subject.

## What was blocked, cut short, or wrong

- **The battery comparison is not measured in the record.** "Much more effective on battery" than the previous generation's positioning is the owner's statement; no soak results comparing the two are retained. It must not be stated outward as a figure.
- **The home-grown path was not taken** — dead reckoning stayed research ([2021-11-22](2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md)). That is the decision, not a loss.
- **The licence decision itself** — who approved it, and when exactly — is not in the record read; the September 2022 evaluation is the dated evidence.

## Evidence

The owner's statements above (the 2026-09-14 inbox note, and the TODO note of 2026-09-24). Device-programme board (committed Trello snapshot): the terrestrial-positioning SDK card of 2022-09-16 and the licence-string card of 2022-09-29. Acquisition date from the linked article, fetched 2026-09-24.

## Evidence limitations

Outward, the vendor is not named ("a commercial positioning service"), and the customer-segment reasoning is told as reasoning, not as company data. The churn reasoning is the owner's professional judgement.

## Related

- [2020-01-01 R4 location fix with the manufacturer's engineers](2020-01-01-r4-location-fix-engineer-to-engineer-borqs.md) — what made him the positioning expert first.
- [2021-10-16 battery and power as a second specialization](2021-10-16-battery-power-second-specialization.md) — positioning and power as one subject.
- [2024-05-15 positioning root cause](2024-05-15-skyhook-positioning-root-cause-diagnostics.md) and [2024-04-03 descriptor leak](2024-04-03-skyhook-file-descriptor-leak-reproduction.md) — living with the bought library.
- [2025-11-15 location engine design](2025-11-15-r5-location-engine-design.md) — the architecture it sits in.

## Record history

- 2026-09-24: created, ingested from inbox note "2026-09-14 positioning - Borqs, Skyhook, calendar time" (deleted from the inbox; its text is preserved verbatim above), with the owner's TODO note of 2026-09-24 and the committed Trello snapshot.
- 2026-09-24: graduated into story `positioning/buying-calendar-time`; `storied` property added, body untouched.
