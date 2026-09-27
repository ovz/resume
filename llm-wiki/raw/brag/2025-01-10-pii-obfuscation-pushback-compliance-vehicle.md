---
title: "Pushed back on home-made obfuscation of device identifiers and coordinates: compliance has a document, an auditor and a scanner, or it is not compliance"
date: "recurring, circa 2024 to 2026 (no single dated instance in the record)"
thread: RSK
domains:
  - "Risk management and compliance"
  - "Security, cryptography, licensing"
context: "Best Buy Health — device software and its logs; teammates with less security training; the enterprise static-analysis scanner"
sensitivity: private-repo
resume-worthy: maybe
storied:
  - "stewardship/a-control-someone-checks"
---

# Pushed back on home-made obfuscation of device identifiers and coordinates: compliance has a document, an auditor and a scanner, or it is not compliance

## What I did — the owner's account (2026-09-24, verbatim)

> I am a Data Security major and I internalized a thing or two about compliance at a young age. Compliance skills are powerful and "power and responsibility" metaphor works good here. Put another story draft that my less security educated team members still periodically put together ad hoc IMEI, lat/lon numbers, etc obfuscations in the spirit of PII  protection. I always push back that we don't have a concrere certification document , no audit by 3rd party security professionals planned etc. Even our enterprise one Checkmarkx scanner would be some real compliance vehicle. Just because you think this sounds like compliance doesn't help during static analysis, audit etc. So keep it simple, practice yagni, don't put PII into logs, but IMEI, lat/lon etc have some technical meaning and obfuscating them unnecessarily creates work to build obfuscation, test obfuscation itself and use obfuscated data and actual compliance process will still cost the same or even more because one guessed what the right answer is despite in this case if there is no book with righ answer the right answer doesn't exist.

This is the entry the [2025-01-16 binary-hardening entry](2025-01-16-ccf-sdk-binary-hardening.md) said this judgement deserved.

## The argument, as he makes it

1. **A control is only a control if something checks it.** A certification document, a third-party audit, or at minimum the enterprise static-analysis scanner. A scheme a developer invents because it "sounds like compliance" is checked by none of them.
2. **Home-made obfuscation has a cost with no offsetting credit.** Build it, test it, and then work with obfuscated data in every diagnosis — and when the real requirement arrives, the compliance work costs the same or more, because the guess has to be found and undone.
3. **Keep the simple rule.** Do not put personal data in logs. Identifiers and coordinates are technically meaningful on a device; changing them ad hoc damages diagnosis without satisfying any auditor.
4. **His rule, in his words:** *if there is no book with the right answer, the right answer doesn't exist* — meaning, find the book (the standard, the policy, the scanner's rule) before writing the code.

## Where it meets the industry's own rules — and the nuance to carry

The position is conservative in the right direction, and it needs one clarification so it is never heard as "identifiers are not sensitive". **They are sensitive.** California's privacy law counts precise geolocation within a 1,850-foot radius as *sensitive* personal information and lists device identifiers among unique identifiers ([Cal. Civ. Code § 1798.140](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.140)); HIPAA's de-identification safe harbor lists "device identifiers and serial numbers" and geographic subdivisions smaller than a state ([45 CFR 164.514](https://www.law.cornell.edu/cfr/text/45/164.514)). OWASP's logging guidance says sensitive personal data should usually not be recorded directly but removed, masked, sanitized, hashed or encrypted, and that a log must not hold data of a higher classification than the logging system is allowed to store ([OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)). And enterprise scanners have a rule for exactly this — Checkmarx's "privacy violation" query traces sensitive values, largely recognised by name, into logging calls.

So the honest shape of his argument is: **because these values are sensitive, the treatment belongs to the compliance programme — the data classification, the log system's access and retention, the scanner's rule — and not to whichever developer happens to be writing the log line.** A guessed scheme can even be worse than none: it can hide a value from a name-based scanner without protecting it.

## Why it matters

It is the security professional's reading applied to everyday code: know which requirement you are satisfying and who will check it, and do not buy the appearance of compliance with engineering time. It connects the Data Security degree to current work without claiming a role he has not held.

## Skills demonstrated

Security and privacy compliance reasoning; distinguishing a control from its appearance; YAGNI applied to security; privacy-law and logging-standard awareness; explaining a security position to engineers without formal training.

## What was blocked, cut short, or wrong

- **It recurs.** "Still periodically put together" — the pushback has to be made again, which says it has not become a team rule.
- **He was sceptical of the scanner's prioritisation at the time.** In September 2024 he wrote that Checkmarx work was "not strategic by any measure"; by January 2025 he was learning the static-analysis tool Best Buy wanted used, and in late 2025 raised a security-scan strategy. Both are true: the scanner is the real compliance vehicle, and chasing its findings was not always the best use of a device team's quarter.

## Evidence

The owner's statement above and in the 2025-01-16 entry. Leadership board (committed Trello snapshot): the Checkmarx cards of 2024-09-11, the static-analysis note of 2025-01-10, and the security-scan strategy card of 2025-09-30. Web sources linked inline, fetched 2026-09-24 (the Checkmarx rule description from a search summary, not a vendor page).

## Evidence limitations

No single instance — a pull request, a review comment, a date — is recorded. Outward, tell it as a recurring judgement with its reasoning, never as a story about a named colleague.

## Related

- [2025-01-16 CCF SDK binary hardening](2025-01-16-ccf-sdk-binary-hardening.md) — where this position was first captured.
- [2025-11-13 Column Mapping Framework](2025-11-13-column-mapping-framework-alation-data-governance.md) — the governance work that reached Cyber Security leadership.
- [2023-09-30 security patch management SOP](2023-09-30-security-patch-management-sop-and-vendor-engagement.md) — the same discipline at fleet level: find the standard (NIST) first.

## Record history

- 2026-09-24: created from the owner's TODO note of 2026-09-24 (verbatim above), with industry grounding fetched the same day. Filed under 2025-01-10, the first dated note of him engaging with the enterprise static-analysis scanner; the judgement itself recurs across 2024–2026.
- 2026-09-24: graduated into story `stewardship/a-control-someone-checks`; `storied` property added, body untouched.
