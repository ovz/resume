---
title: "Corrected callback ownership in asynchronous HTTP file transfers"
date: "2025-12-07; related HTTP test investigation documented 2023-04-17"
thread: CONC
domains:
  - "Architecture and API design"
  - "Embedded and safety-critical devices"
  - "Quality and test automation"
context: "GreatCall / Best Buy Health, cellular-connected medical-alert device software"
sensitivity: private-repo
resume-worthy: yes
---

# Corrected callback ownership in asynchronous HTTP file transfers

## What I did

I corrected a use-after-move error in the shared C++ HTTP transport used by the device software. It affected the early failure paths for both receiving an HTTP response into a file and sending a file-backed HTTP request. The dated source change attributes both corrections to me on December 7, 2025.

The completion callback had already been moved into shared ownership so it could survive until asynchronous I/O finished. If opening the local file failed before network I/O began, however, the error branch still invoked the original, moved-from callback. I changed both branches to invoke the callback through its owning object instead. The fix was small because the ownership model was already appropriate; the exceptional paths were using the wrong object.

This is specifically a **callback ownership and error-delivery correction**, not a claim that moving a request corrupted an HTTP payload. The same ownership discipline has to hold whether an operation completes over the network or fails locally before it starts. A moved-from callable is not a dependable way to report that failure.

I also maintained the neighboring HTTP test infrastructure. A separate same-day change made the tests create their required sandbox directories. An earlier April 2023 change records an investigation into intermittently failing HTTP-client tests. These are separate pieces of evidence: neither test-maintenance activity by itself proves the callback defect was reproduced by a dedicated regression test.

## Fire-and-forget HTTPS failure reporting

My networking experience on this product also includes its self-reported-error path, `report_chronic_error`, whose reports I used in [operational diagnosis and runbook work](2025-01-09-r5-self-reported-error-operational-runbook.md). It is a direct **HTTPS POST to an error-reporting endpoint**, not an MQTT telemetry event. On September 19, 2026 I explicitly asked that this mechanism and the device's behavior under network failure be included in my networking record.

**Fire-and-forget describes the caller's contract, not an absence of HTTP response processing.** The reporting function returns no delivery result. Internally, it starts an asynchronous connect, write and read sequence, retains the objects required by the completion handlers, and has a timeout that closes the connection. Connect, write and read failures are logged locally rather than returned to the component that reported the original error. The original operation's own success, failure or recovery decision does not become conditional on receiving an HTTP acknowledgment for its diagnostic report.

The error-code overload sends the first occurrence of an exact error message and counts repeats for a later summary, limiting repeated report traffic. The raw-payload overload is a separate path without that deduplication. This is meaningful network behavior on a metered cellular device, but it is not reliable-delivery storage: a send attempt is not proof of endpoint acceptance, and submitting a summary clears its counters without waiting for confirmed delivery.

### Failure modes I have to reason about

- **The broker is unavailable, but IP connectivity still works.** Direct HTTPS reporting does not require the MQTT broker session, so the diagnostic path has a different application-service dependency. That does not make it independent of the shared IP path.
- **DNS, TCP or TLS fails, or the reporting endpoint cannot be reached.** The report can fail even while the application continues doing useful work. A quiet monitoring dashboard is therefore not proof of a healthy device.
- **The reporting operation stalls.** The asynchronous timeout provides a close path, but depends on a functioning executor; it is not an independent hardware watchdog and does not prove a hard deadline under event-loop starvation.
- **The error-reporting executor is unavailable.** The direct entry point logs that condition rather than delivering a report. The surrounding application has a separate local error-dump/replay mechanism; it must not be described as a guaranteed retry queue for every failed HTTPS send.
- **The application's TCP/IP data path is broken.** Both MQTT and HTTPS may be unavailable, yet the device need not lose all communication. Its SMS command path provides a separate, narrower means of communication, covered in the [network failure and SMS fallback account](2026-07-29-cellular-mqtt-traffic-scheduling.md#continued-operation-when-the-ip-path-fails).

The experience worth recording is working on a connected device whose fault reporting and recovery cannot assume that the network is healthy. I distinguish an application's local failure, a failed attempt to report it, and loss of a communication channel, because those conditions demand different operational conclusions. I am not claiming original authorship of the inherited error-reporting transport.

## Networking substance

The implementation I worked in separates several responsibilities:

- **Connection establishment:** a common socket abstraction serves plain TCP and TLS-wrapped sockets, with hostname resolution, connection establishment and secure handshaking beneath the HTTP layer.
- **HTTP framing and transfer:** Boost.Beast performs asynchronous reads and writes; string-backed and file-backed bodies have different local-resource lifetimes.
- **Lifetime across completion:** request, response, buffer and callback ownership must survive the initiating function returning. Capturing the owning objects in completion handlers is essential, not incidental allocation.
- **Failure classification:** a local file-open failure is not a server response, a TLS failure or a request deadline. It still has to reach the caller through the agreed completion path.
- **Operation policy above transport:** activation-related HTTP operations distinguish successful responses, retryable server responses, terminal responses, transport failures and elapsed deadlines. A per-attempt observer arbitrates completion versus timeout so only one path consumes that attempt's completion ownership.

The connection helper also uses asynchronous DNS resolution, TCP connection establishment and TLS handshaking. The secure path configures peer and hostname verification and sends the server name through SNI. TLS shutdown is asynchronous with a timer-backed forced close. These are observed properties of the inherited transport, not additional fixes attributed to me. Local file handling and callback execution still occur around that asynchronous network work, so this is not a claim that every operation in the path is nonblocking.

The last point describes the surrounding inherited system, not an HTTP retry mechanism I am claiming to have originally authored. Source inspection establishes the mechanism; my dated change establishes my contribution to the shared transport.

## HTTP timeouts and the watchdog recollection

In September 2026 I recalled: **"HTTP calls that could time out a watch dog"**, adding **"in this repo watchdog is not active and I think we are using asynchrony properly."** This is worth preserving because it identifies a concrete concern from working on the product, but the recollection is not yet a dated incident or a verified fix.

The source review supports a narrower, useful account:

- The examined HTTP transfer path uses asynchronous network reads and writes, rather than a blocking request/response exchange on the application event loop.
- An asynchronous operation can still fail to make progress, retain resources or wait behind other work. Asynchrony alone does not establish correct deadlines, cancellation, teardown or freedom from event-loop starvation.
- The current startup path does **not launch the legacy watchdog or process watcher**. A separate system-monitor integration is present. "The legacy watchdog is inactive" is not equivalent to "the device has no health supervision."
- The timeout wrapper's suppression of a late result is not, by itself, proof that the underlying network operation was canceled and all resources released.

The HTTP callback correction must not be retold as "fixed HTTP calls that reset the watchdog." No evidence reviewed connects that particular fix to that particular symptom. Nor does this review establish that every networking path is nonblocking or that the deployed device cannot stall.

## Why it matters

Networking failures on a cellular device are not confined to packets and servers. A request can fail at DNS, connection establishment, TLS, HTTP policy or the local filesystem. The application has to retain enough state to report the right failure without breaking its own lifetime rules. My contribution is a concrete example of maintaining that boundary in production-oriented embedded C++.

This is recent evidence for a career direction I explicitly want to pursue: products whose central purpose is networking. Networking was supporting infrastructure in this product, but I worked below the level of merely calling a REST API. The work extends the low-level foundation from my earlier cross-platform TCP/IP predictive-job daemon into an asynchronous embedded transport.

## Skills demonstrated

C++ move semantics and callable ownership; Boost.Asio/Beast asynchronous HTTP; TCP/TLS transport abstractions; file-backed upload and download error paths; callback lifetime reasoning; separation of transport failures from application retry policy; diagnosing test prerequisites; cautious distinction between source behavior and device-runtime evidence.

## Evidence

- An owner-authored source change dated December 7, 2025 corrects the two moved-from callback invocations in the shared HTTP connection implementation.
- A second owner-authored change that day establishes the HTTP test directory prerequisites; an April 17, 2023 change records HTTP-client test instability.
- The device repository's existing threading and watchdog documentation was checked against the HTTP source and platform startup code. Exact source paths, revision identifiers and implementation-level evidence are retained offline.
- The owner's September 19, 2026 request supplies the watchdog recollection and the explicit networking-product career goal. It does not supply an incident date or a claim to have authored the whole networking stack.
- The owner's same-day follow-up specifically identifies fire-and-forget error reporting and continued communication through SMS during TCP/IP failure. Direct inspection confirms the HTTPS POST chain, message deduplication, local failure handling and timeout; the existing runbook entry establishes my operational work with these reports.

## Evidence limitations

This capture is grounded in source, authored history and test definitions, not a fresh firmware build, an executed test suite, a packet trace or a device experiment. No release date, field defect rate, latency reduction or avoided reboot count is established. The original transport and operation-policy authorship belongs to the inherited codebase unless separately evidenced.

## Related

- [Cellular radio-quality indication](2023-04-06-cellular-radio-quality-service-indication.md): deliberately separate radio integration, not TCP/IP transport.
- [Cellular MQTT traffic scheduling](2026-07-29-cellular-mqtt-traffic-scheduling.md): separate recent work on periodic traffic, required checks and optional network queries.
- [Boost proficiency](2026-09-14-boost-library-proficiency.md): executor and asynchronous-programming background; this entry adds a distinct, dated HTTP correction.
- [The TCP/IP predictive-job daemon](2004-01-01-spm-client-server-tcpip-daemon.md): the earlier hands-on networking foundation, not a second account of this accomplishment.
- [MQTT test-environment diagnosis](2024-12-31-device-test-automation-robot-framework.md): a separate example of distinguishing connectivity failures from test defects.

## Record history

- 2026-09-19: Created from the owner's networking request and direct inspection of the device repository's source, history, neighboring tests and existing technical wiki. Kept the watchdog recollection explicitly unresolved. Capture only; no synthesis, coverage or public resume promotion.
- 2026-09-19: Expanded at the owner's request with direct fire-and-forget HTTPS error reporting, transport and observability failure modes, and the distinction between best-effort diagnostics and the separate SMS communication path. The additional system context does not change the December 2025 callback-fix date.