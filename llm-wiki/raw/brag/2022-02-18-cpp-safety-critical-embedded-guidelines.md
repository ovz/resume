---
title: "Established C++ guidelines and static analysis for a safety-critical embedded codebase"
date: "2022-02 to 2022-06"
thread: BLD
domains:
  - "embedded and safety-critical devices"
  - "quality and test automation"
  - "architecture and API design"
context: "Best Buy Health, next-generation senior-care wearable — embedded C++ engineering standards"
sensitivity: private-repo
resume-worthy: yes
---

# Established C++ guidelines and static analysis for a safety-critical embedded codebase

## What I did

Led the review of how C++ should be used in a **safety-critical embedded** system for the next-generation device, and turned the answer into written guidelines the team could apply rather than an abstract preference.

- **Evaluated the candidate standards against each other rather than adopting one on reputation.** Compared **MISRA C++**, **JSF** and the **C++ Core Guidelines** on the criterion that actually mattered: which of them the team's static-analysis tooling could genuinely enforce. Established that the platform in use supported MISRA only *partially* — implementing a bounded subset of rules per standard revision — and that JSF had far less mainstream traction than MISRA or the Core Guidelines. A standard the toolchain cannot check is a standard the codebase drifts away from silently.
- **Grounded the guidelines in the existing static-analysis setup** rather than starting from a blank page, taking the codebase's own analysis configuration as the baseline and building the written guidance out from it.
- **Published the result as durable internal documentation**, so the reasoning behind each choice survived the discussion that produced it.
- Worked through the practical toolchain friction that comes with cross-platform embedded development — compiler and dependency resolution differing between developer machines and the target — so the guidelines were runnable rather than theoretical.

## Why it matters

A medical-alert device is safety-adjacent: a defect class that a coding standard and static analysis would have caught is a defect class that reaches a person who depends on the device. Choosing the standard by *enforceability* rather than by prestige is what makes the guidance hold over years, because the check runs on every build instead of relying on reviewer memory.

Doing this at the start of a new device generation, rather than retrofitting it later, set the codebase's conventions while they were still cheap to set.

## Skills demonstrated

Safety-critical embedded C++, coding-standard evaluation (MISRA C++, JSF, C++ Core Guidelines), static-analysis tooling and its real coverage limits, engineering-standards authorship, cross-platform toolchain troubleshooting, technical documentation.

## Evidence

The owner's working board for the device programme, February–June 2022, covering the C++-in-safety-critical-systems review, the static-analysis baseline it built on, the comparison of standards against tool support, and the toolchain issues resolved along the way. Internal ticket identifiers, repository paths and wiki URLs are not reproduced here.

## Related

- [2022-04-06-conan-package-management-embedded-cross-build](2022-04-06-conan-package-management-embedded-cross-build.md) — concurrent work on the same codebase, establishing how its dependencies are versioned and cross-built.
- [2024-05-08-ccf-capability-framework-lcm-open-source](2024-05-08-ccf-capability-framework-lcm-open-source.md) — the later framework work that made these conventions concrete across device SKUs.

## Record history

- 2026-09-09: created from the owner's Trello device-programme board export (2022 C++ guidelines list). Date range inferred from card activity; **owner to confirm** the end date and whether the guidelines were formally adopted team-wide.
