---
title: "Pushed back on moving SPM's C++ codebase to the Intel compiler before a release, and set a careful migration path instead"
date: "2012-12 to 2013-02"
thread: CONC
domains:
  - "Legacy code and platform migrations"
  - "Build, release, CI/CD"
  - "Leadership, management, hiring"
context: "Salford Systems — SPM 7.0 release and SPM 7.1 development, Windows and Linux toolchains"
sensitivity: private-repo
resume-worthy: maybe
storied:
  - "concurrency/the-gatekeeper"
---

# Pushed back on moving SPM's C++ codebase to the Intel compiler before a release, and set a careful migration path instead

## What I did — the owner's account (2026-09-24, verbatim)

> BTW despite fortran compiler bug saga Ken Bernstein and Illya polosukhin got excited to migrate SPM codebase to Intel Cpp compiler. I pushed back strongly Ken even called be "gatekeeper" and I didn't know the word and thought it is a compliment. My pushback was precisely because some blunder in C++ compiler would tank SPM hard and intel had no track record to help out. I also had an intuition that both Illya and Ken are very likely to leave the company soon to their bigger aspirations. It did happen, Ken went to Apple and Illya went to Google. Not too much committment from them, but at least they agreed to disagree. I don't recall we ever did any email communication about this. It is one of the vivid memory of mine, this conversation in the meeting.

## What the mailbox adds

The meeting was in **mid-December 2012**, and there is email around it — more than the owner remembered.

- **The proposal.** Ken Bernstein, newly joined and designated by the founder as technical leader for SPM speed-ups, wanted SPM on Intel's C++ toolchain and Intel TBB in the engine. Illia Polosukhin's case, sent the same day: SPM already used the Intel C++ compiler on the Linux side, Visual C++ could not be used there, so "any problem we will experience with Intel C++ we almost certainly have in Linux already".
- **The owner's written position, 2012-12-18**, replying to a colleague who had left the meeting upset: *"We don't want to get personal on this or anything else but everyone does want to do the best job possible. It is well known from the past experience that upgrading this code base even between versions of the same compiler might introduce problems. This is not a reason to get stuck with 5 year old technology but it calls for a careful approach to migration. In the short run, it is risky to upgrade technology on main code base until SPM 7.0 is out officially in production … We will run some experiments at that time. Let's have a separate discussion about utilizing TBB for engine code. Primarily we need to hear Mikhail understanding on this topic as he is in charge of scientifically intense core of the product."*
- **Then he enabled the experiment rather than blocking it.** Within two days he installed Intel Parallel Studio on the build server and an Intel release configuration was added to the build; over the holidays he helped build the Boost libraries with the Intel toolset. In January 2013 he kept the Intel configurations on the 7.1 line and out of the 7.0 release branch — "the highest priority is to get SPM 7.0 stable".
- **The founder's framing, and the owner's answer.** Dan Steinberg wrote that for speed-ups Ken was the technical leader and the team's job was to support him. The owner's reply named the problem as a way of working, not a person — that pressuring people and disregarding the expertise of other team members was not sustainable, while open technical discussion made the whole team more effective — and committed to "apply my considerable experience with our code base … to facilitate Ken's efforts. He picked quite an exciting topic to explore as his way to get started with the code base. That speaks of talent." Dan called the reply "well written and indeed good philosophy".

## Why it matters

A release-risk judgement made under social pressure, argued on the record's terms (compiler upgrades on this codebase had broken things before), and resolved by sequencing rather than by veto: ship 7.0 on the known toolchain, experiment on 7.1, and hear the statistician who owned the numerical core before putting a threading library into it. The owner facilitated the work he had argued to delay. The year that followed with Intel's Fortran compiler ([2013-12-01](2013-12-01-intel-fortran-14-rollback-premier-support-escalation.md)) is the reason the caution reads as foresight rather than conservatism.

## Skills demonstrated

Release-risk judgement; toolchain migration planning; separating a technical disagreement from a personal one in writing; deferring to the domain owner (the statistician) on the numerical core; enabling a colleague's experiment while protecting the release; managing upward to a founder.

## What was blocked, cut short, or wrong

- **Order of events — settled by the mailbox (owner's ruling, 2026-09-25: "Use the information grounded in emails as authoritative").** This meeting was December 2012; the Intel Fortran 14 regression came after it, December 2013 to 2015. The owner's memory that the push came *despite* the Fortran saga merged the two episodes, and he remembered no email about the debate, where several threads exist. Every telling uses the recorded order: the caution came first, and the Fortran year that followed showed why it was sound. The "past experience" his December 2012 email cites is not identified in the mail read; it is left unnamed rather than guessed.
- **"Gatekeeper"** is the owner's memory of the meeting and does not appear in the messages read. Keep it as his anecdote.
- **What eventually happened to Intel C++ on Windows** is not established here.

## Evidence

Mailbox threads, Salford Systems work account: "Meeting..." (2012-12-18), "Intel Parallel studio" (2012-12-19/20), "Speed matters for GPS" (2012-12-23), "Intel Product Purchase" and "Building Intel C++ executable on the build server" (2012-12-28/30), "7.1 Intel configurations" (2013-01-24), "SPM 7.1: unique_ptr not supported under MacOS X" (2013-02-12, where Illia writes "as Ken pointed out — we should just move to Intel Compiler on a Mac as well as in Linux").

## Evidence limitations

The move-on dates (Ken to Apple, Illia to Google) are the owner's account; Illia Polosukhin's later career is public (see [2012-06-01](2012-06-01-spm7-linux-port-tbb-evaluation.md)). The heated exchange is recorded here because the working relationship is the professional record ([sensitivity tiers](../../wiki/workflows/sensitivity-tiers.md) rule 8); it is never told outward, and no telling characterises the colleague.

## Related

- [2012-06-01 SPM 7 Linux port and TBB evaluation](2012-06-01-spm7-linux-port-tbb-evaluation.md) — the same people and the same TBB question; the evaluation that ended "doomed to fail".
- [2013-12-01 Intel Fortran 14 rollback and Premier Support escalation](2013-12-01-intel-fortran-14-rollback-premier-support-escalation.md) — the toolchain year that followed.
- [2026-09-16 concurrency and parallelism specialization](2026-09-16-concurrency-parallelism-specialization.md) — the capability record this episode belongs to.

## Record history

- 2026-09-24: created from the owner's TODO note of 2026-09-24 (verbatim above), grounded the same day in the Salford mailbox.
- 2026-09-24: graduated into story `concurrency/the-gatekeeper`; `storied` property added, body untouched.
- 2026-09-25: owner ruled the email-grounded record authoritative; *What was blocked* now states the settled order instead of an open question.
