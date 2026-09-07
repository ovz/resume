# Source: Long-Form Resume (archived, 2018 vintage)

> **Doc type:** reference
>
> Summary and harvest map of [`raw/archive/Oleg.Zhylin.resume.md`](../../raw/archive/Oleg.Zhylin.resume.md) (529 lines). Tier **T1 private repo**. Status: **archived 2026-09-06** from `markdown/` via [archive-source.md](../workflows/archive-source.md). Superseded as a resume by the [primary](resume-achievements.md); retained because it is the richest single source of project detail in the corpus.

## Vintage and scope

Written while the owner lived in Poway, CA and had just joined GreatCall (2018); the GreatCall section is two short paragraphs and Best Buy Health does not appear. Contact block includes a Skype handle and the old address — obsolete. Everything from Salford Systems backward is described at full depth: this is the document the primary resume's *Projects Overview* was condensed from. Its avatar link (`assets/oleg-zhylin-gravatar.png`) dangles after the move; raw is immutable, so it is left as-is.

## Disposition

**Archive with active harvest.** The resume framing is dead; the project narratives are not. Each row below is a piece of knowledge absent from (or much thinner in) the primary resume, with where it should live in the wiki. Status `open` means not yet synthesized anywhere; the archived file remains the citable source meanwhile.

## Harvest map

| Section in archived file | Unique knowledge | Target | Status |
|---|---|---|---|
| Summary blockquote | Interest in Rust/Python/JS "et al." phrasing | none — superseded | closed |
| Experience Overview bullets | Fortran legacy handled "through acquisition and own development"; API design "for interaction between components" | [technical themes](../concepts/technical-themes.md) | open |
| 2018–Present GreatCall | "automated desktop end-to-end testing framework" | superseded by primary | closed |
| 2017–2018 Minitab | Minitab/Salford "profound similarity" framing (classical stats vs ML democratization) | [organizations](../entities/organizations.md) | open |
| 2000–2017 Salford Systems intro | Dan Steinberg founder context; TreeNet = Friedman's gradient boosting (2004), Kaggle relevance; CART → SPM naming at v5.0 | [organizations](../entities/organizations.md) | open |
| SPM 8.2 | Triage/feature-creep balance; VS2013→2015 upgrade; SPM Chinese sync process; CMake hybrid build | [accomplishments by domain](../concepts/accomplishments-by-domain.md) § *Build, release, CI/CD* | open |
| Cloud-ready SPM | Elasticity as cornerstone; SeaweedFS for small files vs Hadoop; PFA converters/interpreter after rejecting `.grv`/pickle/PMML; TSV + transparent compression storage decision; funded via SPM 8.2 | [accomplishments by domain](../concepts/accomplishments-by-domain.md) § *Cloud and distributed systems* | open |
| ISLE distributed ML | HDFS deployment; PySpark → Scala rewrite reproduced JVM issues; Databricks POC notebook; Dask demo in under a week; Matthew Rocklin conversation at PyCon 2016 | § *Big data and distributed ML* | open |
| SPM Qt GUI | Business case (Mac users, mobile); QML vs Qt Widgets evaluation; Milo Solutions partner; SPMnonGUI → cross-platform DLL protected by Codemeter; thread-safe interaction layer; PR-based process and team growth; Qt Installer Framework early adoption; Windows/Linux/macOS packages | § *Architecture and API design*, § *Leadership* | open |
| Predictive engines API | Conda chosen for cross-platform parity; Travis Oliphant conversation at PyCon 2014 influenced Anaconda; invoke tasks: Docker dev env, CMake, unit tests, Codemeter protection, Anaconda Cloud publish | § *Architecture and API design* | open |
| Hive scoring utility | `TRANSLATE` to C; deploy `.c` as-is; TCC compiles on every `SELECT TRANSFORM` node | § *Big data and distributed ML* | open |
| Unicode / i18n | 2011 Japanese partner; five-step Unicode hardening process (warnings, regex sweeps, Unicode test inputs, CppCheck, BoundsChecker); 2016 QYDatatech Chinese translation in < 3 weeks; Korean/Japanese contractors | § *Internationalization* | open |
| **In-house computational cluster (2016–2017)** | Not in primary at all: IT contractor coordination; isolated VPN via dedicated Cisco appliance; RancherOS + Rancher, no bare-metal workloads; FreeIPA (not corporate AD); GitLab for VCS/issues/CI | § *Cloud and distributed systems*, § *Security* | open |
| Wibu Codemeter | Trials of FlexLM/RLM/Arxan/Sentinel; German-language advantage with Wibu support; Debug vs Release DLL protection scheme; Codemeter rescued SPM Chinese where CrypKey failed | § *Security, licensing* | open |
| SPM 7.0 | WTL-based MDI dialog framework; GPS (Generalized PathSeeker) GUI; ISLE/RuleLearner pipeline GUI (model compression, rule discovery); Summary Window tab framework; custom tab control; Gitolite/RedMine/CruiseControl.NET toolchain | § *ML products and GUIs* | open |
| Brazil retail promotion optimization | ODBC feature added to SPM; data-cleanup automation; product cannibalization; C#/WPF app; CLR stored procedures; embedded Windows Workflow Foundation designer; promotion-discovery search; database grew to 1 TB → seeded Cloud-ready SPM | § *Data engineering* | open |
| 64-bit upgrade | AIX/HP-UX and other UNIX warnings; regex sweeps; stress tests; Intel Parallel Studio XE; done in one month | § *Legacy code* | open |
| National Health Survey | K-Means → CART → TreeNet pipeline; SAS macro system design (encapsulation, convention over configuration, reuse) | § *Data engineering*, § *ML products* | open |
| 2007 first San Diego visit | Absorbing retiring GUI lead's knowledge; codebase stewardship | [oleg-zhylin](../entities/oleg-zhylin.md) | open |
| Client-server (2004–2005) | Solaris support; native RPM/DEB/PKG installers; shared client/server sources | § *Architecture and API design* | open |
| CART 5.0 | TreeNet's public debut; results-GUI basis | § *ML products and GUIs* | open |
| CART 4.0 | Compact layout algorithm study; tree details charts; tree map; printing | § *ML products and GUIs* | open |
| IIT (1996–2000) | Prof. Gorbenko; first undergrad hired; big-number crypto library; prime generation; full-disk encryption with Win9x VxD driver; elliptic-curve thesis (2000) | § *Security* | open |
| *Personal development* | Family (names/ages — **re-review before any public use**); healthy lifestyle; herbalism; languages with self-rated proficiency (Russian/Ukrainian native, English fluent, Italian advanced, German/Portuguese intermediate, Spanish lower-intermediate, others familiar) | candidate for optional *About me* in the primary; see [primary-resume.md](../resume/primary-resume.md) § rule 5 | open |

## Related

- [Primary resume source page](resume-achievements.md) — what the condensed version kept.
- [Resume overview (archived)](resume-overview.md) — the intermediate condensation.
- [Source map](../sources.md)
