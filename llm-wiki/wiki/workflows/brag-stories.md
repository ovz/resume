# Brag stories — graduating entries, and reading lists

> **Doc type:** how-to
>
> How brag entries graduate into told-able **stories**, how the Obsidian vault shows each stage, and how to pull a reading list before an interview, a networking event or a conversation with an employer. Audience: the owner preparing to talk about his work; agents asked to write a story or produce a reading list. Capture and ingest, which this builds on, are [brag-file.md](brag-file.md).
>
> **Read [voice and prominence](voice-and-prominence.md) first.** This page owns a story's *structure*; that one owns its *voice* — which era register it is told in, how loudly its claim may be made, and how to handle work that was blocked or never shipped. A story that follows the six beats below in the wrong register, or that overclaims, is worse than no story.

## Three stages, and where each shows

| Stage | What it is | Where | In the main graph? |
|---|---|---|---|
| **Captured** | A note in any shape, not yet an entry | `raw/brag/inbox/` | Yes — the loudest colour |
| **Ingested** | A dated entry, folded into the synthesis and the coverage map | `raw/brag/` | **Yes** — this is the working set |
| **Storied** | An entry whose substance now lives in at least one story | `raw/brag/`, carrying a `storied:` property | **No** — on demand only |

A **story is not a longer entry.** An entry is the record of one accomplishment, written so nothing is lost — immutable history. A story is written to be *told*: to a kind of listener, at a length, usually drawing on several entries. It is synthesis, so the repo's rule holds — a story is a rewrite, never a copy.

**Graduating an entry does not edit it.** The body stays exactly as recorded. The only change is one metadata property naming the story that now carries it, which is what lets the vault step it out of the way.

## A story's shape: structure first, then the words

Stories live in `wiki/stories/<cluster>/<slug>.md`, beside a hub note `wiki/stories/<cluster>.md` for the cluster.

**The structure is written before the narrative, and it is not a draft of it.** The beats say what each part of the story is *for*; the narrative is then written to be said aloud, word for word, and rehearsed that way. Writing the words first produces prose that reads well and speaks badly. Writing the beats first produces a story that survives being interrupted, cut short, or told to the wrong listener — because you can drop detail and still land every beat.

### The beats

Six beats carry a story. None of them is optional; everything else is.

| # | Beat | Its job |
|---|---|---|
| 0 | **Offer** | The sentence that proposes the story when nobody asked a question. "There's one from the 2019 recall I still think about." Skip it when answering a direct question. |
| 1 | **Hook** | Buys attention in one sentence. A fact, a number or a contradiction — never a preamble. |
| 2 | **Stakes** | Why it mattered, in terms the listener already cares about. |
| 3 | **Complication** | What made it hard. This is the reason there is a story at all. |
| 4 | **Move** | What you did — the part only you can tell. |
| 5 | **Punchline** | The payoff, said flat. No adjectives; the fact is the applause. |
| 6 | **Handover** | A door for the listener: a question back, or an invitation to go deeper. |

Everything between the beats is **detail**, and detail is droppable *by design*. Each optional line is written so that removing it costs nothing but a breath — which is exactly what replaces it. A two-minute telling and a forty-second telling are the same six beats with different amounts of detail, not two different stories.

### Writing the narrative

- **Pick the era register before the first line.** The 1997 cryptographer and the 2026 architecture owner do not sound alike, and should not — [voice and prominence](voice-and-prominence.md) § *The registers, era by era*.
- **Say every line out loud as you write it.** If it cannot be said in one breath, it is two lines or it is cut.
- **Every phrase does one of three jobs**: spark interest, deliver a punchline, or set one of those up. A line that only informs is detail — mark it optional or delete it.
- **Short declaratives project confidence.** Explaining why something mattered twice projects the opposite.
- **Numbers land bare.** "Forty-four thousand devices" — not "approximately 44,300 units".
- **Present tense for the moment you want to relive**: "I can still see the graph." That is what makes it sound like memory rather than recitation, and it is what puts *you* back in the room while you tell it.
- **Banned openers**: "So basically…", "It's kind of a long story", "I was lucky…", "I don't know if this is interesting, but…". Each one tells the listener not to lean in.
- **End on the handover**, so the story does not need applause to finish.

### Notation

| Mark | Meaning |
|---|---|
| `> …` | Spoken verbatim. Rehearse this text exactly. |
| `*(optional)* …` | Detail. Drop it freely — the drop is a breath, not a stumble. |
| `⟨breathe⟩` | Stop. In and out. The pause is part of the telling, not a gap in it. |

### Template

```markdown
---
cluster: positioning
fits: [embedded, firmware, debugging]
status: draft            # draft | rehearsed
runtime: "2 min"         # the full telling, spoken
---

# <The claim, as a sentence>

## Why I still care
<Two lines, never spoken. What it felt like, what I was afraid of, what I was proud of.
Read this before rehearsing: it is what makes the telling sound like something you
cherish rather than something you memorised.>

## Structure
| # | Beat | In this story |
|---|---|---|
| 0 | Offer | <how I raise it unprompted> |
| 1 | Hook | <the one sentence> |
| 2 | Stakes | <why it mattered> |
| 3 | Complication | <what made it hard> |
| 4 | Move | <what I did> |
| 5 | Punchline | <the payoff> |
| 6 | Handover | <the door I leave open> |

## Narrative — rehearse verbatim

**0 · Offer**
> <spoken>

**1 · Hook**
> <spoken>
⟨breathe⟩

**2 · Stakes**
> <spoken>
*(optional)* <detail that can go>

**3 · Complication**
> <spoken>
⟨breathe⟩

**4 · Move**
> <spoken>
*(optional)* <detail that can go>

**5 · Punchline**
> <spoken>
⟨breathe⟩

**6 · Handover**
> <spoken>

## If they follow up
- **"<likely question>"** → <one-line answer>

## Proof
<Numbers, public records, anything a listener could check.>

## Know it — what stays with me
<T1: names, internal detail, the real reasons. For answering follow-ups, never for saying.>

## Sources
- [<entry>](../../../raw/brag/<entry>.md)

## Related stories
```

`fits` is how a story is found later: the kinds of role, conversation or question it serves. Keep the vocabulary small and reuse it — `embedded`, `firmware`, `architecture`, `principal`, `debugging`, `crisis`, `leadership`, `vendor`, `product`, `regulated`, `data`, `ai`, `integration`.

The two tier sections are load-bearing. **Say it** is what goes in the room; **Know it** is what makes a follow-up question safe to answer without disclosing anything. See [sensitivity tiers](sensitivity-tiers.md) — capture is not disclosure.

## Graduating entries into a story

1. **Pick or open a cluster.** A cluster is a set of stories a listener would ask about together. Its hub note lists the planned and written stories and the entries behind each. Coverage threads are a good first cut, but a cluster is shaped for telling, not for gap-counting.
2. **Write the story** from the template, linking every entry it draws on under *Sources*.
3. **Mark each source entry.** Add `storied:` to its frontmatter — a list of story paths, e.g. `storied: [positioning/home-away-kept-simple]` — and a `## Record history` line. It is the one property that changes after capture, alongside `thread`; the body is never touched. **Never add it empty:** the main graph tests whether the property exists, so an empty `storied:` hides an entry that has not graduated.
4. **Update the hub's table and the [story map](../stories/story-map.md).**

An entry may feed several stories; list them all. Nothing here touches the resume — promotion to `markdown/` stays the [update workflow](../resume/update-workflow.md).

## Reasoning about stories in Obsidian

Obsidian has no named sub-graphs. It has three things that add up to one: graph **filters and colour groups that accept the full search syntax**, a per-note **local graph** with a depth control, and **Bases** tables over properties. Each is a documented core feature.

- **The main graph is the working set.** Its filter is `-[storied]`, so every graduated entry drops out and what remains is stories, synthesis, and entries still waiting to be told. Stories are their own colour group — see [obsidian-vault.md](obsidian-vault.md).
- **A hub's local graph is the cluster's sub-graph.** Open `stories/positioning.md` and run *Open local graph*. Depth 1 shows its stories; depth 2 adds the entries behind them. The local graph has its own settings panel; if graduated entries are hidden there, clear its filter field — the main graph is unaffected.
- **A story's local graph is its evidence.** The same move one level down: the story and the entries it graduated.
- **The raw, on demand.** Search `[storied]` lists every graduated entry; search `[fits:embedded]` finds the stories for an embedded conversation.
- **The catalogue.** [`stories.base`](../stories/stories.base) is a table of every story grouped by cluster; [`brag-entries.base`](../stories/brag-entries.base) lists every entry grouped by thread. Add or reorder columns — `fits`, `status`, `storied` — in the table itself; Obsidian writes the choice back into the file.

## Reading lists

A reading list is the three to seven stories worth rereading before one conversation, in order, each with the angle to tell it from. More than seven is not a reading list.

**Asking an agent.** Name the target — an employer, an event, a role description. The agent:

1. **Establishes the target.** Employer research lives at `wiki/analysis/employers/<employer>/YYYY-MM-DD-<subject>.md` — dated, because research goes stale. If none exists and the target matters beyond one conversation, it writes one.
2. **Lists what the target screens for** — three to six needs, in the target's own words where it can find them.
3. **Matches needs to stories** by `fits` and by cluster, preferring `status: ready`.
4. **Orders them**: strongest evidence first, then recency.
5. **Writes, for each:** the story link, its one-breath line, and the angle for this listener.
6. **Adds the context the conversation will need** — the employer-context page if "why are you leaving?" is likely, and the resume block the listener has probably read.
7. **Keeps the list in the session scratch scope.** A reading list is for one conversation and goes stale with it; only durable employer research belongs in `wiki/analysis/employers/`.

**Doing it yourself.** Open the story map, or `stories.base`, and filter by `fits`. Or search `[fits:<need>]` and open each hit's local graph.

## Related

- [Voice and prominence](voice-and-prominence.md) — the register to tell it in, the prominence it earns, and how to answer what happened to work that stopped.
- [Brag file workflow](brag-file.md) — capture and ingest, the stages before this.
- [Story map](../stories/story-map.md) — every cluster and its hub.
- [Obsidian vault](obsidian-vault.md) — the graph filter, colours and properties.
- [Coverage map](../resume/coverage.md) — the threads that seed clusters.
