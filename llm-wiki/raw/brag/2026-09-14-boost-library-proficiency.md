---
title: "Boost proficiency: hierarchical state machines, asynchronous execution and testing"
date: "2018 to 2026-09-14; earlier experience recorded in the circa-2020 skills inventory"
thread: BOOST
domains:
  - "Architecture and API design"
  - "Quality and test automation"
context: "GreatCall / Best Buy Health embedded C++; earlier cross-career Boost experience"
sensitivity: private-repo
resume-worthy: yes
---

# Boost proficiency: hierarchical state machines, asynchronous execution and testing

## What I did

My Boost experience is not just familiarity with a collection of C++ utilities. The strongest documented examples are maintaining an elaborate **Boost.MSM** state-machine architecture, investigating its event transitions, and reasoning about **Boost.Asio** execution and signal-handling boundaries. **Boost.Test** is separately recorded in my historical skills inventory. That inventory lists **15 years of Boost/C++ and 2 years of Boost Test**, as of approximately 2020, not as current totals. [Archived inventory][skills]

This is a consolidated capability record, not a claim that I wrote every Boost-using component or originally designed the inherited device architecture. The filename uses the endpoint of the owner's September 14 account; the work spans years, and the historical inventory does not establish an exact first-use date.

## Libraries and versions

| Library | Evidence of my usage | Version evidence and boundary |
|---|---|---|
| **Boost.MSM (Meta State Machine)** | Owner-reported stewardship of a top-level device machine composed of submachines and orthogonal regions; direct `boost::msm::back::state_machine` trace in a battery/UI unit-test investigation dated April 17, 2023. | **Boost 1.67.0**, grounded by the device repository's ingested dependency evidence: all three vendored target headers declare `BOOST_VERSION 106700`. This resolves the earlier approximate 1.6x recollection. |
| **Boost.Asio** | August 2022 analysis of a Boost-dependent D-Bus abstraction and how to abstract its executor; a later note explicitly discusses `signal_set`, SIGTERM and possible loss of Asio's signal-handler guarantees. | **Boost 1.67.0**, the same vendored release for ARM Linux, native Linux and native macOS. The older incomplete "boost::asio 1.67 tutorials and how we use it" checklist is supporting historical context, not the primary version evidence. |
| **Boost.Test** | Explicit historical skills-table entry: 2 years of experience. | No release, named test suite or advanced Boost.Test technique recorded. The MSM trace is labelled `gtest`, not Boost.Test. |
| **Boost.Signals2** | The device's cross-component event bus is built directly on `boost::signals2::signal`: a thin wrapper enforces pass-by-value arguments and posts each subscriber's handler onto that subscriber's own single-threaded executor rather than invoking it inline, and the deterministic same-thread delivery order relies on Signals2's documented connect-order slot invocation. | Boost 1.67.0, the same vendored release established for Asio and MSM. |
| **Boost.Filesystem** | Two production call sites resolve and validate paths through `boost::filesystem::current_path()`; a 2026-09 hardening pass added explicit handling for a `boost::filesystem::filesystem_error` that previously escaped uncaught from an unsearchable-parent or symlink-loop path. | Same vendored 1.67.0 release; the exception type is version-appropriate for that release. |
| **Boost.System** | `boost::system::error_category`-derived categories are the repo-wide convention for identifying which subsystem raised an error: dozens of components each define one, and every category name is mapped to a numeric `ErrorCategory` enum value that gets bit-packed into the error-reporting payload. | Same vendored 1.67.0 release. |
| **Boost String Algorithms** | `boost::replace_all` performs in-place placeholder substitution (an unresolved `##imei##` token) across several config fields on a live component before it is torn down and rebuilt. | Same vendored 1.67.0 release. |
| **Boost/C++ overall** | Explicit historical skills-table entry: 15 years; later source records add named MSM and Asio cases. | No complete version history or dated upgrade record. Do not infer a start year by subtracting 15 from an approximate document date. |

Sources: [archived inventory][skills], [device working board][device-board], [leadership working board][leadership-board], and [owner-derived state-machine account][state-machines]. "Boost MSP" in the dictated note and "Boost MSS" in a board narrative are preserved source spellings, normalized here to **Boost.MSM** because the owner now explicitly names MSM and the trace independently names its backend. This does not establish use of a second state-machine library.

## Advanced usage: Boost.MSM

### Hierarchical composition and orthogonal regions

The core architecture was already using Boost.MSM when I joined GreatCall in 2018. It is not a single flat state switch: the owner's account describes a top-level machine with submachines and orthogonal regions, with system lifecycle as a critical state machine. My contribution is understanding and stewarding this inherited architecture as its designers and contractors departed, not retroactively claiming its original design. By September 2026, I described myself as the best and only fully qualified engineer on that codebase. That proficiency assessment is my own account, not an independently measured ranking. [Owner-derived account][state-machines]

### Following typed events through transition actions

An April 17, 2023 unit-test investigation records an unexpected battery/UI transition. I questioned whether shared application state had been constructed yet and traced a charger-disconnection event through an action instantiated with **event, FSM, source-state and target-state types**. The trace explicitly identifies `boost::msm::back::state_machine` and shows an initial-to-disconnected transition where the test expected silent battery behaviour. This is concrete evidence of working through a template-based MSM transition and its initialization dependencies, beyond recognizing the library name. It records a diagnostic hypothesis and trace, not proof of the eventual root cause or fix. [Device board][device-board]

### Integrating modes into the state model

The keep-alive build made the architectural stakes visible: keep-alive had to interact with system lifecycle while ordinary location functionality was disabled. The owner reports that this became sprawling ad hoc conditional logic. A separate MCU-failure UI mode similarly needed deliberate integration across the application processes; the chosen add-on approach went against my recommendation and produced additional unintended behaviours. The transferable skill is identifying when a cross-cutting operating mode belongs in the state model rather than distributing conditions through unrelated paths. These are examples of architectural judgement and advocacy, not claims that a clean MSM redesign shipped. [Owner-derived account][state-machines]

### State machines in an event-driven system

A device-board demo narrative connects the existing Boost-based state-machine and D-Bus architecture to multicast publish/subscribe reasoning while considering Lightweight Communications and Marshalling (LCM) for future work. A May 20, 2024 sprint note separately records publication of finite-state-machine library research. Together they show that my state-machine experience informs framework evaluation and event-driven design, not just maintenance of one machine. The demo's title says 2023 while its surrounding record points to 2024; neither supplies an exact Boost release or a complete list of evaluated libraries. The later embedded-C capability framework is related experience, **not evidence that it uses Boost**. [Device board][device-board]

## Advanced usage: Boost.Asio

### Executor boundaries, D-Bus and off-target testability

August 2022 working notes analyze reuse of the existing message-bus implementation before new hardware is readily available. They distinguish the application-facing bus interface, an injected mock used to post events and assert messages, a threaded D-Bus connection, and helper code with a Boost dependency. I identify the need to abstract **`boost::asio` or another executor**, and weigh retaining the dependency against removing it when reusing the test infrastructure. That is an architectural dependency and testability decision: preserve a production implementation that stands on its own while substituting the bus in tests, rather than inject test-only stubs into production code. The notes propose the executor abstraction; they do not demonstrate that it was implemented. [Device board][device-board]

The card's checklist explicitly pairs **"boost::asio 1.67 tutorials and how we use it"** with **"executors in C++20 or beyond"**. Both items are marked incomplete in the preserved snapshot. This is concrete evidence of the version and execution-model comparison I had identified for study, not proof that the device linked Boost 1.67, that the study was finished, or that C++20 executors were adopted. [Device board][device-board]

### Signal handling and guarantee boundaries

A leadership-board note explicitly says the application handles **SIGTERM**, but **`boost::asio::signal_set`** is limited for the particular requirement. I identify that the alternative under discussion would lose Asio's signal-handler guarantees and that dual handling might be necessary, with further research required. This supports advanced reasoning about the boundary between asynchronous dispatch and process-level signal handling. The note does not specify the exact missing facility, final design, delivered fix or applicable Boost release, so none is invented here. Its last recorded activity is February 16, 2026; that is not treated as the date the work began or shipped. [Leadership board][leadership-board]

## Advanced usage: infrastructure libraries beyond Asio and MSM

### Signals2 as the cross-component event bus

Every cross-component notification in the device's `core` process is a `boost::signals2::signal` underneath a thin wrapper that (a) statically rejects lvalue-reference signal parameters, forcing pass-by-value so a queued handler can never see a stale reference, and (b) posts each subscriber's real handler onto that subscriber's own single-threaded executor instead of invoking it inline. The observable, deterministic behavior — same-thread handlers run in the order they were connected, and in the order the emitting signals fired — depends on Signals2's own documented connect-order slot invocation composed with the posting behavior. This is architectural use of Signals2's ordering guarantee, not just calling `connect()`.

### Filesystem paths and their error surface

Two production write paths resolve their target directory through `boost::filesystem::current_path()`. A 2026-09 hardening pass closed a gap where an unsearchable parent directory, a symlink loop, or an over-long path name would let an unhandled `boost::filesystem::filesystem_error` escape uncaught; the fix adds an explicit `status()`/`status_known` check ahead of the write instead of ignoring that error category.

### System error categories as an organizing convention

`boost::system::error_category` is used as the naming and dispatch mechanism for a repo-wide error-reporting convention: each subsystem defines its own `error_category`-derived class, and every category name is registered against a bit-packed numeric code sent in the error-reporting payload. Extending this convention correctly — adding a category, keeping its name mapped, and testing the mapping — is a recorded engineering rule I contributed to, not merely an incidental use of the type.

### String Algorithms for live in-place substitution

`boost::replace_all` performs placeholder substitution across several configuration string fields — filling in a device identifier a config value carries as an unresolved token — on a component instance that is still alive, immediately before it is torn down and reconstructed with the resolved values.

## Why it matters

The record supports both long-standing breadth and a specific depth claim: maintaining and diagnosing hierarchical, event-driven C++ systems, reasoning about lifecycle interactions, and keeping asynchronous infrastructure testable. The strongest proficiency evidence is **MSM composition and typed-transition diagnosis**, followed by **Asio executor and signal-handling analysis**, with **Signals2, Filesystem, System and String Algorithms** as a wider base of production infrastructure library use across the same codebase. Boost.Test adds a separately recorded testing capability, without enough detail to claim advanced framework-specific techniques.

## Skills demonstrated

- Boost.MSM: submachines, orthogonal regions, typed transition actions, event tracing and lifecycle reasoning.
- Boost.Asio: executor abstraction, asynchronous message-bus integration, `signal_set` and signal-handler guarantee analysis.
- Boost.Signals2: cross-component event-bus design relying on connect-order slot invocation composed with posted, single-threaded delivery.
- Boost.Filesystem: path resolution and a hardened error-handling boundary around `filesystem_error`.
- Boost.System: `error_category` as a repo-wide error-identification and dispatch convention.
- Boost String Algorithms: in-place live-object string substitution ahead of a controlled component rebuild.
- Boost.Test: historical hands-on experience, with specific use cases still unspecified.
- C++ template diagnostics, dependency boundaries, mock-driven off-target testing, inherited-codebase stewardship and evidence-based framework evaluation.

## What was blocked, cut short, or wrong

The owner reports that proper integration of the keep-alive and MCU-failure modes into the state-machine architecture did not win out over ad hoc conditions. The Asio executor abstraction and signal-handling alternative are recorded as ideas or investigations, not completed deliveries. Preserving those limits is part of recording the engineering judgement honestly.

## Evidence

The technical grounding for this consolidation comes from **the device repository's LLM-wiki**, as requested by the owner, not from the resume wiki's earlier derivative summaries. Its ingested threading-model and versioned-documentation source pages establish Boost 1.67.0 for all three vendored targets through `BOOST_VERSION 106700`, with the verification recorded on July 15, 2026. The owner confirms the shared ARM/macOS library comes through the library or sysroot submodules. Employer-internal wiki artifacts and their exact locations remain in the private working evidence; this entry preserves the transferable substance without requiring another checkout to be readable.

The Signals2, Filesystem, System and String Algorithms evidence comes from the same device wiki: its dev-conventions pages document the signal/slot threading model built on `boost::signals2::signal`, the error-reporting convention built on `boost::system::error_category`, and a config-lifetime page documenting `boost::replace_all`; a file-write-contract entity page documents `boost::filesystem::current_path()` and a hardened `filesystem_error` handling path. These are direct citations of dated documentation of production source, not restatements of this entry's own prior claims.

The resume repository's archived inventory, boards and captured owner account remain supporting career evidence for years of experience, dated investigations and personal contribution. They are not substitutes for the device wiki's implementation grounding. Wiki summaries do not independently corroborate themselves.

- The [archived skills inventory][skills] directly names Boost/C++ and Boost Test and their historical experience figures.
- The [preserved device board][device-board] contains the August 2022 reuse/testability analysis, April 17, 2023 MSM transition trace, event-driven architecture demo narrative and May 20, 2024 state-machine research note. Internal ticket IDs, project-specific symbols and URLs remain in the archive rather than being copied here.
- The [preserved leadership board][leadership-board] contains the explicit Asio SIGTERM/`signal_set` investigation note.
- The owner's September 14, 2026 dictated account supplies submachine/orthogonal-region composition, the approximate release recollection, the architecture disagreements and the stewardship assessment; its Boost-relevant substance is preserved above. The [state-machine hub][state-machines] carries the existing synthesis of that account. The September 15 request explicitly asks for Boost proficiency and MSM examples.

## Evidence limitations

**The vendored release is Boost 1.67.0 across ARM Linux, native Linux and native macOS**, established by the device wiki's ingested version-header verification, not inferred from the historical study checklist. Asio and Signals2 guarantees are grounded in the already captured 1.67.0 documentation. This consolidation does not claim a fresh compilation or device execution, or establish that every historical build used that version.

Signals2, Filesystem, System and String Algorithms are grounded the same way as Asio and MSM: cited, dated device-wiki documentation pages describing production source (not this consolidation's own prose, and not a repeat of the historical study checklist). None of the four is a delivered feature or bug fix in its own right — they are recorded as infrastructure the production `core` process is built on and that I work with directly, which is the claim being made.

A repeat, deliberate search specifically for **Boost.MPL** found no matching evidence anywhere in the searched device-wiki text — no page, source excerpt or code reference names it. This is a completed negative search, not an oversight: MPL is not added to this entry.

No distinct evidence was found for personal use of Boost.Statechart, MPL, Fusion, Spirit, Graph, Serialization, Thread or other named Boost libraries. They are not added by assuming what MSM depends on, what a C++ engineer probably uses, or what the standard library later adopted. Likewise, Google Test/gMock, D-Bus, LCM, `std::function`, `std::unique_ptr`, and Qualcomm's unrelated MSM platform terminology are not Boost-library claims.

The 15-year and 2-year figures remain circa-2020 self-reported baselines, not automatically increased to 2026. No performance multiplier, defect reduction, precise shipping outcome, original-framework authorship or unrecorded library upgrade is claimed.

## Related

- [State-machine cluster][state-machines]: the broader keep-alive, failure-mode and stewardship stories, for which this entry supplies consolidated Boost evidence.
- [Skills matrix](../../wiki/concepts/skills-matrix.md): historical baseline and named capability registration.

## Record history

- 2026-09-15: Created and ingested at the owner's request by consolidating the archived inventory, both preserved board exports and the Boost-relevant September 14 account. Exact versions remain unconfirmed; distinct non-Boost inbox material remains pending rather than being deleted or silently treated as ingested.
- 2026-09-15: The initial recheck incorrectly interpreted "this repo" as the resume repository. The owner clarified the intended device repository; its existing wiki grounding establishes Boost 1.67.0 across all three vendored targets. Corrected the exclusive-source statement and superseded the earlier version-unverified conclusion; preserved the historical checklist as historical evidence only.
- 2026-09-19: Finished the interrupted expanded-library capture. Added Boost.Signals2, Boost.Filesystem, Boost.System and Boost String Algorithms, each grounded in dated device-wiki documentation of production source, not inference. A repeat targeted search for Boost.MPL again found no evidence and remains explicitly excluded.

[skills]: ../archive/Oleg.Zhylin.skills_and_responsibilities.md
[device-board]: ../trello/2026-09-09-r5-jira-board.json.xz
[leadership-board]: ../trello/2026-09-09-leadership-board.json.xz
[state-machines]: ../../wiki/stories/state-machines.md