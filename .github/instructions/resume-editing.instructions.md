---
name: resume-editing
description: "Rules that apply when editing an outward-facing document under markdown/."
applyTo: "markdown/**/*.md"
---

You are editing an **outward-facing document**. `Oleg.Zhylin.resume.achievements.md` is the public resume, mirrored to LinkedIn; `Oleg.Zhylin.professional.references.md` is private.

Read [`markdown/AGENTS.md`](../../markdown/AGENTS.md) before changing anything here, then the three LLM-wiki pages it lists — depth and cut rules, Wayback link conventions, and the update workflow. That file carries the rules; this one only guarantees they are pulled in when the edited path matches.

Non-negotiables:

- The achievements resume is public tier. Nothing employer-internal goes in it.
- Brag entries are never copied in directly; they pass through `llm-wiki/wiki/concepts/accomplishments-by-domain.md`.
- Third-party contact details never leave the references document.
- Finish with `script/pandoc_resume.sh all` and treat any `NO IMAGE` line from its verify pass as a build failure.
- Agents do not commit.
