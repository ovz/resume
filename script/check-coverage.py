#!/usr/bin/env python3
"""Validate the sharded coverage map without modifying repository files."""

import argparse
from collections import Counter, defaultdict
from pathlib import Path
import re
import sys


CLAIM = re.compile(r"^\| (?:~~)?`([A-Z]+)-(\d+)`[^|]*\|([^|]+)\|([^|]+)\|$")
THREAD = re.compile(r"^### ([A-Z]+) [—-] ")
LINK = re.compile(r"\]\(([^)]+)\)")
WEIGHTS = {"in": 1, "partial": 0.5, "absent": 0}


def score(counts):
    return sum(counts[state] * weight for state, weight in WEIGHTS.items())


def denominator(counts):
    return sum(counts[state] for state in WEIGHTS)


def check(root):
    base = root / "llm-wiki/wiki/resume"
    map_path = base / "coverage.md"
    text = map_path.read_text()
    errors = []
    warnings = []
    totals = Counter()
    worthy = Counter()
    provisional = Counter()
    seen_claims = set()
    seen_threads = set()
    seen_paths = set()
    ledger_dates = defaultdict(list)
    ledger_path = root / "llm-wiki/wiki/sources/brag-ledger.md"
    for line in ledger_path.read_text().splitlines():
        if not line.startswith("| ["):
            continue
        fields = [field.strip() for field in line.strip("|").split("|")]
        target = LINK.search(fields[0])
        if target:
            entry = (ledger_path.parent / target[1]).resolve()
            ledger_dates[entry.name[:10]].append((fields[3], entry.exists()))

    if any(CLAIM.match(line.strip()) for line in text.splitlines()):
        errors.append("coverage.md must route to claims, not contain them")
    for line in text.splitlines():
        if not line.startswith("| ["):
            continue
        fields = [field.strip() for field in line.strip("|").split("|")]
        if len(fields) != 5:
            errors.append(f"Invalid shard row: {line}")
            continue
        target = LINK.search(fields[0])
        if not target:
            errors.append(f"Missing shard link: {line}")
            continue
        path = (base / target[1]).resolve()
        if path in seen_paths:
            errors.append(f"Duplicate shard: {target[1]}")
            continue
        seen_paths.add(path)
        if not path.is_file():
            errors.append(f"Missing shard: {target[1]}")
            continue
        contents = path.read_text()
        counts = Counter()
        thread_counts = defaultdict(Counter)
        thread_headers = {}
        thread = None
        for row in contents.splitlines():
            heading = THREAD.match(row)
            if heading:
                thread = heading[1]
                if thread in seen_threads:
                    errors.append(f"Duplicate thread: {thread}")
                seen_threads.add(thread)
                thread_counts[thread]
            if row.startswith("**Thread coverage:"):
                thread_headers[thread] = row
            claim = CLAIM.match(row.strip())
            if not claim:
                if re.match(r"^\| (?:~~)?`[A-Z]+-\d+`", row):
                    errors.append(f"Malformed claim: {row}")
                continue
            code, number, source, status = claim.groups()
            claim_id = f"{code}-{number}"
            state = status.strip().strip("*").split()[0]
            if claim_id in seen_claims:
                errors.append(f"Duplicate claim: {claim_id}")
            seen_claims.add(claim_id)
            if code != thread:
                errors.append(f"{claim_id} is outside its owning thread")
            if state not in {*WEIGHTS, "held", "struck"}:
                errors.append(f"Invalid status for {claim_id}: {state}")
                continue
            counts[state] += 1
            thread_counts[code][state] += 1
            if source.strip().startswith("owner,"):
                continue
            entries = ledger_dates.get(source.strip(), [])
            classifications = {entry[0] for entry in entries}
            if len(classifications) != 1:
                errors.append(f"Ambiguous or missing ledger classification: {claim_id}")
            elif classifications == {"yes"}:
                worthy[state] += 1
                if any(not entry[1] for entry in entries):
                    provisional[state] += 1
        expected_codes = {code.strip() for code in fields[1].split(",")}
        if expected_codes != set(thread_counts):
            errors.append(f"Thread routing mismatch: {target[1]}")
        for code, current in thread_counts.items():
            header = thread_headers.get(code, "")
            fraction = re.search(r"\(([\d.]+) of (\d+)", header)
            if not fraction or (float(fraction[1]), int(fraction[2])) != (score(current), denominator(current)):
                errors.append(f"Thread subtotal mismatch: {code}")
        expected_fraction = f"{score(counts):g} / {denominator(counts)}"
        if fields[3] != expected_fraction or fields[4] != str(counts["absent"]):
            errors.append(f"Shard subtotal mismatch: {target[1]}; expected {expected_fraction}, {counts['absent']} absent")
        totals.update(counts)

    for path in (base / "coverage").rglob("*.md"):
        if any(CLAIM.match(line.strip()) for line in path.read_text().splitlines()) and path.resolve() not in seen_paths:
            errors.append(f"Unrouted claim shard: {path.relative_to(base)}")
    if not seen_paths:
        errors.append("No coverage shards found")
    for label, counts in [("All promotable claims", totals), ("Claims from entries marked", worthy)]:
        row = next((line for line in text.splitlines() if line.startswith(f"| {label}")), "")
        fraction = re.search(r"([\d.]+) of (\d+) claims", row)
        if not fraction or (float(fraction[1]), int(fraction[2])) != (score(counts), denominator(counts)):
            errors.append(f"Headline mismatch: {label}")
    for path in [map_path, base / "coverage-history.md", *(base / "coverage").rglob("*.md")]:
        lines = len(path.read_text().splitlines())
        if lines > 1024:
            errors.append(f"Over 1024-line ceiling: {path.relative_to(base)} ({lines})")
        elif lines > 500:
            warnings.append(f"Over preferred 500 lines; review sharding: {path.relative_to(base)} ({lines})")
    for message in warnings:
        print(f"WARN: {message}")
    for message in errors:
        print(f"FAIL: {message}")
    print(f"{len(seen_paths)} shards; {len(seen_threads)} threads; {len(seen_claims)} rows; "
          f"{totals['in']} in / {totals['partial']} partial / {totals['absent']} absent / "
          f"{totals['held']} held / {totals['struck']} struck")
    print(f"Coverage: {score(totals):g}/{denominator(totals)}; "
          f"worthy (ledger): {score(worthy):g}/{denominator(worthy)}")
    if provisional:
        print(f"GAP: worthy totals include {score(provisional):g}/{denominator(provisional)} "
              "from unavailable source entries; classification comes from the ledger")
    print("Coverage structure/counts " + ("FAIL" if errors else "PASS"))
    return 1 if errors else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    sys.exit(check(args.root.resolve()))