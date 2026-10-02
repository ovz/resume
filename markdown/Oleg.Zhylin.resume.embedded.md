<!-- include: _parts/header.md -->

> Professional **Software Engineer** since **1996**, most of it **C++** on **Embedded** and systems software. I build for **Embedded Linux** and **bare-metal/MCU** targets in **Cellular**, **Positioning/Location**, and safety-critical **Health** domains. Intermediate **Rust**; **Python** and **SQL** for the telemetry and data side. I am looking for a **Principal Engineer** position.
>
> I own **Architecture** for a two-line device portfolio today, and I carry the domains a Principal is expected to hold beyond the code: **Systems Design**, **Operational Excellence** and **Observability**, **Quality Engineering**, and **Technical Leadership** of distributed teams up to **15 people**.

----

## My Story

I started as a **Data Security** and **Cryptography** engineer as an undergrad, working for mentors from my University department. It left me with a habit I have never lost: looking at every system from the standpoint of a **Security Professional**.

From **2000 to 2017** at [Salford Systems][salford] — later a [Minitab][minitab] company — I was an architect and technical lead in **Machine Learning/AI**, long before the mainstream caught up. The work was systems work: a cross-platform **Client-Server** engine, **Concurrency** and **Network Protocol** design, a 64-bit migration of a memory-bound codebase, cross-platform packaging and licensing, and the **CI/CD** to ship it all. I managed teams up to **15 people** across the U.S., Ukraine, Poland and China.

Since **2018** at [GreatCall][greatcall] (presently [Best Buy Health][bbh]) I have built **Embedded** mobile devices with cellular connectivity for Seniors — an MVNO running the whole pipeline from hardware manufacturing through to Care. The software I build gives a gift of independence, confidence and livelihood, and it has to work when someone's life depends on it. I applied **Cellular Technologies**, **Positioning/Location (GPS)** and **Distributed System Design** to exceed expectations, met an OKR and over-delivered on **Operational Excellence**, and since **April 2026** I own **Architecture** decisions across both **Wearables** and **Handsets**.

Since **2023**, **AI** changed *what I take on*, not just how fast: I build the **Multi-Agent Orchestration** and **Knowledge Systems** that make it a team capability rather than a personal shortcut. **Stewardship** is my first principle, and I practise it by **shifting quality to the left** and **eliminating toil**. My dream job combines **Innovation**, **Value**, and **Impact**.

## Most prominent achievements

* ***Architecture Ownership** across the device portfolio*. Since **April 2026** I own **Architecture** decisions for both the **Wearables** ([Lively Mobile+][r4], [Lively Mobile 2][r5]) and **Handsets** (*Jitterbug* flip and smart phones) lines — every device of [GreatCall][greatcall] lineage still carried by [Lively][lively_products] — and I stay hands-on across all of them. That breadth means unfamiliar platforms often, so I use **AI-assisted** *Rapid Prototyping* to get productive on a new stack fast and to judge an idea's **Innovation Potential** before it costs a team a quarter.
* *Original **Embedded Software** for an Emergency Response mobile device*. Radio waves and technology stacks are deprived of a sense of urgency to save a human life. I used *modern C++* and scalable architectures to deliver multiple *successful Product Launches*, and went well beyond my designated areas to ensure *Performance*, *Testability*, outstanding *Battery Life* and *Operational Excellence*. I exercised **Concurrency** and **Network Technologies** throughout.
<!-- include: _parts/bullet-retail-shelf.md -->
* **Positioning Technologies** (GNSS — GPS, GLONASS, Galileo — ECID, Wi-Fi, Bluetooth/BLE Beacons). Accurate **Location** fixes are critical for an Emergency Response device. I became **Subject Matter Expert on Positioning** for the Company, diagnosed and fixed implementation issues, and designed and executed a *major upgrade* of the Positioning infrastructure. I went on to architect the **Location Engine** that unifies beacon, GPS and Wi-Fi behind per-provider interfaces, with a state-management layer that arbitrates between sources and falls back when one fails, and I have owned **BLE beacon** home-or-away tracking since its inception — kept deliberately simple across a contract-manufacturer firmware boundary, and carried across **firmware-over-the-air** updates.
* **Fully Automated Fall Detection**. It was imperative for the [Lively Mobile+][r4] PERS product to call for help automatically when a Customer falls. I built the infrastructure to filter **MCU** signals and coordinate device subsystems to place a phone call. Falls are tracked even if the device reboots. Fall detection is Lively Mobile's **killer feature**: the **Care** center is load-bearing, but fall detection is the focused driver. The **sensor-cluster architecture** I designed for the next-generation wearable classifies motion in the sensor's own **machine-learning core**, so the application processor stays asleep — and as architecture owner I am now driving the next round of **fall-detection innovation** for active seniors.
* ***Regulated Medical Devices** and safety-critical process*. I earned the organization's trust to be given the [Current Health][current_health] *Hospital at Home* work, moving from consumer safety-adjacent devices into **regulated medical devices** on a remote patient monitoring platform, and qualified into its medical-device **Quality Management System**: **Design Control** and change control, **CAPA** and non-conformance, **Supplier Quality**, and product release, under **FDA**, **EU** and **Australian** regulatory process including mandatory device reporting and vigilance, all under a full **ISO**-style **Information Security** policy set. In record time I **mastered [Orcanos][orcanos]**, the eQMS/ALM that regulated development actually runs through — the difference between being qualified on paper and being able to move a change through the process. I mastered a **PPG** (photoplethysmography) device just as quickly and added it to a sensor record already spanning accelerometry, gyroscopes, **GNSS** and **BLE** — and relished the integration the work demanded, across technologies, company cultures and people.
* ***Integration** across devices, protocols and organizations*. Integration is the work I keep being drawn to, and the kind I have done varies: two device lines meeting in one care experience, a device programme meeting a contract manufacturer, a regulated medical-device culture meeting a consumer one. On the *Hospital at Home* platform I pushed to bring **[Lively Mobile 2][r5]**'s **fall detection**, a **PPG** wearable and the surrounding sensors into a single experience — where overlapping radios and overlapping vitals are not waste but a second independent path to the same fact, which is exactly what a home without a nurse in the next room needs. I also know where the instinct stops. Building a device **ground-up** keeps the fix in-house, at hardware's six-month-plus pace; integrating **breadth-first** through a thin **white-label** interface keeps the vendor replaceable — a vendor who misses the date loses the order to the next one, which care providers accept far more readily than missed deadlines and device swaps. The trap is the **hybrid**: too specialized to switch vendors, not owned closely enough to fix in-house, so every gap in engineer-to-engineer collaboration becomes a **contract negotiation** running at hardware pace, and the instability lands on the care provider and the vendor alike. I have run the ground-up side and studied the other at close range.
* ***Embedded Platform Frameworks***. I led the design and delivery of an embedded **component framework** standardizing how every device SKU declares, configures and brings up its features — **dependency injection**, **hierarchical state machines** with predictable lifecycle management, and an aligned **structured logging** framework giving consistent logs across every supported device, all in embedded **C**. I modularized and documented it for **open-source** release and external contribution.
<!-- include: _parts/bullet-operational-excellence.md -->
* ***Stewardship**, practised by eliminating toil*. Ownership is my first principle, in several registers: a **[NIST][nist]**-grounded patch-management SOP and **risk appetite** as the basis of **Risk Management**; an official **Data Steward** on the enterprise data catalog for device data; inherited device architectures kept sound after their authors moved on; and a company's **Intellectual Property** transferred under proper **Governance**. Stewardship is the *why* and **eliminating toil** is the *how* — hand work is where drift and single points of knowledge live, so I automate it away.
* ***Quality Engineering** on real hardware*. I architected and implemented **automated tests that run on the device**, cutting testing time and raising quality by orders of magnitude, then onboarded the QA team to the framework so the gains stuck. Combined with unit suites, **End-to-end** automation and production validation, this is how a safety-critical device earns confidence.
* *Software Architecture across **Embedded devices**, **Desktop Applications**, **Command Line**, **Client-Server**, **Distributed Systems**, and **Cloud***. As an architect I provided a **strong vision** and worked with *engineering*, *business* and *scientific* teams to reach the best decisions.
* **Legacy code and platform migrations**. I debugged the classic **Machine Learning** engines at their **Fortran** and **C/C++** numerical core, working the mathematics through with the statisticians who owned it; modernized that legacy codebase; moved a memory-bound product to **64-bit**; and hardened a large C++ codebase for **Unicode** — keeping **Technical Debt** to a pragmatic minimum throughout.
* ***Raising the bar**, and reading the room it is raised in*. I strive to improve and exceed expectations wherever I land, and the interesting half is that environments differ: one team over-performs when the standard goes up, another is surprised and then glad to aim higher, a third is careful by temperament. Reading which is which — and adapting instead of insisting — is what makes a raised bar compound rather than grate.
* ***Management** and **Technical Leadership** of **Distributed** teams*. Coordinating **U.S.** developers with **Outsourcing** contractors in **Ukraine**, **Poland** and **China** is far from trivial; I managed teams up to **15 people**. I *mastered* the power of **Motivated and Self-organizing teams**, achieving my best results by **empowering others** and **leading from behind**.
* ***Hardware and software cadences**, and **engineer-to-engineer** relationships across them*. A device with new hardware and industrial design runs on a rigid cycle of six months or more: its agility lives in the pre-planning, while the software iterates inside it. I mastered both rhythms and the seam between them. My best results came from engineer-to-engineer relationships with manufacturer, silicon and firmware partners — and the classic **Agile Manifesto** already holds everything needed to practise them, which is what makes them a skill that transfers.
* **Data Engineering** for telemetry and diagnostics. **[Data Wrangling][data_wrangling]** easily gobbles up 80% of the time between raw data and a valuable insight. The **ETL** and analysis functionality I built turned fleet and server telemetry into decisions in days or hours, and made contractor QA effort genuinely effective.

<!-- include: _parts/side-note-links.md -->

## Employment History

### 2020-Present. [Best Buy Health][bbh]. Health Engineer Senior.

<!-- include: _parts/experience-best-buy-health.md -->

### 2018-2020. [GreatCall][greatcall]. Health Engineer Senior.

<!-- include: _parts/experience-greatcall.md -->

### 2017-2018. [Minitab Inc.][minitab]. Sr Advisory Software Engineer.

I helped [Salford Systems][salford] become a [Minitab][minitab] company, and was instrumental in transferring its entire **Intellectual Property** under proper **Governance**. I completed the migration to [Visual Studio Team Services][vsts] — codebase, issue tracking and [CI/CD][cicd] — in **less than a year**, cut onboarding from **2-3 months to under a week**, established a stable baseline of the flagship product, and improved automated test coverage while promoting **TDD**.

### 2000-2017. [Salford Systems][salford]. Sr Software Engineer, Architect.

Salford Systems pioneered **Decision Trees** in **Machine Learning**, commercializing the work of the authors of the famous [CART Monograph][cart_monograph]. I was primary **GUI** developer and a collaborator on the **Command Line** and **Machine Learning** engines for the flagship [Salford Predictive Modeler (SPM)][spm82], and architect on the systems work below.

### 1996-2000. [Institute of Information Technology (IIT)][iit]. Software Developer. Data Security Researcher.

I received my undergraduate degree at the [Department of Information Technology Security (ITS)][kafedra_bit] of [Kharkiv National University of Radio Electronics (NURE)][nure_eng], founded by prominent military Rocket Scientists — solid training in **Cryptography**, **Security Policy** and **Risk Assessment**. At [IIT][iit] my largest project was sub-contracting the *Cryptography implementation* for a **Client-Bank** system.

## Selected Projects

*Please feel free to ask me for stories from any of the projects below, or from the Machine Learning product work not listed here.*

### 2004-2005. Client-Server predictive analytics application.

The largest system I have developed *singlehandedly* from the ground up. I designed it entirely and implemented a fully cross-platform **TCP/IP daemon** running multiple jobs on behalf of end users, and provided guidance and a component framework for two developers on the client side. This was my major introduction to **Concurrency**, **Parallelism**, **Network Programming** and **Network Protocol Design**; I built a C++ library implementing a large share of the [Gang of Four (GoF)][gof_book] patterns, which brought my idiomatic C++ to another level.

### 2012. 64-bit migration of a memory-intensive product.

[SPM][spm82] is very memory intensive, and the 4 GB address space of 32-bit systems was a hard limit. I transformed the codebase to compile and run correctly on 64-bit, methodically revisiting every place where addresses and sizes are handled — completed in a month.

### 2011-2017. **Unicode** hardening and **Internationalization (i18n)**.

Warnings, regex sweeps, Unicode test inputs, and both static ([CppCheck][cppcheck]) and dynamic ([BoundsChecker][boundschecker]) analysis, delivered with native partners for Asian markets.

### 2015-2017. [Wibu Codemeter][codemeter] deployment.

I owned **License Managers** — in-house, then [CrypKey][crypkey] — and needed a cross-platform, enterprise-ready replacement protecting all products including engine DLLs. After trials of [FlexLM][flexlm], [Reprise][rlm], [Arxan][arxan] and [Sentinel RMS][safenet], [Wibu Codemeter][codemeter] proved optimal, and I put production solutions together quickly.

### 2016-2017. [SPM 8.2][spm82] production and **CI/CD**.

Main engineer behind preparing and running SPM 8.2 in production. I built a fully automated [CI/CD][cicd] pipeline ([CruiseControl.NET][ccnet] plus PowerShell) that saved the day repeatedly on urgent hotfixes and custom builds, and authored the product installers. Managed a team up to **12 people**.

<!-- include: _parts/education.md -->

<!-- include: _parts/links.md -->
