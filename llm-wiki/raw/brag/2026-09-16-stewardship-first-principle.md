---
title: "Stewardship and ownership as a first principle — security, data, technical and people — practised by eliminating toil"
date: "1996–present (practice; captured 2026-09-16)"
thread: STEW
domains:
  - "Leadership, management, hiring"
  - "Risk management and compliance"
  - "Security, cryptography, licensing"
  - "Operational excellence and observability"
context: "Career-wide: IIT, Salford Systems, Minitab, GreatCall, Best Buy Health"
sensitivity: private-repo
resume-worthy: yes
storied: [stewardship/records-nobody-asked-for]
---

# Stewardship and ownership as a first principle — security, data, technical and people — practised by eliminating toil

## What I did

In the owner's words (2026-09-16): **"Good stewardship and strong sense of ownership was always one of the first principles of my personal and professional life."** And: **"So I am a good steward from security standpoint, from software engineer technical standpoint, have management chops etc."** He asked that several kinds of stewardship appear in the resumes and stories, and that stewardship be put "in a chord with" the *eliminating toil* tagline.

This entry is a **capability entry**: it records the principle and points at the evidence already in the record, register by register, rather than restating it.

### The four registers, with the evidence for each

| Register | What stewardship means there | Evidence in the record |
|---|---|---|
| **Security and risk** | Treating the fleet, and the employer's information, as something held in trust | NIST-grounded patch-management SOP and vendor security feeds ([2023-09-30](2023-09-30-security-patch-management-sop-and-vendor-engagement.md)); risk appetite proposed as the foundation of the risk practice ([2023-08-03](2023-08-03-risk-management-practice-early-analysis.md)); substituting better controls rather than removing one ([2023-12-05](2023-12-05-operational-excellence-launch-readiness.md)); the security professional's reading of every system since IIT (primary resume) |
| **Data** | Owning what data means, who may use it, and what it costs to keep | Official Data Steward on the enterprise data catalog ([2025-01-01](2025-01-01-data-steward-enterprise-data-catalog.md)); data-ownership argument ([2022-05-18](2022-05-18-snowflake-edw-device-telemetry.md)) |
| **Technical** | Leaving a codebase, a portfolio or a pipeline in better condition than it was received | Stewarding an inherited state-machine architecture whose authors are gone ([2026-09-14 Boost](2026-09-14-boost-library-proficiency.md)); retiring a superseded monitor only once its replacement was stable ([2025-01-14](2025-01-14-r5-datadog-monitor-lifecycle-review.md)); naming fifty-plus brittle test protocols as technical debt at the moment they were incurred ([2025-07-18](2025-07-18-fota-vendor-escalation-lively-mobile2.md)); detailed records kept for years, which is what let an entire company's intellectual property be transferred under governance in the Minitab acquisition (primary resume, *Minitab*) |
| **People and organization** | Taking the unowned change instead of waiting; raising the bar in a way that compounds | Owning the embedded monorepo migration the platform group had no capacity for ([2021-08-15](2021-08-15-github-enterprise-migration-monorepo.md)); mentoring and bar-raising ([2025-05-28](2025-05-28-bar-raiser-practice.md)); defending an outsourced team's continuity to leadership ([2015-01-01](2015-01-01-mirabit-outsourcing-vendor-staffing-management.md)); freezing projects so they "can be resurrected effectively" at Minitab (primary resume) |

### Stewardship of the employer's own information

The principle also governs *how the record itself is told*. Internal names that sound generic — a framework's name, the conventional name of a microcontroller — are still the team's own words, so every outward surface describes them by function instead. The owner raised this himself on 2026-09-16; the aliases are recorded in [sensitivity tiers](../../wiki/workflows/sensitivity-tiers.md) § *Public aliases for internal names*.

### In a chord with *eliminating toil*

The owner's tagline — **passionate about shifting quality to the left and eliminating toil** — and stewardship are two halves of one idea: **stewardship is the why, eliminating toil is the how.** A steward is judged by the condition of what they hand on, and the most reliable way to leave a system in better condition is to remove the hand work it depends on, because hand work is where drift, fatigue and single points of knowledge live. The record is full of this: on-device test automation that cut test time by orders of magnitude and was handed to QA so it outlived his attention; onboarding cut from two or three months to under a week; a CI/CD pipeline that "saved the day" on hotfixes; a CI-generated build identity so no defect is ever traced to an anonymous package ([2022-04-06](2022-04-06-conan-package-management-embedded-cross-build.md)); agentless observability that replaced manual fleet investigation.

The industry vocabulary agrees on the definition that makes this a chord rather than a slogan: Google's SRE book defines toil as work that is "manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows" — <https://sre.google/sre-book/eliminating-toil/>. Work with enduring value is exactly what a steward is trying to leave behind.

## Why it matters

- **It is the thread that makes thirty years read as one career.** [Voice and prominence](../../wiki/workflows/voice-and-prominence.md) names a constant across the eras — the security professional's reading, raising the bar, grit without patience for toil. Stewardship is what those have in common.
- **It is well grounded.** Every register has at least two independent entries behind it, several already on the resume; this entry adds the principle, not new claims of fact.
- **It is rarer than it sounds in an individual contributor.** Governance roles, SOPs and risk frameworks are usually someone else's job; here they were taken on alongside the engineering.

## Skills demonstrated

Ownership; security, risk and data governance; technical debt management; inherited-codebase and portfolio stewardship; toil elimination through automation; discretion with employer information.

## Evidence

The linked entries in the table, and the primary resume's Minitab and Salford sections. The principle itself is the owner's statement of 2026-09-16.

## Evidence limitations

- **The principle is self-described.** What is evidenced is the behaviour in each register, not the principle; outward, it should be *shown* through those examples, never asserted as a virtue on its own — the same rule [voice and prominence](../../wiki/workflows/voice-and-prominence.md) applies to humility, respect and trust.
- **The inherited state-machine stewardship is owner-reported** (see the Boost entry's own limitations).

## Related

- [2025-01-01 Data Steward](2025-01-01-data-steward-enterprise-data-catalog.md) — the formal role.
- [2023-09-30 patch management SOP](2023-09-30-security-patch-management-sop-and-vendor-engagement.md), [2023-08-03 risk management](2023-08-03-risk-management-practice-early-analysis.md) — security and risk.
- [2025-01-14 monitor lifecycle review](2025-01-14-r5-datadog-monitor-lifecycle-review.md) — portfolio stewardship.
- [2023-01-30 system-monitor freeze counterexample](2023-01-30-system-monitor-freeze-counterexample.md) — the freeze done wrong, as a counterpoint to the Salford freeze.
- [2025-01-10 compliance-vehicle pushback](2025-01-10-pii-obfuscation-pushback-compliance-vehicle.md) — security stewardship: find the standard before writing the control.

## Record history

- 2026-09-16: created from the owner's direct statements, as a capability entry indexing existing evidence by register, with the toil-elimination chord grounded in Google's SRE definition of toil.
- 2026-09-16: graduated into the story [stewardship/records-nobody-asked-for]; body unchanged.
- 2026-09-24: reciprocal *Related* link to an entry created the same day.
