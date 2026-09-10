# Publish the resume to LinkedIn

> **Doc type:** how-to
>
> How the generated blocks in [`linkedin/`](../../../linkedin/) reach the LinkedIn profile, why that last step is a human pasting rather than an API call, and how the credentials for the one thing that *can* be automated are stored. Audience: the owner, and any agent asked to "push the resume to LinkedIn" or "automate the LinkedIn update".

## The answer, first

**LinkedIn cannot be updated programmatically from this repository.** Not "with difficulty" — the path is closed, and this page exists so the question is researched once rather than every time it comes up.

| Route | Verdict |
|---|---|
| LinkedIn **Profile Edit API** — writes `summary` (the About section) and a position's `description`, exactly the two fields this repo generates | **Closed.** Requires the private `w_compliance` permission. See below. |
| Any other official API | **Does not write profile fields.** The self-serve tier can read your own basic profile and publish a post. Neither touches About or Experience. |
| Browser automation — Playwright, Selenium, a userscript | **Prohibited, and a bad trade.** See *Why not automate the browser*. |
| **NemoClaw** / OpenShell sandboxing | **Not a route.** It is a runtime, not an integration. See *Where NemoClaw fits*. |

What *is* available and worth having: a **post** announcing the update, published through the self-serve `w_member_social` scope. That is a genuinely supported API call, and it is the only write this repo can legitimately make.

So the working arrangement is: the build renders the blocks, [paste assist](#workflow-a-the-paste-round) makes moving them a two-command loop and *records that it happened*, and the optional [announce post](#workflow-c-optional-announce-the-update) is automated.

## Why the Profile Edit API is closed

The API is real and does precisely what would be wanted. Its own documentation opens with:

> The use of this API is restricted to those developers approved by LinkedIn and subject to applicable data restrictions in their agreements.

The permission it requires is `w_compliance`, described in the same table as *"a private permission and access is granted to select developers."* That permission belongs to the **Compliance API Partner Program**, and every gate on it fails for an individual:

- It is a **private, paid partnership**, granted at LinkedIn's discretion.
- The partner or its customers must be **FINRA/SEC registered**.
- The sanctioned use case is **archiving and monitoring member posts for FINRA/SEC compliance** — not maintaining one's own profile.
- The programme is **not accepting new partners**; compliance permissions are documented for reference only and cannot be requested.

Two further requirements would bind even if access were granted, and both are worth knowing because they describe the spirit of the rule: *"The user must request the change to their profile"* and *"The user's change must be posted unaltered to the profile."* LinkedIn's position is that a profile is a person's own statement about themselves. That is not an obstacle to route around; it is the same reason the resume in this repo is written in the first person and reviewed by its owner before it ships.

**Do not re-litigate this per pass.** If the situation changes, it will change by LinkedIn opening a self-serve profile-write product, which would be announced rather than discovered by probing.

## Why not automate the browser

Filling the About field with a headless browser is technically trivial and specifically prohibited. LinkedIn's User Agreement §8.2 bars *developing, supporting or using software, devices, scripts, robots or any other means or processes (including crawlers, browser plugins and add-ons) to scrape the Services or otherwise copy profiles and other data*, and separately bars *using bots or other automated methods to access the Services*. Enforcement is account restriction or termination.

Weigh the trade honestly. The gain is perhaps two minutes, a handful of times a year. The stake is the account that this entire repository exists to keep current — the one linked from the résumé header, the one recruiters are pointed at. **An asymmetric bet against your own shop window.** The paste stays manual.

This is a policy decision recorded here, not a technical limitation to be re-evaluated by the next agent. An agent asked to "just automate the LinkedIn update" should quote this section and offer Workflow A instead.

## Where NemoClaw fits

[NemoClaw](https://github.com/NVIDIA/NemoClaw) is NVIDIA's reference stack for running AI agents inside OpenShell sandboxes — managed inference, network policy, egress control, snapshots, lifecycle. It is installed on this workstation and it is **orthogonal to this problem**: it changes *where code runs and what it may reach*, never *what LinkedIn permits*. Running a prohibited browser automation inside a sandbox does not make it permitted; it makes it a prohibited action with better egress logging.

It does have one honest use here. If [Workflow C](#workflow-c-optional-announce-the-update) is ever set up, the posting script holds an OAuth token and makes an outbound call to exactly one host. That is a good fit for a sandbox with an allow-list egress policy: the token cannot be exfiltrated to anywhere but `api.linkedin.com`, and the credential never enters the general-purpose agent's environment. That is a hardening measure for a workflow that already exists, not a way to obtain capability.

## Workflow A: the paste round

The routine after any resume change. Two commands per field, and the loop is resumable — the record of what has been pasted lives in `linkedin/paste-state.json`, which is committed, so it survives a commit, a reboot, and a fresh clone.

```bash
script/pandoc_resume.sh all          # rebuild; regenerates linkedin/ and enforces the budgets
script/linkedin-sync.py status       # what is out of sync with the profile
```

`status` compares the SHA-256 of each generated block against the hash recorded when it was last confirmed pasted, and reports `NEVER PASTED`, `NEEDS PASTE`, or `in sync`. It exits non-zero while anything is outstanding, so it works as a check in a script or a shell prompt.

Then, for each block it names:

```bash
script/linkedin-sync.py copy about --open   # clipboard + open the profile
#   ... paste into LinkedIn, save ...
script/linkedin-sync.py done about          # record it
```

Three things about the paste itself:

- **Select all in the LinkedIn field before pasting.** LinkedIn appends to whatever is in the box rather than replacing it, and a doubled About section is over the limit and reads badly.
- **The About field is "About"; each Experience description is edited inside that position's own entry.** Employer, title and dates are separate LinkedIn fields — the generated blocks deliberately contain none of them, so nothing is duplicated.
- **LinkedIn's own counter should agree with ours.** If it says you are over, something has gone wrong in the conversion; check `linkedin/README.md` for the block's recorded length rather than trimming blind.

Finish by committing `linkedin/paste-state.json`. An uncommitted paste record is the one thing that makes the next round start from "did I do this?".

### When `status` disagrees with reality

The record is a claim about the profile, not an observation of it — nothing here can read LinkedIn back. If you edited a field directly on the site, the state file is now wrong. Re-run the paste from the generated block (the repo is the source of truth) or, if the site's text is the one you want, bring it back into `markdown/Oleg.Zhylin.resume.achievements.md` and rebuild. Do not hand-edit `paste-state.json`; run `done` after making the two agree.

## Workflow B: credentials in the keyring

Only Workflow C needs these. Set them up when you set that up, not before — the paste round needs no credentials at all, which is why it is the workflow that is always available.

Secrets live in the login keyring via `secret-tool`, under `service=linkedin-resume`, one item per `account`. The helper is `.github/skills/linkedin-publish/secrets.sh`:

```bash
secrets.sh accounts                  # what this integration uses, and what is backed up
secrets.sh set client-secret         # silent prompt; the value never enters argv
secrets.sh list                      # names and dates only — never values
secrets.sh get access-token          # one value, to stdout; pipe it
```

Every credential is tagged **`backup=required`** or **`backup=derived`**:

| Account | Class | Why |
|---|---|---|
| `client-id` | required | Issued once by the developer console |
| `client-secret` | required | Reissuable, but reissuing rotates it for everything using the app |
| `refresh-token` | required | ~1 year; replacing it costs a browser round trip |
| `access-token` | derived | ~60 days, minted from the refresh token |
| `person-urn` | derived | Re-fetchable from the userinfo endpoint |

### Backing up, safely

Only the `required` set is exported. Backing up a token that expires in sixty days achieves nothing and widens the blast radius of the backup.

```bash
secrets.sh export ~/linkedin-secrets.gpg     # prompts for a bundle passphrase
gpg --decrypt ~/linkedin-secrets.gpg | cut -f1   # verify before you rely on it
```

The bundle is symmetrically encrypted with AES-256; the plaintext goes straight down a pipe into `gpg` and is never written to disk, so there is no temporary file to shred. **Treat the cloud as hostile**: it stores ciphertext, and the passphrase must not live in the same account — a bundle and its passphrase in one Drive is one compromise, not two. On a new machine:

```bash
secrets.sh import ~/linkedin-secrets.gpg
```

Derived values are absent by design and are re-minted on first use.

### What the keyring actually protects on this machine

Worth being clear-eyed, because it changes what the keyring is for here.

This workstation has **full-disk encryption** (LUKS on `nvme0n1p2`) and **display-manager autologin** enabled (`/etc/sddm.conf.d/autologin.conf`). With autologin, the session — and the keyring with it — opens without anyone typing a password. **The LUKS passphrase is therefore the real boundary.** The keyring is protecting these credentials from other processes and from casual shoulder-surfing, not from someone who has the disk passphrase and physical access.

That is an acceptable posture for a token whose entire capability is "post to my own LinkedIn feed", and it is the reason the scope should stay at `w_member_social` and nothing more. It would not be acceptable for a credential with real blast radius. Two consequences worth acting on:

- **Keep the scope minimal.** A token that can only post is a token whose loss costs an embarrassing post and a revocation, not an account.
- **Know how to revoke.** LinkedIn's *Settings → Data privacy → Permitted services* lists authorized apps; removing the app invalidates its tokens immediately. Do that first if a laptop goes missing, then `secrets.sh rm` and re-issue.

## Workflow C: optional, announce the update

Supported, self-serve, and the only write this repo can legitimately make. Set it up only if you actually want a post each time the resume changes — the profile fields still have to be pasted either way, so this adds reach, not automation.

**One-time setup.** In the LinkedIn Developer Portal, create an app, associate it with a Page you control, and add the **Share on LinkedIn** product — it is self-serve and grants `w_member_social` without review. Add **Sign In with LinkedIn using OpenID Connect** for the `openid`/`profile` scopes needed to learn your own member URN. Then:

```bash
secrets.sh set client-id
secrets.sh set client-secret
```

**Authorize once**, via the standard three-legged OAuth authorization-code flow, with `redirect_uri` pointed at a loopback address you hold open only for the length of the exchange. Store what comes back:

```bash
secrets.sh set refresh-token     # from the token response
secrets.sh set access-token
```

**Post**, against `POST https://api.linkedin.com/v2/ugcPosts` with `Authorization: Bearer <access-token>` and `X-Restli-Protocol-Version: 2.0.0`, author `urn:li:person:<id>`, visibility `PUBLIC`. Mint a fresh access token from the refresh token when it has expired rather than storing a long-lived one.

Rules to hold to, all of them consequences of the same idea — that this is your own voice being published:

- **Never post automatically from a hook or a cron.** A post is public speech; it gets a human pressing enter. The resume build must not acquire the power to publish.
- **Announce, do not paste.** The post says the resume changed and what changed; it is not the About text. The profile fields are still Workflow A.
- **The token posts, and that is all.** Do not add scopes speculatively.

## Related

- [Primary resume — structure and cut points](../resume/primary-resume.md) § *The LinkedIn mirror* — how blocks are marked and budgeted.
- [Update the outward-facing resume](../resume/update-workflow.md) — the edit pass that produces a new block in the first place.
- [`linkedin/README.md`](../../../linkedin/README.md) — generated; what each block is and how the conversion works.
- [`.github/skills/resume-tooling/SKILL.md`](../../../.github/skills/resume-tooling/SKILL.md) § *The LinkedIn export* — the build target.
- [Sensitivity tiers](sensitivity-tiers.md) — the blocks are T0 public; a post made from them is too.
