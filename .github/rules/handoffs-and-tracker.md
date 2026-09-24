> Shard of the root [`AGENTS.md`](../../AGENTS.md). Load when the task matches its title.

# Hand-offs go in the assignment tracker, never in the chat response

**Anything the owner has to do, decide, verify, or answer is written into the session-wiki's `tasks/assignment_tracker.md`, under an `## Open for the owner` heading, at the moment it is discovered.** Not at the end of the session, and not into the chat.

The chat response says *that* there are open items and where they live. It does not restate them.

Why the rule is absolute:

- **A chat response is not durable.** It disappears with the session, it is not on disk, it cannot be reopened in the editor, and a fresh session cannot read it. An item that exists only in a chat message is an item that will be lost — silently, because nothing reports it missing.
- **The tracker is the resume token.** It is the first thing any session reads. Putting the owner's items anywhere else guarantees the next agent does not know they are outstanding.
- **The owner works from one list.** Two lists — one in the tracker, one scrolled past in a terminal — is worse than either alone, because neither is trustworthy.

A response that ends with a list of things for the owner to do is a defect, even when the list is correct. The correct ending points at the tracker.

If work is under way and no scope exists yet, that is the signal to create one (`session-wiki-pattern` skill), not a licence to hand off in chat.

### Keeping the tracker true

The mechanics are the `session-wiki-pattern` skill's, § *The tracker*. Four rules are this repository's policy:

- **Done items leave the tracker promptly**, into a done-batch file the tracker links — one line per batch, at most twenty, the oldest rotated out.
- **Owner items are re-judged on every resume, before new work.** Read the cheap evidence first — `git log --oneline` since the tracker's date, `git show --stat` only on commits whose subject looks relevant, `git status --short`, `git diff --cached --stat`, `script/linkedin-sync.py status` — then move each owner item that is done or obsolete into a done batch, **with the evidence that decided it**. When the evidence is ambiguous, leave the item open and say what would settle it.
- **Commit guides are owner assignments.** Every proposed commit file appears in the tracker's owner items, with its review guidance, until `git log` shows it landed — partially landed ones say what is still outstanding.
- **`TODO.md` points the owner at trackers that hold owner items** and nothing more. It is the owner's scratch file; an agent does not re-add a trace the owner deleted unless new owner items have appeared since.

Scratch is this workstation's worklog and may grow as it needs to; committed files are the garden of knowledge and hold only what has reached top quality.
