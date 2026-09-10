# 05 · Operating Model

> **Summary.** How the Field CTO group actually runs: the engagement lifecycle, the repeatable "plays," the enablement ramp, the tooling, how it aligns with account teams / BUs / CX / partners, the compensation design, and the KPI framework (leading and lagging) that proves the motion works.

---

## 1. Engagement lifecycle

```mermaid
flowchart LR
    select[1. Select and Trigger] --> frame[2. Executive Framing]
    frame --> arch[3. X-Arch Architecture]
    arch --> value[4. Value Case]
    value --> orchestrate[5. Orchestrate and Close]
    orchestrate --> land[6. Land and Expand]
    land -.next outcome.-> frame
```

| Stage | What the Field CTO does | Output | Extended team |
|-------|-------------------------|--------|---------------|
| **1. Select & trigger** | Confirm the account fits filters and has a live business trigger | Qualified target + control pair | Account Exec, group lead |
| **2. Executive framing** | Run a CxO outcome conversation; agree the business problem | Executive alignment / outcome statement | Account Exec |
| **3. X-Arch architecture** | Design the cross-architecture reference architecture | Reference architecture + roadmap | SEs, BU specialists, Splunk specialists |
| **4. Value case** | Co-build the business case (TCO/ROI/risk) with the customer | Value case / business case | Value engineering, finance |
| **5. Orchestrate & close** | Pull BU sellers/SEs to detail and close each component | Multi-architecture proposal → booking | BU sellers, SEs, deal desk, partners |
| **6. Land & expand** | Ensure adoption; tee up the next outcome | Reference + expansion pipeline | CX, account team |

**Cycle-time target:** first executive framing within 30 days of account selection; first X-Arch opportunity in pipeline within 60–90 days.

## 2. The plays (repeatable motions)

Each play is a packaged, reusable motion with a discovery script, a reference architecture pattern, a value-case template, and proof points. Drawn from [`04-vertical-solution-map.md`](04-vertical-solution-map.md):

| Play | Anchor pillar | Cross-attach | Primary verticals |
|------|---------------|--------------|-------------------|
| **Splunk-attach-to-network** | Observability | Networking, SecOps | All |
| **SOC modernization** | Resilience & SecOps | Observability, Networking | FinServ, Healthcare, Public Sector |
| **Full-stack digital experience** | Observability | Networking | FinServ, Healthcare, Transportation & Logistics |
| **Passive OT visibility** | Observability + Networking | SecOps | Transportation & Logistics, Public Sector/Utilities |
| **Consolidation TCO** | Any | All | All |

**Play maintenance:** the group lead and solution architects own the play library; each play is refreshed quarterly with new proof points and updated integration capabilities.

## 3. Enablement & ramp

A structured program closes the "conversant → proficient" gaps identified in the [skills matrix](03-role-requirements.md#3-skills--knowledge-matrix).

| Phase | Weeks | Focus | Exit criteria |
|-------|-------|-------|---------------|
| **Foundation** | 1–4 | Portfolio fluency across "3 + 1"; Splunk depth; the plays | Pass play certification |
| **Vertical immersion** | 3–6 (overlap) | Deep dive on primary vertical (regs, economics, references) | Deliver a mock CxO briefing |
| **Shadow & reverse-shadow** | 5–10 | Ride-along on live X-Arch deals | Lead a framing session observed |
| **Live with coaching** | 10+ | Own accounts with group-lead coaching | First opportunity framed |

**Ongoing enablement:** monthly play refresh, quarterly vertical deep-dives, a shared win/loss library, and peer review of reference architectures. Leverage the existing Cisco + Splunk skill assets (the workspace's methodology skills for OT safety, Splunk ES/ITSI/OT, Cisco product integrations) as a technical backbone.

## 4. Tooling

| Need | Tool / mechanism |
|------|------------------|
| Account & control tracking | CRM with an **influence ledger** (X-Arch opportunities, architectures per deal, attach) |
| Reference architectures | Shared architecture library + diagram standards |
| Value cases | Standardized TCO/ROI templates |
| Metrics & attribution | Dashboard comparing touched vs. control accounts |
| Knowledge | Play library, win/loss library, proof-point repository |
| Technical depth | Cisco + Splunk demo/lab environments; joint-solution sandboxes |

## 5. Alignment model (leverage, not conflict)

```mermaid
flowchart TB
    fieldcto[Field CTO Seller]
    ae[Account Exec / GAM]
    bu[BU Specialist Sellers]
    se[Systems Engineers]
    splunk[Splunk Specialists]
    cx[Customer Experience CX]
    partners[Partners / SIs]
    fieldcto <--> ae
    fieldcto <--> bu
    fieldcto <--> se
    fieldcto <--> splunk
    fieldcto <--> cx
    fieldcto <--> partners
```

- **Account teams:** the Field CTO is their senior technical strategist for the biggest cross-arch plays; the AE keeps account ownership and commercials.
- **BU specialists & SEs:** the Field CTO frames and orchestrates; specialists detail and close their component and keep their credit.
- **Splunk specialists:** co-own the cross-attach strategy (see RACI in [`03`](03-role-requirements.md#8-raci-vs-existing-teams)).
- **CX:** engaged early so the "land & expand" adoption motion is designed in, not bolted on.
- **Partners / SIs:** the Field CTO co-owns the architecture *with* strategic partners rather than ceding it — protecting margin and the Cisco relationship.

**Governance:** a lightweight weekly deal sync (Field CTO + AE + relevant specialists) and a monthly group review (pipeline, plays, wins/losses, metrics) run by the group lead.

## 6. Compensation design

Principles from [`03`](03-role-requirements.md#6-compensation-philosophy-design-principle-detailed-in-05); mechanics here.

| Component | Weight (illustrative) | Basis |
|-----------|:---:|-------|
| **Influence credit on touched-account bookings** | 50% | Multi-architecture bookings in accounts the Field CTO led |
| **Splunk cross-attach** | 20% | Splunk attach uplift vs. control in touched accounts |
| **Leading indicators** | 15% | C-suite relationships created, X-Arch opportunities framed |
| **Team / strategic MBOs** | 15% | Play development, references, coaching, coverage |

**Non-zero-sum by design:** influence credit is *additive* — BU sellers keep 100% of their product credit, so the org wants the Field CTO involved. Deal desk arbitrates influence credit using the ledger to prevent disputes.

## 7. KPI framework

**Leading indicators (behavior — measured monthly):**
- # of C-suite/executive relationships created or deepened
- # of X-Arch opportunities framed (multi-architecture, outcome-led)
- Architectures per opportunity (target ≥ 3 on led deals)
- Reference architectures produced; plays run
- Time from account selection → first executive framing

**Lagging indicators (results — measured quarterly):**
- Influenced pipeline ($) and influenced/accelerated bookings ($)
- Average deal size: touched vs. control accounts
- Splunk cross-attach rate: touched vs. control
- Win rate on X-Arch deals vs. baseline
- Multi-year / multi-architecture contract value
- Customer references and advisory relationships created

**Attribution method:** every touched account is paired with a comparable **control account**; deltas (deal size, attach, win rate, velocity) are the primary evidence of the motion's value. The deal-desk influence ledger records the Field CTO's role in each opportunity.

**Pilot success thresholds** (feed the Q3 gate in [`07`](07-roadmap-risks.md)):
- Touched accounts show materially higher X-Arch attach and deal size than controls
- Influenced pipeline on track to the Year-1 target
- Positive BU-team sentiment (the motion helps, not hinders)

---

*Continue to [`06-financial-model.md`](06-financial-model.md) for the cost, revenue-impact, and ROI model.*
