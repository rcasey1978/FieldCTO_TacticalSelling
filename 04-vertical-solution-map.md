# 04 · Vertical Solution Map

> **Summary.** This maps each of the four focus verticals to the "3 + 1" architecture pillars, defines the signature cross-architecture bundles/plays, the C-suite outcome and use cases, and the proof points a Field CTO leads with. It also states the OT safety boundary that governs any operational-technology engagement.

---

## The master matrix

Coverage intensity: ●●● = lead / anchor · ●● = strong attach · ● = situational attach.

| Vertical | Secure Networking | Observability & Data (Splunk/TE/AppD) | Resilience & SecOps | AI-Ready Infra |
|----------|:---:|:---:|:---:|:---:|
| **Transportation & Logistics** | ●●● | ●●● | ●● | ● |
| **Financial Services** | ●● | ●●● | ●●● | ●● |
| **Healthcare** | ●●● | ●● | ●●● | ● |
| **Public Sector / Critical Infra** | ●●● | ●● | ●●● | ● |

The Field CTO's job per account: pick the anchor pillar that matches the live business trigger, then design the cross-architecture solution that pulls in the adjacent pillars.

---

## 1. Transportation & Logistics

**C-suite outcome:** *Keep goods and people moving safely and on time — real-time visibility and security across fleets, hubs (ports, airports, rail, depots, warehouses), and the digital logistics platforms customers depend on.*

**Business triggers:** supply-chain resilience mandates, real-time shipment/asset tracking, port/rail/airport modernization, connected-fleet and IoT sensor sprawl, ransomware disrupting logistics operations, NIS2 (transport = critical infrastructure), safety of transport OT (rail signaling, port/airport automation).

| Pillar | What we bring |
|--------|---------------|
| Secure Networking | Distributed-site connectivity (SD-WAN) across ports/depots/stations, IoT segmentation (Meraki / ISE / TrustSec), connected-fleet and edge networking |
| Observability & Data | **Splunk + ITSI** for logistics operations & asset/shipment visibility; **ThousandEyes + AppDynamics** for digital-platform (booking/tracking) experience |
| Resilience & SecOps | Splunk ES + Cisco XDR; transport-OT security (rail signaling, port cranes, airport systems) with human-in-the-loop response |
| AI-Ready Infra | Edge compute for routing optimization and vision at hubs |

**Signature X-Arch bundle — "Always-Moving, Resilient Supply Chain":**
Distributed secure-site networking + IoT/asset visibility in Splunk + digital-platform observability (TE/AppD) + transport-OT SecOps with passive, read-only acquisition.

**Signature use cases:**
- Real-time asset, shipment, and fleet visibility (IoT → Splunk ITSI)
- Secure, resilient connectivity across hundreds of distributed sites (SD-WAN + segmentation)
- Digital logistics-platform experience assurance (network → app → data) for tracking/booking
- Passive transport-OT visibility & security (rail signaling, port/airport automation) — no active probing of control systems
- Ransomware resilience and rapid containment across the logistics network

**Proof points to lead with:** distributed-site secure networking at scale; Splunk logistics operations visibility; passive, read-only transport-OT acquisition as a safety/trust differentiator; NIS2 critical-infrastructure alignment.

**Field engagement kit:**
- *Buyers:* COO / Head of Operations (throughput, uptime), CISO (ransomware, NIS2), CIO (distributed IT), Head of Digital (tracking/booking experience).
- *Discovery questions:* "What does an hour of downtime at your busiest hub cost?" · "How long to inventory every connected asset across your sites today?" · "When a shipment stalls, can you see whether it's the network, the app, or the OT layer?" · "How are you evidencing NIS2 readiness?"
- *Outcome hypotheses (illustrative):* cut mean-time-to-detect for logistics disruptions by >50%; reduce unplanned downtime cost; single pane across IT + OT + digital platform.
- *Common objections → response:* "Our OT team won't allow monitoring" → *passive, read-only, human-in-the-loop; no controller ever touched.* "We already have a NOC tool" → *this correlates network + app + OT + security in one place, not four.*

---

## 2. Financial Services

**C-suite outcome:** *Operational and cyber resilience for always-on digital services, with fraud reduction and regulatory confidence.*

**Business triggers:** DORA / operational-resilience mandates, PCI DSS, fraud losses, digital-channel outages, SOC modernization, cloud migration.

| Pillar | What we bring |
|--------|---------------|
| Secure Networking | Secure connectivity for branches/data centers, Zero Trust (ISE/Duo), SD-WAN for branch |
| Observability & Data | **Splunk Platform + ITSI + AppDynamics + ThousandEyes** — end-to-end digital-experience and transaction observability |
| Resilience & SecOps | **Splunk ES + Cisco XDR + SOAR** — fraud analytics, threat detection, resilience reporting |
| AI-Ready Infra | Data-center modernization for analytics/AI risk models |

**Signature X-Arch bundle — "Resilient Digital Bank":**
ThousandEyes (internet/path) + AppDynamics (app) + Splunk (data/SOC) for full-stack digital-experience assurance, wrapped in Zero Trust networking and a modern SOC.

**Signature use cases:**
- End-to-end observability of a digital transaction (network → app → data)
- DORA-aligned operational-resilience monitoring and evidence
- Fraud detection analytics in Splunk correlated with identity/network signals
- SOC modernization: Splunk ES + XDR + automated response

**Proof points to lead with:** full-stack observability across TE/AppD/Splunk; resilience-and-compliance reporting; consolidation TCO story vs. best-of-breed sprawl.

**Field engagement kit:**
- *Buyers:* CISO (threat + fraud), COO / Head of Operational Resilience (DORA), CIO (digital-channel uptime), Head of Fraud, CFO (consolidation TCO).
- *Discovery questions:* "Can you produce DORA evidence on demand today, and at what effort?" · "When mobile banking degrades, how long to know whether it's the network, the app, or a provider?" · "How many tools sit between a fraud signal and an analyst decision?" · "What's your SIEM renewal timeline?"
- *Outcome hypotheses (illustrative):* faster mean-time-to-resolution on digital-channel incidents; automated resilience evidence; reduced fraud-investigation cycle time; lower SOC tooling TCO through consolidation.
- *Common objections → response:* "We're standardized on another SIEM" → *lead with the network + app context they can't get natively; land ES where the renewal creates a wedge.* "Observability is the app team's budget" → *frame at resilience/board level where the budget consolidates.*

---

## 3. Healthcare

**C-suite outcome:** *Protect patients and data by keeping clinical systems available and connected medical devices secure — under strict privacy rules.*

**Business triggers:** connected medical-device (IoMT) growth, ransomware targeting hospitals, HIPAA, clinical-system uptime, EHR performance, telehealth expansion.

| Pillar | What we bring |
|--------|---------------|
| Secure Networking | Medical-device segmentation & visibility (ISE), secure campus/branch, Zero Trust |
| Observability & Data | **Splunk + AppDynamics** for clinical-application and infrastructure health |
| Resilience & SecOps | **Splunk ES + XDR** — HIPAA-aligned detection, IoMT threat monitoring, SOC |
| AI-Ready Infra | Infrastructure for clinical AI/imaging workloads |

**Signature X-Arch bundle — "Safe Connected Care":**
Medical-device discovery & segmentation + clinical-application observability + HIPAA-aligned SecOps.

**Signature use cases:**
- IoMT device inventory, segmentation, and threat monitoring
- Clinical-application performance assurance (EHR, imaging, telehealth)
- Ransomware detection and rapid, contained response
- HIPAA-aligned audit, access, and data-protection monitoring

**Proof points to lead with:** device-visibility + segmentation joint story; patient-safety framing of uptime; privacy-by-design in the data/SOC layer.

**Field engagement kit:**
- *Buyers:* CISO (ransomware, HIPAA), CIO / CMIO (clinical-system uptime), Head of Biomed/Clinical Engineering (IoMT), Head of Patient Safety.
- *Discovery questions:* "How complete is your connected medical-device inventory, and how is it segmented?" · "What happens to patient care if the EHR degrades for an hour?" · "Could you detect and contain ransomware before it reaches clinical systems?" · "How do you evidence HIPAA access controls?"
- *Outcome hypotheses (illustrative):* full IoMT visibility + segmentation reducing attack surface; faster clinical-app incident resolution; contained ransomware blast radius; audit-ready HIPAA reporting.
- *Common objections → response:* "We can't touch medical devices" → *passive discovery + network-based segmentation; no device agent required.* "Security slows clinicians" → *segmentation + observability improve uptime, which is patient safety.*

---

## 4. Public Sector / Critical Infrastructure

**C-suite outcome:** *Protect critical services and citizens' data, meet mandates, and modernize the SOC — often across IT and OT.*

**Business triggers:** NERC-CIP / NIS2 / national cyber mandates, critical-infrastructure threats, legacy modernization budgets, grid/utility/transport digitization.

| Pillar | What we bring |
|--------|---------------|
| Secure Networking | Segmentation, Zero Trust, secure OT/utility networking, Cyber Vision for utilities |
| Observability & Data | **Splunk** for compliance evidence, operations, and OT visibility |
| Resilience & SecOps | **Splunk ES + XDR + SOAR** — SOC modernization, compliance reporting |
| AI-Ready Infra | Modernization of core data-center/compute |

**Signature X-Arch bundle — "Critical Infrastructure Protection":**
Passive OT/utility visibility (Cyber Vision) + segmentation + Splunk compliance/SOC, aligned to the relevant mandate.

**Signature use cases:**
- Critical-infrastructure asset visibility and segmentation (read-only for OT)
- NERC-CIP / NIS2 compliance monitoring and evidence generation
- SOC modernization for government/agency environments
- Cross-IT/OT threat correlation

**Proof points to lead with:** compliance-evidence automation; critical-infrastructure references; the safety-respecting OT acquisition model.

**Field engagement kit:**
- *Buyers:* CISO / Agency security lead, CIO, Head of Critical Infrastructure / Operations, Compliance/Audit lead.
- *Discovery questions:* "Which mandate (NERC-CIP / NIS2 / national) drives your current program, and what's the deadline?" · "How much manual effort goes into producing compliance evidence?" · "Can you correlate IT and OT threats today?" · "What's the state of your SOC modernization?"
- *Outcome hypotheses (illustrative):* automated compliance-evidence generation cutting audit prep effort; unified IT/OT threat visibility; modern SOC with faster detection/response.
- *Common objections → response:* "Procurement mandates open competition" → *co-author the reference architecture and outcomes early; compete on integrated value, not boxes.* "OT is off-limits" → *passive, read-only acquisition aligned to the safety boundary below.*

---

## OT safety boundary (mandatory for Transportation & Public Sector/Utilities)

Any engagement touching operational technology or safety-instrumented systems (SIS) — including transport OT such as rail signaling, port automation, and airport control systems — operates under a hard, non-negotiable boundary. This boundary is a **competitive differentiator** because it earns OT/operations engineers' trust:

- **Read-only / passive acquisition** for safety-related signals — SPAN/mirror, TAP, one-way diode, or vendor-permitted read-only subscriptions (e.g., Cisco Cyber Vision passive DPI). **No active probing** of control-layer assets.
- **Never write configuration** to PLCs, HMIs, DCS, RTUs, or SIS logic-solvers.
- **Human-in-the-loop response** — automation may notify and pre-stage, but final containment on OT assets requires a human decision with OT-engineering sign-off. SOAR scope ends at the IT / IT-OT DMZ.
- **VISTA never authors the safety lifecycle** — we deliver observability and security analytics *on top of* the customer's safety systems, never the Safety Requirements Specification or SIF-to-SIL artifacts.

The Field CTO uses this boundary explicitly in the room: it demonstrates operational maturity, de-risks the buy for the plant/operations owner, and separates Cisco from vendors who treat OT like IT.

---

## Cross-vertical pattern library (reusable plays)

| Play | Applies to | One-line pitch |
|------|-----------|----------------|
| **Splunk-attach-to-network** | All | "You already run the Cisco network — now see and secure it with Splunk." |
| **SOC modernization** | FinServ, Healthcare, Public Sector | "Splunk ES + Cisco XDR + SOAR = a modern, faster, cheaper-to-run SOC." |
| **Full-stack digital experience** | FinServ, Healthcare, Transportation & Logistics | "ThousandEyes + AppDynamics + Splunk = see every user's experience end-to-end." |
| **Passive OT visibility** | Transportation & Logistics, Public Sector/Utilities | "See and secure transport/critical-infra OT without touching a single controller." |
| **Consolidation TCO** | All | "Replace N vendors with one integrated Cisco + Splunk outcome — lower TCO, less risk." |

---

*Continue to [`05-operating-model.md`](05-operating-model.md) for how the team engages, is enabled, and is measured.*
