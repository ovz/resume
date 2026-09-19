# Resume Coverage Map

> **Doc type:** reference
>
> How much of the captured brag material is actually reflected in the primary resume, tracked one claim at a time and grouped into threads. This is the page to read and think with **before** a resume pass — it says what is missing, not what to write. Audience: the owner deciding what to promote; agents drafting resume text or ingesting a brag entry.
>
> Live document: every ingest adds claims, every promotion flips a status. Statuses are judgement calls, not measurements — see *How the number is built*.

## Where it stands

| Measure | Coverage |
|---|---|
| All promotable claims | **≈ 55%** — 121.5 of 222 claims |
| Claims from entries marked `resume-worthy: yes` | **≈ 57%** — 93 of 163 claims |

115 claims are fully reflected. 13 are gestured at generically. 74 are absent. **Two are `held`** — recorded deliberately and never for the resume — and **one is struck** as wrong; all three are excluded from the totals above. A 2026-09-19 pass added four new absent Boost-infrastructure claims (`BOOST-7` through `BOOST-10`: Signals2, Filesystem, System, String Algorithms) to the existing Boost entry, raising the denominator without moving anything already on the resume. Tables recounted 2026-09-16 (twice): first for nine newly captured concurrency claims from the 2004-2005 client-server daemon and the concurrency-specialization entry, then for eleven new claims (`SALF-1` through `SALF-6`, `CONC-21`, `CONC-22`, `DATA-3` through `DATA-5`) from a breadth-first Gmail survey of Salford Systems-era material — all absent, none deep-dived yet. No resume content was removed either time. Then a promotion pass the same day put concurrency and network programming on the resume: sixteen claims moved (`CONC`, `POS-1`, `PWR-2`, `BOOST-4`, `BOOST-5`) and two were added already `in` (`CONC-23`, `CONC-24`), lifting coverage from 53% to 60%. A third pass the same day added a stewardship thread (`STEW-1` to `STEW-4`) and six `DATA` claims from the Data Steward and NCS-R entries, and promoted stewardship, the Data Steward role and engine-level debugging of the classic ML engines: six claims `in` on arrival (`STEW-1` to `STEW-3`, `DATA-6` to `DATA-8`) and `AI-1` flipped to `in`, with `AI-2` and `CONC-21` to `partial` — 60% to 61%. The worthy-entry figure remains **provisional**: four Home/Away claims use the ledger's classification because their 2023-11-27 source entry is missing. Available worthy entries account for 84.5 of 125; that missing source accounts for the remaining 2.5 of 4. The five `ARC` claims come from the owner's direct statement rather than an entry, so they count in the first row and not the second.

> **How the number got here, and what each past pass promoted, is now [coverage history](coverage-history.md)** — including the two earlier occasions when coverage *fell* while nothing was removed from the resume, which is the metric behaving correctly rather than a regression.

**What this number does not mean.** It is not a grade on the resume. The resume carries 25+ years of work, much of it from before the brag file existed and therefore invisible to this page. What the number measures is narrower: **how much of the captured material has reached the resume**, including retrospective entries such as the Boost proficiency record.

## How the number is built

Each brag entry decomposes into discrete **claims**: one promotable assertion each, small enough to be either in the resume or not. Every claim gets a status:

| Status | Meaning | Weight |
|---|---|---|
| `in` | The resume makes this claim, specifically enough that a reader would take it away. | 1.0 |
| `partial` | The resume gestures at it generically — the theme is present, this specific claim is not. | 0.5 |
| `absent` | Not in the resume in any form. | 0 |

Coverage is the weighted sum over claim count. `partial` at 0.5 is deliberately crude: the point is a direction of travel, not a metric to optimize. When a promotion lands, flip the status in its owning shard and mark the entry's ledger row — see *Maintenance*. `held` and struck claims remain in their thread for provenance but contribute neither weight nor denominator.

## Shards

Load this map first, then only the shard whose subject matches the entry or promotion. Each thread has one home; cross-list sources, never duplicate claims. The table grows with **shards**, not accomplishments. Thread tables remain authoritative for claim wording and status.

| Shard | Threads | Load when | Weighted / claims | Absent |
|---|---|---|---|---|
| [Device Architecture And Delivery](coverage/devices.md) | ARC, FALL, INT, FW, DEV, MED, MFG | Portfolio ownership, device features, platforms, medical devices and manufacturer delivery | 47 / 48 | 0 |
| [Positioning And Power](coverage/positioning-power.md) | POS, PWR | Location, beacon tracking, battery and power trade-offs | 8.5 / 19 | 10 |
| [Reliability And Operations](coverage/reliability.md) | OBS, CRISIS, CONC, COST | Observability, recall response, concurrency and cellular operating cost | 38.5 / 76 | 34 |
| [Engineering And Tooling](coverage/engineering.md) | BLD, AI, BOOST, SALF | Build systems, standards, AI-assisted engineering, Boost proficiency and the Salford Systems technical/organizational record | 10.5 / 29 | 17 |
| [Leadership And Risk](coverage/leadership.md) | LEAD, QA, RSK, STEW | Managing upward, mentorship, test discipline, risk practice and stewardship | 14 / 34 | 20 |
| [Data And Statistics](coverage/data.md) | DATA, STAT | Data engineering, governance and stewardship, statistical reasoning and specialist partnerships | 3 / 16 | 13 |

Interpretation and unresolved editorial choices live in [editorial guidance](coverage/editorial.md), separate from the reference tables.

## Physical design

Prefer pages of **500 lines or fewer**; **1,024 lines is the hard ceiling**. Split a growing claim shard by coherent subject before it exceeds the preferred size. Do not pad short shards, compress paragraphs, or move arbitrary tail sections just to meet a limit. Keep each thread's claims, sources and evidence caveats together. If a thread itself needs multiple pages, give it a small router and uniquely owned subthreads.

This summary has one row per shard and no claim tables. It should only approach 500 lines because the career genuinely needs that many navigation entries, never because claim detail has crept back in. If the shard directory itself grows beyond easy scanning, introduce subject-group routers before reaching 1,024 lines. The target is selective reading, not permission to grow every page to the ceiling.

## Maintenance

- **On ingest:** use the routing table to open only the owning shard. Add the entry's claims to its thread, or open a thread there if needed. New claims default to `absent`. Assign the entry to exactly one primary thread; cross-list it under others without duplicating its claims. Update the shard's thread list in this router when it changes.
- **Statuses:** `in` (fully reflected), `partial` (gestured at generically), `absent` (not there yet), `held` (deliberately never for the resume — the owner's call, not an agent's). `held` claims stay in the tables so the record is complete, and are excluded from every total.
- **On promotion:** when resume text lands, flip the affected claims to `in` or `partial` in the same edit, and set the entry's ledger promotion status. Recompute the thread and headline numbers.
- **Recompute:** run `python3 script/check-coverage.py` from the repository root. The [read-only validator](../../../script/check-coverage.py) follows this router's shard table, checks unique thread/claim ownership, catches unrouted claim files, and reconciles thread, shard and headline counts. It warns above 500 lines and fails above 1,024. Worthy-entry totals use ledger classifications and explicitly report unavailable sources; a structural pass is not a clean source-evidence gate. Keep the derived shard rows and headline figures in sync with the canonical claim tables.
- Claim IDs are stable and never reused. A claim that turns out to be wrong is struck, not deleted, so anything citing it still resolves. A claim retired from the resume returns to `absent` rather than being removed.

## Related

- [Update the outward-facing resume](update-workflow.md) — the pass this page feeds.
- [Primary resume — structure and cut points](primary-resume.md) — where a promoted claim has to fit.
- [Accomplishments by domain](../concepts/accomplishments-by-domain.md) — the same material organized for drafting rather than for gap-spotting.
- [Coverage history](coverage-history.md) — how the figure moved, and what each past pass promoted.
- [Brag ledger](../sources/brag-ledger.md) — ingest and promotion state per entry.
- [Brag file workflow](../workflows/brag-file.md) — capture and ingest.
- [Voice and prominence](../workflows/voice-and-prominence.md) — how a claim's support here decides how loudly it may be made outward.
