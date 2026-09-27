---
title: "Release engineering across three parallel SPM 6.6 build tracks, and a full Japanese resource-table localization"
date: "2009 to 2010"
thread: SALF
domains:
  - "Build, release, CI/CD"
  - "Internationalization"
context: "Salford Systems — Salford Predictive Modeler (SPM) 6.6"
sensitivity: private-repo
resume-worthy: maybe
---

# Release engineering across three parallel SPM 6.6 build tracks, and a full Japanese resource-table localization

## What I did

Reviewed and steered the daily-to-weekly build/release cycle for **Salford Predictive Modeler (SPM) 6.6** across three parallel build tracks (the builds themselves were published by Jeff Powers, on the source-control and CI framework the owner set up with him in 2009) — English (`SPM_En`), Japanese (`SPM_Jp`), and license-protected (`SPM_protected`) — acting as the central reviewer and triager of Mantis bug reports spanning the GUI and the CART/TreeNet engine underneath it.

The largest single piece of it was a **full literal-string-to-resource-table localization effort** for the Japanese build (`SPM_Jp`, ILOC-based string replacement) — a genuine internationalization project restructuring how the codebase held text, not a pass of one-off string fixes. Alongside it, I made **platform-support-floor calls** — dropping Windows 2000 support and setting Windows XP as the minimum — weighing customer impact against the engineering cost of continuing to support an aging platform.

Correspondents on the Gmail threads this is drawn from: Jeffrey Powers, Phillip Colla, Bernie Bernstein, Igor Goncharov, Borys Tysik.

## What the mailbox shows (read 2026-09-25)

- **Autumn 2009, San Diego — the trip report.** On 10 October 2009 the owner summarised a working visit to the U.S. office for Dan Steinberg (in full): his top priority had been **getting Jeff Powers, the newly hired GUI developer, up to speed**, mostly through the Japanese build's testing and bug fixes; he had **extracted about 1,500 of the more than 2,000 string literals** pulled out of the source for localization, reviewed the extraction repeatedly for safety, and proposed a C++ mechanism to make string handling "innately safer" than C macros would allow; he maintained the Salford License Manager and the StatTransfer interaction layer (a build that understands non-ASCII file paths, and a test bed upgraded to unit-test form reusing the command-line build); and **"as a side-product of my work with Jeff we've established Source Control for SPM project … and Continuous Integration framework. Builds can now be created as frequently as needed at no effort."** He also took part in discussions of an SPM engine API "particularly for interaction with Minitab products" — seven years before the acquisition — and studied SEO for the company site. He was self-critical about the onboarding: "it appeared I didn't give Jeff enough guidance before we started literals crunching", and the better path was "an actual feature assignment". Dan: "We were all very happy with your trip … Yes, you qualify handily for the bonus."
- **Who ran the builds.** The "Current Update" build announcements for `SPM_En`, `SPM_Jp` and `SPM_protected` (October 2009 – May 2010) come from Jeff Powers; the owner's replies review them — a missing library in the protected build, Japanese resources not updated, `dlgBaseUnits` instead of hard-coded pixel sizes in dialogs, an upload script. The CI framework that produced them is the one he and Jeff set up.
- **December 2009 — Shift-JIS by default.** When Phil Colla added Shift-JIS translation behind an explicit `[SHIFTJIS]` suffix on `USE`, the owner argued that Japanese users expect their data to just work and proposed a default for the Japanese build: open as Unicode if detectable; otherwise a byte above 0x80 means Shift-JIS; otherwise ASCII — plus explicit encoding suffixes. Phil: "Actually, this is a good suggestion. It is much simpler than scanning for true two-byte Shift-JIS codes. I can implement this in the next version."
- **June 2010 — a Japanese feature.** "Cart Basic Lookup fully Japanese": he committed a functional CART Basic Lookup with a user's guide, and pushed the team toward a common build setup ("The loss of time is inevitable if everyone uses his own solution").

## Why it matters

This is release-engineering and internationalization ownership predating the resume's existing i18n entries (Unicode SPM is dated 2011 in the corpus; this pushes the effort's start back to 2009-2010) and predating the GitHub/monorepo-era build discipline captured from 2021 onward. It shows the same "own the release process end to end" pattern a decade before the later, better-evidenced instances.

## Skills demonstrated

Multi-track release management; cross-cutting bug triage across GUI and engine layers; internationalization architecture (resource tables vs. literal strings); platform-support-floor decision-making balancing customer and engineering cost.

## Evidence

A 2026-09-16 breadth-first Gmail survey (`oleg.zhylin@gmail.com`) identified this as a distinct thread, reached via CC'd/forwarded mail to `ovz@salford-systems.com`. The survey read snippets only, not full threads, and did not attempt to date individual releases or extract specific Mantis ticket counts.

## Evidence limitations

**Numbers now on record:** about 1,500 of 2,000+ string literals extracted by the owner (October 2009 trip report). **Still not recorded:** release cadence as a number, the Mantis backlog size, and the exact ILOC mechanics. The trip report and the Shift-JIS thread were read in full; the build-update threads from snippets.

**The survey's "ran the release cycle" framing is corrected above**: the owner reviewed and steered; Jeff Powers published the builds.

## Related

- [2010-01-01 SPM engine debugging — CART/TreeNet/MARS internals](2010-01-01-spm-engine-debugging-cart-treenet-mars.md) — the same build era's lower-level engine work.
- [2009-02-01 SPM_protected / Wibu-Systems CodeMeter integration](2009-02-01-spm-protected-wibu-codemeter-license-integration.md) — the third build track this entry names.

## Record history

- 2026-09-16: created, ingested from inbox note "gmail-brag-file-candidates.md" (candidate 1).
- 2026-09-25: mailbox read — the October 2009 trip report (string literals, onboarding Jeff Powers, source control and CI set up with him), the Shift-JIS default he proposed and Phil adopted, and the June 2010 Japanese feature; "ran the release cycle" corrected to reviewed and steered.
