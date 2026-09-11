---
title: "Argued a launch-readiness control was the wrong instrument for devices, and proposed what would actually work"
date: "2023-11 to 2023-12-05"
thread: RSK
domains:
  - "operational excellence and observability"
  - "risk management and compliance"
context: "Best Buy Health, R5 wearable, launch readiness and operational excellence"
sensitivity: private-repo
resume-worthy: maybe
---

# Argued a launch-readiness control was the wrong instrument for devices, and proposed what would actually work

## What I did

Ahead of the device's launch decision point, the organization's readiness checklist called for a tabletop exercise — a facilitated walkthrough in which a team rehearses its response to a simulated incident. I concluded it was the wrong control for this system and said so, with a reasoned alternative rather than a refusal.

**Made the argument from the control's own stated objective.** A tabletop exercise is meant to test *when various alerts are detected and what actions need to be taken as a result*. Per our own runbook, we had no alerts at that point — so the exercise would have to invent a substitute objective, and I judged it unlikely any substitute would carry comparable value. That is a specific, checkable argument, not a general objection to process.

**Established the real coupling instead of assuming it.** I worked out and stated that there were no ripple effects from device to backend or backend to device — which is precisely what determines whether a joint incident rehearsal is meaningful. Infrastructure could simulate any problem with any device directly, making the rehearsal redundant for the failure modes that mattered.

**Showed the coverage already existed.** Our QA already tested the device against carrier outage, message-broker outage and battery exhaustion, and the team routinely supported all server-side testing that affected devices. The gap the exercise was meant to close was largely already closed by ordinary practice.

**Offered concrete alternatives rather than stopping at "no".** I proposed that the team gladly support all server-side testing affecting devices, including chaos-engineering-style exercises run in infrastructure where they would actually exercise something; that our team sit on the escalation path; and — as the one genuinely device-shaped scenario I could construct — simulating an emergency shutdown due to overheating and walking the playbook for how we would determine that unlikely event had occurred.

**Checked the precedent** rather than relying on my own reading, confirming with a peer that the handsets organization had not run a tabletop exercise either.

**Read the readiness criteria closely and worked out what was actually wanted.** Going through the decision-point definition, I identified that launch readiness was really asking for *documentation*: design and development complete and technology solutions documented, a documented data and reporting plan with reports ready to run post-launch, and technology products operationalized and ready to launch, run, monitor and maintain. Naming the real requirement is what let the team satisfy it rather than perform a ritual.

**Confirmed the operational baseline explicitly**, establishing during standup that the team was reusing the prior generation's operations and monitoring for this launch — a decision worth having on the record before a launch rather than discovering afterwards.

**Read the guidance critically.** Working through the exercise guide, I flagged where its language was doing no work — including a "parking lot" presented as an inevitability rather than the contingency slot it is meant to be — which is the same scrutiny I would apply to a design document.

## Why it matters

- **Challenging a compliance control on technical grounds, with evidence, is harder and more valuable than complying with it.** The argument rests on system coupling and existing test coverage, not on the effort involved.
- **It substitutes a better control rather than removing one** — chaos-style testing where the failures actually live, escalation-path membership, and the one device-specific scenario worth rehearsing.
- **Identifying that "launch readiness" actually meant documentation** redirected the team's effort from ceremony to the artifact the decision-point reviewers needed.
- It is operational-excellence ownership at the point where it is least rewarding: arguing about a checklist item before a launch.

## Skills demonstrated

Operational excellence; incident-response and readiness practice; risk-based reasoning about controls; system-coupling analysis; constructive challenge to process; stakeholder communication; critical reading of governance documents; site-reliability practice.

## Evidence

Trello device-programme board, *Operational Excellence* list, 2023-11 to 2023-12-05, including the drafted message to the responsible leader, the readiness-criteria analysis, and notes taken against the exercise guide. Internal wiki links and decision-point page references remain in the board archive.

## Related

- [2023-12-21 Device-health observability architecture](2023-12-21-device-health-observability-architecture.md) — the monitoring work that followed, which supplied the alerts this exercise found missing.
- [2023-08-03 Risk-management practice and early analysis](2023-08-03-risk-management-practice-early-analysis.md) — the same risk-first reasoning applied earlier.
- [2024-03-07 R5 Datadog monitoring launch](2024-03-07-r5-datadog-monitoring-launch.md) — where the operational monitoring gap was ultimately closed.

## Record history

- 2026-09-10: created from the Trello device-programme board during the full board ingest.
