---
title: "Ran a phone capability SDK on R5 hardware with the app and the manufacturer's service as separate processes talking over LCM"
date: "2024-10 to 2025-01 (device milestone 2025-01-16)"
thread: FW
domains:
  - "embedded and safety-critical devices"
  - "architecture and API design"
  - "build, release and CI/CD"
context: "Best Buy Health, phone capability SDK for PERS devices, R5-class Qualcomm Linux hardware"
sensitivity: private-repo
resume-worthy: yes
---

# Ran a phone capability SDK on R5 hardware with the app and the manufacturer's service as separate processes talking over LCM

## What I did

Built the phone (MPERS call-handling) capability SDK on top of the [component framework](2024-05-08-ccf-capability-framework-lcm-open-source.md), and took it all the way to running on production-class R5 hardware. Its own README describes it as one of the first capability SDKs built on that framework, so the SDK and the framework were deliberately evolved in lockstep.

**The architecture splits along the organizational boundary, not just a technical one.** The example system is two executables, and which company owns each is the point:

- an **application process** whose source Best Buy Health owns, implementing product behaviour;
- an **ODM service process** the contract manufacturer owns, exposing the platform-specific things — cellular modem, audio playback, buttons — and loading the SDK's shared object.

The manufacturer's service consumes the SDK's public C API to satisfy the application's needs. One header in the tree is explicitly marked as a public include file distributed to parties outside the company: the API contract with the ODM is stated in the source itself rather than only in a specification document.

**The two processes talk over LCM — Lightweight Communications and Marshalling**, the open-source messaging library from the robotics world (<https://github.com/lcm-proj/lcm>), pinned to the public v1.5.0 release and carried over UDP multicast. Three named channels carry the traffic in both directions: commands from the application to the service, events from the service back, and a third channel marshalling the ODM service's **log records** across the process boundary so device logging stays unified across the company boundary. Payloads are JSON, built with the vendored cJSON library.

> **Naming note.** In CCF and everything derived from it, **LCM always means Lightweight Communications and Marshalling** — never lifecycle management. An earlier version of the framework entry glossed it as "lifecycle control"; that was an error, now corrected. The **design rationale** for choosing it — publish/subscribe simplicity, a robotics track record, recordable and replayable messages, and portability to platforms without UDP — is recorded in the [framework entry](2024-05-08-ccf-capability-framework-lcm-open-source.md) § *From the framework specification*, which also proposed rewriting the existing Boost signal buses on it.

**The phone capability itself** models call handling properly rather than as a thin passthrough: mobile-originated and mobile-terminated call direction; service state including a distinct *in-service emergency* value; call states through ringing, dialing, active, disconnected and failed; the 3GPP call-end reason code carried through on disconnect; and volume control via client callbacks. The interface was modelled on the platform's existing D-Bus API specification, so the SDK met the platform where it already was.

**The error taxonomy separates "keep going" from "give up", deliberately.** One return value means the SDK's logic failed but the phone must continue operating; another means a fatal error, with re-initialization documented as a legitimate recovery path. On a medical-alert device the difference between those two is the difference between a degraded call and no call at all.

**Getting it onto the device was its own engineering effort**, and is the part that makes this more than a desk exercise:

- cross-compilation to the device's **Qualcomm MDM9607 ARM** target — `armv7-a`, NEON, soft-float ABI — through an OpenEmbedded `arm-oe-linux-gnueabi` toolchain, with the device **sysroot pinned as a submodule** so the build did not depend on a hand-configured workstation;
- a **Docker build container** (Ubuntu 18.04, GCC 4.9) capturing the whole toolchain, so the device build was reproducible by anyone with Docker and a USB cable;
- a **deployment script over adb**: device into the development cradle, root filesystem remounted read-write, the two executables pushed to the device's `/oem` partition and the shared libraries — the SDK, the framework and LCM itself — into the system library directory;
- a **version stamp** generated at build time from the git commit, describe output, builder and timestamp, so a binary on a device could be traced back to what produced it.

**The tests exercise the real inter-process path.** A gtest LCM test node subscribes to the event and log channels, publishes JSON commands such as *dial* and *exit*, and pumps messages with bounded timeouts — so the multi-process conversation is covered by automated tests rather than only by manual bring-up.

## Why it matters

- **It is the framework proven on real hardware.** A framework that only builds on a workstation is a proposal. This is the same code cross-compiled, deployed and run on the device the product actually ships on.
- **It makes the manufacturer boundary a supported interface instead of a negotiation.** The ODM implements one process against a published C header and a documented message contract; the pieces either side can change independently. That is the modular-boundary argument the owner makes elsewhere, implemented rather than asserted.
- **Choosing LCM is a considered bet.** A proven open-source messaging library with a multicast transport, rather than a bespoke socket protocol or a heavier middleware, keeps the boundary debuggable — any process on the device can subscribe and watch the conversation, which is exactly what the test node does.
- **Logging across the boundary was designed in, not bolted on.** The manufacturer's service emits structured log records that reach Best Buy Health code through the same channel mechanism, extending the device-health observability contract down into a process the company does not own.

## Skills demonstrated

Embedded C (C99) library and API design; multi-process architecture; inter-process communication and publish/subscribe messaging (LCM, UDP multicast); JSON message design; ARM cross-compilation with OpenEmbedded toolchains and pinned sysroots; containerized reproducible builds; on-device deployment via adb; build-time version provenance; multi-process integration testing with GoogleTest; ODM-facing API contracts; telephony domain modelling (3GPP call-end reasons, MO/MT, service states).

## Evidence

Four working copies of the SDK and framework repositories retained on the owner's workstation, with commit history spanning May 2024 to January 2025: the framework's initial commit and cJSON-based logging, the state-machine work, the addition of the LCM dependency, the merged LCM-based events-and-commands branch, and a device branch whose framework commit is titled *"ccfphone builds for R5 device"*. The tree contains the cross-compilation toolchain file, the Docker build definition, the adb deployment script, the sysroot submodule, the public ODM-facing header, the LCM channel constants, and the gtest LCM test node. Internal repository, wiki and ticket URLs exist in the sources and are deliberately not reproduced here.

## Evidence limitations

- **This establishes "built, deployed and exercised on device", not "shipped".** The device branch's most recent commit is explicitly work in progress, ahead of a further LCM point-release upgrade, and the working tree still carries uncommitted build-file changes. No production release, fleet deployment, customer-facing outcome or adoption metric is claimed.
- **The examples are reference implementations.** The two-process system lives in the repository's `examples` tree and demonstrates the intended integration; it is not evidence that a particular manufacturer shipped that exact service.
- **Dates come from commit metadata**, not from a project plan, and describe when work was committed rather than when it was agreed or released.
- **Whether the owner wrote every part is not separable from this evidence alone.** The branches carrying this work are under the owner's own name and the design decisions are his, but the repositories are team repositories with merged pull requests from others.

## What was blocked, cut short, or wrong

- **The dependency model was known to be wrong at the time and said so in writing.** The framework is consumed as a git submodule pinned in lockstep with the SDK, and the README states plainly that a package manager or other more maintainable solution must be considered going forward. That is the same discipline as naming brittle test protocols as debt at the moment they are incurred — the limitation is recorded where the next maintainer will find it, not left as tribal knowledge. It also points straight back at the packaging work the owner had already done on another embedded product.
- **The device branch stops mid-upgrade.** The record ends at a work-in-progress commit rather than at a clean release, and the honest telling says so.

## Related

- [2024-05-08 component framework](2024-05-08-ccf-capability-framework-lcm-open-source.md) — the framework this SDK is built on and evolved alongside; also where the mistaken "lifecycle control" gloss of LCM is corrected.
- [2025-08-30 cross-platform SDK modularization](2025-08-30-cross-platform-sdk-modularization-pers-devices.md) — the requirements and core-versus-adapter boundaries this SDK realizes on a specific capability.
- [2025-01-16 SDK binary hardening](2025-01-16-ccf-sdk-binary-hardening.md) — the security properties of these same binaries: the toolchain mitigations, the pinned and provenance-named dependencies, and the trust boundary in the public header.
- [2024-10-18 Copilot practice for an embedded C SDK](2024-10-18-copilot-embedded-c-sdk-practice.md) — how this codebase was actually written, and the team practice recorded alongside it.
- [2022-08-03 ODM specification authoring](2022-08-03-odm-specification-authoring.md) — the earlier manufacturer-facing API specifications; this is the same boundary expressed as a compilable contract instead of a document.
- [2022-04-06 Conan package management and cross-build](2022-04-06-conan-package-management-embedded-cross-build.md) — the packaging and cross-compilation discipline the README calls for as the fix to the submodule approach.
- [2025-04-13 breadth-first white-label integration](2025-04-13-ble-sdk-breadth-first-white-label.md) — the integration-model argument; this entry is the ground-up side of it, built so the vendor boundary stays modular.

## Record history

- 2026-09-19: created from a direct study of four retained working copies of the SDK and framework repositories, at the owner's request to mine them for what was actually there.
