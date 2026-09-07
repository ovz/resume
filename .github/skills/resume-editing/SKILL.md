---
description: "Editing an outward-facing resume document: load the LLM-wiki resume shard first (cut points, Wayback link conventions, sensitivity tiers, update workflow)."
applyTo: "markdown/**/*.md"
---

# Resume source editing

Before changing any file under `markdown/`, read, in this order:

1. `llm-wiki/wiki/resume/primary-resume.md` — structure, cut points, section and style rules.
2. `llm-wiki/wiki/resume/link-conventions.md` — every hyperlink is a pinned Wayback Machine snapshot.
3. `llm-wiki/wiki/resume/update-workflow.md` — the edit pass, including render check and hand-off.

`markdown/Oleg.Zhylin.resume.achievements.md` is the primary, public resume (mirrored to LinkedIn). Keep it at the public tier defined in `llm-wiki/wiki/workflows/sensitivity-tiers.md`. Do not promote brag entries directly; they flow through `llm-wiki/wiki/concepts/accomplishments-by-domain.md`. Agents do not commit.
