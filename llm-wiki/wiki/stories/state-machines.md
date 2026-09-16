---
cluster: state-machines
aliases:
  - "State machine stories"
  - "Boost MSM stories"
  - "Keep-alive and MCU Fatal UI stories"
---

# State machines, and the codebase whose authors are gone — story cluster

> **Doc type:** reference
>
> Hub for the state-machines cluster: the through-line, the grounding rules, the stories planned, and what each will draw on. Open this note's local graph to see the cluster as a sub-graph. Audience: the owner preparing to talk about legacy code, technical debt and saying no to ad hoc complexity; agents writing these stories.

## The through-line

The device's core runs on **Boost MSM** state machines — a top-level machine composed of submachines and orthogonal regions, with System Lifecycle as the critical one. The design came with the previous device generation, before the owner joined GreatCall in 2018; the colleagues and contractors who built it are long gone, and today he is the best and only fully qualified engineer on that codebase. The story of these years is the opposite of the positioning cluster: not things done right, but a well-built state-machine core that kept receiving new behaviour as **conditions instead of states** — and an engineer arguing, often without winning, that the architecture should absorb the change rather than be routed around.

## Grounding rules for this cluster

- **Ground Boost MSM claims in the Boost.MSM documentation for the Boost version the Lively devices build against** — a 1.6x release from 2018 or earlier, by the owner's recollection, to be confirmed. The library changed little, but documentation examples, front-end options and back-end features differ between releases; current documentation must never be quoted as if it described that codebase.
- **Codebase evidence augments, never restructures.** When the device code is inspected, what it corroborates or refutes is added to the entries and stories as evidence. It does not reorganize a story that the board and the owner's account already ground; and the code itself stays at T2 — [sensitivity tiers](../workflows/sensitivity-tiers.md).
- **Humility, respect and trust** govern every mention of a colleague — [voice and prominence](../workflows/voice-and-prominence.md) § *Humility, respect and trust*. A mandate the owner argued against is told with the reasoning on the other side first.

## Stories

| # | Working title | The claim | Draws on | Status |
|---|---|---|---|---|
| S1 | The keep-alive build was the Rubicon | A keep-alive production build sounds easy, but it had to interact with System Lifecycle and switch off regular location; handled as conditions rather than states, it turned into a sprawl of ad hoc logic, and the owner's answer is a location state machine as the next stage rather than one more increment | Device board: the 2025 System Lifecycle state-machine audit, the 2026 keep-alive engineering and production builds, the 2026 location state-machine ask; [2026-09-01 beacon tracking and FOTA persistence](../../raw/brag/2026-09-01-r5-beacon-tracking-fota-persistence.md); [2021-10-16 battery and power](../../raw/brag/2021-10-16-battery-power-second-specialization.md) | **needs entries** |
| S2 | MCU Fatal UI, bolted on | A mode meaning the microcontroller no longer works and the wearer should call the care centre for a replacement; against his recommendation it was slapped on as sprawling conditional logic instead of being integrated into the core and platform processes on the application processor, and it generates spurious side effects — including disabling beacon tracking | Device board: 2023 Fatal UI app tickets, the 2025 pseudo-Fatal UI work, 2026 findings; brag inbox note of 2026-09-14 | **needs entries** |
| S3 | Steward of a state-machine codebase whose authors are gone | The only engineer fully qualified on the core's state machines, after its designers left and the MCU principal engineer was laid off; raising the bar for a bright junior firmware engineer and for a manager who used to be his peer, without relying on either to move his own career | Device board: the 2024 state-machine libraries research for the capability framework, a 2023 Boost MSM trace from the battery state machine; [professional contacts](../entities/professional-contacts.md); brag inbox note of 2026-09-14 | **needs entries** |

## Related, not conflated

- [Consolidated Boost proficiency](../../raw/brag/2026-09-14-boost-library-proficiency.md) preserves the MSM composition, transition-diagnosis and stewardship evidence alongside Asio and Test. It is a capability entry, not a completed S1-S3 story; the remaining inbox narrative is still pending.
- **[Positioning](positioning.md)** is the success story of the same device and years. Keep the two apart: a positioning story should not carry the state-machine complaints, and a state-machine story should not borrow positioning's wins.
- **P4**, [the beacon tracking story](positioning/home-away-kept-simple.md), currently carries the state-machine half in its pitfall table — the add-ons, the keep-alive breakage, the location state machine. When S1 is written, that half moves here and P4 keeps the beacon design.

## Before writing

The owner's account is in the brag inbox (2026-09-14). Ingest it into dated entries first, grounded in the committed board snapshots, so the stories rest on the record rather than on the message.
