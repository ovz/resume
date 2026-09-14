# Technical Themes

> **Doc type:** explanation
>
> Capabilities that recur across roles and decades — the *why this person* layer above the [accomplishments inventory](accomplishments-by-domain.md). Sources: [primary resume][primary]; [archived long-form resume][long].

## Embedded and safety-critical product engineering

Modern C++, concurrency, battery-aware design, cellular connectivity, positioning, subsystem coordination, and device-side testing recur in the healthcare and emergency-response work. The framing is that radio and software stacks have no sense of urgency of their own; the engineering supplies it. [primary]

## Power, and cost of operation, as first-class constraints

Not a footnote to the embedded work but a second specialization interlocked with the first: positioning and power are treated as one subject, because the same mechanisms — what wakes the application processor, how often the device talks to the network, how long a radio stays on — decide both. The same instinct extends past the battery to the bill: the resource a fleet spends on cellular data is engineered, measured and policed the same way. The recurring habit is that **a claim about a resource is not admissible without a measurement** — an engineering build, devices soaking, a notebook. [battery] [cost]

## Concurrency, and the failures that will not reproduce

A twenty-year thread rather than a listed skill: a cross-platform TCP/IP daemon that taught it, a positioning library losing its fix to a multithreading fault, a race on a power-managed SoC that expressed itself as a wrong sound and a reboot. The method is consistent — when the bug will not reproduce, make the *evidence* reproducible: correlate independent subsystems, look for the same operation happening twice, treat a negative experiment as information, and instrument so the occurrence you cannot schedule leaves a trace. [concurrency]

## Machine learning products

Connecting machine learning theory and predictive engines with usable GUIs, APIs, command-line tools, cloud offerings, and customer-facing data workflows. The repeated concern is serving both domain experts and specialist data scientists from one product. [primary] [long]

## Data engineering

Data preparation, ETL, troubleshooting, forensics, and analytical support are described as the unavoidable 80% and as the enabler of fast iteration — at Salford consulting projects, in the Minitab transition, and in fleet troubleshooting at Best Buy Health. [primary]

## Architecture and interfaces

Desktop, embedded, client-server, distributed, API, cloud, and legacy Fortran systems. The recurring architectural role is connecting technical choices to product and organizational needs, and designing interfaces — network protocols, DLL boundaries, packaged APIs — that let other teams work independently. [primary] [long]

## Quality and operational excellence

Testing, TDD, end-to-end and on-device automation, production validation, telemetry, monitoring, incident response, runbooks, and post-mortems appear as mechanisms for reliability and lower operating cost, not as afterthoughts. "Shifting quality to the left" is the owner's own phrase. [primary]

## Security lens

An undergraduate career in cryptography and information security left a habit of seeing systems as a security professional would — visible later in license-management ownership, identity choices for the in-house cluster, and the emphasis on controlled failure in safety-critical devices. [primary] [long]

## Leadership

Technical leadership, product ownership, hiring, distributed and outsourced teams, Agile practice, mentoring, and management. The preferred style is enabling motivated, self-organizing teams and leading from behind; the recurring result is team members growing into instrumental contributors. [primary] [long]

[primary]: ../../../markdown/Oleg.Zhylin.resume.achievements.md "Primary resume (achievements)"
[battery]: ../../raw/brag/2021-10-16-battery-power-second-specialization.md "Battery and power as a second specialization"
[cost]: ../../raw/brag/2024-01-04-cellular-cost-rogue-device-detection.md "Cellular cost and rogue-device detection"
[concurrency]: ../../raw/brag/2023-09-26-audio-service-race-condition-diagnosis.md "The audio-service race condition"
[long]: ../../raw/archive/Oleg.Zhylin.resume.md "Archived long-form resume"
