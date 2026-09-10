---
name: session-wiki-pattern
description: "USE WHEN planning or maintaining a long, multi-step assignment that must survive context compaction, host-process crash, or session loss — and you want every piece of knowledge the session produces preserved durably so the work can RESTART in a fresh, lean chat from a resume token. A session-wiki is an ephemeral, scope-scoped working wiki in the host repo's gitignored scratch area, structured raw capture → synthesis → index, with a tracker that doubles as the resume token. It is self-contained and needs nothing but a scratch directory. DO NOT USE for single-shot tasks (a simple tracker suffices), or for authoring the host repo's durable committed knowledge, which outlives the session and follows that repo's own conventions."
---

# Session-Wiki Pattern

A **session-wiki** is an ephemeral, scope-scoped working wiki inside a *session sub-directory* under the host repo's gitignored scratch area (e.g. `__untracked_stuff/<scope>/` — crash-safe and machine-transferable). It gives a session the three-layer shape that makes knowledge accumulate instead of scroll past:

> **raw capture → synthesis → index**, with a tracker alongside that doubles as the resume token.

Raw holds what was actually observed, immutable once written. Synthesis distills it into findings that cite raw. An index makes both navigable without reading everything. The point is that (a) all knowledge produced during a long multi-step session is preserved on disk, not just in chat history or volatile memory, and (b) the session can RESTART in a fresh, lean chat from the tracker without losing anything.

## What this skill assumes

**Exactly one thing: a gitignored scratch area in the host repo that a session may write to freely.** Everything else — the structure, the rules, the two context templates — ships in this skill directory. Drop the directory into another repo that has such an area, and it works unmodified.

It specifically does **not** require:

- **A durable committed knowledge base.** Some repos keep one (an "LLM-wiki": a maintained, version-controlled set of synthesized pages). Where that exists, the rules below marked *if the host repo keeps durable committed knowledge* govern how material graduates out of scratch into it. Where it does not, promotion targets a skill, an instruction, a design doc or a README instead, and nothing else in this skill changes. Such a knowledge base is repo-specific content governed by its own repo's conventions — it is not a skill, and this skill never depends on one being installed.
- **A ticket system.** A ticket ID is one kind of scope handle among several; a branch name or any other stable identifier works as well.
- **Other skills.** Named conventions appearing later in this file are *optional host-repo capabilities*, listed so you defer to one if it exists. None is a dependency.
- **A multi-agent cast.** Single-agent use is the baseline; coordinator-specific guidance is marked as such and is skippable.

Examples below write `__untracked_stuff/` for the scratch root because that is this repository's name for it. Substitute whatever the host repo calls its own.

## Why

A long multi-turn session's context grows with accumulated conversation history, not with useful work — re-sent message history can dominate the window (a real session reached ~46% of a 1M-token window this way). Once knowledge lives on disk in a session-wiki, you can `/compact` or open a brand-new chat and resume at near-zero context.

## The one-way reference rule (read this before writing any cross-tier reference)

A session-wiki lives in the host repo's **gitignored** scratch area; the repo's committed content — source, tests, skills, instructions, docs, and any durable knowledge base it happens to keep — lives under **version control**. References between those two tiers are legal in exactly one direction:

> **A non-version-controlled file MAY reference version-controlled content. A version-controlled
> file MUST NEVER reference non-version-controlled content.**

The asymmetry is not a style preference; it follows from what each tier can assume:

- A scratch file exists only on this workstation, in this working tree. Everything under version
control is therefore guaranteed to be present next to it — it can cite a skill, a shard, a source file, a test, freely and by path.
- A committed file must be **complete and self-explaining in a fresh clone**. A fresh clone has
no scratch directory at all. Every pointer from a committed file into scratch is dead on arrival for every reader who is not the machine that created it — and it is *silently* dead: nothing fails, the file just quietly asserts something unreachable.

### What this permits, and what it forbids

**Permitted in a version-controlled file — the scratch *convention*, expressed as a placeholder:**

```
__untracked_stuff/<scope>/tasks/assignment_tracker.md
__untracked_stuff/<ticket>/device_handoff/<UTC>.md
```

A placeholder path teaches the reader where to *create* something. It promises nothing about what exists. Keep the angle-bracket placeholders — do not substitute a real scope name to make the example "concrete".

**Forbidden in a version-controlled file — a pointer to actual scratch content:**

```
Worked reference implementation: __untracked_stuff/ABC-123-some-feature/validation/
See __untracked_stuff/some-audit-2026-01/session-wiki/findings/some-analysis.md
Origin: promoted from __untracked_stuff/some-experiment/deploy.sh
```

Each of those asks a reader to open something a fresh clone does not have. **Every example in a version-controlled file is hypothetical** — if the point being made genuinely needs the evidence, the evidence has not been promoted far enough yet: distill the finding INTO the committed file so it stands alone, and let the scratch copy be the audit trail nobody has to read.

This applies to *any* committed artifact — a `SKILL.md`, an instruction, an `AGENTS.md`, a `README.md`, a durable knowledge page, a shell script's provenance comment, a source-file comment. It is the reference-direction counterpart to the content rule in *Promotion, and independence of durable knowledge* below. A link-checking tool, if the host repo has one, is the mechanized enforcement of this rule; absent one, it is enforced by reading.

### Session-only identifiers are references too, not just paths

The rule is not limited to file paths. A **session-only identifier** — a ticket ID (`ABC-123`), a tracker item ID (`D7`), a scope-directory slug, or a branch name — embedded in a committed comment or doc is exactly the same violation as a dead scratch path: it resolves only by opening the gitignored tracker that assigned it, and it fails exactly as *silently* for a fresh-clone reader, who has no way to know the ID even refers to anything.

```
// Sourced from Foo (ABC-123 D7), which now owns this behaviour.          <- forbidden
// Extracted from Bar per the corner-case fix agreed for this ticket.     <- fine (self-contained)
```

Better still than skipping the label: **skip the label AND state the reasoning itself** — the comment should be understandable on its own, without the reader needing to resolve anything. When in doubt, prefer no tracker/ticket reference at all over an unresolved one; a fresh-clone reader can verify a self-contained reason, but can never verify a label they cannot open.

### Corollary: the session-wiki holds the complete record

Because committed files may not point into scratch, the scratch scope must carry the **complete** account of the work happening on this workstation — every side quest, dead end, capture, and decision. Nothing may be left implicit on the assumption that a committed file will explain it. The committed side keeps the distilled knowledge; the scratch side keeps how that knowledge was arrived at.

## An agent memory tool is agent recall, never the visible record

Most harnesses provide some agent memory mechanism — scoped stores under `/memories/`, a per-project memory directory, a persistent notes file. Whatever the host harness calls it, it exists to serve AGENT efficiency: fast recall, avoiding re-discovery, and durable conventions that help an agent resume work quickly across turns and sessions. That is its entire job, and the rule below holds regardless of which harness is in use.

**Memory must never be the sole or primary home for anything the user would plausibly want to
read or verify.** Unlike a version-controlled file, or a file under `__untracked_stuff/` (gitignored, but still fully visible in the editor and file tree), memory has no equivalent surface — a user does not browse it the way they browse the repo. Whatever the user asked about, or would want to check later, belongs in a VISIBLE tier: a version-controlled doc, skill, or instruction; or, for scope-scoped material, the scope's own `session-wiki/` (`findings/`, `log/`) or `tasks/assignment_tracker.md`.

Memory MAY cache a short POINTER to visible content, for fast recall across sessions. It must NOT host the substance itself:

| Content | Home | Memory's role |
|---|---|---|
| A debugging workaround or tool quirk, agent-only | Memory, directly | Its home — nothing to point to |
| A transferable convention (naming, structure, workflow) | The skill that owns it | One-line pointer only |
| Ticket-specific state (a build version, a tracker's status, a fact the user stated directly) | The live tracker / scope scratch | Headline value + citation, never the reasoning |

A memory entry that restates reasoning already committed to a tracker or skill has quietly become the primary record of that reasoning — exactly what this rule forbids. It will go stale exactly like any other duplicate, except silently, since nobody reads memory to notice.

This is *The one-way reference rule* above, one tier further out: a committed file may not depend on content the reader cannot open; a fact the user cares about may not live only somewhere the user does not look.

## Tolerated redundancy is a tokenomics decision, and it differs per tier

The three tiers an agent writes to — committed content, the scope's session-wiki, and the agent memory tool — obey different redundancy laws because they are paid for differently:

- **Committed content is loaded by strangers.** Whatever form the repo keeps it in — a skill, an instruction, a design doc, a durable knowledge page — every reader pays for every line in it, on every load, forever. Redundancy there is pure cost: one fact, one page, everything else links. So is *perishable* content — a pass count, a ticket or tracker ID, a branch name, an "as of <date>" status, "this ticket" deixis — which is worklog residue that stops being true within days and then costs every future loader while helping none. The test before a sentence lands: *would it still be true and useful to a reader who has never heard of this assignment, on a fresh clone, after the next few commits?*
- **The session-wiki and memory are workstation-local and read by the agent that wrote them.** Here worklog style is the point, and **duplication for locality is tolerated whenever it saves tokens on the next resume**: a tracker line that restates a finding's headline so the resume read does not have to open the finding; a memory pointer that repeats a path already in the tracker; a compacted closed-item summary that duplicates a log chunk's disposition. Each of these spends a few bytes once to save a file read every time the scope is re-entered. The limit is the *substance* rule above — duplicate pointers and headlines, never reasoning — and the compaction discipline below, so the redundancy stays small enough to keep paying for itself.

Where the host repo keeps durable committed knowledge, that repo's own conventions own the repo-specific application of this split — which tier holds what, and any mechanized perishability check. This section is the transferable rationale, and holds with or without such a repo-side convention.

## Sibling directories under the session sub-directory: `tasks/` and `session-wiki/` are always present; `logs/` is optional

Do not conflate these — they nest under one root, but they are distinct, non-overlapping things:

- **The session sub-directory** (`__untracked_stuff/<scope>/`) is a general gitignored scratch area for the whole scope of work. It may hold MANY kinds of material beyond the wiki: deliverables, one-off scripts, notebooks, PR drafts, human-testing protocols, analysis output, whatever the assignment produces. Tooling the scope *runs* and hands to its successor is a distinct category with its own rules — see "Reusable machinery" below.
- **`tasks/`** is a sibling sub-directory that holds `assignment_tracker.md` — the resume token and routing index for the whole scope (see "Ownership model" below). It is NOT nested inside `session-wiki/`.
- **`session-wiki/`** is a sibling sub-directory that holds the structured raw→synthesis→index wiki content described below — findings, bugs, raw captures — AND its own `log/` sub-directory (see "Session log" below), ALWAYS present, for the wiki's own operations history.
- **`logs/`** (scope root, sibling to `session-wiki/`) is OPTIONAL — like `session-wiki-archive/`, it exists only when the scope has a genuine narrative that is NOT about session-wiki's own construction (e.g. real ticket/engineering work distinct from building the wiki itself). Do not maintain an empty or duplicate scope-root `logs/` "just in case"; a scope whose whole story IS session-wiki construction has no need for one.

For a simple session it's fine for everything to flow straight through `tasks/` and `session-wiki/` (with its `log/`) with nothing else alongside them. The general case allows a lot of coexisting non-wiki material at the session sub-directory root, next to (not inside) either.

The scope root does NOT need its own navigation index. `tasks/assignment_tracker.md` is the sole
task/status routing index, while `session-wiki/index.md` is the sole wiki navigation index. Outer
and inner `AGENTS.md` only route to the tracker, wiki index, and `session-wiki/log/` operations log.

## Structure

```
__untracked_stuff/<scope>/            # the "session sub-directory" — general scratch root
  AGENTS.md                           # OUTER — thin pointer (see "Two AGENTS.md files" below)
  tasks/                              # sibling — resume token lives here (see "Ownership model")
    assignment_tracker.md             # the index AND the resume token: items + status + evidence
  session-wiki/                       # sibling — the structured wiki lives HERE, not at scope root
    AGENTS.md                         # INNER — detailed, points to tasks/assignment_tracker.md
    index.md                          # sole navigation index for this session wiki
    raw/                              # immutable captures + open drop-zone (see below)
    findings/                         # synthesis: distilled findings and evidence docs
                                       # (repo-local name, e.g. `changes/` — map it, don't rename)
    bugs/                             # bug reports / repro notes
    commits/                          # proposed commit messages awaiting human review
                                       # (see "Proposed commits" below)
    log/                              # ALWAYS present — session-wiki's OWN operations log
                                       # (see "Session log" below for the naming rules)
      index.md                        # log-of-logs: one line per chunk, for long-gap resumption
      <chunk files>                   # capped-size, dated or wave-based, rolling
  logs/                               # OPTIONAL sibling — whole-scope narrative DISTINCT from
                                       # session-wiki's own construction (see "Session log" below);
                                       # omit entirely when no such genuine narrative exists
    index.md                          # same log-of-logs shape as session-wiki/log/, when present
    <chunk files>
  session-wiki-archive/               # SEPARATE sibling to session-wiki/ — see "Archive" below
  <machinery>/                        # OPTIONAL sibling — the SCOPE-LOCAL half of reusable tooling
                                       # (e.g. `validation/`): this ticket's units, driver, and
                                       # fixtures. Its reusable core is version-controlled
                                       # elsewhere — see "Reusable machinery" below
  <other deliverables>                # README.md, scripts/, analysis/, incoming/, etc. — stay at
                                       # the session sub-directory root, alongside the above,
                                       # NOT inside any of them
```

`tasks/assignment_tracker.md` is the sole task/status routing index and the resume token;
`session-wiki/index.md` is the sole wiki navigation index; `raw/` is the source of truth for captured
material; `findings/` (or its repo-local equivalent) and `bugs/` are synthesis that cite `raw/`;
`session-wiki/log/` is the complete narrative record of the wiki's own construction, with an optional scope-root `logs/` for genuine narrative beyond that (see "Session log" below).

### Scope directory naming: handle + condensed title

A scope directory name is `<handle>-<condensed-title-slug>` — the durable handle (ticket ID, branch-derived identifier, or other stable identifier) followed by a short, human-readable slug condensed from the ticket/assignment title.

Illustrative shapes (hypothetical — see *The one-way reference rule* above):

```
__untracked_stuff/ABC-123-beacon-tracking-corner-cases/    # handle + condensed title
__untracked_stuff/ABC-456-keep-alive-validation-and-pr/
__untracked_stuff/docs-audit-2026-01/                      # non-ticket handle, same shape
```

A bare `__untracked_stuff/ABC-456/` is NOT sufficient. A directory listing is the cheapest discovery surface an agent or human has — a bare ID forces opening files just to learn what a scope is about, and after several tickets the listing becomes unreadable.

Rules:

1. **Handle first, verbatim.** Keep the exact ticket/branch identifier as the leading token so
ID-based search (`ls -d *123*`, `grep ABC-123`) still resolves.
2. **Slug is lowercase kebab-case,** roughly 2–5 words / ≤ 40 characters. Condense the title;
do not transcribe it. Drop filler ("update", "fix", "add") that every assignment shares.
3. **Separator is `-`, not `_`.** One separator style keeps the listing scannable.
4. **The slug names the SUBJECT, not the status.** No `-wip`, `-done`, `-v2`. Status lives in
the outer `AGENTS.md` banner and the tracker.
5. **Distinguish continuations by subject, not by number alone.** When a successor scope covers
the same feature (`ABC-455-keep-alive-via-config` → `ABC-456-keep-alive-validation-and-pr`), let the slug say what each one actually did.
6. **Derive the slug from a real source, not from guesswork:** the ticket title, the scope's
`README.md`/`AGENTS.md` heading, or the branch name — in that order of preference.

#### Normalizing an existing bare-ID scope (audited rename)

Existing scopes named with a bare handle SHOULD be normalized. This is the one sanctioned exception to the freeze rule in *Ticket migration* below, and it is only safe as a single audited operation:

1. Derive each slug from that scope's own `README.md`/`AGENTS.md`/branch — never invent one.
2. Rename, then **rewrite every cross-scope path reference in the same operation** —
`../<old>/`, `../../<old>/`, and `__untracked_stuff/<old>/` — across scope docs AND any version-controlled file that cites the path (wiki shards, skills). Restrict the rewrite to path contexts: a blind substitution corrupts branch names, which share the `<ID>/` prefix shape (`ABC-456/keep_alive_beacon_tracking`).
3. Re-run a dead-link audit over the scope afterwards — mechanically where the host repo has a link-checking tool, otherwise by grepping the old scope name across scope documents and committed files.
4. Log the full old→new mapping in the acting scope's `session-wiki/log/`, and leave already-
written historical log chunks in other scopes unedited — they are an immutable audit trail; the mapping entry is what makes their old paths resolvable.

### Naming (canonical vs. repo-local)

`assignment_tracker.md` is the canonical example name used throughout this skill — use it, not `tracker.md`. Repos may have their own established synthesis-directory name (e.g. `changes/` instead of `findings/`). When that's the case, **map** the repo-local name to its canonical role in the scope's inner `AGENTS.md` (see below) — do not rename an existing, working directory just to match this skill's example names.

### `raw/` is staging, not storage — it has two roles, not one

`raw/` is BOTH of these at once:
1. An **immutable capture** location: agent-harvested command output, logs, specialist returns, written once and never edited in place.
2. An **open drop-zone**: the USER may place source material there anytime they want it ingested into the wiki — exports, notes, screenshots-as-text, anything.

"Immutable" describes what happens to a file already in `raw/` (it is never edited after being written) — it does **not** mean the directory is closed to new arrivals. New files may land in `raw/` at any time, from the user or from an agent.

Both roles are explicitly **transit**, not a destination. The wiki's whole value proposition is synthesis: promoting durable, load-bearing content OUT of `raw/` and into `findings/` (curated, cited, reusable) beats leaving material sitting in `raw/` indefinitely as a "just in case" dump. An ever-growing `raw/` that nothing ever graduates out of has lost the pattern's benefit — it is doing the job of storage, which is not its job. Treat a stale, unpromoted `raw/` file as a synthesis backlog item, not as acceptable steady state.

### Full raw tool-output dumps are not `raw/` material

Not every artifact a session produces belongs in `raw/`, even when it was genuinely captured during the session. The test is whether the artifact is durable source material worth re-reading later — not merely that it came from a real command. A full, verbatim gtest/test-suite log is the common case that fails this test: unit tests can be re-run at will, so the log has no standalone evidential value once its outcome is known. Record only what the record actually needs — a short pass/fail count summary — and reserve full verbatim output for a genuine failure or anomaly worth investigating further. If a full dump is produced anyway (e.g. for local debugging), it belongs in an ordinary, non-version-controlled/non-curated scratch location, not `raw/`; keeping it there "just in case" is ceremony, not synthesis.

### Reusable machinery: the third kind of scope-root material

A mature scope holds three distinct kinds of material, and they obey different rules:

| Kind | Lives in | At succession |
|---|---|---|
| **State** — what is done, what is next | `tasks/` | carried forward (open items only) |
| **Knowledge** — captures, findings, narrative | `session-wiki/` | **cited, never copied** |
| **Machinery** — code the scope runs | a scope-root sibling (`validation/`, `harness/`, …) | **carried forward and split** (see two tiers below) |

Machinery is the one category exempt from cite-don't-copy. Evidence is cited because a second copy of a finding is a second thing to keep true. Machinery must move because a successor scope has to *run* it, and because reaching across a frozen predecessor's directory to import its code makes that predecessor un-freezable — any change to satisfy the successor rewrites the record the predecessor exists to preserve.

#### Two tiers: reusable core vs scope-local extension

Machinery is not one thing. Split it by **lifespan**, and let lifespan decide the home:

| Tier | Lifespan | Home | Status |
|---|---|---|---|
| **Core** — parsing, data model, registries, aggregation, shared utilities | outlives every ticket | a **version-controlled package inside the owning skill** | committed, unit-tested, reviewed |
| **Extension** — one unit per scope: this ticket's patterns, claims, fixtures, driver, human-facing docs | dies with the ticket | the scope's scratch directory | gitignored, never committed |

The extension declares a path dependency on the core. This assumes the repo's physical layout is stable, which is a reasonable assumption for a single-repo workflow and should be stated explicitly where the dependency is declared.

What this buys, and what it costs:

- The core gets **tests, review, and history** — appropriate, because a bug there now corrupts
every scope that depends on it. Scratch code has none of those and does not deserve them.
- Each scope's directory shrinks to the part that is genuinely about that ticket, which is also
the part a reviewer should read.
- The cost is that a core change is no longer a local edit. Changing it must keep the core's own
tests green, not merely one scope's driver.

**Do not promote to core prematurely.** The first scope writes everything locally; the second
scope's carry-forward is what reveals which half was actually reusable. Promoting on a guess produces a "reusable" core shaped around one ticket's accidents.

#### The engine / extension seam

Copying alone produces N divergent forks. Split the machinery instead, at the line between what is true for every scope and what is true for this one:

```
<version-controlled home>/       # the CORE tier — e.g. inside the owning skill
  <package>/            # scope-agnostic: parsing, data model, result contract,
                        # registries, aggregation, shared utilities
  tests/                # real tests — this half is committed, so it is tested
  pyproject.toml

__untracked_stuff/<scope>/<machinery>/   # the EXTENSION tier — scratch
  <units>/              # one registered unit per scope/ticket it covers
    __init__.py         # discovery + registry
    unit_<handleA>_<slug>.py
    unit_<handleB>_<slug>.py   # the new scope adds THIS FILE and nothing else
  <driver>              # notebook/CLI that iterates registered units
  fixtures/             # synthetic input exercising every unit, for a dry run
  pyproject.toml        # path-depends on the core, editable
```

Before the core has earned promotion (first scope, or a one-off), the same seam holds with both tiers side by side in scratch — `engine.py` next to `units/`. The seam is the invariant; the two homes are what the rule of two buys you later.

Rules that keep the seam honest:

1. **Adding a scope adds a file.** If covering the new scope requires editing the engine, the
driver's structure, or a predecessor's unit, the seam is in the wrong place — move it before writing the new unit.
2. **A move is a move, not a rewrite.** When lifting existing logic into a unit, preserve
behavior exactly, and carry its provenance comments (`# src/<file>:<line>`, verification dates) across unchanged. Those comments are the audit trail for why the logic is correct; re-deriving them costs more than the move did.
3. **Namespace whatever the units register** (event kinds, check IDs, fixture sections) by
handle, and make the registry **reject a duplicate registration with a hard error**. Silent shadowing between units is undetectable from a green run.
4. **An empty unit must still render.** A scope registered but not yet implemented reports
"0 items registered — pending <blocked tracker item>" in every output, plus an explicit scope line stating it is NOT covered. Silence lets a reader see green and believe something was verified that was never exercised.
5. **Beware module-registry desynchronization on reload.** Registries are module-global, and
re-running import cells in an interactive driver desynchronizes them — silently in one direction, loudly in the other. Reloading a single-module engine rebinds its registries and
   **deregisters every already-imported unit**, so the driver runs green while asserting nothing.
Reloading a *package* re-runs only its `__init__`, leaves submodule registries populated, and the next unit import dies on a duplicate-id error. The fix for both is explicit teardown then a guard — `reset_registries()` → re-import units → `registry_guard(n)` — never bare `importlib.reload`.
6. **Re-verify in the new scope before trusting it.** A carried-forward harness is a hypothesis
until it has passed its dry run against the bundled fixture *and* a negative test (empty or contradicting input) in its new home. "It worked in the predecessor" is not evidence.
7. **The predecessor's copy stays frozen and runnable.** Do not delete, edit, or re-point it.
Recorded evidence cites the outputs it produced.
8. **Relocating code changes what relative paths mean.** A default computed from `__file__`, a
`../../` fixture path, a discovery root — each silently retargets when its module moves to a different depth. Audit every path-valued default as part of the move; the failure mode is not a crash but an empty result set that reads like "the tester collected nothing".

#### Promote the core, keep the ticket's part in scratch

What graduates out of scratch is **the reusable core plus the discipline**; what stays is the ticket's own unit. Both halves of that sentence matter — an earlier draft of this skill said "never copy code into a skill", and the very next rollover disproved it: the core belonged under version control, where it could be tested and reviewed, precisely because it had stopped being about one ticket.

The trigger is the **rule of two**: on the second scope that needs it, the core is proven reusable — promote it, with tests. On the first scope, leave it local. Cite the live implementation from the skill as the worked reference; the skill documents the API and the lessons, it does not restate the code.

Before promoting, harvest the predecessors: earlier scopes' notebooks and scripts usually contain techniques and — more valuable — recorded *failures* that the new core should encode. Read the archived and superseded artifacts specifically; they hold the "this did not work, and here is why" that clean current code no longer shows. Every utility promoted this way should carry a one-line docstring naming the scope experience that justifies it; a utility nobody can justify that way is speculation, and speculation is what makes a core hard to change later.

The shape this takes in practice: a single-scope validation harness is carried into its successor scope and split into an `engine.py` plus per-scope suites, so one capture proves both scopes; then, once several earlier scopes' notebooks have been mined for technique, the engine graduates to a version-controlled, unit-tested package hosted inside the skill that owns it, with each scope's harness path-depending on that package. Seam hazards 5 and 8 above are the two that bite during those moves — expect them rather than discovering them.

(Stated without ticket IDs or scope slugs on purpose: this file is version-controlled, and *Session-only identifiers are references too* above forbids labels a fresh-clone reader cannot resolve. The reasoning has to carry itself.)

#### Rollover tokenomics

A carry-forward is a predictable, repeatable operation, so it is worth doing cheaply. What made the difference in practice:

- **Delegate the mechanical move to a subagent with an exact spec** — absolute source and target
paths, the module-by-module split, the required verification commands, and what it must NOT touch. Mechanical moves are large-output, low-judgment work; that is the cheapest thing to send away from the main session, and it keeps the coordinating context small enough to still reason about the *design*.
- **Never say "a temp location" or "scratch space" in a dispatch.** Name the exact in-workspace
path. An unqualified "somewhere" reliably lands outside the workspace, where nothing is reviewable or archivable.
- **Send research and implementation as separate dispatches.** Mining predecessors is read-only
and can run thorough and wide; the move that follows is narrow and must be surgical. Combining them forces one context to hold both.
- **Demand verification output in the return, not a claim.** Command output, file list, line
counts. A subagent reporting success without evidence has to be re-verified anyway, which costs more than asking for it up front.
- **Ask the subagent to report what it could NOT ground**, and treat that list as tracker input.
It is cheaper to receive an honest placeholder than to discover an invented one during review.
- **Do the skill and knowledge edits in the coordinating session**, not in the dispatch. They
need judgment about precedence and duplication across files the specialist never loaded.

### Compacting closed items without a big-bang rewrite

A long-running tracker accumulates two different things over its life: open items that still need action, and closed items whose resolution narrative was necessary to work out but is no longer needed to resume. Left unaddressed, closed items accrete multi-paragraph resolution detail that often just restates what a `session-wiki/log/` chunk or a `findings/` page already says — the tracker becomes a second, slightly-differently-worded copy of the same narrative, which costs context on every read and drifts from the source it was copied from.

Compact a closed item's tracker entry to roughly one to three lines as soon as it reaches a terminal status: the disposition, and an evidence pointer (a file path, a test name and count, or a citation to the `session-wiki/log/` chunk or `findings/` page that carries the full narrative). Do not restate the narrative in the tracker once it lives somewhere citable — cite it. This is the same cite-don't-copy discipline this skill applies to evidence elsewhere, applied to the tracker's own closed items.

Do this compaction **incrementally, as each item closes**, not as a periodic big-bang rewrite of the whole tracker. A rewrite that touches every item at once is exactly the kind of large, all-or-nothing edit that can be interrupted, partially applied, or lost to a session crash between "decided" and "written" — and because the decision so easily gets logged as complete before the write is verified, the drift is not just possible but hard to notice afterward. Compacting one item in the same edit that closes it is a small, low-risk operation with nothing to lose if interrupted. If a tracker has already accumulated a backlog of un-compacted closed items, treat compacting it as an ordinary tracker-maintenance item with its own evidence requirement (a before/after item count, or a line-count reduction) rather than an implicit side effect of "cleaning up" — and verify the rewritten file on disk before treating the old version as superseded.

### Rotating tracker generations around 60% DONE

A tracker generation is the set of items accumulated since the last rotation. Incremental
closed-item compaction remains the normal maintenance rule; generation rotation is the milestone
operation that prevents even compact terminal entries from dominating every resume read.

At a genuine milestone or immediately before a new work wave, count the live generation after
compaction. Rotate it when either condition holds:

- `DONE` items account for roughly 60% or more of the generation; or
- every item is terminal and follow-up work is about to begin in the same scope.

The percentage is a pressure signal, not a quota. Do not interrupt an in-flight dependency chain
merely because a count crossed the threshold; rotate at the next coherent milestone.

Rotation is an audited replacement, never a status rewrite:

1. Freeze the entire current tracker unchanged at
   `session-wiki-archive/tasks/assignment_tracker-<generation>.md`. Use a stable generation label
   and never overwrite an earlier archive.
2. Replace the live `tasks/assignment_tracker.md` with a fresh resume marker for the new generation.
3. Carry forward every nonterminal item with its substantive context, owner, status, dependencies,
   and evidence intact. Carry only the minimal compact terminal prerequisite markers still needed
   to understand those live dependencies; cite the archived generation for the full record.
4. Record the milestone, pre/post item counts, archive path, and next action in the `session-wiki/log/` operations log.
5. Verify the archived copy matches the pre-rotation tracker and verify the new live tracker on
   disk before recording the rotation as complete.

If every item is terminal and no immediate follow-up exists, use the same archive procedure and
leave a short live stub: closure, archive link, and the instruction to populate it fresh for the
next assignment. The live tracker must remain mostly resume markers, TODOs, and genuinely active
nonterminal work; loaded context files never become a second status index.

### Archive: `session-wiki-archive/` is a separate sibling, never nested

`session-wiki-archive/` sits next to `session-wiki/`, at the same level — never inside it. It holds COLD or superseded material, on the same "never modified once written" footing as `raw/`, but for material that is no longer live session state rather than fresh captures.

- `session-wiki/` MAY reference archive material.
- Nobody needs to open `session-wiki-archive/` under normal circumstances — the latest `session-wiki/` materials must be self-sufficient on their own.
- Archived material participates in future work strictly **as-needed**: pulled in only when explicitly relevant to a specific question, never loaded by default.

### Archiving invariants (checkable)

Derived from a real failure (a scope that archived to a scope-root `archive/`, left stale banners presenting superseded state as current, and accumulated dead references in its inner `AGENTS.md`):

1. **Archive location invariant.** Archived material lives ONLY in the sibling
`session-wiki-archive/` — never a scope-root `archive/`, never nested inside `session-wiki/`. Any other archive directory in a scope is a defect: MOVE its contents (unmodified) to `session-wiki-archive/` and record the move in `session-wiki/log/`.
2. **Context-stability invariant.** Outer and inner `AGENTS.md` files MUST NOT present branch heads,
status banners, task lists, completed-item inventories, or other volatile resume state. Status,
succession, and tracker-generation changes update the tracker and `session-wiki/log/` operations
log, leaving context files unchanged unless stable routing actually changes.
3. **Dead-reference audit at session close.** Before ending a session (and always during a
migration), audit the scope's outer/inner `AGENTS.md` and live tracker for references to files that were archived, moved, or never created; fix or remove each one. A link-checking tool, where the host repo has one, mechanizes this detection; absent one it is a grep and a read.

### Ticket migration (scope succession)

When a ticket closes but its work continues under a new ticket:

- **Freeze the old scope in place** (immutable — recorded evidence paths must not break). Never
rename the old scope directory as part of a migration; never continue live work inside a scope named for a closed ticket. (The only sanctioned rename is the audited naming normalization in
  *Scope directory naming* above, which rewrites all references in the same operation.)
- **Record closure and succession** in the old tracker's final archived generation and `session-wiki/log/`,
including the successor scope, corrected branch, and closure relationship. Keep the outer/inner
`AGENTS.md` files stable unless physical layout changed.
- **Rotate and archive its final tracker generation** per the milestone convention above; open
items are carried forward to the successor, which leaves the predecessor with a terminal record.
- **Create a fresh sibling scope** named for the new ticket, carrying forward ONLY live state
(open items, hard constraints still in force) and **citing — never copying —** the predecessor's evidence via read-only relative paths.
- **Copy the predecessor's machinery forward and generalize it** at the engine/extension seam —
the one category exempt from cite-don't-copy (see *Reusable machinery* above). Re-verify it in its new home before relying on it.
- Fix any archiving-invariant violations found in the old scope as part of the migration.

Record the migration decision in the SUCCESSOR scope's `session-wiki/findings/` — that record is scratch, and no committed file may point at it (see *The one-way reference rule* above). A migration worth citing from committed content is a migration whose lesson belongs in this skill.

### Capture rule

Specialists MUST capture verbatim output to `raw/<YYYYMMDD>_<desc>.txt` before synthesizing into `findings/` (or the repo-local equivalent). This keeps the synthesis layer honest and enables re-synthesis without re-running commands.

## Ownership model: who owns `tasks/`

If the host repo's agent cast includes a dedicated task-tracking specialist — a named sub-agent or persona, in a harness that supports them — that specialist owns the whole `tasks/` sub-directory: building and maintaining `assignment_tracker.md`, plus whatever internal structure it needs (waves, archiving stale items out of the live tracker). Keeping the tracker lean, well-organized, and evidence-backed is specialized knowledge that belongs to that role.

This role is unlike a narrowly-scoped specialist: its remit spans EVERY other specialist's domain, because tracking work touches whatever any specialist is doing. That breadth means it needs correspondingly broad awareness — make this a durable **habit**, not a fact to memorize once:

- Start from the repo's always-on instructions (`AGENTS.md`, or the host harness's equivalent) and follow wherever they route — a durable knowledge base's index where the repo keeps one, otherwise the skills, docs and per-directory rules they name. The tracking role cannot know in advance which domain a given assignment will touch, so it reads the router rather than one fixed page.
- Check this skill for the structural conventions being applied.
- Check for whatever OTHER conventions or mechanisms the repo has established, by browsing what that router currently surfaces — new mechanisms get added over time, so a hardcoded enumerated list of "things to check" goes stale. The habit is "consult the router and see what's current," not "remember a fixed checklist."

Other specialists (e.g. a general dev specialist) author content into `session-wiki/` files; they do not own `tasks/`.

If a repo's cast has no dedicated task-tracking specialist, any specialist may perform this role — but name the pattern in the repo's own conventions so the repo knows to consider adding one.

## Discovery and surfacing the session-wiki 

How an AI agent learns about the session-wiki-pattern.

1. **Agent reads it from the repo's own instructions (the baseline, and the only path that needs no cast).** `AGENTS.md` and the other always-on customizations point at this skill and at the scratch-area convention. The user need only point at `AGENTS.md` or the scope directory, and the agent loads this skill and the relevant scope's session-wiki on its own.
2. **Choreographer-led, where the host repo actually has a coordinating agent.** In a multi-agent setup, the coordinator's skill-discovery duty includes proactively telling relevant specialists about this skill — and pointing them at the right scope directory — whenever it coordinates multi-step or multi-session work. A single-agent repo simply does not use this path.

## Two `AGENTS.md` files per scope

Every scope gets BOTH an outer and an inner `AGENTS.md`, with distinct jobs:

- **Outer** — at the session sub-directory root (`__untracked_stuff/<scope>/AGENTS.md`). A
  cache-stable routing pointer: stable scope identity, `tasks/assignment_tracker.md` as the first
  read, and links to the inner `AGENTS.md`, wiki index, and operations-log index.
- **Inner** — at `session-wiki/AGENTS.md`. The same cache-stable routing pointer from inside the
  wiki: tracker first, then `index.md`, `log/index.md`, and the higher-level skill or committed
  design that owns physical layout, plus an "agents do not commit" reminder.

Neither file carries mutable branch/HEAD, status, open/completed item lists, evidence summaries, or
content inventories. The assignment tracker and `session-wiki/log/` own all volatile resume state.

Templates for both are provided in this skill's directory:
- [`session-root-context-template.md`](session-root-context-template.md) — outer
- [`session-wiki-context-template.md`](session-wiki-context-template.md) — inner

**Naming warning:** neither template file is literally named `AGENTS.md` — that would risk being mistaken for a real sub-tree `AGENTS.md` when someone browses this skill's directory. Only the copies created inside an actual scope directory should be named `AGENTS.md`.

## Discovery is general, not tied to a ticket system

Discovering a session's scope directory should not assume any single ticketing system, or that one exists at all. A ticket ID is only ONE example handle. Others include a git branch name that matches or relates to the scope directory name, or any other durable identifier established by whoever started the session.

The general instruction: check `__untracked_stuff/<scope-identifier>/` for a matching or creatable session-wiki, where `<scope-identifier>` can be derived from a ticket ID, a branch name, or another stable handle. Deciding whether a matching session exists, or whether to create one, belongs to the agents/specializations relevant to the current work — it is not a rigid rule this skill enforces itself.

## Establish a session-wiki early, for every non-trivial session

A session-wiki ought to be established (discovered or created) early in any non-trivial multi-step session — generally by checking `__untracked_stuff/` for a matching or creatable scope directory. The session-wiki pattern itself (raw→synthesis→index, `tasks/assignment_tracker.md`, two `AGENTS.md` files) is fundamentally similar across all sessions even though each session's specific content varies.

## Session log: `session-wiki/log/` (always) and scope-root `logs/` (optional)

Two distinct logs may exist, never conflated:

- **`session-wiki/log/`** is ALWAYS present. It is session-wiki's own operations log — raw captured, synthesized, promoted, and archived. Every scope has one, because every scope's session-wiki has construction activity worth logging.
- **Scope-root `logs/`** is OPTIONAL, on the same footing as `session-wiki-archive/`: create it only when the scope has a genuine narrative that is NOT about session-wiki's own construction — e.g. real ticket/engineering work (implementation decisions, bugs found and fixed) that exists independently of building the wiki itself. A scope whose whole story IS the session-wiki (nothing beyond wiki construction happened) has no need for a scope-root `logs/` — do not maintain an empty or duplicate one "just in case".

Unlike curated, version-controlled content, both logs are expected to capture ALL side quests, archival decisions, and dead ends — not just the clean narrative. They are closer to an **audit trail** than a curated index, and are more likely to be inspected or audited precisely because they are the honest, complete record rather than a curated one.

Physical design (transferable — describe the shape generically; applies identically to BOTH `session-wiki/log/` and scope-root `logs/`, when the latter exists — **and to a durable knowledge base's own operations log, which is itself scratch; see *An operations log is never version-controlled* below**):

- **Chunk filename:** `YYYY-MM-DD.md` for the first chunk of a day; `YYYY-MM-DD-2.md`, `YYYY-MM-DD-3.md`, … for subsequent chunks. A wave-based scheme (`<wave>-NN.md`) is equally acceptable, as long as it carries a numeric suffix so same-period rollover has an unambiguous next filename.
- **Cap** each chunk at roughly 1 000 lines; roll to the next suffix once a chunk would exceed that.
- **Entry header convention:** `## [YYYY-MM-DD] <op> | <subject>` — a stable prefix makes the log greppable with `grep "^## \[" <chunk> | tail`.
- **Ingest entries additionally record provenance**, so a claim can be traced back to the artifact it came from:
  ```
  ## [YYYY-MM-DD] ingest | <source title> → <destination>
  <one-line summary of what changed>
  - raw file: `raw/<exact-filename>`
  - sha256: `<full-64-char-hex-digest>`
  ```
- Maintain a lightweight `index.md` (a log-of-logs) that summarizes each chunk — its date/wave range and a one-line summary — so a fresh agent resuming after a long gap can jump straight to the relevant era instead of reading every chunk in order.
- Design for resuming after a long dormancy on the order of a couple of years; do not over-engineer for a decade-plus.

### An operations log is never version-controlled

This holds for a **durable, committed** knowledge base too, where the host repo keeps one — not just for session scratch. Such a base earns its keep through distilled knowledge; an append-only "what happened when" log makes it grow with **time** instead of with **knowledge**, and every entry ages into noise a reviewer must still read past. Worse, log entries are exactly the content most likely to cite scratch paths, work waves, and in-flight state — which would put a committed file in violation of *The one-way reference rule* above.

So: a committed knowledge base keeps its operations log in the **scratch scope of whoever maintains it**, using the same shape described here. What graduates into the committed side is the resulting knowledge page, not the record of the session that produced it. How the team arrived at an explanation is reviewed before the knowledge is committed; it is not maintained under version control afterwards.

## Retroactive bootstrap

When applying the session-wiki pattern to a work area that predates the structure:
1. Create `raw/README.md` documenting what was captured before the session-wiki and where the evidence resides. Do NOT fabricate raw captures.
2. Create the `session-wiki/log/` directory with an initial chunk as an append-only record going forward. Only add a scope-root `logs/` too if genuine non-wiki narrative already exists to retroactively capture.
3. Record stable repo-local name mappings in the session-wiki index or owning design; record
   provenance gaps in the tracker, findings, or operations log rather than in loaded `AGENTS.md`.

No prior evidence needs to be retrofitted into `raw/` — an honest gap note in `raw/README.md` is sufficient.

## Restart protocol

A fresh session reads `tasks/assignment_tracker.md` FIRST (the resume token), then loads only the `session-wiki/` pages it needs for the next step, consulting `session-wiki/log/index.md` (and scope-root `logs/index.md`, if present) if it needs deeper history than the tracker carries. A choreographer, if present, rebuilds lean coordination state — not the full history. Because all state is on disk, `/compact` or a new chat is safe at any point.

## Proposed commits: `session-wiki/commits/`

Agents do not commit. The work stops in the working tree and a human reviews it, so the **commit message is a session artifact, not a repository artifact** — it is written to `session-wiki/commits/`, never into a tracked file, a `COMMIT_EDITMSG`, or a staged commit template.

One file per proposed commit. Each names the exact paths it covers, so a reviewer can stage precisely that set and reject the rest without re-deriving the grouping. When one session produces several logically separate commits, write several files rather than one message describing everything; the grouping decision is part of what the reviewer is being asked to approve.

A commit message is subject to *The one-way reference rule* at the top of this skill, and more strictly than most files, because once accepted it becomes permanent version-controlled history read by strangers with no access to this scope. So a proposed message carries no scratch paths, no scope slug, no tracker item ID, no ticket ID, and no "as of this session" deixis. It states what changed and why in terms that stand alone in a fresh clone. Evidence supporting the change stays in `findings/`; the message cites none of it.

The reviewer, not the agent, decides whether to use the message verbatim, edit it, or split the commit.

## Promotion, and independence of durable knowledge

When the assignment closes, stable and broadly-useful knowledge GRADUATES out of the session-wiki into whatever durable home the host repo actually has — the file whose job it already is (a skill, an instruction, a design doc, a `README.md`), or a durable committed knowledge base where the repo keeps one. Ephemeral session state — the tracker, raw captures, repros — is then discarded, or moved to `session-wiki-archive/` if still worth keeping cold.

**Committed content stays independent of scratch.** A session-wiki MAY cite committed content freely; it is transient and benefits from pointing at what is durable. Committed content must never depend on, or be edited to accommodate, session-wiki content. Promotion flows one direction only, and only once the knowledge has proved durable and broadly useful — a finding still phrased in terms of this one assignment has not earned promotion yet.

The reference-direction half of this is *The one-way reference rule* at the top of this skill: independence is not achieved if the committed page still ends with "see `__untracked_stuff/<real-scope>/findings/…`". Promote the substance, then cite nothing.

Where the host repo does keep a durable knowledge base, one further constraint applies: it is repo-specific content governed by its own conventions, and **this skill has no authority over it**. Read those conventions before promoting anything into it, and let them win wherever they differ from anything written here.

## Improvements to agent customizations discovered mid-session

Session-wiki work often surfaces a concrete improvement to the files that constitute agent-loaded knowledge and behavior — a skill, an instruction, an `AGENTS.md`, a durable knowledge page. Two rules, neither of which needs any particular workflow to exist:

- **Capture it where you are.** Write the proposed improvement into the scope's `findings/` when you notice it, rather than carrying it in context to the end of the session — where it is among the first things lost to a crash or a compaction.
- **Do not fold it in silently.** Editing an agent-loaded file changes how every future session behaves, so it is reviewed like any other change — see *Proposed commits* above.

Where the host repo has an established workflow for proposing such changes in batches, defer to it; it will own grouping, apply-commands, and review routing. Absent one, prepare the edit in the working tree and hand it off with everything else.

## Relationship (link, don't duplicate)

**This skill has no required companions.** It is complete on its own. Every capability below is optional: where the host repo has one, defer to it instead of restating its rules here; where it does not, nothing in this skill stops working. The names are conventional labels for a *kind* of capability, not a promise that anything by that name is installed.

| Capability, where the host repo has one | What it owns |
|---|---|
| A durable committed knowledge base (an "LLM-wiki") | The repo's compounding, version-controlled knowledge — the same raw→synthesis→index shape as a session-wiki, but permanent and reviewed. It is **repo-specific content with its own conventions, not a skill**: a session-wiki cites it, promotes into it when knowledge has earned it, and never edits it to suit itself. See *Promotion, and independence of durable knowledge* above. |
| A link-checking tool | Mechanized dead-link and structural-conformance checking over scope documents and committed files. |
| A context-resilience convention | Checkpoint-after-dispatch and harvest mechanics that populate the session-wiki. |
| A multi-agent choreography convention | Delegation and context isolation that keep a coordinator's context small. Irrelevant in a single-agent repo. |
| A customization-patch convention | Batched proposal of changes to skills, instructions, and other agent-loaded files. |
