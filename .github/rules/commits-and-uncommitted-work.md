> Shard of the root [`AGENTS.md`](../../AGENTS.md). Load when the task matches its title.

# Agents do not commit, and uncommitted work is the only thing git cannot give back

Sections: [Agents do not commit](#agents-do-not-commit) · [Uncommitted work](#uncommitted-work-is-the-only-thing-git-cannot-give-back)

## Agents do not commit

**Never run `git commit`, `git push`, `git tag`, or any other history-writing command.** Every change in this repository is reviewed by a human before it lands. This holds without exception, including for changes an agent is confident about and changes the owner appeared to pre-approve in conversation.

What an agent does instead:

1. Leave the work in the working tree, unstaged or staged, and say what changed and why.
2. Write the **proposed commit message** into the session-wiki scratch scope, never into a tracked file and never into the repo. The `session-wiki-pattern` skill owns that scope's layout; commit messages belong alongside its other session artifacts, under a `commits/` directory in the session-wiki. One file per proposed commit, each naming the exact paths it covers.
3. Hand off **through the tracker** — see [`handoffs-and-tracker.md`](handoffs-and-tracker.md). The owner reviews, edits the message if needed, and commits.

`git status`, `git diff`, `git log`, `git show` and other read-only inspection are always fine. So is `git stash` when protecting uncommitted work from a destructive operation.

Proposals stay lean: the ready-to-paste message, plus only what the diff cannot show (a judgement call, something expensive to reverse, a superseded earlier proposal). The owner reads the diff anyway, and long proposals go stale and mislead.

## Uncommitted work is the only thing git cannot give back

Everything in this repository is reviewed before it lands, which means the working tree routinely holds hours of work that exists nowhere else. Two rules follow, and both are about the asymmetry rather than the odds:

- **Before overwriting any region of a file that has uncommitted changes, secure a copy.** `git stash` is sanctioned for exactly this; a copy in the session scratch scope works too. Prefer a section-scoped edit to a whole-file write when the file holds in-flight work — restoring one section is recoverable, rewriting a file is not. Verify a restore by equality against the snapshot, never by eye.
- **When an answer could mean two things and one reading destroys work, ask.** "Rewrite it" and "add to it" are the same three words. The cost of asking is one turn; the cost of guessing wrong is unbounded, so the asymmetry decides it and not the probability.
