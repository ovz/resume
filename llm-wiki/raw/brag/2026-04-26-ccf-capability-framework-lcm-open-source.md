---
title: "Designed and delivered the CCF capability/configuration framework, lifecycle management, and open-source enablement for embedded PERS SDKs"
date: "2026-04-01 to 2026-06 (milestone 2026-04-26)"
thread: FW
domains:
  - "architecture and API design"
  - "embedded and safety-critical devices"
  - "operational excellence and observability"
  - "open source"
context: "Best Buy Health, SDK C libraries for Personal Emergency Response System (PERS) devices, multiple device SKUs"
sensitivity: private-repo
resume-worthy: yes
---

# Designed and delivered the CCF capability/configuration framework, lifecycle management, and open-source enablement for embedded PERS SDKs

## What I did

Led the design and delivery of CCF — the Capability and Configuration Framework — for the SDK C libraries that run on PERS devices. The goal was to standardize capability management, lifecycle control (LCM), and observability across device SKUs, and to make the codebase fit for open-source contribution and broader ecosystem adoption.

- Defined and implemented a reusable capability and configuration framework for embedded C SDKs, supporting dependency injection, hierarchical state machines, and robust lifecycle management.
- Developed a logging framework aligned with CCF, giving consistent, structured logs across all supported devices.
- Integrated LCM patterns into the framework so that initialization, teardown, and error recovery are predictable for every capability.
- Modularized and documented the framework to enable open-source release and external contribution: clear API boundaries and contribution guidelines.

Before CCF, device SDKs handled capabilities, dependencies, and lifecycle events ad hoc, producing inconsistent behaviour and maintenance burden; the lack of standardized logging and state-machine patterns made debugging and cross-device analysis hard; and inconsistent frameworks and documentation kept external contributors away.

**Outward alias.** "CCF" and "Capability and Configuration Framework" are the internal names. Every outward surface says **component framework** (in embedded C, across device SKUs) — see [sensitivity tiers](../../wiki/workflows/sensitivity-tiers.md) § *Public aliases for internal names*. The name sounds generic enough to defend; the point is that it is the team's own name, and a good steward of the employer's information does not publish it.

## Grounded in the source, 2026-09-19

A direct study of four retained working copies of the framework and its first capability SDK added the following, and corrected one thing this entry had wrong.

**"LCM" means two different things, and this entry originally conflated them.** As written above, LCM meant *lifecycle management* — the initialization, teardown and error-recovery discipline the framework provides. But the repositories also depend on **LCM, Lightweight Communications and Marshalling** (<https://github.com/lcm-proj/lcm>), the open-source publish/subscribe messaging library from the robotics world, pinned to its public v1.5.0 release and used as the actual inter-process transport between the company's application and the manufacturer's service. Both are real; they are unrelated; and the messaging library is the one with outward keyword value. The separate record of that work is [2025-01-16 phone capability SDK on R5 hardware](2025-01-16-ccfphone-r5-device-lcm-odm-integration.md). This entry's filename retains the `lcm` token for link stability.

**The hierarchical state machine is hand-built in ANSI C, and its design is specific.** Each state is a function handling events; a state optionally names a super-state function, and when it does not, the machine degrades cleanly to a flat state machine. Transitions raise explicit super-state entry and exit phases carrying the triggering event, so a super-state can act on — or itself redirect — a transition through it. A re-entrancy flag rejects recursive dispatch with its own error code rather than corrupting the machine, and the header documents the single-threaded assumption together with the Active Object pattern as the way to run several machines concurrently. Event codes are 16-bit with a reserved range below user events, and the whole surface returns a single error enumeration covering argument validation, dispatch, transition and logging failures.

**Structured logging is JSON built on a vendored cJSON**, with the framework version emitted in its own informational record — so a log stream identifies the code that produced it.

**The written C style encodes defenses**, not preferences: comparisons ordered so an accidental assignment fails to compile, a zero-terminated-string convention, no relative include paths, and explicit rules for executable lifecycle and memory footprint.

**Dating discrepancy, unresolved — for the owner.** The repository evidence places the framework's initial commit in **May 2024**, its cJSON-based logging in June 2024, the state-machine work in July–August 2024, and the first capability SDK running on R5 hardware in **January 2025**. This entry is dated 2026-04 to 2026-06, from an owner-supplied write-up dated 2026-04-26. Either the 2026 dates describe a distinct later phase — plausibly the open-source enablement and contribution-guideline work, which the retained copies do not cover — or this entry's date is wrong. **The date has deliberately not been changed**; the owner should settle it. Nothing above depends on the answer.

## From the framework specification, 2026-09-19

The owner supplied the governing Confluence design page. It corrects one fact in this entry and adds the reasoning behind the framework's contents.

**Correction — what CCF stands for.** This entry's title and opening call it the *Capability and Configuration Framework*. The specification states it plainly: **CCF stands for "Capability ansi C Framework"**. The original reading is left above so the record shows what was believed; the specification governs. The outward alias is unaffected — every public surface still says *component framework* — and the alias table has been corrected to match.

**Why a framework at all.** Capability libraries share a large amount of common functionality, and the document anticipates needing *significantly different versions of the same capability library as platforms change*. The framework exists to make that easier for in-house engineers **and** for third-party manufacturers — the page names Wistron, Borqs and TCL — which is why the design treats an external vendor as a first-class consumer rather than an afterthought.

**The catalogue of reusable pieces, each with its reason.**

| Piece | The reasoning recorded for it |
|---|---|
| **Memory pool** | A no-dynamic-allocation requirement makes a reusable pool the way to keep memory management straightforward for SDK and manufacturer code alike. The page says C++17 polymorphic memory resources should be studied *for ideas about industry-standard memory management* — borrowing a pattern from modern C++ into an ANSI C design. |
| **Logging** | All log records should be mandated through the framework, with the trade-off named rather than hidden: doing so creates a dependency on the platform's own logging API. |
| **Wakelocks** | The sharpest observation on the page. Wakelock handling is simple, *and manufacturer misuse of it is a known source of defects* — so the SDK should take wakelock management over and guarantee the device is awake when it must be. Wakelocks are called out as fundamental to location and audio, the two subsystems the owner has the deepest record in. |
| **IPC** | Future devices should pass opaque variable-length binary buffers instead of a D-Bus specification, with Qualcomm's QMI use of type-length-value cited as the more universal precedent. |
| **State machine** | A finite state machine is named as the natural representation of most embedded application logic, with the R5 voice-call FSM as the worked example and a shared library as its future home. |

**Why hierarchical, stated as an argument rather than a taste.** Experience on R5 and earlier devices showed a flat state machine to be inadequate: the number of scenarios a personal-emergency device must handle makes flat states grow **exponentially**. The page also concedes the cost — hierarchical machines written by hand demand more convention and discipline — which is precisely what the framework's style rules and its dispatch, transition and phase model were then built to supply.

**A build-versus-buy decision with a real number.** The page evaluates **QP/C**, a commercial real-time embedded framework that combines Active Objects with hierarchical state machines, and records what adopting it would actually cost: the vendor's publicly listed product-line licence of roughly eighteen thousand dollars, *plus* the team learning the framework and running a proof of concept. The conclusion is that further analysis would be needed to justify it. The retained source shows what happened next — the hierarchical state machine was written in-house in ANSI C, with its own tests. Evaluating a mature commercial framework, pricing it, and then building the narrower thing the product actually needed is the decision, not an accident of budget.

**Active Objects as the concurrency model.** Device components are described as active objects, each running an event-driven state machine, with the messaging library proposed as the transport for their events — which is why the shipped header's threading note points at the Active Object pattern.

**The messaging-library case, in full.** The page argues for LCM on four grounds: a simple publish/subscribe model; a track record in robotics and other performance-critical environments, citing the MIT paper behind it; **recordable and replayable messages** (emphasized in the original); and portability to lower-capability platforms without UDP. It goes further than the transport question — it proposes that the existing Boost signal buses on the current and previous device generations could be rewritten on it *without significant loss of performance*, keeping the existing signal nomenclature while eliminating a tedious hand-written marshaling layer and obviating the D-Bus specifications altogether.

**An on-device validation suite as a framework obligation.** The framework is required to support a test suite that an integration-and-validation executable can run **on the device**, to validate firmware automatically and help the manufacturer fix issues — turning "is the ODM's build correct?" into something a program answers rather than an exchange of emails.

**Packaging points back at his own prior work.** The page notes the existing JFrog Artifactory instance and directs the reader to the earlier Conan package-based binaries flow — the work recorded in the 2022 entry — as the basis to build on.

## Why it matters

- **Cross-device consistency:** a single extensible framework for capability management enables rapid onboarding of new device SKUs and cuts code duplication.
- **Improved observability:** standardized logging and state-machine patterns improve diagnosability and shorten time-to-resolution for cross-device issues — extending the fleet observability practice down into the firmware itself (see *Related*).
- **Ecosystem growth:** lower barriers to open-source adoption and contribution widen the developer base and speed innovation.
- **Lifecycle reliability:** predictable LCM patterns reduce lifecycle-related bugs and improve stability across all supported devices.

Adoption metrics (device SKUs onboarded, external contributions received, qualitative developer feedback) are pending.

## Skills demonstrated

Embedded C framework and API design, dependency injection and hierarchical state machines in C, lifecycle management, structured logging design, modularization for open source, technical documentation and contribution-guideline authoring, technical leadership across device SKUs.

## Evidence

Internal design pages for the CCF framework and for logging in CCF; framework code repositories; open-source enablement and contribution guidelines published with the milestone release.

The governing design page — the internal Confluence article *CCF Framework for SDK C Libraries for PERS devices* — was supplied by the owner on 2026-09-19 and is the source for the section above. Its internal wiki, repository, board and ticket URLs are deliberately not reproduced here. QP/C and its licence pricing are the vendor's own public information.

## Related

- [2023-12-21-device-health-observability-architecture](2023-12-21-device-health-observability-architecture.md) — *maintained practice:* the agentless, telemetry-contract approach to device health defined in 2023; CCF's structured logging is the firmware-side realization of the same principle.
- [2024-01-20-errorsummary-json-schema-datadog-limitation](2024-01-20-errorsummary-json-schema-datadog-limitation.md) — earlier lesson that log/telemetry shape must be designed for the consumer; informs the structured-logging design here.
- [2026-09-01-r5-beacon-tracking-fota-persistence](2026-09-01-r5-beacon-tracking-fota-persistence.md) — same device programme and period; applies lifecycle and error-handling discipline to a specific R5 subsystem (thematic link, not a claimed dependency).
- [2026-05-26-ai-adoption-agentic-engineering-choreographer](2026-05-26-ai-adoption-agentic-engineering-choreographer.md) — concurrent enablement work sharing the same lever: reusable framework plus documentation and contribution guidelines to lower onboarding friction.
- [2025-08-30-cross-platform-sdk-modularization-pers-devices](2025-08-30-cross-platform-sdk-modularization-pers-devices.md) — earlier cross-platform SDK requirements and core-versus-adapter modularization that established the architectural foundation for this later component-framework work.
- [2025-01-16-ccfphone-r5-device-lcm-odm-integration](2025-01-16-ccfphone-r5-device-lcm-odm-integration.md) — the first capability SDK built on this framework, taken to real R5 hardware over the LCM messaging library.
- [2025-01-16-ccf-sdk-security-hardening-infosec-presentation](2025-01-16-ccf-sdk-security-hardening-infosec-presentation.md) — the security properties of the binaries this framework produces, and the presentation that carried them to the Cyber Security organization.
- [2024-10-18-copilot-embedded-c-sdk-practice](2024-10-18-copilot-embedded-c-sdk-practice.md) — the AI-assisted engineering practice written into this framework's own repository.

## Record history

- 2026-09-08: created from an owner-supplied brag write-up dated 2026-04-26
- 2026-09-16: added *Outward alias* — the internal name stays here; outward surfaces use "component framework".
- 2026-09-19: linked the earlier cross-platform SDK modularization entry, which records the requirements and boundaries that preceded CCF.
- 2026-09-19: added *Grounded in the source* from a direct study of four retained working copies — the two meanings of "LCM" separated, the state machine's concrete design recorded, and a dating discrepancy raised for the owner without altering the entry's date.
- 2026-09-19: added *From the framework specification* after the owner supplied the governing Confluence design page. **Corrected what CCF stands for** — "Capability ansi C Framework", not "Capability and Configuration Framework" — and recorded the reusable-component catalogue, the wakelock-ownership argument, the exponential-growth case for hierarchical state machines, the QP/C build-versus-buy evaluation, the full messaging-library case, and the on-device validation-suite requirement.
