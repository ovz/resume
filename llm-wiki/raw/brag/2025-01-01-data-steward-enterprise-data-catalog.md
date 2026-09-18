---
title: "Official Data Steward on the enterprise data catalog (Alation) — data governance for device data"
date: "2025 to 2026 (owner's recollection; start date not established — the filename date is a placeholder)"
thread: DATA
domains:
  - "Data engineering"
  - "Risk management and compliance"
context: "Best Buy Health — enterprise data catalog (Alation) and data governance"
sensitivity: private-repo
resume-worthy: yes
---

# Official Data Steward on the enterprise data catalog (Alation) — data governance for device data

## What I did

In the owner's words (2026-09-16): **"I am officially Data Steward in Alation. This is my Data Governance achievement, I believe 2025-2026 time frame. Data Governance dove tails nicely with Risk Management earlier achievement and security professional in general."**

The role is a formal one, not a description of attitude: in Alation, a *Data Steward* is an assigned catalog role responsible for curating a subset of the organization's data — its descriptions, ownership, glossary terms, quality and access policies — through the Data Governance app's Stewardship Workbench. The owner holds it for the device domain, which is where his earlier arguments pointed:

- **2022** — he argued for data-mesh-style ownership of device data by the team that produces it, after learning the warehouse well enough to stop depending on requested reports ([2022-05-18](2022-05-18-snowflake-edw-device-telemetry.md)).
- **2025** — as a steward, he scoped an AI-assisted data product to answer a governance question with cost attached: *do the warehoused device-event tables earn their storage and cellular cost?* — combining lineage, query-log popularity, glossary terms and prompt guidance that explains device-event semantics ([2025-10-29](2025-10-29-ai-data-product-in-alation.md)).

**Why it belongs with risk and security.** Data governance is risk management applied to data: who owns it, what it means, who may use it, and what it costs to keep. The same owner proposed *risk appetite* as the foundation of the Quality organization's risk practice ([2023-08-03](2023-08-03-risk-management-practice-early-analysis.md)) and wrote a NIST-grounded patch-management SOP ([2023-09-30](2023-09-30-security-patch-management-sop-and-vendor-engagement.md)). A data steward is the data-side instance of the same disposition; see [2026-09-16 stewardship as a first principle](2026-09-16-stewardship-first-principle.md).

## Why it matters

- **It turns a long-standing argument into an accountable role.** Arguing for data ownership in 2022 and holding the formal steward role later is the difference between an opinion and a responsibility someone assigned.
- **It is the rare governance role held by a device engineer.** The steward for device-event data understands what the events mean on the device, which is exactly what a catalog cannot infer from column names.
- **It rounds out the stewardship record**: security (patching, vulnerability feeds), risk (risk appetite), and now data.

## Skills demonstrated

Data governance and stewardship; enterprise data catalog curation (Alation); metadata, glossary and lineage design; data ownership models (data mesh); connecting data retention to storage and cellular cost; risk-based thinking applied to data.

## Evidence

- The owner's direct statement, 2026-09-16.
- Related, committed: the 2025-10-29 planning note for the AI data product on the catalog, and the 2022 data-mesh argument.
- Public grounding for what the role is: Alation, *Stewardship Workbench* — <https://www.alation.com/docs/en/latest/steward/StewardshipWorkbench/index.html>; Alation, *Understanding roles* — <https://www.alation.com/docs/en/latest/welcome/CatalogBasics/RolesOverview.html>; Alation, *The role of data stewards* — <https://www.alation.com/blog/role-of-data-stewards/>; general definition — <https://en.wikipedia.org/wiki/Data_steward>.

## Evidence limitations

- **The appointment itself rests on the owner's statement.** No role-assignment record, date, or scope of stewarded data is in this repository, and the personal mailbox holds nothing about it (corporate systems are not connected). The start date is not established; the filename date is a placeholder.
- **What was curated is not itemized.** Which tables, glossary terms or policies the owner stewarded is not recorded; the device-event domain is inferred from the related entries.
- Outward, the claim is the role and the domain — never internal table names, data volumes or policy details.

## What was blocked, cut short, or wrong

Nothing recorded yet. The AI data product in [2025-10-29](2025-10-29-ai-data-product-in-alation.md) was a brainstorm and plan; whether it was demonstrated is not recorded there either.

## Related

- [2026-09-16 Stewardship as a first principle](2026-09-16-stewardship-first-principle.md) — the principle this role is one instance of.
- [2025-10-29 AI data product in Alation](2025-10-29-ai-data-product-in-alation.md) — the stewardship work the role carried.
- [2022-05-18 Snowflake device telemetry](2022-05-18-snowflake-edw-device-telemetry.md) — the data-ownership argument that preceded it.
- [2023-08-03 Risk management practice](2023-08-03-risk-management-practice-early-analysis.md) and [2023-09-30 patch management SOP](2023-09-30-security-patch-management-sop-and-vendor-engagement.md) — the risk and security stewardship it dovetails with.

## Record history

- 2026-09-16: created from the owner's direct statement, with public grounding for the Alation Data Steward role.
