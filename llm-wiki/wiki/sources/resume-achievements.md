# Source: Achievements Resume (PRIMARY)

> **Doc type:** reference
>
> Summary of [`markdown/Oleg.Zhylin.resume.achievements.md`](../../../markdown/Oleg.Zhylin.resume.achievements.md) — the primary, outward-facing resume. Tier **T0 public** (mirrored to LinkedIn). Status: **live**. Rules for editing it are in [resume/primary-resume.md](../resume/primary-resume.md); this page records what the document *is* as of the 2026-09 review.

## Role in the corpus

The current edition of the resume the owner has used for several years. It descends from the archived [resume overview](resume-overview.md) (same Salford/Minitab/IIT spine) and adds the 2018–present Best Buy Health / GreatCall chapter, the target-role statement, the AI-since-2023 line, and the *Employment History* section. Every other resume variant in the repository is superseded by this one.

## Structure map (line numbers as of 2026-09-06)

| Lines | Section | Cut level ([primary-resume.md](../resume/primary-resume.md)) |
|---|---|---|
| 1–5 | Header, contact line (email, cell, Ashburn VA address, LinkedIn) | C0 |
| 7–9 | Summary blockquote: engineer since 1996; C++ and Python; domains; SQL advanced, JS/C# working, Rust intermediate; neural networks for senior health & safety; target Sr. Principal / Sr. Staff; architect/lead/manager value; teams up to 15 | C0 |
| 15–27 | *My Story*: security roots (IIT) → Salford Systems 2000–2017 → Minitab 2017 → GreatCall/Best Buy Health since 2018 (MVNO, embedded devices, positioning, distributed systems, Datadog OKR, cross-team) → AI since 2023, quality-left, toil, Principal-level scope over Lively devices and apps | C1 |
| 29–41 | *Most prominent achievements* — 11 bullets: embedded emergency-response software; positioning SME (GNSS/ECID/Wi-Fi/BLE); fully automated fall detection; data engineering/ETL; ML GUIs; architecture breadth; API design; big data research; legacy Fortran; distributed-team management (15); Agile | C2 |
| 43–45 | *Side Note* explaining Wayback Machine links | C2 boundary |
| 47–83 | *Employment History*: 2018–present Best Buy Health (Lively Mobile+ relaunch 2019, Lively Mobile 2 launch 2024 with Qualcomm Skyhook on Qualcomm LE, ops-excellence, on-device test automation, contractor enablement, telemetry/process-monitor designs, hiring); 2017–2018 Minitab; 2000–2017 Salford Systems; 1996–2000 IIT | beyond C2, chronological |
| 85–255 | *Projects Overview*: 2017–2018 acquisition (13 bullets) → SPM 8.2 → Cloud-ready SPM → ISLE → Qt GUI → Predictive engines API → Hive scoring → Unicode/i18n → Codemeter → SPM 7.0 → Brazil retail → 64-bit → National Health Survey → client-server → CART 5.0 → CART C++/MFC → Navigator API → CART 4.0 | beyond C2, chronological |
| 257–269 | *Education*: NURE Master's (GPA 5.0), Thames Valley certificate, Lyceum "Professional" | after experience |
| 271–346 | Reference-style link definitions | — |

## What only this document says

Claims that exist in no archived variant and therefore must be preserved here or in the wiki:

- Target role and the "work, not titles" positioning; "leveraging AI since 2023"; quality-left and toil-elimination themes; Principal-level scope across the Lively product line.
- Best Buy Health chapter: MVNO on Verizon; 2019 Lively Mobile+ relaunch and data-driven troubleshooting; 2024 Lively Mobile 2 launch; Qualcomm Skyhook positioning upgrade and collaboration with Qualcomm; Datadog-based operational excellence (observability, monitoring, incidents, runbooks, post-mortems) meeting an OKR; on-device automated test architecture and QA enablement; contractor onboarding; telemetry and process-monitoring subsystem designs; interview/hiring contributions.
- Fall detection: MCU signal filtering, subsystem coordination to place a call, persistence across reboot.
- Positioning SME: GNSS (GPS, GLONASS, Galileo), ECID, Wi-Fi, BLE beacons; diagnosed and fixed issues; major infrastructure upgrade.
- Acquisition project detail: migration completed in under a year; onboarding cut from 2–3 months to under a week; stable SPM 8.3 baseline; Nalpeiron licensing; NuGet reuse repository.
- Current contact details (Ashburn, VA).

## Known defects (fix via the update workflow)

| Line | Defect | Fix |
|---|---|---|
| 25 | `Since **2018***` — stray asterisk after bold | `Since **2018**` |
| 27 | bare live URL `https://shop.lively.com/collections/shop-all-products` inline | pinned Wayback reference link, e.g. `[Lively devices and apps][lively_shop]` |
| 49 | `Best Buy Health][bbh]` — missing opening `[` | `[Best Buy Health][bbh]` |
| 51 | `Emergency Response device][r4]` — missing opening `[` | `[Lively Mobile+][r4] Emergency Response device` |
| 286 | `[r5]` title attribute says "Lively Mobile+" | "Lively Mobile 2" |
| 271–346 | live (unarchived) targets `leo`, `olshen`, `chuck`, `databricks`, `dask`, `seaweedfs`, `mrocklin`; several unused keys (`treenet_first`, `oliphant`, `qml`, `milo`, `qt_installer`, `cppcheck`, `boundschecker`, `qydatatech`, `seaweedfs`, `mrocklin`, `pycon2014`, `pycon2016`, `pfa`, `rancher_os`, `rancher`, `freeipa`, `gitlab`, `wtl`, `gps_salford`, `salford_pipelines`, `treenet`, `cart`, `gitolite`, `redmine`, `clr_stored_procedures`, `intel_xe`, `dsteinberg`, `kaggle`) inherited from the long resume | archive live targets per [link conventions](../resume/link-conventions.md); unused keys are harmless but may be pruned or kept for future harvest |

Also: the *Projects Overview* Codemeter paragraph (line 189) has unbalanced bold markers — `**[Reprise License Manager][rlm], **` lacks its closing `**`, and `**[Sentinel RMS - SafeNet][safenet].` likewise (inherited from the long resume).

## What it lacks (candidates from the archive)

Detail present only in the [archived long resume](resume-full.md): the in-house computational cluster project, Unicode/i18n process detail, the SPM 7.0 GUI framework work, Brazil retail ETL/WPF/WWF detail, IIT cryptography specifics (elliptic-curve thesis, full-disk encryption driver), and the *Personal development* section that could seed an optional *About me*. Whether any of it belongs at beyond-C2 depth in the primary is an owner decision made through the [update workflow](../resume/update-workflow.md).

## Related

- [Primary resume rules](../resume/primary-resume.md) · [Link conventions](../resume/link-conventions.md) · [Update workflow](../resume/update-workflow.md)
- [Source map](../sources.md)
