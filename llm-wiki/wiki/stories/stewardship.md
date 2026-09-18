---
cluster: stewardship
aliases:
  - "Stewardship stories"
  - "Ownership stories"
  - "Toil stories"
---

# Stewardship, and eliminating toil — story cluster

> **Doc type:** reference
>
> Hub for the stewardship cluster: the through-line, the stories planned and written, and the entries each draws on. Open this note's local graph to see the cluster as a sub-graph. Audience: the owner asked what he stands for, or asked about ownership, governance, security or process; agents writing these stories.

## The through-line

**Stewardship is the why; eliminating toil is the how.** The owner's first principle is that what you hold — a codebase, a fleet, a dataset, a team's process — is held in trust, and you are judged by its condition when you hand it on. The practice that follows is unsentimental: the most reliable way to leave something better is to remove the hand work it depends on, because hand work is where drift, fatigue and single points of knowledge live.

It shows in four registers, and the useful thing in a conversation is that they are the *same* disposition rather than four interests: **security and risk** (a NIST-grounded patch SOP, risk appetite proposed as the foundation of a risk practice, better controls substituted rather than controls removed), **data** (the formal Data Steward role on the enterprise catalog for device data), **technical** (inherited state machines whose authors have gone, a monitor portfolio retired carefully, technical debt named at the moment it is incurred), and **people and organization** (taking the unowned migration, raising a bar that compounds, defending a team's continuity to leadership).

The register that makes it concrete for a listener is the one where custody was the whole job: an acquisition.

## Stories

| # | Working title | The claim | Draws on | Status |
|---|---|---|---|---|
| ST1 | [I kept records nobody asked me for, and years later they moved a company](stewardship/records-nobody-asked-for.md) | Two decades of records kept as a matter of course are what let an entire company's intellectual property transfer under governance inside a year, with frozen projects left resurrectable and onboarding cut from months to under a week | [2026-09-16 stewardship as a first principle](../../raw/brag/2026-09-16-stewardship-first-principle.md) · primary resume, *Minitab* | **draft written** |
| ST2 | Do these tables earn what they cost to keep? | The Data Steward role on the enterprise catalog, and the AI-assisted data product scoped to answer a governance question with a cost attached — the 2022 argument for device-data ownership coming back as an assigned responsibility | [2025-01-01 Data Steward](../../raw/brag/2025-01-01-data-steward-enterprise-data-catalog.md) · [2025-10-29 AI data product](../../raw/brag/2025-10-29-ai-data-product-in-alation.md) · [2022-05-18 Snowflake telemetry](../../raw/brag/2022-05-18-snowflake-edw-device-telemetry.md) | **planned** — needs the owner's answers on dates and what was stewarded |
| ST3 | Patching immediately is not patching deliberately | Root-causing firmware staleness to a partner's patch-on-release policy, then writing the NIST-grounded SOP and opening vendor security feeds before a launch — security stewardship of a fleet somebody wears | [2023-09-30 patch management SOP](../../raw/brag/2023-09-30-security-patch-management-sop-and-vendor-engagement.md) · [2023-08-03 risk management](../../raw/brag/2023-08-03-risk-management-practice-early-analysis.md) | **planned** |
| ST4 | The bar, and the successor who would not hold it | Holding a professional bar in his twenties when the colleague hired to carry it did not, and making the tooling case anyway — stewardship as what you do when the designated owner is absent | [2012-01-01 Git/RedMine modernization](../../raw/brag/2012-01-01-salford-git-github-redmine-modernization.md) | **planned** — tell it per [voice and prominence](../workflows/voice-and-prominence.md) § *Humility, respect and trust*: the disagreement is about the work, never a verdict on the person, and no name |

## Reach for these when

- **"What do you stand for?" / "What kind of engineer are you?"** — ST1. It answers with a fact rather than an adjective.
- **Governance, compliance, or data-ownership conversations** — ST2 once written; until then ST1's follow-up on the Data Steward role.
- **Security-minded roles** — ST3, then the cryptography roots from the IIT era.
- **"Tell me about eliminating toil" or a conversation about automation and process** — ST1's toil follow-up, then the on-device test automation handed to QA.
- **An acquisition, a wind-down, a migration, or any role where somebody must hold continuity** — ST1 is the whole point.

## Related, not conflated

- **Stewardship is not the same story as raising the bar.** Raising the bar is about the standard set for others; stewardship is about the condition of what is handed on. ST4 sits on the border and is told as stewardship.
- **The observability arc is stewardship in its technical register**, but it is a bigger story about evidence and belongs to its own cluster when that is written — keep ST1 focused on custody.
- **Do not recite the principle.** [Voice and prominence](../workflows/voice-and-prominence.md) applies the same rule to stewardship it applies to humility, respect and trust: let the story show it, and never open with "I am a good steward".

## Related

- [Story map](story-map.md) — every cluster.
- [Leadership and risk coverage](../resume/coverage/leadership.md) § *STEW* — the claims behind these stories.
- [2026-09-16 stewardship as a first principle](../../raw/brag/2026-09-16-stewardship-first-principle.md) — the evidence indexed by register.
