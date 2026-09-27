---
title: "Carrefour \"C4\" promotion-optimization system for Brazil — multi-year client-facing delivery"
date: "2009-12 to 2017"
thread: DATA
domains:
  - "Data engineering"
  - "ML products and GUIs"
context: "Salford Systems — client delivery for Carrefour's Brazilian retail operation"
sensitivity: private-repo
resume-worthy: yes
---

# Carrefour "C4" promotion-optimization system for Brazil — multi-year client-facing delivery

## What I did

Multi-year, client-facing delivery of a demand-forecasting and promotion-optimization system ("C4", `trfretail.com`) for **Carrefour's Brazilian retail operation**, producing weekly predictions that fed directly into the client's pricing-flyer ("**tabloide**") cycle. The system was backed by a roughly **1TB SQL Server database** plus a parallel **SAS** implementation, and I communicated directly with the client's business side — **Antonia Maria Xavier Yamada** and **Ricardo Ludovico** — in Portuguese-inflected English across at least four years, the longest-running single client thread found in the Gmail survey. I also owned data-pipeline reliability for the engagement, including backup and redundancy of the project's shared data store.

This corroborates and extends an existing, thinner record: [`accomplishments-by-domain.md`](../../wiki/concepts/accomplishments-by-domain.md) already carries, from the archived long-form resume, "Brazil retail promotion optimization (2013): full ETL to a 1 TB MS SQL warehouse; C#/WPF automation with CLR stored procedures and embedded Windows Workflow Foundation designer; data cleanup and product-cannibalization modelling." The Gmail survey adds the client-relationship dimension (named business contacts, the parallel SAS build, the demand-curve/tabloide mechanics, the multi-year sustained relationship, and pipeline-reliability ownership) that the archived resume's technical summary does not carry.

**Felipe Fernandez** (`interefe.com`; "Felipe Fernandez Martinez" on LinkedIn), a friend of Dan Steinberg's with long brick-and-mortar retail experience, including in France, was part of the Brazil collaboration: copied on the client's tabloide and perishables files in late 2012, on Dan's "Prescriptive Analytics — we did this for C4" (May 2014), and visiting a São Paulo prospect with Dan (June 2014). The owner names him as a main collaborator of that era (2026-09-16) and says his Salford colleagues were "pleasantly surprised what I did for Promo Optimization". **Illia Polosukhin** also worked on C4 (the owner: "I've just had a brief chat with Illia", August 2013), as did **John Ries**.

## Where it started — the mailbox, read 2026-09-25

The engagement is older than the entry's filename. **The owner's part begins in December 2009**, and it begins as data engineering:

- The C4 analysis pipeline existed first **in SAS, written by John Ries** (`carpool7a.sas`, `sector11v8a.sas`). The owner's job was to **re-create it in MS SQL Server**: stored procedures released in mid-December 2009, checked on small examples, then the full reference database — 72 million rows, too large for his laptop — rebuilt on a server Robert Harper set up, with a consistency-check procedure comparing the SQL Server result against SAS row by row. That comparison is where the defects surfaced and were sent back upstream: a day-of-year computed off by one (`yearday=Sales_Date-mdy(1,1,year)` needed `+ 1`), a competitor-normalised-price variable computed incorrectly in the SAS code, a price-fill anomaly, and the question of what numeric tolerance between SAS and SQL Server is acceptable ("Unit_Price: 5.6324 <> 5.6323 acceptable?").
- In the same weeks the engine release of November 2009 made TSLS models scoreable "in support of Carrefour work" ([2010-01-01](2010-01-01-spm-engine-debugging-cart-treenet-mars.md)).
- So the "parallel SAS implementation" in the survey's summary is the original, and the SQL Server warehouse is the owner's port of it, verified against it. The 1 TB warehouse and the C#/WPF automation of the archived resume grew from there.

## Why it matters

This is "shipped and kept running for a real paying client" evidence, sustained across at least four years — distinct from, and complementary to, the resume's brief technical mention of the same project. It demonstrates direct client-relationship ownership at the business-stakeholder level (not just engineering delivery), plus operational ownership of the data pipeline underneath a live, weekly-cadence business process.

## Skills demonstrated

Client-facing delivery in a second language/dialect (Portuguese-inflected English); demand-forecasting/promotion-optimization system design; large-scale (~1TB) SQL Server data warehousing; parallel implementation maintenance (SQL Server + SAS); data-pipeline reliability, backup and redundancy ownership; sustaining a client relationship across a multi-year engagement.

## Evidence

- The archived long-form resume's Brazil retail promotion optimization section (already cited in `accomplishments-by-domain.md`).
- A 2026-09-16 breadth-first Gmail survey (`oleg.zhylin@gmail.com`), which the survey itself called "the single richest vein in the mailbox," naming the client contacts, the SAS parallel build, the tabloide cycle, and the four-year span, reached via correspondence to `trfretail.com` and Salford addresses.

## Evidence limitations

**Start dated, end not.** The mailbox dates the owner's start to December 2009 (above; the December 2009 hosting thread read in full, the rest of that winter from snippets). The filename date (2013-01-01) is kept because coverage claims key on it. No revenue figures, contract terms, or a precise end date for the engagement are recorded; in April 2017 the owner still proposed building "promotion optimization system based on C4 data" on the cloud platform ([2015-01-01](2015-01-01-mirabit-outsourcing-vendor-staffing-management.md)). The demand-curve modelling approach is named generically ("demand curve") without algorithmic detail; that detail may exist in the fuller thread history or may only exist in the C#/WPF/SAS codebases themselves, which are not accessible from Gmail.

**The owner modelled, not only engineered the data.** His weekly reports show a C4 data-import job with tested ETL and preprocessing (June–July 2013), an SQL implementation of R² (August 2013), problems found with 6,000-tree C4 models in SPM 7.1 (August 2013), and his own "C4 Demand Curves analysis" and modelling on incomplete first-half data (November 2013). **Still unmined:** the correspondence with Antonia Maria Xavier Yamada and Ricardo Ludovico on the demand-curve methodology.

## Related

- [2014-01-01 CloudSML/CloudSPM/BigISLE big-data R&D](2014-01-01-cloudsml-cloudspm-bigisle-big-data-rd.md) — the company's contemporaneous move into cloud/distributed big data, a different axis of the same product-line era.
- [2016-09-01 hybrid container cluster under Rancher](2016-09-01-sparky-hybrid-container-cluster-rancher-aws.md) — the later platform work of the same data programme.

## Record history

- 2026-09-16: created, ingested from inbox note "gmail-brag-file-candidates.md" (candidate 6); merges new Gmail-survey detail into the existing archived-resume-sourced record in `accomplishments-by-domain.md`.
- 2026-09-16: added Felipe Fernandez, Illia Polosukhin and John Ries as collaborators from Gmail, and the owner's account of how colleagues regarded the promotion-optimization work.
- 2026-09-24: reciprocal *Related* link to an entry created the same day.
- 2026-09-25: mailbox read for the start — `date:` widened to 2009-12; *Where it started* added (the SAS-to-SQL Server port with its consistency check, and the defects it surfaced upstream); *Evidence limitations* rewritten.
