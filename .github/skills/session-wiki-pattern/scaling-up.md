---
name: session-wiki-scaling-up
description: "Reference for session-wiki-pattern — machinery that outlives one scope, tracker generation rotation, and scope succession."
---

# Scaling up: machinery, tracker generations, succession

> Companion to [`SKILL.md`](SKILL.md). Load only when a scope **runs code**, has accumulated enough tracker history to need rotating, or is handing work to a successor. A short assignment needs none of it.

## Reusable machinery: the third kind of scope-root material

A mature scope holds three distinct kinds of material, and they obey different rules:

| Kind | Lives in | At succession |
|---|---|---|
| **State** — what is done, what is next | `tasks/` | carried forward (open items only) |
| **Knowledge** — captures, findings, narrative | `session-wiki/` | **cited, never copied** |
| **Machinery** — code the scope runs | a scope-root sibling (`validation/`, `harness/`, …) | **carried forward and split** (see two tiers below) |

Machinery is the one category exempt from cite-don't-copy. Evidence is cited because a second copy of a finding is a second thing to keep true. Machinery must move because a successor scope has to *run* it, and because reaching across a frozen predecessor's directory to import its code makes that predecessor un-freezable — any change to satisfy the successor rewrites the record the predecessor exists to preserve.

## Two tiers: reusable core vs scope-local extension

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

## The engine / extension seam

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

## Promote the core, keep the ticket's part in scratch

What graduates out of scratch is **the reusable core plus the discipline**; what stays is the ticket's own unit. Both halves of that sentence matter — an earlier draft of this skill said "never copy code into a skill", and the very next rollover disproved it: the core belonged under version control, where it could be tested and reviewed, precisely because it had stopped being about one ticket.

The trigger is the **rule of two**: on the second scope that needs it, the core is proven reusable — promote it, with tests. On the first scope, leave it local. Cite the live implementation from the skill as the worked reference; the skill documents the API and the lessons, it does not restate the code.

Before promoting, harvest the predecessors: earlier scopes' notebooks and scripts usually contain techniques and — more valuable — recorded *failures* that the new core should encode. Read the archived and superseded artifacts specifically; they hold the "this did not work, and here is why" that clean current code no longer shows. Every utility promoted this way should carry a one-line docstring naming the scope experience that justifies it; a utility nobody can justify that way is speculation, and speculation is what makes a core hard to change later.

The shape this takes in practice: a single-scope validation harness is carried into its successor scope and split into an `engine.py` plus per-scope suites, so one capture proves both scopes; then, once several earlier scopes' notebooks have been mined for technique, the engine graduates to a version-controlled, unit-tested package hosted inside the skill that owns it, with each scope's harness path-depending on that package. Seam hazards 5 and 8 above are the two that bite during those moves — expect them rather than discovering them.

(Stated without ticket IDs or scope slugs on purpose: this file is version-controlled, and *Session-only identifiers are references too* above forbids labels a fresh-clone reader cannot resolve. The reasoning has to carry itself.)

## Rollover tokenomics

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


## Rotating tracker generations around 60% DONE

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


## Ticket migration (scope succession)

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

