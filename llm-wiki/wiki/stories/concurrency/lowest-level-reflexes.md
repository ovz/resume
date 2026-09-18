---
cluster: concurrency
fits: [embedded, firmware, architecture, principal, vendor, debugging]
status: draft
runtime: "3 min"
---

# I built the hand-rolled version in 2005, so twenty years later I could read someone else's and see it

## Why I still care

The 2005 project is the one I am still proudest of as a piece of engineering, and almost nobody has ever asked me about it, because it sounds like a line item. What I care about is what it did to me: I wrote every thread in that server myself, on three operating systems, with nobody to ask. Twenty years later, reading another company's audio service, I could see the missing critical section the way you see a misspelled word. I did not derive it. I *saw* it. That is not talent. That is what happens when you pay for something the expensive way once, and it never leaves you.

What I was afraid of, in 2026: that being right would not be enough — that I would name the races and nothing would change, because the code belonged to someone else.

## Register

**Two eras, deliberately.** Beats 0-3 are told in the **2000-2017 Salford register** — craft and long horizons, the young engineer alone with three operating systems and the vocabulary of the time ("the daemon", "the wire", "the pattern book"), awe intact. Beats 4-6 shift to the **2020-2026 Best Buy Health register** — ownership and economy, short declaratives, "I asked them to", willing to say what is still open. The shift *is* the story; do not flatten it into one voice. See [voice and prominence](../../workflows/voice-and-prominence.md) § *The registers, era by era*.

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | There is one that starts in 2005 and does not pay off until 2026 |
| 1 | Hook | I wrote a server that ran data-mining jobs for a room full of analysts, and I wrote every thread in it myself, on three operating systems |
| 2 | Stakes | Then: it was the company's strategic project and I was alone on it. Now: it is an emergency-response device, and the audio is how the wearer knows it heard them |
| 3 | Complication | Twenty years later the code is in C, it belongs to another company, I cannot run it, and the bug never reproduces |
| 4 | Move | I read it the way you read a language you speak. Named the races precisely enough to be actioned: predicate outside the mutex, a borrowed pointer treated as owned, a lookup dereferenced after the unlock, a stop flag "protected" because every writer took *some* lock. Then reviewed every round they sent back |
| 5 | Punchline | QA retested it and reported it running smoothly, with no behaviour they could attribute to lingering concurrency — and said it *felt* better |
| 6 | Handover | Ask me where you would get that ability today, because I would not recommend my route |

## Narrative — rehearse verbatim

**0 · Offer**
> There is one I like that starts in 2005 and doesn't pay off until last year.

**1 · Hook**
> In 2005 I built the largest system I've ever built alone. A server that ran machine-learning jobs on behalf of a room full of analysts, so their models ran on real hardware and their data never left the building. Windows, Linux, Solaris. I wrote every thread in it myself.
⟨breathe⟩

**2 · Stakes**
> There was no framework underneath any of that. This is before the standard library had threads. I hand-wrote the accept loop, the protocol on the wire, the job isolation, the lifetimes — on three operating systems that each had their own opinion about all four.
*(optional)* I built a pattern library underneath it, most of the Gang of Four catalogue, in C++, because the patterns were the only vocabulary anybody had then for the shapes I needed. Implementing a pattern is a completely different relationship with it than recognising the name.
> I can still remember the specific fear. Every one of those places was somewhere I could be wrong, and wrong quietly.

**3 · Complication**
> Now jump to last year. Different company, different decade. An emergency-response device people wear, and its audio service is misbehaving. Audio on that device isn't decoration — it's how someone who has just fallen knows the device heard them.
> The code was in C. It belonged to the contract manufacturer, not to us. I couldn't run it, I couldn't fix it, and the failure didn't reproduce.
⟨breathe⟩

**4 · Move**
> So I read it. And that's the whole point of the story — I read it the way you read a language you actually speak.
> The queue predicate was checked outside the mutex that protects the queue. A worker peeked at an item, and a peek borrows a pointer — it doesn't make the item yours to use once you've let the lock go. Somewhere else a request was looked up under a lock and then dereferenced after the unlock, which races another thread removing and freeing it. And there was a shared stop-state object that looked protected, because every writer took *a* lock. Not the same one.
*(optional)* None of those are exotic. That's what makes them dangerous — every one of them looks like working code, and three of them had been working for years.
> Then the part that was actually the work. I turned each of those into a specific correction another team could implement and we could review against their next delivery. And I kept reviewing. Acknowledge the fix that was right, name the one that was still incomplete, ask for the next one. I asked them for a documented lock order, so the discipline would outlive my review.
*(optional)* And I made them reconcile their diagrams with their source. An explanatory diagram is not evidence about what the code does.

**5 · Punchline**
> They fixed it. QA retested the service and reported it running smoothly — nothing they could attribute to lingering concurrency issues. They also said the experience just felt better, which is not a number, and I'll take it.
⟨breathe⟩
> The thing I want you to notice is that I never wrote a line of that service. The value was entirely in being able to read it.

**6 · Handover**
> Ask me where you'd get that ability today — because I wouldn't recommend my route.

## If they follow up

- **"Where would you get it today, then?"** → Not by hand-rolling a server, and I would not ask anyone to. I live in Boost.Asio day to day now, and I know exactly what it buys *because* I built the hand-rolled version first: it makes the execution context an explicit object, so where a piece of work runs is a decision written in the code instead of an accident of which thread called the function. What I would tell someone to do is learn one good abstraction properly — including where its guarantees stop. The last real Asio question I worked was whether an alternative signal design would cost us Asio's signal-handler guarantees around SIGTERM. That is the interesting level: not how to call it, but what it promises and where the promise ends.
- **"Why does an embedded engineer need this more than, say, a backend engineer?"** → Because nobody supplies it. In Python, Go, Java or .NET the runtime already schedules the work and speaks the protocol — you write the handler. On a device, you *are* the runtime. And it isn't only the Linux side: a modern device has two halves. On the bare-metal sensor co-processor microcontroller it's RTOS queues and timers, the wake-up chain that lets the application processor sleep, and the protocol between the two processors. On the hosted Linux side it's threads, wakelocks, a message bus, and a network cadence you design around the modem's wake-ups. Same fundamentals, both halves.
- **"What about Rust?"** → It helps, and I mean that: safe Rust rules out data races at compile time, which is a real class of bug gone. It doesn't rule out race *conditions* — the audio service had those too. And embedded Rust comes with a business mandate people don't say out loud: do it yourself. If the silicon vendor's Rust support isn't good enough, the team accepts the risk of writing that layer or pushing the vendor for it. That's a very different posture from the C and C++ habit of holding the vendor to their SDK's claims and telling everyone to focus on their own application. A team can only take that mandate if it commands the layer below — which is exactly where this skill lives.
- **"What about coroutines?"** → They're the right answer to a lot of this, and they arrived too late for everything in my record. `co_yield` is a C++20 keyword, but C++20 only shipped the machinery — the first usable coroutine type in the standard library is `std::generator` in C++23, which means GCC 14 in 2024 or Visual Studio 2022 17.13 in 2025. Our device builds against a 2018 Boost. A twenty-year-old problem got a good language-level answer about two years ago, on compilers an embedded programme doesn't get to pick.
- **"Isn't reading for races just experience?"** → Partly, and I'd rather not rely on it. That's why I worked through TLA+ in 2026 — it's the other direction on the same problem: reason about the interleavings instead of hoping to observe one. Reading catches what you've seen before. Model checking catches what you haven't.
- **"How do you tell another company their code is wrong without the relationship going cold?"** → You make the requests small, specific and implementable, and you say plainly which of the last round were right. Progress and completion are different things and they both need naming. The one I sent in May thanked them for the shutdown path they'd added, then asked for three focused things. That's the whole technique.
- **"Did you close every finding?"** → No, and I won't claim it. The last review I have still listed open structural and lifecycle concerns, and the QA result came back positive without a patch-by-patch closure ledger behind it. The service got better and I can prove the corrections; I can't prove the races are gone. Nobody can, which is the honest version of this whole field.
- **"What happened to the 2005 system?"** → It shipped on all three platforms with native installers I wrote myself — RPM, DEB and PKG — because a thing you can't hand to a customer's operations team isn't finished. I don't have adoption numbers for it and I don't pretend to.

## Proof

The 2004-2005 client-server system is on the public resume and described at length in the archived long-form resume: singlehanded design and implementation, the TCP/IP daemon, two developers working to a component framework I supplied, Windows/Linux/Solaris, native `.RPM`/`.DEB`/`.PKG` packaging, and a large share of the GoF catalogue implemented as a C++ library.

The audio-service corrections have a dated review and manufacturer-response trail across April and May 2026, with successive source submissions assessed round by round, and one response explicitly retained as sent. The QA outcome is the owner's report of 2026-09-14 and is quoted as such — not a QA document, and not a proof of race freedom.

## Know it — what stays with me

T1, for the Rust follow-up: the vendor example behind the do-it-yourself point is STMicroelectronics — the STM32WB part was the sensor co-processor MCU candidate (internally, the "sensorhub" — never said outward) in the 2021 wearable architecture. It is my example of the posture, not an evaluation on record, and it is never named outward.

T1: the manufacturer's identity, the device programme, the internal artifact names, the specific functions and files in the review trail, and which findings remain open. The manufacturer is named outward only by role — "the contract manufacturer". The failure shapes, the review technique and the 2005 system are all mine to tell.

Also T1 and worth remembering before a follow-up: a later review of mine retracted some wrong line and function citations and revised earlier positive assessments. If someone asks whether the audit was clean, the honest answer is that the audit itself needed corrections — which is a better answer than pretending it didn't.

## Sources

- [2004-01-01 SPM client-server TCP/IP daemon](../../../raw/brag/2004-01-01-spm-client-server-tcpip-daemon.md)
- [2026-04-24 manufacturer audio-service concurrency corrections](../../../raw/brag/2026-04-24-tcl-audio-service-concurrency-corrections.md)
- [2026-09-16 concurrency and parallelism as a deliberate specialization](../../../raw/brag/2026-09-16-concurrency-parallelism-specialization.md) — **cited, not graduated.** Its pattern-literature, Boost.Asio and coroutine substance is told here in the follow-ups; its Intel Fortran half waits on C3, so the entry keeps no `storied:` property.
- [2026-09-14 Boost proficiency](../../../raw/brag/2026-09-14-boost-library-proficiency.md) — **cited, not graduated.** This story tells the entry's Boost.Asio half only; its Boost.MSM substance is untold and belongs to the [state-machines cluster](../state-machines.md), so the entry keeps no `storied:` property and stays in the working graph.

## Related stories

- [The bug I never saw](the-bug-i-never-saw.md) — the same subsystem three years earlier, and the other half of the concurrency skill: finding a race you can never watch happen.
- [The fault that lost the fix](../positioning/the-fault-that-lost-the-fix.md) — a multithreading fault in a third party's library, root-caused from fleet telemetry.
