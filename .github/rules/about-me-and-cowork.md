> Shard of the root [`AGENTS.md`](../../AGENTS.md). Load when the task matches its title.

# about-me and Claude Cowork

**about-me pulls; this repository sends nothing.** The owner's about-me repository (`bitbucket.org/ovz/about-me`) aggregates who the owner is. Its own agent ingests the weekly zips from the Cowork "About Me" task and other cloud sources. On request it also scans the committed git history of every repository under `~/bitbucket`, this one included, for persona facts. Owner's direction, 2026-10-02. It replaces the earlier rule that each repository wrote digests for Cowork.

From here, that means:

- **Write no digests for about-me, and raise no "submit to Cowork" owner items.** about-me reads this repository's committed record. Keeping the record committed and well dated is the whole contribution.
- **Never edit an about-me clone.** Only about-me's own agent edits it.
- **A one-off fact that this repository's record does not hold**, such as something the owner mentions in passing, may go to the mailbox recipient `about-me` as an ordinary mailbox message with `bridge: about-me`. about-me's agent curates it. Nothing more is owed.
- **Reading about-me is fine.** Its voice reports help spoken drafts, and this repository's voice rules win wherever they differ ([career repositories](../../llm-wiki/wiki/workflows/career-repositories.md)).
- **Do not work around the credential guard.** Raw Claude Code transcripts contain pasted credentials. The committed record is the source.

How about-me ingests, scans and curates is set out in about-me's own `AGENTS.md`. The bridge's properties are in the about-me card in the agentic_linux repo. Where Cowork sits among the career repositories is in [`career-repositories.md`](../../llm-wiki/wiki/workflows/career-repositories.md) § *Claude Cowork*.
