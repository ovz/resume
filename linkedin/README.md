# LinkedIn copy-paste blocks

**Generated — do not edit by hand.** `script/pandoc_resume.sh linkedin` rewrites
every file in this directory from the marked sections of the resume sources in
[`markdown/`](../markdown/). Edit the Markdown, re-run the build, paste the
result.

## Why this is committed

Generated output is normally kept out of version control, and the rest of this
repository's build output is. This directory is the deliberate exception,
because the artifact being tracked is not the text — it is **the diff**.
LinkedIn has no API in this workflow: updating the profile means a human
opening a field and pasting. Committing the rendered blocks makes `git status`
after a build the exact answer to "which LinkedIn fields have drifted from my
resume?" — a changed file is a field to re-paste, and an unchanged file is one
to leave alone. Nothing else in the pipeline can answer that question.

## What to paste where

| File | LinkedIn field | Characters | Limit | Headroom | Source |
|---|---|---:|---:|---:|---|
| [`about.txt`](about.txt) | About (My Story) | 2,587 | 2,600 | 13 | [`Oleg.Zhylin.resume.achievements.md`](../markdown/Oleg.Zhylin.resume.achievements.md) |
| [`experience-best-buy-health.txt`](experience-best-buy-health.txt) | Experience — Best Buy Health (2020-present) | 1,995 | 2,000 | 5 | [`Oleg.Zhylin.resume.achievements.md`](../markdown/Oleg.Zhylin.resume.achievements.md) |
| [`experience-greatcall.txt`](experience-greatcall.txt) | Experience — GreatCall (2018-2020) | 1,969 | 2,000 | 31 | [`Oleg.Zhylin.resume.achievements.md`](../markdown/Oleg.Zhylin.resume.achievements.md) |
| [`experience-minitab.txt`](experience-minitab.txt) | Experience — Minitab | 1,872 | 2,000 | 128 | [`Oleg.Zhylin.resume.achievements.md`](../markdown/Oleg.Zhylin.resume.achievements.md) |
| [`experience-salford-systems.txt`](experience-salford-systems.txt) | Experience — Salford Systems | 1,910 | 2,000 | 90 | [`Oleg.Zhylin.resume.achievements.md`](../markdown/Oleg.Zhylin.resume.achievements.md) |
| [`experience-iit.txt`](experience-iit.txt) | Experience — Institute of Information Technology | 1,122 | 2,000 | 878 | [`Oleg.Zhylin.resume.achievements.md`](../markdown/Oleg.Zhylin.resume.achievements.md) |

A build **fails** when a block exceeds its limit, so these files are always
within budget. Character counts include line breaks, which LinkedIn counts too.

## The blocks, in full

Review the whole profile here, top to bottom, before running a single `copy`.
Each block is fenced so nothing is re-rendered — line breaks, bullets and
punctuation appear exactly as LinkedIn will receive them. The per-field `.txt`
files are still what `linkedin-sync copy` puts on the clipboard and what
`git status` reports; this section duplicates them on purpose, so the profile
reads as one document.

### About (My Story)

`about.txt` · 2,587 of 2,600 characters

````text
I build Embedded software that people’s health and safety depends on, and I own the Architecture around it. Since April 2026 I own Architecture decisions across both the Wearables and Handsets lines at Best Buy Health — every device of GreatCall lineage still carried by Lively — and I stay hands-on as an engineer on all of them. I am looking for a Sr. Principal Engineer or Sr. Staff Engineer position.

Professional Software Engineer since 1996, most of it C++, with Python and SQL for the telemetry and data side and intermediate Rust. My domains are Embedded Mobile Devices, Cellular Technologies, Positioning/Location (GNSS), Health, Machine Learning/AI, Data Engineering and Security. Under all of it sit Concurrency and Network Programming, on bare-metal MCUs and embedded Linux alike. I am passionate about shifting quality to the left and eliminating toil.

I began as a Data Security and Cryptography engineer as an undergrad, working for the University mentors who ran the company. It left me a habit I have never lost: reading every system from the standpoint of a Security Professional.

From 2000 to 2017 at Salford Systems — later a Minitab company — I was an architect and technical lead in Machine Learning/AI long before the mainstream caught up. The work was systems work: a cross-platform Client-Server engine, Concurrency and Network Protocol design, a 64-bit migration, distributed ML over peta-scale datasets, and the CI/CD to ship it all. I managed teams up to 15 people across the U.S., Ukraine and China.

Since 2018 at GreatCall (presently Best Buy Health) I have built Embedded devices for Seniors at an MVNO that runs the entire pipeline from hardware manufacturing through to Care. The software gives a gift of independence, confidence and livelihood, and it has to work when someone’s life depends on it. I became the company’s Subject Matter Expert on Positioning, built the fleet Observability practice, and applied Neural Networks to the Health and Safety of Senior Citizens. I then earned the organization’s trust to move into regulated medical devices on a hospital-at-home platform: qualified into a medical-device Quality Management System under FDA, EU and Australian regulatory process, mastered Orcanos and added PPG wearable to a sensor record already spanning accelerometry, GNSS and BLE.

Since 2023, AI changed what I take on, not just how fast: I build the Multi-Agent Orchestration and Knowledge Systems that make it a team capability rather than a personal shortcut. My dream job is a perfect combination of Innovation, Value, and Impact.
````

### Experience — Best Buy Health (2020-present)

`experience-best-buy-health.txt` · 1,995 of 2,000 characters

````text
Since April 2026 I own Architecture decisions across both the Wearables and Handsets lines, while staying hands-on. Fall detection is Lively Mobile’s killer feature, and I am driving its next innovation for active seniors.

I built the fleet Observability practice: an agentless device-health architecture, chosen when no monitoring agent fit the memory budget, the production Monitors on it, and Anomaly Detection tuned from ARIMA/SARIMA first principles. It drastically reduced Cost of Operation and caught defects before customers did. When Lively Mobile 2 moved to a new contract manufacturer mid-programme, that evidence was already in place, so whether the new build behaved was answerable with data, not argument. I was instrumental in making that transition succeed and in bringing the programme back to a regular hardware/software development lifecycle, playing it safe and serving customers at the same time.

We launched Lively Mobile 2 in 2024. I upgraded Positioning via Qualcomm Skyhook on Qualcomm Linux Enablement, then architected the Location Engine unifying GNSS, Wi-Fi and BLE beacons with arbitration and fallback.

Having earned the organization’s trust, I was given Current Health’s Hospital at Home work in regulated medical devices: I qualified into its medical-device Quality Management System — Design Control, CAPA, supplier quality — under FDA, EU and Australian regulation, mastered Orcanos and a PPG wearable in record time, traced a firmware defect that made the platform conclude a patient was unmonitored, and relished the integration it demanded, across devices, technologies, company cultures and people.

I bring Concurrency and Network Programming to bare-metal MCUs and embedded Linux. I own the platform foundations — a Capability and Configuration Framework in embedded C, safety-critical C++ guidelines, Conan packaging with ARM cross-compilation — and since 2023 build the Multi-Agent Orchestration and Knowledge Systems that make AI a team capability.
````

### Experience — GreatCall (2018-2020)

`experience-greatcall.txt` · 1,969 of 2,000 characters

````text
I joined a brilliant team building the Lively Mobile+ Emergency Response device — technology that helps many seniors live a long, independent life. Radio waves and technology stacks are deprived of a sense of urgency to save a human life, so the engineering has to supply it. Embedded constraints made the work creative rather than limiting: latest C++, robust architecture, advanced Concurrency.

I built Fully Automated Fall Detection: the infrastructure to filter MCU signals and coordinate device subsystems to place a phone call by themselves when a Customer falls, tracked even across a reboot. I also became the company’s Subject Matter Expert on Positioning (GNSS — GPS, GLONASS, Galileo — ECID, Wi-Fi, BLE beacons), diagnosing and fixing implementation issues and executing a major upgrade of the Positioning infrastructure. Accurate Location is not a feature on an Emergency Response device; it is the product.

2019 was the hard year, and the formative one. I was instrumental in getting us through the August 2019 CPSC recall of the device and the relaunch that followed. Existing tooling could not say, at fleet scale, which devices were affected or whether a fix had taken; my Data Engineering work on device and server telemetry is what turned that from argument into measurement. The analysis outlived the crisis and changed how the product was maintained. I also watched an entire company — engineering, quality, operations, supply chain, care and executives — coordinate under a hard deadline with customer safety at stake, with unusually transparent leadership — a template I have drawn on ever since.

I took charge of the architecture for automated tests that run on the device, cutting test time and raising quality by orders of magnitude, then onboarded QA engineers so the gains outlived my attention — which is what made contractor spending productive. I contributed Technical Interview challenges and brought prepared, two-way feedback upward.
````

### Experience — Minitab

`experience-minitab.txt` · 1,872 of 2,000 characters

````text
At the end of an almost two-decades-long journey with Salford Systems, I helped it become a Minitab company. I was instrumental in making the entire Intellectual Property of Salford Systems available to Minitab and getting it under proper Governance — detailed records I had kept for years are what made that pace possible.

I completed the migration of Codebase, Issue Tracking and CI/CD onto Visual Studio Team Services in less than a year, while maintaining the legacy CI/CD the platform team had no resources to move. I provided a comprehensive review of every Software Development project in progress, and implemented Top Management’s decisions to freeze some of them properly, so that all of them can be resurrected effectively.

Per a mandate from Top Management I built the process to scale up the development team, cutting onboarding from 2-3 months to less than a week. I established a stable baseline of Salford Predictive Modeler (SPM), identifying and addressing instabilities to create a solid foundation for the incremental SPM v8.3 release, and improved the coverage and quality of Automated Tests with the Quality Engineers, promoting Test-Driven Development.

I brought the Codebase in line with Source Code Style guidelines, using my knowledge of C++ to get the company’s other Tech Leads on board for significant improvements. This was a short tenure and a formative one: the bar rose in some places and not others, and learning to read which is which — rather than assume — is what I took into the next role. I learned the Nalpeiron license manager, introduced it into the product, and spearheaded making the License Management package reusable across all Minitab projects. I advocated a company-wide repository of reusable code based on NuGet, and participated in architecting the next version of the Machine Learning APIs and Cloud offerings on AWS.
````

### Experience — Salford Systems

`experience-salford-systems.txt` · 1,910 of 2,000 characters

````text
Salford Systems’ claim to fame is pioneering Decision Trees in Machine Learning. We commercialized the work of Jerome Friedman, Leo Breiman, Richard Olshen and Charles Stone, the authors of the famous CART Monograph. For me it was enormous fun and hard work to help our customers meet their Data Science and Artificial Intelligence needs long before those terms became buzzwords.

I was the primary Graphical User Interface (GUI) developer and a collaborator on the Command Line and Machine Learning engines for the flagship Salford Predictive Modeler (SPM), across releases from CART 4.0 to SPM 8.2. Serving the whole range of users — from Domain Experts far from statistics to the best Data Scientists in the world — was at the core of the business offering, and those GUIs funded further Machine Learning innovation.

The rest of the work was systems work. I designed and singlehandedly built a cross-platform Client-Server predictive analytics system with a TCP/IP daemon, which was my introduction to Concurrency, Parallelism and Network Protocol Design. I was Chief Architect and Product Owner for the Qt GUI rewrite, a Principal Architect and Product Owner for Cloud-ready SPM (OpenAPI middle layer, React/Redux front end, Python backend on a Redis distributed queue), and the architect of the Machine Learning Predictive engines API. I took SPM to 64 bits, hardened it for Unicode, ran Big Data research on Hadoop, Spark and Dask, built fully automated CI/CD, and selected Wibu Codemeter after trialling every serious licensing alternative.

I managed teams up to 15 people, coordinating U.S. developers with Outsourcing contractors in Ukraine and China. I raised the bar and the teams rose with it: the Ukrainian team over-performed, becoming instrumental contributors to features and quality rather than extra capacity, and the Qt team — surprised at first to be asked to aim higher — was glad of it.
````

### Experience — Institute of Information Technology

`experience-iit.txt` · 1,122 of 2,000 characters

````text
I was fortunate to receive my undergrad degree at the Department of Information Technology Security (ITS) of Kharkiv National University of Radio Electronics (NURE). The department was founded by prominent military Rocket Scientists, and I received solid training in Cryptography, Security Policy and Risk Assessment. These skills proved very useful in professional and personal life.

In 1996 I joined Institute of Information Technology (IIT), the Research and Development entity through which my mentors from the department ran commercial projects — I was the first undergraduate it employed. The biggest project was sub-contracting the Cryptography implementation for a Client-Bank online banking system.

The work was low-level and unforgiving. I built a big-number arithmetic library and prime generation for public-key cryptography, and implemented full-disk encryption with a Windows 9x VxD kernel driver. My Master’s thesis was on Elliptic-Curve Cryptography, well before it became the industry default.

From that time I have an important life skill: to see things from the standpoint of a Security Professional.
````

## How the conversion works

LinkedIn accepts no formatting whatsoever — no bold, no italics, no links, no
headings. The Markdown sources keep all of it, because the same text renders to
PDF, HTML, DOCX and RTF where emphasis carries meaning. Pandoc's `plain` writer
does the stripping: emphasis markers are removed, reference links collapse to
their visible text, URLs and link definitions are dropped, and Unicode
punctuation (em dashes, curly quotes) is preserved. Markdown bullets become
`•`, which LinkedIn renders as pasted. Each paragraph is left on a single
long line — LinkedIn reflows text itself, and a hard-wrapped paste renders as a
column of ragged short lines.

**Emphasis is lost, not faked.** Pasting Unicode look-alike bold (𝗹𝗶𝗸𝗲 𝘁𝗵𝗶𝘀) is
a common trick and is deliberately not used here: screen readers announce those
code points as gibberish or skip them, and LinkedIn's own search and third-party
resume parsers do not match them as words. The bolded terms in the resume are
exactly the keywords worth being found by, so they are emitted as plain text
that indexes correctly.

## Adding a block

Wrap a section of a document in `markdown/` and rebuild:

```markdown
<!-- linkedin: headline limit=220 title="Headline" -->
Text that LinkedIn will receive.
<!-- linkedin: end -->
```

`limit` is required, `title` optional. The slug names the output file and must
be unique across all sources. Removing a marker deletes its file on the next
build — this directory holds nothing that is not generated.
