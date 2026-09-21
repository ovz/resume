---
cluster: production-readiness
aliases:
  - "Design for production stories"
  - "Fleet observability stories"
  - "Operator stories"
  - "On-call stories"
---

# Design for production, and the people who carry the pager — story cluster

> **Doc type:** reference
>
> Hub for the design-for-production cluster: the through-line, the stories planned and written, and the entries each draws on. This is the cluster the [story map](story-map.md) previously reserved as *Fleet observability* (`OBS`); it is widened here, because observability on its own is a capability, and the story worth telling is about **who it is for**. Audience: the owner in a conversation with an operations, platform, SRE or network organization; agents writing these stories.

## The through-line

**The software has a customer who is not the end user, and that customer carries a pager.**

Network engineers, DevOps and platform engineers, NOC staff and whoever is on call at three in the morning are the people who actually operate what gets shipped. They are technically expert, they are interrupted, and they judge software by how it behaves on its worst day rather than its best. Serving that customer well is difficult in a specific way: they cannot be surveyed, they will not file a feature request, and the only honest feedback arrives during an incident.

The owner's position, stated 2026-09-20, is that this is the most rewarding customer he has served — and that his observability, SOP, runbook and tabletop work should be read as **the product he built for them**, not as internal housekeeping adjacent to the real engineering. [*Release It!*](../../raw/brag/2026-09-20-release-it-production-readiness-reading.md) supplies the canonical form of the argument: a platform team has a customer-focused orientation, its customers are the developers and operators, and a separate "DevOps team" is a fallacy because the job is building mechanisms other people use rather than taking their tasks. The owner's own margin note on that passage is *"Enable, not just look for tasks."*

Three things make the claim credible rather than aspirational, and each is a story below:

- **He built the evidence layer when no agent would fit**, then owned the monitors as a portfolio rather than shipping them and leaving.
- **He wrote down the response so it did not depend on him** — runbooks, an SOP, and a tabletop exercise that rehearsed the scenarios before they happened.
- **He got a threshold agreed before an incident**, which is the part nobody does, and which is the difference between a number people act on and a number people argue about.

The economic register runs under all three and is worth surfacing early with an executive audience: monitoring, alerting and dashboards justify themselves in **cost of operation**, not in reassurance. The owner marked exactly that passage in *Release It!* and wrote *"Economic aspect of operational excellence."* His cellular-cost work is the same claim made in money.

## Stories

| # | Working title | The claim | Draws on | Status |
|---|---|---|---|---|
| PR1 | Nobody would take the agent, so we built the evidence anyway | No conventional monitoring agent fit the device's RAM budget, so the fleet got an *agentless* device-health architecture and a wide-contract telemetry event designed to evolve without a firmware release — and when the primary signal turned out to be unqueryable because of quote-bearing JSON keys, the schema was rewritten rather than the question abandoned | [2023-12-21 observability architecture](../../raw/brag/2023-12-21-device-health-observability-architecture.md) · [2024-01-20 ErrorSummary JSON schema](../../raw/brag/2024-01-20-errorsummary-json-schema-datadog-limitation.md) · [2024-03-07 monitoring launch](../../raw/brag/2024-03-07-r5-datadog-monitoring-launch.md) | **planned** |
| PR2 | The threshold we agreed before anything went wrong | Carrier data, device telemetry and warehouse events joined on IMEI to find devices burning real money; a rogue device built deliberately so detection could be validated against something known to be misbehaving; the threshold negotiated in advance, the runbook published, the scenario rehearsed in a tabletop — and a genuine offender found shortly after | [2024-01-04 cellular cost and rogue devices](../../raw/brag/2024-01-04-cellular-cost-rogue-device-detection.md) · [2025-01-09 self-reported-error runbook](../../raw/brag/2025-01-09-r5-self-reported-error-operational-runbook.md) | **planned** — the strongest of the cluster; it ends in money, which few observability stories do |
| PR3 | I retired my own monitor | Owning a monitor portfolio as a product rather than a delivery: alerts validated against an independent firmware signal before being trusted, superseded coverage retired only once its replacement proved stable, and broad fleet alerts converted into device-level questions firmware partners could act on | [2025-01-14 monitor lifecycle review](../../raw/brag/2025-01-14-r5-datadog-monitor-lifecycle-review.md) · [2025-05-29 monitor validated against MCU alerts](../../raw/brag/2025-05-29-r5-anomaly-monitor-validated-against-mcu-alerts.md) · [2025-05-01 device-specific investigations](../../raw/brag/2025-05-01-r5-device-specific-failure-investigations.md) | **planned** |
| PR4 | The error branch nobody ever runs | The owner's own extension of *Release It!*'s failure-mode argument: exception handlers and error paths are commonly first executed in integration testing and too often in production, and the economical place to exercise them is the unit layer — shift-quality-left applied to the category of code that most reliably escapes it | [2026-09-20 Release It! reading](../../raw/brag/2026-09-20-release-it-production-readiness-reading.md) · [2023-09-26 audio-service race diagnosis](../../raw/brag/2023-09-26-audio-service-race-condition-diagnosis.md) | **planned** — the one story in this cluster that is an *argument* rather than an episode; check it against [voice and prominence](../workflows/voice-and-prominence.md) before telling it, because an argument is the easiest thing to over-polish |

## Reach for these when

- **An operations, SRE, platform or network organization is on the other side of the table** — PR2 first. It is the one that ends in a number and a runbook rather than in a dashboard.
- **"Tell me about a time you improved reliability"** — PR1, then PR3 as the follow-up that shows you stayed.
- **"How do you think about monitoring?"** — lead with the economic framing, not the tooling. Then PR2.
- **"What would you do differently / what did the tooling not give you?"** — PR1's schema episode is the honest answer: the platform's own attribute rules made the primary signal unqueryable, and that was found in production.
- **A conversation about testing philosophy** — PR4. It is also the right story when someone asks what he reads and what he does with it.
- **An executive or cost-focused audience** — PR2, told from the bill rather than from the telemetry.

## Related, not conflated

- **This is not the crisis cluster.** The 2019 recall is its own story and is about a company coordinating under a deadline; this cluster is about the standing practice that exists so a crisis is measurable. Keep them apart — told together, the recall swallows everything else.
- **This is stewardship in its technical register**, and [stewardship](stewardship.md) says so from its side. ST1 is about custody; PR3 is about a portfolio. If both come up, tell ST1 and let PR3 be the follow-up.
- **Do not open with the book.** *Release It!* is the vocabulary and the corroboration, not the achievement. The work predates the reading, and a story that opens with what he read sounds like a book report rather than a record.

## Related

- [Story map](story-map.md) — every cluster.
- [Reliability coverage](../resume/coverage/reliability.md) § *OBS*, § *COST* — the claims behind these stories.
- [Four problems, four solutions](../concepts/four-problems.md) § *Operational excellence and observability* — the same domain read as its problem space.
- [2026-09-20 Release It! reading](../../raw/brag/2026-09-20-release-it-production-readiness-reading.md) — where the operators-as-customers framing is argued and sourced.
