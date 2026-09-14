---
title: "Breadth-first white-label device integration, watched from the ground-up side"
date: "2025 (observer role during the Current Health engagement)"
thread: MED
domains:
  - "embedded and safety-critical devices"
  - "architecture and API design"
context: "Current Health: the BLE SDK initiative"
sensitivity: private-repo
resume-worthy: yes
---

# Breadth-first white-label device integration, watched from the ground-up side

## What I did

The platform's **main initiative was a BLE SDK**: go **breadth-first** and be able to integrate any BLE-capable device in **three to five weeks**. The owner's role here was **observer**, deliberately — his expertise is devices designed in-house from the ground up, and he researched the SDK rather than owning it. Recording it matters because it put two opposite models side by side in one organization.

**The two models, plainly.**

| | Ground-up, in-house device | Breadth-first white label |
|---|---|---|
| What you control | The whole stack, including what the sensor does at 3 a.m. on a dying battery | The integration surface only |
| What you buy | Depth: behaviour you can guarantee | Reach: a catalogue in weeks |
| Cadence | Rigid, six months or more per hardware generation | Weeks per device |
| Fails at | Breadth — every new device is a programme | Depth — you inherit whatever the vendor's firmware does |

**Why they do not blend.** This is not the owner's opinion; it is the mainstream reading in both strategy and product architecture:

- **Christensen's modularity theory.** An *interdependent* architecture is one where "the way one is designed and made depends on the way the other is designed and made"; a *modular* one has interfaces that are "specifiable, verifiable, and predictable". Integrated architectures win while a product is **not yet good enough**, modular ones once it is **more than good enough** — and the same proprietary architecture that "in the not-good-enough circumstance was a strength, became a disadvantage in the more-than-good-enough circumstance". The choice is therefore a claim about where the product sits, not a matter of taste.
- **Porter's generic strategies.** A firm that tries to hold two incompatible positions at once is *stuck in the middle* and "fails in achieving any competitive advantage".

Put together: a hybrid that wants the guaranteed behaviour of an in-house device *and* the catalogue of a white-label integration tends to **inherit the costs of both** — the hardware cadence and the vendor dependency — while winning neither the depth nor the reach. **The judgement is about matching the architecture to the maturity of the product**, not about one model being better.

**Why the owner stayed the observer.** Safety-critical behaviour on a device whose firmware you do not own is a different risk problem, and he was not going to claim competence in a model he was watching rather than running.

## Why it matters

- **It is architectural judgement with public grounding**, which is what separates a principal-level opinion from a strong preference.
- **It guards a real conflation.** The record already claims mastery of the hardware/software lifecycle — the rigid-cadence, in-house model. Breadth-first white-label integration is a *different discipline*, and claiming both without distinguishing them would be the overclaim a knowledgeable interviewer would catch.

## Evidence

- Christensen Institute, *Modularity Theory* — <https://www.christenseninstitute.org/theory/modularity/>
- Porter's generic strategies, "stuck in the middle" — <https://en.wikipedia.org/wiki/Porter's_generic_strategies>
- Internal: the BLE SDK initiative's three-to-five-week integration goal — T1; the resume states the general principle, never the employer's target.

## Related

- [2026-09-11 Hardware cadence and engineer-to-engineer practice](2026-09-11-hardware-cadence-engineer-to-engineer.md) — the in-house model this contrasts with.
- [2025-05-18 Fall detection and hospital-at-home integration](2025-05-18-fall-detection-hospital-at-home-integration.md)
- [2024-09-24 Current Health and Hospital at Home](2024-09-24-current-health-hospital-at-home-qms.md)

## Record history

- 2026-09-11: created from the owner's direct statement; the architecture claim grounded in Christensen's modularity theory and Porter's generic strategies so it reads as consensus rather than advocacy.
