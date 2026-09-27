> Shard of the root [`AGENTS.md`](../../AGENTS.md). Load when the task matches its title.

# Sensitivity — the tiers and the three hard rules

Three tiers govern what may be written where: **T0 public** (the primary resume only), **T1 private repo** (everything else committed), **T2 never committed** (employer-internal material, large binaries). Definitions and promotion rules: [`llm-wiki/wiki/workflows/sensitivity-tiers.md`](../../llm-wiki/wiki/workflows/sensitivity-tiers.md).

Three hard rules apply everywhere:

- No committed file may reference a path under `__untracked_stuff/`. A committed file must stand alone in a fresh clone; a pointer into scratch is dead on arrival for every other reader, and dead *silently*. Describe the shape of the scratch convention if you must, but never a concrete scratch path. **The one exception is the root `TODO.md`**, the owner's worklist: it names every session-wiki assignment tracker that still holds action items — in this repository and in its [sibling career repositories](../../llm-wiki/wiki/workflows/career-repositories.md) — so that `git diff` shows what is outstanding. An agent adds the line when a tracker gains owner items and removes it when none remain. `TODO.md` is otherwise the owner's scratch space, and the owner may delete a trace whenever they like. No other committed file may cite those paths.
- Third-party contact details are never copied out of `markdown/Oleg.Zhylin.professional.references.md`.
- Colleague names, roles and the substance of working relationships are recorded in full at T1 — they are the professional record, not an aside to it. Capture is not disclosure: what the owner chooses to say in an interview is a separate judgement, and names still come out at T0.
