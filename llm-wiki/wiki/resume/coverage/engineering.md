# Engineering And Tooling Coverage

> **Doc type:** reference
>
> Build systems, standards, AI-assisted engineering and Boost proficiency. Audience: brag ingest and resume promotion. [Coverage map](../coverage.md) owns totals, counting rules and shard routing; each claim below has one canonical home.

### BLD — Build, packaging and engineering standards

The 2021–2022 platform-and-standards layer under the device programme: where the code lives, how it is built and versioned, and the rules it is written to. Captured 2026-09-09 from the owner's own working boards, years after the fact.

**Entries:** [2021-08-15 GitHub Enterprise migration](../../../raw/brag/2021-08-15-github-enterprise-migration-monorepo.md) · [2022-02-18 C++ safety-critical guidelines](../../../raw/brag/2022-02-18-cpp-safety-critical-embedded-guidelines.md) · [2022-04-06 Conan and cross-build](../../../raw/brag/2022-04-06-conan-package-management-embedded-cross-build.md)

**Thread coverage: 100%** (6 of 6)

| Claim | Source | Status |
|---|---|---|
| `BLD-1` Spearheaded the organization's migration from Atlassian tooling to GitHub Enterprise, personally owning the embedded monorepo case the platform group could not take | 2021-08-15 | **in** |
| `BLD-2` Took ownership of an unowned cross-team change rather than waiting for it to be scheduled, as a deliberate and repeated pattern | 2021-08-15 | **in** |
| `BLD-3` Selected the C++ standard for a safety-critical embedded codebase on what static analysis could actually enforce, comparing MISRA C++, JSF and the Core Guidelines | 2022-02-18 | **in** |
| `BLD-4` Grounded the written guidelines in the existing static-analysis baseline so the rules are checked on every build rather than remembered by reviewers | 2022-02-18 | **in** |
| `BLD-5` Designed a Conan (JFrog Artifactory) versioning and channel-promotion policy tying version fields to releases and pull requests, with CI-generated unique build identity | 2022-04-06 | **in** |
| `BLD-6` Established cross-compilation to the embedded ARM target, including sysroot packaging strategy and toolchain version pinning | 2022-04-06 | **in** |

---

### AI — AI adoption and agentic engineering

**Entries:** [2025-10-29 AI data product](../../../raw/brag/2025-10-29-ai-data-product-in-alation.md) · [2026-05-26 agentic engineering](../../../raw/brag/2026-05-26-ai-adoption-agentic-engineering-choreographer.md) · [2024-10-18 Copilot practice for an embedded C SDK](../../../raw/brag/2024-10-18-copilot-embedded-c-sdk-practice.md)

**Thread coverage: 25%** (3.5 of 14). `AI-1` and `AI-2` reached the resume on 2026-09-16 inside the data-stewardship paragraph; `AI-2` is `partial` because chat-with-your-data is not named. The 2024 embedded-C practice claims (`AI-8` to `AI-14`) arrived absent on 2026-09-19 and put a verifiable 2024 date under the resume's "leveraging AI since 2023".

| Claim | Source | Status |
|---|---|---|
| `AI-1` Scoped an AI-enabled data product on the enterprise data catalog to test whether warehoused device-event tables earn their storage and cellular cost | 2025-10-29 | **in** |
| `AI-2` Combined lineage, query-log usage, glossary metadata and chat-with-your-data exploration into one cost-aware proposal | 2025-10-29 | partial |
| `AI-3` Designed and shipped a multi-agent orchestration layer as an agent plugin, preventing context overflow through delegation | 2026-05-26 | **in** |
| `AI-4` Established a persistent, versioned knowledge base (raw capture → synthesis → index) for the engineering organization | 2026-05-26 | **in** |
| `AI-5` Developed and documented prompt and agent patterns that cut token consumption while holding output quality | 2026-05-26 | absent |
| `AI-6` Integrated agents into code review, documentation and release-note workflows | 2026-05-26 | absent |
| `AI-7` Delivered outcomes at roughly three times the expected rate using AI since 2023 | 2026-05-26 | absent |
| `AI-8` Wrote the team's AI-assisted engineering practice into an embedded C SDK repository in 2024, so it reached everyone who cloned it | 2024-10-18 | absent |
| `AI-9` Kept prompt comments in the source as living documentation, regenerating code when prompt and implementation diverged | 2024-10-18 | absent |
| `AI-10` Established the failing unit test as the most effective prompt, frequently yielding a zero-shot correct implementation | 2024-10-18 | absent |
| `AI-11` Documented a recency-bias failure mode in code suggestions and the context-priming workaround for it | 2024-10-18 | absent |
| `AI-12` Committed editor settings pointing the assistant's code-generation instructions at the repository's own C style guide, years before committed instruction files were standard | 2024-10-18 | absent |
| `AI-13` Required a hallucination check on LLM-generated pull-request summaries and code review | 2024-10-18 | absent |
| `AI-14` Drew a repository physical-design conclusion from workspace-indexing limits, preferring smaller repositories consuming each other through headers | 2024-10-18 | absent |

> `AI-7` was `in` until 2026-09-09 and was **deliberately retired** from the resume, not lost: an unverifiable productivity multiplier was replaced by what was actually built (`AI-3`, `AI-4`). The claim stays on this page because the underlying fact is still true and the owner may want it back — see [editorial questions](editorial.md#open-questions).

---

### SALF — Salford Systems technical and organizational record (2009-2017)

A breadth-first Gmail survey pass (2026-09-16) surfaced eight distinct Salford Systems threads with enough evidence for a dedicated candidate entry each, spanning release engineering, tooling modernization, storage architecture, cross-platform/concurrency work, client delivery, big-data R&D, M&A technical diligence and vendor staffing. Two (engine debugging and the Linux/TBB port) are tracked under `CONC` for their concurrency content; two (Carrefour delivery and CloudSML/BigISLE R&D) are tracked under `DATA`. This thread carries the remainder — release engineering, tooling modernization, storage architecture, M&A diligence and vendor staffing. **None of these entries has been deep-dived**; each is explicit that more detail could be mined from Gmail via the Gmail connector available to Claude, deferred to a later session.

**Entries:** [2009-06-01 SPM release engineering and Japanese localization](../../../raw/brag/2009-06-01-spm-release-engineering-japanese-localization.md) · [2012-01-01 Git/GitHub/RedMine modernization](../../../raw/brag/2012-01-01-salford-git-github-redmine-modernization.md) · [2012-09-01 SPM workspace storage architecture](../../../raw/brag/2012-09-01-spm-workspace-storage-architecture-sqlite-json.md) · [2016-11-01 Minitab acquisition technical diligence](../../../raw/brag/2016-11-01-salford-minitab-acquisition-technical-diligence.md) · [2015-01-01 Mirabit outsourcing vendor staffing](../../../raw/brag/2015-01-01-mirabit-outsourcing-vendor-staffing-management.md) · [2009-02-01 SPM_protected / Wibu-Systems CodeMeter](../../../raw/brag/2009-02-01-spm-protected-wibu-codemeter-license-integration.md)

**Thread coverage: 0%** (0 of 6)

| Claim | Source | Status |
|---|---|---|
| `SALF-1` Directed release engineering across three parallel build tracks (English, Japanese, license-protected) for a commercial statistical modeling product, triaging cross-cutting bug reports as central reviewer, and ran a full literal-string-to-resource-table Japanese localization | 2009-06-01 | absent |
| `SALF-2` Led the technical case for moving a team off Visual SourceSafe onto Git/GitHub and RedMine, including hands-on git-workflow mentorship of a colleague senior in tenure | 2012-01-01 | absent |
| `SALF-3` Owned the architectural decision between SQLite and a JSON-document approach for a new persistent workspace feature's storage layer, articulating the trade-off against ACID requirements | 2012-09-01 | absent |
| `SALF-4` Directly asked by the company president to prepare and help deliver the technical due-diligence presentation to an acquirer's representatives ahead of the company's acquisition | 2016-11-01 | absent |
| `SALF-5` Made and defended staffing recommendations for an outsourced development team across three concurrent products, escalating the case to leadership | 2015-01-01 | absent |
| `SALF-6` Owned a commercial license-protection build track from at least 2009 and corresponded directly with the licensing vendor on integration | 2009-02-01 | absent |

> All six entries are candidates from a single-pass Gmail survey, not full-thread deep-dives — dates, named colleagues and quotes are preserved, but outcomes and full technical detail are largely unconfirmed. See *Evidence limitations* in each entry before promoting any claim.

---

### BOOST - Boost library proficiency

One cross-career capability record, with specific embedded C++ examples. The entry's corrected device-wiki grounding establishes **Boost 1.67.0 across ARM Linux, native Linux and macOS**, corroborated by the three vendored headers. The older Asio 1.67 study checklist is historical context. Investigations and advocacy are not claims of delivered redesigns. A 2026-09-19 pass added Signals2, Filesystem, System and String Algorithms as a wider base of production-infrastructure evidence from the same device wiki; a repeat targeted search again found no evidence of Boost.MPL.

**Entry:** [2026-09-14 Boost proficiency](../../../raw/brag/2026-09-14-boost-library-proficiency.md)

**Thread coverage: 10%** (1 of 10). All ten claims belong to the entry marked `resume-worthy: yes`. `BOOST-4` and `BOOST-5` became `partial` on 2026-09-16: the resume now names Boost.Asio as the day-to-day abstraction and its executor and signal-handling boundaries, without the off-target testing or `signal_set` detail.

| Claim | Source | Status |
|---|---|---|
| `BOOST-1` Works with an inherited Boost.MSM architecture composed of submachines and orthogonal regions | 2026-09-14 | absent |
| `BOOST-2` Diagnosed unexpected MSM transitions using typed action traces and shared-state initialization hypotheses | 2026-09-14 | absent |
| `BOOST-3` Stewards the inherited state-machine architecture and argues for explicit lifecycle integration of cross-cutting modes | 2026-09-14 | absent |
| `BOOST-4` Analyzed Boost.Asio executor boundaries and mockable message-bus reuse for off-target testing | 2026-09-14 | partial |
| `BOOST-5` Identified signal-handling guarantee trade-offs around Boost.Asio signal_set and SIGTERM | 2026-09-14 | partial |
| `BOOST-6` Records long-standing Boost/C++ and Boost.Test experience, with historical 15-year and 2-year baselines rather than invented current totals | 2026-09-14 | absent |
| `BOOST-7` Built the device's cross-component event bus on Boost.Signals2's connect-order slot guarantee, composed with per-subscriber posted delivery | 2026-09-14 | absent |
| `BOOST-8` Resolved production file paths through Boost.Filesystem and closed a gap where `filesystem_error` escaped uncaught from an unsearchable-parent or symlink-loop path | 2026-09-14 | absent |
| `BOOST-9` Used Boost.System `error_category` as the repo-wide convention identifying which subsystem raised an error, mapped to a bit-packed reporting code | 2026-09-14 | absent |
| `BOOST-10` Used Boost String Algorithms (`replace_all`) for in-place placeholder substitution on a live component ahead of a controlled rebuild | 2026-09-14 | absent |
