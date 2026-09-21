# Source: *Release It!*, the owner's annotated copy

> **Doc type:** reference
>
> Summary of the owner's marginal annotations in Michael T. Nygard's *Release It! Design and Deploy Production-Ready Software*, Second Edition (Pragmatic Bookshelf, 2018). Tier **T1** for the annotations, which are the owner's own writing. The **book itself is a copyrighted commercial work and is neither committed nor quoted at length anywhere in this repository** — it stays in the session scratch scope, where `*.pdf` is gitignored. Status: **harvested 2026-09-20**, one pass, complete.

## What this source is

An annotated PDF on the owner's workstation, last modified **2026-07-15**, carrying **255 highlights and 9 standing notes spread across 124 of the book's 366 pages** — from the opening case study through stability antipatterns and patterns, foundations, processes on machines, interconnect, the control plane, security, deployment design, version handling and the closing chapters on adaptation and information architecture.

The annotations were harvested programmatically into the maintainer's session scratch, keeping each note attached to the passage it marks and the running head of its page, so any synthesis can be checked against what was actually marked.

## Why it is worth a source page

Most sources here record what the owner *did*. This one records **what he thinks**, at a level of candour that working documents rarely reach, because marginalia are written for an audience of one.

Three kinds of mark, and the proportions matter when judging the source:

| Kind | Roughly | What it is worth |
|---|---|---|
| Spaced-repetition card cues — *"Card"*, *"List card"*, *"term card"* | the majority | Evidence of deliberate study and of which concepts he judged worth retaining. Little content of their own, and **the deck does not yet exist** |
| Connections to his own systems | ~6 notes | The highest-value marks. Each one ties a book concept to a system he built, and each predates the reading |
| Arguments, extensions and asides | ~15 notes | Where he goes beyond the text, disagrees with it, or is wry about it. This is the part that shows the reading happened |

## What it uniquely contributes

- **The operators-as-customers frame.** Nygard argues a platform team's customers are the application developers and that a separate "DevOps team" is a fallacy; the owner's note is *"Enable, not just look for tasks"*. He has since extended it: the customers for network and platform software are network engineers, DevOps engineers and 24/7 pager carriers — a demanding customer and, in his account, a rewarding one. This is the framing the [networking variant](../resume/variants.md) now uses.
- **Failure-mode coverage belongs at the cheap layer.** His own extension of the book's "drag the system through every failure mode" idea: error branches and exception handlers are commonly first executed in integration testing and too often in production, and unit tests are the economical place to exercise them. It is his shift-quality-left principle applied to a specific neglected category of code.
- **Availability zones are not proper bulkheads**, argued with an economic mechanism rather than a preference.
- **AI removes toil rather than jobs** — the same position as his stewardship material, reached independently in a margin.
- **A stated gap, in his own hand:** limited day-to-day Kubernetes exposure.
- **Operational vocabulary.** The interconnect and control-plane chapters are the densest region of annotation — load balancing, health checks, virtual and migratory IPs, service discovery, routing, demand control and load shedding, log and metric collection, configuration services, canary deployment. This is the language an operations organization already speaks, and having it is what lets his device-side work be recognized rather than translated.

## Harvest status

**Complete, one pass, 2026-09-20.** Folded into:

- [2026-09-20 Release It! production-readiness reading](../../raw/brag/2026-09-20-release-it-production-readiness-reading.md) — the brag entry, which carries the substance.
- [accomplishments by domain](../concepts/accomplishments-by-domain.md) § *Operational excellence and observability*.
- [four problems, four solutions](../concepts/four-problems.md) § *Operational excellence and observability* — the "who is this for?" problem.
- [Design for production story cluster](../stories/production-readiness.md).

Nothing further is expected from this source unless the owner annotates more of it, in which case this page records a second pass rather than being rewritten.

## Caveats for anyone using it

- **Do not quote the book from here.** The harvest contains highlighted passages because a highlight is only meaningful with its text attached, but those passages are Nygard's writing. What may be reproduced in this repository is the **owner's own notes**. A synthesis that needs the book's argument states it in the owner's or the wiki's words.
- **A card cue is not an opinion.** Most marks say only that he wanted to remember something. Do not read agreement, let alone advocacy, into *"Card"*.
- **Marginalia are terse.** Notes quoted in the brag entry are lightly tidied for spelling and sentence breaks and never reworded.
- **One colleague is named** in a note about a test-pyramid conversation — Caleb, who has no entry in [professional contacts](../entities/professional-contacts.md). Recorded in the brag entry so the gap is visible.

## Related

- [Sources map](../sources.md) — every source's tier and disposition.
- [Brag ledger](brag-ledger.md) — ingest and promotion state of the entry this fed.
- [Sensitivity tiers](../workflows/sensitivity-tiers.md) — why the PDF stays in scratch and the annotations do not.
