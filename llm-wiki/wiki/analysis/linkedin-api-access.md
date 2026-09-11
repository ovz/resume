# Can LinkedIn be updated programmatically? The evidence

> **Doc type:** explanation
>
> The sources behind the verdict in [workflows/linkedin-publish.md](../workflows/linkedin-publish.md), with the exact wording each claim rests on and three ways to retrieve what was read. Audience: anyone re-opening the question — including a future agent told to "just automate the LinkedIn update". Tier **T1**.
>
> **Read on 2026-09-10.** Every quotation below was taken from the primary source on that date, not from a search-result summary, except where a row says otherwise.

## Why this page exists separately

[The workflow page](../workflows/linkedin-publish.md) states the verdict and gets on with the job. This page holds the receipts, because the verdict is a *negative* — "there is no supported path" — and a negative is exactly the kind of claim that gets quietly re-litigated by the next person who assumes nobody checked properly. Anyone who wants to overturn it should have to argue with the quotations below rather than with a summary of them.

It also exists because the verdict has a shelf life. LinkedIn could open a self-serve profile-write product tomorrow. When that is being assessed, the useful question is not "what does the documentation say now" but "what changed since 2026-09-10" — and that requires knowing precisely what it said then.

## How to retrieve what was read

Three mechanisms, strongest first. Use whichever the row offers.

1. **Git pin (strongest).** Microsoft Learn's LinkedIn documentation is generated from a public repository, and every page embeds the commit it was built from. A `blob/<sha>/` URL is immutable, points at the exact revision read, and cannot be edited or rate-limited out of existence. This beats a Wayback snapshot outright, and it is why the missing snapshots below are an inconvenience rather than a problem.
2. **Wayback snapshot.** Pinned to a 14-digit timestamp, per the repo's [link conventions](../resume/link-conventions.md). Check the snapshot date against the page's own `updated_at`: a snapshot older than the last edit shows *different text than was read*, and one row below has exactly that defect.
3. **The verbatim quotations** in *The evidence* section. Even if every external source vanishes, the sentences the verdict rests on are committed to this repository.

## Source ledger

| # | Source | Live | Wayback | Git pin (immutable) | Page last updated |
|---|---|---|---|---|---|
| 1 | **Profile Edit API** — the write path that would do the job | [live](https://learn.microsoft.com/en-us/linkedin/shared/integrations/people/profile-edit-api) | [20260212045749](https://web.archive.org/web/20260212045749/https://learn.microsoft.com/en-us/linkedin/shared/integrations/people/profile-edit-api) ⚠ **stale** | [`57591bf`](https://github.com/MicrosoftDocs/linkedin-api-docs/blob/57591bfcfd413f08f52e5aada0d48925d0bf43a6/linkedin-api-docs/shared/integrations/people/profile-edit-api.md) | 2026-04-30 |
| 2 | **Profile Edit API — Positions** — the Experience-description write | [live](https://learn.microsoft.com/en-us/linkedin/shared/integrations/people/profile-edit-api/positions) | **none** | [`0405a67`](https://github.com/MicrosoftDocs/linkedin-api-docs/blob/0405a677c318861f186fb39bc5d60669d99a8e4d/linkedin-api-docs/shared/integrations/people/profile-edit-api/positions.md) | 2023-09-06 |
| 3 | **Compliance APIs Overview** — where `w_compliance` lives | [live](https://learn.microsoft.com/en-us/linkedin/compliance/compliance-api/overview) | [20231202002858](https://web.archive.org/web/20231202002858/https://learn.microsoft.com/en-us/linkedin/compliance/compliance-api/overview) | [`2a57bd2`](https://github.com/MicrosoftDocs/linkedin-api-docs/blob/2a57bd273f9b974f4baff4a55257e77a79b4c195/linkedin-api-docs/compliance/compliance-api/overview.md) | 2023-10-27 |
| 4 | **Compliance FAQ** — the partner-programme gate | [live](https://learn.microsoft.com/en-us/linkedin/compliance/compliance-api/compliance-faq) | **none** | [`b5e53c1`](https://github.com/MicrosoftDocs/linkedin-api-docs/blob/b5e53c17b6e3b6c284acb2f39f22eb0bd386203a/linkedin-api-docs/compliance/compliance-api/compliance-faq.yml) | 2026-05-15 |
| 5 | **Share on LinkedIn** — the one write that *is* self-serve | [live](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin) | [20260806085553](https://web.archive.org/web/20260806085553/https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin) | [`dba38de`](https://github.com/MicrosoftDocs/linkedin-api-docs/blob/dba38de9d1973312c5f3f989e034ab02c729c936/linkedin-api-docs/consumer/integrations/self-serve/share-on-linkedin.md) | 2023-12-14 |
| 6 | **LinkedIn User Agreement** — the automation prohibition | [live](https://www.linkedin.com/legal/user-agreement) | [20260910173926](https://web.archive.org/web/20260910173926/https://www.linkedin.com/legal/user-agreement) — **same day as reading** | — | — |
| 7 | **NVIDIA NemoClaw** — what it is and is not | [live](https://github.com/NVIDIA/NemoClaw) | [20260904103033](https://web.archive.org/web/20260904103033/https://github.com/NVIDIA/NemoClaw) | local clone, read directly | — |
| 8 | Vorp Labs, *permissions that are self-service* — **secondary, not read directly** | [live](https://vorplabs.com/agent-tools/linkedin-cli) | [20260806021129](https://web.archive.org/web/20260806021129/https://vorplabs.com/agent-tools/linkedin-cli) | — | — |

**Row 1's snapshot is stale and must not be quoted from.** The snapshot is 2026-02-12; the page was last updated 2026-04-30. The Wayback copy therefore shows a version *older* than the one this verdict rests on. Use the git pin for row 1.

**Rows 2 and 4 have no snapshot at all**, and Save Page Now could not be reached on 2026-09-10 — anonymous saves returned HTTP 520, and `archive.org`'s availability API rate-limited this host. Both rows have git pins, which is the stronger record anyway. If a snapshot is wanted later, see *Refreshing this page*.

**Row 8 is not load-bearing.** It informed the initial search but was never read directly, and everything it was used for is now grounded in row 5, which is authoritative. It is listed only so the trail is complete. A LinkedIn Help article on prohibited software (`linkedin.com/help/linkedin/answer/a1341387`) was likewise seen only as a search summary; row 6 is the primary source for that point and supersedes it.

## The evidence

### The write path exists and targets exactly the right fields

The Profile Edit API's basic-field list includes **`summary`** — the About section — typed as `MultiLocaleRichText`, with this sample body [1]:

> ```json
> { "patch": { "$set": { "summary": { "localized": { "en_US": { "rawText": "Awesome summary of me." } } } } } }
> ```

And its Positions sub-resource supports `CREATE | PARTIAL_UPDATE | DELETE`, with a writable `description` field [2]. Those two fields are precisely what `linkedin/about.txt` and `linkedin/experience-*.txt` contain. **The capability is not the obstacle.**

### It is gated behind a permission that cannot be obtained

The Profile Edit API page opens with [1]:

> The use of this API is restricted to those developers approved by LinkedIn and subject to applicable data restrictions in their agreements.

and lists one permission [1]:

> `w_compliance` — Required to manage and delete data for compliance. This is a private permission and access is granted to select developers.

The Compliance APIs overview repeats the restriction [3]:

> The use of these APIs is restricted to developers approved by LinkedIn. Reach out to your LinkedIn Relationship Manager or Business Development contact as you will need to meet certain criteria and sign an API agreement with data restrictions in order to use this integration.

And the Compliance FAQ closes every remaining door [4]:

> The Compliance API Partner Program is a private and paid partnership. Acceptance to this partnership is subject to discretion of LinkedIn based on the following criteria. The Partner organization or its customers should be FINRA / SEC registered. The primary use case should be archiving and monitoring LinkedIn member's posts and public correspondence as required to be compliant with FINRA & SEC regulations. Compliance API is a closed permission. The Compliance APIs are currently not accepting applications for new Partners due to resource constraints. Should this change, we will send out formal communications and update our request form.

Four independent disqualifications: private, paid, FINRA/SEC-scoped, and closed to new applicants. **This is a "no", not a "hard to get".**

### Two requirements that would bind even with access

Also from the Profile Edit API page, and worth keeping because they explain the *intent* rather than just the rule [1]:

> - The user must request the change to their profile
> - The users change must be posted unaltered to the profile

A profile is treated as a person's own statement about themselves. That is the same principle behind this repository's own rule that the owner reviews and commits every resume change rather than an agent doing it.

### Browser automation is prohibited by contract

LinkedIn's User Agreement, section 8.2 ("Dos and Don'ts") [6]:

> **Clause 2.** Develop, support or use software, devices, scripts, robots or any other means or processes (such as crawlers, browser plugins and add-ons or any other technology) to scrape or copy the Services

> **Clause 13.** Use bots or other unauthorized automated methods to access the Services, add or download contacts, send or redirect messages, create, comment on, like, share, or re-share posts, or otherwise drive inauthentic engagement

Two things to read carefully here, because the earlier draft of the workflow page paraphrased them loosely:

- **Clause 13 says "unauthorized" automated methods**, and explicitly names creating and sharing posts. Publishing through the official API with `w_member_social` is an *authorized* method and is therefore fine. Driving it from a cron so that posts appear without a human is much closer to "inauthentic engagement", which is why the workflow page requires a human to press enter.
- **Clause 2 has no such qualifier.** Scripted browser interaction with profile fields is prohibited outright, whatever the intent.

### What is self-serve, and its limits

Share on LinkedIn grants one permission [5]:

> `w_member_social` — Required to create a LinkedIn post on behalf of the authenticated member.

and is genuinely self-serve, with no review step [5]:

> If your application does not have this permission, you can add it through the Developer Portal. Select your app from My Apps, navigate to the Products tab, and add the Share on LinkedIn product which will grant you `w_member_social`.

Posts go to `POST https://api.linkedin.com/v2/ugcPosts` with header `X-Restli-Protocol-Version: 2.0.0`, and are rate-limited to **150 requests per member per day** and 100,000 per application [5]. That ceiling is irrelevant at this repo's volume and is recorded only so nobody has to look it up.

Note what this scope does *not* include: it creates posts. It does not read or write the profile. **Announcing an update and updating the profile are different operations, and only the first is available.**

### NemoClaw is orthogonal

NemoClaw describes itself as [7]:

> an open source reference stack for running supported AI agents more safely inside NVIDIA OpenShell sandboxes. It provides guided onboarding, managed inference, network policy, managed integrations, snapshots, and lifecycle operations through the NemoClaw CLI and its agent-specific aliases.

It governs **where code runs and what it may reach**, never what a remote service permits. Running a prohibited automation inside a sandbox does not make it permitted. Its one genuine use here is hardening the optional posting path, and that is recorded in the workflow page rather than here.

## Observed locally, 2026-09-10

Facts about this workstation that the workflow's security posture rests on. Re-check them rather than trusting this list if the machine is rebuilt.

| Observation | How it was checked | Why it matters |
|---|---|---|
| `secret-tool` present, libsecret 0.21.7; `gnome-keyring-daemon` owns `org.freedesktop.secrets` | `pacman -Qo`, `busctl --user list`, and a store/lookup/clear round trip | The keyring is a working secret store, so no new dependency is needed |
| **`secret-tool search` prints secret values in plaintext** | Stored two probe secrets and read the output | The obvious way to list stored credentials is a disclosure. The wrapper filters it |
| **`secret-tool search` writes results to stderr, not stdout** | `2>/dev/null` produced an empty listing; `2>&1 >/dev/null` produced 12 lines | Redirecting stderr — the reflex for a noisy tool — silently yields nothing rather than an error |
| Full-disk encryption: LUKS on `nvme0n1p2` | `lsblk -o NAME,FSTYPE` | Encryption at rest exists |
| **Display-manager autologin is enabled** (`/etc/sddm.conf.d/autologin.conf`, `User=ovz`) with `pam_gnome_keyring` in the sddm PAM stacks | `grep` of `/etc/sddm.conf.d/` and `/etc/pam.d/` | The session and keyring open without a password typed, so **the LUKS passphrase is the real boundary**, not the keyring |
| No GnuPG secret keys exist | `gpg --list-secret-keys` | `pass` and asymmetric encryption are unavailable without setup; the backup bundle uses `gpg --symmetric` instead |

The autologin finding is the consequential one: it is why the workflow insists the OAuth scope stay at `w_member_social` and nothing wider. A credential whose worst-case loss is an embarrassing post and a revocation is an acceptable thing to hold under that posture. A credential with real blast radius would not be.

## Refreshing this page

Re-open the question only on a signal — a LinkedIn developer-blog announcement, or a new self-serve product appearing in the Developer Portal's Products tab. Probing the API for changed behaviour is not a signal and is not worth doing.

When it is re-opened, check rows 1–5 against their live URLs, compare each page's `updated_at` with the value in the ledger, and rewrite *The evidence* rather than appending to it — a stale quotation next to a fresh one is worse than either alone.

To fill in the two missing snapshots (rows 2 and 4), from a host that `archive.org` is not rate-limiting:

```bash
for u in \
  "https://learn.microsoft.com/en-us/linkedin/shared/integrations/people/profile-edit-api/positions" \
  "https://learn.microsoft.com/en-us/linkedin/compliance/compliance-api/compliance-faq" ; do
  curl -sI "https://web.archive.org/save/${u}" | head -1
  sleep 10
done
# then read back the timestamp and record it in the ledger above:
curl -s "https://archive.org/wayback/available?url=<url>" | jq -r '.archived_snapshots.closest.timestamp'
```

Anonymous Save Page Now is unreliable; an archive.org account key makes it dependable. Row 1's stale snapshot should be refreshed the same way, since the git pin covers the claim in the meantime.

## Related

- [Publish the resume to LinkedIn](../workflows/linkedin-publish.md) — the verdict in practice, and the workflows that follow from it.
- [Link conventions](../resume/link-conventions.md) — why this repo pins Wayback timestamps at all.
- [Primary resume — the LinkedIn mirror](../resume/primary-resume.md) — what is being published, and its character budgets.
