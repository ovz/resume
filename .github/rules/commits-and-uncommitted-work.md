> Shard of the root [`AGENTS.md`](../../AGENTS.md). Load when the task matches its title.

# Agents do not commit, and uncommitted work is the only thing git cannot give back

Sections: [Agents do not commit](#agents-do-not-commit) · [Uncommitted work](#uncommitted-work-is-the-only-thing-git-cannot-give-back)

## Agents do not commit

**Never run `git commit`, `git push`, `git tag`, or any other history-writing command.** Every change in this repository is reviewed by a human before it lands, without exception. Leave the work in the working tree and write the proposed commit message into the session-wiki scope's `commits/` — the `session-wiki-pattern` skill owns that format — then hand off through the tracker; see [`handoffs-and-tracker.md`](handoffs-and-tracker.md). Say what changed and why; one file per proposed commit, naming the exact paths it covers.

`git status`, `git diff`, `git log`, `git show` and other read-only inspection are always fine. So is `git stash` when protecting uncommitted work (below).

## Uncommitted work is the only thing git cannot give back

Everything in this repository is reviewed before it lands, which means the working tree routinely holds hours of work that exists nowhere else. Two rules follow, and both are about the asymmetry rather than the odds:

- **Before overwriting any region of a file that has uncommitted changes, secure a copy.** `git stash` is sanctioned for exactly this; a copy in the session scratch scope works too. Prefer a section-scoped edit to a whole-file write when the file holds in-flight work — restoring one section is recoverable, rewriting a file is not. Verify a restore by equality against the snapshot, never by eye.
- **When an answer could mean two things and one reading destroys work, ask.** "Rewrite it" and "add to it" are the same three words. The cost of asking is one turn; the cost of guessing wrong is unbounded, so the asymmetry decides it and not the probability.
