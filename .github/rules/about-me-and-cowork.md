> Shard of the root [`AGENTS.md`](../../AGENTS.md). Load when the task matches its title.

# Sending material to about-me and Claude Cowork

Anything meant for the owner's about-me repository (`bitbucket.org/ovz/about-me`) is **never** written into a local about-me clone. About-me is downstream of Claude Cowork: it is curated by Cowork's weekly review, with its own fact-line format and a *Never store* list (no tokens, no account numbers, nothing about a minor's age or school). Owner's instruction, 2026-09-25.

**How to contribute:**

1. Write a **self-contained message** in `~/mailbox/about-me/inbox/`, following the mailbox protocol in the `agentic_linux` repository's `docs/mailbox.md` (Ask / Context / Done when; no secrets; no scratch paths).
2. Head it with the note that the owner must **submit it to Claude Cowork online** (the "About Me" project); from there it flows into the about-me repository as a milestone zip.
3. Use about-me's `[status · source · date]` fact-line format.
4. Leave a **submit-to-Cowork item** for the owner in the session tracker ([`handoffs-and-tracker.md`](handoffs-and-tracker.md)).

**Do not work around the credential guard.** Raw Claude Code transcripts contain pasted credentials, and the auto-mode classifier blocks bulk extraction from them. Digest from the committed record instead.

Where Cowork sits among the career repositories, and what it may and may not do: [`career-repositories.md`](../../llm-wiki/wiki/workflows/career-repositories.md) § *Claude Cowork*. This repository's direction relative to the cloud is a **round trip** — same page, § *Cloud direction*.
