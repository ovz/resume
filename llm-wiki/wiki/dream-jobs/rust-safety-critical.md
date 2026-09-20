---
title: "Rust in safety-critical embedded"
dream-job: DJ-8
origin: suggested
specialization: emerging
evidence: moderate
horizon: build
fits: [embedded, rust, regulated, architecture, firmware]
status: candidate
---

# ○ Rust in safety-critical embedded

> **Doc type:** reference · **origin: suggested** — proposed by an agent on 2026-09-13 because three things the owner already holds are rarely held together. Not the owner's idea.

## The job

Bringing Rust into firmware that has to be certified — automotive (ISO 26262), medical (IEC 62304), industrial (IEC 61508) — which in practice means as much standards and toolchain work as coding: what the compiler can be relied on to guarantee, what still needs external analysis, how coverage obligations such as MC/DC are met, which crates are admissible, and where the C boundary sits. Roles are firmware architect, platform engineer, or the person a programme hires to answer "can we use Rust here, and prove it".

## Under the Value and Impact tests

**Enabler inside a product company; product at a tools or certification vendor.** The mitigating factor is unusual visibility: being the person who made Rust admissible in a certified programme is a differential with a name attached to it, argued in front of a quality organization rather than buried in a platform. That is a rare case of enabler work that is *seen*, which is what the Impact test actually asks for.

## Why 2026 is the moment

From the Rust Project's own January 2026 safety-critical write-up: a medical-device firm reports "All of the product code that we deploy to end users and customers is currently in Rust" for IEC 62304 Class B software in intensive-care use, and a robotics engineer under IEC 61508 SIL 2 reports "Roughly 90% of what we used to check with external tools is built into Rust's compiler". The same source names the limit — "once you move beyond prototyping into the higher-criticality parts of a system, the ecosystem support thins out fast" — and the stalled MC/DC coverage work now being revived through the Safety-Critical Rust Consortium. Automotive is leading; regulation (EU Cyber Resilience Act, FDA premarket cybersecurity expectations, UNECE WP.29 / ISO 21434) is part of the push. Sources: [specializations landscape](../analysis/2026-09-13-specializations-landscape.md) § *Rust in safety-critical embedded*.

**The field's open problem is the owner's existing skill.** The unanswered questions are about enforceability, tooling and evidence — not about syntax.

## What the record already supports

The rare combination, in three parts:

1. **He has already made the language-rules decision the Rust-in-safety-critical argument is about.** [He chose the C++ standard for a safety-critical embedded codebase on *enforceability* rather than reputation — comparing MISRA C++, JSF and the Core Guidelines by what static analysis could actually check — and then wrote the guidelines against the existing analysis baseline so the rules are verified on every build instead of remembered by reviewers](../../raw/brag/2022-02-18-cpp-safety-critical-embedded-guidelines.md). That is precisely the reasoning a certification-aware Rust adoption needs, applied once already.
2. **He works inside a regulated lifecycle**, [qualified into a medical-device QMS with design control, CAPA and supplier quality, under FDA, EU and Australian process](../../raw/brag/2024-09-24-current-health-hospital-at-home-qms.md) — so the evidence-generation half of the job is familiar rather than theoretical.
3. **He builds embedded platform code now**: [a component framework in embedded C with dependency injection, hierarchical state machines and aligned structured logging, modularized for open-source release](../../raw/brag/2024-05-08-ccf-capability-framework-lcm-open-source.md), plus [Conan packaging on JFrog Artifactory and ARM cross-compilation with sysroot and toolchain pinning](../../raw/brag/2022-04-06-conan-package-management-embedded-cross-build.md) — the toolchain layer where Rust adoption actually lands.

Supporting: intermediate Rust on the resume; "becoming an embedded Rust expert" named in his own notes as the *challenging* development goal he wanted; a 2021 note on his own board that the next device generation could incorporate Rust modules; and Rust among the 2026 study items.

## The gap, and the shortest path

**The gap is shipped Rust.** Studying it and wanting it are documented; no Rust artifact is.

Shortest path, and it is unusually well shaped here:

1. **Port one component of the open-sourced capability framework to Rust**, keeping the C API boundary, and write up what the port cost and what the compiler removed from the review checklist. It is his own code, already modular, already public-facing — the ideal first artifact.
2. **Write the enforceability comparison again, for Rust**: what the compiler guarantees, what still needs external analysis, where MC/DC stands, how crate admissibility would be argued to a quality organization. That document is a portfolio piece and a contribution the consortium ecosystem is short of.
3. Follow the consortium's working groups. Participation is visible, cheap, and exactly how this niche hires.

## The vocabulary to foreground

Embedded Rust · `no_std` · toolchain qualification · MISRA and coding-standard enforceability · static analysis baselines · MC/DC and coverage obligations · ISO 26262 / IEC 62304 / IEC 61508 · FFI and the C boundary · crate admissibility · cybersecurity regulation (CRA, ISO 21434).

## Stories to tell for it

- [Choosing the C++ standard on what static analysis can enforce](../../raw/brag/2022-02-18-cpp-safety-critical-embedded-guidelines.md) — the single best story for this audience, because it is the same argument one language earlier.
- [The component framework taken to open source](../../raw/brag/2024-05-08-ccf-capability-framework-lcm-open-source.md) — embedded C architecture with lifecycle discipline. **Its innovation presentation names Rust in `no_std` mode as the corner-stone of the bare-metal strategy for a future device**, with the owner stating that his own Rust expertise could decide whether such an effort succeeds — the strongest direct evidence for this candidate in the corpus.
- [Qualifying into the medical QMS](../../raw/brag/2024-09-24-current-health-hospital-at-home-qms.md) — the evidence-generation half.

## How to tell if this is the one

**Do step 1 and notice what the writing feels like.** This candidate rewards someone who enjoys arguing a language-and-tooling case to a sceptical quality organization as much as writing the code — and the C++-guidelines entry suggests he does. If the port is fun but the argument is a chore, the honest read is that Rust is a tool he wants, not a field he wants.

## Related

- [Regulated medical device software](regulated-medical-software.md) — the same regulatory world as it is today.
- [Database internals in C++ or Rust](database-internals.md) — the other Rust direction; this one keeps the embedded domain, that one leaves it.
- [Dream-job hub](dream-job-hub.md) · [specializations landscape](../analysis/2026-09-13-specializations-landscape.md).
