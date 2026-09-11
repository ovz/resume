# Primary Resume — structure, cut points, and editing rules

> **Doc type:** reference
>
> **Load this page before touching the primary resume.** It is the always-on shard for refining, improving, or updating [`markdown/Oleg.Zhylin.resume.achievements.md`](../../../markdown/Oleg.Zhylin.resume.achievements.md). Companion pages: [link conventions](link-conventions.md) (how hyperlinks must be built) and [update workflow](update-workflow.md) (the steps of an edit pass). Audience: the owner and any agent editing the resume.

## What the primary resume is

- **File:** [`markdown/Oleg.Zhylin.resume.achievements.md`](../../../markdown/Oleg.Zhylin.resume.achievements.md). The only document in this repository that is mirrored to the owner's LinkedIn profile (linked from the resume header); the Markdown file is the source of truth and LinkedIn is a *rendering* of it, produced by the build — see *The LinkedIn mirror* below.
- **Variants:** a role-specific variant exists at [`markdown/Oleg.Zhylin.resume.embedded.md`](../../../markdown/Oleg.Zhylin.resume.embedded.md), targeting an embedded/C++ Principal Engineer audience. It is T0 public on the same terms, follows every rule on this page, and shares the reference-link block through `markdown/_parts/`. See [update workflow](update-workflow.md) § *Tailored variants* for what differs and how to choose between them. **Rules on this page apply to every variant**, not just the primary.
- **Rendering:** `script/pandoc_resume.sh` builds every `markdown/*.md` through the `pandoc_resume` submodule (HTML, PDF, DOCX, RTF). Page-fit claims below must be verified against a render, not estimated from line counts.
- **Positioning:** the owner seeks an employer interested in the *work*, not the *titles*. Every edit should move weight toward outcomes, scope, and evidence, and away from job-title inflation. Current target roles named in the summary: Sr. Principal Engineer or Sr. Staff Engineer.
- **Genre:** "achievements resume" — a narrative document that reads well when cut at several depths (below). It is not a bullet-only ATS form; keyword coverage is handled by keeping the [skills matrix](../concepts/skills-matrix.md) reflected in the prose.

## The cut-point principle

The document is written so that a reader who stops at any of several conceptual and chronological points still leaves with a correct, self-contained picture. Depth increases monotonically; nothing essential appears only late. Limits are soft — recruiters and AI screeners read digitally — but each cut must still *work as a complete document* if printed and truncated there. The job of the early cuts is to **prompt the reader correctly**: set the frame through which everything after it is interpreted.

| Cut | Approximate size | Reader question it must answer | Intended content |
|---|---|---|---|
| **C0 — the half page** | ~½ printed page | "Who is this and why should I keep reading?" | Header + contact line; the blockquote summary (tenure since 1996, primary languages, domains, target role, architect/lead/manager value, team size). |
| **C1 — the single page** | ~1 printed page | "What is the arc and what is he looking for?" | C0 + *My Story* (security roots → Salford/Minitab ML era → GreatCall/Best Buy Health embedded era → AI since 2023, quality-left, toil elimination, Principal-level scope). |
| **C2 — the double-sided page** | ~2 printed pages | "What has he actually done that matters?" | C1 + *Most prominent achievements* (the headline bullets: embedded emergency-response software, positioning SME, fall detection, data engineering, ML GUIs, architecture breadth, API design, big data, legacy code, distributed-team leadership, Agile). |
| **Beyond C2** | open-ended | "Show me the detail / the timeline." | Chronological *Employment History*, then chronological *Projects Overview*, then *Education*, then optional *About me*. |

Rules that follow from the principle:

1. **Order within a cut is by importance; order beyond C2 is chronological (newest first) or optional.** Do not let a chronological instinct pull recent-but-minor items above C2 content.
2. **Never introduce a claim after C2 that changes the picture set by C0–C2.** If a new accomplishment is important enough to change the frame, it must also surface in C0/C1/C2 text.
3. **Every C2 bullet must trace to a project or employer section below it** so a reader who drills down finds the substance. Orphan bullets are a lint failure.
4. **Education goes after Experience.** It can be hoisted for a specific audience that requires it early (some employers/regions); when hoisted, keep it to the degree lines only.
5. **Optional "About me" lives at the bottom**, for readers who want it. The primary resume currently has none; the archived long resume's *Personal development* section (family, health, languages) is the candidate source — see [`sources/resume-full.md`](../sources/resume-full.md). Anything from it that names family members or their ages must be re-reviewed against [sensitivity tiers](../workflows/sensitivity-tiers.md) before appearing in a public document.
6. **Do not promote a brag entry straight into the resume.** Brag entries land in [accomplishments by domain](../concepts/accomplishments-by-domain.md) first; the resume pulls from there deliberately — see [update workflow](update-workflow.md).

### Current cut map (intended; unverified against a render)

Section order in the file as of the 2026-09-10 pass: header/contact → *My Story* (C1) → *Most prominent achievements* (C2) → *Side Note* on Wayback links → *Employment History* (2020–present Best Buy Health; 2018–2020 GreatCall; 2017–2018 Minitab; 2000–2017 Salford Systems; 1996–2000 IIT) → *Projects Overview* (2024–2026 regulated medical devices … 2000–2001 CART 4.0) → *Education*. An open maintenance item is to render the PDF and record where the page boundaries really fall; until then treat C1/C2 boundaries as design intent.

Two known divergences from the table above, both live:

- **The primary has no C0 summary blockquote.** The cut table describes one and the embedded variant has one; the primary opens straight into *My Story*. Either add it or amend the table — but decide, rather than leaving the two disagreeing.
- **The 2018–present employer now has depth below C2.** Until the 2026-09-10 pass *Projects Overview* was entirely Salford-era, so the current role — the longest and most relevant one — had no drill-down at all. Eight Best Buy Health sections were added. Rule 3 (every C2 bullet traces to a section below it) is satisfiable for the recent work for the first time.

## The LinkedIn mirror

LinkedIn is not a copy of this document and cannot be one. It accepts **no formatting whatsoever** — no bold, no italics, no links, no headings — and it caps each field: **2,600 characters for the About section** and **2,000 for each Experience description**. The full resume is roughly 27,000 characters.

So the mirror is generated, not maintained. Sections of this file are marked

```markdown
<!-- linkedin: experience-minitab limit=2000 title="Experience — Minitab" -->
```

and `script/pandoc_resume.sh linkedin` renders each marked span to plain text, checks it against its budget, and writes it to the tracked `linkedin/` directory. Consequences that bind an editing pass:

0. **The number of Experience sections is a budget decision as well as a factual one.** The 2018–present tenure is split at the GreatCall/Best Buy Health rebrand because that is how the profile lists it — and because two entries carry 4,000 characters where one carried 2,000. Never invent a position to buy space; do reflect a real boundary when there is one.
1. **The budgets are real constraints on this file, not on a separate one.** *My Story* and each *Employment History* section are marked. Text added inside one has to be paid for by text removed from it, and **the build fails** when a block is over — LinkedIn truncates silently on paste, so the failure has to happen here.
2. **Depth belongs below the marked sections.** *Most prominent achievements* and *Projects Overview* are unmarked and unbudgeted. When a promotion does not fit an Experience entry, that is where it goes; the marked sections carry the claims that change what a reader should know in the first two pages.
3. **Never raise a `limit=` to make a build pass.** It is LinkedIn's number.
4. **Formatting stays in the Markdown.** The same text renders to PDF, HTML, DOCX and RTF, where emphasis is load-bearing. The export strips it; do not pre-strip the source.
5. **Only this document carries markers.** One profile, one source — a duplicate slug in a variant is a hard build error.

Emphasis is dropped rather than faked with Unicode look-alike bold: screen readers announce those code points as gibberish, and neither LinkedIn's search nor third-party resume parsers match them as words. The bolded terms here are exactly the keywords worth being found by.

Getting a block from `linkedin/` onto the profile — and why that step has no API — is [publish to LinkedIn](../workflows/linkedin-publish.md).

Mechanics and the exporter's own reasoning: [`.github/skills/resume-tooling/SKILL.md`](../../../.github/skills/resume-tooling/SKILL.md) § *The LinkedIn export*, and the generated [`linkedin/README.md`](../../../linkedin/README.md).

## Section conventions

- **Header:** avatar image (`assets/oleg-zhylin-gravatar.png`), name, one contact line (email, cell, home address, LinkedIn). Contact details are public by the owner's choice.
- **Summary blockquote:** two paragraphs. Paragraph 1 = tenure, languages, domains, target role. Paragraph 2 = value as architect / lead / manager, team size, methodology. Bold the load-bearing nouns; this is what a skimming reader sees.
- **My Story:** first person, one paragraph per career chapter, chronological, ending with the present and the aspiration. Chapters cite the employer via a reference-style link (Wayback-archived; see [link conventions](link-conventions.md)). **This section is the LinkedIn About text**, so it opens with the frame rather than building to it — LinkedIn shows only the first two or three lines before a *see more*, and a reader who does not expand should still have the answer.
- **Most prominent achievements:** unordered list; each bullet opens with a bold or italic-bold headline noun phrase, then one to four sentences of *what*, *why it mattered*, *how*. Ordered by importance to the target role, not by date.
- **Side Note on hyperlinks:** must stay immediately before the first section dense with links (currently *Employment History*). It tells the reader that links go to the Internet Archive on purpose. Do not delete or move it below the links it explains.
- **Employment History:** `### <years>. [Employer][ref]. <Title>.` heading, then narrative paragraphs. Newest first. Titles are stated but not emphasized. **Each section is a LinkedIn Experience description** and is budgeted at 2,000 characters; the marker sits below the heading, because LinkedIn stores employer, title and dates in their own fields and they must not be repeated in the description.
- **Projects Overview:** `### <years>. <Project>` headings, newest first, prose plus lists. Opens with "*Please feel free to ask me for stories from any of the projects below.*" — keep that invitation; it signals depth is available on request.
- **Education:** `### <years> <Degree>. "<Program>"` then institution link and one line of context.
- **Reference-style link block** at the end of the file; every `[key]` used above must be defined there. Keys are lowercase snake_case (`spm82`, `r4`, `bbh`).

## Style conventions

- Emphasis: **bold** for technologies, domains, and headline nouns; *italic* for role nouns, product names in running text, and asides. Keep the density consistent across sections — the early cuts are boldest.
- Numbers and scale are welcome (team of 15, 1 TB database, "orders of magnitude"); vague intensifiers are not.
- First person, past tense for completed work, present tense for ongoing role and aspiration.
- Employer-internal information stays out. The public tier in [sensitivity tiers](../workflows/sensitivity-tiers.md) defines the line; when in doubt, describe the outcome and the skill, not the internal artifact.

## Known defects to fix in the next edit pass

Recorded from the 2026-09 review of the file; see [`sources/resume-achievements.md`](../sources/resume-achievements.md) for line-level detail. Fix them through the [update workflow](update-workflow.md), not ad hoc.

## Related

- [Link conventions](link-conventions.md) — Wayback Machine discipline for every hyperlink.
- [Update workflow](update-workflow.md) — how an edit pass runs, renders, and is handed to the owner.
- [Accomplishments by domain](../concepts/accomplishments-by-domain.md) — the pool the resume draws from.
- [Skills matrix](../concepts/skills-matrix.md) — keyword coverage check.
- [Career overview](../overview.md) — the wiki's synthesis of the arc the resume narrates.
