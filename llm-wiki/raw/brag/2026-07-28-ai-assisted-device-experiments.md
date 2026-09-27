---
title: "Designed and ran device experiments end to end with an AI coding agent — fleet configuration scripts, test procedures, notebook analysis — in calendar time rather than project time"
date: "2026 (documented instance: the keep-alive engineering build soak, 2026-05 to 2026-07)"
thread: AI
domains:
  - "AI-assisted engineering (since 2023)"
  - "Battery, power and cost of operation"
  - "Data engineering"
context: "Best Buy Health — Lively Mobile 2 engineering builds, device soak tests, warehouse telemetry"
sensitivity: private-repo
resume-worthy: yes
---

# Designed and ran device experiments end to end with an AI coding agent — fleet configuration scripts, test procedures, notebook analysis — in calendar time rather than project time

## What I did — the owner's account (2026-09-24, verbatim)

> Throw in a restrospect that with AI such experiment design and execution is literally calendar time expense. This is a perfect case for vibe coding, code review is a breathe because no clever code is allowed and irrelevant code is easily spotted. Once llm is in the correct area of hyperspace it doesn't chaotically blunder to some danger zone just out of coarseness of the model parameters etc. That's why prompt engineer profession was short lived. The challenge to keep LLM in the correct space (single word in the prompt determines succsss/failure) got solved by the industry in the matter of months. For modern LLMs the skill is to keep model comrehensive, demand top quality, not accept half baked results etc. I designed several successful experiments and the experience was stellar. A bunch of scripts configured any number of devices, testing instructions were ones I enjoyed executing, and analysis in Jupyter notebook looks like what would be an initiative for a Data Scientist to spend a week just on the first draft and engineer to put it in production. Now I have production grade internal software on my dev machine in minutes. That's my local SAS-apocalypse episode, but more Javon paradox style. I used to have to figure out what is doable and keep my urges to eliminate toil under strict reality check. Now my good stewardship instincts grow into comprehensive documentation and production grade software. I feel like we solved Navier-Stocks equaltions for Agile software development. Contract negotiation still stands, but comrehensive documentation is not a cope out anymore.

## What the record shows

- **The documented instance.** The 2026 cellular keep-alive work ([2026-07-29](2026-07-29-cellular-mqtt-traffic-scheduling.md)) was validated on engineering builds soaked on real devices; the owner's July 2026 one-on-one note says he was "soaking devices to confirm the effect on battery life", and the [statistical-bar entry](2026-05-17-statistical-bar-and-data-science-partnership.md) records the notebook produced from that build.
- **The shape of the method**, in his account: scripts that configure any number of devices the same way; test procedures written to be executed by a person; analysis in a Jupyter notebook against the telemetry — a week of a data scientist's first draft plus an engineer's productionising, done on his workstation in the time the experiment itself takes.

## His reading of what changed, stated as opinion

- **Experiments now cost calendar time, not project time.** The device soak is the long pole; the tooling around it no longer is.
- **Vibe coding fits this case exactly** — straightforward code, no cleverness allowed, anything irrelevant easy to spot in review.
- **Prompt engineering was a short-lived profession.** Keeping a model in the right region — where one word in a prompt decided success — was solved by the industry in months; the skill now is keeping the model comprehensive, demanding top quality and refusing half-finished results.
- **It is Jevons, not apocalypse.** The 2026 "SaaSpocalypse" reading is that agents replace software; his local experience is the Jevons paradox — cheaper software means he builds far more of it ([Jevons paradox](https://en.wikipedia.org/wiki/Jevons_paradox)). The urge to eliminate toil, once held in check by what was feasible, now turns into documentation and production-grade internal tools.
- **The Agile Manifesto's trade-off moved.** It values "working software over comprehensive documentation" and "customer collaboration over contract negotiation" ([agilemanifesto.org](https://agilemanifesto.org/)); the second still holds, but comprehensive documentation is no longer the expensive side. His own wry version: it feels as though someone solved the Navier–Stokes equations for Agile ([the Millennium problem](https://www.claymath.org/millennium/navier-stokes-equation/)).

## Why it matters

It turns the owner's long-standing preference — a stated hypothesis and the smallest decisive experiment, instead of an analysis campaign — from something he had to ration into something he can afford every time. That is the practical meaning of AI-assisted engineering for an embedded principal: more questions answered by measurement, sooner.

## Skills demonstrated

Experiment design on device fleets; AI-assisted development of test tooling and analysis; Jupyter and warehouse analysis; judgement about where AI code generation is safe; documentation as a by-product of engineering.

## What was blocked, cut short, or wrong

- **"Several successful experiments" are not listed.** Only the keep-alive soak is documented in this repository.
- **Token budgets are a real constraint** — his June 2026 note records a moderate job using a fifth of a monthly allowance and lighter models blundering through iteration. Calendar time is cheap; model time is not free.

## Evidence

The owner's statement above; the leadership-board notes of 2026-06-14 and 2026-07-28 (committed Trello snapshot); the linked keep-alive and statistical-bar entries. Web sources linked inline, fetched 2026-09-24.

## Evidence limitations

"Minutes", "a week" and "production grade" are the owner's characterisations; no timing or review record is retained. Outward, keep to the method and one concrete instance; the opinions are for conversation, marked as his.

## Related

- [2026-05-26 AI adoption and the choreographer agent](2026-05-26-ai-adoption-agentic-engineering-choreographer.md) — the team-level practice.
- [2026-07-29 cellular MQTT traffic scheduling](2026-07-29-cellular-mqtt-traffic-scheduling.md) — the feature the documented experiment validated.
- [2026-05-17 statistical bar](2026-05-17-statistical-bar-and-data-science-partnership.md) — hypothesis first, smallest experiment.
- [2021-11-15 power-budget trade-offs](2021-11-15-r5-product-architecture-power-budget-tradeoffs.md) — the same rigour, before AI.

## Record history

- 2026-09-24: created from the owner's TODO note of 2026-09-24 (verbatim above), grounded in the committed leadership-board snapshot and the linked entries.
