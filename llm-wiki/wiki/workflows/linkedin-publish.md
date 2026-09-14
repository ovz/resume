# Publish the resume to LinkedIn

> **Doc type:** how-to
>
> How the generated blocks in [`linkedin/`](../../../linkedin/) reach the LinkedIn profile, why that last step is a human pasting rather than an API call, and how the credentials for the one thing that *can* be automated are stored. Audience: the owner, and any agent asked to "push the resume to LinkedIn" or "automate the LinkedIn update".
>
> **The sources behind every claim on this page** — live links, Wayback snapshots, immutable git pins and verbatim quotations, all read 2026-09-10 — are in [analysis/linkedin-api-access.md](../analysis/linkedin-api-access.md). Argue with those before overturning anything here.

## The answer, first

**LinkedIn cannot be updated programmatically from this repository.** Not "with difficulty" — the path is closed, and this page exists so the question is researched once rather than every time it comes up.

| Route | Verdict |
|---|---|
| LinkedIn **Profile Edit API** — writes `summary` (the About section) and a position's `description`, exactly the two fields this repo generates | **Closed.** Requires the private `w_compliance` permission. See below. |
| Any other official API | **Does not write profile fields.** The self-serve tier can read your own basic profile and publish a post. Neither touches About or Experience. |
| Browser automation — Playwright, Selenium, a userscript | **Prohibited, and a bad trade.** See *Why not automate the browser*. |
| **NemoClaw** / OpenShell sandboxing | **Not a route.** It is a runtime, not an integration. See *Where NemoClaw fits*. |

What *is* available and worth having: a **post** announcing the update, published through the self-serve `w_member_social` scope. That is a genuinely supported API call, and it is the only write this repo can legitimately make.

So the working arrangement is: the build renders the blocks, and [paste assist](#the-paste-round) makes moving them a single guided pass that *records that it happened*. The announce post is [an option that was researched and not built](#if-the-announce-post-is-ever-wanted).

## Why the Profile Edit API is closed

The API is real and does precisely what would be wanted. Its own documentation opens with:

> The use of this API is restricted to those developers approved by LinkedIn and subject to applicable data restrictions in their agreements.

The permission it requires is `w_compliance`, described in the same table as *"a private permission and access is granted to select developers."* That permission belongs to the **Compliance API Partner Program**, and every gate on it fails for an individual:

- It is a **private, paid partnership**, granted at LinkedIn's discretion.
- The partner or its customers must be **FINRA/SEC registered**.
- The sanctioned use case is **archiving and monitoring member posts for FINRA/SEC compliance** — not maintaining one's own profile.
- The programme is **not accepting new partners**; compliance permissions are documented for reference only and cannot be requested.

Two further requirements would bind even if access were granted, and both are worth knowing because they describe the spirit of the rule: *"The user must request the change to their profile"* and *"The user's change must be posted unaltered to the profile."* LinkedIn's position is that a profile is a person's own statement about themselves. That is not an obstacle to route around; it is the same reason the resume in this repo is written in the first person and reviewed by its owner before it ships.

Every quotation above is reproduced with its source in [the evidence page](../analysis/linkedin-api-access.md), which also records that the Compliance programme fails on four independent counts: private, paid, FINRA/SEC-scoped, and closed to new applicants.

**Do not re-litigate this per pass.** If the situation changes, it will change by LinkedIn opening a self-serve profile-write product, which would be announced rather than discovered by probing.

## Why not automate the browser

Filling the About field with a headless browser is technically trivial and specifically prohibited. LinkedIn's User Agreement §8.2 ("Dos and Don'ts"), clause 2, bars members from:

> Develop, support or use software, devices, scripts, robots or any other means or processes (such as crawlers, browser plugins and add-ons or any other technology) to scrape or copy the Services

That clause carries no qualifier: scripted interaction with profile fields is out, whatever the intent. Clause 13 separately bars *"bots or other **unauthorized** automated methods"* — the qualifier matters, and is what would leave [an announce post](#if-the-announce-post-is-ever-wanted) legitimate. Enforcement is account restriction or termination.

Weigh the trade honestly. The gain is perhaps two minutes, a handful of times a year. The stake is the account that this entire repository exists to keep current — the one linked from the résumé header, the one recruiters are pointed at. **An asymmetric bet against your own shop window.** The paste stays manual.

This is a policy decision recorded here, not a technical limitation to be re-evaluated by the next agent. An agent asked to "just automate the LinkedIn update" should quote this section and offer Workflow A instead.

## Where NemoClaw fits

[NemoClaw](https://github.com/NVIDIA/NemoClaw) is NVIDIA's reference stack for running AI agents inside OpenShell sandboxes — managed inference, network policy, egress control, snapshots, lifecycle. It is installed on this workstation and it is **orthogonal to this problem**: it changes *where code runs and what it may reach*, never *what LinkedIn permits*. Running a prohibited browser automation inside a sandbox does not make it permitted; it makes it a prohibited action with better egress logging.

It does have one honest use here. If [the announce post](#if-the-announce-post-is-ever-wanted) is ever built, the posting script would hold an OAuth token and makes an outbound call to exactly one host. That is a good fit for a sandbox with an allow-list egress policy: the token cannot be exfiltrated to anywhere but `api.linkedin.com`, and the credential never enters the general-purpose agent's environment. That is a hardening measure for a workflow that already exists, not a way to obtain capability.

## The paste round

The routine after any resume change. The loop is resumable — the record of what has been pasted lives in `linkedin/paste-state.json`, which is committed, so it survives a commit, a reboot, and a fresh clone.

```bash
script/pandoc_resume.sh all          # rebuild; regenerates linkedin/ and enforces the budgets
script/linkedin-sync.py status       # what is out of sync with the profile
script/linkedin-sync.py round        # then paste them all in one guided pass
```

`status` compares the SHA-256 of each generated block against the hash recorded when it was last confirmed pasted, and reports `NEVER PASTED`, `NEEDS PASTE`, or `in sync`. It exits non-zero while anything is outstanding, so it works as a check in a script or a shell prompt.

**`round` is the one to use when more than one block is stale.** It opens the profile once, then walks the out-of-sync blocks in order: each is put on the clipboard, named by the profile field it belongs in (`About (My Story)`, `Experience — GreatCall (2018-2020)` — read from the `title=` on the resume's own `<!-- linkedin: -->` markers), and recorded the moment you press Enter. `s` skips a block, `q` stops. **State is written after every block, not at the end**, so a round interrupted by a meeting keeps everything already pasted and the next `round` picks up the rest.

For a single block, the two-command form is still there:

```bash
script/linkedin-sync.py copy about --open   # clipboard + open the profile
#   ... paste into LinkedIn, save ...
script/linkedin-sync.py done about          # record it
```

Two things about the paste itself:

- **Select all in the LinkedIn field before pasting.** LinkedIn appends to whatever is in the box rather than replacing it, and a doubled About section is over the limit and reads badly.
- **LinkedIn's own counter should agree with ours.** If it says you are over, something has gone wrong in the conversion; check `linkedin/README.md` for the block's recorded length rather than trimming blind.

Finish by committing `linkedin/paste-state.json`. An uncommitted paste record is the one thing that makes the next round start from "did I do this?".

### When `status` disagrees with reality

The record is a claim about the profile, not an observation of it — nothing here can read LinkedIn back. If you edited a field directly on the site, the state file is now wrong. Re-run the paste from the generated block (the repo is the source of truth) or, if the site's text is the one you want, bring it back into `markdown/Oleg.Zhylin.resume.achievements.md` and rebuild. Do not hand-edit `paste-state.json`; run `done` after making the two agree.

## If the announce post is ever wanted

**Not built, and not needed for anything above.** The paste round requires no credentials, no LinkedIn app and no network access, which is exactly why it is the workflow that always works. This section exists so the option is not re-researched from scratch, and so the half of it that *was* built can be found.

A post announcing that the resume changed is the one write to LinkedIn that is genuinely supported: the **Share on LinkedIn** product is self-serve, grants `w_member_social` with no review step, and posts go to `POST https://api.linkedin.com/v2/ugcPosts` (150 requests per member per day, which is not a constraint here). It adds reach, not automation — **the profile fields still have to be pasted either way**.

What exists, and what does not:

| Piece | State |
|---|---|
| Credential storage: keyring via `secret-tool`, `backup=required`/`derived` tagging, AES-256 export bundle for cloud backup | **Built and tested**, then archived unused at [`raw/archive/tools/linkedin-secrets.sh`](../../raw/archive/tools/linkedin-secrets.sh) — see [its summary page](../sources/archived-linkedin-secrets-tool.md) |
| LinkedIn app with the Share on LinkedIn product | Does not exist |
| Three-legged OAuth exchange against a loopback redirect | Never written |
| The `ugcPosts` call | Never written |

Three rules would apply, all consequences of the same idea — that this is the owner's own voice being published:

- **Never post automatically from a hook or a cron.** A post is public speech; it gets a human pressing enter. The resume build must not acquire the power to publish. This is not only taste: §8.2 clause 13 bars automated methods that "drive inauthentic engagement", and what keeps an API-published post on the right side of that line is a person deciding to publish it.
- **Announce, do not paste.** The post says the resume changed and what changed; it is not the About text.
- **Keep the scope at `w_member_social` and nothing wider.** A token whose worst case is an embarrassing post and a revocation is an acceptable thing to hold on a workstation with display-manager autologin, where the LUKS passphrase is the real boundary. A credential with real blast radius would not be — see [the evidence page](../analysis/linkedin-api-access.md) § *Observed locally*.

## Related

- [Primary resume — structure and cut points](../resume/primary-resume.md) § *The LinkedIn mirror* — how blocks are marked and budgeted.
- [Update the outward-facing resume](../resume/update-workflow.md) — the edit pass that produces a new block in the first place.
- [`linkedin/README.md`](../../../linkedin/README.md) — generated; what each block is and how the conversion works.
- [`.github/skills/resume-tooling/SKILL.md`](../../../.github/skills/resume-tooling/SKILL.md) § *The LinkedIn export* — the build target.
- [Can LinkedIn be updated programmatically? The evidence](../analysis/linkedin-api-access.md) — the sources, quotations and retrieval links behind this page.
- [Archived: the LinkedIn credential tool](../sources/archived-linkedin-secrets-tool.md) — the credential handling that was built, why it is not in the working set, and what reviving it would take.
- [Sensitivity tiers](sensitivity-tiers.md) — the blocks are T0 public; a post made from them is too.
