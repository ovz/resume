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

**The owner's argument, in his words (2026-09-16).** The earlier version of this entry leaned on "monolith versus modular" and read as abstract; the owner restated the pitfall concretely:

> "The pitfall of hybrid is that ground up goes at hardware lifecycle pace and any flaws in engineer-to-engineer collaboration and too much contract negotiation increases the pain, compromises deadlines etc. Breadth first done right, vendor compromises deadline, order goes to another vendor. We might have to do a round of demos to e.g. a Hospital Corporation or Assisted living, but logically and from experience clients are usually on board to give their customers what works rather than go through pains of missed deadlines and customer service rounds, device swaps etc. Hybrid is still too expensive to change vendors, and we cannot fix stuff in house. So our customer hospital and our vendor CGM both have a trend towards instability painful to everyone."

**The mechanism, plainly: each pure model has an exit; the hybrid has neither.**

| | Ground-up, in-house | Breadth-first white label | Hybrid |
|---|---|---|---|
| When something breaks | **Fix it in-house** — you own the code | **Switch vendors** — the order goes to the next one | Neither: too specialized to switch, not owned enough to fix |
| What sets the pace | Hardware lifecycle, six months or more | The catalogue — weeks per device | Hardware lifecycle, *plus* contract negotiation |
| What the customer sees when a vendor slips | A slipped release you control | At most a round of demos on the replacement device | Missed deadlines, customer-service rounds, device swaps |
| Where the pain lands | Inside the engineering team | On the vendor who lost the order | On everyone: the care provider *and* the vendor |

The two exits map exactly onto the two governance answers in the economics literature:

- **Transaction cost economics (Williamson).** When a relationship needs *relationship-specific* investment — a device customized for one integrator, firmware only one vendor can change — the market "collapses into a two-party negotiation" and each side is exposed to **hold-up**. Williamson's "discriminating alignment" answer is to match governance to the transaction: specific, complex work belongs **inside the firm** (ground-up); standardized, substitutable work belongs **in the market** (breadth-first). The hybrid is specific work governed by contract, which is the mismatch the theory predicts will be expensive. Tadelis & Williamson, *Transaction Cost Economics* — <https://faculty.haas.berkeley.edu/stadelis/tce_org_handbook_111410.pdf>
- **Switching costs and lock-in (Farrell & Klemperer).** Switching costs "hinder customers from changing suppliers in response to changes in efficiency" and hand the incumbent vendor ex post power. Breadth-first integration done right keeps switching costs low *on purpose*, which is what makes "order goes to another vendor" a credible threat and therefore disciplines the vendor's deadline. — <https://eml.berkeley.edu/~webfac/farrell/e220b_s04/switching.pdf>
- **Modularity (Baldwin & Clark; Christensen).** A modular boundary with published design rules is what lets independently built modules be substituted; an interdependent one means "the way one is designed and made depends on the way the other is designed and made", so both sides must be controlled. Christensen adds *when* each wins: integrated while the product is not yet good enough, modular once it is. The hybrid is an interdependent design split across a company boundary. — <https://hbr.org/1997/09/managing-in-an-age-of-modularity> · <https://www.christenseninstitute.org/theory/modularity/>
- **Porter's generic strategies.** Holding two incompatible positions at once is being *stuck in the middle*. — <https://en.wikipedia.org/wiki/Porter's_generic_strategies>
- **Why this bites harder in medical devices.** Multi-sourcing in medical electronics is treated as a continuity-of-care requirement, not only a cost lever, and qualifying a replacement supplier under the quality system takes months — so a supplier that cannot be swapped quickly is a patient-facing risk. — <https://resources.altium.com/p/resilient-medical-electronics-multi-sourcing> · <https://ventureoutsource.com/contract-manufacturing/medical-device-dual-sourcing-tariff>

**The customer side is the owner's experience, and it is the non-obvious half.** A breadth-first swap is cheaper for the care provider than it looks: a hospital system or an assisted-living operator may want a round of demos on the replacement device, but it would rather give its patients a device that works than absorb missed deadlines, service rounds and device swaps. That is what makes the vendor exit usable in practice rather than only in theory.

**The judgement.** Not that one model is better. **Choose the governance deliberately, and design the vendor boundary to match it**: own what you must be able to fix, keep substitutable what you must be able to replace, and treat anything that is neither as a risk to be retired. The ground-up side is the owner's own discipline — see [hardware cadence and engineer-to-engineer practice](2026-09-11-hardware-cadence-engineer-to-engineer.md), whose Agile Manifesto value *customer collaboration over contract negotiation* is exactly what a hybrid forces into reverse.

**Why the owner stayed the observer on the SDK.** Safety-critical behaviour on a device whose firmware you do not own is a different risk problem, and he was not going to claim competence in a model he was watching rather than running.

## Why it matters

- **It is architectural judgement with public grounding**, which is what separates a principal-level opinion from a strong preference — and the grounding is the mechanism (hold-up, switching costs), not an analogy.
- **It guards a real conflation.** The record already claims mastery of the hardware/software lifecycle — the rigid-cadence, in-house model. Breadth-first white-label integration is a *different discipline*, and claiming both without distinguishing them would be the overclaim a knowledgeable interviewer would catch.
- **It names a live failure mode without disclosing it.** The outward version speaks of "a hybrid" and "the care provider and the vendor"; which platform, which customer and which device category stay at T1.

## Evidence

- The owner's direct statements of 2026-09-11 and 2026-09-16 (quoted above).
- Public grounding: Tadelis & Williamson (transaction cost economics, hold-up, discriminating alignment); Farrell & Klemperer (switching costs and lock-in); Baldwin & Clark, HBR 1997 (modularity); Christensen Institute (modularity theory); Porter (stuck in the middle); medical-electronics multi-sourcing — links inline above.
- Internal: the BLE SDK initiative's three-to-five-week integration goal, and the current customer and CGM-vendor relationship the owner describes — **T1**; the resume states the general principle, never the employer's target, customer or vendor.

## Evidence limitations

- **The instability claim rests on the owner's account**, not on an artifact in this repository: no incident record, delivery date or contract is cited. Outward, it is told as a pattern he has seen, never as a named customer's or vendor's failure.
- **"Clients are usually on board" is experience, not a survey.** It is stated as the owner's judgement.

## Related

- [2026-09-11 Hardware cadence and engineer-to-engineer practice](2026-09-11-hardware-cadence-engineer-to-engineer.md) — the in-house model this contrasts with.
- [2025-05-18 Fall detection and hospital-at-home integration](2025-05-18-fall-detection-hospital-at-home-integration.md)
- [2024-09-24 Current Health and Hospital at Home](2024-09-24-current-health-hospital-at-home-qms.md)
- [2025-07-18 FOTA vendor escalation](2025-07-18-fota-vendor-escalation-lively-mobile2.md) — the ground-up model's own version of vendor dependency, resolved by acquiring depth rather than by switching.

## Record history

- 2026-09-11: created from the owner's direct statement; the architecture claim grounded in Christensen's modularity theory and Porter's generic strategies so it reads as consensus rather than advocacy.
- 2026-09-16: rewritten around the owner's restated argument — each pure model has an exit (fix in-house, or switch vendors) and the hybrid has neither. Grounded in transaction cost economics (hold-up), switching-cost theory, Baldwin & Clark's modularity and medical-electronics multi-sourcing; Christensen and Porter kept as supporting rather than leading. Added *Evidence limitations*.
