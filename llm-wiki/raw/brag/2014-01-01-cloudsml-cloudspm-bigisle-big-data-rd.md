---
title: "CloudSML/CloudSPM/BigISLE — driving Salford's cloud and distributed big-data R&D push, including a Gartner analyst briefing"
date: "2014 to 2017"
thread: DATA
domains:
  - "Big data and distributed ML"
  - "Cloud and distributed systems"
  - "Data engineering"
context: "Salford Systems — CloudSML, CloudSPM, BigISLE (Distributed ISLE)"
sensitivity: private-repo
resume-worthy: yes
---

# CloudSML/CloudSPM/BigISLE — driving Salford's cloud and distributed big-data R&D push, including a Gartner analyst briefing

## What I did

R&D push to move Salford's product line into cloud/distributed big-data territory: standing up a **multi-node Hadoop cluster**, integrating **Spark**, running a **Databricks** demo, and prepping technical material for a **Gartner Magic Quadrant** analyst briefing ("2015 Advance Analytics MQ Briefing") that positioned the company's big-data story to an external industry analyst.

This is the same programme already carried in `accomplishments-by-domain.md`'s *Big data and distributed ML* section, sourced from the archived resume: "Distributed ISLE (2014–2016): Hadoop/HDFS → PySpark (Scala experiments) → Databricks partnership → Dask; groundbreaking research on peta-scale datasets" and "Hive scoring utility (2015): hundreds of TreeNet models over billions of rows." The Gmail survey adds the specific product code names (CloudSML, CloudSPM, BigISLE, PySS) and the Gartner Magic Quadrant briefing, which the archived resume's technical summary does not mention.

## The owner's framing — a claim to fame in data engineering (2026-09-24, verbatim)

> must be made as my strong claim to fame in Data Engineering. Databricks must be the top contender of chops still relevant today. Snowflake pretty much obsoleted eye balling query graphs which I spent so much quality time in SQL server and got Relational Algebra ingrained in my mind. I love relational algebra, but unfortutely linear algebra doesn't land in my brain smoothly. Lucky 5% of world population making crazy money on GPT based AI.

Read as a positioning instruction: of the Salford data work, the distributed-ML programme is the part whose skills are still current — the Databricks partnership above all — and it should be told prominently. The SQL Server years are where relational algebra became second nature; a modern warehouse's optimiser has retired most of the hand work of reading query plans, not the reasoning behind it. The linear-algebra line is the owner's honest statement of where his mathematics stops, and belongs beside the [engine-debugging entry](2010-01-01-spm-engine-debugging-cart-treenet-mars.md), which says the same about the statistics.

### Follow-up, 2026-09-24 — what the archived resume and the mailbox add

- **The technology path, as the owner wrote it in 2017** ([archived resume](../archive/Oleg.Zhylin.resume.md) § *2014-2016. Distributed Machine Learning for ISLE*): brute-force distributed decision trees are notoriously hard, so the team chose Importance Sampled Learning Ensembles — grow rules on subsamples, weigh them with big-data operations. Hadoop/HDFS for the training data ("barebone Map/Reduce is counterproductive for any larger scale project"); PySpark, with a Jupyter demo; parts rewritten in Scala to test whether Spark's native language fixed the JVM's cost (it reproduced the same problems); a **Databricks partnership** after meeting the company at Strata in New York in October 2014, producing a Databricks notebook demonstrating the technology ("at that time Databricks cloud was not mature enough to meet all of our use cases"); then **Dask**, which "clicked together" — a first demo in under a week, and a long conversation with its author at PyCon 2016.
- **Cloud-ready SPM, 2015–2017** (same source): one of the principal architects and the product owner. Elastic by design around a distributed work-item queue (Redis), big-data storage and an OpenAPI-specified web API, with React/Redux/PostgreSQL for the web application; SeaweedFS for the many small operational files rather than forcing them into Hadoop; models exchanged through the **Portable Format for Analytics** with the team's own converters and interpreter after PMML and pickle proved unsuitable; data normalised to compressed TSV. Team up to seven. He funded his attention to it by staying the expert on the revenue-generating SPM 8.2 release in parallel.
- **Big-data scoring for a department-store client, 2015**: hundreds of TreeNet models applied to billions of rows inside Hive with `SELECT TRANSFORM` and the Tiny C Compiler, compiling each model's C translation on the fly on every node; in production for at least a year.
- **BigISLE went to external testers, June 2016.** Through the China partner, Huawei's big-data platform team and ZTE were lined up to test BigISLE; the owner had public installation documentation added, including how to hook the demo notebook to a real Spark cluster.
- **The platform it ran on** is its own entry: [2016-09-01 hybrid container cluster](2016-09-01-sparky-hybrid-container-cluster-rancher-aws.md).

## Why it matters

The Gartner MQ briefing detail is the standout addition: it is evidence of driving the company's response to the 2014-era "big data" market shift at the level of external industry positioning, not just internal engineering — genuine platform-strategy involvement, distinct from and complementary to the already-recorded infrastructure work.

## Skills demonstrated

Distributed big-data infrastructure (Hadoop/HDFS, Spark, Databricks); platform-strategy R&D; preparing technical material for external industry-analyst engagement (Gartner).

## Evidence

- `accomplishments-by-domain.md` § *Big data and distributed ML*, sourced from the archived long-form resume.
- A 2026-09-16 breadth-first Gmail survey, which surfaced the CloudSML/CloudSPM/BigISLE/PySS naming and the Gartner Magic Quadrant briefing preparation.

## Evidence limitations

**Breadth-first candidate, not a deep-dive.** The survey did not establish how CloudSML, CloudSPM and BigISLE relate to each other as product names (successive names for the same effort, or distinct components — unclear), nor what specifically was presented in the Gartner briefing or its outcome. No claim is made about how the briefing was received or whether it affected the company's MQ placement.

**Partly mined 2026-09-24.** The mailbox confirmed the BigISLE external testing (2016) and the CloudSML/TestSPM cloud work (2017); the naming relationship is now reasonably clear — BigISLE is the distributed ISLE engine, CloudSML and CloudSPM the cloud product line around it. Still not found: the Gartner briefing material or its outcome. The Databricks partnership and the technology sequence rest on the owner's own 2017 write-up, not on third-party confirmation.

## Related

- [2013-01-01 Carrefour C4 promotion optimization, Brazil](2013-01-01-carrefour-c4-promotion-optimization-brazil.md) — the client-delivery side of the same era, and the SQL Server years.
- [2016-09-01 hybrid container cluster under Rancher](2016-09-01-sparky-hybrid-container-cluster-rancher-aws.md) — the platform the programme ran on, across AWS and on-premises.

## Record history

- 2026-09-16: created, ingested from inbox note "gmail-brag-file-candidates.md" (candidate 7); merges new Gmail-survey detail (product naming, Gartner briefing) into the existing archived-resume-sourced record in `accomplishments-by-domain.md`.
- 2026-09-24: owner's positioning note added verbatim (a claim to fame in data engineering); follow-up from the archived resume and mailbox (Databricks partnership, Dask, Cloud-ready SPM architecture, Hive scoring, BigISLE external testing); `date:` widened to 2017 because the programme continued; *Data engineering* domain added.
