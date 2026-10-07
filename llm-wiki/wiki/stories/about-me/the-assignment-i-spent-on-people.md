---
cluster: about-me
fits: [leadership, principal, mentoring, quality, defence]
status: draft
runtime: "100 s spoken in full, 45 s without the optional lines"
---

# I learned the test framework in two days, so I spent the assignment growing the people around it

## Why I still care

The owner, 2026-09-13: *"Robot Framework was not a growth item. I mastered it in a couple of days."* What made the period worth having was choosing, deliberately, what he would build himself, what he would guide others to do, and what he would guide them *not* to do — and wanting the expert role to end up with someone else. He was learning to encourage that rather than absorb it. Under it sits the thing he minds most about how engineers grow: *"curiosity followed at an early age is what made engineers like me who we are."*

**The cue:** the guiding questions he wrote out before going to the colleague stuck on the message-broker test — had he run the pause test, what else had he tried. That page of questions is the scene.

## Register

Best Buy Health, 2024: ownership and economy. He says "I decided" plainly. The assignment arrived from above and the story does not argue with it; it says what he made of it. See [voice and prominence](../../workflows/voice-and-prominence.md) § *Judgment over throughput*: the refusal in this period is told as what he protected, and only if asked.

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | A time an assignment was not aimed at his growth, and what he did with it |
| 1 | Hook | Learned the framework in two days |
| 2 | Stakes | Test automation for an emergency-response wearable, built largely by junior and QA engineers |
| 3 | Complication | The hard tests could not pass because the environment, not the test, was broken; some of the engineers were new to all of it |
| 4 | Move | Decided what to build himself and what to guide; worked the hardest failures and handed back diagnoses as questions; introduced pull-request discipline; wanted others to own the expert role |
| 5 | Punchline | The framework took two days; what he is proud of is the engineers' own diagnoses and the pull-request discipline he introduced |
| 6 | Handover | A question about how they grow people through routine work |

## Narrative — rehearse verbatim

*Lines built from the owner's own framing of 2026-09-13 in the source entry; beat 4's second paragraph is agent-drafted from the entry's technical record.*

**0 · Offer**
> I can tell you about a time an assignment was not really aimed at my growth, and what I made of it anyway.

**1 · Hook**
> In 2024 our team was asked to automate device testing with Robot Framework. I learned the framework in a couple of days.
⟨breathe⟩

**2 · Stakes**
> The device is an emergency-response wearable for seniors, so the tests matter. And much of the automation was going to be written by junior engineers and QA engineers, some of them new to all of it.

**3 · Complication**
> The hard part was never the framework. The tests that would not pass were failing because the environment was broken, not the test. And a test suite that nobody trusts is worse than no suite.
*(optional)* One colleague was stuck on a test for message batching. The keyword could not even be found, and underneath that, the connection to the broker from a laptop was too unreliable to base a test on.
⟨breathe⟩

**4 · Move**
> So I decided where my time should go. I would take the failures nobody could get past, and I would guide everyone else rather than do it for them. When I found a diagnosis, I handed it back as questions, so the engineer could reach it himself. And I introduced the team to pull-request discipline.
*(optional)* For the broker test I wrote down, with the evidence, that the approach could not work, and proposed testing in staging instead, where we could first check the brokers were really there.
> I also wanted somebody else to become the Robot expert. I was learning to encourage that, rather than to absorb it.

**5 · Punchline**
> The framework took me two days. What I'm proud of is that the engineers made the diagnoses themselves, and that I got them working through pull requests.
⟨breathe⟩

**6 · Handover**
> How do you grow people on your team through the routine work, rather than only through the big projects?

## If they follow up

- **"Why not just fix it yourself? It would have been faster."** → It would have been faster that week. But the suite was going to be theirs to maintain, and a fix they did not understand would come back to me. I wrote my questions down before I went to a colleague, so the conversation started from what he had already tried.
- **"Did someone take over the expert role?"** → *Owner to answer from memory.* The record shows the intent and the mentoring, not who ended up holding it; say that plainly if unsure.
- **"Was everyone receptive?"** → Not everyone. Some engineers were complying rather than curious, and some were genuinely inexperienced and had little time to follow their curiosity. I could choose what to guide; I could not create the time.
- **"Did you push back on anything?"** → One thing. There was an idea to make unit-test coverage a number that others watch. I argued to keep unit tests as an engineering instrument, because once a number is watched it stops being a tool. Say it as what you protected, in one sentence, and move on.
- **"What about AI — doesn't it make this mentoring unnecessary?"** → His own rule, if it is asked: prompt engineering is easy to learn and easy to master; building good software is far more multi-dimensional. So the mentoring problem moved; it did not go away.
- **Defence listener** → This is disciplined initiative inside someone else's intent: the assignment was theirs, the way to make it worth having was his. Let them name it; do not recite doctrine.

## Proof

The owner's Trello device-programme board, *R5.5 Automation* list, July 2024 to January 2025: the broker investigation, the drafted questions to the colleague, the token-investigation checklists and the code-review notes. All private; nothing here is public.

## Know it — what stays with me

- The automation was a top-down mandate, and it came with an attempt to make unit-test coverage an externally observed metric. His objection, verbatim from the entry: it takes unit tests out of his toolbox. The pushback is on record as an argument, not as a settled outcome.
- He recorded at the time that the development goal lacked a challenge, and named the challenging alternatives: SDK innovation or becoming an embedded Rust expert.
- He considers his own boards, not the employer's tracker, the real record of this period — a statement about the tooling, never about the people.
- Technical depth if asked: the missing library decorator; the broker's disconnect return code over VPN; the OAuth bearer-token investigation he worked from the specification; moving fixed timeouts to framework-native timing; proposing CI access so an AI coding agent could open pull requests against the automation repository.

## Sources

- [2024-12-31 test automation turned into a mentorship practice](../../../raw/brag/2024-12-31-device-test-automation-robot-framework.md)
- [2026-10-02 autonomy and communicated outcomes](../../../raw/brag/2026-10-02-autonomy-and-communicated-outcomes.md) — the practice this story shows.

## Related stories

- [I taught people to ask where the ninety-fifth percentile is](percentiles-not-averages.md) — the other "grew someone" story: a way of thinking, where this one is a way of working.
- [I built the hand-rolled version in 2005](../concurrency/lowest-level-reflexes.md) — the same habit of handing the diagnosis over so others can act on it, applied to a manufacturer's engineers.
- [I presented our monitors and caught a misbehaving device in front of the room](showing-the-monitors.md) — the companion: there the result is made known, here it is handed on.
