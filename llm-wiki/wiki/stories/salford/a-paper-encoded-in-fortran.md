---
cluster: salford
fits: [debugging, data, architecture, principal]
status: draft
runtime: "2 min"
---

# A mathematical paper, encoded in Fortran

## Why I still care

I was the GUI guy. The engines were where the actual science lived, written by and for people who thought in statistics, and I had no business in there — until something broke in a way that needed someone who could read code for a living. I can still remember the particular feeling of opening a Fortran routine that is really a paper, and realising I could not tell whether what I was looking at was a bug or the mathematics doing something I did not understand yet. Finding out which was the whole job. I am glad I went in, and I am glad I found the edge of what I could do, because that is where I learned what the statisticians were actually for.

## Register

**2000-2017, Salford Systems.** Craft and long horizons, in the era's own vocabulary — *data mining*, *predictive modelling*, not "ML/AI". Junior where he was junior: the awe is part of it. The present-day self narrates the contrast with today's tooling; the past self does not know it is coming. See [voice and prominence](../../workflows/voice-and-prominence.md) § *The registers, era by era*.

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | There is one from the machine-learning years, before that was a fashionable phrase |
| 1 | Hook | The source code was a mathematical paper that happened to be written in Fortran |
| 2 | Stakes | The engines were the product; a wrong number is worse than a crash |
| 3 | Complication | I could not tell a bug from the mathematics, and there was no assistant to ask |
| 4 | Move | Learned enough of the mathematics to isolate it, and worked the rest with the people who owned it |
| 5 | Punchline | Found my mathematical boundary, and found what my colleagues were worth |
| 6 | Handover | Ask me what happens when the compiler itself is wrong |

## Narrative — rehearse verbatim

**0 · Offer**
> Can I give you one from the data-mining years? Before anybody called it AI.

**1 · Hook**
> Our decision-tree and boosting engines were Fortran, descended from the original research code. Opening one of those routines is not like opening an application. It is a mathematical paper that happens to be executable.
⟨breathe⟩

**2 · Stakes**
> Those engines were the product. Customers built credit models and medical research on them. And the failure mode that frightens you in numerical code is not the crash — it is the number that comes back looking perfectly reasonable and is wrong.

**3 · Complication**
> Here is what made it hard. I am a software engineer. I could read the code, and I could not always tell whether a result was a defect or the algorithm doing something correct that I did not understand yet. And this was well before you could paste a routine into an assistant and ask it what the mathematics is doing. There was the paper, the code, and the people.
⟨breathe⟩

**4 · Move**
> So I did two things, and I think the order matters.
> First, I learned enough of the mathematics to ask a precise question. Not enough to derive it — enough to isolate. I chased assertion failures down to how long a model's internal structures were supposed to stay alive. I found a statistic that was computed along a path shared by two different commands, which is exactly where a change for one quietly becomes wrong for the other.
> Second, I took those precise questions to the people who owned the mathematics, including the author of the engine himself. Not "this looks wrong" — "here is the path, here are the two callers, here is what differs; is this a property or a defect?"
*(optional)* And I got defensive about it in the code: assertions as watchdogs, so the abnormal state announces itself instead of propagating into a plausible-looking answer.

**5 · Punchline**
> I found the edge of my mathematics, precisely, and I stopped being embarrassed by it. Source code that is not your bread and butter shows you very vividly where your talents are — and whose talents you need. That is the most useful thing that codebase taught me, and I have used it in every specialist room since.
⟨breathe⟩

**6 · Handover**
> Ask me about the year we lost to a compiler, because that is the same story with a vendor in it.

## If they follow up

- **"The compiler?"** → The Fortran backend was built with a vendor compiler, and it had bugs that were miscompiling the part of the product that does the real work. The vendor engaged properly and stayed responsive, and resolution still took about a year, which the business paid for. The lesson I took is that a responsive vendor and an acceptable time-to-resolution are two different things, and only the second one is on your critical path. I have used that judgement on every vendor dependency since. *(The year and the compiler version are not something I can pin down precisely, and I would rather say so than invent it.)*
- **"How deep does your mathematics actually go?"** → Deep enough to isolate a numerical defect and ask a statistician the right question; not deep enough to derive the algorithm. I am precise about that line, because in a room with real statisticians, the fastest way to lose the room is to overstate it.
- **"Where else did you step into somebody else's language?"** → SAS. A pharmaceutical client commissioned an analysis of a national mental-health survey and the data preparation was the whole job, so I learned SAS from scratch and built a macro system for it — including getting a codebase written for an older SAS to run again. That was my first pharma client, about a decade before I moved into regulated medical devices, and the habits are the same ones: someone else's domain, learned properly, with their experts close by.
- **"Would AI change how you'd do that today?"** → It would change the first half and not the second. An assistant will explain an unfamiliar numerical routine now, which is genuinely faster than reading a paper for two days. It will not tell you whether the result your customer is looking at is a statistical property or a defect, and it will not be accountable for the answer. You still need the specialist, and you still need to have earned the standing to interrupt them.
- **"Was the team good?"** → Unusually. The company existed to commercialize the work of the people who invented these methods, so the statistical bar in the building was extremely high — and they were generous with me, which is not guaranteed when the software person turns up in the science. I think they were a bit surprised how far the software person kept getting into their code.

## Proof

Public and on the resume: the Fortran legacy codebase, technical debt kept to a minimum, and the engines themselves — CART, TreeNet, MARS — commercializing the CART monograph authors' work.

Private and thinner: the specific defects (model-structure lifetime assertions, a statistic computed on a path shared between two commands, partial-dependency semantics) come from a single breadth-first survey of the owner's mail, not a deep dive; no bug identifiers, fix dates or releases are recorded. The "assertions as watchdogs" line is the owner's own from that correspondence and should be re-verified against the full message before it is quoted as an exact wording. The compiler episode is undated. **Tell this story at the level of the method, not the ticket.**

## Know it — what stays with me

T1: the engine author in the dialogue is Dan Steinberg, the company's founder and a listed reference; Mykhaylo Golovnya was the statistician lead alongside. The owner has said these names may be used in a story; roles carry it better outward, and credit goes by role first. The product is SPM (Salford Predictive Modeler), which is public. The vendor compiler is Intel's, which is fine to name but adds nothing.

## Sources

- [2010-01-01 SPM engine debugging — CART/TreeNet/MARS internals](../../../raw/brag/2010-01-01-spm-engine-debugging-cart-treenet-mars.md)
- [2026-09-16 concurrency and parallelism specialization](../../../raw/brag/2026-09-16-concurrency-parallelism-specialization.md) § *Living with the Intel Fortran compiler* — cited, not graduated; its own story (C3) is still blocked on dating
- [2010-05-01 NCS-R SAS data preparation](../../../raw/brag/2010-05-01-ncs-r-sas-data-preparation-pharma-client.md) — the SAS follow-up

## Related stories

- [I kept records nobody asked me for](../stewardship/records-nobody-asked-for.md) — what the same seventeen years bought at the end of them.
- [I built the hand-rolled version in 2005](../concurrency/lowest-level-reflexes.md) — the same era, the systems half.
