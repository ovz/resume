---
title: "Designed and delivered CCF — the Capability C Framework — with lifecycle management and open-source enablement for embedded PERS SDKs"
date: "2024-05 to 2025-01 (framework initial commit 2024-05-08; first capability SDK on R5 hardware 2025-01-16)"
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

# Designed and delivered CCF — the Capability C Framework — with lifecycle management and open-source enablement for embedded PERS SDKs

## What I did

Led the design and delivery of CCF — the **Capability C Framework** — for the SDK C libraries that run on PERS devices. The goal was to standardize capability management, lifecycle management, and observability across device SKUs, and to make the codebase fit for open-source contribution and broader ecosystem adoption.

- Defined and implemented a reusable capability and configuration framework for embedded C SDKs, supporting dependency injection, hierarchical state machines, and robust lifecycle management.
- Developed a logging framework aligned with CCF, giving consistent, structured logs across all supported devices.
- Integrated lifecycle-management patterns into the framework so that initialization, teardown, and error recovery are predictable for every capability.
- Modularized and documented the framework to enable open-source release and external contribution: clear API boundaries and contribution guidelines.

Before CCF, device SDKs handled capabilities, dependencies, and lifecycle events ad hoc, producing inconsistent behaviour and maintenance burden; the lack of standardized logging and state-machine patterns made debugging and cross-device analysis hard; and inconsistent frameworks and documentation kept external contributors away.

**Outward alias.** "CCF" and "Capability and Configuration Framework" are the internal names. Every outward surface says **component framework** (in embedded C, across device SKUs) — see [sensitivity tiers](../../wiki/workflows/sensitivity-tiers.md) § *Public aliases for internal names*. The name sounds generic enough to defend; the point is that it is the team's own name, and a good steward of the employer's information does not publish it.

## Grounded in the source, 2026-09-19

A direct study of four retained working copies of the framework and its first capability SDK added the following, and corrected one thing this entry had wrong.

**"LCM" in this record means Lightweight Communications and Marshalling, and never lifecycle management.** An earlier version of this entry glossed LCM as "lifecycle control". **That was simply wrong**, and the owner has confirmed it: in the context of CCF and everything derived from it, LCM is always [Lightweight Communications and Marshalling](https://github.com/lcm-proj/lcm) — the open-source publish/subscribe messaging library from the robotics world, pinned to its public v1.5.0 release and used as the real inter-process transport between the company's application and the manufacturer's service. The framework genuinely does provide lifecycle management; that capability simply is not called LCM. The wording above has been corrected rather than preserved, because an incorrect acronym expansion is a defect and not a superseded belief. The implementation record is [2025-01-16 phone capability SDK on R5 hardware](2025-01-16-ccfphone-r5-device-lcm-odm-integration.md).

**The hierarchical state machine is hand-built in ANSI C, and its design is specific.** Each state is a function handling events; a state optionally names a super-state function, and when it does not, the machine degrades cleanly to a flat state machine. Transitions raise explicit super-state entry and exit phases carrying the triggering event, so a super-state can act on — or itself redirect — a transition through it. A re-entrancy flag rejects recursive dispatch with its own error code rather than corrupting the machine, and the header documents the single-threaded assumption together with the Active Object pattern as the way to run several machines concurrently. Event codes are 16-bit with a reserved range below user events, and the whole surface returns a single error enumeration covering argument validation, dispatch, transition and logging failures.

**Structured logging is JSON built on a vendored cJSON**, with the framework version emitted in its own informational record — so a log stream identifies the code that produced it.

**The written C style encodes defenses**, not preferences: comparisons ordered so an accidental assignment fails to compile, a zero-terminated-string convention, no relative include paths, and explicit rules for executable lifecycle and memory footprint.

**Dating — settled by the owner, 2026-09-20: the dates come from the repository.** The framework's initial commit is **2024-05-08**, its cJSON-based logging June 2024, the state-machine work July–August 2024, and the first capability SDK running on R5 hardware **2025-01-16**. This entry was previously dated 2026-04 to 2026-06 from an owner-supplied write-up; that date described when the write-up was made, not when the work happened. The entry and its filename are now dated from the repository. The innovation presentation independently corroborates the period — it places Capability SDKs in the **FY25 roadmap**.

## From the framework specification, 2026-09-19

The owner supplied the governing Confluence design page. It corrects one fact in this entry and adds the reasoning behind the framework's contents.

**Correction — what CCF stands for.** An earlier version of this entry called it the *Capability and Configuration Framework*. It is not. The design specification says **"Capability ansi C Framework"** and the owner's own presentation says **"Capability C Framework"** — the two differ only in whether *ansi* is spoken, and the spoken version is the one he uses in front of an audience. Either way the middle word is **C, the programming language**. The outward alias is unaffected: every public surface still says *component framework*.

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

## From the innovation presentation, 2026-09-20

The owner gave a full presentation on this work — *Capability SDKs (CCF) innovation: CCFPhone SDK ideas and achievements* — and its speaker notes are his words as spoken. They add the argument, the economics and several things no specification records.

**The one-sentence thesis, his own:** *"The innovation that we came up with is to ship more code and less text documents."*

**Why the old model could not simply be pushed harder.** He lays out the current collaboration as a six-step loop — Best Buy writes a specification, the manufacturer implements from scratch, questions are asked ("too many or too few"), Best Buy QA raises tickets, manufacturer QA works them, the manufacturer ships — and then makes the observation that carries the argument: Best Buy has limited influence over the manufacturer's own cycle, and pressing harder on it would most likely make that cycle *longer*, not shorter. So the lever has to be what gets shipped into it.

**The step he calls most strategic is the feedback one.** In the improved loop, step six is *upgrade the SDK* from what product development actually taught. In his words: *"Of course, we are good at dreaming and the reality check is going to be brutal. The thing is, we will take it face on and fix our SDK."* He is explicit that saving calendar time and improving quality matter less than the course correction.

**And he names the cautionary precedent by name.** A contractor team led by Michael Caisse built XPMF, a cutting-edge reusable framework for handhelds that is *still in production* — and rebuilding it for a different platform is a dead end because the toolset that produced the original binaries is practically unrecoverable. That is the failure mode step six exists to avoid, and it is a generous way to make the point: the framework was brilliant, and it still trapped its owner.

**Language choice, decided by developer reality rather than purity.** C99, not C90 — C90 was tried and found to be *"too much of unhealthy stress for a C++ developer crew"*, with the added judgement that if a future hardware vendor mandates a compiler that cannot manage C99, the team has a bigger problem than the standard.

**Fourteen capability SDKs were considered, and the choice of the first was deliberate.** Voice/MPERS won because it is the killer capability the product line was built on; Motion and Fall Detection are harder to prototype because they are bare-metal MCU code running machine learning against sensor data, and Device Management was the close runner-up. His caveat is the interesting part: *if only one capability SDK ever ships for the next device, it will be Motion* — he picked the tractable prototype while saying out loud which one actually matters.

**The economics of the manufacturer boundary, stated plainly.** The manufacturer authors the phone service, which loads Best Buy binaries; Best Buy's own process gets the same code plus the private facilities the manufacturer never sees. His reasoning for keeping the manufacturer's surface to a set of callbacks: *"the simpler is the interface the faster and better the job is done"* — followed by the line that explains why, which most engineers would leave unsaid: *"Actually, the money flows in the opposite direction."* Best Buy pays for that work, so every hour of manufacturer puzzlement is a bill. The pay-off he names is the ability to update phone-service behaviour without involving the manufacturer at all, avoiding expensive non-recurrent engineering — *"the more mature the SDK becomes, the LESS code ODM must write"*.

**The state machine, demonstrated rather than asserted.** Four states, with `NO_CALL` carrying no sub-states and an `ON_CALL` superstate holding everything common. He notes it re-affirms phone as the right thing to prototype, and says plainly: *"All this functionality is implemented already. I could easily replace phone-service in R5 with this one."*

**On working with Copilot, two observations that have aged well.** That duplication which would be a smell in hand-written code helps the model find context, which he reframes as an achievement in *code locality* — and the line that captures the shift: *"Comments are now called prompts"*, because *"Human memory is not a hard drive, but Copilot's memory actually is one."* He flags the August 2024 arrival of code-generation instruction files as the fix for the repetitive prompts scattered through the codebase, and names the real hazard as failing to timebox arguing with the tool.

**On LCM, the concept he leads with is connascence.** Marshalling in the current device is manual and error-prone, and LCM's type-specification language addresses *connascence of type* — Meilir Page-Jones's metric for dependency strength — directly. He goes as far as saying the entire device could be rewritten on LCM, replacing MQTT, D-Bus and Boost.Signal, while noting honestly that MQTT's quality-of-service and broker features might be a larger effort than moving the manufacturer's processes off D-Bus.

**The bare-metal strategy is Rust.** For a future device without a hosted environment he names Rust in `no_std` mode as the corner-stone, with a board-support-package framework, Active Objects for soft real-time concurrency, and tests running on target rather than off it. He is candid that *"Rust-everything will make us a cutting-edge so a business case should better be sharp enough too"*, and equally candid about self-interest: his own Rust expertise could be the deciding factor in whether such an effort succeeds, which is why he is putting in the learning hours.

**Tracing was designed for the constrained case first.** Structured JSON through cJSON, chosen because it runs even on an MCU, with the counter-intuitive justification that a `printf`-based approach is *more* expensive there and free-form logs are tedious to produce and to consume — and with the downstream benefit that Datadog ingests JSON natively.

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

The governing design page — the internal Confluence article *CCF Framework for SDK C Libraries for PERS devices* — was supplied by the owner on 2026-09-19 and is the source for the specification section above. Its internal wiki, repository, board and ticket URLs are deliberately not reproduced here. QP/C and its licence pricing are the vendor's own public information.

The innovation presentation *Capability SDKs (CCF) innovation* was supplied on 2026-09-20; its speaker notes across sixteen content slides are the source for the presentation section, and are the owner's words as spoken to a Best Buy Health audience. Extracted notes are retained in the maintainer's scratch scope.

## Related

- [2023-12-21-device-health-observability-architecture](2023-12-21-device-health-observability-architecture.md) — *maintained practice:* the agentless, telemetry-contract approach to device health defined in 2023; CCF's structured logging is the firmware-side realization of the same principle.
- [2024-01-20-errorsummary-json-schema-datadog-limitation](2024-01-20-errorsummary-json-schema-datadog-limitation.md) — earlier lesson that log/telemetry shape must be designed for the consumer; informs the structured-logging design here.
- [2026-09-01-r5-beacon-tracking-fota-persistence](2026-09-01-r5-beacon-tracking-fota-persistence.md) — same device programme and period; applies lifecycle and error-handling discipline to a specific R5 subsystem (thematic link, not a claimed dependency).
- [2026-05-26-ai-adoption-agentic-engineering-choreographer](2026-05-26-ai-adoption-agentic-engineering-choreographer.md) — concurrent enablement work sharing the same lever: reusable framework plus documentation and contribution guidelines to lower onboarding friction.
- [2025-08-30-cross-platform-sdk-modularization-pers-devices](2025-08-30-cross-platform-sdk-modularization-pers-devices.md) — earlier cross-platform SDK requirements and core-versus-adapter modularization that established the architectural foundation for this later component-framework work.
- [2025-01-16-ccfphone-r5-device-lcm-odm-integration](2025-01-16-ccfphone-r5-device-lcm-odm-integration.md) — the first capability SDK built on this framework, taken to real R5 hardware over the LCM messaging library.
- [2025-01-16-ccf-sdk-binary-hardening](2025-01-16-ccf-sdk-binary-hardening.md) — the security properties of the binaries this framework produces.
- [2023-01-30-system-monitor-freeze-counterexample](2023-01-30-system-monitor-freeze-counterexample.md) — the same consultancy's process supervisor, paused without a build-and-run check; the stewardship side of the XPMF precedent.
- [2024-10-18-copilot-embedded-c-sdk-practice](2024-10-18-copilot-embedded-c-sdk-practice.md) — the AI-assisted engineering practice written into this framework's own repository.

## Record history

- 2026-09-08: created from an owner-supplied brag write-up dated 2026-04-26
- 2026-09-16: added *Outward alias* — the internal name stays here; outward surfaces use "component framework".
- 2026-09-19: linked the earlier cross-platform SDK modularization entry, which records the requirements and boundaries that preceded CCF.
- 2026-09-19: added *Grounded in the source* from a direct study of four retained working copies — the two meanings of "LCM" separated, the state machine's concrete design recorded, and a dating discrepancy raised for the owner without altering the entry's date.
- 2026-09-19: added *From the framework specification* after the owner supplied the governing Confluence design page. **Corrected what CCF stands for** — "Capability ansi C Framework", not "Capability and Configuration Framework" — and recorded the reusable-component catalogue, the wakelock-ownership argument, the exponential-growth case for hierarchical state machines, the QP/C build-versus-buy evaluation, the full messaging-library case, and the on-device validation-suite requirement.
- 2026-09-20: **two corrections on the owner's instruction.** LCM in CCF and all derived work means Lightweight Communications and Marshalling and never lifecycle management — the earlier "lifecycle control (LCM)" gloss was an error and has been rewritten rather than preserved. And the entry is **re-dated from the repository** (2024-05 to 2025-01), replacing the 2026-04 date that came from the write-up rather than the work; the file was renamed to match. Added *From the innovation presentation* from the deck's verbatim speaker notes, including the XPMF precedent, the C99 decision, the fourteen candidate SDKs, the manufacturer-boundary economics, the Copilot observations, connascence of type, and the Rust bare-metal strategy.
- 2026-09-24: related link to the 2023-01-30 system-monitor entry.
