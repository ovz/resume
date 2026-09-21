---
title: "Separated optional device traffic from required work in a cellular MQTT keep-alive mode"
date: "2026-05-13 to 2026-07-29"
thread: PWR
domains:
  - "Embedded and safety-critical devices"
  - "Architecture and API design"
  - "Battery, power and cost of operation"
context: "Best Buy Health, Lively Mobile 2 cellular-connected medical-alert device"
sensitivity: private-repo
resume-worthy: yes
---

# Separated optional device traffic from required work in a cellular MQTT keep-alive mode

## What I did

I implemented and refined a reduced-activity operating mode for the device's periodic synchronization, separating optional work from required checks while retaining the MQTT communication path. The dated source history records my work on flush coordination in May 2026, configuration and component gating in July, and a July 29 merge of the keep-alive/beacon-tracking work.

This is the detailed networking implementation episode behind the broader [battery and power specialization](2021-10-16-battery-power-second-specialization.md). It is not an additional independent battery-saving result. My contribution was to reconstruct which activities actually belonged to the periodic cycle, make the controls coherent across their consumers, and preserve work that should not disappear simply because a low-activity mode was requested.

### Separate the schedule from the work scheduled

The periodic timer and the optional jobs it triggers are different things. Stopping a timer indiscriminately would also remove the opportunities to do required maintenance and progress the communication cycle. In the examined implementation the scheduler continues to reschedule; a separate configuration controls whether optional work is dispatched.

I worked through that separation at the component boundaries rather than treating "keep-alive only" as one boolean checked at the top of the whole system. The current path performs its resource-health check, dispatches mandatory sync participants and then conditionally dispatches optional participants. Successful completion requests an MQTT flush; a failed completion does not take that same success path.

### Keep resource protection active

A July 18 change specifically moved the file-descriptor check ahead of the optional-work suppression. **FD here means file descriptors, not fall detection.** That distinction matters on this product, which also has automated fall detection.

A reduced-activity mode is not permission to disable the checks that keep the process viable. File-descriptor exhaustion can prevent new sockets and other Linux resources from being opened. Preserving the existing recovery decision while reducing optional activity is a concrete example of treating network behavior and process health as connected concerns.

### Make automatic network-status queries optional without removing diagnostics

I moved the periodic network-information request to the optional-work dispatch and added a test asserting that the request is not sent when disabled. The related code and tests distinguish suppression, re-enabling and normal operation. An explicitly requested network query remains a separate path; reducing periodic activity need not remove the means to diagnose the device.

This is **cellular networking at the device integration boundary**: controlling when the application asks the modem-facing platform for network state and when that information participates in a telemetry cycle. It is not a claim to have implemented the cellular modem's protocol stack.

### Coordinate configuration across components

The work also consolidated shared sync configuration and carried enable/disable behavior through the components that consume it. Location activity, network-information requests and other periodic tasks cannot each interpret the same mode differently without making an experiment or a production configuration unreliable.

I added and maintained unit-test expectations around those boundaries. Test source is evidence of the intended contract and my implementation work; this capture does not claim a fresh test run.

### Named the change, and reconciled its configuration stories

The merge is PR #220, titled around "keep-alive-only mode" and "major-sync optional-task gating" — the same distinction as the component-boundary work above, expressed at the ticket level for firmware and operations audiences who read PR descriptions rather than source. I wrote the PR description to say when and why to use keep-alive-only, how it interacts with major-sync tasks, and what safety and monitoring guarantees remain in each configuration, so a future engineer or operator can adjust the settings without re-deriving the design from source.

Alongside the merge, I worked through a set of keep-alive configuration Jiras — reconciliation and in-home ('inside-home major sync') behavior tickets — that had accumulated inconsistent expectations about what "keep-alive-only" actually suppresses. That reconciliation work is the configuration-semantics half of this episode: making the settings mean one agreed thing across the tickets that referenced them, not a second independent feature. The inside-home major-sync ticket itself is part of the beacon-tracking add-on history, not a new claim here; see [beacon tracking](2023-11-27-r5-home-away-beacon-tracking.md) and its [2025-2026 add-on record](2026-09-01-r5-beacon-tracking-fota-persistence.md).

## MQTT mechanics I worked within

The inherited messaging stack makes this more than a timer exercise:

- The MQTT client/network executor is separate from the main application executor. Callback delivery back to application components is queued onto their owning executor.
- MQTT session keep-alive, the application's periodic synchronization, and the flushing of queued application messages are separate mechanisms. Tuning one does not automatically prove anything about the others.
- Messages can accumulate before a flush. Existing persistence and flush tracking distinguish pending work from work already in flight, including an initial backlog after reconnect.
- The existing client has connection-state handling, delayed reconnection, credentials and pause behavior. A functioning cellular link alone does not imply a connected broker session, successful authorization or a drained application queue.

These are the conditions my changes had to respect. I am not claiming original authorship of the broker, persistence engine, reconnect algorithm or MQTT implementation. Nor does requesting a flush prove that the broker or a downstream consumer received every message, or establish exactly-once processing.

## Continued operation when the IP path fails

My networking experience includes operating and maintaining a device that does not become wholly dependent on its TCP/IP data path. As I put it in the September 19, 2026 follow-up: **"r5 device operates even if TCP/IP stack is broken. There is a fallback on SMS so device is still in communication"**. The important product behavior is continued operation with a reduced set of communication capabilities, rather than treating an unavailable MQTT connection as a completely unreachable device.

The implementation makes that statement concrete. It has a modem-facing SMS path separate from the application's TCP/TLS sockets, and the command engine accepts messages from both SMS and MQTT. SMS is not merely a notification that the normal connection failed:

- **Event-triggered location communication:** the emergency-response path requests a cached location and sends its formatted report over SMS. The associated tests include the fall-detected event source.
- **Periodic alarm-location communication:** periodic location reports in that path are formatted and sent over SMS as well. Those sends do not first wait for an MQTT timeout; they provide an independently triggered channel rather than a generic resend of failed MQTT packets.
- **Inbound requests and supported replies:** communication tests and location requests can arrive over SMS, with corresponding result payloads returned over SMS when available. The location handler selects its response format according to the incoming transport.
- **Recovery of the normal messaging path:** supported SMS commands can change the broker connection configuration or pause MQTT. A management action intended to affect a broken broker connection need not require that same connection to deliver the action.

This is cellular **networked-system resilience**, kept separate from the radio-quality entry. The useful distinction is between an IP-based application path and the cellular messaging facility the platform exposes. It is not a claim that the modem or carrier uses no IP internally; SMS may itself depend on carrier technologies such as IMS.

### The failure boundaries matter

| Failure condition | What remains possible, and what does not follow |
|---|---|
| MQTT broker/session unavailable while IP remains usable | The separate HTTPS diagnostic endpoint may still be reachable; supported SMS communication remains a separate option. |
| Application TCP/IP data path unusable | HTTPS reporting and MQTT may both be lost, while local device functions and supported SMS location/command communication can continue if their own dependencies remain healthy. This is the owner's stated operating experience, supported by the separate source paths, not a new fault-injection result. |
| No fresh location fix | A cached-location path exists, but receiving a location message is not proof that its fix is fresh or accurate. A location request may also complete as a failure or without a reply payload. |
| SMS cannot be prepared or sent | Key retrieval, encoding/encryption, payload size and send-result failures are distinct failure modes. The queue retries failed sends within the requested attempt budget when failure results arrive; success is not assumed merely because a message was queued. |
| Modem, cellular service, platform messaging or the application executor also fails | SMS is not guaranteed to survive. The paths share hardware and execution dependencies, and this record does not claim continued communication through an arbitrary kernel failure or complete cellular outage. |

The HTTPS `report_chronic_error` mechanism remains a **best-effort diagnostic side channel**, described in the [HTTP record](2025-12-07-http-transfer-callback-ownership.md#fire-and-forget-https-failure-reporting). Its reports are not automatically converted to SMS, nor is every MQTT command or telemetry payload supported over SMS. Preserving selected care and recovery communication is different from preserving the complete cloud feature set.

The engineering experience I want to carry into networking-focused products is reasoning about those partial failures: identifying which dependency has failed, which function can continue, what information can still get out, and which recovery action is still reachable. The codebase already had the SMS architecture; I am claiming hands-on work within and understanding of this resilient product, not sole authorship of its fallback design.

## Why it matters

For a battery-powered device on a metered cellular connection, unnecessary application traffic spends both energy and data. The useful engineering question is not simply "can we make fewer requests?" It is which work can be suppressed, which checks must remain, how the mode resumes, and what observable behavior establishes that the experiment did what it intended.

My existing power record describes an engineering build, notebook analysis and device soak testing for this effort. The code history adds independently inspectable authorship and the actual control boundaries. Neither source supplies a publishable before/after battery measurement here, so this record claims the implementation and investigation, not an invented saving.

This is my recent network-facing product work, even though networking was not the product's main value proposition. In September 2026 I explicitly identified a goal of building products more dedicated to networking. The transferable experience is event-driven network-client engineering, separating liveness from useful application progress, controlling traffic generation, and making failure and recovery behavior observable.

## What was blocked, cut short, or wrong

The broader power record says this refactoring broke beacon tracking, that I found the breakage, and that resolving it cost the original estimate. I had argued for a simpler beacon design; its simplicity limited the repair. That is part of this episode, not a detail to lose when describing the networking work.

The state-machine record also preserves my concern that a cross-cutting mode was being implemented through accumulating conditions rather than clean lifecycle integration. This entry does not claim that a comprehensive state-machine redesign shipped.

"Keep-alive only" is a mode label, not a demonstrated promise of complete network silence apart from MQTT pings. Required work and independently triggered traffic remain distinct concerns.

## Skills demonstrated

MQTT application integration; event-driven C++ and executor boundaries; periodic scheduling; required-versus-optional work partitioning; cellular telemetry query control; batching and flush-completion reasoning; file-descriptor resource protection; shared configuration; negative test expectations; battery/data-cost experiment design; cross-component regression diagnosis.

## Evidence

- Owner-authored source changes dated May 13 and July 18-21, 2026; the keep-alive/beacon-tracking branch merge dated July 29 as PR #220 ("keep-alive-only mode / major-sync optional-task gating"), with a PR description covering when to use the mode, its interaction with major sync, and the safety guarantees retained. A separately supplied draft cited July 15, 2026 as an "impact date" for the same PR; the July 29 date is the one grounded in direct source/merge inspection and is treated as authoritative here.
- Current synchronization, platform network-query, MQTT and flush-tracking implementation; neighboring unit-test definitions for query suppression and resumption. Source identifiers and exact internal paths retained offline.
- [Battery and power specialization](2021-10-16-battery-power-second-specialization.md): contemporaneous board-derived account of the engineering build, notebook, soak tests, regression and architecture concerns.
- [Boost proficiency](2026-09-14-boost-library-proficiency.md): existing evidence for the event-driven architecture and cross-cutting-mode design concern.
- The owner's September 19, 2026 follow-up explicitly states continued R5 operation and SMS communication when the TCP/IP path is broken. Direct source review corroborates separate SMS ingress/egress, supported command and reply routing, broker recovery commands, and event-triggered/periodic location reports sent over SMS. Neighboring tests describe retries, queue processing, rejected inputs and location-message behavior; they were read, not executed.

## Evidence limitations

An authored change or merge is not proof of installation across the fleet. The source review did not run the firmware, exercise a broker, inspect packet captures or repeat battery experiments. There is no new measured battery improvement, byte reduction, throughput gain or fleet reliability statistic in this entry. Internal release labels, endpoints, configurations and telemetry volumes are deliberately not copied into this record.

The degraded-operation account combines the owner's direct experience with source-confirmed alternative communication paths. No new experiment disabled TCP/IP while demonstrating SMS, location or call behavior. No particular network incident date, recovery-time figure or fleet-wide survival rate is established. SMS design provenance predates the 2026 scheduling episode; it is recorded here as the operating context that gives that work its failure-mode significance.

This supports networked-device software engineering, not unearned claims of BGP/OSPF deployment, carrier-core implementation, congestion-control research or RF design. Radio signal-quality work is a separate accomplishment.

## Related

- [Cellular radio-quality indication](2023-04-06-cellular-radio-quality-service-indication.md): the separate radio-technology record; signal quality is not application-session health.
- [HTTP callback ownership](2025-12-07-http-transfer-callback-ownership.md): separate, directly authored transport correction and the carefully bounded HTTP/watchdog recollection.
- [Cellular data-cost investigations](2024-01-04-cellular-cost-rogue-device-detection.md): carrier/device/warehouse correlation, controlled traffic generation and an operational response to excessive usage; already captured, not duplicated here.
- [MQTT broker-test diagnosis](2024-12-31-device-test-automation-robot-framework.md): distinguishing laptop/VPN connectivity problems from a device or batching defect.
- [The TCP/IP predictive-job daemon](2004-01-01-spm-client-server-tcpip-daemon.md): earlier transport, concurrency and protocol-design foundation.

## Record history

- 2026-09-19: Created as the detailed networking implementation episode related to the existing power-specialization record, using direct source/history inspection and the owner's networking-career request. Capture only; no synthesis, coverage or public resume promotion.
- 2026-09-19: Expanded at the owner's request with continued operation under application TCP/IP failure, separate SMS location and command communication, recovery capabilities and explicit shared-dependency limits. This system-level experience is not recast as original SMS architecture authorship or a measured outcome of the scheduling change.
- 2026-09-21: Updated from an owner-supplied structured brag draft describing the same PR under the working name "keep-alive-only mode & sync gating" (PR #220). Added the PR number, the PR-description documentation practice, and the keep-alive-configuration/in-home-behavior Jira reconciliation. The draft's operational-metrics claims (battery-life deltas, traffic-byte reductions, ticket-rate changes) are **pending** and not recorded as achieved impact, consistent with this entry's existing evidence limitations; no new measurement is added by this update. Session-wiki capture: `20260921_brag-keep-alive-only-mode-sync-gating.md`.