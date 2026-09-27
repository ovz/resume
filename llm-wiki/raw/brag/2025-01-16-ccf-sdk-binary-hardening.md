---
title: "Built the SDK's binaries and supply chain to an information-security standard"
date: "2024-07 to 2025-01 (hardened device toolchain 2025-01-16)"
thread: RSK
domains:
  - "security, cryptography, licensing"
  - "embedded and safety-critical devices"
  - "risk management and compliance"
context: "Best Buy Health, component framework and phone capability SDK for PERS devices"
sensitivity: private-repo
resume-worthy: yes
---

# Built the SDK's binaries and supply chain to an information-security standard

## What I did

The security posture of the SDK is not a document; it is in the build, the dependency layout and the house style.

### Hardening that is actually in the build

The device toolchain file for the SDK does not merely cross-compile — it compiles and links every binary with a deliberate exploit-mitigation set. In the flags themselves:

| Mitigation in the build | What it defends against |
|---|---|
| `-fstack-protector` and `-fstack-protector-strong` | Stack-smashing: canaries detect buffer overruns before a corrupted return address is used |
| `-Wa,--noexecstack` and `-Wl,-z,noexecstack` | Executing injected code from the stack — the classic shellcode path |
| `-pie` / `-fpie` | Position-independent executables, which is what makes address-space layout randomization effective on the target |
| `-Wl,-z,relro,-z,now` | Full RELRO with immediate binding: the relocation table is made read-only, closing GOT-overwrite hijacking |
| `-s` | Symbols stripped from the shipped binary, raising the cost of reverse engineering |

That set is the recognized baseline for hardened Linux binaries, applied to an **ARM device target** where it is far less automatic than on a modern desktop distribution — the toolchain is an older OpenEmbedded GCC and every flag had to be put there on purpose.

### The supply chain, made inspectable

- **Third-party open source is vendored with its provenance in the directory name**, recording both the upstream project and its author or organization rather than an anonymous `third_party` folder. Anyone auditing the tree can see what came from where without consulting a separate manifest.
- The vendored dependencies are **pinned to specific public release tags**, not floating branches.
- One of them ships its own security policy and fuzzing harnesses in the vendored copy, so the fuzz-testing provenance travels with the code.
- The SDK's own dependency footprint is deliberately small — ANSI/C99 with minimal dependencies and predictable memory use was a stated requirement of the SDK programme, which is itself a security property on a constrained device.

### The trust boundary, stated in the source

A header in the tree is explicitly marked as a public include file distributed to parties outside the company. The boundary between code the company owns and code a manufacturer supplies is therefore visible in the source, not only in a contract — and the process split that goes with it means the manufacturer's service and the company's application are separate address spaces communicating over a defined message contract.

### Defensive coding conventions, enforced as house style

The codebase's written C style encodes defenses rather than preferences: **Yoda conditionals** (`if (NULL == ptr)`) adopted explicitly to make an accidental assignment in a comparison a compile error; a zero-terminated-string convention; a ban on relative include paths; and rules for executable lifecycle and memory footprint. The framework's state machine carries a **re-entrancy guard** that returns a distinct error rather than allowing recursive dispatch, and input validation is a first-class part of every return-value enumeration — invalid argument, uninitialized, dependencies uninitialized — rather than an assertion that vanishes in a release build.

## Why it matters

- **It is security built in at the point where it is cheapest and most durable.** Mitigations set in a toolchain file apply to every binary the SDK produces, for every device that consumes it, without anyone remembering to do anything. That is the same principle as choosing a C++ standard on what static analysis can enforce: put the rule where the build checks it.
- **It gives a device SDK a real answer to a security review.** "Compiled hardened, dependencies pinned and attributable, trust boundary explicit, input validated at every entry point" is a set of claims an auditor can verify, rather than assurances.
- **It connects two parts of the owner's record that are usually kept apart** — the Ukrainian Data Security degree and early cryptography engineering at one end, embedded platform work at the other.

## Skills demonstrated

Embedded binary hardening and exploit mitigation (stack protection, NX, PIE/ASLR, RELRO); toolchain-level security configuration for ARM targets; open-source supply-chain provenance and pinning; trust-boundary design across an organizational boundary; defensive C coding standards; input-validation discipline.

## Evidence

The retained working copies of the SDK and framework repositories contain the device toolchain file with the full mitigation flag set, the provenance-named vendored open-source directories with pinned release tags, the public ODM-facing header carrying its distribution notice, the written C and C++ style guides including the accidental-assignment rule, and the state machine's re-entrancy guard and return-value enumerations. Commit history dates the style rules to July–November 2024 and the hardened device toolchain to January 2025.

## Evidence limitations

- **The hardening flags are in the build; their effect was not measured here.** No penetration test, binary-analysis report (`checksec` or equivalent), threat model or security review finding is retained. The claim is that the mitigations are configured, not that the device was proven secure.
- **Authorship of the toolchain file is not separable from this evidence alone.** Cross-compilation flag sets of this shape are commonly inherited from a platform SDK environment, and the file's own comments say most cross-compilation flags were taken from the SDK environment. The honest claim is that the owner carried them into this project's build and understood what they were for — not that he originated them.

## The compliance judgement he brings — owner's position, captured for a future entry

From the owner's own working notes: he pushes back when teammates add ad-hoc obfuscation of values such as device identifiers or coordinates "in the spirit of PII protection", arguing that without a certification document, a planned third-party audit or an enterprise static-analysis scanner in the path, self-invented obfuscation is not compliance — it creates work to build it, work to test it, work to consume the obfuscated data, and leaves the real compliance cost unchanged. His rule is the simple one: keep personally identifying data out of logs, and leave technically meaningful values intact. He grounds this in a Data Security degree and says compliance skills carry responsibility with their power.

This is a distinct accomplishment about engineering judgement rather than about this SDK, and it is recorded here only so it is not lost. **It now has its own entry**, [2025-01-10](2025-01-10-pii-obfuscation-pushback-compliance-vehicle.md), built on the owner's fuller statement of 2026-09-24 and the industry rules it meets.

## Related

- [2025-01-16 phone capability SDK on R5 hardware](2025-01-16-ccfphone-r5-device-lcm-odm-integration.md) — the binaries these mitigations apply to, and the process boundary named here.
- [2024-05-08 component framework](2024-05-08-ccf-capability-framework-lcm-open-source.md) — the framework whose style rules and state machine carry the defensive conventions.
- [2025-11-13 Column Mapping Framework](2025-11-13-column-mapping-framework-alation-data-governance.md) — the work that actually reached Cyber Security leadership, and where the owner's information-security argument is made.
- [2023-09-30 security patch management SOP and vendor engagement](2023-09-30-security-patch-management-sop-and-vendor-engagement.md) — the fleet-level security practice; this entry is the same concern at build time.
- [2022-02-18 C++ safety-critical embedded guidelines](2022-02-18-cpp-safety-critical-embedded-guidelines.md) — the earlier instance of the same principle: choose rules the toolchain can enforce.
- [2026-09-16 stewardship as a first principle](2026-09-16-stewardship-first-principle.md) — security and risk as one of the registers of stewardship.

## Record history

- 2026-09-19: created from a direct study of the retained SDK and framework working copies, plus a presentation claim.
- 2026-09-20: **the presentation was removed from this entry — it did not belong here.** The talk the owner gave to Cyber Security leadership was about the Column Mapping Framework and data governance, not about this SDK hardening work; attaching it here was an inference error made while ingesting. It now has its own entry. This entry was renamed accordingly and is purely the build-and-supply-chain record, which is entirely source-grounded.
- 2026-09-24: pointer to the new compliance-judgement entry.
