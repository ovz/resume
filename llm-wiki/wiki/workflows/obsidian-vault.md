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
| 🟠 **Amber** | brag entries with `resume-worthy: yes` | Captured and judged promotable, **not yet on the resume**. These are the nodes to move next. |
| 🟢 **Teal** | all other brag entries | Captured. Real evidence, not necessarily resume material. |
| 🟣 **Purple** | `wiki/analysis/` | Durable answers to questions that came up — context, not accomplishments. |
| 🔵 **Steel blue** | `wiki/resume/` | The resume machinery: structure, link conventions, coverage map. |
| 🔵 **Blue** | rest of `wiki/` | Synthesis: domains, entities, workflows, sources. |
| ⚪ **Grey** | rest of `raw/` | Archived sources. |

### What the shapes tell you

- **An orphan brag entry — a teal or amber node floating with no edges — is not in the ledger.** Orphans are deliberately shown for exactly this reason. Every ingested entry is linked from [the brag ledger](../sources/brag-ledger.md) and from [coverage](../resume/coverage.md), so an unlinked entry is one the ingest pass missed. That is the "needs to get properly into the brag ledger" signal, visible without opening anything.
- **A tight cluster is a thread.** Entries cross-link through their `## Related` sections, so work on the same story pulls together. When a new thought arrives, the cluster it lands near is where it belongs; if it lands nowhere, it may be starting a new thread.
- **Amber nodes far from the gold node** are the promotion backlog, at a glance.

### Useful graph filters

Type these into the graph's search box to isolate one view:

| Goal | Filter |
|---|---|
| Just the promotion backlog | `path:llm-wiki/raw/brag [resume-worthy:yes]` |
| One thread only | `[thread:MED]` — swap the code; see [coverage](../resume/coverage.md) |
| One domain | `[domains:"positioning and location"]` |
| Everything captured about a topic | `path:llm-wiki/raw/brag beacon` |
| What is waiting to be filed | `path:llm-wiki/raw/brag/inbox` |

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

**`thread` is the one to get right when adding an entry**, because it is what makes the topic cluster findable later. If nothing fits, that is a signal to open a new thread in the coverage map rather than to force a bad match.

## What the vault deliberately hides

`.obsidian/app.json` filters out repository plumbing so the graph shows the career, not the tooling: the build submodule, scratch directories, agent instruction files, skills, scripts, the compressed board archives, and `llm-wiki/index.md` itself.

**`index.md` is hidden on purpose.** It links to every page, so including it would collapse every cluster into a single star and destroy exactly the structure the graph is for. Navigate by index in the editor; navigate by cluster in the graph.

## Maintenance

- **Adding a property to entries** means updating all of them, plus the template in [brag file workflow](brag-file.md) § *Template*. A property that exists on some entries and not others is worse than no property, because filters silently under-report.
- **Changing a colour group** means updating the table above in the same edit. A legend that disagrees with the graph is how someone concludes the graph is lying.
- **Do not add tags for pipeline state.** The folder is the status for un-ingested notes, and the ledger owns ingest and promotion state. A tag duplicating either would drift silently, and nothing would catch it.
- Vault settings are committed so the vault opens the same way on every machine; per-machine UI state (`workspace.json`, caches, installed plugins) is gitignored.

## Related

- [Brag file workflow](brag-file.md) — capture and ingest, and the entry template.
- [Coverage map](../resume/coverage.md) — the threads, and what has reached the resume.
- [Brag ledger](../sources/brag-ledger.md) — ingest and promotion state per entry.
