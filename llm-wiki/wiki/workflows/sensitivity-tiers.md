# Sensitivity Tiers

> **Doc type:** reference
>
> Where each kind of information may live in this repository, and what must happen before it moves up a tier. Audience: the owner and every agent writing into `llm-wiki/`, `markdown/`, or `__untracked_stuff/`.

## Why tiers

The owner is a principal-level engineer; a great deal of what makes the career story true is knowledge an employer would consider internal. That knowledge legitimately lives in the owner's head and may be *used* to write accurate, outcome-level claims — but the artifacts, names, numbers, and internals themselves must not be published, and much of it should not even be committed. The repository is private; only the primary resume is public. Three tiers make the line explicit.

## The tiers

| Tier | Name | Where it lives | Who can see it | Examples |
|---|---|---|---|---|
| **T0** | **Public** | `markdown/Oleg.Zhylin.resume.achievements.md` and any future tailored variant in `markdown/` | Anyone (LinkedIn mirror, sent to recruiters) | Employers, product names already public, released products, publicly documented technologies, outcome-level claims ("drastically reduced cost of operation"), the owner's own contact details (owner's choice). |
| **T1** | **Private repo** | Everything else under version control: `llm-wiki/**` (including `raw/brag/`), `markdown/Oleg.Zhylin.professional.references.md`, `archive/**` | The owner and collaborators with repo access | Brag entries written at outcome level; wiki synthesis; reference contacts (third-party PII — handled below); personal correspondence already committed (see `sources/minitab-2018-correspondence.md`). |
| **T2** | **Never committed** | `__untracked_stuff/<scope>/session-wiki/raw/` (gitignored) or outside the repo entirely | The owner's workstation only | Employer-internal documents, OneNote/Confluence exports, PDFs, screenshots, meeting notes, internal metrics, customer names, code names, unreleased plans, incident details, anything "illegal, unprofessional, or unfair to reveal about a current or former employer". Also any file large enough to bloat the repo, regardless of content. |

## Rules

1. **Promotion is a rewrite, not a copy.** T2 → T1 means rewriting the fact at the level of *what the owner did, what skill it demonstrates, and what outcome it had*, with no internal artifact names, figures the employer has not published, or customer identities. Colleague and collaborator names are fine at T1 — see rule 8, which governs people in full. T1 → T0 means an additional pass through [primary-resume.md](../resume/primary-resume.md) § *Style conventions*, a check that every named product or technology is already public, and dropping colleague names.
2. **Committed files never reference T2 paths** (`__untracked_stuff/...`). A committed page may say "evidence retained offline"; it may not say where. This is the one-way reference rule from the `session-wiki-pattern` skill.
3. **Third-party PII stays in its source.** The references document holds phone numbers and emails of former colleagues. Wiki pages cite the document and may list name, relationship, and period; they never copy contact details. Consent to be a reference is not consent to be indexed.
4. **Brag entries carry a tier tag** (`sensitivity: public-friendly` or `sensitivity: private-repo`). An entry that cannot honestly be tagged either way is T2 material and belongs in the maintainer scope's `raw/`, not in `llm-wiki/raw/brag/`.
5. **Large files are T2 by size alone.** PDFs, images beyond the single avatar, exports. `.gitignore` already excludes `*.pdf`, `*.htm*`, and `__untracked_stuff`. An agent never adds an exception to this. **The owner may**, per rule 6, when the material is the owner's own property and losing it would be worse than storing it — the committed Trello board exports under [`raw/trello/`](../../raw/trello/) are the one standing case. Such an exception is recorded where the files live, states what it does *not* license (in particular, that an archived file is still not a source to quote outward), and never becomes a general precedent for committing exports. Once the owner has granted one, [large imports](large-imports.md) is the procedure that carries it out: the working copy stays uncompressed in a scratch scope, and the committed copy is compressed and checksummed.
6. **The owner may downgrade a tier, never an agent.** If an agent believes something committed should not be, it flags it in the maintainer tracker and leaves the file in place.
7. **A case that resists the policy is a defect in the policy.** Most brag input is written with the professional record in mind and classifies without effort. When something genuinely does not — an artifact type these rules do not cover, an ambiguous partner or customer reference — do not settle it with a silent one-off judgement. Apply the most conservative reading, record the case, and propose a refinement here. Repeated judgement calls in the same spot mean this page needs rewriting, not that the reader needs to be more careful.
8. **Names, roles and interactions belong in the record.** A career is made of people. Who the owner worked with, what their role was, how the collaboration ran, what was disagreed about and how it resolved, who mentored whom, how a team responded to a change the owner introduced — this is not incidental colour around the professional record, it *is* the professional record, and a wiki that strips it keeps the artifacts and loses the experience. So at T1: **record the interaction fully, including names and roles.** Do not soften it into "a colleague" or "a stakeholder"; do not drop the substance of a working relationship because it involved friction, a performance conversation, or a competing candidate for a promotion. Three things stay out regardless: contact details, which live only in the references document (rule 3); anyone under an NDA, an unannounced partnership, or an explicit request not to be named, who is recorded by role only; and gratuitous personal material with no bearing on the working relationship. Everything else is captured.

   **Capture is not disclosure.** These rules govern what is *written down at T1*, which is a private record the owner keeps in order to remember their own career accurately. What the owner then chooses to *say* — in an interview, a reference call, a conversation — is a separate judgement made in the moment, and is normally far more reserved: names rarely need mentioning to make a point about the work. Conflating the two is what produces a record too vague to be useful, so do not pre-redact the wiki on the theory that something might one day be repeated aloud. T0 remains the actual disclosure boundary, and colleague names come out there.

## Where the line usually falls (heuristics)

- A technology, vendor, or partner the employer has publicly acknowledged (e.g. a vendor named in a press release or product page) → T0-eligible.
- The *fact* that an OKR was met, an operational metric improved, a launch shipped → T0-eligible at outcome level; the metric's value and the internal dashboard → T2.
- An internal system's name → T2; its *function* ("a telemetry pipeline", "device-side test harness") → T0-eligible.
- A colleague's contribution, a disagreement, a mentoring relationship, a reorganization → name the people and record what actually happened; T1 (names come out at T0). This is the professional record, not an aside to it — see rule 8. Contact details stay in the references document. Exception: partners or individuals covered by an NDA, an unannounced partnership, or an explicit request not to be named → role only.
- Anything about a current employer's roadmap → T2 until it ships publicly.
- **An internal name that happens to sound generic is still an internal name.** "Defensibly generic" is not the test; *is this what the team calls it internally?* is. Such a name gets a public alias, below.

## Public aliases for internal names

Some internal names read like ordinary English, which is exactly how they leak. Each one below has a **public alias** used on every outward surface — the resumes, LinkedIn, and any story or synthesis page whose text could be spoken or copied outward. The internal name stays in the brag entry that records the work, at T1, because that is where the owner needs to recognise it; the entry notes the alias so the mapping is never lost. The alias describes **function, in lower case** rather than inventing a pseudo-product name, which is what keeps it from reading as a disclosure of its own.

| Internal name (T1 only) | Public alias | What it is | Entry |
|---|---|---|---|
| CCF — "Capability and Configuration Framework" | **component framework** (embedded C, across device SKUs) | The framework standardizing how device features are declared, configured and brought up | [2026-04-26](../../raw/brag/2026-04-26-ccf-capability-framework-lcm-open-source.md) |
| "sensorhub" — the conventional name for the wearable's microcontroller | **sensor co-processor** (MCU) | The low-power microcontroller between the sensors and the application processor | [2021-11-22](../../raw/brag/2021-11-22-dead-reckoning-sensor-cluster-mcu-architecture.md), [2022-08-03](../../raw/brag/2022-08-03-odm-specification-authoring.md) |

Adding a row is how a new internal name is handled; do not coin an alias in one page and leave the others. A search for the internal name across `markdown/`, `linkedin/`, `wiki/stories/`, `wiki/concepts/`, `wiki/dream-jobs/` and `wiki/resume/` should return nothing but this table.

## Related

- [Brag file workflow](brag-file.md) — where the tier tag is applied.
- [Large imports](large-imports.md) — how an owner-granted rule 5 exception is actually carried out.
- [Archive a source](archive-source.md) — archived documents keep the tier they had.
- [Primary resume](../resume/primary-resume.md) — the T0 document.
