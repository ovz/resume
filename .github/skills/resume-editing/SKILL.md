---
name: resume-editing
description: "Edit an outward-facing resume document in markdown/ — the public achievements resume or the private references document. Loads the depth, link and sensitivity rules that must be applied before changing either file, plus the render-and-verify step that closes the edit. USE WHEN asked to refine, update, tailor, or proofread the resume, or to promote an already-synthesized accomplishment onto it. DO NOT USE for editing the llm-wiki knowledge layer, and DO NOT USE for recording a new accomplishment as it happens — that is brag-capture, a separate earlier step."
---

# Resume source editing

The rules for editing these documents are in [`markdown/AGENTS.md`](../../../markdown/AGENTS.md). Read that file, then the three LLM-wiki pages it lists, before making any change.

This skill is the on-demand entry point for agents that match on skill descriptions; `markdown/AGENTS.md` is the same guidance delivered automatically when the edited file is in `markdown/`. The content is not duplicated here so the two cannot drift.

## The shape of the task

1. **Load the depth rules first.** `llm-wiki/wiki/resume/primary-resume.md` defines the cut principle. Text written before reading it usually lands at the wrong depth, which is this repo's most common failure.
2. **Draft against the wiki, not the brag files.** Accomplishments reach the resume through `llm-wiki/wiki/concepts/accomplishments-by-domain.md`, rewritten at each hop.
3. **Check the tier.** The achievements resume is public and mirrored to LinkedIn.
4. **Link as a Wayback snapshot**, defined in the reference-link block at the bottom of the file.
5. **Render and verify:** `script/pandoc_resume.sh all`. The run ends by asserting the portrait PNG is embedded in all four formats; a `NO IMAGE` line is a build failure, not a cosmetic one.
6. **Hand off.** Agents do not commit — see the root [`AGENTS.md`](../../../AGENTS.md).
