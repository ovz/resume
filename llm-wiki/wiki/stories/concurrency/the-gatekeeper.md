---
cluster: concurrency
fits: [principal, leadership, integration, vendor]
status: draft
runtime: "2 min"
---

# They called me a gatekeeper, and I took it as a compliment

## Why I still care

Two genuinely brilliant people wanted to move faster than I thought was safe, and one of them had just been put in charge of exactly that by the founder. I had to say "not yet" without it becoming "no", and then help them do the thing I had asked them to wait for. The word I misunderstood still makes me smile.

**Cue:** the meeting in December 2012, and my reply the same afternoon — *"This is not a reason to get stuck with 5 year old technology but it calls for a careful approach to migration."*

## Register

**2000-2017, Salford Systems**, and the present self smiling at the younger one's English. Credit and concession before the point; no verdict on anyone. The humour is self-directed and is the only humour beat. Lines lifted from the owner's note of 2026-09-24 and his email of 2012-12-18 per [spoken drafts](../../workflows/spoken-drafts.md).

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | One where I was called a gatekeeper |
| 1 | Hook | Two brilliant colleagues wanted to move the whole C++ codebase to Intel's compiler; I pushed back |
| 2 | Stakes | A release about to ship; a compiler blunder would hurt the product badly |
| 3 | Complication | They were right about a lot, one was newly in charge of speed-ups — and I did not know the word |
| 4 | Move | Wrote down a careful path: ship on the known toolchain, experiment on the next version, hear the statistician on the engine — then set up the experiment myself |
| 5 | Punchline | We agreed to disagree, and the plan held |
| 6 | Handover | How do you tell a careful "not yet" from a gatekeeper's "no"? |

## Narrative — rehearse verbatim

**0 · Offer**
> I have one where somebody called me a gatekeeper, and I took it as a compliment.

**1 · Hook**
> In 2012 two brilliant colleagues wanted to move our whole C++ codebase onto Intel's compiler, and bring a new threading library into the engine. I pushed back, strongly.
⟨breathe⟩

**2 · Stakes**
> We were about to ship a major release. And from past experience, upgrading that codebase even between versions of the same compiler had introduced problems. A blunder in the compiler would have hurt the product badly.

**3 · Complication**
> They were right about a lot. The Intel compiler made faster code, and we were already using it on Linux. One of them had just been put in charge of speed-ups by our founder. The meeting got tense, and at some point one of them called me a gatekeeper.
> English is my second language, and I did not know that word. I thought it was a compliment.
⟨breathe⟩

**4 · Move**
> That afternoon I wrote down what I actually meant. This is not a reason to get stuck with five-year-old technology, but it calls for a careful approach. Ship the release on the toolchain we know. Run the experiments on the next version. And before a threading library goes into the engine, hear from the statistician who owns that code.
> Then I installed the Intel toolchain on the build server myself, and helped build the libraries for their experiment.

**5 · Punchline**
> We agreed to disagree, and the plan held: the release on the compiler we knew, and the experiment on the next version, on a build server I had set up for it.
⟨breathe⟩

**6 · Handover**
> I think about how you tell a careful "not yet" from a gatekeeper's "no". How do you tell the difference on your team?

## If they follow up

- **"Were you right?"** → A year later the next Fortran compiler broke our release builds, and I had to roll the whole team back. So I felt the caution was earned. How the C++ compiler question itself ended, I would not claim either way.
- **"How did you handle the colleague who was upset?"** → I wrote to him that we did not want to make it personal, and that everyone wanted to do the best job possible. Then, to the founder, I said I would put my experience with the codebase behind his effort, because he had picked an exciting problem to start with. That was true.
- **"What does 'gatekeeper' mean to you now?"** → *(agent-drafted — replace with your own)* Someone who says no to protect their own position. I try to be the opposite: say "not yet", say why, say what would change my mind, and then help.

## Proof

The mailbox has the meeting's aftermath: the colleague's note, the reply quoted above, the build-server setup two days later, and the January 2013 decision to keep the new configurations off the release branch.

## Know it — what stays with me

T1: **Ken Bernstein** (newly joined, Bernie's son, a chip-design expert, later at Apple) and **Illia Polosukhin** (later at Google, a co-author of the transformer paper, and NEAR). Dan Steinberg named Ken technical leader for speed-ups on 2012-12-23 and asked me to support his decisions; I agreed, and said pressuring people and disregarding other people's expertise was not sustainable. Ken left the meeting upset — his email says so. The threading library was Intel TBB; Misha (Mikhail Golovnya) had disagreed with bringing it into the engine. **Order, settled by the mail (my ruling, 2026-09-25):** this meeting was December 2012, and the Fortran 14 trouble came after it, 2013–2015. My memory of pushing back "despite the Fortran saga" merged the two, and there was email about it after all. The "past experience" my 2012 email cites is never named, so I do not name it either. My sense that both would leave for bigger things is mine, and it is never said. Illia's later fame is never used as borrowed credibility.

## Sources

- [2012-12-18 Intel C++ compiler migration — a careful path](../../../raw/brag/2012-12-18-intel-cpp-compiler-migration-careful-path.md)
- Cited, not graduated: [2012-06-01 SPM 7 Linux port and TBB evaluation](../../../raw/brag/2012-06-01-spm7-linux-port-tbb-evaluation.md)

## Related stories

- [I pinned a whole team to the older compiler for a year and a half](the-compiler-was-wrong.md) — what happened a year later.
- [Stewardship cluster, ST4 (planned)](../stewardship.md) — the other Salford story about holding a professional line.
