---
title: "Defined a cross-platform SDK architecture for PERS devices"
date: "2025-06 to 2025-08 (impact date 2025-08-30)"
thread: FW
domains:
  - "architecture and API design"
  - "embedded and safety-critical devices"
  - "build, release and CI/CD"
context: "Best Buy Health, SDK C libraries for Personal Emergency Response System (PERS) devices, Linux-based systems and MCUs"
sensitivity: private-repo
resume-worthy: yes
---

# Defined a cross-platform SDK architecture for PERS devices

## What I did

Worked on SDKs for Personal Emergency Response System (PERS) devices running on Linux-based systems and MCUs. The existing device- and vendor-specific SDK structures duplicated logic, used inconsistent abstractions, and coupled core capabilities to particular platforms.

- Co-authored and refined requirements for SDK C libraries, covering ANSI C compatibility, minimal dependencies, predictable memory usage, and a clear separation between core SDK responsibilities and ODM integrations. Captured the requirements in a shared contract for future SDK work.
- Refactored the architecture to separate platform-agnostic capabilities — including fall detection logic, audio-control state machines, location abstractions and device management — from platform-specific adapters such as OS services, IPC and hardware drivers.
- Introduced clear header and library boundaries so core libraries could be reused across Linux and MCU targets with minimal platform-specific change.
- Defined stable public C headers for capabilities and configuration, suitable for ODM and internal-team consumption, and organized the SDKs as versioned static or dynamic libraries for distribution through existing artifact repositories.
- Aligned the modularization with the emerging CCF concepts and identified existing R5 source areas that were candidates for extraction into reusable SDK components.

## From the specification itself, 2026-09-19

The owner supplied the actual Confluence specification this entry summarizes. It is a stronger document than the summary suggested, and the following is what it adds.

**The strategic idea, and it is the best line in the document: an SDK is a way to inject our own code into the manufacturer's process.** Until then, everything Best Buy Health needed an ODM to build was communicated as a specification document — with the result, stated plainly in the document, that *both* sides spent extra time on concerns outside their core expertise. Shipping a library instead of a specification moves the behaviour the company cares about into the manufacturer's process, where the company still owns it. The interface requirements follow from that: usable by the ODM, and flexible enough to change behaviour on the fly.

That is a direct evolution of the owner's own earlier work — he had authored the manufacturer-facing specification set in 2022, and this document is him concluding that the specification, done well, is still the wrong instrument.

**Five requirements, each with a reason.** A C-based interface for maximum compatibility; minimal third-party dependencies; an automated test suite covering all functionality; unit tests with a code-coverage metric; and minimal dynamic allocation.

**The static-versus-dynamic decision is asymmetric, deliberately, and grounded in an incident.**

| Consumer | Links against | Why |
|---|---|---|
| ODM code | Dynamic shared objects (`.so`) | The company can upgrade SDK behaviour without the manufacturer recompiling anything |
| In-house code | Static libraries (`.a`) | Simpler development, and direct access to private headers and implementation details |

The justification is experience rather than preference: integrating the Qualcomm/Skyhook location library, there was a recurring need to deploy unplanned code changes, and it *helped a lot* that the location-manager service did not require recompilation. The same document proposes utility libraries — logging, state machines — as static libraries, since in-house code is always their consumer.

**Public and private headers are separated on purpose**, so manufacturer code is insulated from in-house implementation details rather than merely discouraged from depending on them.

**The worked example is the reusable core of a capability.** The ODM's location-manager service on R5 was implemented to a D-Bus specification — practical, but it left nothing reusable, so the next device would re-implement it from scratch. The document picks out one thing worth owning: deciding whether one location fix is better than another. A shared library exposing that predicate lets the company own the logic, reuse it across devices, and vary it where a device needs something different. That is the modularization argument reduced to a single function, and it connects straight to the location-engine work.

**Portability is written into the coding style.** Newer ISO C features are to be used conservatively so the likelihood of compiling unchanged for a restricted target such as an MCU stays high, with ANSI C as the default; free-standing functions follow Python-style naming (`location_fix_is_better(const struct Fix*, const struct Fix*)` is the document's own example). A shared repository template was to carry all of it, providing both static and dynamic targets so every SDK started compliant instead of being audited afterwards.

**ODM context.** The document names the manufacturers this was written for — Wistron, Borqs and TCL — and Wistron as the one that implemented the R5 location service. Those names stay at T1; outward text says "a contract manufacturer".

## Why it matters

The architecture makes new-device integration a thinner adapter exercise rather than a fresh implementation of each capability, reducing duplication and inconsistency across PERS devices. Shared fixes and enhancements can benefit every consumer of a core library, while stable boundaries make the SDK easier for engineers and vendors to understand and extend. The requirements and modular structure also created the foundation for later component-framework and lifecycle-management work.

## Skills demonstrated

Cross-platform embedded architecture, ANSI C library design, API and header-boundary design, platform abstraction, dependency minimization, predictable-memory design, static and dynamic library packaging, ODM integration, technical requirements authoring, and framework evolution.

## Evidence

Internal requirements and architectural design materials for SDK C libraries; source repositories showing platform-agnostic core libraries and platform-specific adapters; versioned library and artifact-repository packaging conventions. The entry's technical evidence is described generically because the source materials are internal.

The governing specification itself was supplied by the owner on 2026-09-19 as a rendered copy of the internal Confluence page *Requirements for SDK C Libraries for PERS devices*, and is the source for the section above. Its internal wiki, repository and board URLs are deliberately not reproduced here.

## Evidence limitations

The technical requirements and architectural intent are documented, and the code structure reflects the stated separation. Adoption and efficiency data — reduced onboarding time, number of SKUs sharing components, and defect reduction from shared fixes — were not systematically captured in the supplied note. The entry therefore does not claim measured time-to-market improvement, a specific number of onboarded SKUs, or quantified defect reduction.

**The specification is a design document, and much of it is written in the imperative future** — "shall be", "could provide", "is expected to". It establishes what was decided and required, not what was subsequently built or adopted. The reusable location-fix predicate, the shared repository template and the utility-library split are proposals in this document; only some of them are corroborated as built by the retained source trees. **Authorship is not separately attested**: the document is a team Confluence page, its content matches the owner's account and his adjacent authored work, and no contradicting evidence was found — but no byline is reproduced in the supplied copy.

## What was blocked, cut short, or wrong

No blocker or failed approach was supplied. The expected benefits are recorded as architectural consequences and intended outcomes, not as measured results.

## Related

- [2026-04-26-ccf-capability-framework-lcm-open-source](2026-04-26-ccf-capability-framework-lcm-open-source.md) — later component-framework work that builds on the earlier cross-platform SDK requirements and modular boundaries.
- [2025-04-13-ble-sdk-breadth-first-white-label](2025-04-13-ble-sdk-breadth-first-white-label.md) — related SDK work in the same broader device programme; that entry records an observer role on a breadth-first white-label model, while this entry records direct cross-platform modularization work.
- [2022-08-03-odm-specification-authoring](2022-08-03-odm-specification-authoring.md) — earlier manufacturer-facing API and integration specifications.

## Record history

- 2026-09-19: created from an owner-supplied accomplishment note dated 2025-08-30.
- 2026-09-19: added *From the specification itself* after the owner supplied the governing Confluence requirements page — the code-injection strategy, the asymmetric static/dynamic policy and its Skyhook grounding, public/private header separation, the reusable location-fix-quality example, and the ANSI C portability rules. Evidence limitations extended to separate what the document decided from what was built.
