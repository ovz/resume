---
cluster: concurrency
fits: [embedded, debugging, vendor, firmware]
status: draft
runtime: "2 min"
---

# A process leaking file descriptors is like a car with a broken alternator: everything misbehaves, each part differently

## Why I still care

This was before AI could read a vendor's code for me. I sat with a large amount of the chip vendor's code and ran experiments by hand until the leak had an address. Then I had to tell my manager that the right fix was out of our reach, and that the honest plan was a mitigation. I am proud of both halves — the reading, and saying the second thing plainly.

**Cue:** my note to my manager in May 2021 — *"mitigation is the only realistic way to address it for R4. This is because we cannot engage Qualcomm's help to fix QMI routing code."*

## Register

**2020-2026, Best Buy Health**, on the previous-generation device. Ownership and economy; plain about what could not be fixed. The metaphor is the owner's and is the story's one metaphor. The chip vendor is not named. Lines lifted from his note of 2026-09-24 per [spoken drafts](../../workflows/spoken-drafts.md).

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | One about a bug whose symptoms were everywhere |
| 1 | Hook | On Linux everything is a file, and something was leaking file descriptors |
| 2 | Stakes | The leak sat under the services that talk to the modem — most of a cellular emergency device |
| 3 | Complication | Failures at random places; the out-of-memory killer may never come; the alternator |
| 4 | Move | Read the vendor's code and experimented by hand until the leak had an address |
| 5 | Punchline | The fix belonged in the vendor's code, out of reach — so I said so, and we mitigated |
| 6 | Handover | Have you had to ship a mitigation instead of a fix? |

## Narrative — rehearse verbatim

**0 · Offer**
> There's one about a bug where the symptoms were everywhere, which is the worst kind.

**1 · Hook**
> On Linux everything is a file — sockets, pipes, devices, timers. And on our previous wearable, something was leaking file descriptors.
⟨breathe⟩

**2 · Stakes**
> The leak sat underneath the services that talk to the modem. On a cellular emergency device, that is most of them.

**3 · Complication**
> A process that leaks file descriptors is supposed to get caught by the out-of-memory killer. In practice, on a small embedded Linux system, that might arrive late or never, because descriptors cost almost no memory. Instead the process fails at whatever call happens to come next.
> It is like a broken alternator in a car. The alternator gives electricity to every piece of a modern car, so the failure modes are many, and each one looks different and a little funny.
⟨breathe⟩

**4 · Move**
> So I stopped chasing symptoms and went to the code. I read a lot of the chip vendor's code, and did a series of experiments by hand, until the leak had an address — the vendor's routing layer for the modem interface.

**5 · Punchline**
> The real fix belonged in the vendor's code, and we could not get them to make it for that device. So I told my manager plainly that mitigation was the only realistic answer for that product, and we mitigated.
⟨breathe⟩

**6 · Handover**
> Have you ever had to ship a mitigation instead of a fix? I find that is where the honest conversations happen.

## If they follow up

- **"How do you catch a descriptor leak?"** → Count them. On Linux every process's open descriptors are listed under `/proc`, so a descriptor count that only goes up is the signal. And the error has a name — the per-process limit is reached, `EMFILE` — so you can watch for that too. On the next device, a guard like that caught a second leak.
- **"Why doesn't the out-of-memory killer help?"** → Because the limit is per process and counted in descriptors, not bytes. The process hits its descriptor limit long before memory is under any pressure, so nothing kills it — it just starts failing.
- **"What was the mitigation?"** → *(owner to supply — not in the record)*.
- **"Would AI change how you'd do it now?"** → Reading a large unfamiliar codebase is exactly what an AI assistant is good at — it reads all of it and forgets nothing. The experiments would still be mine.

## Proof

The May 2021 note to my manager is in the committed leadership-board snapshot. The `EMFILE` semantics are in the Linux manual ([open(2)](https://man7.org/linux/man-pages/man2/open.2.html)).

## Know it — what stays with me

T1: the chip vendor is **Qualcomm**, and the layer is **QMI** (the Qualcomm MSM Interface) routing on the Lively Mobile+ (R4) modem SoC. The experiments, the exact leaking path and the mitigation are my recollection; no code or ticket is retained. The device's software is embedded Linux of the Yocto kind.

## Sources

- [2021-05-19 QMI file-descriptor leak and the mitigation](../../../raw/brag/2021-05-19-r4-qmi-file-descriptor-leak-mitigation.md)

## Related stories

- [The positioning library leaked twice](the-guard-that-counted-descriptors.md) — the next device, and two more leaks.
- [I never heard the bug once, and I still know what it was](the-bug-i-never-saw.md) — another failure that had to be found far from where it showed.
