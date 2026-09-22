---
title: "Carried unit-test discipline across device firmware, SDK, sensor and smartwatch repositories"
date: "2021-10 to 2026-05 (source-grounded scan range)"
thread: QA
domains:
  - "quality and test automation"
  - "embedded and safety-critical devices"
  - "build, release and CI/CD"
context: "Best Buy Health and GreatCall device software repositories"
sensitivity: private-repo
resume-worthy: yes
---

# Carried unit-test discipline across device firmware, SDK, sensor and smartwatch repositories

## What I did

A repo-wide scan of local device-software checkouts shows that my unit-testing contribution was not a single episode. R5 device-test stability is the largest and most nuanced part, and it remains its own entry, but the same practice appears across earlier and newer repositories: making off-target tests run reliably, setting up gtest in reusable templates, carrying CI test runners into microcontroller-adjacent work, and building a smartwatch proof-of-concept around a broad unit-test surface.

The source-grounded categories are:

- **R4 device-core devcontainer stabilization.** In 2022 I worked through the older device core so unit tests passed in a devcontainer, including timeouts, platform-condition fixes and environment-specific assertions. This is the predecessor to the later R5 Ubuntu/Docker stabilization work.
- **Package-template gtest and Conan integration.** In 2022 I used the shared package-template work to prove that gtest could be pulled into the package/build path and that both static and dynamic consumers could be exercised through tests, so the template was not only a build artifact but a testable component boundary.
- **R5 firmware-core stability and behavioural tests.** The detailed record lives in [the R5 test-stability entry](2024-01-01-r5-ci-test-stability-monitoring-hygiene.md): CI runner stabilization, brittle-test quarantine, real SQLite fixtures, working-directory checks, sandbox setup, repeat-run stress scripts and behavioural unit tests.
- **Robot/device automation and mentorship.** The detailed record lives in [the Robot automation entry](2024-12-31-device-test-automation-robot-framework.md): debugging broken environments, refusing brittle tests, mentoring QA and junior engineers, and pushing back on coverage-as-dashboard behaviour.
- **Component-framework and phone SDK tests.** The detailed record lives in [the Copilot embedded-C practice](2024-10-18-copilot-embedded-c-sdk-practice.md) and [phone capability SDK](2025-01-16-ccfphone-r5-device-lcm-odm-integration.md): unit tests as an AI/design interface, generated corner cases kept as reviewable tests, and GoogleTest-style integration tests over real message channels.
- **Sensor co-processor gtest CI.** In 2026 I touched the low-level sensor firmware support surface around gtest scripts and CI workflows, including dockerized gtest execution and artifact-handling fixes. This is smaller than the R5 core work but shows the same instinct carried down to the microcontroller-adjacent layer.
- **Smartwatch proof-of-concept unit-test breadth.** In 2026 I built or expanded Kotlin unit tests across a smartwatch proof of concept: feature flags, permissions, fall detection, reboot handling, complications, medication flows, heart-rate classification, blood-oxygen pipeline behaviour, navigation and view-model logic. The pattern is test-first domain modelling: isolate the device behaviour and edge cases in ordinary unit tests before relying on emulator or on-watch validation.

## Why it matters

This is a through-line rather than a one-off skill. Across generations and stacks, I keep turning hard-to-test device behaviour into deterministic, reviewable tests: first by making the build/test environment reliable, then by naming or quarantining false-positive sources, then by moving behaviour into unit-testable seams.

It also shows judgement about what a test can and cannot prove. A unit test is strongest when it captures domain logic, failure-mode handling or a contract boundary. It is weaker when it pretends an unreliable external environment is a stable dependency. The record contains both moves: add tests where they make behaviour cheaper to reason about, and refuse or quarantine tests that would make CI less trustworthy.

## Skills demonstrated

Unit-test architecture across C++, C, Robot Framework and Kotlin; gtest and GoogleTest-style harnesses; Kotlin/JVM test design; CI test-runner design; devcontainer and Docker test stabilization; fixture and sandbox design; package-template testing; behavioural testing of embedded and wearable-device domains; testability judgement; mentoring and review of test code.

## Evidence

Read-only scan of local Git histories under the owner's development workspace on 2026-09-22, filtered to the owner's author identities and test-related commits. The scan covered device core, package template, Robot automation, component framework, phone capability SDK, sensor co-processor and smartwatch proof-of-concept repositories. Exact repository paths, branch names, commit hashes, test names and internal identifiers are retained in the maintainer scratch evidence map rather than copied here.

## Evidence limitations

The scan proves authored contributions and recurring categories; it does not prove adoption, test pass rates, flakiness reduction percentages, or production outcomes. Some checkouts had pre-existing dirty worktrees and some commits are WIP or merge commits. The smartwatch proof-of-concept work is especially broad and recent; it supports unit-test breadth and domain-modelling practice, not a shipped watch product.

## What was blocked, cut short, or wrong

Unit tests cannot substitute for hardware, emulator or fleet validation. The point of this record is narrower: making the logic and failure modes cheap to exercise before they reach those expensive layers, and keeping CI from being polluted by tests whose dependencies are not under test control.

## Related

- [2024-01-01 R5 test stability](2024-01-01-r5-ci-test-stability-monitoring-hygiene.md) — the largest and most nuanced slice of the unit-testing record.
- [2024-12-31 Robot automation and mentorship](2024-12-31-device-test-automation-robot-framework.md) — device-level automation, environment diagnosis and mentorship under a test-automation mandate.
- [2024-10-18 Copilot embedded-C practice](2024-10-18-copilot-embedded-c-sdk-practice.md) — unit tests as prompt and design surface in the component framework.
- [2025-01-16 phone capability SDK](2025-01-16-ccfphone-r5-device-lcm-odm-integration.md) — GoogleTest-style integration tests over live message channels.
- [2022-04-06 Conan package and cross-build strategy](2022-04-06-conan-package-management-embedded-cross-build.md) — package-template and cross-build work this entry extends with its testability evidence.

## Record history

- 2026-09-22: created from the comprehensive `~/ghe` unit-testing audit after the owner clarified that Robot, CCF and newer-repo unit-testing accomplishments are still brag material, while R5 remains the largest and most nuanced slice.
