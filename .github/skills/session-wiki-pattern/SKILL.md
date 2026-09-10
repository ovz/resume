---
name: session-wiki-pattern
description: "USE WHEN planning or maintaining a long, multi-step assignment that must survive context compaction, host-process crash, or session loss — and you want every piece of knowledge the session produces preserved durably so the work can RESTART in a fresh, lean chat from a resume token. A session-wiki is an ephemeral, scope-scoped working wiki in the host repo's gitignored scratch area, structured raw capture → synthesis → index, with a tracker that doubles as the resume token. It is self-contained and needs nothing but a scratch directory. DO NOT USE for single-shot tasks (a simple tracker suffices), or for authoring the host repo's durable committed knowledge, which outlives the session and follows that repo's own conventions."
---

# Session-Wiki Pattern

A **session-wiki** is an ephemeral, scope-scoped working wiki inside a *session sub-directory* under the host repo's gitignored scratch area (e.g. `__untracked_stuff/<scope>/` — crash-safe and machine-transferable). It gives a session the three-layer shape that makes knowledge accumulate instead of scroll past:

> **raw capture → synthesis → index**, with a tracker alongside that doubles as the resume token.

Raw holds what was actually observed, immutable once written. Synthesis distills it into findings that cite raw. An index makes both navigable without reading everything. The point is that (a) all knowledge produced during a long multi-step session is preserved on disk, not just in chat history or volatile memory, and (b) the session can RESTART in a fresh, lean chat from the tracker without losing anything.

## Where the rest of this skill lives

This file is the core: the doctrine and the structure. Four companions hold material that only some scopes need. Load one when its trigger fires; do not load it speculatively.

| File | Load when |
|---|---|
| [`commits.md`](commits.md) | Preparing work for the owner to commit — the commit-file format and review-order guidance |
| [`scaling-up.md`](scaling-up.md) | The scope **runs code** that must outlive it, the tracker needs rotating, or work is passing to a successor scope |
| [`naming-and-archiving.md`](naming-and-archiving.md) | Creating or renaming a scope directory, archiving cold material, or retrofitting the pattern onto existing work |
| [`logs.md`](logs.md) | Creating or rolling a log chunk, or deciding where a knowledge base's operations log belongs |

Plus two templates copied into a scope, never read as instructions: [`session-root-context-template.md`](session-root-context-template.md) and [`session-wiki-context-template.md`](session-wiki-context-template.md).

## What this skill assumes

**Exactly one thing: a gitignored scratch area in the host repo that a session may write to freely.** Everything else ships in this skill directory. Drop the directory into another repo that has such an area, and it works unmodified.

It specifically does **not** require:

- **A durable committed knowledge base.** Some repos keep one (an "LLM-wiki": a maintained, version-controlled set of synthesized pages). Where that exists, it governs how material graduates out of scratch into it. Where it does not, promotion targets a skill, an instruction, a design doc or a README instead, and nothing else changes. Such a knowledge base is repo-specific content governed by its own repo's conventions — it is not a skill, and this skill never depends on one being installed.
- **A ticket system.** A ticket ID is one kind of scope handle among several; a branch name or any other stable identifier works as well.
- **Other skills.** Named conventions appearing below are *optional host-repo capabilities*, listed so you defer to one if it exists. None is a dependency.
- **A multi-agent cast.** Single-agent use is the baseline; coordinator-specific guidance is marked as such and is skippable.

Examples write `__untracked_stuff/` for the scratch root because that is this repository's name for it. Substitute whatever the host repo calls its own.

## Why

A long multi-turn session's context grows with accumulated conversation history, not with useful work — re-sent message history can dominate the window. Once knowledge lives on disk in a session-wiki, you can `/compact` or open a brand-new chat and resume at near-zero context.

## The one-way reference rule

*Read this before writing any cross-tier reference.*

A session-wiki lives in the host repo's **gitignored** scratch area; the repo's committed content — source, tests, skills, instructions, docs, and any durable knowledge base it happens to keep — lives under **version control**. References between those two tiers are legal in exactly one direction:

> **A non-version-controlled file MAY reference version-controlled content. A version-controlled
> file MUST NEVER reference non-version-controlled content.**

The asymmetry follows from what each tier can assume. A scratch file exists only on this workstation, so everything under version control is guaranteed to sit next to it and can be cited freely by path. A committed file must be **complete and self-explaining in a fresh clone** — and a fresh clone has no scratch directory at all, so every pointer from a committed file into scratch is dead on arrival for every reader who is not the machine that created it. It is *silently* dead: nothing fails, the file just quietly asserts something unreachable.

**Permitted in a version-controlled file — the scratch *convention*, as a placeholder:**

```
__untracked_stuff/<scope>/tasks/assignment_tracker.md  rm -rf "${out_dir}"
}

target="${1:-all}"
case "${target}" in
  clean) clean; exit 0 ;
```

A placeholder teaches the reader where to *create* something and promises nothing about what exists. Keep the angle brackets; do not substitute a real scope name to make it "concrete".

**Forbidden — a pointer to actual scratch content:**

```
See __untracked_stuff/some-audit-2026-01/session-wiki/findings/some-analysis.md
Origin: promoted from __untracked_stuff/some-experiment/deploy.sh
```

**Every example in a version-controlled file is hypothetical.** If the point genuinely needs the evidence, the evidence has not been promoted far enough: distill the finding INTO the committed file so it stands alone, and let the scratch copy be the audit trail nobody has to read. This applies to any committed artifact — a `SKILL.md`, an instruction, an `AGENTS.md`, a `README.md`, a durable knowledge page, a script's provenance comment, a source comment. A link-checking tool, where the host repo has one, mechanizes enforcement; absent one it is enforced by reading.

### Session-only identifiers are references too

The rule is not limited to paths. A **session-only identifier** — a ticket ID (`ABC-123`), a tracker item ID (`D7`), a scope slug, a branch name — embedded in a committed comment or doc is the same violation: it resolves only by opening the gitignored tracker that assigned it, and fails just as silently for a fresh-clone reader who cannot know the ID refers to anything.

```
// Sourced from Foo (ABC-123 D7), which now owns this behaviour.          <- forbidden
// Extracted from Bar per the corner-case fix agreed for this ticket.     <- fine (self-contained)
```

Better than skipping the label: **skip the label AND state the reasoning itself**, so the comment is understandable on its own. Prefer no ticket reference at all over an unresolved one.

### Corollary: the session-wiki holds the complete record

Because committed files may not point into scratch, the scratch scope must carry the **complete** account of the work — every side quest, dead end, capture and decision. Nothing may be left implicit on the assumption that a committed file will explain it. The committed side keeps the distilled knowledge; the scratch side keeps how it was arrived at.

## An agent memory tool is agent recall, never the visible record

Whatever the host harness calls its memory mechanism, it serves AGENT efficiency: fast recall and durable conventions across turns. That is its entire job.

**Memory must never be the sole home for anything the user would plausibly want to read or verify.** Unlike a committed file, or a gitignored file that is still visible in the editor and file tree, memory has no surface a user browses. Whatever the user asked about, or would want to check later, belongs in a VISIBLE tier: a committed doc, or the scope's own `session-wiki/` or `tasks/assignment_tracker.md`.

Memory MAY cache a short **pointer** to visible content. It must not host the substance: a memory entry restating reasoning already committed elsewhere has quietly become the primary record of that reasoning, and will go stale silently, since nobody reads memory to notice. This is the one-way reference rule one tier further out — a fact the user cares about may not live only somewhere the user does not look.

## Tolerated redundancy differs per tier

The three tiers an agent writes to obey different redundancy laws because they are paid for differently:

- **Committed content is loaded by strangers.** Every reader pays for every line, on every load, forever. Redundancy is pure cost: one fact, one page, everything else links. So is *perishable* content — a pass count, a ticket ID, a branch name, an "as of <date>" status — worklog residue that stops being true within days and then costs every future loader. The test: *would this still be true and useful to a reader who has never heard of this assignment, on a fresh clone, after the next few commits?*
- **The session-wiki and memory are workstation-local**, read by the agent that wrote them. Worklog style is the point, and **duplication for locality is tolerated whenever it saves tokens on the next resume** — a tracker line restating a finding's headline so the resume read need not open the finding. The limit is the *substance* rule above: duplicate pointers and headlines, never reasoning.

## Structure

`tasks/` and `session-wiki/` are always present; everything else is optional. Do not conflate them — they nest under one root but are distinct, non-overlapping things.

```
__untracked_stuff/<scope>/            # the "session sub-directory" — general scratch root
  AGENTS.md                           # OUTER — thin routing pointer
  tasks/                              # sibling — resume token lives here
    assignment_tracker.md             # the index AND the resume token: items + status + evidence
  session-wiki/                       # sibling — the structured wiki lives HERE, not at scope root
    AGENTS.md                         # INNER — routing pointer from inside the wiki
    index.md                          # sole navigation index for this session wiki
    raw/                              # immutable captures + open drop-zone
    findings/                         # synthesis: distilled findings citing raw
                                       # (repo-local name, e.g. `changes/` — map it, don't rename)
    bugs/                             # bug reports / repro notes
    commits/                          # commit files awaiting human review — see commits.md
    log/                              # ALWAYS present — this wiki's own operations log
      index.md                        # log-of-logs: one line per chunk
      <chunk files>                   # capped, dated or wave-based, rolling
  logs/                               # OPTIONAL — whole-scope narrative DISTINCT from
                                       # session-wiki's own construction; omit when none exists
  session-wiki-archive/               # OPTIONAL sibling — cold/superseded material
  <machinery>/                        # OPTIONAL — scope-local half of reusable tooling
  <other deliverables>                # README.md, scripts/, analysis/ — at the scope root,
                                       # alongside the above, NOT inside any of them
```

`tasks/assignment_tracker.md` is the sole task/status routing index and the resume token; `session-wiki/index.md` is the sole wiki navigation index. The scope root needs no navigation index of its own. Scope directory naming: [`naming-and-archiving.md`](naming-and-archiving.md).

**Repo-local names.** `assignment_tracker.md` is canonical — use it, not `tracker.md`. Where a repo has an established synthesis-directory name (`changes/` instead of `findings/`), **map** it to its canonical role in the scope's inner `AGENTS.md`; do not rename a working directory to match this skill's examples.

### `raw/` is staging, not storage

`raw/` is both an **immutable capture** location (agent-harvested output, written once, never edited) and an **open drop-zone** the user may put source material into at any time. "Immutable" describes what happens to a file already there — it does not mean the directory is closed to new arrivals.

Both roles are **transit**, not a destination. The wiki's value is synthesis: promoting durable content OUT of `raw/` into `findings/` beats leaving it as a "just in case" dump. Treat a stale, unpromoted `raw/` file as a synthesis backlog item, not acceptable steady state.

**Full tool-output dumps are not `raw/` material.** The test is whether an artifact is durable source worth re-reading, not merely that it came from a real command. A verbatim test-suite log fails it — tests can be re-run, so the log has no standalone evidential value once its outcome is known. Record a pass/fail summary; reserve full output for a genuine anomaly.

### Capture rule

Specialists MUST capture verbatim output to `raw/<YYYYMMDD>_<desc>.txt` before synthesizing into `findings/`. This keeps synthesis honest and enables re-synthesis without re-running commands.

## The tracker

`tasks/assignment_tracker.md` carries open items, status, dependencies and evidence pointers. It is read first on every resume, so it earns its size or loses it.

**Compact a closed item as soon as it reaches a terminal status** — one to three lines: the disposition, and an evidence pointer (a path, a test name and count, or a citation to the log chunk or findings page carrying the full narrative). Do not restate a narrative that already lives somewhere citable; cite it.

Do this **incrementally, as each item closes**, never as a periodic big-bang rewrite. A rewrite touching every item at once is exactly the edit that gets interrupted or partially applied, and the drift is hard to notice afterwards because the decision gets logged as complete before the write is verified. Compacting one item in the same edit that closes it has nothing to lose if interrupted.

When the tracker accumulates enough terminal items to dominate a resume read, rotate a generation: [`scaling-up.md`](scaling-up.md).

## Two `AGENTS.md` files per scope

Every scope gets both, with distinct jobs:

- **Outer** (`<scope>/AGENTS.md`) — a cache-stable routing pointer: stable scope identity, the tracker as first read, links to the inner file, wiki index and log index.
- **Inner** (`session-wiki/AGENTS.md`) — the same from inside the wiki: tracker first, then `index.md`, `log/index.md`, and the design that owns physical layout, plus an "agents do not commit" reminder.

Neither carries mutable branch/HEAD, status, open-item lists, evidence summaries or content inventories. The tracker and `session-wiki/log/` own all volatile resume state.

Copy them from the two templates in this directory. **Naming warning:** neither template is literally named `AGENTS.md` — that would risk being mistaken for a real sub-tree instruction file when browsing this skill. Only the copies inside an actual scope take that name.

## Discovery, and establishing a scope

A session-wiki should be established — discovered or created — early in any non-trivial multi-step session, by checking the scratch area for a matching or creatable scope directory. The pattern is the same across sessions even though each session's content differs.

Discovery does not assume a ticketing system, or that one exists: `<scope-identifier>` may derive from a ticket ID, a branch name, or any other stable handle. Deciding whether a matching scope exists, or whether to create one, belongs to the agent doing the work — this skill does not enforce it.

Two ways an agent learns about all this:

1. **From the repo's own instructions** (the baseline, and the only path needing no cast). `AGENTS.md` and the other always-on customizations point here. The user need only point at `AGENTS.md` or the scope directory.
2. **Coordinator-led**, where the host repo actually has a coordinating agent. A single-agent repo does not use this path.

## Session log

`session-wiki/log/` is ALWAYS present — the wiki's own operations history: raw captured, synthesized, promoted, archived. A scope-root `logs/` is OPTIONAL, for a genuine narrative that is *not* about the wiki's own construction; a scope whose whole story is wiki construction needs none, and an empty one is worse than none.

Unlike curated committed content, both logs capture ALL side quests, archival decisions and dead ends — they are an audit trail, not a curated index, and are more likely to be inspected precisely because they are honest rather than tidy.

Chunking, naming, provenance entries and the log-of-logs: [`logs.md`](logs.md).
  rm -rf "${out_dir}"
}

target="${1:-all}"
case "${target}" in
  clean) clean; exit 0 ;
## Restart protocol

A fresh session reads `tasks/assignment_tracker.md` FIRST (the resume token), then loads only the `session-wiki/` pages needed for the next step, consulting `log/index.md` if it needs deeper history than the tracker carries. Because all state is on disk, `/compact` or a new chat is safe at any point.

## Commits

Agents do not commit. Work stops in the working tree, and each commit is described in a file under `session-wiki/commits/` — written as a pull-request description for a human reviewer, with the essence first, a review order, and what is skimmable.

Format, naming, and the rules that make a commit file worth reading: [`commits.md`](commits.md).

## Promotion, and independence of durable knowledge

When the assignment closes, stable and broadly-useful knowledge GRADUATES out of the session-wiki into whatever durable home the host repo has — the file whose job it already is (a skill, an instruction, a design doc, a `README.md`), or a durable knowledge base where one exists. Ephemeral state — the tracker, raw captures, repros — is then discarded, or moved to `session-wiki-archive/` if worth keeping cold.

**Committed content stays independent of scratch.** A session-wiki MAY cite committed content freely. Committed content must never depend on, or be edited to accommodate, session-wiki content. Promotion flows one direction only, and only once knowledge has proved durable — a finding still phrased in terms of this one assignment has not earned it.

The reference-direction half is *The one-way reference rule* above: independence is not achieved if the committed page still ends with "see `__untracked_stuff/<real-scope>/findings/…`". Promote the substance, then cite nothing.

Where the host repo keeps a durable knowledge base, it is repo-specific content governed by its own conventions, and **this skill has no authority over it**. Read those conventions before promoting into it; let them win wherever they differ.

## Improvements to agent customizations discovered mid-session

Session work often surfaces a concrete improvement to agent-loaded files — a skill, an instruction, an `AGENTS.md`, a knowledge page. Two rules, needing no particular workflow to exist:

- **Capture it where you are.** Write it into `findings/` when you notice it, rather than carrying it in context to the end of the session, where it is among the first things lost to a crash or compaction.
- **Do not fold it in silently.** Editing an agent-loaded file changes how every future session behaves, so it is reviewed like any other change — see *Commits* above.

Where the host repo has a workflow for proposing such changes in batches, defer to it. Absent one, prepare the edit in the working tree and hand it off with everything else.

## Ownership model: who owns `tasks/`

Where the host repo's cast includes a dedicated task-tracking specialist, that specialist owns the whole `tasks/` sub-directory. Its remit spans every other specialist's domain, so it needs correspondingly broad awareness — a durable habit, not a memorized list: start from the repo's always-on instructions and follow where they route, check this skill for the structural conventions, and browse what that router currently surfaces rather than working from a hardcoded checklist that goes stale.

Where a repo has no such specialist, any agent performs the role — but name the pattern in the repo's own conventions so it knows to consider adding one.

## Relationship (link, don't duplicate)

**This skill has no required companions.** Every capability below is optional: where the host repo has one, defer to it instead of restating its rules; where it does not, nothing here stops working. The names are conventional labels, not a promise that anything by that name is installed.

| Capability, where the host repo has one | What it owns |
|---|---|
| A durable committed knowledge base (an "LLM-wiki") | The repo's compounding, version-controlled knowledge — same raw→synthesis→index shape, but permanent and reviewed. **Repo-specific content with its own conventions, not a skill.** |
| A link-checking tool | Mechanized dead-link and structural-conformance checking |
| A context-resilience convention | Checkpoint-after-dispatch and harvest mechanics that populate the session-wiki |
| A multi-agent choreography convention | Delegation and context isolation. Irrelevant in a single-agent repo |
| A customization-patch convention | Batched proposal of changes to agent-loaded files |
