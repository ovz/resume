---
cluster: positioning
fits: [architecture, embedded, firmware, principal, product]
status: draft
runtime: "2 min"
---

# Three ways to know where someone is, and one place that decides which to believe

## Why I still care

I had wanted this architecture since 2021 and got to build it in 2025. The satisfying part is not the interfaces — it is that the last piece of it was a bug report about firmware updates, and fixing that properly turned out to be the same problem as the architecture. Nothing about this was glamorous. It is the work I would point at if someone asked what I actually do.

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | There is one about consolidation that ends somewhere I did not expect |
| 1 | Hook | Three ways to know where someone is, and three different pieces of code deciding which one to believe |
| 2 | Stakes | In-home presence detection is what the safety features are built on |
| 3 | Complication | Each source evolves on its own schedule, and every firmware update wiped the device's memory of which beacons were the user's |
| 4 | Move | One interface per provider, one layer that arbitrates and falls back — then made the beacon pairing survive the update by restoring it before the location subsystem starts |
| 5 | Punchline | An update now costs the user nothing: the device wakes up already knowing whose home it is in, and never leaves the low-power mode |
| 6 | Handover | Where does your system decide which of two disagreeing sources to trust? |

## Narrative — rehearse verbatim

**0 · Offer**
> There is one about consolidation that ends somewhere I did not expect it to.

**1 · Hook**
> The device had three ways to know where someone was — beacons, satellites, and Wi-Fi — and three different pieces of code deciding which one to believe.
⟨breathe⟩

**2 · Stakes**
> In-home presence detection is what the safety features sit on. Whether the device thinks you are home is not a detail; it changes what it does when something goes wrong.

**3 · Complication**
> Each source evolves on its own schedule. A vendor library updates, a radio behaves differently, a new technique shows up. With the logic scattered, every one of those is a change in four places and a new way to be inconsistent.
*(optional)* And you inherit that fragmentation. Nobody sat down and designed it. It is what three features added in three years looks like.
> Then there was the one that actually bothered me. Every firmware update, the device forgot which beacons were the user's. Pairing gone. So it dropped out of low-power presence detection and back into high-frequency polling — worse location, worse battery, and someone has to re-pair.
⟨breathe⟩

**4 · Move**
> So: one interface per provider. Beacon, satellite, Wi-Fi, each behind the same shape. Above them, one layer that holds state, arbitrates between sources, and knows what to do when one of them goes away. Standard data format, standard update mechanism, fallback in one place instead of three.
*(optional)* The test of that design is not the code. It is that adding the next technique — Wi-Fi round-trip timing, whatever BLE does next — is an addition and not a renovation.
> And then the update problem turned out to be the same problem. Paired beacon state is state, so it belongs in that layer, and it has to cross the firmware boundary. We serialize it to a handoff file with a schema, and restore it **before** the location subsystem comes up. Not after. Before — so the engine never has a moment where it thinks it has no beacons.
*(optional)* I also went after the silent failures around it. Error categorization that says what actually went wrong, and deliberate handling of microcontroller reboots rather than whatever happened to occur.

**5 · Punchline**
> So an update costs the user nothing now. The device comes back up already knowing whose home it is in, and it never leaves the low-power mode to find out.
⟨breathe⟩

**6 · Handover**
> That arbitration layer is the part I would ask about in someone else's system. Where do you decide which of two disagreeing sources to trust?

## If they follow up

- **"What made you confident the interfaces were right?"** → The beacon work came after the engine and landed as a provider change, not an engine change. That is the only real test an interface gets.
- **"Do you have the numbers?"** → Not yet, honestly. Support-ticket reduction and measured battery life are post-release data. What I can say without hand-waving is the mechanism: staying in presence detection instead of polling is the difference, and that is the mode the device now keeps through an update.
- **"Why does restore order matter that much?"** → Because a subsystem that starts empty and gets corrected is a subsystem that emitted a wrong answer first. On presence detection, a wrong answer is a false "away".
- **"Was the fragmentation anyone's fault?"** → No. It is what three features added over three years looks like. Consolidation is maintenance that finally got argued for, and getting that argued for is most of the job.

## Proof

An internal design document with diagrams, interface definitions and usage examples; the provider interfaces visible in the repositories; a merged pull request implementing the persistence and restoration, and a second for the corner cases and reboot handling. Operational metrics are pending post-deployment data, and I say so.

## Know it — what stays with me

T1: the repository, the handoff file's schema and name, the Jira stories, the specific corner cases and which of them came from field investigations. Internal defect detail on a current employer's product stays in.

## Sources

- [2025-11-15 R5 location engine design](../../../raw/brag/2025-11-15-r5-location-engine-design.md)
- [2026-09-01 R5 beacon tracking and FOTA persistence](../../../raw/brag/2026-09-01-r5-beacon-tracking-fota-persistence.md)

## Related stories

- [We decided the battery before we decided what the device looked like](power-budget-non-issue.md) — the constraint this engine was eventually built to satisfy.
- [The fault that lost the fix](the-fault-that-lost-the-fix.md) — the field evidence that made the case for consolidating.
