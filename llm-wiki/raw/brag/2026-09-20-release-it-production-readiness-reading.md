---
title: "Worked through Release It! end to end, argued it at the enterprise book club, and found most of it already in my own practice"
date: "2026-07 to 2026-09 (annotation file last modified 2026-07-15; ingested 2026-09-20)"
thread: OBS
domains:
  - "Operational excellence and observability"
  - "Architecture and API design"
  - "Quality and test automation"
  - "Leadership, management, hiring"
context: "Best Buy Health; the book discussed with peers at the Best Buy Digital and Technology (DAT) book club"
sensitivity: private-repo
resume-worthy: yes
---

# Worked through Release It! end to end, argued it at the enterprise book club, and found most of it already in my own practice

## What I did

I read **Michael T. Nygard's *Release It! Design and Deploy Production-Ready Software*, Second Edition** properly — not skimmed. My annotated copy carries **255 highlights and 9 standing notes across 124 of its pages**, running from the opening case study to the closing chapters on adaptation and information architecture. A large share of the marks are card cues for spaced repetition; the rest are arguments with the text, connections to my own systems, or things I wanted to raise with other people.

I then **discussed it with peers at the Best Buy Digital and Technology (DAT) book club**, and on many of the points we agreed. Several of my notes are written *to* that room rather than to myself — *"What does everyone think about automated testing terminology? Useful? Doesn't really matter?"*, and *"lets discuss as I don't have much exposure to day to day all things Kubernetes"*.

**Why this belongs in the record rather than on a reading list.** The book is the canonical statement of *design for production*: stability patterns, the control plane, transparency, deployment, and the argument that operability is a feature rather than an afterthought. Most of what it prescribes I was already doing, under my own names, and having the canonical vocabulary for it changes how I can talk about my own work — to a hiring panel, and to an enterprise networking organization whose engineers carry pagers.

### The frame I took from it, and want to use

Nygard's platform chapter is where the book named something I already believed. A platform team, he argues, has a **customer-focused orientation, and its customers are the application developers** — and he is blunt that a separate "DevOps team" is a fallacy, because the platform builds mechanisms that let other people do things rather than taking tasks on their behalf. My own marginal note on that section is *"Enable, not just look for tasks"*.

**My extension of it, stated 2026-09-20:** the customers for network and platform software are **network engineers, DevOps engineers, and the people carrying a 24/7 pager**. Caring for that customer is genuinely hard — they are technically expert, they are interrupted at three in the morning, and they judge your software by how it behaves on its worst day rather than its best. It is also the most rewarding customer I have served, because the feedback is immediate and unsentimental. My observability, SOP and runbook work is what I have actually built for that customer, and I want it read that way rather than as internal housekeeping.

### Where the book described something I had already built

These are the notes where I connected the text to my own systems, and they are the reason the reading was not abstract:

- **A TCP connection can sit for days without a packet crossing it.** My note: *"That's mqtt keep alive for you."* The book's point about connections existing only as objects in the endpoints' memory is exactly the constraint behind the cellular MQTT keep-alive work.
- **Monitoring implemented by the teams that own the service.** My note against the control-plane section on who builds monitors: *"And that's what we do in health suborg with our Datadog."* The book treats team-owned monitors as the mature pattern; that was already the arrangement I had built.
- **Transparency as an economic argument.** Against the passage arguing that monitoring, log collection, alerting and dashboarding are about economic value more than technical availability, I wrote *"Economic aspect of operational excellence."* This is the same claim my cellular-cost and rogue-device work makes in money rather than in reassurance.
- **A resource failure that fails a test rather than a customer.** Against the opening case study's connection-close defect: *"this same issue made unit tests for lively mobile 2 flaky. We are using real sqlite instances and sometimes close on database could throw. Making it non throwing saves the day."*
- **Release trains.** Against the deployment case study: *"Big fat release trains were pretty ugly during GreatCall days. The office party that accompanied the release was nice but extra free days off and long term health consequences do add up."* The human cost of a deployment practice, observed first-hand.

### Where I argued with it, or went further

The notes I care about most are the ones that are not agreement:

- **Failure-mode testing belongs at the cheap layer of the test pyramid.** The book's idea of dragging a system through every failure mode is, in my note, *"a brilliant idea"* — and then I pushed on where it should happen: *"unit tests are simple and economical way to get the failure mode code execute in isolation. Then we have less to worry about when crafting our integration tests. I believe it is pretty common that exception handlers and error code branches get executed at best during integration testing and too commonly in production."* That is my own **shift-quality-left** principle applied to a specific, usually-neglected category of code: the error branches.
- **AWS availability zones are not proper bulkheads.** My note: *"If AWS didn't want multi-cloud, they would make Availability Zones proper bulkheads. Either give people economical means to do things right or bear consequences of where smart developer minds go."* An architecture claim with an economic mechanism behind it, which is how I prefer to argue.
- **AI against toil, not against jobs.** Against the section on operators taking themselves out of the loop: *"That's what AI should help us doing, rather than scare us jobless. If promise is fulfilled the toil is gone. So we can focus on all the yet unknown places to be in the loop and solve something."*
- **Buzzwords get interpreted, and the interpretations drift.** On evolutionary architecture: *"I believe evolutionary architecture is hanging out with data products at some retirement resort."* On thrashing: *"was a hype term 10 years ago... I am not hearing it much anymore."* On the two-pizza team: *"such interpretations are rarely stable and evolve with the buzz cycle."* The disposition is consistent — take the mechanism, distrust the label.
- **Failure modes have a shared nature.** The note I wrote at the end of the stability-antipatterns chapter is the one that reads least like an engineering note and most like the way I actually think: the failure modes all share a dark fundamental nature, and it is the systems that stay creative that hold together.

### The operational vocabulary I now have

The networking and control-plane chapters were the densest part of my reading, and they are the part most relevant to an employer whose engineers run networks: load balancing and its hardware, software and reverse-proxy forms; health checks and stickiness; virtual IPs and migratory virtual IPs; service discovery and why not to build your own; network routing and ambiguous-route resolution; demand control — Little's law, load shedding, residence time, listen queues and listen-queue purge, `TIME_WAIT`; the control plane, its cost, and the checklist of what belongs in one; log and metric collectors, push versus pull, nominal metric ranges; configuration services and their CAP-bound reality; canary deployments, command queues and scriptable interfaces.

I already worked in most of these ideas on the device and fleet side. What the book gave me is the **shared vocabulary an operations organization already speaks**, which is the difference between describing my work and having it recognized.

## Why it matters

- **It re-frames a decade of my operational work around its customer.** Observability, runbooks, SOPs and tabletop exercises are not adjacent to my engineering; they are the product I built for operators, and *Release It!* supplies the argument and the language for saying so.
- **It is evidence of deliberate practice, not just experience.** 255 marked passages, spaced-repetition cards, and a book club where the ideas were argued with peers is a different claim from having read a well-known book.
- **The disagreements are the credible part.** Agreeing with a canonical text costs nothing. Naming where I would go further — failure-mode coverage at the unit layer, availability zones as incomplete bulkheads — is what shows the reading was actually done.
- **It closes the loop with the networking record.** A network software engineer whose customers are network engineers should be able to speak about load shedding, health checks and control planes without translation. Now I can, and the reading is dated and evidenced.

## Skills demonstrated

Production-readiness and resilience engineering vocabulary; stability patterns and antipatterns; control-plane and platform design; operability as a designed feature; transparency, logging and metrics design; deployment design and release strategy; demand control and load shedding; service discovery and load balancing concepts; deliberate practice through spaced repetition; technical discussion and persuasion with peers outside the reporting line.

## What was blocked, cut short, or wrong

- **Kubernetes is a stated gap, in my own words.** My note asks to discuss it because *"I don't have much exposure to day to day all things Kubernetes."* The container and orchestration material is the part of the book I read as a learner rather than as a practitioner, and I do not claim otherwise.
- **The Anki cards are largely unbuilt.** A large share of the 255 marks are card cues — *"Card"*, *"List card"*, *"term card"* — and the deck does not yet exist. The reading is real; the spaced-repetition practice is a stated intention that the record should not inflate.
- **The book club is not minuted.** That peers agreed on many points is my own account, with no attendance record or notes behind it.

## Evidence

- The annotated PDF on my workstation, last modified 2026-07-15, carrying 255 highlights and 9 notes across 124 pages. The harvest of those annotations is retained in the maintainer's session scratch; the PDF itself is a copyrighted commercial book and is neither committed nor quoted at length anywhere in this repository.
- The notes quoted above are **my own writing in the margins**, not the book's text.
- One note names a colleague, Caleb, in connection with a test-pyramid conversation the week before. He is not otherwise in this record; see *Related*.
- The connections to my own systems are corroborated by the entries in *Related*, each of which predates this reading.

## Evidence limitations

- **The reading dates are inferred from the file's modification time**, 2026-07-15, which establishes when annotation last happened rather than when it started. No start date is recorded, and the book-club session or sessions are undated.
- **"Many of them were in agreement" is my recollection**, stated 2026-09-20. No participant is named beyond Caleb, and nothing is attributed to any individual.
- **Marginal notes are terse by nature.** Several quoted above are lightly tidied for spelling and sentence breaks; none is reworded. Where a note was a bare card cue it is described as such rather than dressed up as a judgement.
- **The book's own text is not the evidence here.** What this entry establishes is what I read, what I marked, what I concluded and where it met my own work — not any claim the book makes.

## Related

- [2023-12-21 device-health observability architecture](2023-12-21-device-health-observability-architecture.md) — the agentless architecture the book's transparency chapter describes in the abstract.
- [2025-01-09 self-reported-error operational runbook](2025-01-09-r5-self-reported-error-operational-runbook.md) — the runbook built for the operator as customer.
- [2024-01-04 cellular cost and rogue-device detection](2024-01-04-cellular-cost-rogue-device-detection.md) — the runbook, the agreed threshold and the tabletop exercise; observability paying for itself in money, which is the book's economic argument.
- [2025-01-14 monitor lifecycle review](2025-01-14-r5-datadog-monitor-lifecycle-review.md) — owning the monitor portfolio as a product, which is what a platform team does for its customers.
- [2023-09-30 patch-management SOP and vendor engagement](2023-09-30-security-patch-management-sop-and-vendor-engagement.md) — the SOP register of the same practice.
- [2026-07-29 cellular MQTT traffic scheduling](2026-07-29-cellular-mqtt-traffic-scheduling.md) — the keep-alive work one of these notes points straight at.
- [2026-09-20 network programming foundations and mentors](2026-09-20-network-programming-foundations-and-mentors.md) — the other half of the reading record, and the same enterprise networking organization.
- [2026-09-16 stewardship as a first principle](2026-09-16-stewardship-first-principle.md) — eliminating toil, which the AI note above restates.

## Record history

- 2026-09-20: created during the networking resume-variant pass, from a harvest of the owner's own highlights and notes in his annotated copy. The operators-as-customers framing, the failure-mode/test-pyramid argument, the availability-zones position and the Kubernetes gap are all new to the corpus. Caleb is named in a source note and has no entry in [professional contacts](../../wiki/entities/professional-contacts.md); recorded here so the gap is visible rather than silently dropped.
