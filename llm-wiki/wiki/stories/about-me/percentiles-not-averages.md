---
cluster: about-me
fits: [data, principal, leadership, mentoring]
status: draft
runtime: "90 s"
---

# I taught people to ask where the ninety-fifth percentile is, instead of correcting their averages

## Why I still care

Nobody in that room was careless. They were doing what every spreadsheet invites you to do, and I had seventeen years of watching statisticians wince at exactly that. What I am proud of is that I made it a question people could ask themselves, not a correction they had to receive from me.

**Cue:** the card on my one-on-one agenda in November 2022 — *"Talk: why we don't use percentiles and other important things about r5 locations"* — and, two years later, one location fix in San Diego reported at eight metres of accuracy.

## Register

**2020-2026, Best Buy Health**, told from humility and stewardship: this is a story about helping other people think better, not about being the smartest statistician in the building. He is not a statistician and says so. See [voice and prominence](../../workflows/voice-and-prominence.md); lines built per [spoken drafts](../../workflows/spoken-drafts.md) from his note of 2026-09-24.

## Structure

| # | Beat | In this story |
|---|---|---|
| 0 | Offer | One about statistics that is really a mentoring story |
| 1 | Hook | Everyone knows data matters; people still reason with a mean and a standard deviation as if the world were normal |
| 2 | Stakes | On a device people depend on, the tail is where the customers who need you are |
| 3 | Complication | Nobody chose the assumption — they didn't know they had made it — and correcting people's statistics gets you ignored |
| 4 | Move | Taught percentiles, starting with location accuracy, and one question to carry |
| 5 | Punchline | Stopped correcting analyses and taught one question instead |
| 6 | Handover | How does your team talk about the tail? |

## Narrative — rehearse verbatim

**0 · Offer**
> I have one about statistics, and it is really a story about helping people think, more than about maths.

**1 · Hook**
> Where I work now, most people have caught the drift that data is important. But they still compute a mean and a standard deviation and reason about them as if everything is normally distributed. And they don't even realise they assumed a normal distribution.
⟨breathe⟩

**2 · Stakes**
> On an emergency device that matters, because the customers who need you are not in the middle of the curve. The average location fix can look fine while the devices in the tail — indoors, in a basement, with a bad radio — are the ones somebody is trying to find.

**3 · Complication**
> Nobody did this on purpose. A spreadsheet hands you an average, so you use it. And if you walk in and tell people their statistics are wrong, you are the fastest way to get ignored.
⟨breathe⟩

**4 · Move**
> So I taught percentiles instead. I started with location accuracy, because everybody on the team cared about it. Half of the fixes are better than this number, nine out of ten are better than that one — and here is what lives past the ninety-fifth.
*(optional)* Location accuracy is a good teacher. Indoor and outdoor fixes are two different populations, so the "average" describes neither of them.
> My own theory — and it is only my opinion — is that the normal distribution got its name because people like a world where the mean is intuitive and three-sigma events just never happen. The real world is multimodal, with long tails.
*(optional)* Karl Pearson, who made the name popular, regretted it. He wrote that it leads people to believe every other distribution is abnormal.

**5 · Punchline**
> So I stopped correcting people's analyses. I gave them one question to ask themselves: where is the ninety-fifth percentile, and what is out past it?
⟨breathe⟩

**6 · Handover**
> I'm curious how your team talks about the tail. Is it a number on the dashboard, or a conversation?

## If they follow up

- **"Are you a statistician?"** → No. I spent seventeen years building software for statisticians, which taught me when to ask for one. My own mathematics stops short of theirs, and I say so.
- **"Give me a concrete example."** → A single location fix in San Diego reported at eight metres of accuracy. To me that said the fix came from Wi-Fi, which pointed at the older positioning path — and that path is known to hand back a reasonable-looking default when it has nothing better. That is the same habit: take the one odd point and ask what mechanism produced it, instead of averaging it away.
- **"Have you grown people / promoted anyone?"** → Honestly, formal promotions were rare where I have been. Salford was a small company, and my years at GreatCall and Best Buy Health were years of a business absorbing an acquisition, not growing headcount. The growing I have done is this kind — teaching, mentoring, pull-request discipline, raising the bar — and I would like a role where that becomes formal.
- **"Why not just use the median?"** → The median is a good start, and it hides the tail just as well as the mean does. You need the median and a high percentile together, and on a safety device you look at the maximum too.

## Refresher — look up while rehearsing, never recite

- **Normal distribution.** About 68% of values within one standard deviation of the mean, 95% within two, 99.7% within three. So under a normal model a three-sigma event happens about **once in 370** observations.
- **The only guarantee for any distribution is much weaker.** Chebyshev's inequality: at most 1/k² of values lie more than k standard deviations from the mean. At three sigma that is up to **one in nine**, not one in 370. That gap is the whole argument in one number.
- **Percentiles.** The p-th percentile is the value below which p% of observations fall. p50 is the median; p90, p95, p99 describe the tail. Percentiles need no assumption about the shape of the distribution, which is why they are the safe default for latency, location error or battery drain.
- **Multimodal.** More than one peak — typically more than one population mixed together (indoor and outdoor fixes, two firmware versions, two carriers). A mean between two peaks may describe no device at all.
- **Heavy tail and power law.** A power law has probability falling off as x to the power −α. The tail decays slowly, so extreme values are rare but not negligible. For a power-law density the mean is finite only when α > 2 and the variance only when α > 3 — below that, a sample standard deviation keeps growing as you collect more data and describes nothing. Familiar faces: Pareto's 80/20 rule, Zipf's law for word frequencies, file sizes, city sizes, the few devices that burn most of the cellular data.
- **Do not claim a power law from a straight line on a log-log plot.** Clauset, Shalizi and Newman showed that least-squares fitting on log-log axes gives poor estimates, and that many "power laws" are better described as log-normal ([Power-law distributions in empirical data](https://arxiv.org/abs/0706.1062)). Say "heavy-tailed" unless you have done the fit properly.
- **Latency engineers reached the same place from practice.** Gil Tene's talk *How NOT to Measure Latency* calls out "the fallacy of using standard deviation measurements" and "the strongly multi-modal nature of latency" ([QCon London 2013](https://qconlondon.com/london2018/london-2013/qconlondon.com/london-2013/presentation/How%20NOT%20to%20Measure%20Latency.html)).
- **The name.** Pearson (1920): calling the Laplace–Gaussian curve "normal" had "the disadvantage of leading people to believe that all other distributions of frequency are in one sense or another 'abnormal'" ([origin of the name](https://condor.depaul.edu/ntiourir/NormalOrigin.htm)). Peirce used the word in 1873 and Galton from 1877; Pearson made it stick.

## Proof

The agenda card of November 2022 and the eight-metre fix of September 2024 are in the committed board snapshots. The broader statistical practice is its own entry, with its limits stated.

## Know it — what stays with me

T1: the location subsystem and its vendor path (the eight-metre value pointed at the previous generation's Wi-Fi positioning); which analyses I thought were poorly grounded, and whose they were — never told. Whether the November 2022 talk was delivered, and to whom, is not in the record; in my words it is "an ongoing PSO-style activity to help people to assume adequate statistical mindset" — so I tell it as a habit I keep, never as one talk I gave.

## Sources

- [2022-11-10 Percentiles over averages](../../../raw/brag/2022-11-10-percentiles-over-averages-location-statistics.md)
- [2026-05-17 Statistical bar and the Data Science partnership](../../../raw/brag/2026-05-17-statistical-bar-and-data-science-partnership.md) — cited, not graduated

## Related stories

- [Why I do this work](why-i-do-this-work.md) — the stance underneath.
- [The Lively Home lesson](the-mission-lesson.md) — the other half of the same note.
