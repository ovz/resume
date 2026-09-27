---
cluster: stewardship
fits: [regulated, principal, security, leadership]
status: draft
runtime: "90 s"
---

# I push back on home-made obfuscation in our logs, because a control only counts if someone checks it

## Why I still care

I studied data security before I studied anything else, and the people who taught me were strict about one thing: a control is something you can show to whoever checks it. When a teammate hand-rolls a scheme to hide device identifiers "for privacy", the instinct is good and the work is wasted, and I would rather spend my credibility pointing at the real rulebook than reviewing their cipher.

**Cue:** my January 2025 note, when the enterprise static-analysis question reached my own open-source work — *"I'll see if I could gain some hands-on knowledge on static analysis for C and C++ Best Buy would like us to use."*

## Register

**2020-2026, Best Buy Health**, with the constant thread from the IIT years — the security professional's reading of a system. Plain, never condescending about colleagues with less security training. Lines lifted from the owner's note of 2026-09-24 per [spoken drafts](../../workflows/spoken-drafts.md); the story's one saying is his.

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | A small security one that keeps coming up |
| 1 | Hook | Teammates periodically hand-roll obfuscation for device identifiers and coordinates in logs, and I push back |
| 2 | Stakes | This data really is sensitive — which is exactly why guessing is dangerous |
| 3 | Complication | The instinct is good, and pushing back can sound like not caring about privacy |
| 4 | Move | Three questions: is there a certification document, an audit, or at least our scanner? Keep it simple; find the book |
| 5 | Punchline | Send people to the rulebook before they write the code |
| 6 | Handover | What counts as a control on your team? |

## Narrative — rehearse verbatim

**0 · Offer**
> I have a small security one, because it keeps coming up.

**1 · Hook**
> Every so often someone on my team writes their own obfuscation for device identifiers or coordinates in our logs, in the spirit of protecting personal data. And I push back.
⟨breathe⟩

**2 · Stakes**
> Not because the data isn't sensitive. It is. Precise location is sensitive personal information under privacy law, and on a health device the identifiers matter too. That is exactly why guessing at the answer is a bad idea.

**3 · Complication**
> The instinct is a good one, and pushing back can sound like I don't care about privacy. I do. I majored in data security, and I learned early that compliance skills are powerful — and with that power comes responsibility for using them properly.
⟨breathe⟩

**4 · Move**
> So I ask three questions. Is there a certification document that says what we must do? Is there an audit planned by third-party security professionals? Or at least, will our enterprise static-analysis scanner check it? If nothing checks it, it isn't a control.
> And the home-made version costs a lot. You build it, you test it, and then every diagnosis afterwards works with scrambled data. When the real requirement arrives, compliance costs the same or more, because now someone has to find the guess and undo it.
> The way I put it to myself is: if there is no book with the right answer, the right answer doesn't exist yet. So we keep it simple — no personal data in logs — and we go and find the book.

**5 · Punchline**
> So instead of reviewing somebody's scheme, I send them to the rulebook first — the policy, the standard, the scanner's rule — and then we write the code that satisfies it.
⟨breathe⟩

**6 · Handover**
> I'm curious what counts as a control on your team, and who checks it.

## If they follow up

- **"But aren't device identifiers and coordinates personal data?"** → Yes. California's privacy law treats precise geolocation as sensitive personal information and counts device identifiers as unique identifiers, and HIPAA's de-identification rule lists device identifiers and small geographic areas. That is my point: because they are sensitive, how we treat them belongs to the compliance programme — classification, who can read the logs, how long we keep them — not to whoever writes the log line.
- **"Can a home-made scheme actually make things worse?"** → It can. A static-analysis scanner often recognises sensitive values partly by their names. Rename or scramble a value in a clever way and you may hide it from the tool without protecting it at all.
- **"Where does this come from for you?"** → My master's is in data security, from a department founded by engineers who took security policy and risk seriously. My first job was implementing cryptography for a bank's client system as an undergraduate.
- **"Were you a fan of the scanner?"** → Honestly, I was sceptical of how much of a device team's quarter should go to chasing its findings. But it is a real compliance vehicle, and a hand-rolled scheme is not.

## Proof

The privacy-law and logging rules are public: [Cal. Civ. Code § 1798.140](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.140) (precise geolocation; device identifiers), [45 CFR 164.514](https://www.law.cornell.edu/cfr/text/45/164.514) (safe-harbor identifiers), the [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html). The engineering practice is the owner's recurring account; no single instance is recorded.

## Know it — what stays with me

T1: the scanner is **Checkmarx**; in September 2024 I called the Checkmarx work "not strategic by any measure" and an "arbitrary requirement" in my own notes, and by 2025 I was learning it and raising a security-scan strategy. The values in question are IMEI and latitude/longitude. The teammates are never named, and the story never implies they were careless — the instinct was right, the method was not.

## Sources

- [2025-01-10 Home-made obfuscation versus a compliance vehicle](../../../raw/brag/2025-01-10-pii-obfuscation-pushback-compliance-vehicle.md)
- Cited, not graduated: [2025-01-16 SDK binary hardening](../../../raw/brag/2025-01-16-ccf-sdk-binary-hardening.md)

## Related stories

- [I kept records nobody asked me for](records-nobody-asked-for.md) — stewardship's other registers, including the patch SOP.
