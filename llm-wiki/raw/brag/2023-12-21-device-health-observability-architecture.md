# Co-designed device-health observability architecture for an agentless embedded fleet

- date: 2023-12-21 to 2024-02-05
- context: Best Buy Health, fleet-wide health observability strategy for a cellular-connected embedded medical-alert device
- domains: architecture and API design, embedded and safety-critical devices, operational excellence and observability
- sensitivity: private-repo
- resume-worthy: maybe

## What I did

Co-designed, with a peer on the device-communications engineering team, the strategy for fleet-wide health observability on an embedded, cellular-connected medical-alert device for which a conventional monitoring agent was not viable. Personally drove the feasibility check with the observability vendor's support organization and confirmed there was no supported path to run a standard agent on the device's embedded-Linux/Yocto firmware image — no package-manager-based deployment model existed, and the agent's published minimum memory footprint approached the device's entire RAM budget — closing off an appealing but infeasible option before the team invested further in it. Co-authored the resulting design: a single, wide-contract "monitoring event" published periodically over the device's existing telemetry channel and forwarded server-side into the observability platform, deliberately avoiding a narrowly-typed event contract so the schema could evolve without a firmware release. Proposed the metric set (CPU, memory, storage, file descriptors, thermal, uptime, and similar health indicators) and reviewed candidate downstream consumers (a self-service portal's "device missing" detection, mass rogue-device response).

## Why it matters

Established the architectural direction used to get full-fleet health observability without an on-device agent, on a device class where hardware resources and firmware release cadence are hard constraints; the negative feasibility result on the agent path saved the team from a dead-end investment.

## Skills demonstrated

Embedded-systems constraint analysis, cross-team architecture collaboration, vendor feasibility evaluation, telemetry contract design for firmware-release-constrained systems.

## Evidence

Cross-team chat log and internal design-page draft (December 2023–February 2024); vendor support correspondence confirming no supported embedded-agent path.

## Record history

- 2026-09-07: created
