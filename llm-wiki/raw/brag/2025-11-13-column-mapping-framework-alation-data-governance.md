---
title: "Built the Column Mapping Framework — Copilot-driven roundtrip engineering from device source code into the enterprise data catalog — and carried its information-security case to Cyber Security leadership"
date: "2025-11 to 2025-12 (sibling-team demo 2025-11-13; Cyber Security meeting 2025-12-22)"
thread: DATA
domains:
  - "data engineering"
  - "AI-assisted engineering"
  - "risk management and compliance"
  - "security, cryptography, licensing"
context: "Best Buy Health, Device Analytics telemetry in Snowflake, Alation enterprise data catalog"
sensitivity: private-repo
resume-worthy: yes
---

# Built the Column Mapping Framework — Copilot-driven roundtrip engineering from device source code into the enterprise data catalog — and carried its information-security case to Cyber Security leadership

## What I did

Device Analytics events — the telemetry the PERS devices publish over MQTT into the Snowflake warehouse — had **no documentation at all** in the enterprise data catalog. More than thirty tables and nine hundred columns, of which the R5 device alone contributes thirty-four tables. Column descriptions were blank. The catalog and the thing it described had no connection.

The insight the framework rests on is that **the device source code is the ground truth**: C++ that constructs the JSON payloads and publishes them as MQTT messages fully determines what nearly every warehouse column means. And GitHub Copilot is good at reading source code.

**So the framework puts a bridge between them, and the bridge is Markdown.** Mapping files in Markdown sit between the source code and the catalog — chosen because, in his framing, *"for GitHub Copilot, Markdown is just another Programming Language"*, as native to it as C++ or Java. Nothing in the device source had to change to accommodate the catalog. The catalog's own API turned out to want CSV with HTML inside the cells, which he handled with upload scripts plus a set of tactical wins — a glossary architecture and knowledge-graph patterns that pay off wherever terminology repeats.

The result is **roundtrip engineering**: source code to mapping file to catalog, and back again for verification.

**Over thirty tables and nine hundred columns were cataloged**, covering location, steps, power and UI events, with every description grounded in source code rather than in recollection. Before the framework, coverage was limited, the documentation lag ran to weeks or months, and accuracy varied by who you asked — with the only alternative being to grind through the source by hand and type into a web UI.

**The change he is proudest of is cultural, and it is a process change rather than a tool.** Documentation moved into the development workflow the way unit tests did: the code change and the mapping update happen **in the same pull request**, so a reviewer sees both and can answer the only question that matters — does the mapping still match the code? That is what makes maintenance a property of the process instead of a promise.

## The argument he makes about why this generalizes

He is careful to place the innovation honestly: the GPT architecture is the real breakthrough, and he calls his own framework *"a secondary innovation"*. What makes it interesting is the shape of it.

**Roundtrip engineering was tried before and failed.** He names Rational Rose, model-driven development and UML roundtripping directly — *"We believed it would become the industry standard. It didn't scale."* His diagnosis of why LLMs change the answer is the sharp part: the old approach needed **one universal process**, and the new one does not. A customized roundtrip per codebase is now affordable, so unification is no longer the price of automation.

**The framework is designed to ride the model's improvement curve.** Its current rough edges are expected to be fixed not by rewriting it but by Copilot getting better — so the thing compounds without further investment, which is why he reaches for Einstein's line about compound interest.

**And the broader vision is that codebases start communicating through data catalogs.** Two systems coupled through a shared warehouse must agree on what each column *means*, not merely its type — his example is a location-accuracy field whose semantics drift in device firmware while the analytics side goes on assuming the old definition. That semantic coupling has always been managed by tribal knowledge. The framework makes it explicit and machine-checkable, which is the overdue promise of data mesh and data products.

## The information-security case, and the meeting

**The scaling argument he took to the security organization:** the framework came out of data governance, which makes it an easy win for the things that feed a security posture — technology asset inventories, data classification workflows — and from there it extends to the security tooling already running in the build: static analysis, container scanning, all of it wired into GitHub Actions where somebody has to choose which checks are release gates.

His claim is that this **shifts the work radically left**. The problem with security scanning, in his reading, is not detection but that *the ability to act on the results is so limited*. Put the policies and the tooling into context while the code is being written and reviewed, and a pull request — which is precisely a change increment that can create or modify a risk — becomes the natural unit of risk management. His stated end point: *"we can make an Information Security Agent that is present in every team"*, with risk management part of development from time zero and effectively zero overhead for the teams.

He also states his own standing plainly, which he rarely does: *"I believe I am somewhat uniquely qualified in both Software Engineering and Risk Management. My major from Ukraine was in Data Security."* And he expects most developers to pick up a risk-analysis mindset readily if given a framework to contribute through.

**The meeting.** He presented the achievement first to his sibling teams on **13 November 2025**, and that session was recorded. His mentor **Tim Wodarski** then mentioned the achievement to **Amber Kashmark, Senior Director of Cyber Security Risk & Compliance**, and the owner organized a meeting with her for **22 December 2025**, offering to adapt the sibling-team presentation for a security audience. **Rodd Johnson** took part as well — a data-governance leader at Best Buy Health whom the owner describes as brilliant, and who had been delighted and grateful about the Alation work. The owner's account is that Amber appreciated the presentation, Rodd gave him a great deal of support, and **a follow-up is pending**.

## A further vision: regulated compliance and quality systems

The same mechanism extends to regulatory compliance — every data element traceable to source code, so an auditor can follow lineage from catalog documentation to device firmware to warehouse table, and PII identification becomes systematic rather than requiring PII experts to also be source-code experts.

He pushes it one step further, drawing on the regulated medical-device work: he had used **Orcanos**, the eQMS at Current Health, and calls it comprehensive and effective but heavyweight — every team member required to master it, a great deal of manual labour on every small piece, and adoption that was still far from ubiquitous. His explanation is the thread that runs through his whole record: *"humans don't scale."* An AI-powered roundtrip quality-management system is, on this evidence, achievable.

His line about why documentation decays is worth keeping verbatim: *"We remember what it took to build the docs. Redoing the whole initiative feels like waste. So, we rationalize ourselves into accepting stale docs rather than face the toil."* And the answer: *"Tools of today, like GitHub Copilot, automate our forgetfulness."*

## Why it matters

- **It is a measured governance result, not a proposal.** Thirty-plus tables and nine hundred-plus columns went from blank to source-grounded, and the mechanism that keeps them correct is a review step rather than a person's diligence.
- **It reached outside his own organization on its merits.** A device-team engineer's data-governance framework getting a meeting with the Senior Director of Cyber Security Risk & Compliance, brokered by his mentor and supported by the data-governance leader, is organizational influence well beyond the device line.
- **It is the clearest instance of his standing theme** — eliminating toil as the practice of stewardship — applied to the thing every organization claims to want and almost none sustains.
- **It joins two halves of his background that rarely meet**: a Data Security degree and twenty-five years of engineering, aimed at making risk management a development activity.

## Skills demonstrated

Data governance and cataloging at scale; roundtrip engineering with LLMs; GitHub Copilot-driven automation; Markdown-as-interface design; Alation API integration and glossary/knowledge-graph architecture; Snowflake warehouse and MQTT telemetry semantics; documentation-as-code process design; security-posture and risk-management argument; executive presentation to a non-engineering audience.

## Evidence

The owner's presentation deck *Column Mapping Framework — Lively Mobile2 device source code to Alation Data Catalog*, whose speaker notes are his words as spoken; a recorded demo delivered to sibling teams on 13 November 2025; a Teams meeting invitation he authored for 22 December 2025 naming Amber Kashmark and describing the framework and the prior recording; and the column-mapping working materials retained in the device repository. Internal wiki, repository and recording links are deliberately not reproduced here.

## Evidence limitations

- **The table and column counts are the owner's own reporting** from his deck ("30+ tables, 900+ columns"; thirty-four tables for R5). No catalog export, coverage report or independent audit is retained here.
- **The outcome of the Cyber Security meeting is "appreciated, follow-up pending" and nothing more.** No adoption decision, policy change, funding, or extension of the framework into security tooling is claimed. Amber Kashmark's and Rodd Johnson's reactions rest on the owner's account.
- **The information-security scaling is an argument, not a delivery.** Asset inventories, classification workflows and scanner integration are proposed in the deck. Only the data-governance application was actually built.
- **The QMS and regulatory extensions are explicitly a vision**, offered as such in the deck, and must never be told as delivered work.
- **"Before" figures are qualitative.** "Weeks to months" and "accuracy varies" describe the prior state as he experienced it, without a baseline measurement.

## What was blocked, cut short, or wrong

Nothing was blocked. The honest shape of the story is that the built part is narrower than the argued part: one codebase's telemetry is cataloged, the named next targets — the handsets repository and the device-communication repository that owns the cloud side between MQTT and Snowflake — had not been taken at the time of the deck, and the security extension exists as a pitch with a receptive first audience.

## Related

- [2025-01-01 Data Steward on the enterprise data catalog](2025-01-01-data-steward-enterprise-data-catalog.md) — the governance role this work is the deepest technical expression of.
- [2025-10-29 AI data product in the catalog](2025-10-29-ai-data-product-in-alation.md) — the adjacent catalog initiative from the same period; that one scopes a data product, this one populates and maintains the catalog itself.
- [2022-05-18 Snowflake warehouse and device telemetry](2022-05-18-snowflake-edw-device-telemetry.md) — learning the warehouse directly, and the data-mesh ownership argument this work realizes.
- [2024-10-18 Copilot practice for an embedded C SDK](2024-10-18-copilot-embedded-c-sdk-practice.md) — the same engineer's earlier, embedded-side Copilot practice; prompts-as-documentation there, source-as-ground-truth here.
- [2026-05-26 AI adoption and agentic engineering](2026-05-26-ai-adoption-agentic-engineering-choreographer.md) — the later agentic work; this framework is a concrete production instance of the same conviction.
- [2024-09-24 Current Health and the quality management system](2024-09-24-current-health-hospital-at-home-qms.md) — the Orcanos experience behind the QMS extension.
- [2025-01-16 SDK binary hardening](2025-01-16-ccf-sdk-binary-hardening.md) — the device-side security engineering; distinct work, and **not** what the Cyber Security meeting was about.
- [2025-05-23 mentorship and the Principal Engineer goal](2025-05-23-mentorship-principal-engineer-goal.md) — Tim Wodarski, the mentor who opened the door to this meeting.
- [2025-01-10 compliance-vehicle pushback](2025-01-10-pii-obfuscation-pushback-compliance-vehicle.md) — the same governance instinct applied to log lines.

## Record history

- 2026-09-20: created from the owner's presentation deck and meeting invitation. **This entry corrects an ingest error made on 2026-09-19**, when the Cyber Security presentation was attached to the SDK binary-hardening entry on the assumption that "infosec applicability" referred to the device SDK. It did not — the talk was about this framework, and the security entry has been corrected and renamed.
- 2026-09-24: reciprocal *Related* link to an entry created the same day.
