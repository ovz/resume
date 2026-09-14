---
name: linkedin-publish
description: "Get the generated LinkedIn blocks from linkedin/ onto the LinkedIn profile. Covers the paste round and its committed record of what has actually been pasted, and carries the researched answer to whether any of it can be automated. USE WHEN asked to update, push, sync or publish the profile, when the build reports blocks that changed, or when asked whether the LinkedIn API can be automated. DO NOT USE for changing what the blocks say — that is resume-editing, which edits the Markdown the blocks are rendered from."
---

# Publishing to LinkedIn

The procedure, the research behind it, and the security posture live in [`llm-wiki/wiki/workflows/linkedin-publish.md`](../../../llm-wiki/wiki/workflows/linkedin-publish.md). Read that page. It is not restated here so the two cannot drift.

## Answer this before doing anything else

If the request is some form of *"automate the LinkedIn update"*, the answer is **no, and it has been researched**:

- The **Profile Edit API** writes `summary` and a position's `description` — exactly the fields this repo generates — and is gated behind the private `w_compliance` permission. That belongs to a paid, FINRA/SEC-scoped partner programme that is **not accepting applications**.
- **Browser automation is prohibited** by LinkedIn's User Agreement §8.2, on pain of account restriction. It is an asymmetric bet against the account the whole repository exists to keep current.
- **NemoClaw does not change either fact.** It governs where code runs and what it may reach, never what LinkedIn permits.

Quote the workflow page's reasoning and offer the paste round instead. Do not build browser automation, and do not propose a third-party scraping API as a workaround.

## The shape of the task

1. **Rebuild first.** `script/pandoc_resume.sh all` regenerates `linkedin/` and fails if a block is over its field limit.
2. **Ask what is outstanding.** `script/linkedin-sync.py status` — compares each block against the hash recorded when it was last confirmed pasted. Non-zero exit while anything is outstanding.
3. **Offer `round` when more than one block is stale.** `script/linkedin-sync.py round` walks every out-of-sync block in one pass — clipboard, the profile field it belongs in, record on confirm — and writes state after each, so an interrupted round loses nothing. For a single block, `copy <slug> --open` then `done <slug>`. The owner does the pasting; an agent never drives the browser.
4. **Commit `linkedin/paste-state.json`.** An uncommitted paste record is what makes the next round start from "did I already do this?".
5. **Hand off.** Agents do not commit — see the root [`AGENTS.md`](../../../AGENTS.md).

## Tools in this folder

`linkedin_sync.py` — paste assist and the paste record. It touches no secrets and makes no network requests, which is why the paste round works on any machine with a clipboard and needs no setup.

Nothing else lives here. Credential handling for the announce post was built, never wired up, and archived at [`llm-wiki/raw/archive/tools/linkedin-secrets.sh`](../../../llm-wiki/raw/archive/tools/linkedin-secrets.sh) with [a summary page](../../../llm-wiki/wiki/sources/archived-linkedin-secrets-tool.md). **Do not resurrect it into this folder speculatively** — it has no caller until a LinkedIn app and an OAuth exchange exist, and unused code in a live tool directory reads as a claim that it is used.

That summary page is also the place to start before writing *any* credential handling for this repo: it records two silent `secret-tool` traps, a backup classification worth reusing, and why secrets must never be passed as command-line arguments.
