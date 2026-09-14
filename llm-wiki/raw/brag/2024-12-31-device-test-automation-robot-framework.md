---
title: "Turned a top-down test-automation mandate into a mentorship practice, and unblocked the automation nobody could get to pass"
date: "2024-07 to 2025-01"
thread: QA
domains:
  - "leadership, management, hiring"
  - "quality and test automation"
  - "cloud and distributed systems"
  - "AI-assisted engineering (since 2023)"
context: "Best Buy Health, R5 / Lively Mobile+ wearable, QA automation"
sensitivity: private-repo
resume-worthy: maybe
---

# Turned a top-down test-automation mandate into a mentorship practice, and unblocked the automation nobody could get to pass

## What I did

I worked the hard, unglamorous end of the wearable automation suite — the tests that could not be made to pass because the environment, not the test, was broken — and made a point of handing back diagnoses rather than just fixes.

**Diagnosed why the message-broker test could not work, and said so plainly.** A colleague was stuck automating verification that MQTT messages were batched. I reproduced it and found the immediate cause was mechanical — the keyword could not even be found because the library decorator was missing from the class, so no working implementation had been supplied. I then spent a day researching the deeper failure: connecting to the broker from a laptop was disconnecting with a specific return code and would not reconnect, and after investigating the VPN path I concluded the connection was **too unreliable to base a test on**. Recording "this approach cannot work, here is the evidence" is more useful than leaving a flaky test in the suite.

**Proposed a test design that verified the right thing.** Rather than testing against a broker reachable from a laptop, I recommended running a pause-style test *in the staging environment* — first establishing that the brokers we were trying to exercise were actually present and working, and only then checking that devices worked with the same broker. I also identified that a self-contained pause test was itself a good check that the whole stack worked, and was willing to defer the broker test until a better API existed rather than ship something brittle.

**Handled the collaboration deliberately.** I wrote out guiding questions before approaching my colleague — had he run the pause test, what other new steps had he tried — so the conversation started from what had actually been attempted rather than from my conclusions. I passed on a specific candidate fix I had found, and reported honestly when it appeared to have no effect.

**Ran an OAuth token investigation to unblock a whole class of tests.** Automating steps that required action on an internal provisioning system meant obtaining a bearer token. I worked it methodically: tried to capture the token in browser developer tools and found it was not in the trace and strongly suspected it was deliberately obscured; followed a colleague's suggestion that it might be carried in a cookie; checked browser and OS keychain storage; worked through the specification to locate the authorization grant; and asked concrete questions about the flow — where the actual test call originates, whether it is visible client-side, and whether resending a ping and receiving an expired-page response revokes the access token. Read the relevant bearer-token specification directly rather than guessing.

**Debugged the environment, not just the code** — chasing device activation failures in staging across settings persistence, the state database, alternate devices, and the provisioning system simply being offline, so that test failures could be attributed correctly.

**Improved the suite's engineering quality**, including code review of exception handling, moving a fixed timeout out of the test body in favour of framework-native timing, sharing topic constants rather than duplicating them, and chasing down duplicate message reports in logs.

**Pushed automation of the automation.** I proposed configuring CI so an AI coding agent could actually open pull requests against the automation repository — treating the agent as a contributor with a route to land work, rather than a suggestion box — and used AI assistants as an explicit investigative tool during the token work.

## What this was really about — the owner's framing, added 2026-09-13

The technical content above is accurate and it is **not** where the value of this period sits. Set straight, in my own terms:

**Robot Framework was not a growth item.** I mastered it in a couple of days. For an engineer with my experience that is far below what a development goal should be — I said so at the time, recording that the goal was applicable to the work but lacked a challenge, and that the genuinely challenging alternatives were innovation with SDKs or becoming an embedded Rust expert. I also wanted other team members to take over the Robot expert role, and I was learning to encourage that rather than to absorb it.

**The mandate came top-down.** Test automation was not a bet the team placed; it was an instruction, and it arrived with the usual accompaniment — an attempt to make **unit-test coverage an externally observable metric, with increasing coverage as the goal**. I pushed back hard on that, on one specific ground: it takes unit tests out of my toolbox. A number someone else watches stops being an engineering instrument and becomes a thing to satisfy, and I will not give up a tool I rely on to feed a dashboard.

**My own records are the real task tracker.** The employer's issue tracker is shaped by mandates rather than by the work, which is why the durable account of what I actually did in this period lives in my own boards. That is a statement about the tooling, not about the people.

**So I converted the mandate into the growth item it would not otherwise have been: mentorship.** With Robot Framework I found a way to grow as a mentor of junior engineers and QA engineers, and I worked out the tradeoff deliberately — what I build myself, what I guide others to do, and what I guide them *not* to do. I introduced them to **pull-request discipline**, which outlives any framework. The two failure modes I was working with were different and both real:

- Some QA engineers were **not interested**, but had to comply with the mandate. Guidance there is about making compliance produce something worth having.
- Some **genuinely lacked experience**, and the mandate gave them no room for it. This is the part I mind: curiosity followed at an early age is what made engineers like me who we are, and a compliance schedule leaves no time to channel it. You cannot mentor someone into experience they were never given time to acquire.

**On AI and mentorship, since it is the obvious question now.** Modern AI coding makes mentorship considerably less challenging — much of what used to need a person now needs a prompt. But inexperienced people do not master *building good software* through prompts in a few days. **Prompt engineering is easy to learn and easy to master; software is far more multi-dimensional.** That asymmetry is exactly why the mentoring problem did not go away, it moved.

## Why it matters

- **The transferable accomplishment is the mentorship, not the framework.** A top-down mandate with a bad metric attached is the ordinary condition of senior engineering inside a large organization, and the useful skill is converting it into something that develops people — while refusing the part of it that would degrade your own practice. Both halves happened here.
- **Distinguishing a broken test from a broken environment is the core skill in test automation**, and getting it wrong produces a suite nobody trusts. The MQTT conclusion — that the connection path was too unreliable to test through — prevented exactly that.
- **The proposed redesign tests the real property** (do the brokers exist and work in staging, then do devices work with them) rather than the property that happened to be easy to assert.
- **It is mentoring in the useful form:** reproducing a colleague's blocker, finding both the shallow and the deep cause, and returning guiding questions rather than a verdict.
- **The OAuth investigation is protocol-level work** — reading the specification, reasoning about token lifecycle and revocation — not trial and error.
- The AI-agent CI proposal is early, practical thinking about agents as contributors, consistent with the later AI-adoption work.

## Skills demonstrated

Mentoring junior engineers and QA under a compliance mandate; pull-request discipline as a taught practice; deciding what to build versus what to guide; pushing back on a metric that would degrade engineering practice; Robot Framework and keyword-driven test automation; MQTT and message-broker behaviour; OAuth 2.0 bearer tokens and authorization flows; staging-environment debugging; distinguishing environmental from functional failure; peer mentoring and diagnostic handover; CI configuration for AI coding agents; test-suite code quality.

## What was blocked, cut short, or wrong

- **The development goal itself was weak, and I knew it at the time.** Robot Framework took days to master; the challenging alternatives I named — SDK innovation, embedded Rust — were not what the mandate wanted. This period is an example of making something worthwhile out of an assignment that was not aimed at my growth.
- **The push to make unit-test coverage an externally observed metric** was resisted rather than defeated on the record; what I can show is the argument I made and why.
- **The mandate's schedule was the real constraint on the inexperienced engineers**, and I could not change it. I could only choose what to build myself and what to guide them through.
- **Some of the people were complying rather than curious**, which limits how far mentorship can go regardless of how it is done.

## Evidence limitations

The technical detail is fully documented in the owner's own board. The mentorship framing, the coverage-metric pushback and the reasoning about curiosity are the owner's account, recorded 2026-09-13 — contemporaneous notes exist for the weak-development-goal judgement and for the intent to hand the Robot expert role to others, but not for the coverage-metric exchange as a discrete event.

## Evidence

Trello device-programme board, *R5.5 Automation* list (15 cards), 2024-07 through 2025-01, including the broker investigation, the drafted messages to the colleague, the token-investigation checklists and the code-review notes. Repository names, internal wiki links, ticket identifiers and colleague usernames remain in the board archive.

## Related

- [2022-02-18 C++ safety-critical embedded guidelines](2022-02-18-cpp-safety-critical-embedded-guidelines.md) — the earlier engineering-standards work in the same programme.
- [2026-05-26 AI adoption and agentic engineering](2026-05-26-ai-adoption-agentic-engineering-choreographer.md) — where the AI-agent-as-contributor thinking developed further.
- [2025-05-01 R5 device-specific failure investigations](2025-05-01-r5-device-specific-failure-investigations.md) — the same diagnostic approach applied to fleet failures.
- [2025-05-23 mentorship toward Principal](2025-05-23-mentorship-principal-engineer-goal.md) — being mentored, in the same period as mentoring; the two are one practice seen from both ends.
- [2021-06-29 engineering excellency and meeting facilitation](2021-06-29-engineering-excellency-and-meeting-facilitation.md) — the earlier instance of refusing a process that would decay engineering quality, argued systemically rather than personally.

## Record history

- 2026-09-10: created from the Trello device-programme board during the full board ingest.
- 2026-09-13: reframed at the owner's direction. The headline now leads with the mentorship practice rather than the framework; added *What this was really about* (weak development goal, top-down mandate, the unit-test-coverage metric pushback, the build-versus-guide tradeoff, pull-request discipline, the two kinds of unready mentee, and prompt engineering versus software judgement), plus *What was blocked* and *Evidence limitations*. Domains gained leadership. Re-ingested the same day.
