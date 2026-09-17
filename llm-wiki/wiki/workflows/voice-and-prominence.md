# Voice and prominence — how the record gets told

> **Doc type:** reference
>
> The two rules that govern every outward telling of this career: **one voice, many registers**, and **prominence follows evidence**. Plus the protocol for talking honestly about work that was blocked, frozen or never shipped. Audience: the owner rehearsing a story or preparing for a conversation; any agent writing a story, a resume line, a LinkedIn block or a reading list.
>
> This is a foundation pillar of this repository's agent instructions, not an optional style guide. A story that obeys [brag-stories.md](brag-stories.md)'s six beats and breaks the rules here is worse than no story: it will either sound like someone else, or claim more than the record can carry.

## The two rules

1. **One voice, many registers.** Every telling should sound recognisably like the same person — so that the owner's brain drops into storytelling mode from the first line, on any story in the corpus. But thirty years cannot be told in one register. The 1996 cryptography undergraduate and the 2026 architecture owner are the same person with different information, different authority and different stakes, and a telling that flattens them into today's voice loses exactly what makes the early material worth hearing.
2. **Prominence follows evidence.** How loudly a claim is made is set by how well it is supported *and* how much it mattered — never by stated impact alone. This cuts in both directions, and the upward direction is the one people neglect: **false humility is a defect**, as much as overclaiming is. A well-grounded, high-impact accomplishment that appears nowhere prominent is a failure of this file.

## Getting into the mode: role-play, not performance

The owner's own framing, and it is load-bearing: **channel the genuine past self, then merge it with the present self.** Not "remember what happened in 2019" — *be* the engineer who was staring at that graph in 2019, and let the person you are now narrate what he could not see yet. That combination is what makes a telling sound like something cherished rather than something memorised, and it is why the story template's *Why I still care* section is written before the narrative and never spoken aloud.

Role-play is also the mechanism that makes this fun. Business communication treated as a role to inhabit is play; treated as a report to produce, it is a chore, and a chore becomes grind. The owner is gritty and will finish either way — but he **hates toil and reliably eliminates it**, and that disposition is itself part of the voice. It shows up as impatience with ceremony, a preference for the cheap decisive experiment, and a habit of automating whatever was done twice. Do not write it out in the name of professionalism.

Practical consequences when writing or rehearsing:

- **Speak in the tense of the era you are in.** Present tense for the moment you want to relive — "I can still see the log gap" — and past tense for everything you are only reporting.
- **Use the vocabulary you had then.** In 2005 nobody said "observability"; you said "the daemon's log". Retrofitted vocabulary is the fastest way to sound like a summary of yourself.
- **Let the earlier self be junior where he was junior.** The 1997 story is better told with the awe intact than re-narrated as though you always knew.
- **Keep one constant thread audible across all of them** — see the last row of the table below. That is what makes it one career rather than five jobs.

## The registers, era by era

| Era | Who you were | The register it earns | Say it only from inside this era | The trap |
|---|---|---|---|---|
| **1996-2000** — cryptography at IIT | The first undergraduate the institute hired, working for his own university mentors | Wonder and rigour. Low-level, unforgiving work described with the pleasure of someone who could not believe he was allowed to do it | Big-number arithmetic by hand, a kernel driver on Win9x, elliptic curves before they were the default — and what it felt like to be trusted with a bank's cryptography at that age | Narrating it with today's security vocabulary and losing the awe |
| **2000-2017** — Salford Systems | Product engineer growing into architect and product owner, in machine learning before the words existed | Craft and long horizons. The register of someone who shipped the same product line for seventeen years and watched a field become fashionable around him | Serving Nobel-adjacent statisticians and non-statistical domain experts from one GUI; commercializing the CART authors' work; the client-server daemon that taught him concurrency | Using 2026 ML vocabulary for 2006 work, which makes it sound derivative rather than early |
| **2017-2018** — Minitab | The person who held two decades of institutional knowledge during an acquisition | Custody and dry judgement. Short, factual, slightly wry — a register about responsibility rather than achievement | What it takes to transfer an entire company's intellectual property and freeze projects so they can actually be resurrected; reading an environment instead of assuming one | Turning a short tenure into either a triumph or a grievance. It was neither |
| **2018-2020** — GreatCall | Hands-on embedded engineer on a device people's safety depends on, through a recall | Urgency and plainness. Short declaratives, bare numbers, no adjectives. The stakes do the work | The 2019 recall and relaunch; making a fleet answerable with telemetry when nothing could say which devices were affected; watching a whole company coordinate under a hard deadline | Dramatising it. The facts are already dramatic; adding emphasis reads as insecurity |
| **2020-2026** — Best Buy Health | Architecture owner across two device lines, still hands-on, working through other people | Ownership and economy. Calm, specific, willing to say "I decided" and equally willing to say "that was blocked" | Choosing a C++ standard on what static analysis can enforce; agentless observability because no agent fit the RAM budget; earning the regulated medical work by asking for a year | Sounding like a manager. The authority here comes from still being in the code |
| **All eras** | The constant | The security professional's reading of any system; raising the bar and then reading whether the room lets a raised bar compound; builder-architect close enough to implement; grit without patience for toil | — | Dropping the thread, so the career reads as five jobs instead of one arc |

## Prominence follows evidence

**The ordering rule.** Rank every candidate claim by *support × impact*, then let position, length and repetition follow that rank. Position means the first two pages of the resume, the top of the About section, the first thirty seconds of an answer, and which stories make a reading list at all.

| Support | Impact | What it gets |
|---|---|---|
| Well grounded | High | **Lead with it.** Resume front matter, LinkedIn About, the first story in any reading list. Repeat it across surfaces — repetition is prominence |
| Well grounded | Modest | **Credibility ballast.** Depth sections, follow-up answers, the specific detail that proves the big claim is not decoration |
| Thin | High *as stated* | **Demote, never delete.** It stays in the brag file at full strength, and the outward version is narrowed to the part that is actually supported. A loud claim on thin support puts every other claim on the page into question |
| Thin | Modest | **Brag file only**, until evidence accrues. Capture is not disclosure |

**Where "support" is read from, mechanically.** Three places, and none of them is memory: the claim's status in [coverage.md](../resume/coverage.md); the entry's `## Evidence` and — where present — `## Evidence limitations` section; and the entry's `## What was blocked, cut short, or wrong` section. An entry that says its own weakest point out loud is *more* usable outward, not less, because the outward version can then be drawn precisely at the line the evidence reaches.

**Against false humility.** "Instrumental in", "helped with", "participated in" and "was involved in" are the house style of a career that undersells itself. Where the owner decided, designed, root-caused, argued, or owned, the verb says so. Where he observed, supported or watched from an adjacent seat, the verb says *that* — and the record already does exactly this in places, which is why the strong claims are believable.

**Numbers land bare or not at all.** A quantified claim with no evidence behind it is the worst of both worlds: it invites the one question you cannot answer. The corpus already contains a retired productivity multiplier for exactly this reason.

## Blocked, frozen, and never shipped

Thirty years contains work that shipped and was seen by customers, work that was built and stopped, and work that was argued for and refused. **All three are tellable, and the second and third are often the more interesting.** A follow-up question about what happened to something is not a trap; answering it honestly is a large part of what makes the wins credible.

Three buckets, and the honest sentence for each:

- **Shipped, and customers saw it.** Say so plainly and attach the outcome. This is where prominence belongs by default.
- **Built, then stopped, frozen or overtaken.** Say what was built, say it stopped, and say what you learned — including where the reason was organizational rather than technical. "Proposed and worked, then slowed; nothing shipped" is already the house phrasing for this in the record.
- **Argued for and not taken up.** Say what you argued, what the argument rested on, and what you did next. A negative result you reached and acted on — a prototype cut short because it would not have paid for itself — is engineering judgement, not failure.

**The lesson is part of the win.** For every blocker, be ready with both halves: the ones overcome (and how), and the ones not overcome (and what they taught). The second list is shorter and lands harder, because almost nobody volunteers it.

**The employer-secret boundary is separate from, and narrower than, discretion.** Honest telling never requires disclosure. What stays out: unreleased plans and roadmaps, internal defects in a current employer's product, manufacturer and component-vendor identities, colleague names at the public tier, and anything covered by [sensitivity tiers](sensitivity-tiers.md) § *T2*. What is unambiguously the owner's own to tell: that he proposed something, the reasoning he used, the constraint he found, what the experience taught him, and the outcome as far as the public record already shows it. *"That one didn't ship, and here's what I took from it"* discloses nothing.

## Humility, respect and trust — what every telling about people keeps

The owner's working values, and the check for any story that involves a colleague: **humility** — nobody is the only capable person in the room, and being right quietly beats being right loudly and late; **respect** — a colleague's competence and constraints are assumed, and disagreement is about the work; **trust** — people get the benefit of the doubt, and work handed to someone is not quietly redone.

**Do not cite the source or recite the three as a slogan.** They come from *Software Engineering at Google*, and for some listeners adopting one company's engineering culture reads as a matter of faith rather than judgement. Let the stories show the values.

**Why these three, stated 2026-09-14.** The owner prefers a small, consistent set of principles with a clear switch between them over a set that tries to cover everything. Amazon's leadership principles were a strong set in their original form; as the list grew, the principles began to interact and argue with each other. Three that do not conflict are easier to work with than many that do.

In a telling:

- **Friction with a colleague** is told as what the disagreement was about in the work, never as a verdict on the person. The private record keeps the full account ([sensitivity tiers](sensitivity-tiers.md) rule 8); the telling does not need it.
- **Raising the bar for someone** is told as what they could do next, not what they could not do.
- **A decision that went against you** is told as the reasoning on the other side first, then yours.
- **Credit** goes to people by role, generously, and before your own part.

## Applying it

| Doing this | Apply |
|---|---|
| Writing a story ([brag-stories.md](brag-stories.md)) | Pick the era register before writing the narrative; write *Why I still care* first; put blocked work in *If they follow up* with its lesson |
| Building a reading list | Order by support × impact, not by recency alone; include at least one blocked-work answer, because it will be asked |
| A resume pass ([update-workflow.md](../resume/update-workflow.md)) | Prominence table above decides placement before wording is drafted; check the claim's coverage status first |
| A LinkedIn pass ([linkedin-publish.md](linkedin-publish.md)) | The About section is the highest-prominence surface in the corpus. Only well-grounded, high-impact claims belong in its first paragraph |
| Ingesting a brag entry ([brag-file.md](brag-file.md)) | Write `## Evidence limitations` and `## What was blocked, cut short, or wrong` while the detail is fresh. They are what makes later prominence decisions possible |
| Considering a dream job ([dream-job hub](../dream-jobs/dream-job-hub.md)) | Same rule: a candidate's stated fit is worth nothing without the record behind it, which is why each candidate page carries an evidence grade |

## Maintenance

- **The era table is stable; the registers are not opinions to relitigate per story.** Change it only when the owner's own account of an era changes.
- **A claim's prominence is re-derived when its support changes** — a new brag entry, a re-ingest, or a promotion. Coverage status changing is the trigger.
- Do not copy these rules into a story, a skill or an `AGENTS.md`. They live here and are linked; see [`.github/AGENTS.md`](../../../.github/AGENTS.md) § *Single source of truth*.

## Related

- [Brag stories](brag-stories.md) — the six beats, the notation, and how an entry graduates into a story.
- [Coverage map](../resume/coverage.md) — where a claim's support is recorded, claim by claim.
- [Sensitivity tiers](sensitivity-tiers.md) — the disclosure boundary this page defers to.
- [Dream-job hub](../dream-jobs/dream-job-hub.md) — where the same evidence discipline is applied to the future rather than the past.
- [Primary resume](../resume/primary-resume.md) — the surface where prominence is actually spent.
