---
title: "Unblocked device test automation across MQTT, OAuth and staging environments, and mentored the engineer who was stuck"
date: "2024-07 to 2025-01"
thread: QA
domains:
  - "quality and test automation"
  - "cloud and distributed systems"
  - "AI-assisted engineering (since 2023)"
context: "Best Buy Health, R5 / Lively Mobile+ wearable, QA automation"
sensitivity: private-repo
resume-worthy: maybe
---

# Unblocked device test automation across MQTT, OAuth and staging environments, and mentored the engineer who was stuck

## What I did

I worked the hard, unglamorous end of the wearable automation suite — the tests that could not be made to pass because the environment, not the test, was broken — and made a point of handing back diagnoses rather than just fixes.

**Diagnosed why the message-broker test could not work, and said so plainly.** A colleague was stuck automating verification that MQTT messages were batched. I reproduced it and found the immediate cause was mechanical — the keyword could not even be found because the library decorator was missing from the class, so no working implementation had been supplied. I then spent a day researching the deeper failure: connecting to the broker from a laptop was disconnecting with a specific return code and would not reconnect, and after investigating the VPN path I concluded the connection was **too unreliable to base a test on**. Recording "this approach cannot work, here is the evidence" is more useful than leaving a flaky test in the suite.

**Proposed a test design that verified the right thing.** Rather than testing against a broker reachable from a laptop, I recommended running a pause-style test *in the staging environment* — first establishing that the brokers we were trying to exercise were actually present and working, and only then checking that devices worked with the same broker. I also identified that a self-contained pause test was itself a good check that the whole stack worked, and was willing to defer the broker test until a better API existed rather than ship something brittle.

**Handled the collaboration deliberately.** I wrote out guiding questions before approaching my colleague — had he run the pause test, what other new steps had he tried — so the conversation started from what had actually been attempted rather than from my conclusions. I passed on a specific candidate fix I had found, and reported honestly when it appeared to have no effect.

**Ran an OAuth token investigation to unblock a whole class of tests.** Automating steps that required action on an internal provisioning system meant obtaining a bearer token. I worked it methodically: tried to capture the token in browser developer tools and found it was not in the trace and strongly suspected it was deliberately obscured; followed a colleague's suggestion that it might be carried in a cookie; checked browser and OS keychain storage; worked through the specification to locate the authorization grant; and asked concrete questions about the flow — where the actual test call originates, whether it is visible client-side, and whether resending a ping and receiving an expired-page response revokes the access token. Read the relevant bearer-token specification directly rather than guessing.

**Debugged the environment, not just the code** — chasing device activation failures in staging across settings persistence, the state database, alternate devices, and the provisioning system simply being offline, so that test failures could be attributed correctly.

**Improved the suite's engineering quality**, including code review of exception handling, moving a fixed timeout out of the test body in favour of framework-native timing, sharing topic constants rather than duplicating them, and chasing down duplicate message reports in logs.

**Pushed automation of the automation.** I proposed configuring CI so an AI coding agent could actually open pull requests against the automation repository — treating the agent as a contributor with a route to land work, rather than a suggestion box — and used AI assistants as an explicit investigative tool during the token work.

## Why it matters

- **Distinguishing a broken test from a broken environment is the core skill in test automation**, and getting it wrong produces a suite nobody trusts. The MQTT conclusion — that the connection path was too unreliable to test through — prevented exactly that.
- **The proposed redesign tests the real property** (do the brokers exist and work in staging, then do devices work with them) rather than the property that happened to be easy to assert.
- **It is mentoring in the useful form:** reproducing a colleague's blocker, finding both the shallow and the deep cause, and returning guiding questions rather than a verdict.
- **The OAuth investigation is protocol-level work** — reading the specification, reasoning about token lifecycle and revocation — not trial and error.
- The AI-agent CI proposal is early, practical thinking about agents as contributors, consistent with the later AI-adoption work.

## Skills demonstrated

Robot Framework and keyword-driven test automation; MQTT and message-broker behaviour; OAuth 2.0 bearer tokens and authorization flows; staging-environment debugging; distinguishing environmental from functional failure; peer mentoring and diagnostic handover; CI configuration for AI coding agents; test-suite code quality.

## Evidence

Trello device-programme board, *R5.5 Automation* list (15 cards), 2024-07 through 2025-01, including the broker investigation, the drafted messages to the colleague, the token-investigation checklists and the code-review notes. Repository names, internal wiki links, ticket identifiers and colleague usernames remain in the board archive.

## Related

- [2022-02-18 C++ safety-critical embedded guidelines](2022-02-18-cpp-safety-critical-embedded-guidelines.md) — the earlier engineering-standards work in the same programme.
- [2026-05-26 AI adoption and agentic engineering](2026-05-26-ai-adoption-agentic-engineering-choreographer.md) — where the AI-agent-as-contributor thinking developed further.
- [2025-05-01 R5 device-specific failure investigations](2025-05-01-r5-device-specific-failure-investigations.md) — the same diagnostic approach applied to fleet failures.

## Record history

- 2026-09-10: created from the Trello device-programme board during the full board ingest.
