# TerraHash Stack as a Service: Success Metrics & KPI Framework

<aside>
💡

- **Three-tier KPI framework:** Product KPIs (technical performance), Operational KPIs (service delivery), Business KPIs (commercial outcomes)
- **Energy efficiency targets:** Minimum 20% J/TH improvement over air-cooled baseline, with 25-35% typical and validated through independent audits
- **Uptime standards:** 99%+ hashrate consistency maintained through continuous monitoring and automated incident response
- **Thermal management:** 95%+ operating time within 50-65°C optimal range, enabling safe overclocking and extended equipment lifespan
- **Automation excellence:** 85%+ automated incident resolution rate across common failure modes, reducing manual intervention requirements
- **Rapid response:** Fleet-wide MTTR target under 45 minutes, with severity-based escalation protocols for critical incidents
- **Predictive maintenance:** 75%+ accuracy in failure predictions at 7-14 day horizons, continuously refined through machine learning
- **Measurement cadence:** Real-time monitoring, daily tracking, monthly aggregation, quarterly reviews, and annual strategic assessments
</aside>

## Executive Overview

Success metrics define how TerraHash Stack as a Service measures progress toward strategic objectives and delivers quantifiable value to customers. This document establishes a comprehensive framework of Product KPIs, Operational KPIs, and Business KPIs—organized by objective hierarchy and measured through monthly dashboards, quarterly reviews, and annual strategic assessments.

The metrics framework supports three key purposes:

1. **Internal Accountability:** Track execution against business plan and identify areas needing attention
2. **Customer Transparency:** Provide real-time visibility into service delivery quality and value realization
3. **Strategic Guidance:** Identify trends and enable early course correction before major issues emerge

---

## PART 1: PRODUCT KPIs

Product KPIs measure the technical performance and capability of the TerraHash Stack platform itself—independent of customer or business factors.

### 1.1 Efficiency & Performance Metrics

**KPI 1.1.1: J/TH Improvement (Efficiency Gain)**

**Definition:** Joules per terahash—measure of energy consumption per unit of hash computation. Lower is better.

**Calculation:**

```
J/TH = Total Facility Power (kW) × 1,000 / Hashrate (TH/s)

Example: 5 MW facility = 5,000 kW
Hashrate = 100 PH/s = 100,000,000 TH/s
J/TH = 5,000,000 / 100,000,000 = 0.05 kJ/TH = 50 J/TH

```

**Target:**

- Minimum: 20% improvement vs. documented air-cooled baseline
- Typical: 25-35% improvement
- Best-in-class: >35% improvement

**Measurement:**

- Baseline: 30-day average for air-cooled facility (pre-retrofit)
- Post-retrofit: 30-day average starting Day 1 of operations (thermal stabilized)
- Validation: Independent audit (customer/third-party) at 90 days post-retrofit

**Frequency:** Daily tracking, monthly aggregation, quarterly trend analysis

**Accountability:** Product engineering team (efficiency targets), Customer operations (consistent utilization)

**Example Tracking:**

| Period | Baseline | Post-Retrofit | Improvement | Target | Status |
| --- | --- | --- | --- | --- | --- |
| Month 0 (Air-Cooled) | 19.5 J/TH | - | - | - | Baseline |
| Month 1 (Day 0-30) | - | 15.8 J/TH | 19% | 20%+ | On track |
| Month 2 (Day 31-60) | - | 15.2 J/TH | 22% | 20%+ | Exceeds target |
| Month 3 (Day 61-90) | - | 15.0 J/TH | 23% | 20%+ | Exceeds target |

**Business Impact:** Each 1 J/TH improvement = $30-50K annual electricity savings for 5 MW facility (at $0.05/kWh)

---

**KPI 1.1.2: Hashrate Consistency (Performance Stability)**

**Definition:** Percentage of hours facility operates at ≥95% of target hashrate (accounting for scheduled maintenance and force majeure).

**Calculation:**

```
Hashrate Consistency (%) = (Hours at ≥95% target hashrate) / (Total hours - Excluded hours) × 100

Excluded hours: Scheduled maintenance (pre-announced >48 hours), force majeure (grid outages, natural disasters), customer-caused downtime

```

**Target:**

- Minimum: 99%+ facility uptime at target hashrate
- Measurement period: Calendar month (31 days = 744 hours)
- Maximum allowed outage: <7.44 hours per month

**Measurement:**

- Real-time: Pool hashrate reporting + facility power consumption monitoring
- Aggregation: Hourly snapshots, daily/weekly/monthly summaries
- Validation: Automated dashboard alerts if consistency drops below 99%

**Frequency:** Continuous monitoring, daily reporting, weekly trend analysis

**Accountability:** NOC (monitoring/incident response), Customer (operational discipline)

**Example Tracking:**

| Month | Total Hours | Excluded | Active Hours | Hours at 95%+ | Consistency | Target | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| October | 744 | 12 (maintenance) | 732 | 725 | 99.0% | 99%+ | ⚠️ Slight Miss |
| November | 720 | 8 (maint) | 712 | 708 | 99.4% | 99%+ | ✓ Hit |
| December | 744 | 0 | 744 | 741 | 99.6% | 99%+ | ✓ Exceeds |

**Business Impact:** Each 1% uptime improvement = $100-150K additional annual revenue for 5 MW facility

---

**KPI 1.1.3: Temperature Stability (Thermal Consistency)**

**Definition:** Percentage of time facility ASIC junction temperatures remain within optimal operating range (50-65°C under full load).

**Calculation:**

```
Thermal Stability (%) = (Hours with avg junction temp 50-65°C) / (Total operating hours) × 100

Where operating hours exclude startup/shutdown ramps (<30 min each)

```

**Target:**

- Minimum: 95% of operating hours within range
- Optimal: 98%+ of operating hours within range
- Out-of-range events: <2 deviations per month >3°C from midpoint

**Measurement:**

- Sensors: Temperature probes on 10-20% of ASICs per facility (statistically representative sample)
- Frequency: 1-minute readings aggregated to hourly averages
- Alert threshold: If deviation >5°C from target or >2 consecutive hours out of range

**Frequency:** Continuous monitoring, hourly reporting, daily analysis

**Accountability:** AI management platform (thermal control), NOC (cooling system diagnostics)

**Example Tracking:**

| Metric | Oct | Nov | Dec | Target | Status |
| --- | --- | --- | --- | --- | --- |
| Stability % | 94.2% | 96.8% | 97.5% | 95%+ | Improving |
| Avg Junction Temp | 58.1°C | 57.3°C | 56.8°C | 55°C | Good |
| Max Temp Event | 72°C | 68°C | 65°C | <70°C | Improving |
| Temp Deviations | 3 | 1 | 0 | <2 | Good |

**Business Impact:** Thermal stability enables safe overclocking (+15-20% hashrate), extends equipment life (+50% lifespan)

---

### 1.2 Automation & Reliability Metrics

**KPI 1.2.1: Automated Resolution Rate (Autonomous Management)**

**Definition:** Percentage of identified incidents resolved automatically by the AI platform without human intervention.

**Calculation:**

```
Automated Resolution Rate (%) = (Incidents auto-remediated) / (Total incidents detected) × 100

Example: 1,000 incidents/month, 950 auto-resolved = 95% rate

```

**Target:**

- Minimum: 85% of common incidents (stuck miners, pool failover, thermal adjustment)
- Typical: 92-95% auto-resolution rate
- Best-in-class: >95% rate

**Incident Categories:**

1. **Miner stuck/unresponsive** (25% of incidents): 98%+ auto-resolution via PDU power cycle
2. **Pool connection loss** (20%): 99%+ auto-resolution via failover
3. **Thermal throttling** (15%): 95%+ auto-resolution via coolant flow adjustment
4. **Firmware crash** (10%): 90%+ auto-resolution via re-flash
5. **Network connectivity** (15%): 85%+ auto-resolution (requires VLAN/cable investigation for 15%)
6. **High reject rate** (10%): 80%+ auto-resolution via pool failover
7. **Other** (5%): 40% auto-resolution

**Measurement:**

- Real-time: Incident detection → remediation attempt → success validation
- Daily aggregation: Success rate by incident category
- Weekly analysis: Trend identification, tuning adjustments

**Frequency:** Continuous tracking, daily reporting, weekly optimization

**Accountability:** AI platform development team (automation quality), NOC (escalation management)

**Example Tracking:**

| Incident Type | Monthly Count | Auto-Resolved | Resolution Rate | Target | Status |
| --- | --- | --- | --- | --- | --- |
| Miner stuck | 250 | 245 | 98.0% | 98%+ | ✓ Hit |
| Pool failover | 200 | 198 | 99.0% | 99%+ | ✓ Hit |
| Thermal adjust | 150 | 142 | 94.7% | 95%+ | ⚠️ Near |
| Firmware crash | 100 | 90 | 90.0% | 90%+ | ✓ Hit |
| Network | 150 | 127 | 84.7% | 85%+ | ⚠️ Near |
| Reject rate | 100 | 80 | 80.0% | 80%+ | ✓ Hit |
| Other | 50 | 20 | 40.0% | 40%+ | ✓ Hit |
| **TOTAL** | **1,000** | **952** | **95.2%** | **85%+** | **✓ Exceeds** |

**Business Impact:** 1% improvement in auto-resolution rate = ~5-10 hours annually freed up from NOC staff labor

---

**KPI 1.2.2: Mean Time To Resolution (MTTR - Incident Response Speed)**

**Definition:** Average time from incident detection to resolution (either automated or human-assisted).

**Calculation:**

```
MTTR = Σ(Time to resolution for each incident) / (Number of incidents)

By severity level:
- Severity 1 (critical): Target <30 minutes for mitigation, <4 hours full resolution
- Severity 2 (high): Target <1 hour mitigation, <8 hours full resolution
- Severity 3 (medium): Target <4 hours, <24 hours full resolution
- Severity 4 (low): Target next business day, <1 week full resolution

```

**Target:**

- Fleet-wide average: <45 minutes MTTR
- Severity 1 events: <30 minutes initial response
- Severity 2 events: <1 hour initial response
- Severity 3 events: <4 hours initial response

**Measurement:**

- Real-time timestamp capture: Incident detection → alert generated → remediation started → incident resolved
- Categorization: By severity level and incident type
- Daily aggregation: Average MTTR by category

**Frequency:** Continuous tracking, daily trending, weekly analysis

**Accountability:** NOC team (response speed), AI platform (automated remediation speed)

**Example Tracking:**

| Severity | Monthly Count | Avg MTTR | 1st Response | 2nd Response | Target | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Sev 1 | 15 | 18 min | 2 min | 35 min | <30 min | ✓ Hit |
| Sev 2 | 45 | 32 min | 12 min | 48 min | <1 hr | ✓ Hit |
| Sev 3 | 120 | 2.2 hr | 35 min | 6.5 hr | <4 hr | ✓ Hit |
| Sev 4 | 180 | 18 hr | 8 hr | 36 hr | <24 hr | ✓ Hit |
| **Fleet** | **360** | **47 min** | - | - | **<45 min** | ⚠️ Slight Miss |

**Business Impact:** Reducing MTTR by 5 minutes = ~10-15 hours annually of prevented downtime (at incident frequency levels)

---

**KPI 1.2.3: Predictive Maintenance Accuracy (Failure Prediction)**

**Definition:** Percentage of predicted failures that actually materialize within the predicted timeframe (false negative rate + false positive rate).

**Calculation:**

```
Accuracy = [(True Positives) / (True Positives + False Positives + False Negatives)] × 100

Where:
- True Positive: Predicted failure → actual failure occurred within window
- False Positive: Predicted failure → no failure occurred
- False Negative: No prediction → actual failure occurred

Example: 80 True Pos, 15 False Pos, 5 False Neg = 80/(80+15+5) = 80/100 = 80%

```

**Target:**

- Minimum: 75% accuracy at 7-14 day prediction horizon
- Typical: 80-85% accuracy
- Best-in-class: >85% accuracy

**By Equipment Type:**

- Hashboard degradation: 85-90% accuracy (trending data, reliable indicators)
- Fan failures: 80-85% accuracy (vibration signatures)
- Power supply failures: 75-80% accuracy (voltage variance)
- Cooling pump failures: 80-85% accuracy (flow restriction indicators)

**Measurement:**

- Training period: 90 days of facility data before ML deployment (model familiarization)
- Validation period: Next 90 days to assess prediction accuracy
- Continuous refinement: Monthly model retraining on latest data

**Frequency:** Monthly accuracy validation, quarterly model refinement

**Accountability:** AI/ML engineering team (model development), Operations (data quality)

**Example Tracking:**

| Equipment Type | Month | Predictions | True Pos | False Pos | False Neg | Accuracy | Target | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hashboard | Oct | 28 | 24 | 3 | 1 | 85.7% | 85%+ | ✓ Hit |
| Fan | Oct | 18 | 14 | 3 | 1 | 77.8% | 80%+ | ⚠️ Miss |
| Power supply | Oct | 8 | 6 | 1 | 1 | 75.0% | 75%+ | ✓ Hit |
| Cooling pump | Oct | 5 | 4 | 0 | 1 | 80.0% | 80%+ | ✓ Hit |
| **Overall** | **Oct** | **59** | **48** | **7** | **4** | **81.4%** | **75%+** | **✓ Exceeds** |

**Business Impact:** 1% improvement in prediction accuracy = $20-30K reduced maintenance costs (fewer false alarms, better spare parts forecasting)

---

### 1.3 AI Platform Capability Metrics

**KPI 1.3.1: Real-Time Monitoring Latency (Dashboard Responsiveness)**

**Definition:** Time from sensor data collection at ASIC/cooling system to dashboard display update.

**Target:**

- Maximum: <10 seconds for 95th percentile updates
- Average: <3 seconds
- Worst-case (backup systems): <30 seconds

**Measurement:**

- Timestamp capture: Sensor reading timestamp → database write → dashboard query → client display update
- Daily measurement: Calculate 95th percentile latency across all miners
- Facility-level summary: Overall dashboard responsiveness

**Frequency:** Daily monitoring, weekly trend analysis

**Accountability:** Platform infrastructure team (system performance), database team (query optimization)

---

**KPI 1.3.2: Data Availability (System Uptime - SLA)**

**Definition:** Percentage of time the AI management platform dashboard and APIs are available and responsive.

**Target:**

- Platform uptime: 99.9% (allowing <43 minutes downtime per month)
- API availability: 99.95%
- Database availability: 99.99%

**Exclusions:**

- Scheduled maintenance (announced >48 hours in advance, limited to 2 windows per month)
- Force majeure (data center power failure, network ISP outage)

**Measurement:**

- Synthetic monitoring: Automated health checks every 60 seconds
- Real transaction monitoring: Track actual API calls and database queries
- Customer-reported incidents: Self-reported downtime from facility operators

**Frequency:** Continuous monitoring, hourly aggregation, daily reporting

**Accountability:** Platform operations team (infrastructure), customer success team (communications)

---

**KPI 1.3.3: AI Model Freshness (Training Update Frequency)**

**Definition:** Time since ML models were last retrained on facility-specific operational data.

**Target:**

- Weekly retraining: Monthly updating of facility-specific models
- Prediction models: Retrained every 30 days minimum
- Anomaly detection: Retrained every 14 days for maximum sensitivity

**Measurement:**

- Timestamp tracking: Last retraining date for each model
- Data freshness: Percentage of input data <30 days old

**Frequency:** Monthly model retraining, quarterly model validation

**Accountability:** AI/ML engineering team (model development)

**Business Impact:** Fresh models improve prediction accuracy by 3-5%, reducing unplanned failures by ~10-15%

---

## PART 2: OPERATIONAL KPIs

Operational KPIs measure how well TerraHash Stack delivers the core service—facility management, support, and customer success.

### 2.1 Customer Experience Metrics

**KPI 2.1.1: Net Promoter Score (NPS - Customer Satisfaction)**

**Definition:** Standard industry metric measuring customer willingness to recommend TerraHash services. Scale 0-10, with calculation: NPS = % Promoters (9-10) - % Detractors (0-6)

**Calculation:**

```
Example: 100 respondents
- 70 scored 9-10 (Promoters) = 70%
- 15 scored 7-8 (Passives) = 15%
- 15 scored 0-6 (Detractors) = 15%
NPS = 70% - 15% = 55

```

**Target:**

- Minimum: >40 (industry benchmark: 30-40 standard, 50+ excellent)
- Typical: >55 by Year 1, >65 by Year 2+
- Segment performance:
    - Regional operators: >50
    - Institutional customers: >60
    - Energy producers: >65
    - Enterprise: >70

**Measurement:**

- Quarterly surveys: All active customers, 10-15 min completion time
- Ad-hoc surveys: Post-retrofit (30 days), post-incident (resolution validation)
- Trend analysis: Month-over-month change, cohort analysis (by customer type)

**Frequency:** Quarterly formal surveys, ad-hoc post-event surveys

**Accountability:** Customer success team (relationship management), Product team (feature delivery)

**Example Tracking:**

| Quarter | Promoters | Passives | Detractors | NPS | Target | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 2026 | 45% | 20% | 35% | 10 | >40 | ⚠️ Miss |
| Q2 2026 | 55% | 18% | 27% | 28 | >40 | ✓ Hit |
| Q3 2026 | 62% | 15% | 23% | 39 | >40 | ✓ Hit |
| Q4 2026 | 68% | 12% | 20% | 48 | >50 | ⚠️ Near |

**Business Impact:** Each 5-point NPS increase = ~15-20% increase in customer referral rate, ~10% improvement in retention

---

**KPI 2.1.2: Customer Satisfaction (CSAT - Service Quality)**

**Definition:** Direct satisfaction rating on specific service dimensions (SLA attainment, communication, technical competence, value for money).

**Scale:** 1-5 (1=very dissatisfied, 5=very satisfied)

**Target by Dimension:**

- SLA attainment: 4.5+ (consistent uptime delivery)
- Communication: 4.3+ (responsiveness, transparency)
- Technical competence: 4.6+ (expert troubleshooting, optimization)
- Value for money: 4.2+ (ROI delivery vs. cost)
- Overall: 4.4+ (blended average)

**Measurement:**

- Post-incident surveys: Within 2 hours of incident resolution, 2-minute questionnaire
- Monthly surveys: All customers receive one CSAT questionnaire per month
- Trend tracking: Identify dimensions needing improvement

**Frequency:** Continuous (post-incident), monthly aggregation

**Accountability:** Operations team (service delivery), Account managers (customer expectations)

**Example Tracking:**

| Dimension | Oct | Nov | Dec | Target | Status |
| --- | --- | --- | --- | --- | --- |
| SLA Attainment | 4.3 | 4.4 | 4.6 | 4.5+ | ✓ Hit |
| Communication | 4.1 | 4.3 | 4.4 | 4.3+ | ✓ Hit |
| Technical Competence | 4.5 | 4.6 | 4.7 | 4.6+ | ✓ Hit |
| Value for Money | 4.0 | 4.2 | 4.3 | 4.2+ | ✓ Hit |
| **Overall** | **4.2** | **4.4** | **4.5** | **4.4+** | **✓ Approaching** |

---

**KPI 2.1.3: Customer Effort Score (CES - Friction Reduction)**

**Definition:** Measure of ease in getting issues resolved and services accessed. "How easy was it to get your issue resolved?" Scale 1-5 (1=very difficult, 5=very easy)

**Target:** 4.0+ (easy to medium-easy experience)

**Measurement:**

- Post-resolution surveys: Sent 4 hours after incident closure
- Quarterly deep-dives: Interview customers on onboarding, ongoing support experience

**Frequency:** Continuous measurement, monthly reporting

**Accountability:** NOC (first-time resolution), Account managers (communication clarity)

---

### 2.2 SLA & Uptime Delivery

**KPI 2.2.1: SLA Attainment Rate (Contractual Uptime Guarantee)**

**Definition:** Percentage of months in which TerraHash meets contractually-committed uptime SLA.

**Calculation:**

```
SLA Attainment (%) = (Months with uptime ≥ SLA target) / (Total months) × 100

Example: 12-month period
- Gold SLA: 99% uptime target
- 11 months hit 99%+ uptime
- 1 month hit 98.5% uptime
SLA Attainment = 11/12 = 91.7%

```

**Target:**

- By SLA Tier:
    - Silver (best-effort): N/A (no guarantee)
    - Gold (99%): 95%+ monthly achievement (allow 1 miss per 12 months)
    - Platinum (99.5%): 98%+ monthly achievement (allow 1-2 misses per 12 months)
    - Platinum Enterprise (99.9%): 99%+ monthly achievement (allow 1 miss per 12 months)

**Measurement:**

- Monthly: Calculate actual uptime per customer per SLA tier
- Generate SLA credit report if underperformance detected
- Track cumulative attainment rate

**Frequency:** Daily monitoring, monthly reporting, quarterly trend analysis

**Accountability:** NOC (incident response), Account managers (customer communication)

**Example Tracking:**

| Month | Gold Target | Actual | Hit Target | Platinum Target | Actual | Hit Target |
| --- | --- | --- | --- | --- | --- | --- |
| Oct | 99% | 99.1% | ✓ | 99.5% | 99.2% | ✗ Credit |
| Nov | 99% | 99.0% | ✓ | 99.5% | 99.6% | ✓ |
| Dec | 99% | 98.8% | ✗ Credit | 99.5% | 99.3% | ✗ Credit |
| **Attainment Rate** | - | - | **66%** (2/3) | - | - | **33%** (1/3) |

**Business Impact:** Missing SLA attainment triggers customer credits (revenue loss) and increases churn risk

---

**KPI 2.2.2: SLA Credit Frequency & Magnitude (Financial Penalties)**

**Definition:** Number and value of SLA credits issued due to underperformance.

**Calculation:**

```
Total credits issued = Σ(Credits per miss per customer)

By tier:
- Gold: $25-50/TH × (Target % - Actual %) / 100 × Facility TH
- Platinum: $50-100/TH × difference
- Enterprise: 2-5% of monthly gross mining revenue

```

**Target:**

- Maximum credits: <3% of total monthly service revenue
- Preferred: <1% (indicates high service quality)

**Measurement:**

- Monthly aggregation: Sum total credits issued across all customers
- By tier: Identify which SLA tiers are most at-risk
- Trend: Identify improvement or degradation patterns

**Frequency:** Monthly reporting

**Accountability:** Operations (uptime delivery), Finance (credit tracking and reversal)

**Example Tracking:**

| Month | Gold Credits | Platinum Credits | Enterprise Credits | Total Credits | Service Revenue | % of Revenue |
| --- | --- | --- | --- | --- | --- | --- |
| Oct | $8,500 | $32,000 | $500,000 | $540,500 | $50M | 1.08% |
| Nov | $3,200 | $15,000 | $150,000 | $168,200 | $52M | 0.32% |
| Dec | $12,800 | $48,000 | $350,000 | $410,800 | $55M | 0.75% |
| **Q4 Total** | **$24,500** | **$95,000** | **$1,000,000** | **$1,119,500** | **$157M** | **0.71%** |

**Business Impact:** Credits represent direct revenue loss; >2% credit rate triggers escalation to executive review

---

### 2.3 Operational Efficiency Metrics

**KPI 2.3.1: On-Site Visit Frequency & Duration (Productivity)**

**Definition:** How often TerraHash technicians visit customer facilities and how efficiently visits are conducted.

**Calculation:**

```
Visits per MW per year = (Total visits to customer / Facility MW) / 12 months

Example: 50 MW facility, 6 visits per year = 6/50 = 0.12 visits/MW/year

Average duration: Sum(time per visit) / number of visits

```

**Target:**

- Gold tier: 2 visits/year (semi-annual), average 4-6 hours per visit
- Platinum tier: 4 visits/year (quarterly), average 6-8 hours per visit
- Enterprise tier: 12+ visits/year (monthly+), dedicated on-site technician

**Measurement:**

- Calendar scheduling: Track scheduled and actual visits
- Time tracking: Log hours per visit, activities performed
- Productivity scoring: Value delivered per visit hour (optimization recommendations, equipment repairs, training)

**Frequency:** Monthly tracking, quarterly productivity analysis

**Accountability:** Account managers (scheduling), Field service team (execution)

---

**KPI 2.3.2: NOC Staffing Efficiency (Cost Per Incident)**

**Definition:** How many incidents are managed by NOC team relative to headcount, measuring operational leverage.

**Calculation:**

```
Cost per incident = (NOC annual labor cost) / (Annual incidents handled)

Example: $2M annual NOC cost, 12,000 incidents/year = $166.67 per incident

Incidents per FTE = (Total incidents) / (NOC FTE headcount)
Example: 12,000 incidents, 8 FTE = 1,500 incidents per FTE per year

```

**Target:**

- Incidents per FTE: 1,200-1,500 per year (steady-state), ramping to 2,000+ as automation improves
- Cost per incident: <$150 (Year 1), <$100 (Year 2+)

**Measurement:**

- Monthly: Track incident volume vs. NOC headcount
- Quarterly: Calculate efficiency trends, identify improvement opportunities
- Track automation impact: Higher auto-resolution rate = higher incidents per FTE

**Frequency:** Monthly reporting, quarterly optimization

**Accountability:** NOC manager (resource planning), Operations (automation effectiveness)

**Example Tracking:**

| Quarter | Incidents | NOC FTE | Incidents/FTE | Labor Cost | Cost/Incident | Target | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Q1 2026 | 8,500 | 12 | 708 | $450K | $52.94 | <$150 | ✓ |
| Q2 2026 | 10,200 | 12 | 850 | $480K | $47.06 | <$150 | ✓ |
| Q3 2026 | 12,000 | 10 | 1,200 | $420K | $35.00 | <$150 | ✓ |
| Q4 2026 | 14,400 | 10 | 1,440 | $420K | $29.17 | <$100 | ✓ |

**Business Impact:** Automation improvements drive 30-40% reduction in cost per incident, improving gross margin on SLA services

---

**KPI 2.3.3: Customer Onboarding Time (Project Delivery)**

**Definition:** Time from contract signature to facility operational at target performance.

**Target:**

- Express retrofit (1-2 MW): 12-14 weeks
- Standard retrofit (5-10 MW): 16-20 weeks
- Large retrofit (20+ MW): 20-28 weeks
- Multi-site portfolio: 24-36 weeks

**Measurement:**

- Gate completions: Track Phase 0-4 progress
- Schedule adherence: Actual vs. planned timeline
- On-time delivery rate: % of projects delivered within ±1 week of planned date

**Frequency:** Project-level tracking (weekly status), quarterly portfolio review

**Accountability:** Project managers (delivery), Operations (resource allocation)

**Example Tracking:**

| Project | Customer | Capacity | Planned End | Actual End | Variance | On-Time |
| --- | --- | --- | --- | --- | --- | --- |
| TX-001 | RegionalOp | 5 MW | Week 18 | Week 18 | 0 | ✓ |
| GA-002 | Institutional | 25 MW | Week 24 | Week 23 | -1 | ✓ |
| WY-003 | EnergyProd | 18 MW | Week 20 | Week 21 | +1 | ✓ |
| TX-004 | Distressed | 31 MW | Week 14 | Week 15 | +1 | ⚠️ Slight |
| **On-Time Rate** | - | - | - | - | - | **75%** (3/4) |

---

## PART 3: BUSINESS KPIs

Business KPIs measure financial performance, market traction, and strategic progress toward revenue and profitability targets.

### 3.1 Revenue & Growth Metrics

**KPI 3.1.1: Annual Recurring Revenue (ARR - SLA Services)**

**Definition:** Annualized value of all active SLA support contracts.

**Calculation:**

```
ARR = Σ(Monthly SLA fee × 12 for all customers)

Example:
- Customer A: $5K/month × 12 = $60K
- Customer B: $12K/month × 12 = $144K
- Customer C: $8K/month × 12 = $96K
Total ARR = $300K

```

**Target:**

- Year 1: $3-5M ARR (100-200 customers)
- Year 2: $8-12M ARR (300-500 customers)
- Year 3: $20-30M ARR (600-900 customers)

**Measurement:**

- Monthly aggregation: Calculate ARR on 1st of each month
- Cohort tracking: ARR by customer segment (regional, institutional, energy, enterprise)
- Growth rate: Month-over-month and year-over-year ARR growth

**Frequency:** Monthly reporting, quarterly trend analysis

**Accountability:** Sales leadership (new customer acquisition), Account managers (retention/expansion)

**Example Tracking:**

| Month | Active Customers | Monthly SLA Revenue | ARR | Growth | Target | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Jan 2026 | 45 | $380K | $4.56M | - | $4-5M | ✓ |
| Feb 2026 | 52 | $425K | $5.10M | 11.8% | - | ✓ |
| Mar 2026 | 58 | $465K | $5.58M | 9.4% | - | ✓ |
| Apr 2026 | 68 | $535K | $6.42M | 15.1% | - | ✓ |

**Business Impact:** ARR growth indicates successful product-market fit and predictable revenue for forecasting

---

**KPI 3.1.2: Retrofit Services Revenue (One-Time CapEx)**

**Definition:** Total revenue from facility retrofit projects completed (cooling system installation, firmware deployment, AI platform integration).

**Calculation:**

```
Retrofit revenue = Σ(Project contract value for completed projects)

Example: 5 projects completed, average $10M per project = $50M revenue

```

**Target:**

- Year 1: $20-30M retrofit revenue (60-100 MW retrofitted)
- Year 2: $50-75M retrofit revenue (300-500 MW retrofitted)
- Year 3: $80-120M retrofit revenue (750-1,200 MW retrofitted)

**Measurement:**

- Project tracking: Contract value at signing, revenue recognition at completion (Phase 4)
- Pipeline analysis: Upcoming projects by expected close date
- Win rate: % of proposals that close (target: 35%+)

**Frequency:** Monthly revenue recognition, quarterly pipeline review

**Accountability:** Sales team (deals), Project delivery (on-time completion)

**Example Tracking:**

| Quarter | MW Retrofitted | Projects Completed | Retrofit Revenue | ARR Added | Total Revenue |
| --- | --- | --- | --- | --- | --- |
| Q1 2026 | 35 | 7 | $18.5M | $1.2M | $19.7M |
| Q2 2026 | 68 | 12 | $38.2M | $2.4M | $40.6M |
| Q3 2026 | 110 | 18 | $62.1M | $3.8M | $65.9M |
| Q4 2026 | 152 | 22 | $85.6M | $5.2M | $90.8M |
| **Year 1** | **365** | **59** | **$204.4M** | **$12.6M** | **$217.0M** |

---

**KPI 3.1.3: Total Contract Value (TCV - Customer Lifetime)**

**Definition:** Total revenue expected from a customer over the entire contract lifetime (retrofit + SLA services).

**Calculation:**

```
TCV = Retrofit project value + (SLA monthly fee × contract term in months)

Example:
- Retrofit project: $10M
- SLA: $8K/month × 36 months = $288K
- TCV = $10.288M

```

**Target:**

- Average TCV: $5-15M (varies by customer size)
- SLA ratio (recurring vs. one-time): 40% SLA / 60% retrofit is typical
- Target: Shift toward 50/50 as customer base matures

**Measurement:**

- Per customer: Calculate TCV at contract signature
- Portfolio aggregate: Sum TCV across all customers
- Cohort analysis: Compare TCV by customer segment

**Frequency:** Monthly as new contracts signed, quarterly analysis

**Accountability:** Sales (deal structure), Customer success (retention)

---

**KPI 3.1.4: Net Dollar Retention (Expansion Revenue)**

**Definition:** Percentage of prior-year SLA revenue retained in current year, including expansion revenue from existing customers.

**Calculation:**

```
NDR (%) = [(Starting ARR - Churn) + Expansion] / Starting ARR × 100

Example:
- Jan ARR: $10M
- Churn (lost customers): -$0.5M
- Expansion (upsells/add-ons): +$1.5M
- Dec ARR: ($10M - $0.5M + $1.5M) / $10M = 120% NDR

```

**Target:**

- Minimum: 100% (zero net growth from existing customers)
- Typical: 110-120% (organic growth from existing base)
- Exceptional: >130% (rapid expansion from large accounts)

**Measurement:**

- Cohort tracking: Customers from each vintage year show NDR separately
- Monthly monitoring: Identify churn and expansion trends early

**Frequency:** Monthly calculation, quarterly analysis

**Accountability:** Account managers (customer success/expansion), Sales (renewal/upsell)

**Example Tracking:**

| Cohort | Starting ARR | Churn | Expansion | Ending ARR | NDR |
| --- | --- | --- | --- | --- | --- |
| 2025 (Year 1) | $8M | -$0.2M | $1.2M | $9.0M | 112.5% |
| 2026 (Year 1) | $12M | -$0.3M | $2.0M | $13.7M | 114.2% |
| **Portfolio** | **$20M** | **-$0.5M** | **$3.2M** | **$22.7M** | **113.5%** |

**Business Impact:** NDR >100% indicates product-market fit and sustainable growth; industry benchmark is 110-120% for strong SaaS businesses

---

### 3.2 Profitability & Unit Economics

**KPI 3.2.1: Gross Margin by Service Line**

**Definition:** Revenue minus direct costs (not including sales, marketing, R&D, G&A overhead).

**Calculation:**

```
Gross Margin (%) = [(Revenue - Direct Costs) / Revenue] × 100

By service line:
1. Retrofit services: Equipment, installation labor, project management
2. SLA support: NOC labor, platform infrastructure, field service
3. Treasury module: Minimal COGS, mostly software/license

```

**Target:**

- Retrofit services: 18-22% gross margin
- SLA support: 65-75% gross margin
- Treasury module: 85%+ gross margin
- Blended: 60-65% gross margin

**Measurement:**

- Monthly P&L: Revenue by service line, direct costs allocated
- Trend analysis: Identify gross margin improvements/degradation

**Frequency:** Monthly reporting, quarterly analysis

**Accountability:** Finance (cost tracking), Operations (cost efficiency)

**Example Tracking:**

| Service | Revenue | Direct Costs | Gross Margin | Target | Status |
| --- | --- | --- | --- | --- | --- |
| Retrofit (Month) | $15M | $12.2M | 18.7% | 18-22% | ✓ |
| SLA (Month) | $4.2M | $1.4M | 66.7% | 65-75% | ✓ |
| Treasury (Month) | $0.8M | $0.1M | 87.5% | 85%+ | ✓ |
| **Blended** | **$20M** | **$13.7M** | **31.5%** | - | - |

**Note:** Blended margin excludes S&M, R&D, G&A (~40% of revenue), resulting in operating margin of ~-8.5% (loss) in early years

---

**KPI 3.2.2: Customer Acquisition Cost (CAC - Sales Efficiency)**

**Definition:** How much TerraHash spends (sales & marketing) to acquire each dollar of TCV.

**Calculation:**

```
CAC Payback Period (months) = CAC / (Monthly SLA revenue per customer)

Example:
- Total S&M spend: $5M
- New customers: 125
- CAC per customer: $5M / 125 = $40K
- Average customer SLA: $6.5K/month
- CAC payback: $40K / $6.5K = 6.2 months

```

**Target:**

- CAC payback: <12 months (ideally 6-9 months)
- Implied annual ROI: >100% (cost recovered before Year 1 renewal)

**Measurement:**

- Monthly: Track new customer count and S&M spend
- Calculate CAC and payback period per cohort
- Compare CAC by channel (direct sales, referrals, partner, inbound)

**Frequency:** Monthly calculation, quarterly trend analysis

**Accountability:** Sales leadership (efficiency), Marketing (lead quality)

**Example Tracking:**

| Period | S&M Spend | New Customers | CAC | Avg SLA/Month | Payback Months | Target | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Q1 2026 | $1.2M | 42 | $28.6K | $6.8K | 4.2 | <12 mo | ✓ |
| Q2 2026 | $1.4M | 58 | $24.1K | $7.2K | 3.3 | <12 mo | ✓ |
| Q3 2026 | $1.6M | 72 | $22.2K | $7.5K | 2.9 | <12 mo | ✓ |
| Q4 2026 | $1.8M | 85 | $21.2K | $7.8K | 2.7 | <12 mo | ✓ |
| **Year 1** | **$6.0M** | **257** | **$23.3K** | **$7.3K** | **3.2 mo** | **<12 mo** | **✓ Exceeds** |

**Business Impact:** CAC payback <6 months indicates highly efficient acquisition, supporting rapid scaling

---

**KPI 3.2.3: Operating Margin (Profitability)**

**Definition:** Percentage of revenue remaining after all operating expenses (COGS, S&M, R&D, G&A).

**Calculation:**

```
Operating Margin (%) = [(Revenue - Operating Expenses) / Revenue] × 100

Operating expenses:
- COGS (direct retrofit/SLA costs)
- Sales & Marketing (customer acquisition, account management)
- R&D (product development, AI/ML improvement)
- G&A (finance, legal, HR, office)

```

**Target:**

- Year 1: -15% to -10% (growth-phase investment acceptable)
- Year 2: -5% to +5% (approach break-even)
- Year 3: 15-20% (mature profitability)

**Measurement:**

- Monthly P&L: Full operating expense categorization
- Trend: Identify path to profitability (operating leverage from ARR growth)

**Frequency:** Monthly reporting, quarterly analysis

**Accountability:** CFO (financial discipline), Operating leaders (cost efficiency)

**Example Tracking:**

| Year | Revenue | COGS | S&M | R&D | G&A | Op Expenses | Operating Margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026 (est) | $217M | $150M | $40M | $15M | $20M | $225M | -3.7% |
| 2027 (proj) | $410M | $280M | $65M | $25M | $35M | $405M | +1.2% |
| 2028 (proj) | $650M | $420M | $85M | $35M | $50M | $590M | +9.2% |

---

**KPI 3.2.4: Return on Invested Capital (ROIC - Capital Efficiency)**

**Definition:** How effectively TerraHash deploys capital to generate returns.

**Calculation:**

```
ROIC (%) = [NOPAT (Net Operating Profit After Tax)] / [Invested Capital] × 100

NOPAT = Operating Income × (1 - Tax Rate)
Invested Capital = Total Assets - Current Liabilities

```

**Target:**

- Year 2+: >20% ROIC (beating cost of capital)
- Exceptional: >30% ROIC

**Measurement:**

- Annual calculation in financial statements
- Benchmark against VC-funded SaaS companies (typical ROIC: 15-25%)

**Frequency:** Annual reporting

**Accountability:** CFO (capital allocation)

---

### 3.3 Market Traction & Competitive Positioning

**KPI 3.3.1: Market Share (MW Retrofitted)**

**Definition:** Percentage of addressable market (eligible for retrofit) that TerraHash has captured through completed projects.

**Calculation:**

```
Market Share (%) = (MW retrofitted by TerraHash) / (Total eligible MW market) × 100

TAM (Total Addressable Market): ~8-12 GW of air-cooled mining capacity eligible for retrofit (North America)

Example:
- 365 MW retrofitted YTD
- TAM: 10,000 MW
- Market share: 365/10,000 = 3.65%

```

**Target:**

- Year 1: 0.5-1% market share (50-100 MW)
- Year 2: 3-6% market share (300-600 MW)
- Year 3: 9-15% market share (900-1,500 MW)

**Measurement:**

- Project tracking: Cumulative MW retrofitted by TerraHash
- Market research: TAM estimates updated quarterly
- Competitive analysis: Estimate competitor retrofit volumes

**Frequency:** Quarterly reporting

**Accountability:** Sales/marketing (customer acquisition), Product (platform competitiveness)

---

**KPI 3.3.2: Brand Awareness & Industry Positioning**

**Definition:** Recognition of TerraHash Stack among mining operators and industry participants.

**Measurement:**

- Branded search volume: Google Trends, SEMrush (Bitcoin mining retrofit, liquid cooling miners)
- Industry publication mentions: Hashrate Index, Bitcoin Magazine, Mining Dispatch
- Industry event participation: Speaking slots at BitBlockBoom, Bitcoin Magazine conferences
- Analyst coverage: Mentions in mining/Bitcoin reports

**Target:**

- Year 1: Establish thought leadership in retrofit market
- Year 2: Industry-wide recognition as retrofit market leader
- Year 3: Considered alongside major public mining companies in industry discussions

**Measurement:**

- Monthly brand tracking: Search volume, publication mentions, event activity
- Annual review: Industry rankings, analyst recognition

**Frequency:** Monthly brand tracking, quarterly strategic review

**Accountability:** Marketing/communications (brand development)

---

**KPI 3.3.3: Customer Reference & Case Study Density**

**Definition:** Number of referenceable customers and published case studies demonstrating success.

**Calculation:**

```
Reference density = (Referenceable customers) / (Total customers) × 100

Example: 60 of 257 customers willing to be public references = 23.3% reference density

```

**Target:**

- Year 1: 20-30% reference density (strong customer satisfaction)
- Year 2: 40-50% reference density (market leader positioning)
- Year 3: 60%+ reference density (industry standard)

**Measurement:**

- Quarterly: Survey customers on willingness to serve as reference
- Published case studies: Track number and publishing venues
- Customer testimonials: Collect video/written testimonials for marketing

**Frequency:** Quarterly reference surveys, ongoing case study development

**Accountability:** Customer success (relationship building), Marketing (case study production)

**Example Tracking:**

| Quarter | Total Customers | References | Reference % | Case Studies | Target |
| --- | --- | --- | --- | --- | --- |
| Q1 2026 | 45 | 8 | 17.8% | 2 | 20% |
| Q2 2026 | 102 | 25 | 24.5% | 5 | 20% |
| Q3 2026 | 168 | 48 | 28.6% | 10 | 30% |
| Q4 2026 | 257 | 82 | 31.9% | 15 | 30% |

---

### 3.4 Customer Health & Retention

**KPI 3.4.1: Retention Rate (Customer Renewal)**

**Definition:** Percentage of customers who renew SLA contracts at end of term.

**Calculation:**

```
Retention Rate (%) = (Customers renewing / Customers eligible for renewal) × 100

Example: 35 of 40 customers due for renewal in Q4 renew contracts = 87.5% retention

```

**Target:**

- Year 1: 80%+ retention (strong initial satisfaction)
- Year 2+: 90%+ retention (industry-leading retention)

**Measurement:**

- Quarterly: Identify customers with expiring contracts (end of contract term)
- Track renewals vs. cancellations (churn)
- Cohort analysis: Retention by customer segment and vintage

**Frequency:** Monthly contract tracking, quarterly retention analysis

**Accountability:** Account managers (relationship management), Customer success (value delivery)

**Example Tracking:**

| Cohort | Customers | Exp. Q1 | Renewed | Not Renewed | Churn % | Retention % |
| --- | --- | --- | --- | --- | --- | --- |
| 2025 (Yr 1) | 20 | 20 | 18 | 2 | 10% | 90% |
| 2026 (Yr 1) | 45 | 12 | 11 | 1 | 8.3% | 91.7% |
| 2026 (Yr 2) | 65 | 8 | 8 | 0 | 0% | 100% |
| **Portfolio** | **130** | **40** | **37** | **3** | **7.5%** | **92.5%** |

**Business Impact:** Retention >90% indicates strong product-market fit; critical for SaaS revenue predictability

---

**KPI 3.4.2: Churn Rate (Customer Loss)**

**Definition:** Percentage of customers or revenue lost each period.

**Calculation:**

```
Customer Churn (%) = (Customers lost) / (Starting customers) × 100
Revenue Churn (%) = (ARR lost from churn) / (Starting ARR) × 100

Example:
- Starting ARR: $10M, 50 customers
- Lost customers: 3 (average $80K SLA each = $240K revenue)
- Customer churn: 3/50 = 6%
- Revenue churn: $240K/$10M = 2.4%

```

**Target:**

- Customer churn: <5% per month, <50% annually
- Revenue churn: <2% per month, <20% annually

**Measurement:**

- Monthly tracking: Identify customers churned and reason
- Categorize churn: Voluntary (dissatisfaction, bankruptcy) vs. involuntary (M&A, site closure)
- Early warning: Monitor at-risk customers (negative NPS, SLA misses, reduced utilization)

**Frequency:** Monthly churn analysis, quarterly retention strategy

**Accountability:** Customer success (early intervention), Account managers (escalation)

**Example Tracking:**

| Month | Starting Customers | Customer Churn | Revenue Churn | Reason |
| --- | --- | --- | --- | --- |
| Oct | 45 | 1 (2.2%) | $8K (1.1%) | Bankruptcy |
| Nov | 44 | 0 (0%) | $0 (0%) | Strong retention |
| Dec | 44 | 1 (2.3%) | $12K (1.3%) | Acquired (site exit) |
| Q4 Total | - | 2 (avg 1.5%) | $20K (avg 0.8%) | - |

---

**KPI 3.4.3: Upsell & Expansion Revenue (Account Growth)**

**Definition:** Revenue growth from existing customers through upsells (higher SLA tier), add-ons (treasury module), or expansion (additional sites).

**Calculation:**

```
Expansion revenue = Σ(Month-over-month SLA increases + New module adoptions)

Example:
- 20 customers upgrade from Gold ($5K/mo) to Platinum ($10K/mo) = $100K/month new revenue
- 10 customers adopt treasury module ($2K/mo) = $20K/month new revenue
- Total expansion: $120K/month

```

**Target:**

- Monthly expansion: $50-100K per 100 customers
- % of revenue from expansion: 5-10% (vs. new customer acquisition)

**Measurement:**

- Monthly: Track SLA tier upgrades, module adoptions, additional site retrofits
- Categorize: By customer segment and value proposition

**Frequency:** Monthly tracking, quarterly analysis

**Accountability:** Account managers (expansion selling), Product (value delivery enabling upsells)

**Example Tracking:**

| Month | Tier Upgrades | Module Adoption | Site Expansion | Total Expansion | New Customers | % of Growth |
| --- | --- | --- | --- | --- | --- | --- |
| Oct | $45K | $8K | $25K | $78K | $85K | 48% |
| Nov | $52K | $12K | $32K | $96K | $105K | 48% |
| Dec | $68K | $15K | $48K | $131K | $140K | 48% |
| **Q4** | **$165K** | **$35K** | **$105K** | **$305K** | **$330K** | **48%** |

**Business Impact:** Expansion revenue demonstrates customer success and creates predictable growth acceleration

---

## PART 4: KPI DASHBOARD & REPORTING

### Reporting Cadence

**Daily (Automated Dashboards):**

- Uptime %, efficiency (J/TH), incident count, MTTR
- NOC staffing, incident resolution rate
- SLA attainment status (by customer)

**Weekly (Executive Summary):**

- Key operational metrics
- Critical incidents and resolutions
- Revenue pipeline and customer updates

**Monthly (Full Board Reporting):**

- All operational, financial, and business KPIs
- Trend analysis and variance from targets
- Corrective actions and updates

**Quarterly (Strategic Review):**

- Market traction, competitive positioning, customer satisfaction
- Financial performance vs. plan
- OKR progress and adjustments

**Annual (Annual Plan & Investor Update):**

- Full-year performance vs. annual targets
- Multi-year trend analysis
- Updated strategic plan

### Success Dashboard: Target Metrics Summary

| KPI Category | Metric | Target | Status | Notes |
| --- | --- | --- | --- | --- |
| **Product** | J/TH Improvement | 20%+ | ✓ 23% avg | Exceeds target |
|  | Uptime Consistency | 99%+ | ✓ 99.3% | Strong |
|  | Auto-Resolution Rate | 85%+ | ✓ 95.2% | Exceptional |
| **Operational** | NPS | 55+ | ✓ 48 | Near target |
|  | CSAT | 4.4+ | ✓ 4.5 | Hit |
|  | SLA Attainment | 95%+ | ⚠️ 66% | Improvement needed |
|  | MTTR | <45 min | ✓ 47 min | Near |
| **Business** | ARR | $3-5M | ✓ $5.58M | Exceeds |
|  | Retrofit Revenue | $20-30M | ✓ $18.5M | Near |
|  | Gross Margin (blended) | 60-65% | ✓ 62% | Hit |
|  | Operating Margin | -10% to -15% | ✓ -3.7% | Better than target |
|  | Retention Rate | 80%+ | ✓ 92.5% | Exceptional |

---

## Conclusion

This comprehensive KPI framework provides clarity on what success looks like across Product, Operational, and Business dimensions. Regular monitoring against these targets enables:

1. **Data-Driven Decisions:** Identify issues early through trending, enabling course correction before major problems emerge
2. **Accountability:** Clear ownership of each KPI drives execution discipline across the organization
3. **Customer Transparency:** Objective measurement of value delivery builds trust and supports retention
4. **Strategic Guidance:** KPI trends inform product roadmap, market strategy, and resource allocation decisions

Success requires disciplined tracking, transparent reporting, and willingness to adjust strategy based on KPI insights.