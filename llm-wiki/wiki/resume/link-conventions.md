# Link Conventions — Wayback Machine snapshots as the default hyperlink

> **Doc type:** reference
>
> Rules for every hyperlink in the primary resume and in any other outward-facing document built from `markdown/`. Audience: the owner and any agent editing resume sources. Loaded together with [primary-resume.md](primary-resume.md).

## Why archived links, not live links

Companies rebrand, restructure their sites, get acquired, and delete product pages. A live URL in a resume that has been in use for years silently rots, and a rotted link reads as carelessness. Worse, a live page can be *edited* after the resume cites it, so the reader no longer sees what the author saw.

The resume therefore links to the **Internet Archive Wayback Machine** (`web.archive.org`). This gives the reader three things a live link cannot:

1. **Drill-down that works.** The reader can open the link and see the product, company, paper, or tool exactly as it was described.
2. **A timestamp.** The snapshot date is in the URL and in the Wayback banner, so the reader knows *when* this was true.
3. **Reputational attributes of a bona fide historical snapshot.** The archive is a neutral third party; the snapshot is evidence that the page existed in that form at that time, not an assertion the author can retouch later.

The resume says this to the reader explicitly in its *Side Note: Hyperlinks lead to the Internet Archive Wayback Machine* section. Keep that note; it is what turns an unusual link style into a deliberate, trust-building choice.

## URL forms

| Form | Example | When to use |
|---|---|---|
| **Pinned snapshot (preferred)** | `https://web.archive.org/web/20240407110931/https://www.lively.com/medical-alerts/lively-mobile2` | Any new link. The 14-digit `YYYYMMDDhhmmss` stamp fixes the exact capture and is what gives the reader the timestamp guarantee. |
| **Latest snapshot (fallback)** | `https://web.archive.org/web/https://www.salford-systems.com` | Legacy links in the file and cases where the specific capture date does not matter (a stable organization home page). Resolves to the most recent capture, so it can drift — acceptable for identity, weak for evidence. |
| **Live URL (exception)** | `https://www.linkedin.com/in/olegzhylin/`, `mailto:` | Only for the owner's own contact surfaces, and for pages whose live form *is* the point (a profile the reader should visit live). |

Prefer `https://web.archive.org/...`; some legacy entries use `http://web.archive.org/...` — both resolve, but new entries use `https`.

## How to add or replace a link

1. Find the best page that describes the thing as the owner experienced it — a product page from the relevant year, the paper, the tool's home page — not a marketing page from today.
2. Look the URL up on the Wayback Machine. Choose a capture **close to the time the described work happened** (e.g. a 2003 capture for the CART 5.0 release, a 2024 capture for Lively Mobile 2). If the only captures are recent, that is still better than live.
3. If no capture exists, request one (Wayback "Save Page Now") and then pin the resulting timestamp. Do not leave a live URL because archiving felt like extra work.
4. Add a **reference-style definition** at the bottom of the file: `[key]: <archived-url> "<human title>"`. The title attribute is the reader's tooltip and the wiki's label; make it the proper name (product, company, person, paper), not the URL.
5. Use `[visible text][key]` in the body. Reuse an existing key when the target is the same; do not create near-duplicate keys.
6. Verify the link renders and resolves (open it once). Record nothing in the wiki about the verification beyond fixing what is broken — the resume is the artifact.

## Key naming

- Lowercase snake_case; short, mnemonic: `spm82`, `spm70`, `cart_4_0`, `r4` (Lively Mobile+), `r5` (Lively Mobile 2), `bbh`, `greatcall`, `salford`, `minitab`, `iit`, `nure_eng`.
- People: surname or first name (`jerry`, `leo`, `olshen`, `chuck`, `dsteinberg`, `oliphant`, `mrocklin`).
- Tools and concepts: the plain name (`codemeter`, `dask`, `tcc`, `cicd`, `data_wrangling`).
- One definition per key; keys are shared across all `markdown/` documents, so a key means the same thing everywhere.

## Observed inconsistencies in the primary resume (as of the 2026-09 review)

Listed so an edit pass can normalize them; not fixed by the wiki itself.

- Live (unarchived) targets: `leo`, `olshen`, `chuck`, `databricks`, `dask`, `seaweedfs`, `mrocklin`. Decide per link: archive them, or accept as "identity" exceptions.
- `[r5]` title reads "Lively Mobile+" but the target is the Lively Mobile 2 page; title should read "Lively Mobile 2".
- A bare live URL to `shop.lively.com/collections/shop-all-products` appears inline in *My Story*; convert to a pinned Wayback reference link.
- Two body references have a missing opening bracket (`Best Buy Health][bbh]`, `Emergency Response device][r4]`), so they render as literal text instead of links.
- Mixed `http://` / `https://` scheme on `web.archive.org` definitions; harmless, normalize opportunistically.

## Related

- [Primary resume](primary-resume.md) — where the *Side Note* must sit and how link keys are used in each section.
- [Update workflow](update-workflow.md) — link verification is a step of every edit pass.
