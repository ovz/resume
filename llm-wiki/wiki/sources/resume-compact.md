# Compact Resume

> **Doc type:** reference
>
> Source and claim map for [the compact variant](../../../markdown/Oleg.Zhylin.resume.compact.md), the edition submitted wherever a page limit applies. Audience: the owner choosing what to submit, and agents carrying a change from the primary into it. The resume is T0 public; this provenance page is T1. Its brief, covering audience, budget and boundaries, is in [variants](../resume/variants.md#compact-page-limited-submissions--live).

## What it is

The compact variant is the [primary resume](resume-achievements.md) under a page budget. It is not tailored to an audience. It exists because some submission systems cap a resume's length (the first case, in October 2026, was a recruiter's ten-page limit, most likely applied to the DOCX as their system renders it), and the primary renders at about eighteen pages. So the compact variant **says nothing the primary does not say**. It shares every piece of text the budget allows, and it departs from the primary only where the budget forces it.

| Depth | Content | Where the text lives |
|---|---|---|
| C0–C1 | Header and *My Story* | Shared fragments [`header.md`](../../../markdown/_parts/header.md) and [`my-story.md`](../../../markdown/_parts/my-story.md). *My Story* is the LinkedIn About text, so the compact edition and the profile always say the same thing |
| C2 | *Most prominent achievements*: 16 bullets in three groups. **Embedded devices for health and safety** (9), **How I work** (3), **Machine learning, before the mainstream** (4) | Inline, except the two shared bullets [`bullet-retail-shelf.md`](../../../markdown/_parts/bullet-retail-shelf.md) and [`bullet-operational-excellence.md`](../../../markdown/_parts/bullet-operational-excellence.md) |
| Beyond C2 | *Employment History*: one short paragraph per period, naming that period's threads without elaborating them. An invitation line offers the stories behind the achievements, and the full edition | Inline |
| — | Side note, *Education* (degrees only), link block | Shared fragments |

The group headings name no employer or date range. Resume parsers look for an employer-and-dates pattern, and a heading like that inside the achievements section can be parsed out as a duplicate position. Each bullet names its place and year in its own text instead.

## Page budget

**At most 7 pages as a DOCX, measured by opening it in LibreOffice.** That leaves about 30% headroom under a 10-page cap, which covers the difference between LibreOffice, Word and an ATS conversion, and between Letter and A4 paper. Measured on 2026-10-07: 6 pages as the build's PDF and 7 as the DOCX, with the seventh page less than half full. The primary measured 18 and 19 pages the same day.

How to measure, after any change to the compact text or to a fragment it includes:

```bash
script/pandoc_resume.sh all
soffice --headless --convert-to pdf --outdir <scratch> pandoc_resume/output/Oleg.Zhylin.resume.compact.docx
pdfinfo <scratch>/Oleg.Zhylin.resume.compact.pdf | grep Pages
```

The fragments are the part to watch. *My Story* is capped by LinkedIn at 2,600 characters, so it cannot grow far. The two shared bullets have no cap, though, and a sentence added to either one for the primary's sake also lands here.

## Claim provenance

Every compact bullet condenses text already in the primary. The table names the primary sections each one draws on, so that a change to any of them shows which compact bullet has to follow, and the coverage threads behind them.

| Compact bullet | Primary text it condenses | Threads |
|---|---|---|
| *Architecture Ownership, from the first device to the portfolio* | Achievements *Architecture Ownership* and *Original Embedded Software*; GreatCall employment, first paragraph | `ARC`, `AI` |
| *Embedded software sold off the shelf* | Shared fragment, identical | `SHELF` |
| *Concurrency and Network Programming* | Achievements bullet of the same name; project *Concurrency on the device* | `CONC`, `BOOST` |
| *Positioning Technologies* | Achievements bullet; Best Buy Health employment (the Skyhook upgrade); project *Location Engine and BLE beacon tracking* | `POS` |
| *Fully Automated Fall Detection* | Achievements bullet; project *Next generation wearable* (the sensor cluster) | `FALL`, `DEV` |
| *Regulated Medical Devices* | Achievements bullet; project *Regulated medical devices* (the PPG description and the firmware defect) | `MED` |
| *Embedded Platform Foundations* | Achievements *Embedded Platform Frameworks*; projects *Embedded component framework* and *Embedded platform: monorepo, packaging and C++ standards* | `FW`, `BLD` |
| *Operational Excellence and Observability* | Shared fragment, identical | `OBS` |
| *Data Engineering, from consulting cases to a device recall* | Achievements *Data Engineering*; GreatCall employment, the 2019 recall paragraph | `DATA`, `CRISIS` |
| *Integration, and the engineer-to-engineer relationships it runs on* | Achievements *Integration* and *Hardware and software cadences* | `INT`, `MFG` |
| *Stewardship, practised by shifting quality left and eliminating toil* | Achievements *Stewardship*; GreatCall employment, the on-device test paragraph | `STEW`, `QA`, `RSK` |
| *Management, Technical Leadership, and the people who make Agile work* | Achievements *Agile*, *Raising the bar* and *Management of distributed teams*; Salford employment, last paragraph | `LEAD` |
| *Machine Learning products, from the desktop to the cloud* | Achievements *Advanced GUI*, *Software Architecture* and *API Design*; Salford employment, second and third paragraphs | `SALF` |
| *Big Data and Distributed Machine Learning* | Achievements bullet, identical | `SALF` |
| *Machine Learning engines from the inside, and legacy code* | Achievements bullet; Salford employment (64 bits, Unicode) | `AI`, `SALF` |
| *Custody of a company's engineering through its acquisition* | Minitab employment; project *Acquisition of Salford Systems by Minitab* | `SALF`, `STEW` |

The five employment paragraphs summarize the primary's employment sections of the same period, and add no claim of their own.

Coverage is unchanged by this document. The [coverage map](../resume/coverage.md) measures the primary, and nothing reached the compact edition without being in the primary first.

## Deliberate exclusions

Everything below stays in the primary and is the material to offer when a reader asks for a story:

- **All of *Projects Overview*.** It is about thirty thousand characters, roughly ten pages on its own.
- **From Best Buy Health:** the firmware-over-the-air escalation during the inventory crisis, the wearable power budget and dead-reckoning study, the beacon-tracking design restraint, the risk and launch-readiness detail beyond one line, and the manufacturer-facing specification set.
- **From the Salford Systems era:** the CART-era GUI work, the Hive scoring utility, the national health survey data preparation, the Brazilian retail project, the Codemeter selection, internationalization, and SPM 7.0 and 8.2 release detail.
- **Elsewhere:** the *Rust* do-it-yourself paragraph from the concurrency bullet, the GreatCall interview challenges, and the Lyceum "Professional" schooling.

## Carrying a change into the compact edition

1. A new accomplishment reaches the primary first, through the [update workflow](../resume/update-workflow.md), and never lands here first.
2. Find the primary section it changed in the provenance table above. If a compact bullet condenses that section, decide whether the change alters what a reader should take from that bullet. Usually it does not, and the compact edition stays as it is.
3. A change to *My Story* or to either shared bullet arrives automatically. Re-measure the page count.
4. When a new primary achievement deserves a compact bullet, add it to the group it belongs in and give it a row in the table above, then re-measure.
