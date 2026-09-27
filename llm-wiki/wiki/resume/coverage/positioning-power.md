# Positioning And Power Coverage

> **Doc type:** reference
>
> Location, beacon tracking, battery and power trade-offs. Audience: brag ingest and resume promotion. [Coverage map](../coverage.md) owns totals, counting rules and shard routing; each claim below has one canonical home.

### POS — Positioning and location

Four entries, 2023–2026: a feature owned from its inception, field diagnostics, and the architecture.

**Entries:** [2023-11-27 Home/Away beacon tracking](../../../raw/brag/2023-11-27-r5-home-away-beacon-tracking.md) · [2024-05-15 positioning root cause](../../../raw/brag/2024-05-15-skyhook-positioning-root-cause-diagnostics.md) · [2025-11-15 location engine](../../../raw/brag/2025-11-15-r5-location-engine-design.md) · [2026-09-01 beacon FOTA persistence](../../../raw/brag/2026-09-01-r5-beacon-tracking-fota-persistence.md) · [2020-01-01 R4 location fix](../../../raw/brag/2020-01-01-r4-location-fix-engineer-to-engineer-borqs.md) · [2022-09-16 buying positioning and calendar time](../../../raw/brag/2022-09-16-skyhook-license-buy-calendar-time.md) · [2024-04-03 positioning-library descriptor leak](../../../raw/brag/2024-04-03-skyhook-file-descriptor-leak-reproduction.md)

**Thread coverage: 50%** (9 of 18)

| Claim | Source | Status |
|---|---|---|
| `POS-1` Root-caused a recurring positioning-library failure — a multithreading fault losing the location fix — via telemetry log correlation | 2024-05-15 | **in** |
| `POS-2` Identified the missing service-restart step that left the fallback path unable to fully recover affected devices | 2024-05-15 | absent |
| `POS-3` Reinterpreted an existing error-count signal as a proxy for time-without-fix, changing how the team thresholds it | 2024-05-15 | absent |
| `POS-4` Architected a modular location engine unifying beacon, GPS and Wi-Fi behind per-provider interfaces | 2025-11-15 | **in** |
| `POS-5` Built the state-management layer arbitrating between sources, with fallback when a provider fails | 2025-11-15 | **in** |
| `POS-6` Documented design and interfaces so other teams can extend the engine for new device variants | 2025-11-15 | **in** |
| `POS-7` Designed schema-backed persistence restoring paired beacon state across firmware-over-the-air updates | 2026-09-01 | **in** |
| ~~`POS-8` Kept devices in low-power beacon presence detection after updates instead of high-frequency polling, protecting battery life fleet-wide~~ — never customer-exposed, no fleet outcome | 2026-09-01 | struck 2026-09-14 |
| `POS-9` Hardened beacon/FOTA error categorization and made MCU reboot/fatal handling deliberate rather than incidental | 2026-09-01 | absent |
| `POS-10` Owned BLE beacon tracking from its inception, designing Home/Away as the simplest feature that answers home or away | 2023-11-27 | **in** |
| `POS-11` Drove the contract manufacturer's MCU and cradle BLE firmware to specification against a frozen cradle firmware | 2023-11-27 | **in** |
| `POS-12` Designed for optionality and held scope minimal (YAGNI) while consumers were out of scope, then argued for a location state machine as the next stage once top-down add-ons accreted | 2023-11-27 | partial |
| `POS-13` Named the long-running feature branch as technical debt while it accrued, and paid it down | 2023-11-27 | absent |
| `POS-14` Fixed degrading location on the previous-generation device through engineer-to-engineer work with the manufacturer's engineers and the chip vendor, becoming the company's positioning expert | 2020-01-01 | **partial** |
| `POS-15` Argued to license a commercial positioning service per device over home-grown fusion, on commercial-customer reliability and calendar time | 2022-09-16 | **in** |
| `POS-16` Evaluated the vendor SDK against the previous generation as the baseline before adopting it | 2022-09-16 | absent |
| `POS-17` Built a direct engineering relationship with the positioning vendor where chip-vendor communication otherwise routes through the manufacturer | 2022-09-16 | absent |
| `POS-18` Reproduced a third-party positioning library's slow file-descriptor leak (five days of uptime to appear) and, with designed experiments, ruled the library out and narrowed the leak to the device's location client | 2024-04-03 | absent |
| `POS-19` Escalated an earlier leak's library fix into the release after the manufacturer's update process held it back for almost a year | 2024-04-03 | absent |

> Corrected 2026-09-14: beacon tracking was an assignment owned since 2023 and never customer-exposed, so `POS-8` is struck and the beacon paragraph in *Projects Overview* was rewritten around `POS-10`–`POS-12`. `POS-4`–`POS-6` stay `in`; the engine entry's outcome claims are unconfirmed, see its limitations. `POS-2`/`POS-3` remain interview detail.

---

### PWR — Battery and power as a standing specialization

The owner's second major, and the same subject as `POS` seen from the power side. `DEV` holds the 2021 argument that started it; this thread holds the standing expertise and the judgement calls it enabled, through 2026.

**Entries:** [2021-10-16 battery and power as a second specialization](../../../raw/brag/2021-10-16-battery-power-second-specialization.md) · cross-listed: [2021-11-15 power budget](../../../raw/brag/2021-11-15-r5-product-architecture-power-budget-tradeoffs.md) and [2021-11-22 sensor cluster](../../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md) (claims under `DEV`)

**Thread coverage: ≈ 14%** (1 of 7)

| Claim | Source | Status |
|---|---|---|
| `PWR-1` Carries battery and power management as a second specialization alongside positioning, on a cellular wearable | 2021-10-16 | absent |
| `PWR-2` Established the mechanical interlock between the two: the fallback breadcrumbing interval specified in units of MQTT keep-alive intervals, so a location report rides an existing network wake-up | 2021-10-16 | **in** |
| `PWR-3` Holds a platform-level intuition for power on Qualcomm MDM-class SoCs — modem-versus-AP positioning, combo-radio beacon scanning, wakelocks, cellular power-saving modes | 2021-10-16 | absent |
| `PWR-4` Reduced battery questions from analysis campaigns to a stated hypothesis plus a cheap experiment, and has been consistently right in recent years | 2021-10-16 | absent |
| `PWR-5` Delivered the 2026 keep-alive production configuration, with a notebook from the engineering build and device soak testing to confirm the battery effect | 2021-10-16 | absent |
| `PWR-6` Advises product management and business partners on what will and will not move battery life before a quarter is spent finding out | 2021-10-16 | absent |
| `PWR-7` Cut a prototyping path short on his own finding that MCU-based positioning might not reduce the power budget — a negative result reached and acted on | 2021-10-16 | absent |

> `PWR-4` and `PWR-6` are the claims to watch: both are genuinely principal-level and both currently rest on the owner's own assessment, with no measured before/after committed. Promote them narrowly, or promote `PWR-2` and `PWR-5` instead, which are documented. See [voice and prominence](../../workflows/voice-and-prominence.md) § *Prominence follows evidence*.
