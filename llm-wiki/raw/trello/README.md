# Trello board exports

Dated, verbatim snapshots of the owner's own Trello boards, committed for safekeeping at the owner's explicit direction. The boards are the owner's property and hold years of working history that exists nowhere else.

Each snapshot is stored **compressed and checksummed** — see [large imports](../../wiki/workflows/large-imports.md) for why, and for the procedure that produced these files.

## What is here

| File | Board | Snapshot | Original | Archive | sha256 of plaintext (first 16) | Contents |
|---|---|---|---|---|---|---|
| `2026-09-09-r5-jira-board.json.xz` | device programme working board | 2026-09-09 | 5.6 MB | 510 KB | `e0b78b908102c21f` | 1254 cards, 195 lists |
| `2026-09-09-leadership-board.json.xz` | leadership, one-on-ones, quarterly conversations | 2026-09-09 | 6.0 MB | 386 KB | `69d580787a121d72` | 1445 cards, 166 lists |

The hash is of the **uncompressed** JSON, so it stays checkable no matter which compressor version wrote the archive, and confirms any unpacked copy is genuine.

## Reading one

The archives are xz (LZMA2). Nothing needs installing — Python's standard library decodes xz on every platform:

```bash
python3 script/large-import.py unpack llm-wiki/raw/trello/2026-09-09-leadership-board.json.xz --out <somewhere outside the repo>
python3 script/large-import.py verify llm-wiki/raw/trello/2026-09-09-leadership-board.json.xz --sha256 69d580787a121d72
```

`xz -dc`, `unxz -k`, 7-Zip and most desktop archive managers read them too. **Unpack outside the repository**, into a scratch working area — the uncompressed copy is not committed, and a stray one in the working tree is how the corruption described below happened.

## Naming and re-export

`YYYY-MM-DD-<board>-board.json.xz`, dated by the day the export was taken. The owner continues to use these boards and intends to tidy them and re-export later, so **later snapshots sit alongside earlier ones rather than replacing them** — a tidied board loses cards, and the point of a snapshot is that it still holds what the board held that day. Never overwrite an existing snapshot; add a new dated file. The packing tool refuses to overwrite for exactly this reason.

On re-ingest, diff against the previous snapshot rather than re-reading everything: what matters is what is new since the last harvest.

## Why compressed, and one thing that already went wrong

Compression here is not only about size, though 12 MB becoming 900 KB in every clone is the visible part.

The r5-jira snapshot was briefly committed uncompressed, and was found with the string `009-commit-trello-board-snapshots.md` appended to it — a misdirected shell redirection from an unrelated task — leaving a 5.9 MB JSON file that no longer parsed. The recorded checksum is what identified the good copy and made the damage a five-second diagnosis instead of a silent loss. The archives here are compressed so a stray append cannot plausibly land in one, and checksummed so it would be caught if it did.

## Tier: T1 by owner decision, T2 by default rule

These files would ordinarily be **T2, never committed** — they are employer-adjacent working records and they are large. The owner has deliberately downgraded them to T1 for preservation, which is the owner's call to make and nobody else's ([sensitivity tiers](../../wiki/workflows/sensitivity-tiers.md) rules 5 and 6). What that decision does *not* change:

- **Nothing here may be quoted or cited outward.** These files are an archive, not a source to draw public text from. Anything reaching `markdown/` still travels the normal path: a brag entry at T1, then a promotion pass that re-checks the public tier.
- **The contents remain sensitive at T1.** They carry internal ticket identifiers, internal deep links, repository paths, and component-vendor and ODM detail. Those specifics stay in the archive and do not travel into committed entries.
- **This repository must stay private.** These files raise the cost of that assumption being wrong.

## These boards are hand-curated: harvest them fully

The boards are the owner's own notes, written by the owner, about the owner's own working life. **There is nothing in them the owner needs withheld from their professional records.**

That includes the leadership board's one-on-one material, quarterly conversations, promotion discussions and named accounts of how colleagues worked together. Earlier guidance told ingest to take roles and relationships but leave that material behind; that guidance was wrong and has been withdrawn. Those interactions are an integral part of the owner's professional experience — how a team was led, how disagreements resolved, how people were developed — and a record that omits them keeps the artifacts and loses the career.

So: harvest at T1 with names, roles and substance intact, per [sensitivity tiers](../../wiki/workflows/sensitivity-tiers.md) rule 8. The limits that still apply are the ordinary ones — no contact details, and capture is not disclosure: what is recorded here at T1 is a private record, separate from what the owner chooses to say aloud, and colleague names still come out at T0.

## What has been harvested

**2026-09-09** — a first pass produced four brag entries (GitHub Enterprise migration, safety-critical C++ guidelines, Conan cross-build, quarterly-conversation practice) plus roles in professional contacts.

**2026-09-10** — the full ingest, after the restriction above was withdrawn, produced twelve more entries spanning the sensor and dead-reckoning research, product architecture and power budget, the ODM specification work, data-warehouse telemetry, launch readiness, test automation, the FOTA escalation, and the leadership material — upward feedback, meeting facilitation, the performance conversation, Staff Engineer positioning and the mentorship.

The thematic lists are now substantially harvested. What remains is the dated sprint and one-on-one lists, which are a working log useful for corroborating dates rather than a source of new entries. Full state: [`wiki/sources/trello-boards.md`](../../wiki/sources/trello-boards.md).
