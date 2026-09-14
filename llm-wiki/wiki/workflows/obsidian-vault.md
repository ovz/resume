# The Obsidian vault: where to dump, where to look

> **Doc type:** how-to
>
> How the vault is set up so a thought that arrives at a random moment has an obvious destination, and so "what do I already have on this?" is answerable in seconds. Audience: the owner at the keyboard; agents changing `.obsidian/` or the brag entry schema.

## The loop this is built for

```
a topic hits your mind
        │
        ▼
  is it already a thing?  ──no──▶  drop it in raw/brag/inbox/   ← the RED cluster
        │ yes                       (any filename, any shape)
        ▼
  open the entry, append          ← the TEAL / AMBER cluster
        │
        ▼
  next ingest pass folds it into the wiki and the coverage map
        │
        ▼
  promotion pass moves it to markdown/   ← the GOLD node
```

Two rules make this work, and neither is about Obsidian:

- **The inbox folder is the status.** A note in `raw/brag/inbox/` has not been ingested; an empty inbox means everything has. Never leave an ingested note there "just in case" — that breaks the only signal the folder carries.
- **Never delete detail on the way in.** Capture is cheap and re-capture is impossible. See [brag file workflow](brag-file.md).

## Reading the graph

Open the graph view. Colour is the pipeline stage:

| Colour | What it is | What it means |
|---|---|---|
| 🔴 **Red-orange** | `raw/brag/inbox/` | **Un-ingested. This is where you dump.** A red node is a to-do. |
| 🟡 **Gold** | `markdown/` | The outward-facing resume — the destination everything is aiming at. |
| 💚 **Vivid green** | `wiki/dream-jobs/` with `origin: owner` | **The owner's own dream jobs.** The brightest nodes in the vault, deliberately: this is where the career is pointed. |
| 🟩 **Sage green** | rest of `wiki/dream-jobs/` | **Agent-suggested candidate directions.** Same family, lower confidence — the colour says "someone else's idea" at a glance. |
| 🩷 **Magenta** | `wiki/stories/` | **Told-able stories** — what you reread before an interview or an event. |
| 🟠 **Amber** | brag entries with `resume-worthy: yes` | Captured and judged promotable, **not yet on the resume**. These are the nodes to move next. |
| 🟢 **Teal** | all other brag entries | Captured. Real evidence, not necessarily resume material. |
| 🟣 **Deep purple** | `wiki/analysis/employers/` | Employer research — past employers and prospective ones, one dated page per piece of research. |
| 🟣 **Purple** | `wiki/analysis/` | Durable answers to questions that came up — context, not accomplishments. |
| 🔵 **Steel blue** | `wiki/resume/` | The resume machinery: structure, link conventions, coverage map. |
| 🔵 **Blue** | rest of `wiki/` | Synthesis: domains, entities, workflows, sources. |
| ⚪ **Grey** | rest of `raw/` | Archived sources. |

**The main graph hides graduated entries.** Its filter is `-[storied]`: once an entry's substance is told in a story, it steps out of the working view. It stays one move away — the story's local graph, a search for `[storied]`, or the catalogue. See [brag stories](brag-stories.md).

### What the shapes tell you

- **An orphan brag entry — a teal or amber node floating with no edges — is not in the ledger.** Orphans are deliberately shown for exactly this reason. Every ingested entry is linked from [the brag ledger](../sources/brag-ledger.md) and from [coverage](../resume/coverage.md), so an unlinked entry is one the ingest pass missed. That is the "needs to get properly into the brag ledger" signal, visible without opening anything.
- **A tight cluster is a thread.** Entries cross-link through their `## Related` sections, so work on the same story pulls together. When a new thought arrives, the cluster it lands near is where it belongs; if it lands nowhere, it may be starting a new thread.
- **Amber nodes far from the gold node** are the promotion backlog, at a glance.
- **A green node with few edges is a dream job asserted rather than sourced.** Candidate pages link to the brag entries behind them, so a well-grounded direction sits visibly on top of its evidence and a thin one floats. That is the same signal the `evidence:` grade carries in text, and it is why the [hub](../dream-jobs/dream-job-hub.md) is worth opening from the graph rather than from the index.

### Useful graph filters

Type these into the graph's search box to isolate one view:

| Goal | Filter |
|---|---|
| Just the promotion backlog | `path:llm-wiki/raw/brag [resume-worthy:yes]` |
| One thread only | `[thread:MED]` — swap the code; see [coverage](../resume/coverage.md) |
| One domain | `[domains:"positioning and location"]` |
| Everything captured about a topic | `path:llm-wiki/raw/brag beacon` |
| What is waiting to be filed | `path:llm-wiki/raw/brag/inbox` |
| Every entry that has graduated into a story | `[storied]` |
| Stories for one kind of conversation | `[fits:embedded]` — swap the need |
| One cluster as a sub-graph | open its hub, e.g. `stories/positioning.md`, then *Open local graph* at depth 2 |
| Only the owner's own dream jobs | `path:llm-wiki/wiki/dream-jobs [origin:owner]` |
| Dream jobs pursuable on today's record | `[horizon:now]` — swap for `build` or `stretch` |
| Dream jobs whose fit is thinly evidenced | `[evidence:thin]` |
| One dream job and the evidence under it | open its page, then *Open local graph* at depth 1 |

## Entry properties

Brag entries carry YAML frontmatter, so Obsidian indexes them as **properties** — visible in the right-hand panel, searchable with `[key:value]`, and usable in graph groups:

| Property | Purpose |
|---|---|
| `title` | The headline, repeated from the `#` heading (property views show this; the graph shows the filename) |
| `date` | When the accomplishment happened — a range is fine, so it is a string not a date type |
| `thread` | The [coverage](../resume/coverage.md) thread code — the topic cluster this belongs to |
| `domains` | A list, from [accomplishments by domain](../concepts/accomplishments-by-domain.md) |
| `context` | Employer / project / team, as publicly describable |
| `sensitivity` | `private-repo` or `public-friendly` — see [sensitivity tiers](sensitivity-tiers.md) |
| `resume-worthy` | `yes` / `maybe` / `no` — the owner's judgement, and what drives the amber colour |
| `storied` | *Added only at graduation.* The stories this entry now lives in, as a list of paths. Its presence is what the main graph filters on, so **never add it empty** — an empty `storied:` hides an entry that has not graduated |

Stories carry their own three properties — `cluster`, `fits`, `status` — described in [brag stories](brag-stories.md).

**Dream-job pages carry six**, described in the [hub](../dream-jobs/dream-job-hub.md): `dream-job` (the stable `DJ-n` id), **`origin`** (`owner` or `suggested` — what the two green colours group on, and the one property an agent may never change to `owner`), `specialization` (`established` or `emerging`), `evidence` (`strong` / `moderate` / `thin`), `horizon` (`now` / `build` / `stretch`), and `status` (`candidate` / `pursuing` / `parked` / `retired`). They reuse the stories' `fits` vocabulary so a candidate and the stories that serve it can be found with the same search.

**`thread` is the one to get right when adding an entry**, because it is what makes the topic cluster findable later. If nothing fits, that is a signal to open a new thread in the coverage map rather than to force a bad match.

## What the vault deliberately hides

`.obsidian/app.json` filters out repository plumbing so the graph shows the career, not the tooling: the build submodule, scratch directories, agent instruction files, skills, scripts, the compressed board archives, and `llm-wiki/index.md` itself.

**`index.md` is hidden on purpose.** It links to every page, so including it would collapse every cluster into a single star and destroy exactly the structure the graph is for. Navigate by index in the editor; navigate by cluster in the graph.

## Maintenance

- **Adding a property to entries** means updating all of them, plus the template in [brag file workflow](brag-file.md) § *Template*. A property that exists on some entries and not others is worse than no property, because filters silently under-report.
- **Changing a colour group** means updating the table above in the same edit, and **in the same order** — Obsidian applies the first matching group, so a specific query (`… [origin:owner]`, `… [resume-worthy:yes]`, `wiki/analysis/employers`) must sit above the general one it refines. A legend that disagrees with the graph is how someone concludes the graph is lying.
- **`.obsidian/graph.json` is the committed source of these colours and of the main graph's `-[storied]` filter.** Per-machine UI state in `workspace.json` is gitignored and can hold a *stale copy* of graph settings for a graph pane that is already open, so after this file changes, close the graph pane and reopen it before concluding a colour did not apply.
- **Do not add tags for pipeline state.** The folder is the status for un-ingested notes, and the ledger owns ingest and promotion state. A tag duplicating either would drift silently, and nothing would catch it.
- Vault settings are committed so the vault opens the same way on every machine; per-machine UI state (`workspace.json`, caches, installed plugins) is gitignored.

## Related

- [Brag file workflow](brag-file.md) — capture and ingest, and the entry template.
- [Coverage map](../resume/coverage.md) — the threads, and what has reached the resume.
- [Brag ledger](../sources/brag-ledger.md) — ingest and promotion state per entry.
- [Dream-job hub](../dream-jobs/dream-job-hub.md) — the green cluster, and what its properties mean.
