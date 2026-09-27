---
cluster: concurrency
fits: [vendor, principal, integration, debugging]
status: draft
runtime: "90 s"
---

# I pinned a whole team to the older compiler for a year and a half, because the new one broke our release builds

## Why I still care

The engine at the centre of that product was a mathematical paper turned into Fortran by one of the people who invented the method. I was the one who decided which compiler every developer on two continents was allowed to build it with. When the new compiler broke release builds six weeks after I had called it stable, it was my call to undo, and I did not enjoy saying "I was wrong, roll back" to the whole team. I am glad I said it fast.

**Cue:** my own email of 13 January 2014 — *"Given a number of issues we are having with Intel Fortran 14 we stick with Fortran 13 for the time being"* — with the exact menu path for every workstation, written out step by step.

## Register

**2000-2017, Salford Systems.** Craft and long horizons; the era's vocabulary — build server, release build, compiler version — not "developer platform". Lines lifted from the owner's mail and his statement of 2026-09-16 per [spoken drafts](../../workflows/spoken-drafts.md).

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | One about living with a vendor's compiler |
| 1 | Hook | The numerical heart of the product was Fortran, built with Intel's compiler |
| 2 | Stakes | Every model a customer built ran through that code |
| 3 | Complication | Certified the new version; six weeks later it broke release builds |
| 4 | Move | Rolled everyone back and pinned the version; escalated to Intel when first-line help stalled |
| 5 | Punchline | About a year and a half later we moved again — together, build server first |
| 6 | Handover | How do you decide when to take a new compiler? |

## Narrative — rehearse verbatim

**0 · Offer**
> There's one from the machine-learning years about living with somebody else's compiler.

**1 · Hook**
> The numerical heart of our product was Fortran — code that came from Jerome Friedman's own research — and we built it with Intel's Fortran compiler.
⟨breathe⟩

**2 · Stakes**
> Every model a customer built went through that code. If the compiler got something wrong, the product was wrong, and nobody would see it in the source.

**3 · Complication**
> At the end of 2013 I tested the new major version, said it was stable enough, and moved the build server to it. Six weeks later we had internal compiler errors in our release builds at full optimisation, a linker problem, and a crash in the decision-tree engine.
⟨breathe⟩

**4 · Move**
> So I rolled everybody back. Developers in the U.S. and in Ukraine, the exact older version, both 32- and 64-bit, and core libraries only from the build server configured that way.
> Then I worked it with Intel. Their support was responsive, and when the first person could not help, I reopened the case and asked for it to be escalated.

**5 · Punchline**
> We stayed on the older compiler for about a year and a half. When we moved again, we moved together, build server first, because everybody has to be running the same version of the compiler.
⟨breathe⟩

**6 · Handover**
> How does your team decide when to take a new compiler?

## If they follow up

- **"What did you learn from it?"** → Intel was responsive — the engagement was real. But the time to resolution cost the business. A responsive vendor and an acceptable time to resolution are two different things, and only the second one is on your critical path. I ask about the second one now, every time.
- **"Why not just lower the optimisation level?"** → *(agent-drafted — confirm)* You can, and on the Unix side a colleague building at a lower level did not see the errors. But then your release is no longer the product you tested, and you have traded a compiler bug for a performance regression in the one part customers pay for.
- **"Was it a miscompilation?"** → No — internal compiler errors in the optimised release build, a linker problem and a crash. I used to remember it as wrong code, but the mail is clear, and I go by the mail.
- **"How does this connect to what you do now?"** → The same shape shows up every time a vendor sits on the critical path — a chip vendor's library, a manufacturer's firmware. Certify on one machine, pin everyone, roll back fast, escalate when it stalls, and move together.

## Proof

The mailbox dates it: the certification of December 2013, the rollback email of January 2014, the Premier Support escalation of May 2014, the team's move to a later release in June 2015.

## Know it — what stays with me

T1: Intel Premier Support issues 696480 (a Fortran-debugger slowdown, 2013) and 6000037617 (escalated May 2014); I also wrote to Intel's Fortran support lead about the internal compiler error. **The fix version is not in the record**, and "a year of active collaboration" is my memory. The record also shows this came *after* the 2012 C++ compiler debate, not before it, which is not how I first remembered it — see the gatekeeper story.

## Sources

- [2013-12-01 Intel Fortran 14 rollback and Premier Support escalation](../../../raw/brag/2013-12-01-intel-fortran-14-rollback-premier-support-escalation.md)
- Cited, not graduated: [2026-09-16 concurrency and parallelism specialization](../../../raw/brag/2026-09-16-concurrency-parallelism-specialization.md)

## Related stories

- [They called me a gatekeeper, and I took it as a compliment](the-gatekeeper.md) — the argument for care, a year earlier.
- [A mathematical paper, encoded in Fortran](../salford/a-paper-encoded-in-fortran.md) — the engines this compiler built.
