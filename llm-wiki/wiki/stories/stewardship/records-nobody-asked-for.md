---
cluster: stewardship
fits: [leadership, principal, architecture, product]
status: draft
runtime: "2 min"
---

# I kept records nobody asked me for, and years later they moved a company

## Why I still care

Seventeen years of a product line, and the part I am proudest of is the boring part: I wrote things down. Not because anyone asked — nobody audits an engineer's notes — but because I never liked the feeling that a decision existed only in somebody's memory. Then the company was acquired, and the notes stopped being my habit and became the company's ability to move. What I felt at the time was mostly relief: an acquisition is where knowledge goes to die, and this one did not have to.

## Register

**2017-2018, Minitab.** Custody and dry judgement — short, factual, slightly wry. It is a story about responsibility, not achievement, and the trap is turning a two-year tenure into either a triumph or a grievance. It was neither. See [voice and prominence](../../workflows/voice-and-prominence.md) § *The registers, era by era*.

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | There is one from an acquisition I still think about |
| 1 | Hook | Seventeen years of a company's intellectual property had to move, and what made it possible was a filing habit |
| 2 | Stakes | Knowledge is what an acquirer is actually buying, and it is the first thing that evaporates |
| 3 | Complication | Some projects had to be stopped, not finished — and stopping a project badly destroys it |
| 4 | Move | Transferred the IP under governance, froze the stopped work so it could be restarted, and cut onboarding from months to a week |
| 5 | Punchline | The migration took under a year, and every frozen project could still be picked up |
| 6 | Handover | Ask me what I mean by freezing a project properly |

## Narrative — rehearse verbatim

**0 · Offer**
> I have one from an acquisition that taught me what I actually value.

**1 · Hook**
> Seventeen years of one company's intellectual property had to be handed to another company. What made that possible was not heroics. It was that I had kept detailed records for years, because I did not trust anything important to live only in somebody's head.
⟨breathe⟩

**2 · Stakes**
> When one company buys another, what it is really buying is knowledge — the product, why it works, what was tried and abandoned. That is also the first thing to evaporate, because people leave and nobody writes down what everyone already knows.

**3 · Complication**
> And it was not just a transfer. Leadership decided some projects would not continue. Stopping a project is easy; stopping one so it can be restarted is not. A project that is abandoned rather than frozen is gone, even if all the code is still there.
⟨breathe⟩

**4 · Move**
> So I treated the whole thing as custody. Everything went across under proper governance — the codebase, the issue tracking, the build and release pipeline, onto the acquirer's platform, while I kept the old pipeline alive for the team that had no capacity to move it yet.
> The frozen projects I documented to the standard of "somebody who was not here could pick this up": where it stood, what it depended on, what the next step was, and what we already knew did not work.
*(optional)* And I built the scale-up process that came with the merger, which cut onboarding from two or three months to under a week — because the fastest way to stop being the person everyone has to ask is to write down the thing they keep asking.

**5 · Punchline**
> The migration was done in under a year, and every one of those stopped projects could still be resurrected. I was told the pace was possible because of the records.
⟨breathe⟩

**6 · Handover**
> Ask me what I mean by freezing a project properly — it is the part most people get wrong.

## If they follow up

- **"What does freezing a project properly mean?"** → Write the state down as if the reader is a stranger, because they will be: the decision history, not just the code; the dependency versions; the one experiment that failed and why. The test is whether someone who never met you can restart it. Most "paused" projects fail that test on day one.
- **"What does a freeze done wrong look like?"** → I have seen one since. At my current company an outside consultancy built a process supervisor for the device — fully unit-tested, good engineers. Because the device was delayed, it was put on hold. When it was time to bring it back, the unit tests did not run. It went to production anyway, and it still has no working test harness, because nobody has had the time to work out how to run them. If I had been running that freeze, the one thing I would have insisted on is that on the day you stop, somebody who is not the author builds it and runs the tests, and writes down how. The same consultancy's messaging framework has a beautiful design and depends on a niche code generator for its interfaces — nobody can build it today.
- **"Isn't that just documentation?"** → It is documentation with an owner. The difference is that I kept it when nobody was asking for it and there was no deadline attached, which is the only time it actually gets written.
- **"Where else does this show up?"** → It is the thread through my career. The security version: I wrote a NIST-grounded patch-management SOP for a fleet of devices after tracing firmware staleness to a partner who patched on release, which is not the same thing as patching deliberately. The data version: I hold the formal Data Steward role on our enterprise data catalog for device data — governance is just risk management applied to data, who owns it and what it means and whether it earns what it costs to keep. The code version: I am the one fully qualified on a state-machine architecture whose authors have all left.
- **"How does that square with eliminating toil? Records sound like toil."** → Opposite ends of the same idea. A steward is judged by the condition of what is handed on, and hand work is where drift and single points of knowledge live — so I automate it away. On-device test automation that cut testing time by orders of magnitude, and then I onboarded the QA engineers onto it so the gain outlived my attention. That last part is the stewardship half; building it was the easy half.
- **"Was the acquisition good for you?"** → It was short and it was formative. I learned to read an environment instead of assuming one — the bar rose in some places and not others, and knowing which is which is what I took into the next role.
- **"You keep saying 'under governance'. What did that involve?"** → Ownership and licensing of every asset established, records of what was ours and what was third-party, and no silent gaps. It is dull, and it is exactly what nobody wants to reconstruct two years later in a legal conversation.

## Proof

Public, on the resume: the intellectual-property transfer under governance, the migration of codebase, issue tracking and CI/CD completed in under a year while the legacy pipeline was maintained, the comprehensive review of in-progress projects and the freeze carried out so they remain resurrectable, and onboarding cut from two or three months to under a week.

The claim that the records are *why* the pace was possible is the owner's own account, stated on the resume. No acquirer-side confirmation is in the record, and the separation correspondence in the archive is personal and legal material that is never cited as endorsement.

## Know it — what stays with me

T1: the acquirer is Minitab and the acquired company Salford Systems, both public on the resume; the frictions of the post-acquisition environment, the separation correspondence, and the recommendation letter Minitab declined to sign are recorded in the archive and are **never** told outward or used as endorsement. The Data Steward register names Alation internally; outward it is "our enterprise data catalog". The inherited state-machine codebase is owner-reported.

**The counterexample, T1:** the process supervisor is the R5 "system-monitor", built by Ciere Consulting (Michael Caisse); the messaging framework is XPMF, which depends on the Genie tool; the contractor relationship was managed by Christopher VanKirk, who took the contractors' word that it was done. My note of January 2023 names it as "the blast from the past". Told without names, and never as a verdict on the colleague — the lesson is what a freeze needs.

## Sources

- [2026-09-16 Stewardship as a first principle](../../../raw/brag/2026-09-16-stewardship-first-principle.md)
- [Primary resume](../../../../markdown/Oleg.Zhylin.resume.achievements.md) § *Minitab* and § *2017-2018 Acquisition of Salford Systems by Minitab*
- [2023-01-30 process-supervisor freeze counterexample](../../../raw/brag/2023-01-30-system-monitor-freeze-counterexample.md) — the freeze done wrong, in the follow-ups
- [2025-01-01 Data Steward](../../../raw/brag/2025-01-01-data-steward-enterprise-data-catalog.md) · [2023-09-30 patch management SOP](../../../raw/brag/2023-09-30-security-patch-management-sop-and-vendor-engagement.md) — the follow-up registers

## Related stories

- [A mathematical paper, encoded in Fortran](../salford/a-paper-encoded-in-fortran.md) — the same era, the other half of what long tenure buys.
