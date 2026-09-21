# Four problems, four solutions — a domain read as its problem space

> **Doc type:** explanation
>
> Russ White's habit of mind, applied to this career's domains: state the small set of
> problems anything in a domain must solve, enumerate the solution space for each, then
> point at where this record actually answered it. It is a **rehearsal and interview aid**
> — the thing to read before a conversation where someone asks what you understand about a
> domain rather than what you shipped in it. Audience: the owner preparing to speak; an
> agent drafting a story, a resume line or a reading list that needs a domain's shape.
>
> Not a claims inventory — that is [accomplishments by domain](accomplishments-by-domain.md)
> — and not a coverage tracker, which is [coverage.md](../resume/coverage.md). Nothing here
> is promotable on its own; the *Where this record answers it* column is what is promotable,
> and it is already tracked elsewhere.

## Why this shape

The heuristic comes from network architect **Russ White**, whose
[Rule 11 Reader](https://rule11.tech/) the owner names as one of his beacons as of 2026.
White offers it explicitly against the OSI model: he says he does not find OSI "very
useful in day-to-day work" and prefers "simpler yet extensible models", because a model
that tries to put everything in one place stops working as a thinking tool. What he wants
instead is **a mental map that makes you ask a useful question**.

That is the property worth stealing, and it is why this page exists for domains White
never wrote about. A layer diagram tells you where something sits. A problem list tells
you what to ask about it.

**One correction, carried deliberately.** The owner's paraphrase is "four basic problems
and four basic solutions in each domain". White's actual model names four problems with
**three** solution options each. The paraphrase is repaired here rather than reproduced,
for the reason given in the
[foundations entry](../../raw/brag/2026-09-20-network-programming-foundations-and-mentors.md)
— it is exactly the detail a networking interviewer notices. Downstream, "four problems"
is the load-bearing half; the solution counts vary by domain and are not forced to four.

**What is White's and what is not.** The *Networking* section below is White's own model,
cited to an article he wrote. **Every other section is this repository's derivation** — the
same method applied to the owner's record, not a published taxonomy. They are marked as
such and must not be attributed to him.

---

## Networking — Russ White's model, unmodified

Source: Russ White, *Beyond OSI: The "Four Things" Model Of Networking*
([Packet Pushers](https://packetpushers.net/blog/beyond-osi-the-four-things-model-of-networking/)),
corroborated by the structure of *Computer Networking Problems and Solutions* (White and
Ethan Banks, Cisco Press, 2017), which states a problem, enumerates its solution space,
and then shows which protocol chose what.

| # | Problem | White's solution space | Where this record answers it |
|---|---|---|---|
| 1 | **Marshaling** — format data so the sender transmits something the receiver understands | encoding; a shared dictionary and grammar; data protection | A hand-designed wire protocol whose two ends **could not drift**, because one set of shared sources built both client and server [daemon]. Twenty years later the same problem solved the opposite way: **LCM's type-specification language** as a shared grammar, chosen because manual marshaling on the device was error-prone — the owner's stated concept for it is *connascence of type* [lcm]. In between, a **wide-contract JSON telemetry event** designed so the schema could evolve without a firmware release [obs], and the array-based schema rewrite when quote-bearing keys turned out to be unqueryable [json] |
| 2 | **Multiplexing** — let more than two hosts share one physical or logical circuit | naming; mapping; routing | **Three named LCM channels over UDP multicast** — commands out, events back, and the manufacturer's log records across the process boundary — so any process on the device can subscribe and watch the conversation [lcm]. Earlier: **per-job isolation and lifetimes** inside one daemon serving many analysts [daemon]. At fleet scale the identifier *is* the mapping — carrier data, device telemetry and warehouse events joined **on IMEI** [cost] |
| 3 | **Flow control** — do not send faster than the receiver can consume | windows; queues; dropping data | The device's whole sync design is this problem under a power and money budget: **separating the schedule from the work scheduled**, so a reduced-activity mode suppresses optional dispatch while required maintenance and the MQTT cycle continue; queued messages accumulate and are **flushed** on success, with pending work distinguished from work in flight [mqtt]. The deliberate *drop* answer: **first occurrence sent, repeats counted** for a later summary, to bound diagnostic traffic on a metered link [http] |
| 4 | **Error control** — data must not be changed or damaged in transit | drop; request retransmission; attempt correction | The interesting answers here are about **what the application concludes** when control fails. Fire-and-forget HTTPS reporting returns no delivery result, so a quiet dashboard is **not** proof of a healthy device — and the failure modes are enumerated rather than assumed: broker down but IP up, DNS/TCP/TLS failure, stalled operation, dead executor [http]. When the IP path is gone entirely the device **degrades to SMS** rather than going dark [mqtt]. And a low-signal indicator is deliberately **not** an end-to-end reachability test: voice-service status, packet-data availability, TCP, TLS and broker health are five different observations [radio] |

**The gap to name out loud.** Routing — White's third multiplexing solution — is the one
box this record does not fill. There is no routing-protocol or switch-configuration
practice here, and the [networking variant](../resume/variants.md) is written so it never
implies otherwise.

---

## Derived sections

Everything below applies White's *method* to domains he did not write about. The problems
are this repository's, chosen because the record has something real to say about each.

### Positioning and location

| # | Problem | The solution space | Where this record answers it |
|---|---|---|---|
| 1 | **Getting a fix at all** — the sky is not always available | GNSS; Wi-Fi; cell ID; BLE proximity; dead reckoning from inertial sensors | A **Location Engine** unifying GNSS, Wi-Fi and BLE beacons behind per-provider interfaces [locengine]; the Skyhook upgrade on Qualcomm Linux Enablement [skyhook]; dead reckoning specified against heading and gyroscope-precession requirements [sensor] |
| 2 | **Choosing between disagreeing sources** | trust one; arbitrate by confidence; fuse; fall back on failure | A **state-management layer that arbitrates and falls back cleanly** when a provider fails, which is the engine's actual reason to exist [locengine] |
| 3 | **Paying for the fix** — every fix costs power, and sometimes bytes | duty-cycle it; ride wake-ups you are already making; push classification down the stack; answer a cheaper question instead | Location reports scheduled **in units of MQTT keep-alive intervals**, so they ride network wake-ups the device was making anyway [mqtt]; the design goal that positioning be a **non-issue** in the power budget [power]; home-or-away answered by **BLE beacon proximity** rather than by a fix [homeaway] |
| 4 | **Knowing the fix is wrong** | cross-check against an independent source; watch the fault paths, not the values | A **multithreading fault in a positioning library's listener thread**, found from fleet telemetry rather than from a bad coordinate [skyhookdiag] |

### Concurrency

| # | Problem | The solution space | Where this record answers it |
|---|---|---|---|
| 1 | **Shared state** | don't share; lock it; make it immutable; own it in one place | Races named precisely enough to be implemented in someone else's C: a queue predicate checked outside its mutex, a peeked pointer used after unlock, shared stop state under inconsistent locks [tcl] |
| 2 | **Lifetime across an asynchronous boundary** | shared ownership; capture the owner in the completion handler; cancel deterministically | The **use-after-move callback correction**: ownership was already right, the exceptional paths were invoking the moved-from object [http] |
| 3 | **Ordering and progress** | lock order; queues and executors; a single-threaded island | Executor and signal-handling boundaries on the application processor; callbacks delivered back onto their owning executor [mqtt]; a **documented lock order** required from the manufacturer before stress testing counted as evidence [tcl] |
| 4 | **The failure that will not reproduce** | reproduce the bug; or make the *evidence* reproducible | The method this record is actually known for: correlate independent subsystems, look for **the same operation happening twice**, treat a negative experiment as information, instrument for an occurrence you cannot schedule [audio] |

### Power and cost of operation

| # | Problem | The solution space | Where this record answers it |
|---|---|---|---|
| 1 | **Staying asleep** | duty-cycling; wake on interrupt; push work to a lower-power processor | A **sensor cluster and dedicated BLE MCU** between sensors and the application processor, with motion classified in the **sensor's own ML core**, so the AP never wakes [sensor] |
| 2 | **Deciding the budget before the hardware exists** | inherit it from the enclosure; or make it a researchable constraint decided first | Arguing the **battery budget must precede the form factor**, and naming that capable hardware costs power twice — once for the part, again for the software that uses it [power] |
| 3 | **Bytes are money, not just milliamps** | measure per device; set a threshold in advance; police the tail | Carrier, telemetry and warehouse data joined on IMEI to find individual units burning data — with the threshold **agreed before an incident**, validated against a deliberately built rogue device [cost] |
| 4 | **Proving any of it** | argue from datasheets; or measure | The standing habit: **a claim about a resource is not admissible without a measurement** — an engineering build, devices soaking, a notebook [cost] [power] |

### Embedded and safety-critical devices

| # | Problem | The solution space | Where this record answers it |
|---|---|---|---|
| 1 | **The thing must work when someone's life depends on it** | redundancy; controlled failure; independent paths to the same fact | Falls tracked **across a reboot** [primary]; overlapping radios and overlapping vitals argued as a **second independent path**, not waste, for a home with no nurse in the next room [integration] |
| 2 | **You do not own the whole device** | specify the boundary; keep the vendor replaceable; or own it ground-up | The manufacturer-facing specification set separating hard requirements from recommendations [odmspec]; the explicit **ground-up vs breadth-first vs hybrid** analysis, where the hybrid is named as the trap [integration] |
| 3 | **Every SKU drifts** | per-SKU branches; or one framework everything declares itself through | The embedded-C **component framework** — dependency injection, hierarchical state machines, aligned structured logging across every supported device [ccf] |
| 4 | **Correctness has to be checkable, not remembered** | review; runtime test; static enforcement | A C++ standard chosen on **what static analysis can actually enforce** rather than on reputation, with the guidelines authored against the existing baseline [cppstd]; **automated tests that run on the device** [primary] |

### Data engineering

| # | Problem | The solution space | Where this record answers it |
|---|---|---|---|
| 1 | **The data does not exist yet** | instrument the source; design the event before you need it | The wide-contract telemetry event, designed to evolve without a firmware release [obs] |
| 2 | **It exists but cannot be queried** | reshape it; or work around the platform | Quote-bearing JSON keys rejected by the platform's attribute rules, diagnosed and fixed with an **array-based schema** [json] |
| 3 | **Nobody knows what it means or who owns it** | tribal knowledge; a catalog with real stewardship | Official **Data Steward** on the enterprise catalog for device data, and the column-mapping framework behind it [steward] [colmap] |
| 4 | **Does it earn what it costs to keep?** | keep everything; or ask the question with lineage and usage | An AI-assisted data product scoped to answer exactly that for warehoused device events, combining lineage, query-log usage and glossary terms [aidata] |

### Operational excellence and observability

| # | Problem | The solution space | Where this record answers it |
|---|---|---|---|
| 0 | **Who is this for?** | nobody in particular; the developer who wrote it; the operator who carries the pager | Named explicitly, and it decides the rest of the table: the customers for platform and network software are network engineers, DevOps and on-call staff, so a signal earns its place by what it lets an interrupted expert do at 3 a.m. Runbooks, an agreed threshold and a tabletop exercise are that customer's product, not housekeeping [cost] [runbook] [releaseit] |
| 1 | **You cannot install an agent** | accept blindness; or design agentless | The **agentless** device-health architecture, chosen after establishing no conventional agent fit the RAM budget [obs] |
| 2 | **Too many alerts, or the wrong ones** | thresholds; seasonality-aware models; partition the model | Anomaly detection tuned from **ARIMA/SARIMA** first principles, with partitioning by error category established empirically to cut false positives [arima] |
| 3 | **Is the alert telling the truth?** | wait and see; or correlate with an independent signal | The first meaningful firing validated against **independent MCU alerts from firmware engineering** [mcualert] |
| 4 | **A monitor outlives its usefulness** | leave it; or steward the portfolio | Monitor-lifecycle review, retiring superseded coverage only once the replacement proved stable [monlife] |

---

## Using it

- **Before an interview in a domain**, read that domain's four rows and nothing else. Four
  problems is roughly what fits in working memory, and each row already carries the story
  that answers it.
- **When a question arrives that the record cannot answer**, the table shows which box is
  empty — say so and say why, per
  [voice and prominence](../workflows/voice-and-prominence.md) § *Blocked, frozen and never
  shipped*. Routing in the networking table is the model for this.
- **When drafting a resume variant**, the *Where this record answers it* column is a
  ready-made ordering: a variant that covers all four problems of its domain reads as
  understanding the domain rather than as having worked in it.

## Maintenance

- **The networking section is White's and is not edited** except to correct a
  misstatement of his model. Everything else is this repository's and may be revised as
  the record grows.
- **A new brag entry does not automatically earn a row.** Rows are the *best* answer the
  record has to a problem, not every answer; the inventory lives in
  [accomplishments by domain](accomplishments-by-domain.md).
- **Derived domains are a first pass, drafted 2026-09-20.** Positioning, concurrency and
  power are the most settled; data engineering and observability have the most room to
  change. Leadership has no section yet, deliberately — the method may not transfer to a
  domain whose problems are people, and that is worth deciding rather than assuming.

## Related

- [Accomplishments by domain](accomplishments-by-domain.md) — the claims inventory these rows point into.
- [Technical themes](technical-themes.md) — the same capabilities read as recurring threads rather than as problem spaces.
- [Network programming foundations](../../raw/brag/2026-09-20-network-programming-foundations-and-mentors.md) — where the heuristic came from, and the correction to the owner's paraphrase.
- [Resume variants](../resume/variants.md) — the networking variant this page was written alongside.
- [Voice and prominence](../workflows/voice-and-prominence.md) — how a gap in one of these tables is said out loud.

[daemon]: ../../raw/brag/2004-01-01-spm-client-server-tcpip-daemon.md "TCP/IP predictive-analytics daemon (2004-2005)"
[lcm]: ../../raw/brag/2025-01-16-ccfphone-r5-device-lcm-odm-integration.md "Phone capability SDK over LCM on R5 hardware"
[ccf]: ../../raw/brag/2024-05-08-ccf-capability-framework-lcm-open-source.md "Embedded component framework"
[http]: ../../raw/brag/2025-12-07-http-transfer-callback-ownership.md "HTTP transfer callback ownership and fire-and-forget reporting"
[mqtt]: ../../raw/brag/2026-07-29-cellular-mqtt-traffic-scheduling.md "Cellular MQTT keep-alive traffic scheduling"
[radio]: ../../raw/brag/2023-04-06-cellular-radio-quality-service-indication.md "Cellular radio quality and service indication"
[cost]: ../../raw/brag/2024-01-04-cellular-cost-rogue-device-detection.md "Cellular cost and rogue-device detection"
[obs]: ../../raw/brag/2023-12-21-device-health-observability-architecture.md "Agentless device-health observability architecture"
[json]: ../../raw/brag/2024-01-20-errorsummary-json-schema-datadog-limitation.md "ErrorSummary JSON schema limitation"
[arima]: ../../raw/brag/2024-05-05-r5-anomaly-detection-arima-tuning.md "Anomaly detection ARIMA/SARIMA tuning"
[mcualert]: ../../raw/brag/2025-05-29-r5-anomaly-monitor-validated-against-mcu-alerts.md "Anomaly monitor validated against MCU alerts"
[monlife]: ../../raw/brag/2025-01-14-r5-datadog-monitor-lifecycle-review.md "Monitor lifecycle review"
[runbook]: ../../raw/brag/2025-01-09-r5-self-reported-error-operational-runbook.md "Self-reported-error operational runbook"
[releaseit]: ../../raw/brag/2026-09-20-release-it-production-readiness-reading.md "Release It! production-readiness reading"
[locengine]: ../../raw/brag/2025-11-15-r5-location-engine-design.md "Location Engine design"
[skyhook]: ../../raw/brag/2025-05-01-qualcomm-skyhook-device-identity.md "Qualcomm Skyhook positioning and device identity"
[skyhookdiag]: ../../raw/brag/2024-05-15-skyhook-positioning-root-cause-diagnostics.md "Positioning root-cause diagnostics"
[homeaway]: ../../raw/brag/2023-11-27-r5-home-away-beacon-tracking.md "Home-away BLE beacon tracking"
[sensor]: ../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md "Dead reckoning and sensor-cluster architecture"
[power]: ../../raw/brag/2021-11-15-r5-product-architecture-power-budget-tradeoffs.md "Power budget trade-offs"
[audio]: ../../raw/brag/2023-09-26-audio-service-race-condition-diagnosis.md "Audio-service race-condition diagnosis"
[tcl]: ../../raw/brag/2026-04-24-tcl-audio-service-concurrency-corrections.md "Manufacturer audio-service concurrency corrections"
[odmspec]: ../../raw/brag/2022-08-03-odm-specification-authoring.md "Manufacturer specification authoring"
[cppstd]: ../../raw/brag/2022-02-18-cpp-safety-critical-embedded-guidelines.md "Safety-critical C++ guidelines"
[integration]: ../../raw/brag/2025-04-13-ble-sdk-breadth-first-white-label.md "Breadth-first white-label integration"
[steward]: ../../raw/brag/2025-01-01-data-steward-enterprise-data-catalog.md "Data Steward on the enterprise data catalog"
[colmap]: ../../raw/brag/2025-11-13-column-mapping-framework-alation-data-governance.md "Column-mapping framework"
[aidata]: ../../raw/brag/2025-10-29-ai-data-product-in-alation.md "AI data product in Alation"
[primary]: ../../../markdown/Oleg.Zhylin.resume.achievements.md "Primary resume (achievements)"
