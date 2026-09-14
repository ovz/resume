---
title: "Held the statistical bar on device analytics, and kept the Data Science partnership working"
date: "2019 to 2026-05 (ongoing; documented evidence runs 2023-10 → 2026-05)"
thread: STAT
domains:
  - "data engineering"
  - "operational excellence and observability"
  - "ML products and GUIs"
context: "GreatCall and Best Buy Health — device analytics, the enterprise data warehouse, and the extended Data Science organization"
sensitivity: private-repo
resume-worthy: yes
---

# Held the statistical bar on device analytics, and kept the Data Science partnership working

## What I did

Two things that look separate and are not: I **argued for statistical reasoning where statistics is the right tool**, and I **replaced statistical theatre with a cheap decisive experiment** everywhere else. Knowing which situation you are in is the whole skill, and eighteen years commercializing decision-tree and ensemble machine learning is where I learned to tell.

**Hypothesis first, then the smallest experiment that can settle it.** On device questions — battery life above all — the default instinct around me was to gather more data and analyse harder. Usually a stated hypothesis plus an engineering build, a handful of devices and a notebook produced a clearer answer in days than a brute-force campaign would have produced in weeks, and a great deal of crude quasi-statistical effort never had to happen. When the question genuinely needed statistics, I said so and argued for real statisticians to be engaged rather than approximated.

**Holding the bar, repeatedly.** Statistical significance and sound statistical reasoning were subject to repeated bar-raising across both the GreatCall and the Best Buy Health eras — this was not one conversation but a standard that had to be re-established. The documented instances of me meeting it myself:

- **Reasoning about the anomaly-detection model rather than treating it as a black box**: applying ARIMA/SARIMA theory to fleet-scale monitors, and establishing *empirically* that partitioning the model by error category sharply cuts false positives — a hypothesis stated, then validated against real incident data.
- **Validating a monitor's first meaningful firing against independent evidence** — correlating it with MCU error alerts raised separately by firmware engineering, rather than accepting agreement with itself.
- **Setting an observation loop** to judge whether a monitor kept earning its place, instead of declaring victory at deployment.

**Staying aligned with Data Science, deliberately.** I presented the anomaly monitors to the extended Data Science team, asked leadership repeatedly to allocate Data Science capacity to the device domain, and developed a working tactic for a team with its own priorities: make clear I could do the work myself, so that the choice is between helping and being bypassed rather than between helping and waiting. Good outcomes came from the business taking the advice to involve proper statisticians; the cost of not doing it showed up as conclusions nobody could defend.

**Notebooks instead of spreadsheets.** The waste I kept seeing was enormous hand-built spreadsheets: slow to produce, impossible to re-run, and yielding conclusions that were poorly grounded and unclear even to their authors. The replacement was crisp Jupyter notebooks going straight at the warehouse — the data-usage analysis notebook kept in the device test-automation repository, the notebook produced from the 2026 keep-alive engineering build, warehouse queries per device-identity list — producing a result that is clear, re-runnable and authoritative, and that someone else can re-open a year later.

## Why it matters

Device telemetry at fleet scale is exactly the domain where a plausible-looking analysis is most dangerous: the sample is huge, the effects are small, the population is heterogeneous, and almost any hypothesis can be made to look true by a sufficiently motivated spreadsheet. Being the person in the room who could tell a real effect from a story — and who would rather run one decisive experiment than argue — is what made the observability programme's conclusions trustworthy enough to act on. It is also the least visible of my contributions, because its output is usually *work that did not happen*.

## Skills demonstrated

Applied statistics and time-series reasoning (ARIMA/SARIMA); experiment design and hypothesis framing; validating a signal against an independent one; Jupyter and warehouse SQL as the analysis surface; eliminating analytical toil; working across an organizational boundary with a specialist team that has its own priorities; machine-learning background applied as judgement rather than as tooling.

## What was blocked, cut short, or wrong

- **Data Science capacity for the device domain was something I had to keep asking for**, quarter after quarter, and the ask appears in my own development-support notes more often than the allocation appears. The tactic of signalling that I would do it myself was a workaround for a resourcing answer I never fully got.
- **The waste I eliminated is easier to evidence than the waste I only witnessed.** The spreadsheet-driven analyses I considered poorly grounded were other people's work, and this entry deliberately does not name them or characterize them beyond the practice.
- An **anomaly-detection initiative in the hospital-at-home context stayed with the platform team** rather than becoming mine, even though the technique was the same one I had already tuned on the device fleet.

## Evidence

The leadership board carries the quarterly-conversation records naming the Datadog anomaly-monitor presentation to the extended Data Science team and the repeated requests for Data Science capacity, the mentor thread setting out the prioritization tactic, and the one-on-one exchange offering to show the notebook from the keep-alive build. The device-programme board carries the data-usage notebook reference and the warehouse query notes. Both are the committed Trello snapshots. The ARIMA/SARIMA tuning and the monitor validation are their own entries, with their own evidence.

## Evidence limitations

- **This is the weakest-supported of the four bodies of material captured on 2026-09-13.** The practice is real and the adjacent entries are strong, but several of its specific claims — the occasions on which the business followed the advice to engage statisticians, the scale of the spreadsheet waste, and notebooks integrated *directly* into the warehouse as a standing pattern rather than as instances — rest on the owner's statement alone.
- What *is* independently documented is narrower and should carry any outward claim: statistical reasoning applied to a production anomaly model, a hypothesis validated empirically, a monitor checked against an independent signal, and notebooks in a repository rather than spreadsheets on a share.
- Prominence should follow that split — see [voice and prominence](../../wiki/workflows/voice-and-prominence.md).

## Related

- [2024-05-05-r5-anomaly-detection-arima-tuning](2024-05-05-r5-anomaly-detection-arima-tuning.md) — the documented centre of this practice: statistical theory applied, then a partition hypothesis validated against real incidents.
- [2025-05-29-r5-anomaly-monitor-validated-against-mcu-alerts](2025-05-29-r5-anomaly-monitor-validated-against-mcu-alerts.md) — validation against an independent signal, and the observation loop.
- [2021-10-16-battery-power-second-specialization](2021-10-16-battery-power-second-specialization.md) — the domain where the cheap-experiment half of this practice mattered most.
- [2024-01-04-cellular-cost-rogue-device-detection](2024-01-04-cellular-cost-rogue-device-detection.md) — a threshold agreed in advance and validated against a deliberately misbehaving device, rather than negotiated during an incident.
- [2022-05-18-snowflake-edw-device-telemetry](2022-05-18-snowflake-edw-device-telemetry.md) — the warehouse access that made notebooks a credible replacement for requested reports.

## Record history

- 2026-09-13: created from the owner's direct statement of 2026-09-13, grounded the same day in the committed Trello snapshots. Filed at the recent end of the range, where the documented evidence is; the 2019 start is the owner's dating of the practice, supported for that period only by the primary resume's account of introducing the team to data-science tooling during the 2019 relaunch.
