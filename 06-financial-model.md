# 06 · Financial Model

> **Summary.** A transparent, assumption-driven model for the Field CTO pilot: the cost build-up, the revenue-impact logic, a 3-year illustrative P&L, ROI/payback, and a sensitivity analysis. **Every number here is illustrative and parameterized** — replace the inputs in the assumptions register with real Cisco/Splunk actuals before it goes to finance. Nothing here is reported Cisco financial data.

---

## 0. Assumptions register (edit these first)

| # | Assumption | Illustrative value | Notes / where to calibrate |
|---|------------|--------------------|-----------------------------|
| A1 | Fully-loaded cost, Field CTO (L1) | $400K / yr | Comp + benefits + overhead + allocation |
| A2 | Fully-loaded cost, group lead (L3) | $600K / yr | Senior leader |
| A3 | Fully-loaded cost, X-Arch solution architect | $350K / yr | |
| A4 | Fully-loaded cost, deal desk / ops | $200K / yr | |
| A5 | Enablement + tooling + travel | 15% of personnel | Ramp-heavy in Y1 |
| A6 | Named accounts per Field CTO | 6 | Range 5–8 |
| A7 | X-Arch opportunities framed / Field CTO / yr | 4 | Ramps up over the year |
| A8 | Avg influenced deal size (X-Arch) | ~$1.9M | Multi-architecture, multi-year |
| A9 | Influenced-pipeline → incremental/accelerated bookings conversion | ~33% | Attributable via control-group delta |
| A10 | Blended gross margin on incremental bookings | 60% | Cisco + Splunk blended; calibrate |
| A11 | Deal-size uplift, touched vs. control | +30–50% | Core attribution metric |
| A12 | Splunk cross-attach uplift, touched vs. control | +X pts | Set from baseline attach rate |
| A13 | Ramp: productive quarters in Y1 | ~2 of 4 | Enablement + first-deal lag |

> Change A1–A13 and every table below recomputes. The model is intentionally simple and linear so leadership can stress-test it live.

**Rationale for the key assumptions:**
- **A8 (avg influenced deal size ~$1.9M):** an X-Arch deal spans 3+ architectures over multiple years; this is deliberately conservative for strategic accounts and should be raised if the focus set skews to marquee accounts.
- **A9 (conversion ~33%):** only the *attributable* delta versus control counts as incremental — not all influenced pipeline. A third is a cautious enterprise close/attribution rate.
- **A10 (gross margin 60%):** a blended placeholder across hardware, software, and Splunk subscription; the real number shifts the whole return and is the single most important input for finance to replace.
- **A11–A12 (uplift deltas):** these are the *proof* of the motion — measured, not assumed — via matched control accounts. The Y1 targets should be set from each account's real baseline.
- **A13 (ramp ~2 of 4 quarters):** senior hires plus enterprise sales cycles mean the first two quarters are mostly framing, not bookings.

---

## 1. Cost model (Year-1 pilot)

| Role | Count | Unit cost (A1–A4) | Subtotal |
|------|:---:|---:|---:|
| Field CTO (L1) | 8 | $400K | $3.20M |
| Chief Field CTO / group lead (L3) | 1 | $600K | $0.60M |
| X-Arch solution architect | 2 | $350K | $0.70M |
| Deal desk / ops / enablement | 1 | $200K | $0.20M |
| **Personnel subtotal** | **12** | | **$4.70M** |
| Enablement + tooling + travel (A5: 15%) | | | $0.705M |
| **Total Year-1 cost** | | | **≈ $5.4M** |

## 2. Revenue-impact model (Year-1 pilot)

**Step-by-step (using the register):**

1. Coverage: 8 Field CTOs × 6 accounts (A6) = **48 named accounts** (each paired with a control).
2. Opportunities: 8 × 4 (A7) = **32 X-Arch opportunities framed** in Y1 (ramp-adjusted via A13).
3. Influenced pipeline: 32 × ~$1.9M (A8) ≈ **$60M direct**; with multi-year and expansion framing the *influenced* pipeline the team touches is materially larger → **~$180M influenced pipeline** target (A6–A8 across the full touched base incl. expansion).
4. Incremental/accelerated bookings: influenced pipeline × conversion (A9 ~33%) ≈ **$60M**.
5. Incremental gross margin: $60M × 60% (A10) = **$36M**.

| Metric | Year-1 target (illustrative) |
|--------|------------------------------|
| Named accounts touched | 48 |
| X-Arch opportunities framed | ~32 |
| Influenced pipeline | ~$180M |
| Incremental / accelerated bookings | ~$60M |
| Incremental gross margin (A10) | ~$36M |

### Bottom-up check — a single account (illustrative)

To validate the top-down number, build it from one account and multiply. This is the calculation a Field CTO does per account in the value case.

| Line | Logic | Illustrative |
|------|-------|--------------|
| Current annual spend (networking only) | Account record | $3.0M |
| X-Arch expansion (Splunk ES + XDR + ThousandEyes, multi-year TCV) | The attach the Field CTO frames | +$3.0M |
| New multi-architecture relationship value | Sum | ~$6.0M |
| Incremental vs. control (attributable) | Delta a comparable untouched account would *not* have gained | ~$2.5M |
| Incremental gross margin (A10 60%) | | ~$1.5M |

**Scale-up:** if each Field CTO lands ~3 such outcomes across their focus set, 8 Field CTOs × 3 × ~$2.5M ≈ **$60M incremental bookings** — reconciling with the top-down model. Only ~4–5 such outcomes *for the entire team* are needed to clear break-even.

## 3. ROI & payback (Year-1 pilot)

| Measure | Value |
|---------|-------|
| Year-1 cost | $5.4M |
| Incremental gross margin | $36M |
| **Net contribution (margin − cost)** | **$30.6M** |
| **ROI (on gross margin)** | **~5.7×** |
| **Break-even incremental bookings** (cost ÷ A10) | **~$9M** |
| **Payback** | **< 12 months** |

**Read this line carefully:** the pilot only needs **~$9M of incremental bookings** (at 60% margin) to cover its entire $5.4M cost. That is roughly **five** modeled X-Arch deals. The downside is bounded; the model breaks even at a small fraction of the target.

## 4. Three-year illustrative P&L (scale path)

Assumes a successful pilot expands the team; inputs still driven by the register.

| Line | Year 1 (pilot) | Year 2 (scale) | Year 3 (scale) |
|------|---:|---:|---:|
| Field CTOs (heads) | 8 | 18 | 32 |
| Total team (heads) | 12 | 26 | 44 |
| Total cost | $5.4M | $11.5M | $19.0M |
| Influenced pipeline | $180M | $420M | $760M |
| Incremental / accelerated bookings | $60M | $150M | $280M |
| Incremental gross margin (60%) | $36M | $90M | $168M |
| **Net contribution** | **$30.6M** | **$78.5M** | **$149M** |
| Cumulative net contribution | $30.6M | $109M | $258M |
| ROI (gross margin ÷ cost) | 5.7× | 7.8× | 8.8× |

Efficiency improves with scale as the play library matures, ramp shortens, and references compound.

## 5. Sensitivity analysis

Net Year-1 contribution ($M) as incremental bookings and gross margin vary. Cost held at $5.4M.

| Incremental bookings ↓ / GM → | 50% GM | 55% GM | 60% GM | 65% GM |
|---|---:|---:|---:|---:|
| **$20M** | $4.6 | $5.6 | $6.6 | $7.6 |
| **$40M** | $14.6 | $16.6 | $18.6 | $20.6 |
| **$60M** (target) | $24.6 | $27.6 | $30.6 | $33.6 |
| **$80M** | $34.6 | $38.6 | $42.6 | $46.6 |

**Even the pessimistic corner** ($20M bookings, 50% margin) returns **+$4.6M net** — the pilot is profitable across essentially the entire plausible range.

### Three named scenarios (narrative)

| Scenario | What happens | Incremental bookings | Net contribution | Decision |
|----------|--------------|---------------------:|-----------------:|----------|
| **Conservative** | Slow ramp, only strongest accounts convert; attach uplift modest | ~$25M | ~$9M | Continue; tune targeting |
| **Base (plan)** | Ramp as modeled; attach + deal-size deltas materialize | ~$60M | ~$31M | Expand per 3-year path |
| **Upside** | Consolidation tailwind; multiple marquee accounts land multi-year | ~$90M | ~$46M | Accelerate hiring early |

All three clear break-even; the difference is the *pace of scale*, not whether the pilot pays back. The Q3 gate ([`07`](07-roadmap-risks.md)) exists to catch the sub-conservative case early.

### Downside / stress case

| Scenario | Incremental bookings | Net contribution | Verdict |
|----------|---:|---:|---------|
| Severe under-performance | $12M | ~$1.8M | Still net-positive |
| Break-even | ~$9M | ~$0 | Threshold |
| Below break-even | < $9M | Negative | Q3 gate stops the pilot |

The Q3 go/expand/stop gate ([`07`](07-roadmap-risks.md)) ensures spend stops before it ever approaches the negative region.

## 6. What finance should validate

Before this goes forward, replace the illustrative inputs with actuals for: (a) real fully-loaded costs (A1–A4); (b) the true blended gross margin on the target mix (A10); (c) baseline Splunk attach and deal-size in comparable accounts (A11–A12) to set the control-group deltas; and (d) realistic ramp (A13). The structure holds; only the inputs change.

---

*Continue to [`07-roadmap-risks.md`](07-roadmap-risks.md) for the phased rollout, milestones, and risk mitigations.*
