---
title: "Wrote the team's AI-assisted engineering practice for an embedded C SDK, including machine-readable code-style instructions"
date: "2024-06 to 2024-12 (instruction files 2024-10-18)"
thread: AI
domains:
  - "AI-assisted engineering"
  - "embedded and safety-critical devices"
  - "quality and test automation"
context: "Best Buy Health, component framework and phone capability SDK for PERS devices"
sensitivity: private-repo
resume-worthy: yes
---

# Wrote the team's AI-assisted engineering practice for an embedded C SDK, including machine-readable code-style instructions

## What I did

The framework repository's README is not a description of the framework — it is a **practice guide for building embedded C with GitHub Copilot**, written into the repository so it reached everyone who cloned it. It states outright that Copilot was used to build the repository's content, and that generated content is usually preceded by the comments used as prompts. This was 2024, on a safety-adjacent C codebase, while most of the industry was still arguing about whether to allow the tool at all.

**The practices it establishes, each of which is a real position rather than a platitude:**

- **Prompt comments are kept in the source as documentation.** The comment that produced the code stays above the code, so changing the requirement means changing the prompt and regenerating. Misleading or experimental prompts are deleted rather than left to rot. The guide even notes the tell that the two are in sync — Copilot stops offering suggestions when the code already matches the comment.
- **Write the failing unit test first, then let the test drive generation.** The stated reason is empirical rather than doctrinal: unit-test code is far easier for the model to use as a prompt, and a zero-shot correct implementation is often the result. Where code cannot be covered by a test, that has to be documented where a reader of the code will see it.
- **Regenerate when things drift.** Once the prompt and the code diverge, re-invoke the model, then inspect and reconcile the differences — giving the model a chance to reconcile recent changes against the rest of the repository. For a localized mismatch, the guide prescribes selecting the region and using inline chat to make it consistent.
- **A documented model failure mode, with a workaround.** He recorded that Copilot tends to suggest code resembling whatever was most recently typed or generated, in preference to a solution consistent with the rest of the project or simply a better one — and that the practical countermeasure is to find similar existing code and paste it into context first. He also recorded where the behaviour helps: with uniform error handling, the model reliably completes the conditional correctly from context.
- **LLM summarization is for pull requests and code review — with an explicit hallucination check.** The guide tells the reader to use it liberally and then to go back to the original material and confirm nothing invented slipped in.
- **Context management as an engineering constraint on repository design.** The guide observes that codebases beyond a few thousand files are treated as large by workspace indexing, and draws a physical-design conclusion from it: prefer smaller repositories consuming each other through header files. Tooling limits are allowed to inform architecture.

**The part that dates best: he made the code style machine-readable.** In October 2024 he committed editor settings pointing Copilot's code-generation instructions at the repository's own C style guide, with instruction files enabled — so the house rules (the accidental-assignment guard, the string and include conventions, the lifecycle and memory-footprint rules) were fed to the model automatically rather than relying on reviewers to catch violations. He also recorded the honest caveat next to it: the tool follows such guidance only partially and will not follow external links, so it is acceptable to repeat the style rules at the top of implementation files.

That is the same mechanism — a repository-committed instructions file steering an AI assistant — that this resume repository and the wider industry standardized on considerably later.

## Why it matters

- **It is AI adoption as team enablement, not personal productivity.** The artifact is a practice other engineers and vendor contributors inherit by cloning the repository, which is the difference between using a tool well and raising an organization's floor.
- **The observations are empirical and falsifiable.** Recency bias in suggestions, tests as the most effective prompt, the no-suggestion signal, indexing limits — these are things he noticed, wrote down and designed around, not vendor claims repeated.
- **It puts a verifiable 2024 date on AI-assisted engineering** in the record, in embedded C, supporting the resume's "leveraging AI since 2023" claim with something concrete and earlier than the 2026 agentic work.
- **It anticipated where the tooling went.** Committed instruction files, context attachment, AI-written pull-request summaries with a human verification step — all of it became standard practice afterwards.

## The owner's retrospective, in his own words (2026)

From his working notes, on how the skill itself changed:

> "That's why prompt engineer profession was short lived. The challenge to keep LLM in the correct space (single word in the prompt determines success/failure) got solved by the industry in the matter of months. For modern LLMs the skill is to keep model comprehensive, demand top quality, not accept half baked results etc."

He also names the kind of work where the leverage is greatest — code where cleverness is not allowed and irrelevant code is easy to spot, which makes review fast — and observes that experiment tooling which once had to be rationed against his own instinct to eliminate toil is now cheap enough to build properly. He calls the result production-grade internal software in minutes, and frames it as a Jevons-paradox effect rather than a pure saving: comprehensive documentation stopped being an excuse.

## Skills demonstrated

AI-assisted software engineering; prompt engineering and its documented limits; machine-readable coding-standard enforcement; test-first development with generative tooling; technical writing for team enablement; empirical evaluation of developer tooling; repository physical design under tooling constraints.

## Evidence

The framework repository's README in the retained working copies carries the full practice guide. Commit history dates a pull-request-summary reference to June 2024, the code-generation instruction settings to 18 October 2024, and the removal of an experimental prompt from the style guide to the following day; a dedicated branch for the pull-request guidance also exists. The C and C++ style guides referenced by those settings are in the same tree.

## Evidence limitations

- **Authorship of the guide is strongly implied but not separately attested.** The repository is a team repository; the branch naming and the owner's account place this work with him, and no contradicting evidence was found, but no document in this repository states authorship explicitly.
- **No adoption or outcome measurement exists.** There is no record of how many engineers followed the guide, whether the instruction files measurably changed generated code, or any defect or velocity effect. The claim is that the practice was written, committed and configured — not that its benefits were quantified.
- **The retrospective quoted above is 2026 commentary**, not a 2024 observation, and is presented as such.

## Related

- [2026-05-26 AI adoption and agentic engineering](2026-05-26-ai-adoption-agentic-engineering-choreographer.md) — the later, larger AI work; this entry is its documented antecedent, two years earlier and in embedded C.
- [2024-12-31 device test automation and mentorship](2024-12-31-device-test-automation-robot-framework.md) — the same period; there he gave an AI coding agent a route to land pull requests, and named the limits of AI-assisted mentorship.
- [2025-01-16 phone capability SDK on R5 hardware](2025-01-16-ccfphone-r5-device-lcm-odm-integration.md) — the codebase this practice was written for and applied to.
- [2025-01-16 SDK security hardening](2025-01-16-ccf-sdk-security-hardening-infosec-presentation.md) — the defensive style rules that the instruction files fed to the model.
- [2026-04-26 component framework](2026-04-26-ccf-capability-framework-lcm-open-source.md) — the framework whose repository carries the guide.

## Record history

- 2026-09-19: created from a direct study of the retained framework and SDK working copies, with the retrospective drawn from the owner's committed working notes.
