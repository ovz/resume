> Shard of the root [`AGENTS.md`](../../AGENTS.md). Load when the task matches its title.

# Sending material to about-me and Claude Cowork

Anything meant for the owner's about-me repository (`bitbucket.org/ovz/about-me`) is **never** written into a local about-me clone. About-me is downstream of Claude Cowork: it is curated by Cowork's weekly review, with its own fact-line format and a *Never store* list (no tokens, no account numbers, nothing about a minor's age or school). Owner's instruction, 2026-09-25.

**How to contribute: the mailbox, like any other recipient.** Anyone may drop a message straight into `~/mailbox/about-me/inbox/`: an agent here, or the owner by hand. No other repository has to be present or consulted first; the convention is the channel. An agent writing one keeps to the mailbox protocol (one self-contained Markdown file, Ask / Context / Done when, no secrets, no scratch paths), adds `bridge: about-me` to its frontmatter, and:

1. Writes each fact as `- [status · source · YYYY-MM-DD] The fact, as a complete sentence.` Status is `candidate` unless the owner said it.
2. Re-checks the *Never store* list above before saving, and says what was left out without repeating it.
3. Leaves an owner item in the session tracker ([`handoffs-and-tracker.md`](handoffs-and-tracker.md)): *submit the message to the Cowork "About Me" project.* Cowork is what turns it into an about-me milestone.

A note in the root `TODO.md` that is meant for about-me is a draft of such a message; turn it into one when working the tracker. When the agentic_linux repo is on the machine, its `profile/bridges/about-me.md` card has the bridge's full properties and the receiving side. It is extra detail, not a gate.

**Do not work around the credential guard.** Raw Claude Code transcripts contain pasted credentials, and the auto-mode classifier blocks bulk extraction from them. Digest from the committed record instead.

Where Cowork sits among the career repositories, and what it may and may not do: [`career-repositories.md`](../../llm-wiki/wiki/workflows/career-repositories.md) § *Claude Cowork*. This repository's direction relative to the cloud is a **round trip** — same page, § *Cloud direction*.
