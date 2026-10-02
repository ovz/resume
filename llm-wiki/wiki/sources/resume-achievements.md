# Source: Achievements Resume (PRIMARY)

> **Doc type:** reference
>
> Summary of [`markdown/Oleg.Zhylin.resume.achievements.md`](../../../markdown/Oleg.Zhylin.resume.achievements.md) — the primary, outward-facing resume. Tier **T0 public** (mirrored to LinkedIn). Status: **live**. Rules for editing it are in [resume/primary-resume.md](../resume/primary-resume.md); this page records what the document *is* as of the 2026-09 review.

## Role in the corpus

The current edition of the resume the owner has used for several years. It descends from the archived [resume overview](resume-overview.md) (same Salford/Minitab/IIT spine) and adds the 2018–present Best Buy Health / GreatCall chapter, the target-role statement, the AI-since-2023 line, and the *Employment History* section. Every other resume variant in the repository is superseded by this one.

## Structure map (line numbers as of 2026-09-10, second pass)

| Lines | Section | Cut level ([primary-resume.md](../resume/primary-resume.md)) |
|---|---|---|
| 1 | Header include (`_parts/header.md`): portrait, name, contact line | C0 |
| 3–17 | *My Story*, six paragraphs: present scope and target role → languages and domains → security roots → Salford/Minitab ML era as systems work → GreatCall/Best Buy Health embedded era ending in regulated medical devices → AI since 2023. **Marked `linkedin: about`, 2,600 characters** | C1 |
| 19–39 | *Most prominent achievements* — 15 bullets (two added 2026-09-16: **stewardship practised by eliminating toil**, and **machine-learning engines from the inside**, which replaced the bare *Legacy code* bullet): architecture ownership; embedded emergency-response software; **concurrency and network programming as the embedded fundamentals, bare-metal MCU and hosted Linux alike (added 2026-09-16)**; positioning incl. the Location Engine; fall detection; regulated medical devices (QMS, Orcanos, Gen2, PPG); embedded platform frameworks; operational excellence (shared fragment); data engineering; ML GUIs; architecture breadth; API design; big data; legacy code; distributed-team management; Agile. **Added 2026-10-01, second position:** *Embedded software sold off the shelf* (shared fragment `_parts/bullet-retail-shelf.md`, also in the embedded variant) | C2 |
| 37 | *Side Note* include explaining Wayback Machine links | C2 boundary |
| 39–103 | *Employment History*, each section **marked `linkedin: experience-*`, 2,000 characters**: 41 Best Buy Health 2020–present; 55 GreatCall 2018–2020; 69 Minitab; 81 Salford Systems; 93 IIT. **Since 2026-10-01 the Best Buy Health and GreatCall bodies are shared fragments** (`_parts/experience-best-buy-health.md`, `_parts/experience-greatcall.md`), wrapped by the primary's `linkedin:` markers and included unmarked by the embedded variant | beyond C2, chronological |
| 105–332 | *Projects Overview*. Eight Best Buy Health sections (109 regulated medical devices, 123 the embedded component framework — renamed 2026-09-16 from the internal name to its public alias, 127 location engine, the 2023-2026 concurrency section added 2026-09-16, 133 FOTA escalation, 137 fleet observability, then security/risk, embedded platform, wearable power budget, and **2019–2026 on the shelf at Best Buy (added 2026-10-01; primary only — the elaboration behind the shared shelf bullet)**), followed by the Salford-era sequence to CART 4.0 | beyond C2, chronological |
| — | *Education* include, then Lyceum "Professional" | after experience |
| — | Reference-style link definitions (`_parts/links.md` include) | — |

**The 2018–present tenure is two sections, not one.** GreatCall 2018–2020 and Best Buy Health 2020–present, matching how the LinkedIn profile lists the positions. It is one continuous employment; splitting it doubles the LinkedIn Experience budget for the most relevant eight years of the record, and lets the early device work and the current architecture scope each be told properly. Both carry the same title string — see *Known defects*.

Line numbers move on every pass; the marked-section boundaries do not, and are the load-bearing part of this table.

## What only this document says

Claims that exist in no archived variant and therefore must be preserved here or in the wiki:

- Stewardship as a stated first principle, in chord with toil elimination, and the Data Steward role on the enterprise data catalog (2026-09-16).
- Engine-level debugging of the classic machine-learning implementations in Fortran and C/C++, alongside the statisticians who owned them (2026-09-16).
- Target role and the "work, not titles" positioning; "leveraging AI since 2023"; quality-left and toil-elimination themes; Principal-level scope across the Lively product line.
- Best Buy Health chapter: MVNO on Verizon; 2019 Lively Mobile+ relaunch and data-driven troubleshooting; 2024 Lively Mobile 2 launch; Qualcomm Skyhook positioning upgrade and collaboration with Qualcomm; Datadog-based operational excellence (observability, monitoring, incidents, runbooks, post-mortems) meeting an OKR; on-device automated test architecture and QA enablement; contractor onboarding; telemetry and process-monitoring subsystem designs; interview/hiring contributions.
- Fall detection: MCU signal filtering, subsystem coordination to place a call, persistence across reboot.
- Positioning SME: GNSS (GPS, GLONASS, Galileo), ECID, Wi-Fi, BLE beacons; diagnosed and fixed issues; major infrastructure upgrade.
- Acquisition project detail: migration completed in under a year; onboarding cut from 2–3 months to under a week; stable SPM 8.3 baseline; Nalpeiron licensing; NuGet reuse repository.
- Current contact details (Ashburn, VA).

## Known defects (fix via the update workflow)

**The 2026-09-06 list was cleared by the 2026-09-10 pass.** The stray asterisk after `Since **2018**`, the bare live `shop.lively.com` URL, the two references missing an opening bracket, the `[r5]` title attribute, and the unbalanced bold in the Codemeter paragraph are all fixed; the sections that carried most of them were rewritten outright.

What remains:

| Where | Defect | Fix |
|---|---|---|
| `_parts/links.md` | Live (unarchived) targets: `leo`, `olshen`, `chuck`, `databricks`, `dask`, `seaweedfs`, `mrocklin` | Archive per [link conventions](../resume/link-conventions.md), or accept as deliberate "identity" exceptions and say so there |
| `_parts/links.md` | Mixed `http://` and `https://` schemes on `web.archive.org` definitions | Harmless; normalize opportunistically |
| `_parts/links.md` | Unused keys inherited from the long resume (`treenet_first`, `oliphant`, `qml`, `milo`, `qt_installer`, `cppcheck`, `boundschecker`, `qydatatech`, `seaweedfs`, `mrocklin`, `pycon2014`, `pycon2016`, `pfa`, `rancher_os`, `rancher`, `freeipa`, `gitlab`, `wtl`, `gps_salford`, `salford_pipelines`, `treenet`, `cart`, `gitolite`, `redmine`, `clr_stored_procedures`, `intel_xe`, `dsteinberg`, `kaggle`) | Harmless. Keep for future harvest, or prune deliberately — but note the fragment is shared, so the embedded variant may use one the primary does not |
| Document structure | No C0 summary blockquote, though [primary-resume.md](../resume/primary-resume.md) § *cut map* describes one and the embedded variant has one | Add it, or amend the cut table. The two currently disagree |

**Resolved 2026-09-11:** employment titles. The owner keeps *Health Engineer Senior* for both 2018-onward positions, and the embedded variant was aligned to it.

## What it lacks (candidates from the archive)

Detail present only in the [archived long resume](resume-full.md): the in-house computational cluster project, Unicode/i18n process detail, the SPM 7.0 GUI framework work, Brazil retail ETL/WPF/WWF detail, IIT cryptography specifics (elliptic-curve thesis, full-disk encryption driver), and the *Personal development* section that could seed an optional *About me*. Whether any of it belongs at beyond-C2 depth in the primary is an owner decision made through the [update workflow](../resume/update-workflow.md).

## Related

- [Primary resume rules](../resume/primary-resume.md) · [Link conventions](../resume/link-conventions.md) · [Update workflow](../resume/update-workflow.md)
- [Source map](../sources.md)
