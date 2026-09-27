---
title: "Learned SAS from scratch and built the data preparation for a pharmaceutical client's analysis of the National Comorbidity Survey Replication"
date: "2010-05 to 2010-09, follow-up 2013-01 (Gmail); the resume heads the project 2008-2009 — unresolved"
thread: DATA
domains:
  - "Data engineering"
  - "ML products and GUIs"
context: "Salford Systems — consulting engagement for Johnson & Johnson on the NCS-R dataset"
sensitivity: private-repo
resume-worthy: yes
---

# Learned SAS from scratch and built the data preparation for a pharmaceutical client's analysis of the National Comorbidity Survey Replication

## What I did

The public resume already carries this project, unnamed: a contract for "a major *National Health Survey* for a large *Pharmaceutical* company", where the owner learned **SAS** from scratch and built a system of **SAS macros** that warehoused the data, the client commended the work, and follow-on projects used the same dataset. This entry names what the resume does not, at T1.

- **The survey** was the **National Comorbidity Survey Replication (NCS-R)** — a nationally representative U.S. household survey of mental health, 2001–2003, 9,282 adults interviewed with DSM-IV diagnostic instruments, distributed by ICPSR as part of the Collaborative Psychiatric Epidemiology Surveys (study 20240).
- **The client** was **Johnson & Johnson** ("J+J" in the mail), with **Marsha Wilcox** as the client-side contact. At Salford, **Mikhail Golovnya** led the engagement and **John Ries** was the colleague on the SAS and Unix side.
- **The work, from the mailbox:** locating the correct ICPSR raw data (May 2010); discovering that "the entire J+J codebase on gracie was run in SAS 8 back in the day and was never attempted in" the current SAS, and getting it to run — including a SAS Institute support case for a segmentation violation in a DATA step (July 2010); working section by section through the survey's substance-use modules ("Substance appeared to be convoluted enough so I could only finish alcohol today"), with Mikhail taking each section into client meetings; a written data-preparation document the client had requested (May 2010); forking the data-prep code for a cluster analysis (June 2010); adding the DSM diagnosis variables the client asked for (September 2010); and in January 2013, extracting the transformation code for a requested set of variables and delivering it to the client, who thanked him the same day.

**The owner's own account (2026-09-16):** "National Comorbidity survey was with J&J. We can weave this in into stories that I got early exposed to Pharma companies and this helped with my medical device tenure and I also over achieved and outdone in-house SAS expert on building SAS stuff."

## Why it matters

- **Early exposure to pharmaceutical clients and clinical data.** A decade before regulated medical devices, the owner was working with psychiatric-epidemiology data for a pharma client: diagnostic variables, survey weights, and a client that needed its data-preparation method written down. That is the root the owner draws on for his medical-device tenure.
- **A software engineer out-built a SAS specialist in SAS.** The owner learned the language for the engagement and, in his account, delivered beyond the in-house SAS expertise — the same pattern as the Fortran engine work ([2010-01-01](2010-01-01-spm-engine-debugging-cart-treenet-mars.md)): stepping into a specialist's language and meeting the specialist's bar.
- **Legacy made runnable.** Getting a SAS 8 codebase to run on a later SAS is a migration problem, and the kind the owner kept solving.

## Skills demonstrated

SAS and SAS macro programming learned from scratch; survey-data preparation (ICPSR, DSM-IV diagnostic variables); legacy SAS migration; client-facing methodology documentation; working a vendor support case; collaborating with a statistician lead across client meetings.

## Evidence

- Gmail, owner's Salford account, snippets: "Raw data for NCS-R" (2010-05-04), "Formats for ncsr1p.sas7bdat" (2010-05-04), "Does just alcohol part of the substance makes immediate sense?" (2010-05-10/12), "NCS-R data preparation document for J+J" (2010-05-14), "Correps, 30 dims, Substance and Tobacco" (2010-05-25), "Third times the charm" (2010-06-07), "[SAS …] Segmentation Violation In Task [ DATASTEP ]" (2010-07-06), "NCS-R profile fixed" (2010-07-06), "DSM_XXX variables in NCS-R" (2010-09-08), "NCSR study SAS code" (2013-01-15/16).
- The primary resume's 2008-2009 project section; the archived long-form resume's *National Health Survey* bullet cited in [accomplishments by domain](../../wiki/concepts/accomplishments-by-domain.md).
- Public: NCS-R — <https://ghdx.healthdata.org/record/united-states-national-comorbidity-survey-replication-2001-2003>; ICPSR study 20240 — <https://www.icpsr.umich.edu/web/ICPSR/studies/20240/summary>; Harvard NCS — <https://www.hcp.med.harvard.edu/ncs/>; Kessler & Merikangas, *The NCS-R: background and aims* (2004) — <https://onlinelibrary.wiley.com/doi/10.1002/mpr.166>.

## Evidence limitations

- **The dates disagree, and the mailbox now says who ran the earlier phase (read 2026-09-25).** The earlier NCS-R data preparation, 2008 to January 2009, was **John Ries's**: on 15 January 2009 he wrote to a partner analyst "I've been completely out of the loop on NHANES (been focused on NCS-R)", set out Salford's missing-value conventions for the survey (impute skipped answers from prior ones; `.r` refused, `.d` don't know, `.n` not applicable; never overwrite a raw variable; label every new one) and offered his SAS macros. The owner's own record starts later: in May 2010 he asked John for "the document you've prepared back then" on data-preparation methodology, because the client had asked again, and in June 2010 he **forked the NCS-R data-prep code for the cluster analysis** "and made changes to minimize .n making a judgment wherever possible … keep .n usage to local (not section-wide)" — e.g. treating a respondent as a non-smoker when the screener shows no smoking issues and the section was skipped. His own SAS learning is visible from December 2009, reproducing a colleague's SAS pipeline for the Carrefour project in SQL Server ("Next time will do look up in SAS manual before asking").
- **This bears on the public resume.** Its *2008-2009* project section says "I learned SAS from scratch and created a system based on SAS macros." On the mail, the 2008–2009 phase and its macro system were John's; the owner's work is 2010 (and the January 2013 follow-up), and his SAS learning dates from late 2009. Either the resume's date and attribution need correcting, or the owner has a 2008–2009 role the mail does not show. **Owner to decide; the resume is untouched.**
- **"Outdid the in-house SAS expert" is the owner's account.** The mailbox shows the work, not a comparison; who the in-house expert was is not recorded, and nobody is named until the owner says.
- **The client's name is T1.** Outward it stays "a large pharmaceutical company", as the resume already has it; the survey itself is public and may be named.
- The January 2009 and May–June 2010 threads were read in full; the rest from snippets.

## Related

- [2013-01-01 Carrefour C4 promotion optimization](2013-01-01-carrefour-c4-promotion-optimization-brazil.md) — the next large client engagement, with its own parallel SAS build.
- [2010-01-01 SPM engine debugging](2010-01-01-spm-engine-debugging-cart-treenet-mars.md) — the same period's other specialist-language work.
- [2024-09-24 Current Health and Hospital at Home](2024-09-24-current-health-hospital-at-home-qms.md) — the regulated medical-device work this early exposure fed.

## Record history

- 2026-09-16: created from the owner's statement and a Gmail search that identified the survey, client, contacts and dates; public grounding for the NCS-R added.
- 2026-09-25: mailbox read — the 2008–2009 phase was John Ries's; the owner's own work is 2010 (a judged-imputation fork for the cluster analysis) and 2013; the resume's *2008-2009* section flagged for the owner.
