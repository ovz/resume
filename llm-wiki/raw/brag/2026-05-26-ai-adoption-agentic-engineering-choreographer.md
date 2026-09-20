---
title: "Led AI adoption and agentic engineering for developer productivity and token optimization"
date: "2026-05-01 to 2026-09 (design milestone 2026-05-26; ongoing)"
thread: AI
domains:
  - "AI-assisted engineering"
  - "leadership and organizational influence"
  - "developer productivity"
  - "knowledge management"
  - "cost discipline"
context: "Best Buy Health, engineering organization — Copilot/LLM tooling, multi-agent orchestration, internal knowledge base"
sensitivity: private-repo
resume-worthy: yes
---

# Led AI adoption and agentic engineering for developer productivity and token optimization

## What I did

Led the adoption and integration of advanced AI tooling and agentic workflows within the engineering organization, focused on using large language models and multi-agent orchestration to accelerate development, raise deliverable quality, and keep resource (token) usage under control.

- Designed and implemented a multi-agent orchestration layer — a "choreographer" agent shipped as an agent plugin — that coordinates LLM-based specialist agents and local skills, prevents context overflow through aggressive delegation, and enables dynamic skill discovery.
- Established a persistent, versioned internal knowledge base (an "LLM-wiki": raw capture → LLM synthesis → index) for AI-generated and human-curated knowledge, improving discoverability and reuse of best practices, code snippets, and design patterns.
- Developed and enforced prompt-engineering patterns and agent workflows that minimize token consumption while maximizing output quality; documented them as internal agent-quality and token-optimization guidelines.
- Integrated AI agents into code review, documentation generation, and release-note workflows, reducing manual effort and increasing consistency across deliverables.

The problems this addressed: developer productivity limited by manual orchestration of several AI tools and constant context switching (with context overflow as the failure mode); inconsistent application of AI-generated insights and no central place to share what worked; and unoptimized prompting and tool usage burning tokens and operating cost.

### Follow-up, 2026-09: the gap an agent noticed, and what it implies

While the owner prepared the beacon tracking release candidate in August 2026, AI-assisted research flagged that surviving a firmware-over-the-air update was missing from the 2023 design — without the updated firmware documents being part of what it had read ([2026-09-01 beacon tracking and FOTA persistence](2026-09-01-r5-beacon-tracking-fota-persistence.md)). The owner's position, in his own words (stated 2026-09-14, lightly corrected):

> This also confirmed my early intuition since I started doing agentic coding that the strength of AI coding agent is that it will read all the inputs and not forget about any important piece of 1000 pages manual. Obviously one might mis-prompt forgetfulness but I cannot imagine how I with my software engineering experience will ever prompt AI to do a bad job. And I don't believe junior engineers will ever be challenged to tell AI to do the best job possible. If anything, modern AI is not good enough to tell people that we have gaps in our risk management posture and require adequate grounding as a company policy (thus giving senior engineers and leaders more ways to help juniors), not just one of the "possible TODOs" checklists.

Read as a claim: the agent's advantage is completeness of reading, not judgement; the failure mode is an unchallenged prompt, which lands on less experienced engineers; and the remedy is organizational — grounding required by risk-management policy — rather than a checklist item. It connects this practice to the owner's [risk management](2023-08-03-risk-management-practice-early-analysis.md) work.

## Why it matters

- **Accelerated delivery:** reduced time-to-ship for key features and documentation by automating repetitive tasks and enabling parallel agent workflows.
- **Higher-quality deliverables:** more consistent code and documentation through shared, AI-driven best practices and knowledge reuse.
- **Optimal tokenomics:** lower operating cost by optimizing prompt structure and agent orchestration, evidenced by reduced average token consumption per workflow.
- **Organizational enablement:** reusable patterns and frameworks that let other teams adopt agentic engineering with minimal onboarding friction.

This is a *practice* accomplishment as much as a delivery: it establishes and maintains a way of working (delegation discipline, knowledge capture, cost discipline) whose value compounds over time, in the same spirit as the earlier operational-excellence programme (see *Related*).

Quantitative metrics (developer time saved, reduction in manual review cycles, aggregate token usage improvement) are pending post-adoption data.

## Skills demonstrated

Multi-agent system design, LLM prompt and context engineering, agent-plugin packaging, knowledge-management system design, cost/efficiency engineering ("tokenomics"), developer-experience leadership, organizational enablement and evangelism.

## Evidence

Merged pull request introducing the choreographer agent to the internal agent-plugin repository; the internal LLM-wiki knowledge base; internal agent-quality and token-optimization guideline documents.

## Related

- [2025-10-29-ai-data-product-in-alation](2025-10-29-ai-data-product-in-alation.md) — earlier AI-assisted-analytics exploration on the data-catalog side; this entry is the engineering-workflow side of the same "leverage AI since 2023" thread.
- [2024-04-18-r5-datadog-community-presentation](2024-04-18-r5-datadog-community-presentation.md) — precedent for reframing a team-level effort as reusable cross-team guidance; the same move is made here with agent patterns and the knowledge base.
- [2024-05-08-ccf-capability-framework-lcm-open-source](2024-05-08-ccf-capability-framework-lcm-open-source.md) — earlier enablement work sharing the same lever: reusable framework plus documentation and contribution guidelines to lower onboarding friction.
- [2026-09-01-r5-beacon-tracking-fota-persistence](2026-09-01-r5-beacon-tracking-fota-persistence.md) — the FOTA gap AI-assisted research caught, which the follow-up above draws on.

## Record history

- 2026-09-08: created from an owner-supplied brag write-up dated 2026-05-26
- 2026-09-14: *Follow-up, 2026-09* added from the owner's statement — the FOTA gap an agent noticed, and his position that grounding belongs in risk-management policy; *Related* link to the 2026-09-01 entry.
