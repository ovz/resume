# LinkedIn profile visibility — what actually gets a profile found

> **Doc type:** explanation
>
> Research of 2026-09-14 into "SEO" for a LinkedIn profile: what LinkedIn itself says decides whether a recruiter finds a profile, which popular claims have no source, and what cadence of updates follows for this profile. Audience: the owner deciding how often, and where, to touch the profile; an agent planning a LinkedIn pass. How blocks get onto the profile is [publish to LinkedIn](../workflows/linkedin-publish.md).

## The question, and the answer first

The owner's hypothesis: **neither yearly nor daily updates will improve the chances of LinkedIn promoting the profile.** That is right as a statement about *cadence*, with one qualification about *what* an update changes.

1. **Recency is not a named ranking factor.** LinkedIn's own engineering description of Recruiter search says matching candidates are "selected and then ranked based on a variety of factors" by machine-learned models, naming three: the "similarity of their work experience/skills with the search criteria", the "job posting location", and "the likelihood of a response from an interested candidate". Update frequency is not among them. [eng-2019]
2. **An update that changes what the profile matches does get seen.** Recruiter saved-search alerts run daily and notify the recruiter "each time a profile is created or updated which matches your criteria". [alerts-2009] So a substantive edit — new skills, a sharper headline, a rewritten experience block — can put the profile in front of every recruiter whose saved search it now matches. LinkedIn does not document whether a trivial edit re-triggers alerts, and a profile that pings the same searches daily for no reason is noise, not visibility.
3. **"Open to Work — recruiters only" is the most direct documented lever.** Recruiters can filter search results to candidates who are open to work, and the recruiters-only setting shows the signal to Recruiter users rather than to every member. LinkedIn "takes steps to prevent" Recruiter users at the current employer from seeing it, "but cannot guarantee complete privacy". [otw-member] [otw-recruiter]
4. **Responsiveness plausibly matters more than posting.** "Likelihood of a response" is a ranking factor; LinkedIn does not publish its inputs. Replying promptly to recruiter messages is the obvious behaviour it would reward. *This is inference, not a documented mechanism.*

**For this profile, then:** update on **events**, not on a calendar — which is what the [paste round](../workflows/linkedin-publish.md) already does, since a changed block is a field to re-paste. Spend the effort on the fields recruiters search, not on how often they change.

## Where the effort goes

| Lever | Why it counts | Where it is tracked |
|---|---|---|
| **Headline** | Search matches on titles and skills; the headline is the text most likely to carry the exact terms a recruiter types. Semantic matching means precise real terms beat keyword lists | LinkedIn headline item in the brag-stories-and-linkedin scope's tracker |
| **Skills section** | "Work experience/skills similarity" is the first named factor | Skills and Featured item, same tracker |
| **Current title and experience text** | Also "work experience" similarity; already generated from the resume | The paste round |
| **Location and work preferences** | "Job posting location" is a named factor; Open to Work adds workplace-type filters (on-site, remote, hybrid) [workplace-filter] | Owner decision |
| **Open to Work, recruiters only** | Directly filterable in Recruiter; privacy from the current employer is not guaranteed | Owner decision |
| **Answering recruiters** | Plausibly feeds "likelihood of a response" | Habit |

The vocabulary to put in those fields is already chosen per direction: each [dream-job candidate](../dream-jobs/dream-job-hub.md) has a *vocabulary to foreground* section.

## Claims found that have no source

Career-advice sites repeat precise numbers that no LinkedIn page supports. Found in the 2026-09-14 search and **not to be acted on as stated**: that the headline and current position carry "approximately 60%" of ranking weight; that a headline keyword counts "approximately three times" one in a past role; that recent certifications yield "40% more search appearances"; that a "2026 update" added activity-in-the-last-30-days and photo-quality completeness signals; that weekly posters rank above identical dormant profiles. [blogs] The direction of some of these is plausible — headline terms matter, a complete profile helps — but the numbers are folklore until LinkedIn publishes them.

## Limits of this research

The engineering article dates from 2019 and describes an architecture LinkedIn has since extended with semantic and representation-learning features; the named factors are the stable part. The alerts page dates from 2009, and the help pages are current as searched. Nothing here covers LinkedIn's feed algorithm, which governs posts rather than recruiter search.

## Sources

Read directly on 2026-09-14:

- [eng-2019] LinkedIn Engineering, *AI Behind LinkedIn Recruiter Search and Recommendation Systems*, 2019-04-22 — <https://www.linkedin.com/blog/engineering/recommendations/ai-behind-linkedin-recruiter-search-and-recommendation-systems>
- [alerts-2009] LinkedIn Talent Blog, *Find the Latest Matches with LinkedIn Recruiter Search Alerts*, 2009-08-03 — <https://www.linkedin.com/business/talent/blog/product-tips/find-latest-matches-with-linkedin-recruiter-search-alerts>

From search-result summaries of LinkedIn's help centre, 2026-09-14:

- [otw-member] *Let recruiters know you're Open to Work* — <https://www.linkedin.com/help/linkedin/answer/a507508/let-recruiters-know-you-re-open-to-work?lang=en>
- [otw-recruiter] *View candidates who are open to work in Recruiter* — <https://www.linkedin.com/help/recruiter/answer/a419131/view-candidates-who-are-open-to-work-in-recruiter>
- [workplace-filter] *Filter candidates by workplace type in Recruiter and Talent Hub* — <https://www.linkedin.com/help/recruiter/answer/a527316>
- Saved searches and alerts — <https://www.linkedin.com/help/recruiter/answer/a414065/save-searches-and-set-up-search-alerts-in-recruiter-and-recruiter-lite?lang=en>

The unsourced claims above, for provenance only:

- [blogs] <https://blog.theinterviewguys.com/linkedin-keywords/> · <https://resumevera.com/blogs/linkedin-profile-optimization-guide-2026> · <https://www.hyperclapper.com/blog-posts/linkedin-skills-recruiters-search> · <https://blog.theinterviewguys.com/why-recruiters-are-skipping-your-linkedin-profile/>

## Related

- [Publish to LinkedIn](../workflows/linkedin-publish.md) — the paste round, which already implements an event cadence.
- [Can LinkedIn be updated programmatically?](linkedin-api-access.md) — why the profile is pasted by hand.
- [Career repositories](../workflows/career-repositories.md) — LinkedIn as the outward channel of the job search.
