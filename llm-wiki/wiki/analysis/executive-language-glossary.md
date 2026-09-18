# Executive language — a glossary for reading the employer record

> **Doc type:** reference
>
> Plain-English definitions of the financial and corporate vocabulary that appears in this repository's employer material. The owner is an engineer, not a finance professional; this page exists so that "a $475 million goodwill impairment" reads as a fact with a meaning rather than as executive noise. Audience: the owner preparing to discuss an employer's public record; agents writing employer analysis. Tier **T1** — everything here is public or definitional.

## How to use it

Link a term here on **first use** in an analysis page, and only elaborate inline when the meaning changes the argument. The test: if a sentence works for a reader who does not know the term, link it; if the sentence *depends* on knowing it, say it in one clause and link as well.

## Money that was spent

**Acquisition price.** What the buyer paid, usually stated as cash or shares. Best Buy acquired GreatCall for **$800 million in cash** (announced 15 Aug 2018, from private-equity owner GTCR, with more than 900,000 paying subscribers) and Current Health for approximately **$400 million** in 2021.

**Definitive agreement.** The signed, binding contract to buy. It precedes *closing*, which is when the deal actually completes — often a quarter later, which is why an announcement date and a completion date differ.

**Private-equity seller.** A firm that owned the business as an investment and is exiting. It says nothing about the business's health; it is how that owner always ends.

## Money that was written off

**Goodwill.** When a buyer pays more than the fair value of a target's identifiable assets, the difference is recorded as an asset called goodwill — the premium paid for the business as a going concern: brand, customers, the team, expected growth.

**Goodwill impairment.** An accounting recognition that the goodwill is no longer worth what the balance sheet says, because the business's expected future is now worse than it was at purchase. **It is not cash leaving the company** — the cash left at acquisition, years earlier. It is the company stating publicly that the earlier price is not going to be justified.

That distinction matters for reading a career. A $475 million impairment does not mean the business burned $475 million that year; it means management revised down what the business will ever be worth, and had to say so.

**Non-cash charge.** Any expense that reduces reported profit without money moving. Impairments and write-downs are the usual kind.

**Pre-tax.** Stated before the tax effect, which is how most charges are announced; the after-tax hit to net income is smaller.

**Reporting unit.** The chunk of the company at which goodwill is tested — here, Best Buy Health as a unit rather than Best Buy as a whole. It is why a charge can be enormous for a division and modest against group revenue.

**Asset impairment / write-down.** The same idea applied to assets other than goodwill: equipment, software, intangibles.

## Money that was rearranged

**Restructuring charge.** The cost of deliberately changing the shape of the business: severance (*termination benefits*), contract exits, and impairments of assets the new shape does not need. A restructuring charge is usually part cash and part non-cash, and the announcement normally splits the two.

**Divestiture.** Selling a business the company owns. Best Buy divested Current Health by selling it **back to its co-founder** in June 2025 — a sale to the person who built it, not to a strategic buyer, which is itself informative about the price.

**Wind-down.** Closing a line of business rather than selling it.

## How the results are reported

**Fiscal year (FY).** A company's own accounting year, which need not match the calendar. **Best Buy's fiscal year ends in late January or early February**, so *FY2026* ran to 31 Jan 2026 — a fiscal-year label is roughly one year ahead of the calendar year it mostly covers. Getting this wrong shifts every event by up to a year.

**Comparable sales ("comps").** Sales growth excluding new and closed stores, so it measures whether the existing business is growing rather than whether the estate is. The headline number retail is judged on.

**10-K / 10-Q / 8-K.** Annual report, quarterly report, and the filing for a material event between them. All public on SEC EDGAR, and the primary source when a press article and a filing disagree.

## Terms from the device and platform side

**ODM (original design manufacturer).** A partner that designs *and* builds a product the customer sells under its own brand — more than a contract manufacturer, which builds to someone else's design. Changing ODM mid-programme means re-establishing both the design relationship and the production line.

**White label.** A product built by one company and sold under another's brand. A *breadth-first white-label integration* strategy aims to support many third-party devices quickly rather than to build few devices deeply.

**Interdependent vs modular architecture** (Christensen's modularity theory). *Interdependent*: "the way one is designed and made depends on the way the other is designed and made" — you must control both sides. *Modular*: interfaces are "specifiable, verifiable, and predictable", so it does not matter who makes the parts. Integrated architectures win while a product is **not yet good enough**; modular ones win once it is **more than good enough**. Choosing is a claim about where the product sits, not a matter of taste. <https://www.christenseninstitute.org/theory/modularity/>

**Stuck in the middle** (Porter's generic strategies). A firm pursuing two incompatible positions at once achieves neither advantage and underperforms both. <https://en.wikipedia.org/wiki/Porter's_generic_strategies>

**Asset specificity and hold-up** (Williamson's transaction cost economics). An investment is *relationship-specific* when it is worth much less outside one partnership — firmware only one vendor can change, a device customized for one integrator. Once it is sunk, the open market "collapses into a two-party negotiation" and either side can *hold up* the other. The prescription, *discriminating alignment*, is to match governance to the transaction: specific, complex work inside the firm; standardized, substitutable work in the market. <https://faculty.haas.berkeley.edu/stadelis/tce_org_handbook_111410.pdf>

**Switching costs and lock-in** (Farrell & Klemperer). The cost of changing supplier; high switching costs "hinder customers from changing suppliers in response to changes in efficiency" and give the incumbent ex post power. A credible threat to move the order is what disciplines a supplier's deadline. <https://eml.berkeley.edu/~webfac/farrell/e220b_s04/switching.pdf>

**Modularity as substitution** (Baldwin & Clark, HBR 1997). Modules designed independently to published design rules can be swapped; that is the business value of the boundary, not tidiness. <https://hbr.org/1997/09/managing-in-an-age-of-modularity>

**The hybrid device-integration trap** — the four entries above applied together. Building devices *ground-up* keeps the fix in-house; integrating *breadth-first* through a thin standard interface keeps the vendor replaceable. A hybrid — too specialized to switch vendors, not owned enough to fix in-house — has neither exit, runs at hardware pace with contract negotiation layered on, and spreads the instability onto both the care provider and the vendor. Worked example: [2025-04-13 breadth-first white label](../../raw/brag/2025-04-13-ble-sdk-breadth-first-white-label.md).

**CMS Acute Hospital Care at Home waiver.** The U.S. regulatory permission, launched November 2020, that let Medicare-certified hospitals treat inpatient-level patients at home — and the reimbursement basis the hospital-at-home market depended on. Its repeated short extensions are the "waiver uncertainty" cited as a cause of slow adoption.

## Related

- [Best Buy Health 2024–2026: the divestiture on the public record](employers/best-buy-health/2026-09-10-best-buy-health-2024-2026-divestiture-public-record.md) — where most of these terms appear in context.
- [Organizations](../entities/organizations.md) — employers and the role played at each.
