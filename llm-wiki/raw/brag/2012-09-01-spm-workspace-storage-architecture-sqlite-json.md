---
title: "Owned the SQLite-vs-JSON storage-architecture decision for the SPM workspace feature"
date: "2012 to 2013"
thread: SALF
domains:
  - "Architecture and API design"
  - "Data engineering"
context: "Salford Systems — SPM workspace persistent-storage layer"
sensitivity: private-repo
resume-worthy: maybe
---

# Owned the SQLite-vs-JSON storage-architecture decision for the SPM workspace feature

## What I did

Owned the architectural decision for a new persistent **"SPM workspace"** feature — evaluating **SQLite** against a JSON-document approach for storing model metadata, data info, and prediction-success records — and articulated the trade-off explicitly: *"relational data model has its strong points, but they make sense when you need ACID..."*

## Why it matters

Small in scope on its own, but a clean, quotable example of deliberate storage-architecture reasoning (relational vs. document, weighed against ACID requirements) rather than default tool selection — corroborating evidence for the architecture/API-design domain from an era otherwise thin in the corpus.

## Skills demonstrated

Data-storage architecture decision-making; relational-vs-document trade-off reasoning grounded in ACID requirements; feature-level persistence design for a desktop analytics product.

## Evidence

A 2026-09-16 breadth-first Gmail survey identified this thread by keyword (SQLite, JSON storage, ACID, SPM workspace) and preserved the verbatim ACID-tradeoff quote.

## Evidence limitations

**Breadth-first candidate, not a deep-dive.** The survey preserved the framing and the quote but not which option was actually chosen, nor the eventual schema. Do not assume SQLite was the final choice without confirming it against the full thread.

**More detail could be mined from Gmail via the Gmail connector available to Claude** — specifically, which storage approach shipped and why. Deferred to a later session (this desktop or a Claude web chat), not performed here.

## Related

- [2012-01-01 Git/GitHub/RedMine modernization](2012-01-01-salford-git-github-redmine-modernization.md) — the same tooling-modernization era.

## Record history

- 2026-09-16: created, ingested from inbox note "gmail-brag-file-candidates.md" (candidate 5).
