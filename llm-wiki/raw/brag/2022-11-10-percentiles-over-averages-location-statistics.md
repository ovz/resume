---
title: "Taught colleagues to reason in percentiles instead of means and standard deviations, starting with device location quality"
date: "2022-11 to 2026 (ongoing)"
thread: STAT
domains:
  - "Data engineering"
  - "Positioning and location"
  - "Leadership, management, hiring"
context: "Best Buy Health — Lively Mobile 2 location quality, fleet telemetry, and colleagues across engineering and product"
sensitivity: private-repo
resume-worthy: maybe
storied:
  - "about-me/percentiles-not-averages"
---

# Taught colleagues to reason in percentiles instead of means and standard deviations, starting with device location quality

## What I did — the owner's account (2026-09-24, verbatim)

> At my present place most people cought the drift that data is important. Still people compute mean and std dev and reason about them as if everything is normally distributed. They don't even realize they assume normal distribution and no proper statistical reasoning happening. I had to educate people about percentiles. One of my big insights is that normal distribution is called so because people like things where mean is intuitive and stuff 3 sigma away just never happens. Real world is multimodal with crazy power law (include power law and related statistical items refresher so that I could look up as I rehearse the story). I want to tell the story from the position of humility, good stewardship, helping others to grow. Didn't have much opportunity to formally promote other people. Salford Systems was a small company and GreatCall was buidling up goodwill repairment steadily since acquisition (that's my leaders usually right story - every blunder I saw coming and some of them I could even voice against; Livey Home which was visioned as full smart home solution sounded out of touch, incurred non-trivial waste and was one of dominating factors to pivot towards osterity aka profitability; I expressed my expert opinion early and it fell on deaf ears; That was my learning of what poorly defined missions does to even rich organization; We weren't general magic but MVNO on top of Verizon cannot be run on a shoestring budget, so some of that rich company pshyco complex was present until goodwill repairment ran out)

("goodwill repairment" is goodwill impairment; "osterity" is austerity. The Lively Home half of this note is its own entry, [2019-01-01](2019-01-01-lively-home-objection-mission-definition.md).)

## What the record shows

- **November 2022 — a planned talk.** A card in the owner's one-on-one agenda: *"Talk: why we don't use percentiles and other important things about r5 locations."* Location accuracy on a wearable is the textbook case for the argument: fix error is bounded below and long-tailed above, indoor and outdoor fixes form different populations, and a mean plus a standard deviation describes none of them.
- **The same instinct in the location work that followed.** September 2024, reading R4 field data: a single 8-metre-accuracy fix in San Diego told him the source was Wi-Fi, therefore iZat, therefore susceptible to a "reasonable default" — a placeholder value returned where a measurement should be. Reading one point in a distribution for what it says about the mechanism is the same skill as refusing to summarise the distribution by its mean.
- **The owner's statistical grounding** is seventeen years commercialising decision trees and ensembles, and the bar he held on device analytics ([2026-05-17](2026-05-17-statistical-bar-and-data-science-partnership.md)).

**His insight, as an opinion, with the history that supports it.** The owner's reading is that the normal distribution earned its name because people like a world where the mean is intuitive and three-sigma events never happen. The history is kinder to him than most folk etymology: Karl Pearson, who popularised the name, wrote in 1920 that calling the Laplace–Gaussian curve "normal" had "the disadvantage of leading people to believe that all other distributions of frequency are in one sense or another 'abnormal'" — and a main theme of Pearson's own work was that data did not normally follow it ([origin of the name](https://condor.depaul.edu/ntiourir/NormalOrigin.htm)). Latency engineering reached the same place from practice: Gil Tene's widely cited talk calls out "the fallacy of using standard deviation measurements" and "the strongly multi-modal nature of latency" ([QCon London 2013](https://qconlondon.com/london2018/london-2013/qconlondon.com/london-2013/presentation/How%20NOT%20to%20Measure%20Latency.html)).

## Why it matters

A team that reasons about device behaviour in means and standard deviations will set thresholds that fire on the wrong devices and miss the ones that matter, and will be surprised by events it had declared impossible. Percentiles are the cheap, explainable fix; teaching them is stewardship of how a whole team thinks, not only of one analysis.

## Skills demonstrated

Distribution-aware reasoning (percentiles, multimodality, heavy tails); explaining statistics to non-statisticians; reading a single outlier for mechanism; teaching as a form of raising the bar.

## What was blocked, cut short, or wrong

- **Formal promotion of others is thin in the owner's record, and he says why.** Salford Systems was a small company; at GreatCall and Best Buy Health the years after the acquisition were years of goodwill impairment rather than growth. His people-growth record is informal — teaching, mentoring, pull-request discipline, the bar — and this entry is one instance of it. That is the honest answer to "have you promoted anyone?".
- **Whether the November 2022 talk was delivered, and to whom,** is not in the record: the card is an agenda item. Asked, the owner described the practice rather than the event (2026-09-25, verbatim): *"This is an ongoing PSO-style activity to help people to assume adequate statistical mindset."* So it is told as a continuing practice, not as a single talk; the talk's delivery stays unconfirmed, and "PSO" is recorded as he wrote it, unexpanded.

## Evidence

The owner's statement above. Leadership board (committed Trello snapshot): the agenda card of 2022-11-10. Device-programme board (committed Trello snapshot): the R4 location-data card of 2024-09-19. Web sources linked inline, fetched 2026-09-24.

## Evidence limitations

"I had to educate people about percentiles" is the owner's account; no deck, recording or attendee list is retained. Keep outward claims to the practice — reasoning in percentiles and teaching it — rather than to an audience or an outcome.

## Related

- [2026-05-17 statistical bar and the Data Science partnership](2026-05-17-statistical-bar-and-data-science-partnership.md) — the broader practice this is one instance of.
- [2019-01-01 Lively Home objection](2019-01-01-lively-home-objection-mission-definition.md) — the other half of the same note.
- [2024-05-05 anomaly-detection tuning](2024-05-05-r5-anomaly-detection-arima-tuning.md) — statistical reasoning applied to production monitors.

## Record history

- 2026-09-24: created from the owner's TODO note of 2026-09-24 (verbatim above), grounded in the committed Trello snapshots and three web sources fetched the same day.
- 2026-09-24: graduated into story `about-me/percentiles-not-averages`; `storied` property added, body untouched.
- 2026-09-25: owner's answer on the 2022 talk added to *What was blocked* — an ongoing practice, not a one-off talk.
