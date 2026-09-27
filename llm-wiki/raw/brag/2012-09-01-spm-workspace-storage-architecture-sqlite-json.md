---
title: "Argued for four years that SPM's models belonged in a document store and its data in a separate columnar one — a storage architecture that never shipped"
date: "2012-12 to 2017-02"
thread: SALF
domains:
  - "Architecture and API design"
  - "Data engineering"
context: "Salford Systems — SPM workspace persistent-storage layer"
sensitivity: private-repo
resume-worthy: maybe   # architecture advocacy, never shipped — see What the mailbox shows
---

# Argued for four years that SPM's models belonged in a document store and its data in a separate columnar one — a storage architecture that never shipped

## What I did

Owned the architectural decision for a new persistent **"SPM workspace"** feature — evaluating **SQLite** against a JSON-document approach for storing model metadata, data info, and prediction-success records — and articulated the trade-off explicitly: *"relational data model has its strong points, but they make sense when you need ACID..."*

> **Needs more evidence (owner, 2026-09-16).** Do not promote this entry until the thread is read in full. The owner recalls "something similar from CloudSPM era, but that's several years later, and Vlad Frolov was a solid guidance in this regard" — so the storage decision may belong to 2015–2017 Cloud-ready SPM work rather than, or as well as, a 2012 desktop feature, and the reasoning may have been shared with Vlad Frolov. Until the dates and the decision are established, treat the date, the ownership claim and the quote as provisional.

## What the mailbox shows (read 2026-09-25)

The full threads replace the survey's framing. There was **no single decision, and nothing shipped**; what the record holds is one consistent architectural position, argued across four years and four threads.

- **31 December 2012 – 1 January 2013, "SQLite".** Ken Bernstein floated SQLite for SPM's *temporary files* (transactional, adjustable in-memory storage, asynchronous I/O). The owner answered that the team was "looking for a data storage layer to build an SPM workspace" and leaned to NoSQL — "essentially we want our stuff in JSON" — while calling it "a topic for strategic discussions in the future". Illia Polosukhin split the question: JSON for metadata (data info, model information, prediction-success tables), something "blazingly fast" for the data itself. The owner's reply is the quote the survey kept, in full: *"Relational data model has it's strong points, but they make sense when you need ACID to some extent. In our case, I don't see much need in it. We can do just fine being eventually consistent. And we could benefit greatly for better out-of-box scalability."*
- **26 November 2013, "Thoughts on Model Stores and Management".** Dan Steinberg asked how SPM 8 should rethink the *grove* (SPM's model container) for large ensembles and model batteries. The owner: *"The features we need groves to have are those of a database. In my opinion noSQL document-oriented databases (MongoDb, CouchDb etc) are the best match. This way we are not constrained by a rigid relational format and still can index content however we like."* Illia objected that an external database must be installed on customers' machines, which many could not do, and proposed an embedded store or HDF5 with models serialised to JSON; Dan agreed with Illia.
- **12 October 2014, "Database research".** With a colleague's survey of columnar databases on the table and Dan's requirement — SPM took about forty minutes to cross-tabulate two integers on a 12 GB dataset that SQLite answered in forty seconds, and he was managing some 300 models a week by hand — the owner separated the problem: *"It is important to consider a database to replace groves and a database to store data separately. For the former document-based database sounds like the right choice … For columnar data storage, we might even get away with Redis. Or look into cutting-edge ideas by guys like Michael Stonebraker … in products like Vertica."* Vlad Frolov argued for an embedded engine to keep installation stable.
- **25 February 2017, "UnQLite".** Vlad proposed UnQLite — embedded, serverless, transactional, a JSON document store — as the grove replacement, which reconciled the owner's document model with Illia's and Vlad's no-install constraint. The owner explained the model to the team: documents addressable by hash in O(1), and *"putting all the relevant data into a single document. In contrast to SQL the data is denormalized. It is ok to duplicate information"* — a scoring document and a full-information document that reference each other.

The owner's recollection (2026-09-16) of "something similar from CloudSPM era … Vlad Frolov was a solid guidance" is the 2017 thread; the 2012 thread is the same position five years earlier.

## Why it matters

A consistent, early and well-reasoned storage position — document store for model metadata, separate columnar storage for data, consistency requirements stated rather than assumed, denormalisation accepted deliberately — held from 2012 to 2017 and refined by colleagues' deployment constraints rather than abandoned. It is corroborating evidence for architecture judgement and for the data-engineering credential of the 2014–2017 programme. It is **not** evidence of a shipped system.

## Skills demonstrated

Data-storage architecture decision-making; relational-vs-document trade-off reasoning grounded in ACID requirements; feature-level persistence design for a desktop analytics product.

## Evidence

A 2026-09-16 breadth-first Gmail survey identified this thread by keyword (SQLite, JSON storage, ACID, SPM workspace) and preserved the verbatim ACID-tradeoff quote.

## Evidence limitations

**Nothing shipped, as far as the mail shows.** No workspace feature, grove replacement or UnQLite integration appears after February 2017; the Minitab acquisition followed that year. Tell it as architecture advocacy, never as a delivered system.

**"Owned the decision" was the survey's framing and is withdrawn.** The owner argued a position; the founder sided with Illia's installation concern in 2013, and no decision is recorded. SQLite was never the owner's proposal — it was Ken's, for temporary files.

**The filename date (2012-09-01) predates the first thread (2012-12-31)**; it is kept because coverage claims key on it.

## Related

- [2012-01-01 Git/GitHub/RedMine modernization](2012-01-01-salford-git-github-redmine-modernization.md) — the same tooling-modernization era.

## Record history

- 2026-09-16: created, ingested from inbox note "gmail-brag-file-candidates.md" (candidate 5).
- 2026-09-16: marked **needs more evidence** at the owner's request; recorded his recollection that a similar decision belongs to the CloudSPM era with Vlad Frolov's guidance.
- 2026-09-25: four full mailbox threads read (2012-12, 2013-11, 2014-10, 2017-02); title, date and *Why it matters* corrected from "owned the decision" to a four-year position that never shipped; the needs-more-evidence note is resolved by *What the mailbox shows*.
