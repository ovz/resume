---
title: "Owned SPM's licence protection from the protected build track of 2009 to a CodeMeter licensing programme he planned in 2015 and ran through 2017, across Windows, Linux and macOS"
date: "2009 to 2017"
thread: SALF
domains:
  - "Security, cryptography, licensing"
context: "Salford Systems — SPM_protected build track, Wibu-Systems CodeMeter"
sensitivity: private-repo
resume-worthy: maybe
---

# Owned SPM's licence protection from the protected build track of 2009 to a CodeMeter licensing programme he planned in 2015 and ran through 2017, across Windows, Linux and macOS

## What I did

Owned the license-protected build track (`SPM_protected`) from at least 2009 onward and corresponded directly with **Wibu-Systems** — the licensing/DRM vendor — on **CodeMeter** integration in 2014.

This sits alongside an existing, broader claim in `accomplishments-by-domain.md` § *Security, cryptography, licensing*, sourced from the primary and archived resumes: "License management ownership: in-house managers, CrypKey, then Wibu Codemeter selected after trials of FlexLM/RLM/Arxan/Sentinel; Debug/Release DLL protection scheme; Nalpeiron at Minitab, packaged for company-wide reuse." That claim describes the vendor-selection decision; this entry is the corroborating evidence that ownership of the resulting build track was sustained for years afterward, not a one-time integration.

## What the mailbox shows, 2015–2017 (read 2026-09-25)

The survey saw "Wibu correspondence in 2014". The full record is a licensing programme the owner planned, sold internally and ran for two years.

- **April 2015 — the plan.** To Dan Steinberg, "Allocating Wibu help to implement licensing": use the vendor as a contractor to migrate to CodeMeter faster, in two stages. **Stage 1, Salford's own:** agree the licensing structure across development, sales and marketing; command-line licence generation (one to two days); reading and enforcing the licence in SPM (up to a week) — "the couple of weeks we discussed I need to spend". **Stage 2, with the vendor:** the vendor's web licence portal (customer and employee areas, manual or automatic generation), which "replaces and hugely extends" the in-house licence generator, with the vendor advising on licence structure "w/o learning how to program SPM". Dan: "Sounds good."
- **May 2015 — the hard cases.** Protected DLLs that crashed, an encrypted executable that could not load a DLL, and an encrypted **debug** DLL that could not be debugged — "I just want client application to be debuggable" — which the vendor's engineer escalated to Germany as matching another customer's case. (This is the resume's "Debug/Release DLL protection scheme".) Asked by Dan in the same week for a protected 8.1 build for outside contractors, he answered: "I would prefer to make it Wibu Codemeter protected. Crypkey is doable too."
- **September 2016 — macOS and Linux.** Protecting the new Qt application on macOS with the vendor's `AxProtector` tool: dynamic-library load paths in the app bundle, whether the tool handles `.app` bundles at all, and a refusal to run the protection step with `sudo` on the build server — *"In production AxProtectorMacX is supposed to run on a build server. I strongly prefer _not_ to run a build server script from a user account with sudo rights."* He reviewed binary differences to explain an "empty encryption" effect, filed documentation errata with the vendor, and ran a CodeMeter licence server on the corporate network for the team's own machines.
- **February–April 2017 — in production.** CodeMeter-protected SPM 8 builds shipped to enterprise customers in banking and payments and to a Chinese distributor; he approved the distributor's virtual-machine licence containers, reviewed its customer documentation, diagnosed customer licence failures from the vendor's diagnostic dumps (a VM running a bare-metal-only container; a duplicated container), worked Linux licence discovery with the vendor ("Is it your general observation that auto-discovery doesn't work reliably on Linux?"), kept a separate minimally protected kill-date branch for one customer, and negotiated a new batch of activation licences after a customer's request for thirty individual machine licences exhausted the supply. The draft SPM 9.0 memo of March 2017 lists "CodeMeter based license management implementation" among its big items, beside the grove database.

## People

**The owner names Felipe as the main person he collaborated with** (2026-09-16): "We need Felippe (I think Hernandez, but I am not sure) as main person I collaborated with. Felipe is a good friend of Dan Steinberg and he has extensive experience in brick and mortar stores. He worked in France and during our collaboration in Brazil for Carrefour."

**What the mailbox says, which does not yet line up with this entry.** Gmail has **Felipe Fernandez** (`interefe.com`; his LinkedIn profile reads "Felipe Fernandez Martinez", and the owner receives his posts, so they are probably connected). He appears copied on the Carrefour promotion-optimization files in late 2012, on Dan Steinberg's "Prescriptive Analytics — we did this for C4" (2014), visiting a São Paulo prospect with Dan (2014), and on retail-analytics threads to 2015 — **all on the Carrefour and Brazilian-retail side, none on licensing.** So the surname is most likely *Fernandez*, not *Hernandez*, and his collaboration is best evidenced on [the Carrefour entry](2013-01-01-carrefour-c4-promotion-optimization-brazil.md). Whether he also had a part in the protected-build and licensing work is **not established**; recorded here as the owner said it, pending his confirmation.

**Also on this track:** **Jeff Powers** was testing the CruiseControl.NET build of `SPM_Protected` in September 2009 ("I haven't tested the CCNET with SPM_Protected, I will give it a go now") — see [2012-01-01](2012-01-01-salford-git-github-redmine-modernization.md) for who he was.

**How the owner's Salford colleagues saw him.** In the owner's words: "All my Salford colleagues were of high opinion of my abilities, appreciated my achievements and were pleasantly surprised what I did for Promo Optimization and pretty much everywhere else during 18 years of Salford tenure." He names Dan Steinberg, Felipe and Mikhail (Mykhaylo) Golovnya — Dan and Mikhail are both listed references. This is for stories to mention casually, never on the resume and never as a quotation of what someone said.

## Why it matters

Minor on its own, but useful corroboration for **sustained** ownership of commercial software-protection/licensing infrastructure — not just the open builds, and not just the point-in-time vendor-selection decision the existing claim already records.

## Skills demonstrated

Commercial software license-protection integration (Wibu-Systems CodeMeter); sustained ownership of a parallel protected build track over multiple years; direct vendor correspondence.

## Evidence

- `accomplishments-by-domain.md` § *Security, cryptography, licensing* (the vendor-selection claim, from the primary/archived resumes).
- A 2026-09-16 breadth-first Gmail survey, which named the `SPM_protected` build track (also referenced in the [2009 release-engineering entry](2009-06-01-spm-release-engineering-japanese-localization.md)) and dated direct Wibu-Systems correspondence to 2014.

## Evidence limitations

**The 2014 correspondence is an evaluation.** His weekly reports show a "Wibu evaluation" and work with the vendor's representatives from June to September 2014, after studying RLM in April 2013 — the trial phase behind the resume's vendor-selection list; the individual 2014 threads were not read. The 2016–2017 threads were read from subjects and snippets, the April 2015 plan in full. **Customer names are T1** (banks, a payments network, a Chinese internet company, the distributor) and never go outward; outward this is "enterprise customers in financial services and a distributor in China".

**The vendor-selection decision** (trials of FlexLM, RLM, Arxan, Sentinel) is resume-sourced and was not re-found in the mail read here.

## Related

- [2009-06-01 SPM release engineering and Japanese localization](2009-06-01-spm-release-engineering-japanese-localization.md) — names the same `SPM_protected` build track as one of three parallel tracks.

## Record history

- 2026-09-16: created, ingested from inbox note "gmail-brag-file-candidates.md" (candidate 10); merges new Gmail-survey detail into the existing primary/archived-resume-sourced claim in `accomplishments-by-domain.md`.
- 2026-09-16: added *People* — the owner names Felipe as main collaborator; Gmail places Felipe Fernandez on Carrefour work rather than licensing, so the link is recorded as unconfirmed. Added Jeff Powers's 2009 `SPM_Protected` CI testing and the owner's account of how Salford colleagues regarded him.
- 2026-09-25: mailbox read for 2015–2017 — title and date widened from "2009 to 2014" to the CodeMeter programme he planned (April 2015) and ran to 2017; *What the mailbox shows* added; *Evidence limitations* rewritten.
