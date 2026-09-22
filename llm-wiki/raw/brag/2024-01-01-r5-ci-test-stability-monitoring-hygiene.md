---
title: "Reduced R5 device-test flakiness through CI, fixture and working-directory stabilization"
date: "2022-08 to 2026-09 (source-grounded range; precise impact milestone pending CI-history review)"
thread: QA
domains:
  - "quality and test automation"
  - "build, release and CI/CD"
  - "operational excellence and observability"
context: "Best Buy Health, R5 firmware core and GitHub Actions CI"
sensitivity: private-repo
resume-worthy: yes
---

# Reduced R5 device-test flakiness through CI, fixture and working-directory stabilization

## What I did

The R5 firmware core was built and validated through a GitHub Actions pipeline covering unit and integration tests, static analysis and other checks on every change. Over time, flaky timing-sensitive tests, Ubuntu-runner differences and Datadog, logging and lint warnings had made CI noisy enough that developers treated failures as possible false positives, re-ran jobs and sometimes ignored failures they believed were unrelated.

Over several years, with concentrated fixes in 2023–2026, I treated that as CI and test-infrastructure technical debt rather than as an accepted background condition:

- Investigated long-standing intermittent failures in the R5 core test suite, especially failures that appeared sporadically in GitHub Actions.
- Replaced brittle sleep-based assumptions where possible with explicit synchronization points and deterministic conditions.
- Adjusted timeouts and retry logic to reflect realistic execution times without masking real failures.
- Isolated environment-specific causes, including Ubuntu runner behaviour, locale and timezone quirks, and filesystem timing, then updated tests or helpers for consistent behaviour across environments.
- Reduced CI log spam and irrelevant Datadog and monitoring warnings; tightened logging so benign expected conditions were not repeatedly reported as warnings or errors.
- Reviewed GitHub Actions configuration for deterministic ordering where needed, job isolation against state leakage, judicious retries and actionable failure output.

## R5 device-test stability scan, 2026-09-22

A focused read-only Git-history scan of the R5 device firmware checkout narrowed this entry to the device-test stability work itself. Robot, component-framework and phone-capability SDK accomplishments are accepted elsewhere in the record; this section is only about reducing flakiness in R5 off-target device tests and CI. The exact commit hashes, internal paths and source-repository details are retained in the maintainer scratch evidence map, not copied here. The public-safe categories are:

- **Ubuntu CI runner and `ctest` stabilization.** Made the Linux CI gate more trustworthy by treating test invocation, runner resource limits, deterministic ordering, working directory and failure propagation as engineering problems, not as incidental workflow details.
- **Quarantine of known-brittle tests.** Disabled or gated tests that were explicitly identified as brittle or randomly failing in the Ubuntu Docker path, so the CI signal stopped being poisoned by known false positives while the failure mode stayed visible in history.
- **Real SQLite `state.db` fixture reliability.** Centralized setup and teardown for tests that require a real SQLite state database: remove stale database state, write the migration script into the test temp area, open the database against that migration path, verify it opened, and clean up both database and migration script afterwards.
- **Working-directory and sandbox checks.** Added explicit test-environment checks and sandbox-directory setup so tests fail immediately with actionable context when run from the wrong directory or without expected temporary paths, instead of cascading into confusing file-not-found or path-dependent failures.
- **Direct flaky-test and brittle-test repair.** Repaired individual tests whose failure modes involved HTTP behaviour, command callbacks, relative paths, zero-battery shutdown handling, update/download failure paths, asynchronous futures, filesystem assumptions and runner constraints.
- **Behavioural unit tests as executable specifications.** Used unit tests to encode embedded-device behaviours — battery and charger state, LEDs, calls, location errors and beacon tracking — so implementation changes could be reviewed against executable examples rather than prose alone.
- **Test readability and maintainability cleanup.** Replaced magic values with named constants, normalized platform conditionals, cleaned naming and reduced incidental complexity so failures were easier to understand.
- **Repeat-run stress harnesses.** Added scripts that intentionally run suites repeatedly and write pass/fail summaries and per-run logs, turning flake discovery into a deliberate workflow rather than waiting for accidental CI failures.
- **Timeout and asynchronous-boundary discipline.** Made asynchronous progress observable and bounded in tests through explicit wait helpers, timeout handling, promise/future reset and callback-state cleanup.

## Why it matters

The goal was to make a red build mean a real problem again without weakening coverage or suppressing real alerts. The owner reports that the resulting pipeline and test surface were more deterministic: developers spent less time re-running jobs, logs made root causes easier to identify, and new flakiness could be treated as a regression instead of accepted background noise.

This was incremental quality work rather than a one-off cleanup. The accumulated fixes made it practical to add tests without overwhelming developers with spurious failures and restored CI as a useful gate in the firmware workflow.

## Skills demonstrated

Flaky-test diagnosis, deterministic test design, real SQLite fixture design, working-directory validation, sandbox setup, synchronization and timeout reasoning, cross-platform CI debugging, GitHub Actions workflow design, test-environment isolation, behavioural test design, logging hygiene, monitoring signal design, and incremental technical-debt reduction.

## Evidence

The technical evidence is a focused author-scoped scan of the accessible local R5 firmware checkout. The scan found repeated contributions to test execution, CI, fixtures, working-directory validation, state-database setup/teardown, sandbox setup, brittle-test quarantine, stress-test scripts, timeouts and individual flaky-test repair. Exact source identifiers and internal paths are retained offline.

## Evidence limitations

The technical pattern is now source-grounded by commit history, but the operational outcome remains bounded. No before-and-after flakiness rate, rerun count, developer-hours estimate or complete failure taxonomy is currently recorded. The entry therefore does not claim a measured percentage improvement, a specific number of fixed tests, or that every intermittent failure was eliminated.

The precise impact milestone remains pending. The strongest visible stabilization cluster is in 2023, with later related work in 2024–2026; a final impact date should be selected from the merge date of the most significant CI or test-stability cluster, not inferred from this scan alone.

## What was blocked, cut short, or wrong

Several source commits are WIP, merge or troubleshooting snapshots. Some changes deliberately disable or gate brittle tests in a particular environment; this entry treats that as signal hygiene and quarantine, not as a claim that coverage increased in those moments. The operational result is recorded as an owner-reported improvement in trust and signal-to-noise, not as a reconstructed CI metric.

## Related

- [2024-12-31-device-test-automation-robot-framework](2024-12-31-device-test-automation-robot-framework.md) — related test-automation work distinguishing broken tests from broken environments; this entry covers the firmware-core CI gate and its accumulated stability cleanup.
- [2023-12-05-operational-excellence-launch-readiness](2023-12-05-operational-excellence-launch-readiness.md) — related quality judgement about choosing controls that expose real system failures rather than satisfying a noisy process.
- [2024-03-01-r5-fleet-observability-analytics-datadog](2024-03-01-r5-fleet-observability-analytics-datadog.md) — related R5 monitoring work; this entry concerns CI and engineering signal hygiene rather than fleet observability.

## Record history

- 2026-09-21: created from the owner's supplied CI-stability and monitoring-hygiene note; precise impact date left pending because the referenced R5 repository was unavailable for Git-history review.
- 2026-09-22: re-grounded against five years of accessible Git history across R5 firmware, test automation, component-framework and phone-capability SDK checkouts; widened the entry from CI stability to the broader unit-test-quality record while keeping internal commit/path details in scratch only.
- 2026-09-22: narrowed the entry back to R5 device-test stability after the owner clarified that Robot, CCF and newer-repo accomplishments are accepted but separate. Added the R5-specific mechanisms: brittle-test quarantine, real SQLite `state.db` fixture setup/teardown, working-directory validation, sandbox setup and stress-test scripts.
