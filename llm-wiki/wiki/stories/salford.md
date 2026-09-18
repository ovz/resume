---
cluster: salford
aliases:
  - "Salford stories"
  - "Machine learning era stories"
  - "Data mining stories"
---

# Salford Systems, and the machine-learning era before it was fashionable — story cluster

> **Doc type:** reference
>
> Hub for the Salford Systems cluster: seventeen years of commercial machine learning, client delivery and specialist languages. Open this note's local graph to see the cluster as a sub-graph. Audience: the owner in a conversation about depth, data or long tenure; agents writing these stories.

## The through-line

**He kept walking into rooms where he was not the specialist, and earning the right to stay.** Salford Systems commercialized the work of the authors of the CART monograph — Breiman, Friedman, Olshen and Stone — so the building's expertise was statistical, and the owner's was software engineering. What he did with that, repeatedly, was learn enough of the other discipline to be useful in it and then defer to the people who owned it: debugging the numerical engines in Fortran alongside the statisticians who wrote them; learning SAS from scratch to prepare a national health survey for a pharmaceutical client; taking a Brazilian retailer's promotion optimization from data to a weekly business cycle.

The through-line for a listener is not "I did a lot of things". It is **depth acquired deliberately, in someone else's language, without pretending to be them** — and the long tenure that made it possible. The register is craft and long horizons, and the era's own vocabulary: *data mining*, not "ML/AI".

## Stories

| # | Working title | The claim | Draws on | Status |
|---|---|---|---|---|
| SF1 | [A mathematical paper, encoded in Fortran](salford/a-paper-encoded-in-fortran.md) | Debugged the classic decision-tree and boosting engines at their numerical core, in a language and a mathematics that were not his, alongside the statisticians who owned them — and found where his own mathematical boundary is | [2010-01-01 engine debugging](../../raw/brag/2010-01-01-spm-engine-debugging-cart-treenet-mars.md) · [2026-09-16 concurrency specialization](../../raw/brag/2026-09-16-concurrency-parallelism-specialization.md) § *Living with the Intel Fortran compiler* | **draft written** |
| SF2 | I learned SAS in a month for a pharmaceutical client | Learned SAS from scratch for a national mental-health survey commissioned by a pharma client, made a legacy SAS 8 codebase run again, documented the preparation method the client asked for — and out-built the in-house SAS expertise. The first pharmaceutical client of a career that later moved into regulated medical devices | [2010-05-01 NCS-R SAS data preparation](../../raw/brag/2010-05-01-ncs-r-sas-data-preparation-pharma-client.md) | **planned** — needs the owner's answer on the date conflict and on who the in-house expert was |
| SF3 | The weekly flyer of a Brazilian hypermarket chain | Four years of demand forecasting and promotion optimization feeding a retailer's weekly pricing-flyer cycle, a 1 TB warehouse underneath it, and the client relationship carried in his second language | [2013-01-01 Carrefour C4](../../raw/brag/2013-01-01-carrefour-c4-promotion-optimization-brazil.md) | **planned** |
| SF4 | Two vendors, two countries, one product | Running an outsourced Qt rewrite with a Polish vendor and a Ukrainian team at once — architecture authority, a merge-request-per-day cadence, and defending which developers to keep when the headcount case went to leadership | [2015-01-01 Mirabit staffing](../../raw/brag/2015-01-01-mirabit-outsourcing-vendor-staffing-management.md) | **planned** — blocked on the owner confirming the vendor split |

Cross-listed and told elsewhere: the [2004-2005 client-server daemon](concurrency.md) is Salford-era but belongs to the concurrency cluster, where its punchline lives; the [Minitab acquisition](stewardship/records-nobody-asked-for.md) is where the seventeen years pay off and belongs to stewardship.

## Reach for these when

- **"You were somewhere seventeen years — why?"** — SF1 first. Long tenure sounds like inertia until it sounds like depth.
- **Data, statistics or ML-adjacent roles where the question is how deep the mathematics goes** — SF1, told at exactly its honest depth: he read the mathematics well enough to debug it, and the statisticians owned it.
- **Health, pharma or regulated conversations** — SF2, which is the earliest clinical-data work in the record and the root of the medical-device move.
- **Client-facing delivery, or "have you worked directly with a customer?"** — SF3.
- **Managing distributed and outsourced teams** — SF4, then the bar-raising material in [leadership coverage](../resume/coverage/leadership.md).

## Know it — what stays with the owner

The people. Dan Steinberg (founder and president, and a listed reference), Mykhaylo "Mikhail/Misha" Golovnya (a listed reference, and the statistician lead on the pharma engagement), and Felipe Fernandez on the Brazilian work. The owner's account, 2026-09-16: "All my Salford colleagues were of high opinion of my abilities, appreciated my achievements and were pleasantly surprised what I did for Promo Optimization and pretty much everywhere else during 18 years of Salford tenure." **He has said these three may be named in stories** — but the telling still works better with roles than names, and credit goes to them by role, generously, before his own part. Never a claim about what someone said unless they said it in writing.

Also T1: Illia Polosukhin was a Salford colleague in this era, later a co-author of the transformer paper — a fact to volunteer only where it is relevant and never as borrowed credibility.

## Related

- [Story map](story-map.md) — every cluster.
- [Engineering and tooling coverage](../resume/coverage/engineering.md) § *SALF* and [data coverage](../resume/coverage/data.md) § *DATA* — the claims behind these stories, most of them still `absent` from the resume.
- [Voice and prominence](../workflows/voice-and-prominence.md) § *The registers* — the 2000-2017 register these are told in, and its trap: 2026 vocabulary for 2006 work.
