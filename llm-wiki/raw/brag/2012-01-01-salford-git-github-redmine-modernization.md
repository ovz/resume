---
title: "Led Salford's move from SVN to Git — an access-controlled gitolite server, RedMine wiki runbooks, and a cut-over made against colleagues' advice to wait"
date: "2012-01 to 2013"
thread: SALF
domains:
  - "Build, release, CI/CD"
  - "Leadership, management, hiring"
context: "Salford Systems — source control and issue tracking"
sensitivity: private-repo
resume-worthy: maybe
---

# Led Salford's move from SVN to Git — an access-controlled gitolite server, RedMine wiki runbooks, and a cut-over made against colleagues' advice to wait

## What I did

Led the technical conversation around moving the team off **Visual SourceSafe (VSS)** and onto **Git/GitHub**, and onto **RedMine** for issue tracking — process leadership introducing modern SCM and issue-tracking practice to a company still on legacy tooling in 2012. This included hands-on git-workflow mentorship — explaining tag-based commit marking and `git reset` vs. `git commit` semantics, and by extension a line-ending policy (CRLF/LF) — delivered to **John Ries**, a senior colleague who had been with the company far longer than I had.

## The people behind it — the owner's account (2026-09-16)

**"It was more than a longer-tenured colleague."** The survey framed this as mentoring someone senior in tenure. The owner's account of the organizational situation is sharper:

- **Bernie Bernstein** had been in charge of SPM — in the owner's recollection roughly 2000–2005 — and the owner "learned a lot from him"; he was brilliant, and was retiring as he approached ninety. Bernie is a listed reference (Salford, June 2000 – January 2009).
- **Jeff Powers** was hired by the U.S. office as Bernie's **official successor**. The mailbox has him at Salford by 2009 (testing the `SPM_Protected` CI build, chasing link errors in the GUI engine library) and his domain account disabled by the owner in October 2014, after he left. In the owner's words: "in contrast Jeff was good for nothing job hopper. It was remarkable similarity to Wally character from Dilbert, just a more discrete slacker."
- **What the owner took from it:** "I learned a ton in that much younger age to stand up to rent seekers and hold my professional bar high." The tooling modernization is one place that showed: the case for Git and RedMine was made by the engineer doing the work, not by the designated successor.

**Telling it.** This is recorded in full because it is part of the professional record ([sensitivity tiers](../../wiki/workflows/sensitivity-tiers.md) rule 8). Outward, it follows [voice and prominence](../../wiki/workflows/voice-and-prominence.md) § *Humility, respect and trust*: the disagreement is told as what it was about in the work — who carried the modernization, and holding the bar when the designated owner did not — never as a verdict on a person, and never with a name. John Ries, the colleague the survey named as mentee, remains recorded; the owner did not correct that part.

## What the mailbox shows (read 2026-09-25) — and a correction

**The move off Visual SourceSafe was not this.** SourceSafe gave way to **SVN in 2010**, carried out by Jeff Powers: "We are no longer using VSS because it takes too long to download" (May 2010, to the Ukrainian team) and "VSS repositories transferred to SVN on Linux" (November 2010). What the owner led was the next step, **SVN to Git**, and the record of it is detailed:

- **January 2012 — gitolite first, for contractors.** To John Ries: *"I have an idea of a setup I want on marco. We will use it immediately for contractors and side projects and eventually we might migrate our main repositories too"* — gitolite for "virtual users determined by public keys and fine-grained access control", so that the offshore team's protected source tree could be cloned and branched "rather than validating changes after they are committed to the main branch". A week later he proposed moving the protected SPM build to gitolite too.
- **March–June 2012 — the external-libraries repository in Git, and encryption.** The shared `c:\lib` dependency tree moved to Git; he measured `gitcrypt`'s cost ("quite noticeably slows things down") and raised repository encryption with Illia Polosukhin.
- **October 2012 — the stated plan.** *"Our strategic plan is to migrate to git so we are not evolving our SVN repositories."*
- **1 November 2012 — the argument.** He proposed migrating "right away", because massive code changes and a release that involved branching and merging were coming. Illia objected that a git-svn repository would expose all the code to the Ukrainian team and proposed waiting for SPM 8; Ken Bernstein wanted to "start clean on git with SPM 8" and warned of a productivity hit for three colleagues who did not know Git. The owner: *"I'm not worried much about the learning curve. The concept of check in and check out is still there and the tooling is straightforward. For advanced tasks or, especially, problems git is much more effective."*
- **4–5 December 2012 — the cut-over.** *"At this point we start migration from svn to git. SVN for SPM700 will go read-only tomorrow morning."* He held the freeze until 10 p.m. for a colleague's last commit, ran a morning session to bring everyone up to speed, and pointed the team to RedMine wiki runbooks — how to configure a client machine, Git in general, and a Version Control article on branching and naming conventions whose aim was "to accommodate the real world requirements to our software development process and implement automation for as many routine tasks as possible". The access control did its job on day one: the offshore developer's push to an unconventional branch name was denied by the gitolite rules, and the owner's answer was the naming convention.
- **2013 — it stuck.** Merges of SPM 7.0 into `master`, submodules, RedMine issue numbers in commit discussions, and a gtest upgrade across repositories are routine in the 2013 mail; in June 2013 he asked whether to open a paid GitHub or Bitbucket account for a contractor.

## Why it matters

A migration led end to end by the engineer doing the work: an access-controlled server built first for contractors, a stated strategy, a timing argument won against two strong colleagues, a scheduled freeze, runbooks in the team wiki, and adoption that held. The access control is also what answered the strongest objection — that Git would expose the protected engine source to the offshore team. It predates and is distinct from the later, better-evidenced [2021 GitHub Enterprise migration](2021-08-15-github-enterprise-migration-monorepo.md) and the Minitab-era VSTS migration already on the resume — a third, earlier instance of the same "owns the migration off legacy SCM" pattern.

## Skills demonstrated

Source-control and issue-tracker migration advocacy; git workflow instruction (tags, reset vs. commit, line-ending policy); mentoring a colleague senior in tenure; driving a process-modernization decision without positional authority over the target platform.

## Evidence

A 2026-09-16 breadth-first Gmail survey identified this thread by keyword (GitHub, RedMine, VSS, git tags, git reset vs. commit, line-ending policy) and named John Ries as the mentee.

## Evidence limitations

**The survey's framing was wrong on two counts** and is corrected above: the legacy system replaced was SVN, not SourceSafe, and the main repository was a self-hosted gitolite server, not GitHub (GitHub or Bitbucket comes up only in 2013, for a contractor). The SourceSafe-to-SVN move of 2010 was Jeff Powers's work. That is a fact about the record, and it bears on the owner's account of the succession above: the modernization he led was the second step, not the first.

**The John Ries mentoring detail** (tags, reset versus commit, line endings) comes from the 2026-09-16 survey and was not re-read here; the 2012 threads show John as the colleague who helped set up gitolite on `marco` and asked practical questions at cut-over.

**Who approved the migration** is not stated; Dan Steinberg and David Tolliver were copied on the cut-over notice.

## Related

- [2021-08-15 GitHub Enterprise migration and monorepo](2021-08-15-github-enterprise-migration-monorepo.md) — the same pattern, a decade later, at Best Buy Health.

## Record history

- 2026-09-16: created, ingested from inbox note "gmail-brag-file-candidates.md" (candidate 3).
- 2026-09-16: added the owner's account of the succession — Bernie Bernstein retiring, Jeff Powers hired as official successor, and learning to stand up to rent seekers — with mailbox corroboration of Jeff's tenure (2009 to 2014).
- 2026-09-25: mailbox read in full — title, date and *Why it matters* corrected from "off Visual SourceSafe onto Git/GitHub" to the SVN-to-Git migration he led (gitolite, RedMine runbooks, the 2012-11 timing argument, the 2012-12-05 cut-over); recorded that the 2010 SourceSafe-to-SVN move was Jeff Powers's.
