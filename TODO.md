> This file is for typing next prompts that I couldn't submit earlier. AI agnts are allowed to use this content to see what comes next, but no automatic work items queued. Unless

- I explicitly allow to cover full TODO

- Token budget is unlimited (grounded in a source that can give strong guarantees of this kind)

# Open assignment trackers

> Agent traces: each line is a session-wiki tracker that holds items **for you** — commit guides to land, decisions, checks. The paths are this workstation's scratch. This is your scratch file: delete a line whenever you like; an agent re-adds a trace only when new owner items appear.

- `__untracked_stuff/2026-09-14-career-system-plan/tasks/assignment_tracker.md` — **start here**: your items by priority (land commit guides 030–031 first), and the suggested sequence of Claude sessions
- `__untracked_stuff/2026-09-16-stewardship-integration-grounding/tasks/assignment_tracker.md` — land its commit guides after 032–033; approve the two public aliases; Felipe, Mirabit vs Milo Solutions, NCS-R date and Data Steward facts
- `../job-search-infra/__untracked_stuff/2026-09-14-career-system-inception/tasks/assignment_tracker.md` — land commit 001, router go-ahead, Cowork project, employer-research home
- `../cpp_edu/__untracked_stuff/2026-09-14-career-system-inception/tasks/assignment_tracker.md` — land commit 001, router go-ahead, Boost version

# llm-wiki/wiki/stories/positioning/home-away-kept-simple.md

In this and other stories fix the narrative style. Rewrite sentences like

```
A design review where everyone agreed and nobody engaged. 

The cradle's firmware was frozen at launch — an irreversible decision, made early. 

```

These are more statements than steps in the story. And this style is usually associated with AI generating spoken narrative. Also Fix narrative related agent customizations to sound human rather than like in examples above. Note that using such sentences in speach structure somewhat makes sense. These are not spoken verbatim, though. In speach they sound like artificial corporate, marketing, etc speak. While I am marketing myself (thus the structure), when I tell the story I channel my memories and put them in words. Most humans don't think in tag lines








## Networking tailored resume

# Must mention Rich Stevens book

To this day this is the bible of network programming. Misha brought this book to Ukraine during his visit and I devoured it. this was one of my pillars for predictive jobs tcp/ip daemon  and I am an advanced network programmer to this day.

# My mentor Tim Wodarski is in charge of networking

Tim told me a lot of war stories about networking at best buy. This landed on furtile soil given my networking expereinces with strong foundation on Client/Server SPM (TCP/IP predictive job daemon) and being side initiative for many of the projects, obviously including cellular enabled R5.

This confirmed I am a die hard fan of russ white. I did listen to his O'Reilly content and this cemented my network engineering understanding. I am even glad I do not specialize on networks and stuck in dogmas and looking forward to embrace such specialization and be successful because of Russ White and my mentor Tim advice and inspiration

 
rule11.tech
 (titled Rule 11 Reader) is the official personal website and primary technical blog of network architect Russ White. This is one of my beacon in the world of today as of 2026

 Another saying from Russ is "there are usually 4 basic problems and 4 basic solution in each domain". Upgrade my domains with stories around up to 4 such fundamental problems and top 4 solutions 4 them. Steal 4 network problem from Russ White.









# llm-wiki/wiki/stories/positioning/power-budget-non-issue.md

Power budget trade off analysis is something rather obvious even for juniors, not to mention executives and other non-techincal people. The story is about cutting corners on statistically significant estimation with proper groundng. This story interplas with STM discovery board, MEMs etc. While proving significant motion, ML core, dead reckoning etc are not just keyword match on vendor marketing but actually observed is fundamental, no less important is not only locate the correct numbers in data sheets etc but also add them to budget with the correct analysis. Make sure the approach to battery budget like any other industry wide "standard of care" (medical metaphor a good fit here) for embedded devices matches industry consensus and not something that will raise eyebrows, sound revolutionary, controversial etc. e.g. Russ White critisism of ISO OSI network model resonates with professionals and shows that I think and I care, not just defer to authority. I am a Data Security major and I internalized a thing or two about compliance at a young age. Compliance skills are powerful and "power and responsibility" metaphor works good here. Put another story draft that my less security educated team members still periodically put together ad hoc IMEI, lat/lon numbers, etc obfuscations in the spirit of PII  protection. I always push back that we don't have a concrere certification document , no audit by 3rd party security professionals planned etc. Even our enterprise one Checkmarkx scanner would be some real compliance vehicle. Just because you think this sounds like compliance doesn't help during static analysis, audit etc. So keep it simple, practice yagni, don't put PII into logs, but IMEI, lat/lon etc have some technical meaning and obfuscating them unnecessarily creates work to build obfuscation, test obfuscation itself and use obfuscated data and actual compliance process will still cost the same or even more because one guessed what the right answer is despite in this case if there is no book with righ answer the right answer doesn't exist. 

Another related fact is that SKyhook was decided for positioning. Among other things r5 skyhook powered location fix is much more effective on battery as compared to iZat qualcomm (lookup exact names) previous generation positioning. Qualcomm did a good call purchasing skyhook. We didn't get skyhook just for battery. As I tell in another story, commercial customers e.g. assisted living don't appreciate 1.0 technology. Consumers might tolerate some variability and 1.0 kinds of blunder might drive the churn up somewhat, but rarely be single signficant factor that hikes the churn and kills the product. one of those cases when "no product" means no churn, otherwise getting something in the field is progress, perfectionism is stagnation and failure.

Throw in a restrospect that with AI such experiment design and execution is literally calendar time expense. This is a perfect case for vibe coding, code review is a breathe because no clever code is allowed and irrelevant code is easily spotted. Once llm is in the correct area of hyperspace it doesn't chaotically blunder to some danger zone just out of coarseness of the model parameters etc. That's why prompt engineer profession was short lived. The challenge to keep LLM in the correct space (single word in the prompt determines succsss/failure) got solved by the industry in the matter of months. For modern LLMs the skill is to keep model comrehensive, demand top quality, not accept half baked results etc. I designed several successful experiments and the experience was stellar. A bunch of scripts configured any number of devices, testing instructions were ones I enjoyed executing, and analysis in Jupyter notebook looks like what would be an initiative for a Data Scientist to spend a week just on the first draft and engineer to put it in production. Now I have production grade internal software on my dev machine in minutes. That's my local SAS-apocalypse episode, but more Javon paradox style. I used to have to figure out what is doable and keep my urges to eliminate toil under strict reality check. Now my good stewardship instincts grow into comprehensive documentation and production grade software. I feel like we solved Navier-Stocks equaltions for Agile software development. Contract negotiation still stands, but comrehensive documentation is not a cope out anymore. 











# llm-wiki/wiki/stories/concurrency.md

Need to mine gmail for intel communicatoion. And otherwise must make sure everything from gmail is properly in this repo, those brags I started and up to and including completely missed ones.

# Intel TBB

Fix everywhere it is Intel TBB not TPL.

```
"Intel TPL" is ambiguous — Intel's threading library is TBB (now oneTBB); TPL is Microsoft's .NET Task Parallel Library. The specialization entry preserves the owner's wording and does not pick one.
```

BTW despite fortran compiler bug saga Ken Bernstein and Illya polosukhin got excited to migrate SPM codebase to Intel Cpp compiler. I pushed back strongly Ken even called be "gatekeeper" and I didn't know the word and thought it is a compliment. My pushback was precisely because some blunder in C++ compiler would tank SPM hard and intel had no track record to help out. I also had an intuition that both Illya and Ken are very likely to leave the company soon to their bigger aspirations. It did happen, Ken went to Apple and Illya went to Google. Not too much committment from them, but at least they agreed to disagree. I don't recall we ever did any email communication about this. It is one of the vivid memory of mine, this conversation in the meeting.













# Ingest

## Discover

Run copilot to see which GreatCall or best buy stories and other material need support from Outlook copilot or Rovo Jira/Confluence

# llm-wiki/wiki/stories/stewardship.md

Get all the material for data goverance stretch assignment with Alation, Rodd Johnson, etc In 

- Outlook

- Rovo

- Trello











# llm-wiki/wiki/resume/coverage/engineering.md

There are a number of facts to mine Gmail for **Via Clause Cowork**

# llm-wiki/wiki/stories/stewardship/records-nobody-asked-for.md

Can be augmented with system-monitor story from best buy era. A contractor team lead by C++ superstar Michael Casey created a system-monitor process to manager lifecycle of r5 device (there is a detailed record of design specs in confluence). The project was fully unit tested. Because of r5 delays we had to defer putting system monitor on actual device. When it was time to resurrect the project unit tests didn't work. If I was in charge of the freeze, I would make sure everything builds and runs. But it was CVK who worked with contractors, and he just took their word for it and never tested himself. system-monitor is still in production with no unit test security harness as no one has time to figure out how to run them. xpmf (extensibe portable mobile framework) is another creation of Michael Casey consulting. It does MQTT handling and has beautiful design, but it relies on niche tool called Genie for interface definitions. No one knows how to build xpmf to this day.












## CCF repos

Enrich CCF material with what was actually in repos. I might have actual traces two CCF processes talking to each other over LCM. LCM might be a good keyword for resume, including one for Embedded. Might attract some robotics oriented employers. Make sure to link the public  github.










# Tailored Resume





## C++ expert

Boost
Concurrency

## Edge/embedded AI expert

## Network programmer

TCP/IP daemon
Network engineering foundations

## Database programmer

Data engineering experience
Strong data science background
Strong C++ background
Could lead data engineering team with use of AI and other modern ways

llm-wiki/raw/brag/2014-01-01-cloudsml-cloudspm-bigisle-big-data-rd.md must be made as my strong claim to fame in Data Engineering. Databricks must be the top contender of chops still relevant today. Snowflake pretty much obsoleted eye balling query graphs which I spent so much quality time in SQL server and got Relational Algebra ingrained in my mind. I love relational algebra, but unfortutely linear algebra doesn't land in my brain smoothly. Lucky 5% of world population making crazy money on GPT based AI.






# Concurrency

session to incorporate everything is STOPPED BECAUSE OF SESSION LIMIT

# Boost

I recently ingested brag material about my mastery of boost C++ library. Work through material and promote it to stories

# Cyber Security - CSO appreticeship

Official title is 26 years old, but many side-projjects that are security related, and otherwise, I resurrected Embedded from Computer Engineering Data security majjor from ukraine (not computer science based, because how things were in UA in 1990s) and I am sure I can grow into CSO role, if there is an opportunity. 






























## 2. The five era registers in the voice page: if one reads wrong, that table is the thing to fix.


















# Obesedian visibility - Sonnet


if I look for "captured" using ctrl+f in obesedian I don't see the 

```
| **Captured** | A note in any shape, not yet an entry | `raw/brag/inbox/` | Yes — the loudest colour |
```
as per llm-wiki/wiki/workflows/brag-stories.md

<screnshot>

troubleshoot and make sure obesedian instructions and references are actually grounded and it is always clear in md files how to observe promised stuff in obesedian app on this omarchy. Make the guide concrete which filters to set, color group definitions etc. Author so that I locate stuff in obsedian ui rather than enter manually and then forget and diverge. llm-wiki is the garden of knowledge, so ai can token effectively point me to the right place and I find stuff e.g. in obesedian ui , discover what i need, enhance and enrich this repo etc.

make sure it is clear how to see in obesedian where stories exist and where they don't.

current graph view

<screenshot>


doesn't readily show what llm-wiki/wiki/workflows/obsidian-vault.md describes


# Ingest my ebooks with notes

These are also  bragging material



 

 
















- read coverage and represent all worthy material