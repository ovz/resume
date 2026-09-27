---
cluster: salford
fits: [data, architecture, principal, leadership, integration]
status: draft
runtime: "2 min"
---

# My best peer collaboration was with the engineer who talked me into repaving our whole cluster

## Why I still care

I had working systems I was responsible for, and he wanted to take the whole cluster down and rebuild it his way. He was right, and the thing I am proudest of is that I let myself be convinced. We were strong in different halves of the problem, and for once neither of us had to pretend to know the other half.

**Cue:** my email to him in February 2017, when the cloud provider's own services started to pull us in — *"Is your plan to stick to 'vanilla' rancher and ignore platform specifics or push ECS/EFS solution to completion?"*

## Register

**2000-2017, Salford Systems**, near the end. Craft and long horizons; the era's words — cluster, containers, big data. The colleague is "my co-architect" in every spoken line. Lines lifted from the owner's note of 2026-09-24 per [spoken drafts](../../workflows/spoken-drafts.md).

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | When asked about the best peer collaboration |
| 1 | Hook | My co-architect talked me into repaving our entire in-house big-data cluster into containers |
| 2 | Stakes | A small company whose whole engineering ran on that cluster, and that needed to show partners it could build in the cloud |
| 3 | Complication | Strong in different halves; cloud new to both; a repave risks everyone's daily work |
| 4 | Move | One rule — no workloads on bare hardware; identity and isolation first; then into AWS without lock-in |
| 5 | Punchline | One platform across our machines and AWS, data and workers in both, and the cloud product building models on big data |
| 6 | Handover | What makes a peer collaboration work for you? |

## Narrative — rehearse verbatim

**0 · Offer**
> If you ask me about the best peer collaboration I have had, there's one from 2016.

**1 · Hook**
> My co-architect talked me into repaving our entire in-house big-data cluster — every machine — and running everything in containers.
⟨breathe⟩

**2 · Stakes**
> We were a small company, and that cluster ran our engineering: the builds, the regression tests, source control, chat, identity. And we needed to show partners that we could develop and run new software fully in the cloud.

**3 · Complication**
> We were both strong in our areas. I was the expert on the company's technology; he was Python and Linux. The cloud — mainly AWS — was new for all of us. And repaving a cluster that everybody works on every day is not a small thing to agree to.
⟨breathe⟩

**4 · Move**
> So we agreed on one rule: no workloads on bare hardware, everything in containers, under a container manager. Identity came first, on its own server, and outside contractors got in through an isolated VPN, not through the office network.
> Then, when we moved into AWS, the provider's own services started to pull us in. I asked him whether we were staying with the vanilla container platform or going all in on theirs. We stayed portable.

**5 · Punchline**
> We ended up with one container platform across our own machines and AWS, with the data and the model-building workers running in both places. And our cloud product demonstrated model building on big data on it.
⟨breathe⟩

**6 · Handover**
> What makes a peer collaboration work for you? For me it was that neither of us had to pretend to know the other half.

## If they follow up

- **"Did it go smoothly?"** → No. Our identity server was unstable for about three months, and once an outside IT contractor rebooted every server at the same time. The job then was to keep people working — fall back to the old source-control server, and make sure everyone knew exactly what to do — while he fixed it.
- **"Why did the company want to be in the cloud?"** → I put it to the team as a business need, not an engineering fashion: we had to show potential partners that we developed and ran new software in the cloud. My co-architect asked the right question — why move development at all — and that is the answer we agreed on.
- **"How does this connect to data engineering?"** → It was the platform under our distributed machine-learning programme: Hadoop, then Spark, a partnership with Databricks after we met them at Strata in 2014, and then Dask, which finally clicked. That programme is the data-engineering work of mine that is still most current.
- **"What happened to it?"** → The company was acquired in 2017, and its own cloud roadmap ended there. The Ukrainian team went on as their own company.

## Proof

The archived long-form resume (the cluster, RancherOS and Rancher, FreeIPA, GitLab, the isolated VPN, "no workloads on barebone hardware"); the Salford mailbox of 2016–2017 (the cluster's services, the cloud decision, the February 2017 question quoted above, the acquirer's demonstration).

## Know it — what stays with me

T1: the co-architect is **Vladyslav (Vlad) Frolov**, later at NEAR; Illia Polosukhin was the earlier Python and Linux partner. The cluster was called Sparky; it ran GitLab, FreeIPA and Mattermost, and the TestSPM regression cluster beside it. TestSPM ran on AWS for the acquirer's visit in February 2017; a distributed TreeNet MPI server was deployed to it by pipeline in March 2017. The Ukrainian team became Mirabit in March 2017. "Successfully demonstrated model building on big data" is my characterisation; the mail shows demonstrations and progress reports, not a benchmark.

## Sources

- [2016-09-01 Hybrid container cluster under Rancher](../../../raw/brag/2016-09-01-sparky-hybrid-container-cluster-rancher-aws.md)
- Cited, not graduated: [2014-01-01 CloudSML / CloudSPM / BigISLE](../../../raw/brag/2014-01-01-cloudsml-cloudspm-bigisle-big-data-rd.md)

## Related stories

- [A mathematical paper, encoded in Fortran](a-paper-encoded-in-fortran.md) — the engines the cluster ran.
- [I kept records nobody asked me for](../stewardship/records-nobody-asked-for.md) — what happened when the company was acquired.
