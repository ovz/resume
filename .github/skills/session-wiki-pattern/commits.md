---
name: session-wiki-commits
description: "Reference for session-wiki-pattern — how to write a commit file in session-wiki/commits/: the message, plus only what the diff cannot show."
---

# Commits: `session-wiki/commits/`

> Companion to [`SKILL.md`](SKILL.md). Load when preparing work for the owner to commit.

Agents do not commit. Work stops in the working tree and a human reviews it, so the **commit message is a session artifact, not a repository artifact** — it is written to `session-wiki/commits/`, never into a tracked file, a `COMMIT_EDITMSG`, or a staged commit template.

## Keep it lean

**The reviewer reads the diff. Do not restate it.**

A commit file exists to carry two things:

1. **The commit message**, ready to paste.
2. **Only what the diff cannot show** — and often that is nothing.

That is the whole format. No file-inventory table, no review order, no skim list, no verification recap, no essence paragraph rephrasing the message. Every one of those duplicates something the reviewer already sees, and a long proposal goes stale faster than a short one — which makes it worse than none, because a reviewer who trusts it is reading a description of code that has since changed.

Write the message, then stop. Add a note underneath only when it clears this bar:

- A **judgement call** that could reasonably have gone the other way, and what it would cost to reverse.
- Something **expensive or irreversible** — history size, a public artifact, a deleted original.
- A **superseded earlier commit file**, named, so it does not get landed by mistake.
- A **dependency or ordering constraint** between commit files.

"I verified it works" is not a note. Neither is "this file was renamed" — the diff says so.

## Shape

```markdown
# <Subject line — imperative mood, ≤ 70 characters>

```
<the verbatim message, ready to paste>
```

## Notes            <!-- omit entirely when there is nothing that clears the bar -->

- <judgement call, irreversible cost, supersession, or ordering constraint>
```

## One file per commit

Name them `NNN-<short-slug>.md`, numbered in the order prepared, continuing the number sequence the owner is already reviewing rather than restarting per scope. When one session produces several logically separate commits, write several files — **the grouping decision is part of what the owner is being asked to approve**, and it is one of the few things a diff genuinely cannot show.

Prefer **path-disjoint** commits so each can land independently. Where two genuinely touch the same file, say so in a note and state the order.

## The message body is version-controlled history

A commit message is subject to *The one-way reference rule* in [`SKILL.md`](SKILL.md), and more strictly than most files, because once accepted it becomes permanent history read by strangers with no access to this scope.

So the message carries **no scratch paths, no scope slug, no tracker item ID, no ticket ID, and no "as of this session" deixis.** It states what changed and why in terms that stand alone in a fresh clone.

**Wrap the message body at 72 characters** so `git log` reads correctly in a terminal. Notes outside the fenced block are read in an editor and need no hard wrapping.

## Handover

Record the handover in `tasks/assignment_tracker.md` — which commit files are ready, in what order, and anything the owner has to decide before landing them — and let the chat response point at the tracker rather than repeat it (SKILL.md § *The tracker*). Do not stage on the owner's behalf unless asked, and never commit. The owner decides whether to use the message verbatim, edit it, or split the commit.
