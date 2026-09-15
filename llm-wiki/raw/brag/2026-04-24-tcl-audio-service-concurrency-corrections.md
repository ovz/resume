---
title: "Drove TCL's audio-service corrections through repeated concurrency review to a smoother QA-tested result"
date: "2026-04 to 2026-05"
thread: CONC
domains:
  - "embedded and safety-critical devices"
  - "quality and test automation"
  - "leadership, management, hiring"
context: "Best Buy Health - Lively Mobile 2, embedded Linux audio and manufacturer collaboration"
sensitivity: private-repo
resume-worthy: yes
---

# Drove TCL's audio-service corrections through repeated concurrency review to a smoother QA-tested result

## What I did

**I got TCL to correct the audio service, carrying the work through successive technical reviews rather than stopping at a defect report.** This was the later corrective-engineering effort in the same subsystem as my [earlier intermittent-audio investigation](2023-09-26-audio-service-race-condition-diagnosis.md), not another telling of that diagnosis. TCL owned the implementation; my contribution was the technical direction, concrete correction requests, review of the returned changes, and persistence needed to get the service improved. QA supplied the subsequent retest.

The dated review and manufacturer-response trail runs through April and May 2026. I translated concurrency findings into specific, standards-grounded requirements that another engineering team could implement and that we could review against the next source delivery. I distinguished progress from completion: acknowledge the fix that was right, identify the remaining unsafe access or incomplete pattern, and ask for the next focused correction.

### Make synchronization and ownership explicit

The core was a conventional producer-consumer design in C using POSIX threads and GLib queues, not timing delays or extra flags pretending to track mutex ownership. The correction requests called for checking the queue predicate while holding its mutex, waiting in a predicate loop, removing an item to transfer ownership to the worker, and processing it outside the queue lock. Producers were to perform the related queue decision, update, and notification in one critical section. That was the agreed implementation pattern, not a claim that POSIX universally forbids signalling outside a mutex.

The distinctions mattered. Peeking at a queue item borrows a pointer; it does not make the item safe to use after releasing the queue's mutex. Looking up a request under a lock and dereferencing the result after unlocking can race removal and freeing by another thread. Likewise, a shared stop-state object is not protected merely because each writer takes *some* lock: its accesses need a consistent synchronization discipline. I pushed those ownership rules into the corrections and asked for a documented mutex order so the discipline could be maintained after the immediate review.

The sent May response shows the working relationship in miniature: I thanked TCL for the progress, including the new shutdown path, then asked them to finish applying the drain-loop pattern to the remaining queue-backed workers, fix the still-inconsistent stop-state access, and document lock order. The subsequent review recorded those requested changes in the returned source. A later submission removed the obsolete shared stop state entirely, eliminating that particular race surface rather than retaining an unnecessary object behind more locks.

### Review the service lifecycle, not only its busiest loop

The corrective work also addressed C and ALSA resource lifetimes: stack-allocated control objects must not escape their allocating function; control handles need closing on the success path as well as the error path. The review trail records corrections in those areas, movement toward atomic cross-thread state, and a shutdown path that requests worker exit and joins workers before queue cleanup. Those were concrete improvements, not evidence that every startup, shutdown, or allocation-policy concern had been closed.

I required the supplied execution diagrams and the source to describe the same system. The review compared submissions across rounds, rather than accepting an explanatory diagram or a reassuring response as a substitute for what the code actually did. This made it possible to distinguish a repaired defect, an incomplete correction, a regression, and a remaining concern outside that round's scope.

### Make testing capable of answering the question

The manufacturer-facing requirements separated structural correctness from runtime qualification. Known undefined behaviour and unclear ownership were to be corrected before treating a stress-test result as useful acceptance evidence. The proposed test work combined playback, stopping, volume changes, call-state transitions, and teardown, with diagnostic mutex checking and explicit checks for request completion, crashes, reboots, and resource growth.

This was test design and acceptance discipline. The retained plans are not proof that every proposed sanitizer, instrumented build, or soak ran. The later QA outcome below is the observed result the owner reports, and is recorded separately for that reason.

## Outcome: the QA retest

The owner's report, received on 2026-09-14:

> Retesting of the resulting audio service by QA confirmed that after our fixes audio-service runs smoothly and no behaviours attributable to lingering concurrency issues were noticed. Subjective improvement of user experience was also noted.

**The work reached a QA-observed improvement, not just an audit deliverable.** After our fixes, QA found the service running smoothly, noticed no behaviours attributable to lingering concurrency issues, and also noted a subjective improvement in user experience. The experience observation is qualitative, not a measured latency or satisfaction gain; the concurrency observation is bounded by what QA exercised and observed, not a proof that no races remain.

## Why it matters

Audio prompts and call-related sound are part of how a wearer understands an emergency-response device. Getting the service to behave smoothly improves the interaction the wearer actually experiences. This work joined low-level concurrency reasoning to an external team's corrective implementation and a subsequent QA result, demonstrating influence across the manufacturer boundary as well as technical depth.

The professional contribution is neither "I wrote TCL's service" nor merely "I found some races." I made the required corrections precise enough to act on, kept reviewing until the vendor's implementation improved, and the resulting service was reported by QA to run smoothly with a subjectively better user experience.

## Skills demonstrated

Embedded C and Linux; POSIX thread synchronization; GLib queue ownership; condition-variable predicates; critical-section design; shared-state and lock-order reasoning; C/ALSA object and handle lifetimes; shutdown sequencing; source-versus-diagram review; regression review across vendor submissions; acceptance-test design; manufacturer-facing technical leadership and constructive, persistent correction requests.

## What was blocked, cut short, or wrong

- Early submissions were not considered ready for meaningful stress testing. Fixes arrived incrementally, and accepting one corrected pattern did not establish correctness of every worker or lifecycle path.
- The latest retained May review still listed unresolved structural, call-state/power, cancellation-semantics, and lifecycle concerns. Some were proposed gates, others follow-up work. It did not sign off the whole service.
- The review material itself needed correction: a later review retracted wrong line/function citations and revisited earlier positive assessments. Preserve that limitation rather than treating an audit's finding labels or pass table as infallible.
- The later QA report is positive evidence about the resulting service, but the supplied record does not connect each remaining May finding to a final corrective patch and test result. Do not silently turn the QA report into that missing closure ledger.

## Evidence

- Internal audio-service audit and technical research covering execution flows, queue and mutex ownership, thread creation, shared-state signalling, ALSA lifetimes, and audio routing; corrective requests and acceptance-test drafts from April 2026.
- Successive manufacturer source submissions and assessments dated 21 and 28 April, and 6, 9, and 15 May 2026. The April response identifies TCL as the implementation owner, correcting an earlier vendor attribution.
- A retained copy explicitly marked as the sent 6 May manufacturer comment: acknowledgement of progress, three focused continuing-correction requests, followed by the 9 May assessment of the returned changes.
- The 15 May source and review draft document further improvements, remaining findings, and corrections to prior review statements. These are internal engineering artifacts, retained offline rather than copied into this private career record.
- The owner's direct statement of 14 September 2026 supplies personal attribution for driving TCL's corrections and the subsequent QA outcome quoted above.

## Evidence limitations

The April-May range dates the documented corrective-review work; the filename anchors the dated April correction request. The exact date of the later QA retest is not recorded. September 14 is the date its outcome was reported, not an invented test or release date.

The technical trail supports the corrective process and concrete changes between submissions. Some responses are drafts; only the retained May comment is explicitly labelled sent. The source assessments are static-review evidence, not an independent runtime verification performed during this capture. Their claims are not all independently re-audited here.

The QA result comes from the owner's report, not an attached QA report or raw test log. Test duration, device count, build identity, workload coverage, final patch-by-patch disposition, and production deployment are not established. No defect-free claim, formal proof, quantified UX improvement, fleet-wide result, or sole-authorship claim follows from this entry. Nor does this establish that the specific intermittent symptom in the 2023 investigation had one proven cause that this work definitively closed.

TCL's identity and the manufacturer relationship stay at T1, consistent with the existing manufacturer-transition record. Proprietary code, internal artifact names and identifiers, detailed incident data, and test-load figures remain offline. A public rendering would need a separate sensitivity pass and would name only the contract manufacturer by role.

## Related

- [2023-09-26 audio-service race-condition diagnosis](2023-09-26-audio-service-race-condition-diagnosis.md) - the earlier evidence-led diagnosis; this entry adds the distinct vendor-correction effort and later QA outcome without retroactively claiming sole closure of that original defect.

## Record history

- 2026-09-14: created and ingested from the April-May internal audit and manufacturer-revision trail, plus the owner's direct report of the subsequent QA retest. Classified as related to, not a duplicate of, the earlier audio investigation; internal artifacts remain offline and the positive QA result is explicitly owner-reported.