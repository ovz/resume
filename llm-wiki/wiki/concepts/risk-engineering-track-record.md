# Risk Engineering Track Record

> **Doc type:** reference
>
> Evidence and reusable telling for the owner's Risk Engineer capability and Engineering Manager positioning. This is a capability track, not a dream-job candidate or a separate Risk Engineer resume. The owner explicitly made that distinction on 2026-09-22: risk management belongs to his Data Security background; engineering management is useful across the directions he wants to pursue. The single management variant is routed from [variants](../resume/variants.md).

## Positioning

**Security-trained engineer who makes risk management usable in engineering decisions.** The record combines risk-practice analysis, control design, operational evidence, vendor coordination and data stewardship. Its distinguishing feature is the ability to inspect the implementation as well as question the process. It does not establish a formal Risk Engineer title, enterprise risk-program ownership, actuarial modelling or regulatory sign-off authority. [Risk practice][risk] · [Patch management][patch] · [Readiness][readiness] · [Data governance][data]

For an Engineering Manager audience, lead with distributed-team delivery and developing engineers, then use risk work to demonstrate judgement: choosing useful controls, explaining trade-offs, making dependencies explicit and coordinating specialists. Risk should strengthen the management case rather than replace evidence of managing people. The established record includes teams up to 15, QA enablement and acquisition onboarding; it does not justify inventing a current manager title or a direct-report count. [Domain synthesis](accomplishments-by-domain.md#leadership-management-hiring)

## Three Angles, Distinct Evidence

The supplied retrospective report offers three overlapping interpretations. Keep them as views of a connected practice, not three independent transformations. The dated risk note corroborates only part of the report; the practical examples below have their own evidence trails.

| Angle | Supported personal contribution | Risk Engineer emphasis | Engineering Manager emphasis |
|---|---|---|---|
| Make risk explicit in governance | Identified limited probability quantification and uneven planning; proposed risk appetite and alignment with product-development practice | Assessment quality, appetite, disposition vocabulary and consistent methods | A reasoned improvement proposal across functional boundaries, not an implemented enterprise process |
| Turn guidance into usable controls | Drafted a NIST-grounded patch-management SOP and vendor outreach; later evidence describes a fuller operating model, with adoption still bounded | Security exposure balanced against stability, verification and lifecycle cost | Give engineering, security and vendor partners a repeatable decision path |
| Keep delivery reviews focused on the system | Challenged a launch-readiness exercise using system coupling and existing test coverage; proposed relevant tests and escalation arrangements | Control relevance, residual gaps and evidence of readiness | Constructive disagreement with concrete alternatives, not a campaign against governance |

Sources, row order: [risk practice][risk], [patch management][patch], [launch readiness][readiness]. These are separately dated contributions. The report's delivery experiments, merchandise-data migration and disaster-recovery examples remain attribution leads, not substitutions for these sources.

## Reusable Wording

### Risk Practice, Short Version

I reviewed our risk-management guidance and found that probability was receiving little quantitative treatment and planning was uneven across the organization. I proposed risk appetite as a foundation and alignment with product-development practice. The contribution I can point to is the analysis and proposal; I would not describe it as an adopted enterprise framework. [risk]

### Practical Controls, Short Version

I drafted a NIST-grounded patch-management SOP for embedded firmware. The difficult decision was how to address security vulnerabilities without making a safety-relevant device unstable or allowing its software to become unmaintainable. I also drafted vendor outreach around vulnerability notification. The operating model is documented; I do not have a measured reduction in patch time to claim. [patch]

### Engineering Management, Short Version

Before a device launch, I questioned whether the requested incident exercise would test the risks we actually had. I checked the system's dependencies and existing test coverage, then proposed relevant failure testing, escalation participation and a device-specific scenario. I was willing to challenge a control, but I brought a concrete alternative and explained the reasoning. [readiness]

These are source-bounded tellings, not quotations from the owner. For a longer conversation, follow with the implementation detail in the linked entries. Avoid "process wars" outward: explain the disagreement about a control's purpose without assigning motives or disparaging colleagues.

## Broader Evidence

| Capability | Evidence | Boundary |
|---|---|---|
| Security foundation | Data Security training, cryptography engineering and risk-assessment education in the [primary resume](../../../markdown/Oleg.Zhylin.resume.achievements.md); the owner explicitly connects this background to risk in [data governance][data] | A foundation and sustained mindset, not a claim of a risk certification |
| Engineering control design | [SDK hardening](../../raw/brag/2025-01-16-ccf-sdk-binary-hardening.md): build-time mitigations, explicit trust boundary and dependency provenance | Source evidence, not a penetration-test result |
| Operational detection and response | [Cellular cost controls](../../raw/brag/2024-01-04-cellular-cost-rogue-device-detection.md): deliberate test stimulus, agreed detection threshold, runbook and subsequent real detection | A concrete operational case; no invented savings figure |
| Regulated development | [Medical-device QMS](../../raw/brag/2024-09-24-current-health-hospital-at-home-qms.md): qualification, change control and practical use of the quality system | Worked within the QMS; did not own regulatory certification |
| Data governance and security influence | [Source-grounded catalog work][data], presented to enterprise Cyber Security leadership as a way to shift inventory, classification and checks into development | Catalog work was built; broader security integration was proposed, not shown deployed |
| Delivery under vendor constraints | [Firmware escalation](../../raw/brag/2025-07-18-fota-vendor-escalation-lively-mobile2.md): technical depth, cross-vendor escalation and explicit technical-debt accounting | Do not turn a workable resolution into permanent elimination of the risk |

## Report Claims Not Yet Earned

The [canonical risk entry][risk] retains the report's technical detail and limitations. No report claim is lost by withholding it from a resume.

- **Governance diagnosis:** an image-only article is not proof of an empty methodology. The image and referenced content would need inspection. A likelihood-severity matrix is useful, but its absence alone does not prove that no risk management occurs.
- **Terminology:** value and downside exposure are useful separate lenses. "Opportunity and impact" language alone does not prove conceptual confusion; risk can include uncertainty about positive as well as negative objectives. Describe the actual ambiguity observed rather than declaring an entire framework wrong.
- **Scoring:** multiplying ordinal severity and likelihood ranks is prioritization, not automatically a calibrated probability estimate or expected-loss model. The note supports advocacy for more quantitative assessment, not delivery of quantitative risk modelling.
- **Attribution:** the existence of a template, risk register, experiment plan or recovery plan establishes neither authorship nor application by the owner. Reviewing, recommending, authoring, implementing and operating are distinct verbs.
- **Impact:** guardrails show intended control; they do not prove that customer harm was avoided. Claimed adoption, changed stakeholder behaviour, successful experiments, reduced delays and recovery improvements need outcome evidence.

Those distinctions protect the strongest claim: the owner brings security-informed judgement to engineering and organizational decisions, with implemented controls and operational examples elsewhere in the record. They do not demote a reasoned proposal merely because enterprise adoption has not been established.

[risk]: ../../raw/brag/2023-08-03-risk-management-practice-early-analysis.md
[patch]: ../../raw/brag/2023-09-30-security-patch-management-sop-and-vendor-engagement.md
[readiness]: ../../raw/brag/2023-12-05-operational-excellence-launch-readiness.md
[data]: ../../raw/brag/2025-11-13-column-mapping-framework-alation-data-governance.md