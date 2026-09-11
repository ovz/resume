---
title: "Designed the Conan package and cross-build strategy for an embedded C++ product"
date: "2022-04-06 to 2022-06"
thread: BLD
domains:
  - "build"
  - "release"
  - "CI/CD"
  - "embedded and safety-critical devices"
  - "architecture and API design"
context: "Best Buy Health, next-generation senior-care wearable — embedded C++ dependency management and cross-compilation"
sensitivity: private-repo
resume-worthy: yes
---

# Designed the Conan package and cross-build strategy for an embedded C++ product

## What I did

Designed how the device's C++ components would be **versioned, packaged and cross-built**, using **Conan** as the package manager, and wrote the policy down so the team applied one scheme instead of improvising per component.

**A versioning and promotion policy mapped onto channels.** Rather than treat a package version as an opaque string, I gave each field a job and tied the channels to the release path:

- *Major* distinguishes releases — the version is cut when a release is.
- *Minor* distinguishes pull requests, and can be incremented as needed within one.
- *Revision* is the field engineers coordinate on in the special cases that always eventually arise.
- The development channel takes the full scheme; the test channel's major/minor match the *upcoming* release, so promoting a tested package to production is a plain upload rather than a rebuild.
- **CI appends its own unique suffix**, so two builds of nominally the same version are still distinguishable — the failure this prevents is the one where a bug reproduces against a package nobody can identify.

**"Living at the head" where it earns its keep.** Components that track the latest build of a dependency declare that directly, so routine work does not pay a manual version-bump tax on every change; components that need pinning still pin.

**Cross-building to the ARM target.** I researched building the product for the device from a developer machine, which is the part that decides whether the scheme is usable day to day. I worked through the realistic options — packaging sysroots as a Conan package, a container carrying them, or consuming them as a submodule — and through the toolchain mechanics: how tool requirements behave when cross-compiling (including the documented cases where they are silently *not* satisfied), which parts of the vendor's guidance were current versus obsolete, and pinning the specific compiler version the target demanded.

## Why it matters

Dependency and build strategy is the sort of decision that is nearly free to make correctly at the start of a device generation and extremely expensive to change once dozens of components have each invented their own convention. Tying versions to releases and pull requests made a package's provenance readable from its version alone, and making CI builds individually identifiable meant a defect could always be traced to the exact artifact that carried it.

The cross-build work removed the constraint that only a correctly-configured machine could produce a target build — the difference between a reproducible pipeline and tribal knowledge.

## Skills demonstrated

C++ dependency management (Conan), package versioning and promotion-channel design, cross-compilation and toolchain construction for embedded ARM targets, sysroot packaging strategies, CI/CD integration, writing engineering policy that others can follow, self-directed research against vendor documentation of uneven quality.

## Evidence

The owner's working board for the device programme, April–June 2022: a written package-flow and version-policy note covering channel semantics and CI-generated build suffixes, and a cross-building research thread covering sysroot packaging options, tool-requirement behaviour when cross-compiling, and compiler-version pinning for the ARM profile. Vendor documentation and community threads are cited there as public references; internal repository paths are not reproduced here.

## Related

- [2021-08-15-github-enterprise-migration-monorepo](2021-08-15-github-enterprise-migration-monorepo.md) — the platform migration that made the CI automation this policy depends on possible.
- [2022-02-18-cpp-safety-critical-embedded-guidelines](2022-02-18-cpp-safety-critical-embedded-guidelines.md) — concurrent work setting how C++ is written in the same codebase, as this sets how it is built.
- [2026-04-26-ccf-capability-framework-lcm-open-source](2026-04-26-ccf-capability-framework-lcm-open-source.md) — the later framework whose modular, contribution-ready packaging assumes exactly this kind of dependency discipline.

## Record history

- 2026-09-09: created from the owner's Trello device-programme board export (Conan list). The card dates cluster on 2022-04-06 with follow-on activity; **owner to confirm** how far the policy was adopted and whether the cross-build approach shipped.
