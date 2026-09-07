# Enterprise security patch management SOP and vendor security-feed engagement

- date: 2023-09-30
- context: Best Buy Health / Lively device security and vulnerability management
- domains: security, vulnerability management, vendor management, process design
- sensitivity: private-repo
- resume-worthy: maybe

## What I did

Drafted a Standard Operating Procedure for applying security patches to the device fleet's embedded Linux firmware, grounding it in NIST's Guide to Enterprise Patch Management Planning: the four risk responses (accept/mitigate/transfer/avoid), the principle that only patching/upgrading fully eliminates a vulnerability without losing functionality, and the need to verify a patch actually took effect once applied. Documented a patch-history lesson learned: an ODM partner's policy of applying upstream firmware patches immediately as they became available had introduced product instability, leaving the fleet on an old firmware branch that is now hard to bring current — informing a more deliberate, risk-based patch cadence going forward (the notes floated re-testing on a roughly six-month cadence as a possible trade-off). Also drafted outreach letters to two device-software vendors — a positioning-technology partner (Skyhook) and an over-the-air update vendor — asking how they notify and ship vulnerability patches and critical fixes, to formally establish security feeds ahead of a device launch.

## Why it matters

Moved the product's patch practice from ad hoc, vendor-push driven updates toward a documented, NIST-grounded, risk-based SOP — the kind of preventive-maintenance mindset the NIST guide argues improves security/business communication and consensus on planning. Named and preserved a concrete root cause of firmware staleness so it can inform future ODM engagement instead of repeating it. Initiated direct vendor conversations to establish ongoing vulnerability-notification channels, a prerequisite for sustaining the operational-excellence work already on the primary resume.

## Skills demonstrated

Security and vulnerability-management process design, applying a national framework (NIST SP 1800-31 family) to a real product, risk-based decision-making, root-cause analysis of a firmware lifecycle problem, technical writing (SOP/internal-wiki authoring), and vendor relationship management.

## Evidence

An internal wiki article draft (dated September 30, 2023) citing the NIST Guide to Enterprise Patch Management Planning, and draft outreach emails to two device-software vendors from the same date; internal artifacts not reproduced here.

## Record history

- 2026-09-06: created
