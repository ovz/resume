---
cluster: positioning
fits: [embedded, firmware, architecture, principal, leadership, vendor, integration, ai]
status: draft
runtime: "3 min"
---

# Every classic pitfall around beacon tracking was survivable alone; together they multiplied

## Why I still care

This is the one where I watched textbook pitfalls stop being a list and start being a product. A frozen cradle, a missing consumer, pressure to gold-plate, a branch that lived too long, and then add-on after add-on — any one of them I could absorb, and I did. What I am proud of is that I saw early which factor I actually controlled, the number of states, and kept driving it down: Home/Away in 2023, and in 2026 the argument that the next stage is a real location state machine, not one more little thing. Being right was quiet both times, and I would rather be right quietly than loudly late.

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | One for "what does a principal engineer actually do on a feature nobody thinks is hard?" |
| 1 | Hook | Home or away — a small feature that took three years, almost none of it code |
| 2 | Stakes | The beacon is the charging cradle in a senior's home; a caregiver, often the one paying, wants to know |
| 3 | Complication | A frozen cradle, a manufacturer's firmware, a consumer out of scope, gold-plating pressure, a skimmed design, a long-lived branch — and the realisation that they multiply |
| 4 | Move | Drive down the factor you control — states. Spend the rest where the risk is. When top-down add-ons accrete, stop adding and ask for a stage change |
| 5 | Punchline | Release candidate in August 2026 on the same small design; you beat multiplying pitfalls by driving one factor toward one, not by trimming each |
| 6 | Handover | Where are the pitfalls multiplying for you, and which factor do you control? |

## Narrative — rehearse verbatim

**0 · Offer**
> There is one I tell when someone asks what a principal engineer actually does on a feature nobody thinks is hard.

**1 · Hook**
> Beacon tracking. On paper it answers one question: is the wearer home, or away. It took three years, and almost none of that was the code.
⟨breathe⟩

**2 · Stakes**
> It is an emergency-response wearable for active seniors. The beacon is the charging cradle in their home — and whether they are home is exactly what a caregiver wants to know. Often the caregiver is the one paying for the subscription.

**3 · Complication**
> It came to me as an assignment, and I could see at once the device side was the easy part. Everything around it was a classic pitfall.
> The cradle's firmware was frozen at launch — an irreversible decision, made early. The radio firmware on both ends belonged to our contract manufacturer. And the teams who would consume the result were out of my scope. I was building a producer without its consumer.
*(optional)* Then the usual suspects arrived on time. Pressure to build something more capable than anyone had asked for. Decisions re-argued while I was implementing them. A design review where everyone agreed and nobody engaged. A feature branch that lived long enough to charge interest.
> Any one of those, you absorb. What experience tells you — and this one proved — is that they do not add up. They multiply.
⟨breathe⟩

**4 · Move**
> So I went after the one factor I actually controlled: the number of states. Home/Away. One home cradle. Enter, exit, a report every few minutes. No state machine — it did not need one.
*(optional)* The pressure to add was constant, so I asked my manager, out loud, to help me prune scope.
> Then I put the rest of the effort where the risk was. I drove the manufacturer's firmware, build after build, until cradle linking worked. I built relationships downstream without a mandate to. I wrote the design for optionality, because I could not ask its consumers what they needed. And I named the branch as debt, and paid it down.
⟨breathe⟩
> That held. Then the add-ons came — top down, each one a reasonable little thing. Freshness on exit. Freshness on every beacon event. Syncs that behave differently inside the home. A test call when the cradle links. And underneath, a keep-alive refactor that broke beacon tracking outright.
> The small design is why that break was cheap to fix. But by this summer every new add-on was multiplying corner cases — against firmware updates, microcontroller reboots, and a QA pass we had deferred.
> So I stopped adding. I closed a ticket without a pull request, and asked for a decision instead: the next stage has to be a proper location state machine. Not one more little thing.
*(optional)* And I was not going to be the person who broke firmware updates. I had an AI agent read every execution flow, and it found the one gap my 2023 design never had to cover.

**5 · Punchline**
> The release candidate landed in August 2026 — surviving firmware updates, still standing on that small design.
> What I carry from it: you do not beat pitfalls that multiply by trimming each one a little. You find the factor you control, and you drive it toward one.
⟨breathe⟩

**6 · Handover**
> So — where are the pitfalls multiplying in your system right now, and which factor do you actually control?

## The pitfalls, and how they multiplied

Reference for follow-ups — never recited. Each row is a well-known pitfall, where it showed, which factor of the cost it inflated, and what I did about it.

| Classic pitfall | Where it showed | Factor it inflated | Countermove |
|---|---|---|---|
| **The irreversible decision made early** (a one-way door) | Cradle firmware fixed "in stone" at the September 2023 code freeze | Cost of any cradle defect — permanent | Validated end to end before freeze; drove the manufacturer build by build until linking worked |
| **A producer without its consumer** (Conway's law at an org boundary) | Care-centre, caregiver-app and web teams out of scope; in 2026 Device Communications wrote their own pages instead of reading the design | Uncertainty about whether any state is the right one | Relationships without a mandate; design for optionality; in 2026, co-designed the cradle-linked event as a contract in their format |
| **Gold-plating and premature optimisation** | Steady pressure in 2023 for a more capable, more coupled solution | Number of states | YAGNI, linked-cradle-only; asked the manager to help prune |
| **Requirements re-litigated mid-implementation** | Cradle behaviour re-argued in May 2023 while I was building, and moving house; multi-cradle descoped on a manufacturer call | Rework | Built to a state others could pick up; a spoofer so device logic did not wait for firmware |
| **Documentation rot and the rubber-stamp review** | A cradle design document that "remained rotting" when Find Me came into scope; the 2023 Home/Away design skimmed, silent agreement | Undetected design risk | Argued for a single source of truth; wrote the document for the reader who would need it later |
| **The long-lived feature branch, and debt that compounds** | 2023–2024 branch; "the more time passes the more interest we end up paying" (2025) | Everything above, over time | Named it as debt while it accrued; paid it down in 2024; status report in 2025 |
| **Feature creep by accretion — "just one more little thing"** | Top-down add-ons, 2025–2026: freshness on beacon exit, beacon location freshness, inside-home major sync, skipping fix requests on major syncs, an inside-home location-fix interval, a test call on cradle linking | Number of states | Stopped adding: closed a ticket without a pull request, asked for a decision |
| **The implicit state machine** (accidental complexity) | "Current location-related functionality is already an alternative implementation of a state machine" (2026) | States and transitions nobody can see | A location state machine as the next stage — the right tool once there are enough states to need it |
| **Hidden coupling** | The keep-alive production refactoring broke beacon tracking; microcontroller fatal UI turned out to disable it | Execution flows each state must survive | The small design kept the fix cheap; found both in my own testing |
| **Test-space explosion with verification deferred** | Firmware-update flows, microcontroller reboots, on-device-only testing, QA deferred | Cost to verify each combination | Argued in January 2026 to defer cleverness about microcontroller reboots rather than overload QA; AI-assisted analysis of every firmware-update flow |
| **Bus factor of one** | 2023: the team's plan assumed I would build it all; 2026: "a more sophisticated solution that no one but me fully understands" | Risk on every other factor | Kept it small enough to explain; wrote it down |

**Why multiply, not add** — my reading of it, put in one line: the cost of the next change is roughly *states × execution flows × cost to verify each combination × uncertainty that the requirement is right × how few people understand it*. The pitfalls above each sit on a different factor, so they compound. The cradle freeze and the missing consumer were factors I could not touch; the number of states was the one I could. That is why Home/Away had no state machine in 2023, and why in 2026 the answer is an explicit one: first keep the states few, then, when add-ons push them up anyway, make them visible and testable.

## If they follow up

- **"So did it ship?"** → Not to customers, and I say that plainly. It was built and validated end to end on the wearable and the cradle, because the cradle needed it; customer exposure was never in scope. What exists is a release candidate from August 2026.
- **"Did you get the state machine?"** → Not yet — I have asked for it as the next stage, and that is where it stands. It is not a reversal of 2023: three events never needed a state machine, and adding one then would have been the premature complexity I was arguing against. The add-ons changed the problem. The code is already an implicit state machine spread across flags and timers; making it explicit is how the state count becomes visible and testable again.
- **"Why not just keep adding carefully?"** → Because every increment looks cheap on its own ticket and the cost lands on the product of all of them. When a ticket needs its own explanation of five others to be safe, the next increment is the wrong unit of work.
- **"Which pitfall would you remove if you could?"** → The missing consumer. Most add-ons were guesses at what downstream needed. With the consumers in the room, several would not exist — the 2026 co-design on the cradle-linked event is what it should have looked like from the start.
- **"What would you do differently?"** → Put the stage change in the plan on day one: simple first, and an explicit state machine once the add-on count crosses a line agreed in advance. Then the 2026 conversation is a scheduled step, not an argument.
- **"What did the firmware freeze cost?"** → Every cradle behaviour missed before code freeze became permanent. So I tested the manufacturer's cradle builds myself, filed the defects, wrote the test instructions and read their test reports until linking worked from the device's side. I still think updatable cradle firmware is the healthier practice.
- **"Tell me about the AI part."** → Surviving a firmware update was not in my 2023 design, and the updated firmware documents were not in what the agent had. It flagged the gap anyway. That is the strength I bet on: it reads all the inputs and does not forget page nine hundred of the manual. You can still prompt it into forgetting — I do not worry about experienced engineers doing that; I worry nobody challenges juniors to ask it for the best job. That is why grounding belongs in company risk-management policy, not on a list of possible TODOs.
- **"Was it frustrating?"** → At times. For a while the work was invisible while a launch schedule was being judged. What I took from it was to make the non-obvious work visible, not to do less of it.

## Proof

Design documents for cradle tracking and downstream compatibility; the simplified implementation passing the embedded team's code review in 2023; the manufacturer defect tickets and cradle test-report reviews; a 2024 demo of a beacon *enter* event reaching the caregiver app; a 2025 status report; the add-on tickets of 2025–2026; the August 2026 release candidate; the written request for a location state machine as the next stage. There is no customer outcome to cite, and I do not claim one.

## Know it — what stays with me

T1: the manufacturer was Wistron. Shiping Wang and Rob Gonsiewski ran the microcontroller and cradle testing, and in January 2026 I felt they were being comprehensive "without proper grounding in the definition of the space to be comprehensive about". CVK pushed for the more capable version in 2023. Joel Stair wrote the Link compatibility page; Jeremy Moore and Philippe Darvish were the Link contacts, Jordan Alhadoff and Nathan Hall the caregiver-app ones; JR and Shannon on Device Communications in 2026; Hao Do is the manager I asked for the green light. Cradle firmware was fixed "in stone" with the September 2023 code freeze; multi-cradle tracking descoped on a manufacturer call in May 2023; the product manager reduced the likelihood of doing beacon tracking at all in September 2023. The design: three events, a five-minute proximity report interval, a sixteen-cradle store. The add-ons and when they appear on the board: location freshness on beacon exit (2025-01, then 2025-12 to 2026-01), beacon location freshness (2026-05/06), inside-home major sync (2026-06), skipping location-fix requests on major syncs (2026-07), the inside-home location-fix interval (2026-08), the cradle-link test call (2026-04). The keep-alive breakage was 2026-07-28; the location state machine was requested for a later maintenance release in August 2026 and is not green-lit. "Top down mandated" and "AI spotted the gap" rest on my own account rather than an artifact. Current-employer defects and the unreleased feature stay in.

## Sources

- [2023-11-27 Home/Away beacon tracking](../../../raw/brag/2023-11-27-r5-home-away-beacon-tracking.md)
- [2026-09-01 R5 beacon tracking and FOTA persistence](../../../raw/brag/2026-09-01-r5-beacon-tracking-fota-persistence.md)

## Related stories

- [We decided the battery before we decided what the device looked like](power-budget-non-issue.md) — the earlier BLE-beacon research belongs to that story, not to this one; this feature was assigned, not an outgrowth of it.
- [The fault that lost the fix](the-fault-that-lost-the-fix.md) — the same positioning subsystem, seen from field telemetry.
