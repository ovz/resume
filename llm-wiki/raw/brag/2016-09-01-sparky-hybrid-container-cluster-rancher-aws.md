---
title: "Repaved Salford's in-house big-data cluster into containers under Rancher, and ran CloudSPM's model building across AWS and on-premises"
date: "2016 to 2017-03"
thread: DATA
domains:
  - "Big data and distributed ML"
  - "Cloud and distributed systems"
  - "Build, release, CI/CD"
  - "Security, cryptography, licensing"
context: "Salford Systems — the in-house computational cluster, TestSPM, CloudSML/CloudSPM, distributed TreeNet; co-architect Vladyslav (Vlad) Frolov"
sensitivity: private-repo
resume-worthy: yes
storied:
  - "salford/the-best-peer-collaboration"
---

# Repaved Salford's in-house big-data cluster into containers under Rancher, and ran CloudSPM's model building across AWS and on-premises

## What I did — the owner's account (2026-09-24, verbatim)

> My best peer to peer collaboration was on ClaudeSPM . Vlad Frolov and I were both strong in our areas, I am more on SME for Salford Systems technology and he and Illya Polosukhin were Python, Linux etc. Cloud (mainly AWS) was new for us all . memorable episode is when Vlad convinced me to repave the entire in-house big data cluster into Rancher and host everything in containers. It was an involved initiative, but as a result we ran hybrid AWS/onprem container based cloud and CloudSPM successfully demonstrated model building on big data. Both data and workers ran in AWS and on prem

("ClaudeSPM" is CloudSPM, the product's cloud edition.)

## What the archived resume and the mailbox add

- **The cluster, as the owner wrote it up in 2017** ([archived resume](../archive/Oleg.Zhylin.resume.md) § *2016-2017. In-house Computational Cluster project*): an IT contractor installed the hardware; the requirement was to let outside contractors reach the cluster while enforcing access control to the corporate network, and let corporate users use it transparently — solved with an isolated VPN access point on a dedicated Cisco appliance. RancherOS on the bare machines, Rancher on top, and "as a matter of principle, we ran no workloads on barebone hardware. Everything ran in containers." Containerised services: FreeIPA for identity, because authenticating through the corporate Active Directory was "not prudent from security standpoint"; GitLab for version control, issue tracking and CI/CD.
- **It ran the company's engineering.** By September 2016 the cluster ("Sparky") hosted Mattermost, GitLab and FreeIPA; one FreeIPA login covered GitLab, VPN and chat; the TestSPM cluster of Hadoop-era machines ran the regression queue. The clusters were deliberately separated from the internal office network.
- **The move to the cloud was a business decision he carried.** January 2017: the founder wanted TestSPM in the cloud; the owner relayed "a strong urge to get the entire development environment to Public Cloud", and when Vlad asked for the rationale, proposed the answer to the founder himself — *"This is a business need. We need to show potential partners that we develop and run new software fully in the Cloud."* February 2017, on Vlad's AWS "vendoring" problems: *"Is your plan to stick to 'vanilla' rancher and ignore platform specifics or push ECS/EFS solution to completion?"* — the choice that kept the platform portable between AWS and the in-house machines.
- **What it carried.** TestSPM on AWS, demonstrated to the acquirer's team in February 2017; CloudSML progress reported to the founder with screenshots; a distributed TreeNet MPI server built by GitLab pipeline and deployed to a Rancher stack in March 2017, with the owner pushing to get the lead statistician "up and running on Sparky sooner rather than later".

## Why it matters

This is the most complete piece of platform engineering in the Salford record: identity, network isolation, CI/CD and chat on one containerised cluster the team owned, then extended into a public cloud without being locked to it, while the data and the model-building workers ran in both places. It is also the owner's own answer to "best peer collaboration" — two engineers strong in different halves of the problem, one persuading the other into a bigger change than he would have chosen, and both better for it.

## Skills demonstrated

Container platform design (RancherOS, Rancher); identity management (FreeIPA) and network isolation for contractor access; self-hosted CI/CD (GitLab); hybrid cloud across AWS and on-premises hardware without vendor lock-in; carrying a business rationale to an engineering team; peer collaboration across a skill split.

## What was blocked, cut short, or wrong

- **The cluster had real outages.** FreeIPA instability ran for about three months in 2016 and needed reinitialising; an outside IT contractor's maintenance once rebooted every server at once. The owner's handling in the mail is to keep people working (fall back to the older Git server) and ask for clear instructions, not to assign blame.
- **The acquisition overtook it.** Minitab's arrival in 2017 ended Salford's independent cloud roadmap; the Ukrainian team moved to its own company, Mirabit, in March 2017.

## Evidence

The archived long-form resume (committed). Mailbox threads, Salford Systems work account, 2016-06 to 2017-03, including "BigISLE test in Huawei", "Mattermost", "Network down UPDATE II", "Centos6-VM", "Account Blocked on GitLab", "Test SPM upgrades", "TestSPM on AWS", "TestSPM on AWS demo for minitab", "CloudSML progress with screenshots", "TN_MPI pipeline" and "Script-robot and Unlock email accounts" (which names GitLab running on Rancher).

## Evidence limitations

"Vlad convinced me" is the owner's account; the mail shows Vlad building and running the platform and the owner setting direction, not the conversation in which the repave was agreed. "Successfully demonstrated model building on big data" is the owner's characterisation; the mail shows the demonstrations and progress reports, not a benchmark.

## Related

- [2014-01-01 CloudSML / CloudSPM / BigISLE](2014-01-01-cloudsml-cloudspm-bigisle-big-data-rd.md) — the distributed-ML programme this platform served.
- [2016-11-01 Salford–Minitab acquisition technical diligence](2016-11-01-salford-minitab-acquisition-technical-diligence.md) — the acquirer's visit that asked to see this infrastructure.
- [2015-01-01 outsourcing vendor staffing](2015-01-01-mirabit-outsourcing-vendor-staffing-management.md) — the team, and the Mirabit name.

## Record history

- 2026-09-24: created from the owner's TODO note of 2026-09-24 (verbatim above), grounded the same day in the archived resume and the Salford mailbox.
- 2026-09-24: graduated into story `salford/the-best-peer-collaboration`; `storied` property added, body untouched.
