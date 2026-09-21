---
title: "Network programming foundations: Stevens, a daemon built from the book, and the two people who kept the thread alive"
date: "2026-09-20 (statement); the foundations it describes run from ~2004 to the present"
thread: CONC
domains:
  - "Architecture and API design"
  - "Cloud and distributed systems"
  - "Leadership, management, hiring"
context: "Spans Salford Systems (the TCP/IP daemon) and Best Buy Health (the mentorship); the reading and the influences are the owner's own"
sensitivity: private-repo
resume-worthy: yes
---

# Network programming foundations: Stevens, a daemon built from the book, and the two people who kept the thread alive

## What I did

This entry records something the corpus had been asserting without grounding. The
[2004-2005 TCP/IP daemon entry](2004-01-01-spm-client-server-tcpip-daemon.md) says I did
concurrency, parallelism, network programming and protocol design "all four at once with
nobody to ask". That is true about *people*. It is not true about *sources*, and the
source matters, because it is why the result was competent rather than merely finished.

### The book

**Mykhaylo "Misha" Golovnya brought me W. Richard Stevens' *UNIX Network Programming*
on a visit to Ukraine, and I devoured it.** I was a Salford Systems contractor working
from Kharkiv at the time, and a physical technical book arriving from the U.S. side of
the company was not a small thing.

Stevens is still the reference for writing network code — the socket API, accept loops,
I/O multiplexing, the concurrent-server designs and what each one costs. My statement,
2026-09-20: *"To this day this is the bible of network programming."*

**It was one of the pillars the predictive-jobs TCP/IP daemon was built on.** That is the
honest causal claim and I want it recorded as a causal claim rather than a coincidence of
dates: I did not invent a concurrent server design in 2004 from first principles, I
learned the design space from Stevens and then chose within it, on three operating
systems, alone. The part that was genuinely unassisted was applying it — there was no one
to ask when Solaris and Windows disagreed.

**I am an advanced network programmer to this day**, and I state that plainly rather than
hedging it, because the record behind it is twenty years long and is listed in *Related*
below.

### The mentor who is in charge of networking

**Tim Wodarski** — Senior Director, Networking, in Best Buy's Digital and Technology
organization, and my mentor for over a year — **told me a lot of war stories about
networking at Best Buy.** Enterprise networking at retail scale is not my domain and I
have never claimed it is. The point is what those stories landed on.

**They landed on fertile soil.** I was not hearing them as a curious outsider. I had the
client/server SPM daemon behind me, and networking had been a side initiative in a long
list of projects since — most obviously the cellular-connected wearable, where I own the
device's side of the transport. So the war stories connected to things I had actually
built, and that is what turned a mentoring relationship about career trajectory into one
that also fed a technical thread.

This is also a note about how the mentorship works, which is recorded separately in
[2025-05-23 mentorship and the Principal Engineer goal](2025-05-23-mentorship-principal-engineer-goal.md):
I bring him live problems. The networking conversation was not on the agenda for the
mentorship; it happened because the person assigned to me happens to run networking, and
I noticed that was worth something and used it.

### Russ White, and why I am glad I never specialized

**Tim's stories confirmed something I already suspected: I am a die-hard fan of Russ
White.** I went through his O'Reilly video content, and **it cemented my network
engineering understanding** — not my network *programming*, which Stevens gave me, but
the layer above it, where you reason about why a protocol is shaped the way it is.

[rule11.tech](https://rule11.tech/), the *Rule 11 Reader*, is White's personal site and
primary technical blog. My statement, 2026-09-20: **it is one of my beacons in the world
of today, as of 2026.**

The judgement I actually want on the record, because it is unusual and it is mine:

> **I am glad I did not specialize in networks and get stuck in dogmas** — and I am
> looking forward to embracing such a specialization and being successful at it,
> *because of* Russ White's and Tim's advice and inspiration.

Both halves are sincere and they are not in tension. Career network engineers inherit a
body of received practice; arriving at the specialization late, from the programming side
and with White's problem-first framing, means arriving without the dogmas. That is an
argument for me taking a networking role, not against it.

### The heuristic, and the correction it needs

White's habit of mind is the thing I took. My paraphrase of it, 2026-09-20: *"there are
usually 4 basic problems and 4 basic solutions in each domain."*

**The paraphrase is close but not exact, and the exact version is better.** White's
["Four Things" model](https://packetpushers.net/blog/beyond-osi-the-four-things-model-of-networking/),
which he offers explicitly as an alternative to OSI, names **four problems** — marshaling,
multiplexing, flow control, error control — and gives each **three** solution options, not
four. He is direct about why he bothers: he does not find OSI "very useful in day-to-day
work" and prefers "simpler yet extensible models", because a model that tries to put
everything in one place stops working as a thinking tool. What he wants is a mental map
that makes you ask a useful question.

I asked for this to be generalized across my domains. That work is
[four problems, four solutions](../../wiki/concepts/four-problems.md).

## Why it matters

- **It closes a grounding gap, not a bragging gap.** "Advanced network programmer" was
  already implied by the record. What was missing was where the competence came from, and
  a claim whose origin you can state is a claim you can defend in an interview.
- **It is the piece the networking resume variant could not be written without.** The
  [variants page](../../wiki/resume/variants.md) said so explicitly before this entry
  existed: the owner's networking foundations and mentors "are his to tell; they enter
  this variant only once captured as brag entries."
- **The anti-dogma argument is a positioning asset.** Most candidates for a networking
  role argue they have specialized. Arguing that arriving without the received practice is
  a feature — and naming the practitioner whose framing replaces it — is a better answer
  and a rarer one.
- **It gives the mentorship a second dimension.** The existing record has Tim as a career
  mentor. He is also, incidentally, a networking director whose war stories fed a technical
  thread, which is a fair thing to notice about how to use a mentor well.

## Skills demonstrated

Network programming from the primary literature; socket and concurrent-server design;
reading a domain through its problem space rather than its layer diagram; using a
mentoring relationship beyond its stated purpose; locating and correcting one's own
paraphrase of a source.

## What was blocked, cut short, or wrong

- **My paraphrase of White's model was wrong in one detail** — four solutions rather than
  three — and I would rather the record carry the correction than the paraphrase. It is a
  small thing, and it is exactly the kind of small thing a networking interviewer notices.
- **I never specialized.** That is a real gap against a career network engineer and the
  resume must not pretend otherwise. The honest framing is the one above: programming-side
  depth, engineering-side understanding, no routing-protocol or switch-configuration
  practice at all.
- **The war stories are Tim's, not mine.** Nothing from them is a claim of my experience,
  and nothing from them reaches any outward document.

## Evidence

- The owner's statement of 2026-09-20, captured verbatim in the maintainer's session
  scratch — the Stevens/Misha account, the Tim Wodarski account, the Russ White account
  and the rule11.tech identification are all from it.
- Misha's identity as Mykhaylo Golovnya, a Salford colleague and a listed reference, is
  established in [professional contacts](../../wiki/entities/professional-contacts.md).
- Tim Wodarski's role — Senior Director, Networking, Best Buy DAT — is recorded in the
  same page, stated by the owner 2026-09-14, and predates this entry.
- Russ White's Four Things model is cited above to an article **he wrote**, not to a
  summary of him, precisely so the correction to the owner's paraphrase rests on the
  source rather than on recollection.
- The daemon this reading produced is
  [2004-01-01 TCP/IP daemon](2004-01-01-spm-client-server-tcpip-daemon.md), itself grounded
  in the contemporaneous archived long-form resume.

## Evidence limitations

- **Misha's visit is undated.** The owner's account places the book before the 2004-2005
  daemon and nothing narrows it further. No month or year is claimed, and the filename
  date is the capture date, not the event.
- **The specific Stevens volume is the owner's confirmation, given 2026-09-20** when asked
  to choose between *UNIX Network Programming* and *TCP/IP Illustrated*. It is a
  recollection of a book received roughly twenty years earlier.
- **"Advanced network programmer to this day" is the owner's self-assessment.** It is well
  supported by the entries in *Related*, but it is a self-assessment and the wording
  outward should rest on the artifacts rather than on the adjective.
- **No O'Reilly title is recorded** for the White video content the owner worked through.
  Do not name one.
- The Tim Wodarski conversations are undated one-on-ones; the leadership-board lists cited
  in the mentorship entry are the surrounding evidence, and none of them is quoted here.

## Related

- [2004-01-01 TCP/IP daemon](2004-01-01-spm-client-server-tcpip-daemon.md) — what the
  Stevens reading was spent on, and the origin of the concurrency thread.
- [2026-09-16 concurrency and parallelism as a deliberate specialization](2026-09-16-concurrency-parallelism-specialization.md)
  — the specialization this is the networking half of.
- [2025-05-23 mentorship and the Principal Engineer goal](2025-05-23-mentorship-principal-engineer-goal.md)
  — the mentoring relationship, recorded from the career side.
- [2025-01-16 phone capability SDK over LCM](2025-01-16-ccfphone-r5-device-lcm-odm-integration.md)
  — UDP multicast publish/subscribe between two processes; the non-TCP leg of the record.
- [2025-12-07 HTTP transfer callback ownership](2025-12-07-http-transfer-callback-ownership.md)
  — asynchronous HTTP, TLS, and fire-and-forget reporting on a device that cannot assume
  the network is healthy.
- [2026-07-29 cellular MQTT traffic scheduling](2026-07-29-cellular-mqtt-traffic-scheduling.md)
  — keep-alive, flush coordination, and the SMS path when IP is gone.
- [2024-01-04 cellular cost and rogue-device detection](2024-01-04-cellular-cost-rogue-device-detection.md)
  — bytes as money on an MVNO the company owns.

## Record history

- 2026-09-20: created from the owner's statement of the same day, during the networking
  resume-variant pass. The Stevens/Misha account, the rule11.tech identification and the
  anti-dogma framing are new to the corpus; the Four Things model was grounded to White's
  own article and the owner's paraphrase corrected rather than preserved.
