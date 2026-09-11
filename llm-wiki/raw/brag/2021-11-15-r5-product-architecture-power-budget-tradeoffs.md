---
title: "Framed the next-generation wearable's architecture as an explicit battery-versus-hardware budget, and set the product direction from it"
date: "2021-11 to 2022-06"
thread: DEV
domains:
  - "architecture and API design"
  - "embedded and safety-critical devices"
context: "Best Buy Health, R5 senior-care wearable, product and system architecture"
sensitivity: private-repo
resume-worthy: yes
---

# Framed the next-generation wearable's architecture as an explicit battery-versus-hardware budget, and set the product direction from it

## What I did

Before the next-generation wearable had a form factor, a bill of materials or a schedule, I argued that the organization was about to make its architecture decisions in the wrong order, and set out the framing that put them in the right one.

**Made the budget the first-class constraint.** The central argument: decide the *battery* before the *form factor*, not the other way round. Battery capacity is something R&D can research and quantify; form factor is a creative constraint that industrial design can then work within. Getting this backwards means the enclosure dictates what the device can do, discovered late.

**Wrote out the trade-off structure explicitly**, so the coupling was visible rather than argued case by case:

- **Battery size vs. hardware quantity** — a larger battery powers more hardware, but a smaller battery leaves physical room for more hardware. Both directions are real, and they oppose.
- **Advanced hardware eats the battery budget twice** — once for the part itself, and again because software that makes good use of advanced hardware costs more power than software that ignores it.
- **Cost vs. capability** — a smaller battery is cheaper and leaves room for more hardware, but more hardware is more expensive. The naive cost saving reverses.
- Noted where technology choice escapes the trade-off: network-based positioning techniques are both power-efficient and computationally cheap on the device side.

**Set the positioning goal in budget terms.** The target I articulated was that location and positioning should be a *non-issue* in the power budget — the device spends some power to know where it is, but never enough that it becomes a major line item or that a mistake there can sink the battery. That goal is what the dead-reckoning and sensor-cluster architecture was designed to hit.

**Set the sleep-first system principle:** the device sleeps by default, and network, button and sensor events wake it only when needed. Everything else in the architecture follows from that.

**Explored the product's strategic shape**, keeping several framings alive rather than closing early:

- R5 as a **hub** versus R5 as a **self-contained device**, and what each implies for the battery.
- Modularity and reuse across the device line, with a smart cane called out as a plausibly separate product line rather than a variant.
- International coverage as a real opportunity — the user base travels, and 5G plus private Wi-Fi on cruise ships and similar venues opens coverage that had been assumed away. Noted that eSIM makes multi-carrier support feasible in a single device, extending providers almost anywhere, at the cost of an additional activation protocol.
- Named the competitive threats honestly, including phone-based fall detection paired with a cloud contact-centre service, and the AR/VR and MEMS-speaker ecosystem as a source of future competition needing only a base station with call capability.
- Identified the market insight that some customer segments will not count the money they spend, provided the product **keeps their lives easy** — and that loyalty follows ease, not features.

**Held the line on architectural coupling.** Recorded as a major architecture law that unwanted coupling to the recordable event bus must be prevented, and that *why* matters more than *how* when that kind of decision is being made.

**Named the schedule reality up front:** the device had to be operational by a fixed date, which severely timeboxed what could be afforded before build started. The trade-off framing existed precisely so that timebox would be spent on the decisions that mattered.

**Pushed on serialization as a strategic lever.** Proposed researching an automated way to convert positioning data structures to JSON at compile time — generating conversion code from C structures rather than hand-writing it — and looked at whether a ProtoBuf-family serializer could be capitalized on rather than building in-house, on the argument that an embedded platform may as well inherit the industry's work. Connected it to an internal embedded-development training exercise that had covered serialization, as a way to build on existing team knowledge.

## Why it matters

- **It changed the order of the decisions.** Deciding battery before form factor, and making the trade-offs explicit, is the difference between an architecture that is chosen and one that is inherited from an enclosure drawing.
- **It gave the positioning work a target** — "not a major item in the power budget" is a design constraint an engineer can actually build against, which is what the sensor-cluster architecture was built to satisfy.
- **It kept strategic options open on purpose**, with hub-versus-self-contained and international coverage still live, rather than being foreclosed by an early implementation decision.
- **It is architecture at the product level, not the module level** — market segment, competitive threat, cost, battery and coupling reasoned about together, which is the altitude the work was expected at.

## Skills demonstrated

System and product architecture; power budgeting as a design discipline; explicit trade-off analysis; technology strategy and competitive analysis; embedded platform decision-making; separating decidable constraints from creative ones; architectural coupling discipline; build-versus-adopt reasoning.

## Evidence

Trello device-programme board, *R5 Vision*, *R5 Trade Offs*, *R5 Strategic directions*, *R5 Power Budget* and *R4-style R5* lists, 2021-11 onward, plus the power-budget task and its reading notes. Internal wiki links, ticket identifiers and vendor application notes remain in the board archive.

## Related

- [2021-11-22 Dead reckoning and sensor-cluster architecture](2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) — the positioning architecture built to meet the power goal set here.
- [2025-11-15 R5 location engine design](2025-11-15-r5-location-engine-design.md) — the location architecture that eventually shipped.

## Record history

- 2026-09-10: created from the Trello device-programme board during the full board ingest.
