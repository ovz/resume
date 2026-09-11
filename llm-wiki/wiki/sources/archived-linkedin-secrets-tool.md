# Archived: the LinkedIn credential tool

> **Doc type:** reference
>
> What [`raw/archive/tools/linkedin-secrets.sh`](../../raw/archive/tools/linkedin-secrets.sh) is, why it is archived rather than deleted, and what it would take to revive it. Audience: anyone who finds the script and wonders whether it is live, or who is about to write credential handling for this repo. Tier **T1**.

## What it is

A `secret-tool` wrapper: store, retrieve, list and remove credentials in the login keyring under `service=linkedin-resume`, plus an encrypted backup bundle for the subset that cannot be regenerated.

It was written on 2026-09-10 alongside the LinkedIn publishing research, to hold the OAuth credentials for an **announce post** — the one write to LinkedIn that is genuinely supported. It is tested end to end: set/get/list/rm against the real keyring, and an export/import round trip through a stubbed `gpg`.

## Why it is archived

**It serves a workflow that was never built.** The research it accompanied concluded that LinkedIn's profile fields cannot be written programmatically at all — see [analysis/linkedin-api-access.md](../analysis/linkedin-api-access.md). What survived that finding was the paste round, which needs no credentials, and an optional announce post, which was documented but not implemented because it requires a LinkedIn app that does not exist.

So the script had no caller. Left in `.github/skills/linkedin-publish/` it would have read as part of the working set, and the next person to open that folder would have had to work out for themselves that nothing invoked it. **Unused code in a live tool directory is a claim that it is used.**

It is archived rather than deleted because it works, it is tested, and the two behaviours it encodes are the kind that cost an hour each to rediscover.

## What it encodes that is worth keeping

Three things outlive the LinkedIn use case, and any future credential handling in this repo should start from them rather than re-derive them.

**Two `secret-tool` traps, both silent:**

- **`secret-tool search` prints secret values in plaintext.** The obvious way to list what is stored is therefore a credential disclosure — onto the terminal, into scrollback, and into the transcript of any agent sharing that terminal. The script filters the whole span between `secret = ` and `created = ` rather than pattern-matching around it, so a multi-line value cannot print a fragment of itself into the listing either. That was verified adversarially.
- **`secret-tool search` writes its results to stderr, not stdout.** Redirecting stderr away — the reflex when a tool is noisy — yields an empty listing rather than an error, so the failure looks like "nothing is stored".

**A backup classification worth reusing.** Every credential is tagged `backup=required` or `backup=derived`. Only the required set is exported. Backing up a token that expires in sixty days achieves nothing and widens the blast radius of the backup — the bundle becomes a richer target for no gain.

**A safe export shape.** The plaintext goes straight down a pipe into `gpg --symmetric --cipher-algo AES256`, so it never exists as a file and there is nothing to shred afterwards. Cloud storage is treated as hostile: it holds ciphertext, and the passphrase is kept out of the account holding the bundle.

Also worth carrying forward: **secrets are read from stdin or a silent prompt, never from a command-line argument**, because argv is visible in `ps`, in `/proc`, in shell history, and in an agent's view of the terminal.

## What it would take to revive it

Only if the announce post is actually wanted — the paste round does not need it.

1. Create a LinkedIn app, associate it with a Page, and add the self-serve **Share on LinkedIn** product for `w_member_social`.
2. Copy the script out of the archive into `.github/skills/linkedin-publish/` — copy, do not move; `raw/` is immutable.
3. Write the missing piece: a three-legged OAuth authorization-code exchange against a loopback redirect, and the `ugcPosts` call. That is the part that was never written.
4. Re-read [the workflow page](../workflows/linkedin-publish.md) § *If the announce post is ever wanted*, which carries the rules that apply — above all that a post is public speech and gets a human pressing enter, never a hook or a cron.

Before reviving it, re-check the keyring posture recorded in [analysis/linkedin-api-access.md](../analysis/linkedin-api-access.md) § *Observed locally*: this workstation has display-manager autologin, so the session and keyring open without a password and the LUKS passphrase is the real boundary. That is acceptable for a token scoped to `w_member_social` and nothing wider.

## Related

- [Publish the resume to LinkedIn](../workflows/linkedin-publish.md) — the live workflow, which needs no credentials.
- [Can LinkedIn be updated programmatically? The evidence](../analysis/linkedin-api-access.md) — why the workflow this served was not built.
- [Source map](../sources.md) — disposition of every source.
