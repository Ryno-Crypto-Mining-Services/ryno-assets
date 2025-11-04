# TerraHash Stack as a Service: Detailed Retrofit Use Cases

<aside>
💡

- **TerraHash Stack as a Service transforms existing bitcoin mining facilities through systematic retrofitting with liquid cooling, advanced firmware, and AI-powered management**
- **Detailed use cases demonstrate 16-36% hashrate improvements, 11-19% efficiency gains, and 16-24 month payback periods across diverse facility types**
- **Retrofit approach preserves existing hashboard investments while eliminating thermal throttling, reducing maintenance labor by 60%+, and achieving 99%+ uptime**
- **Phased deployment methodology minimizes operational disruption, with zone-by-zone conversions maintaining 80-90% facility hashrate during transitions**
- **Technology stack combines Chilldyne negative-pressure liquid cooling, BraiinsOS+ autotuning firmware, and TerraHash AI platform for comprehensive optimization**
- **Financial models show $2-12M annual profit improvements for 5-25 MW facilities, with 5-year NPVs ranging from $7-35M at 10% discount rates**
- **Strategic benefits include extended equipment lifespan (+50%), future-proofed competitiveness through multiple halvings, and foundations for heat recovery monetization**
- **Applicable across facility types: container-based operations, warehouse deployments, hybrid mixed-generation fleets, and facilities requiring immersion conversion pathways**
</aside>

# Executive Summary

This document provides comprehensive, scenario-based use cases demonstrating how TerraHash Stack as a Service transforms diverse existing bitcoin mining facilities through systematic retrofitting. Each use case includes baseline conditions, detailed transformation steps, technical specifications, timeline projections, financial analysis, and expected outcomes—providing actionable blueprints for facility operators considering infrastructure modernization.

---

## USE CASE 1: Container-Based Air-Cooled Facility Retrofit

### Baseline Facility Profile

**Operator Profile:** Regional Mining Operator (Persona 1)
**Location:** West Texas (hot climate, summer peak temps 95-110°F)
**Capacity:** 5 MW across 10x modified 40ft shipping containers
**Current Configuration:**

- 10 containers, each housing 60 Bitmain S19j Pro (100 TH/s) miners = 600 total miners
- Traditional air cooling: Internal fans + external evaporative cooling units
- Stock firmware with basic monitoring
- 60 PH/s baseline hashrate
- Power consumption: 5.1 MW (including cooling overhead)
- Infrastructure age: 3 years

**Current Performance Metrics:**

- Efficiency: 18.5 J/TH (at optimal conditions)
- Summer throttling: 25-30% hashrate reduction during peak heat (June-September)
- Actual annual uptime: 88% (seasonal downtime + failures)
- Effective annual hashrate: 52.8 PH/s (accounting for throttling and downtime)
- Maintenance labor: 4 FTE technicians
- Annual maintenance costs: $180,000

**Pain Points:**

- $850K annual revenue loss from summer throttling and downtime
- High noise levels (85+ dB) creating community complaints
- Excessive dust accumulation requiring weekly cleaning
- Fan failures causing ~15 miner outages per month
- Inability to safely overclock due to thermal constraints

### Retrofit Transformation Plan

**Phase 1: Engineering & Assessment (Weeks 1-2)**

**Site Survey Activities:**

- Infrared thermal imaging of all 10 containers during peak load
- Power quality analysis and load profiling
- Structural assessment of container foundations for CDU weight
- Network infrastructure audit and upgrade requirements
- Environmental monitoring (ambient temps, humidity, dust levels)

**Design Deliverables:**

- Container-by-container retrofit sequencing plan (phased deployment)
- Chilldyne CDU-1500 placement and coolant routing diagrams
- THS-4X21P-C55 modular chassis migration plan
- Electrical load rebalancing calculations
- Project timeline with critical path analysis

**Phase 2: Long-Lead Procurement (Weeks 2-4)**

**Equipment Orders:**

- 10x Chilldyne CDU-1500 units (1.5 MW cooling capacity each)[file:173][file:6]
- 720x THS-4X21P-C55 modular liquid-cooled chassis (20% expansion capacity)[file:173]
- 600x Chilldyne cold plates with quick-disconnect fittings
- 3,000L glycol coolant mixture (30% ethylene glycol/water)
- Flexible plastic coolant distribution tubing and manifolds
- 10x dry cooler heat rejection units (roof-mount or adjacent)

**Firmware & Management:**

- BraiinsOS+ licenses for 600 miners (per-chip autotuning)[web:77][web:80]
- TerraHash AI management platform deployment
- Network upgrades: 10Gb fiber backbone, managed switches

**Phase 3: Phased Container Retrofit (Weeks 5-12)**

**Container Conversion Process (per container, 1 week each):**

**Day 1-2: Preparation & Decommissioning**

- Power down miners in target container (maintains 90% facility hashrate)
- Remove S19j Pro miners from stock air-cooled cases
- Discard fans, casings, and obsolete components
- Clean and inspect hashboards, power supplies, control boards

**Day 3-4: Infrastructure Installation**

- Install Chilldyne CDU-1500 unit with 0.6m service clearance[file:6]
- Mount dry cooler on container roof or adjacent pad
- Install primary coolant loop: CDU → manifold → racks → return
- Route flexible plastic tubing through overhead cable trays
- Install rack-level coolant manifolds with quick-disconnects

**Day 5-6: Miner Migration & Integration**

- Mount hashboards into THS-4X21P-C55 chassis (3 boards per 4U chassis)
- Attach Chilldyne cold plates to ASIC chips (turbulator-enhanced design)[file:6]
- Install chassis into racks (12-15 chassis per rack, 60 per container)
- Connect quick-disconnect coolant fittings
- Install power distribution and network connectivity

**Day 7: Commissioning & Testing**

- Fill and pressurize coolant loop (negative pressure system)[file:6]
- Verify -25 to -4 Hg vacuum operation (leak-proof validation)
- Flash BraiinsOS+ with baseline autotuning profiles
- Power-on sequence and thermal stabilization (target: 50-60°C junction temp)
- 24-hour burn-in with performance validation
- Handoff to operations with container #1 complete

**Parallel Activities (Throughout Weeks 5-12):**

- AI management platform deployment on edge compute infrastructure
- Integration with existing power monitoring and security systems
- Technician training on liquid cooling maintenance and troubleshooting
- Documentation of as-built configurations and operational procedures

**Phase 4: Fleet-Wide Optimization (Weeks 13-16)**

**AI Platform Calibration:**

- 30-day baseline data collection across all 10 containers
- ML model training for predictive failure detection
- Per-miner autotuning optimization (frequency/voltage curves)
- Automated alert threshold configuration
- Integration with automated treasury management module

**Safe Overclocking Activation:**

- Gradual power increase from 3,250W → 3,600W per miner (10% increments)
- Thermal monitoring to maintain <65°C junction temps
- Hashrate validation: 100 TH/s → 120 TH/s per miner (+20%)
- Efficiency improvement: 18.5 J/TH → 15.0 J/TH (liquid cooling + firmware)[file:6][web:80]

### Technical Specifications: Post-Retrofit

**Cooling System:**

- Technology: Chilldyne CDU-1500 negative pressure direct-to-chip
- Cooling capacity: 15 MW total (1.5 MW per container)
- Coolant: 30% ethylene glycol/70% deionized water
- Flow rate: 400 GPM per CDU unit[file:6]
- Approach temperature: 3°C at full load[file:6]
- Operating pressure: -25 to -4 Hg (vacuum)[file:6]
- Heat rejection: 10x roof-mounted dry coolers

**Mining Hardware:**

- Configuration: 600 miners in THS-4X21P-C55 chassis
- Hashrate per miner: 120 TH/s (20% overclocked)
- Power per miner: 3,600W
- Total facility hashrate: 72 PH/s (+20% vs. baseline)
- Total power consumption: 2,160 kW miners + 100 kW cooling = 2,260 kW per container
- Facility power: 4.52 MW (11% reduction vs. air-cooled despite higher hashrate)

**Automation & Management:**

- Firmware: BraiinsOS+ with per-chip autotuning
- Management: TerraHash AI platform with predictive maintenance
- Monitoring: Real-time temperature, flow rate, power, hashrate
- Alerting: Automated incident detection and remediation
- Treasury: Automated BTC/stablecoin allocation module

### Financial Analysis

**Capital Investment:**

| Item | Unit Cost | Quantity | Total |
| --- | --- | --- | --- |
| Chilldyne CDU-1500 units | $180,000 | 10 | $1,800,000 |
| THS-4X21P-C55 chassis | $450 | 720 | $324,000 |
| Cold plates & fittings | $285 | 720 | $205,200 |
| Dry coolers & heat rejection | $25,000 | 10 | $250,000 |
| Coolant system (tubing, manifolds, pumps) | $15,000 | 10 | $150,000 |
| BraiinsOS+ licenses | $30 | 600 | $18,000 |
| AI management platform | $150,000 | 1 | $150,000 |
| Installation & commissioning | $35,000 | 10 | $350,000 |
| Network & infrastructure upgrades | - | - | $120,000 |
| **Total Retrofit Investment** | - | - | **$3,367,200** |
| Cost per MW | - | - | **$673,440/MW** |

**Operational Impact:**

| Metric | Before Retrofit | After Retrofit | Improvement |
| --- | --- | --- | --- |
| Hashrate (annual average) | 52.8 PH/s | 72 PH/s | +36% |
| Power consumption | 5.1 MW | 4.52 MW | -11% |
| Efficiency | 18.5 J/TH | 15.0 J/TH | -19% |
| Uptime | 88% | 99%+ | +11 percentage points |
| Maintenance labor (FTE) | 4.0 | 1.5 | -62% |
| Annual maintenance costs | $180,000 | $65,000 | -64% |

**Revenue & Profitability (assuming $0.06/kWh electricity, $65K BTC):**

| Metric | Before | After | Delta |
| --- | --- | --- | --- |
| Daily BTC mined | 0.237 BTC | 0.324 BTC | +0.087 BTC |
| Daily revenue | $15,405 | $21,060 | +$5,655 |
| Annual revenue | $5,623,000 | $7,687,000 | +$2,064,000 |
| Annual electricity cost | $2,680,000 | $2,375,000 | -$305,000 |
| Annual maintenance | $180,000 | $65,000 | -$115,000 |
| **Annual profit improvement** | - | - | **+$2,484,000** |
| **Payback period** | - | - | **16.2 months** |
| **5-year NPV (10% discount)** | - | - | **+$7.2M** |

### Expected Outcomes

**Performance Targets (Achieved within 90 days):**

- Hashrate: 72 PH/s sustained (no seasonal throttling)
- Uptime: 99.2% facility-level availability
- Efficiency: 15.0 J/TH (19% improvement)
- Junction temps: 50-60°C constant (vs. 65-80°C air-cooled)
- Noise: 60 dB (vs. 85+ dB), resolving community complaints

**Operational Improvements:**

- Zero summer throttling (eliminates $850K annual revenue loss)
- Predictive maintenance: 80%+ failure prediction accuracy 3-7 days in advance
- Automated remediation: 95% of incidents resolved without human intervention
- Maintenance labor reduction: 4 FTE → 1.5 FTE ($120K annual savings)
- Extended equipment lifespan: 24 months → 36+ months (+50%)

**Strategic Benefits:**

- Facility competitive through 2-3 network difficulty halvings
- Enables expansion to 6-7 MW within existing containers (density increase)
- Foundation for heat recovery monetization (greenhouse, district heating)
- Improved insurance rates due to leak-proof cooling technology
- Enhanced resale value for facility exit scenarios

---

## USE CASE 2: Large Warehouse Air-Cooled Retrofit

### Baseline Facility Profile

**Operator Profile:** Institutional Mining Company (Persona 2)
**Location:** Georgia (moderate climate, humidity challenges)
**Capacity:** 25 MW warehouse facility
**Current Configuration:**

- 50,000 sq ft industrial warehouse with hot/cold aisle design
- 7,200 Bitmain S19 series miners (mix of S19, S19j, S19 XP)
- Traditional air cooling: CRAC units + hot aisle containment
- Stock firmware on 90% of fleet, custom firmware on 10%
- Baseline hashrate: 750 PH/s
- Infrastructure age: 2-4 years (rolling deployment)

**Current Performance Metrics:**

- Average efficiency: 19.8 J/TH (fleet-weighted)
- Uptime: 91% (maintenance, failures, weather events)
- Cooling energy: 22% of total facility power (PUE 1.28)
- Maintenance staff: 18 FTE technicians + 4 managers
- HVAC maintenance: $420K annually
- Miner maintenance: $680K annually

**Pain Points:**

- Inconsistent performance across facility zones (hot spots, uneven airflow)
- High humidity in summer causing condensation and corrosion issues
- Excessive HVAC power consumption eating into margins
- Manual troubleshooting for 180-250 miner failures per month
- Difficulty recruiting and retaining qualified technicians
- Lack of real-time visibility into per-miner economics

### Retrofit Transformation Plan

**Phase 1: Facility Assessment & Zone Planning (Weeks 1-3)**

**Engineering Analysis:**

- 3D thermal mapping using FLIR infrared cameras (identify hot spots)
- Electrical infrastructure capacity analysis (panel-by-panel)
- Structural load calculations for coolant distribution infrastructure
- HVAC decommissioning plan and utility reclamation
- Network backbone upgrade requirements (40Gb spine, 10Gb leaf)

**Zone-Based Deployment Strategy:**
The 25 MW facility is divided into 5 zones (5 MW each) for phased retrofit:

- **Zone 1 (Weeks 4-7):** Pilot zone, newest equipment, highest performance
- **Zone 2-3 (Weeks 8-15):** Highest-density zones, greatest thermal challenges
- **Zone 4 (Weeks 16-19):** Mid-age equipment, moderate density
- **Zone 5 (Weeks 20-23):** Oldest equipment, lowest density, potential immersion path

**Phase-Gate Approval:** Executive review after Zone 1 completion validates ROI model and de-risks full facility rollout.

**Phase 2: Zone 1 Pilot Deployment (Weeks 4-7)**

**Infrastructure Installation:**

- Install 4x Chilldyne CDU-1500 units (6 MW total cooling capacity for 5 MW zone)
- Deploy modular rack systems with integrated coolant manifolds
- Install centralized glycol distribution and heat rejection system
- Upgrade electrical panels with smart PDUs and real-time monitoring
- Deploy edge compute cluster for AI management (Kubernetes on bare metal)

**Miner Migration (1,440 miners):**

- Remove miners from existing racks in 72-unit batches
- Migrate hashboards to THS-4X21P-C55 modular chassis
- Install Chilldyne cold plates with quick-disconnect fittings
- Mount chassis in new liquid-cooled rack systems (15 chassis per rack)
- Flash BraiinsOS+ with zone-specific autotuning profiles

**Zone 1 Commissioning:**

- 7-day thermal stabilization and performance validation
- AI platform baseline data collection
- Automated alert threshold calibration
- Technician training on Zone 1 systems
- Executive demonstration and phase-gate review

**Phase 3: Zones 2-5 Full Rollout (Weeks 8-23)**

**Parallel Deployment Strategy:**

- Two installation crews working on adjacent zones simultaneously
- Zone 2 & 3 deployment: Weeks 8-15 (highest priority, most challenging)
- Zone 4 deployment: Weeks 16-19 (mid-priority)
- Zone 5 deployment: Weeks 20-23 (oldest equipment, potential immersion)

**Zone 5 Alternative Path: Immersion Cooling**
For the oldest S19 (non-XP) equipment in Zone 5, evaluate immersion cooling retrofit:

- Deploy 12x Fog Hashing C6 or HashHouse immersion tanks (120 kW each)[web:19][web:25]
- Extend equipment lifespan by 18-24 months vs. air cooling
- Lower retrofit cost: $280K/MW vs. $420K/MW for direct-to-chip
- Heat recovery integration for adjacent industrial park or district heating

**Phase 4: AI Platform & Treasury Integration (Weeks 16-24)**

**AI Management Deployment:**

- Centralized monitoring dashboard aggregating all 7,200 miners
- ML model training on 30-60 days of facility-wide operational data
- Predictive maintenance deployment: 14-day advance failure warnings
- Automated remediation: miner reboots, pool failover, thermal adjustments
- Integration with ERP system (SAP) for financial reconciliation

**Treasury Management Module:**

- Automated BTC/stablecoin allocation based on risk profile (60% HODL target)
- Integration with institutional custody (Fortris or Fireblocks)
- Real-time cost-per-BTC tracking by zone and cohort
- Scenario-based reinvestment modeling (difficulty projections)
- Automated tax reporting and cost-basis tracking

**Phase 5: HVAC Decommissioning & Optimization (Weeks 24-26)**

**Legacy Infrastructure Removal:**

- Decommission and remove 18x CRAC units (sell or repurpose)
- Reclaim electrical capacity: 1.4 MW freed up for additional miners
- Remove hot/cold aisle containment infrastructure
- Simplify facility airflow to ambient ventilation only
- Realize immediate $95K/month electricity savings from HVAC removal

### Technical Specifications: Post-Retrofit

**Cooling System:**

- **Zones 1-4 (20 MW):** 16x Chilldyne CDU-1500 units (direct-to-chip)
- **Zone 5 (5 MW):** 12x Fog Hashing C6 immersion tanks (120 kW each)
- **Heat rejection:** Centralized cooling tower + dry cooler hybrid (1.2 MW backup)
- **Coolant:** 30% glycol/water (Zones 1-4), engineered dielectric fluid (Zone 5)
- **Total cooling capacity:** 26.5 MW (6% overhead)

**Mining Hardware:**

- **Zones 1-4:** 5,760 miners in THS-4X21P-C55 chassis, 20% overclocked
- **Zone 5:** 1,440 miners in immersion tanks, 15% overclocked
- **Total facility hashrate:** 950 PH/s (+27% vs. baseline)
- **Total power consumption:** 24.8 MW (including cooling)
- **PUE:** 1.04 (vs. 1.28 pre-retrofit)

**Automation:**

- **Firmware:** BraiinsOS+ fleet-wide with per-chip autotuning
- **Management:** TerraHash AI platform, centralized NOC dashboard
- **Monitoring:** Real-time per-miner telemetry (temperature, power, hashrate, efficiency)
- **Alerting:** Automated incident detection, triage, and remediation
- **Treasury:** Automated allocation, custody integration, tax reporting

### Financial Analysis

**Capital Investment:**

| Item | Cost | Notes |
| --- | --- | --- |
| Chilldyne CDU-1500 units (16x) | $2,880,000 | Zones 1-4 |
| Fog Hashing C6 tanks (12x) | $720,000 | Zone 5 immersion |
| THS-4X21P-C55 chassis (6,480x) | $2,916,000 | 20% expansion capacity |
| Cold plates, fittings, manifolds | $1,850,000 | Zones 1-4 |
| Cooling towers & heat rejection | $950,000 | Centralized system |
| BraiinsOS+ licenses (7,200x) | $216,000 | Fleet-wide |
| AI management platform (enterprise) | $450,000 | Includes NOC, treasury module |
| Electrical & rack infrastructure | $1,200,000 | PDUs, panels, racks |
| Installation & commissioning | $1,800,000 | 20-week deployment |
| **Total Retrofit Investment** | **$12,982,000** |  |
| **Cost per MW** | **$519,280/MW** |  |

**Operational Impact:**

| Metric | Before | After | Improvement |
| --- | --- | --- | --- |
| Hashrate (annual avg) | 682.5 PH/s | 950 PH/s | +39% |
| Power consumption | 31.9 MW | 24.8 MW | -22% |
| Efficiency | 19.8 J/TH | 15.6 J/TH | -21% |
| PUE | 1.28 | 1.04 | -19% |
| Uptime | 91% | 99%+ | +8 pp |
| Maintenance staff (FTE) | 22 | 8 | -64% |
| Annual maintenance cost | $1,100,000 | $380,000 | -65% |

**Revenue & Profitability (assuming $0.05/kWh, $65K BTC):**

| Metric | Before | After | Delta |
| --- | --- | --- | --- |
| Daily BTC mined | 3.07 BTC | 4.28 BTC | +1.21 BTC |
| Daily revenue | $199,550 | $278,200 | +$78,650 |
| Annual revenue | $72.8M | $101.5M | +$28.7M |
| Annual electricity cost | $13.97M | $10.86M | -$3.11M |
| Annual maintenance | $1.10M | $0.38M | -$0.72M |
| **Annual profit improvement** | - | - | **+$32.53M** |
| **Payback period** | - | - | **4.8 months** |
| **3-year NPV (12% discount)** | - | - | **+$72.4M** |

### Expected Outcomes

**Performance Targets (Achieved within 120 days):**

- Hashrate: 950 PH/s sustained across all zones
- Uptime: 99.3% facility-level (99.5% Zones 1-4, 98.5% Zone 5)
- Efficiency: 15.6 J/TH fleet-weighted average
- PUE: 1.04 (vs. 1.28 baseline, 19% cooling power reduction)
- Junction temps: 52-62°C constant across zones

**Operational Transformation:**

- Eliminate hot spot issues through superior thermal management
- Predictive maintenance: 85%+ accuracy, 7-14 day advance warning
- Labor reduction: 22 FTE → 8 FTE ($840K annual savings)
- Automated incident resolution: 97% without human intervention
- Extended equipment lifespan: 24 months → 34 months average

**Strategic Achievements:**

- Fleet standardization enables rapid integration of future acquisitions
- SOC2 Type II compliance achieved (institutional investor requirement)
- Integration with SAP ERP provides board-ready financial reporting
- Heat recovery pathway identified for Zone 5 (industrial co-generation)
- Facility positioned as institutional-grade for potential sale or expansion

---

## USE CASE 3: Institutional Portfolio Multi-Site Retrofit

### Baseline Facility Profile

**Operator Profile:** Institutional Mining Company (Persona 2)
**Location:** Multi-site portfolio (Texas, Wyoming, North Dakota)
**Capacity:** 120 MW across 6 facilities
**Current Configuration:**

- **Site A (TX):** 40 MW, air-cooled, 3 years old
- **Site B (TX):** 25 MW, air-cooled, 2 years old
- **Site C (WY):** 20 MW, basic immersion, 4 years old
- **Site D (ND):** 15 MW, air-cooled containers, 18 months old
- **Site E (TX):** 12 MW, air-cooled, acquired 6 months ago (distressed asset)
- **Site F (WY):** 8 MW, air-cooled, 5 years old (legacy)

**Fleet Composition:**

- 32,000+ total miners (mix: S17, S19, S19j Pro, S19 XP, T21)
- Heterogeneous firmware (stock, BraiinsOS, VNish, custom)
- Inconsistent monitoring systems (3 different DCIM platforms)
- Decentralized operations (site-level management, no unified NOC)

**Current Performance Metrics:**

- Average efficiency: 20.2 J/TH (fleet-weighted, includes older hardware)
- Average uptime: 89% (site variability: 82-94%)
- Maintenance: 65 FTE across all sites ($3.9M annually)
- Quarterly hashrate per MW trending downward (-3% QoQ) due to aging fleet

**Strategic Drivers:**

- Board mandate: Achieve top-quartile efficiency metrics within 18 months
- Investor pressure: Improve cost per BTC by 25%+ to justify valuation
- Acquisition integration: Standardize Site E (distressed) within 90 days
- Compliance: Achieve SOC2 Type II for institutional mining services business
- Competitive positioning: Prepare for network difficulty increase post-halving

### Retrofit Transformation Strategy

**Phased Portfolio Approach: 18-Month Program**

**Phase 1: Pilot + Quick Wins (Months 1-4)**

- **Site D (ND, 15 MW):** Newest equipment, containerized, fastest retrofit
    - Deploy TerraHash containerized solution (identical to Use Case 1)
    - Validate ROI model and establish reference implementation
    - Train core retrofit team for deployment to other sites
- **Site E (TX, 12 MW):** Distressed asset acquisition, urgent turnaround
    - Rapid assessment and fixed-price retrofit contract
    - Priority: Stabilize operations and achieve institutional-grade metrics
    - Timeline: 90-day transformation (compressed schedule)

**Phase 2: Large Facility Standardization (Months 5-10)**

- **Site A (TX, 40 MW):** Flagship facility, largest scale
    - Zone-by-zone retrofit (8 zones, 5 MW each)
    - Serve as blueprint for large-facility playbook
    - Deploy enterprise NOC and treasury management hub
- **Site B (TX, 25 MW):** Second-largest, adjacent to Site A
    - Leverage Site A learnings and supply chain efficiencies
    - Parallel deployment with shared project management
    - Coordinate cooling tower infrastructure for potential shared services

**Phase 3: Legacy & Specialized Sites (Months 11-18)**

- **Site C (WY, 20 MW):** Existing basic immersion, needs standardization
    - Upgrade to TerraHash-compatible immersion (Fog Hashing C6 standardization)
    - Retrofit AI management and treasury modules
    - Integrate heat recovery for adjacent agricultural operations
- **Site F (WY, 8 MW):** Oldest site, S17-heavy fleet
    - Economic analysis: Retrofit vs. decommission
    - If retrofit: Immersion cooling to extend S17 lifespan 12-18 months
    - If decommission: Salvage infrastructure, redeploy to other sites

**Phase 4: Fleet Integration & Optimization (Months 12-18, parallel)**

- Centralized NOC deployment across all sites
- Unified AI management platform (single pane of glass)
- Enterprise treasury management with consolidated custody
- SOC2 Type II certification process and audit
- Board-level reporting dashboards and investor communications framework

### Site-Specific Retrofit Details

**Site A (TX, 40 MW) - Flagship Transformation**

**Baseline:** 10,800 S19/S19j Pro miners, air-cooled warehouse, 420 PH/s
**Target:** 580 PH/s (+38%), 99% uptime, 15.2 J/TH

**Retrofit Configuration:**

- 8 zones (5 MW each), phased deployment over 24 weeks
- 26x Chilldyne CDU-1500 units (38 MW cooling capacity)
- 12,960 THS-4X21P-C55 chassis (20% expansion capacity)
- BraiinsOS+ fleet-wide deployment with zone-specific tuning
- Enterprise NOC deployment (24/7 monitoring, Tier 1 SLA)
- **Investment:** $22.4M ($560K/MW)
- **Payback:** 5.2 months

**Site E (TX, 12 MW) - Rapid Turnaround**

**Baseline:** Distressed acquisition, 3,200 mixed miners (S17, S19), 85% uptime, poor maintenance
**Target:** 165 PH/s, 98% uptime, institutional-grade operations within 90 days

**Rapid Retrofit Approach:**

- Fixed-price contract with performance guarantees
- Prioritize highest-ROI equipment (S19 series first)
- Deploy 9x Chilldyne CDU-1500 units
- Accelerated installation: 3 crews working parallel zones
- **Investment:** $6.8M ($567K/MW)
- **Timeline:** 90 days (compressed)
- **Strategic value:** Demonstrates rapid turnaround capability for future acquisitions

**Site C (WY, 20 MW) - Immersion Standardization**

**Baseline:** Existing basic single-phase immersion (non-standard tanks), 520 PH/s
**Target:** 680 PH/s, standardized operations, heat recovery integration

**Retrofit Configuration:**

- Replace non-standard immersion with 48x Fog Hashing C6 tanks (standardized)[web:19][web:25]
- Install heat recovery infrastructure for adjacent greenhouse complex
- Deploy TerraHash AI management platform
- **Investment:** $11.2M ($560K/MW)
- **Heat recovery revenue:** $320K annually (greenhouse heating)
- **Payback:** 6.1 months (including heat recovery)

**Site F (WY, 8 MW) - Legacy Equipment Decision**

**Economic Analysis:**

- Retrofit cost: $4.8M ($600K/MW, higher due to S17 complexity)
- Equipment remaining life: 12-18 months maximum
- Alternative: Decommission, reallocate infrastructure to Site A/B expansion
- **Decision:** Partial retrofit (50% of capacity) + begin phased decommissioning
- **Salvage value:** $1.2M (electrical panels, cooling, racks)

### Portfolio-Wide Technical Specifications

**Unified Cooling Architecture:**

- **Primary:** Chilldyne CDU-1500 direct-to-chip (Sites A, B, D, E)
- **Secondary:** Fog Hashing C6 immersion (Site C standardized, Site F partial)
- **Total cooling capacity:** 128 MW (7% overhead across portfolio)

**Fleet Configuration:**

- **Active miners:** 31,500 (post Site F decommissioning)
- **Chassis:** 35,000 THS-4X21P-C55 units (includes expansion capacity)
- **Total hashrate:** 3,650 PH/s (+42% vs. baseline 2,570 PH/s)
- **Total power:** 119 MW (includes cooling, vs. 153 MW baseline with air cooling)

**Centralized Management:**

- **NOC:** Enterprise 24/7 operations center (Site A hub, remote monitoring all sites)
- **Firmware:** 100% BraiinsOS+ standardization across portfolio
- **AI Platform:** Unified TerraHash management (single pane of glass)
- **Treasury:** Consolidated custody (Fortris), automated allocation (65% HODL target)
- **Compliance:** SOC2 Type II certification achieved Month 16

### Financial Analysis: Portfolio-Wide

**Capital Investment Summary:**

| Site | Capacity | Investment | Timeline | Cost/MW |
| --- | --- | --- | --- | --- |
| Site A (TX) | 40 MW | $22,400,000 | 24 weeks | $560K/MW |
| Site B (TX) | 25 MW | $13,750,000 | 20 weeks | $550K/MW |
| Site C (WY) | 20 MW | $11,200,000 | 18 weeks | $560K/MW |
| Site D (ND) | 15 MW | $8,250,000 | 16 weeks | $550K/MW |
| Site E (TX) | 12 MW | $6,800,000 | 12 weeks | $567K/MW |
| Site F (WY) | 4 MW | $2,400,000 | 14 weeks | $600K/MW |
| NOC & Treasury | Portfolio | $3,200,000 | - | - |
| **Total** | **116 MW** | **$68,000,000** | **18 months** | **$586K/MW** |

**Operational Impact (Portfolio-Wide):**

| Metric | Before | After | Improvement |
| --- | --- | --- | --- |
| Hashrate | 2,570 PH/s | 3,650 PH/s | +42% |
| Power consumption | 153 MW | 119 MW | -22% |
| Efficiency | 20.2 J/TH | 15.5 J/TH | -23% |
| Uptime | 89% | 99%+ | +10 pp |
| Maintenance staff | 65 FTE | 22 FTE | -66% |
| Annual maintenance | $3.9M | $1.32M | -66% |

**Revenue & Profitability (assuming $0.05/kWh, $65K BTC):**

| Metric | Before | After | Delta |
| --- | --- | --- | --- |
| Daily BTC mined | 11.57 BTC | 16.44 BTC | +4.87 BTC |
| Daily revenue | $752,050 | $1,068,600 | +$316,550 |
| Annual revenue | $274.5M | $390.0M | +$115.5M |
| Annual electricity | $67.0M | $52.1M | -$14.9M |
| Annual maintenance | $3.9M | $1.32M | -$2.58M |
| **Annual profit improvement** | - | - | **+$132.98M** |
| **Payback period (portfolio)** | - | - | **6.1 months** |
| **3-year NPV (12% discount)** | - | - | **+$298M** |

### Expected Outcomes & Strategic Impact

**Operational Excellence:**

- Unified operations achieving 99%+ uptime across portfolio
- Centralized NOC reducing labor costs by $2.58M annually
- Predictive maintenance preventing 85%+ of failures fleet-wide
- Standardized fleet simplifying spare parts inventory and logistics

**Financial Performance:**

- Cost per BTC reduction: 35% (exceeds board mandate of 25%)
- Quarterly hashrate per MW improvement: +42% vs. declining baseline
- Energy consumption reduction: 34 MW freed for expansion or resale
- Top-quartile efficiency metrics achieved within 18-month target

**Institutional Positioning:**

- SOC2 Type II certification enables institutional mining services offering
- Board-ready reporting and investor dashboards enhance transparency
- Standardized operations facilitate rapid integration of future acquisitions
- Heat recovery at Site C demonstrates ESG commitment and revenue diversification

**Competitive Advantage:**

- Fleet positioned to remain profitable through 2-3 difficulty halvings
- Expansion capacity: 12 MW immediate growth within existing infrastructure
- Acquisition readiness: Proven playbook for rapid distressed asset turnaround (Site E)
- Strategic optionality: Infrastructure supports pivot to AI/HPC if mining economics deteriorate

---

## USE CASE 4: Energy Producer Turnkey Facility Management

### Baseline Facility Profile

**Operator Profile:** Energy Producer / Co-Location Provider (Persona 3)
**Location:** Montana (hydro + wind renewable energy complex)
**Capacity:** 18 MW mining facility (co-located at power generation site)
**Parent Company:** Regional utility with 500 MW renewable generation portfolio
**Current Configuration:**

- Purpose-built data center facility adjacent to 75 MW hydroelectric dam
- 4,800 Whatsminer M30S+ and M50S+ miners
- Basic air cooling with evaporative cooling assistance
- Stock firmware, limited automation
- Mining as grid demand response and curtailment monetization strategy

**Current Performance Metrics:**

- Hashrate: 540 PH/s
- Uptime: 87% (frequent grid integration issues, manual curtailment response)
- Internal mining expertise: 2 FTE (limited blockchain/mining knowledge)
- Reliance on external consultants: $420K annually
- Difficulty monetizing waste heat (rural location, limited offtake)

**Strategic Objectives:**

- Minimize internal resource allocation (<5% FTE commitment)
- Maintain focus on core energy business (mining as ancillary revenue)
- Achieve guaranteed uptime SLA for board confidence
- Integrate with existing grid management (SCADA) and curtailment protocols
- Explore heat reuse for industrial or agricultural applications

### Retrofit Transformation: Turnkey Operations Handoff

**Phase 1: Comprehensive Facility Assessment (Weeks 1-3)**

**TerraHash Assessment Team Deliverables:**

- Technical due diligence: facility condition, equipment inventory, infrastructure assessment
- Grid integration analysis: SCADA protocols, curtailment response requirements
- Heat recovery feasibility study: Identify potential offtake partners (greenhouses, lumber drying, aquaculture)
- Operational gap analysis: Compare current vs. institutional-grade standards
- Financial modeling: ROI projections with sensitivity analysis

**Client Decision Framework:**

- Fixed-price retrofit proposal with performance guarantees
- Guaranteed uptime SLA (99%+ with financial remedies)
- White-glove integration with existing utility operations
- Optional: Full operational management (mining-as-a-service)

**Phase 2: Retrofit & Infrastructure Modernization (Weeks 4-16)**

**Cooling System Upgrade:**

- Install 13x Chilldyne CDU-1500 units (19.5 MW cooling capacity)
- Migrate 4,800 miners to THS-4X5M-C55 chassis (custom for Whatsminer architecture)
- Deploy centralized heat recovery system with 85% thermal capture
- Integrate with facility SCADA for automated thermal management

**Automation & Grid Integration:**

- Deploy TerraHash AI management platform with SCADA integration
- Implement automated curtailment response (sub-second load shedding capability)
- Install demand response protocols for frequency regulation participation
- BraiinsOS+ deployment with dynamic power scaling

**Heat Recovery Infrastructure:**

- Install 2.5 MW heat recovery system with external heat exchangers
- Partner identification and offtake agreements (greenhouse complex, 8 miles)
- Heat distribution piping and metering infrastructure
- Contractual framework: $18/MMBtu heat sales (vs. $0 baseline)

**Phase 3: Operational Handoff & Managed Services (Weeks 17+)**

**TerraHash Platinum SLA Service:**

- **24/7 NOC Monitoring:** Remote management from TerraHash centralized operations
- **On-Site Presence:** 1 FTE TerraHash technician (vs. 2 FTE client staff previously)
- **Automated Curtailment:** Integration with utility dispatch system (5-second response)
- **Predictive Maintenance:** Parts inventory and automated RMA processing
- **Monthly Reporting:** Executive dashboards for client board presentations

**Client Retained Responsibilities:**

- Facility security and physical access control
- Utility-side electrical infrastructure maintenance
- Strategic decision-making (expansion, equipment refresh, treasury policy)
- Quarterly business reviews with TerraHash account team

### Technical Specifications: Post-Retrofit

**Cooling System:**

- Technology: Chilldyne CDU-1500 direct-to-chip liquid cooling
- Cooling capacity: 19.5 MW total (13 units)
- Heat recovery: 85% thermal capture (15.3 MW recoverable heat)
- Integration: SCADA-controlled with automated thermal management

**Mining Hardware:**

- Configuration: 4,800 Whatsminer M30S+/M50S+ in THS-4X5M-C55 chassis
- Hashrate per miner: M30S+ 112 TH/s, M50S+ 136 TH/s (fleet average: 125 TH/s, +12% overclock)
- Total facility hashrate: 600 PH/s (+11% vs. baseline)
- Total power consumption: 18.2 MW (including cooling)

**Grid Integration:**

- Automated curtailment response: <5 second load reduction (0-100% capacity)
- Frequency regulation: ±2 Hz response capability
- SCADA integration: Real-time power consumption reporting to utility dispatch
- Demand response participation: ERCOT/MISO programs (revenue diversification)

**Heat Recovery System:**

- Thermal capture capacity: 15.3 MW (85% of mining heat)
- Heat delivery temperature: 70-85°C (suitable for greenhouse, industrial)
- Annual heat production: 134,000 MMBtu
- Heat sales revenue: $2.41M annually ($18/MMBtu contract)

### Financial Analysis

**Capital Investment:**

| Item | Cost | Notes |
| --- | --- | --- |
| Chilldyne CDU-1500 units (13x) | $2,340,000 | Direct-to-chip cooling |
| THS-4X5M-C55 chassis (5,400x) | $2,430,000 | 12% expansion capacity |
| Cold plates, fittings, manifolds | $1,380,000 | Whatsminer architecture |
| Heat recovery system | $980,000 | 85% capture, 15.3 MW |
| BraiinsOS+ licenses (4,800x) | $144,000 | Fleet-wide deployment |
| AI management platform | $280,000 | SCADA integration |
| SCADA integration & automation | $420,000 | Utility-grade systems |
| Installation & commissioning | $950,000 | 12-week deployment |
| **Total Retrofit Investment** | **$8,924,000** |  |
| **Cost per MW** | **$495,778/MW** |  |

**Managed Services Pricing:**

- **Base infrastructure fee:** $45,000/month ($540K annually)
- **Performance fee:** 3.5% of gross mining revenue
- **Heat recovery management:** 8% of heat sales revenue
- **Estimated annual fee:** $1.92M (3-year contract, Year 1)

**Operational Impact:**

| Metric | Before | After | Improvement |
| --- | --- | --- | --- |
| Hashrate | 540 PH/s | 600 PH/s | +11% |
| Uptime | 87% | 99.2% | +12 pp |
| Internal staff (FTE) | 2.0 | 0.1 | -95% |
| External consultant costs | $420K | $0 | -100% |
| Heat monetization | $0 | $2.41M | New revenue |

**Revenue & Profitability (client perspective, $0.03/kWh captive power, $65K BTC):**

| Metric | Before | After | Delta |
| --- | --- | --- | --- |
| Daily BTC mined | 2.43 BTC | 2.70 BTC | +0.27 BTC |
| Daily mining revenue | $157,950 | $175,500 | +$17,550 |
| Annual mining revenue | $57.65M | $64.06M | +$6.41M |
| Annual heat revenue | $0 | $2.41M | +$2.41M |
| **Total annual revenue** | **$57.65M** | **$66.47M** | **+$8.82M** |
| Annual electricity cost | $4.73M | $4.78M | +$0.05M |
| TerraHash managed services fee | $0 | $1.92M | -$1.92M |
| Internal labor + consultants | $0.64M | $0.06M | -$0.58M |
| **Annual net benefit** | - | - | **+$7.27M** |
| **Payback period** | - | - | **14.7 months** |
| **3-year NPV (10% discount)** | - | - | **+$16.8M** |

### Expected Outcomes & Strategic Value

**Client Internal Impact:**

- Resource allocation: 2 FTE → 0.1 FTE (95% reduction, <5% commitment target achieved)
- Management complexity: Eliminated daily mining operations oversight
- Board confidence: Guaranteed 99%+ uptime SLA with financial remedies

**Grid Integration Excellence:**

- Automated curtailment response: <5 second load reduction (vs. 15-30 minutes manual)
- Frequency regulation participation: $280K annual ancillary services revenue
- SCADA integration: Real-time visibility for utility dispatch coordination
- Demand response optimization: Maximize revenue during grid stress events

**Heat Recovery Value Creation:**

- New revenue stream: $2.41M annually (vs. $0 baseline)
- Greenhouse partnership: 8-mile heat distribution network
- Environmental benefit: Offset 12,000 tons CO2 annually (natural gas displacement)
- Strategic positioning: "Net-positive energy" facility for regulatory/PR benefits

**Operational Transformation:**

- Institutional-grade operations: 99.2% uptime, predictive maintenance, automated remediation
- Consultant elimination: $420K annual savings, no external dependencies
- Expansion optionality: Infrastructure supports 22 MW capacity (22% expansion ready)
- Exit flexibility: Proven operations enable potential sale or JV opportunities

**Risk Mitigation:**

- Performance guarantees: TerraHash assumes operational risk
- SLA financial remedies: Client protected against underperformance
- Managed services model: Fixed monthly costs vs. variable consultant fees
- Technology refresh: TerraHash responsible for maintaining competitive efficiency

---

## USE CASE 5: Distressed Asset Rapid Turnaround

### Baseline Facility Profile

**Operator Profile:** Distressed Asset Acquirer (Persona 4)
**Location:** Kentucky (low-cost electricity region)
**Capacity:** 35 MW facility (acquired at auction)
**Acquisition Context:**

- Previous operator bankruptcy (overleveraged, poor operational execution)
- Facility acquired at $0.18/W (vs. $0.50-0.70/W replacement cost)
- Equipment age: 2-4 years, mix of S19/T19 models
- Infrastructure condition: Moderate neglect, requires immediate remediation

**Current State at Acquisition:**

- 9,400 miners (60% operational, 40% offline due to failures/neglect)
- Actual hashrate: 420 PH/s (vs. 700 PH/s theoretical if fully operational)
- Air cooling system: Poorly maintained, multiple HVAC failures
- Firmware: Stock, no optimization or automation
- Uptime: ~65% (frequent outages, thermal issues, power quality problems)
- Maintenance backlog: 3,800 miners require repair/refurbishment

**Acquisition Objectives:**

- Rapid stabilization and value creation (6-12 month hold period)
- Achieve institutional-grade operations to attract strategic buyer or tenant
- Demonstrate 2x EBITDA improvement for exit valuation
- Fixed-price retrofit with performance guarantees (minimize execution risk)

### Rapid Turnaround Strategy: 90-Day Transformation

**Phase 1: Emergency Stabilization & Assessment (Days 1-14)**

**Immediate Actions (Days 1-7):**

- Deploy TerraHash rapid response team (4 engineers + project manager)
- Facility-wide audit: Electrical infrastructure, cooling systems, miner inventory
- Triage operational miners: Identify high-value equipment for immediate optimization
- Emergency repairs: Power quality issues, critical HVAC failures
- Baseline performance documentation (hashrate, uptime, efficiency by zone)

**Retrofit Design & Fixed-Price Proposal (Days 8-14):**

- Zone-based retrofit plan: Prioritize highest-ROI equipment first
- Equipment disposition:
    - **Tier 1 (5,600 S19 XP/Pro):** Full liquid cooling retrofit
    - **Tier 2 (2,400 S19):** Refurbish + air cooling optimization
    - **Tier 3 (1,400 T19/failed units):** Salvage for parts, decommission
- Fixed-price contract: $18.9M turnkey retrofit with 99% uptime guarantee
- Performance guarantee: Achieve 850 PH/s within 90 days or financial remedy

**Phase 2: Parallel Execution - Equipment & Infrastructure (Days 15-75)**

**Track 1: Tier 1 Equipment Liquid Cooling Retrofit (Days 15-65)**

- Deploy 26x Chilldyne CDU-1500 units (expedited procurement, 3-week lead time)
- Migrate 5,600 S19 XP/Pro miners to THS-4X21P-C55 chassis
- Install direct-to-chip liquid cooling infrastructure
- BraiinsOS+ deployment with aggressive overclocking profiles (+18%)
- Target: 750 PH/s from Tier 1 equipment

**Track 2: Tier 2 Equipment Refurbishment (Days 15-60)**

- Repair/refurbish 2,400 S19 miners (hashboard replacement, cleaning, testing)
- Optimize existing air cooling (repair HVAC, improve airflow management)
- Basic firmware upgrade (BraiinsOS standard, conservative tuning)
- Target: 120 PH/s from Tier 2 equipment

**Track 3: Infrastructure Remediation (Days 15-75)**

- Electrical system upgrades: Panel replacements, power quality improvements
- Network infrastructure: Deploy 40Gb backbone, managed switches, monitoring
- Security systems: Access control, surveillance, alarm integration
- Safety & compliance: Fire suppression, emergency systems, OSHA compliance
- Facility aesthetics: Painting, signage, landscaping (institutional presentation)

**Phase 3: Commissioning & Optimization (Days 76-90)**

**System Integration & Performance Validation:**

- TerraHash AI management platform deployment
- Automated monitoring and alerting across all zones
- 7-day thermal stabilization and efficiency optimization
- Performance validation: Achieve 870 PH/s total (target: 850 PH/s)

**Institutional-Grade Documentation:**

- As-built engineering drawings and technical documentation
- Operations manuals and maintenance procedures
- SOPs for routine operations and emergency response
- Financial reporting framework (cost per BTC, uptime, efficiency KPIs)
- Compliance documentation (electrical, safety, environmental permits)

**Marketing & Exit Preparation:**

- Professional facility photography and virtual tour
- Investment memorandum for strategic buyer outreach
- Operations performance data package (30-60-90 day reports)
- Proof of institutional-grade operations for tenant or buyer diligence

### Technical Specifications: Post-Retrofit

**Cooling System:**

- **Tier 1 (26 MW):** 26x Chilldyne CDU-1500 units, direct-to-chip liquid cooling
- **Tier 2 (7 MW):** Optimized air cooling, repaired HVAC systems
- **Total cooling capacity:** 33 MW (includes redundancy)

**Mining Hardware:**

- **Active miners:** 8,000 (5,600 liquid-cooled + 2,400 air-cooled)
- **Total hashrate:** 870 PH/s (750 PH/s Tier 1 + 120 PH/s Tier 2)
- **Total power consumption:** 31.8 MW (including cooling)
- **Efficiency:** 15.4 J/TH (Tier 1), 19.2 J/TH (Tier 2), 16.2 J/TH blended

**Automation & Management:**

- **Firmware:** BraiinsOS+ on Tier 1 (aggressive tuning), BraiinsOS standard on Tier 2
- **Management:** TerraHash AI platform with predictive maintenance
- **Monitoring:** Real-time dashboards, automated alerting, NOC integration

### Financial Analysis: Acquisition to Exit

**Acquisition & Retrofit Investment:**

| Item | Cost | Notes |
| --- | --- | --- |
| **Facility acquisition** | $6,300,000 | $0.18/W for 35 MW capacity |
| Chilldyne CDU-1500 units (26x) | $4,680,000 | Tier 1 liquid cooling |
| THS-4X21P-C55 chassis (6,320x) | $2,844,000 | 12% expansion capacity |
| Equipment refurbishment (Tier 2) | $1,680,000 | Hashboard repair, cleaning |
| Infrastructure remediation | $2,800,000 | Electrical, network, facility |
| BraiinsOS+ licenses (8,000x) | $240,000 | Fleet-wide deployment |
| AI management platform | $320,000 | Rapid deployment package |
| Installation & commissioning | $2,100,000 | Expedited schedule |
| Project management & contingency | $1,236,000 | 10% buffer for unknowns |
| **Total Investment** | **$22,200,000** |  |
| **Effective cost per MW** | **$634,286/MW** |  |

**Operational Performance: Pre vs. Post Retrofit**

| Metric | At Acquisition | Post-Retrofit (Day 90) | Improvement |
| --- | --- | --- | --- |
| Operational miners | 5,600 (60%) | 8,000 (85%) | +43% |
| Hashrate | 420 PH/s | 870 PH/s | +107% |
| Uptime | 65% | 99%+ | +34 pp |
| Power consumption | 35 MW | 31.8 MW | -9% |
| Efficiency | 22.5 J/TH | 16.2 J/TH | -28% |

**Exit Valuation Analysis (12-Month Hold Period):**

**Baseline Valuation (at acquisition):**

- Acquisition price: $6.3M ($0.18/W)
- Distressed facility, poor operations, high execution risk

**Target Exit Valuation (Month 12):**

- **Method 1: Replacement Cost:** 31 MW operating @ $0.55/W = $17.05M
- **Method 2: Revenue Multiple:** $42.8M annual revenue x 0.45 = $19.26M
- **Method 3: EBITDA Multiple:** $15.2M EBITDA x 2.5 = $38.0M (institutional buyer)
- **Conservative Exit Price:** $28-32M (split between revenue and EBITDA methods)

**Investment Returns:**

| Metric | Value |
| --- | --- |
| Total investment | $22.2M (acquisition + retrofit) |
| Conservative exit price | $30.0M (midpoint) |
| Gross profit | $7.8M |
| Holding period EBITDA (12 months) | $15.2M |
| Total value creation | $23.0M |
| **Gross IRR** | **104%** (12-month hold) |
| **Cash-on-Cash Return** | **104%** |

**Annual Operating Performance (Post-Retrofit, Stabilized):**

| Metric | Annual Value |
| --- | --- |
| Revenue (mining) | $42.8M ($65K BTC, $0.04/kWh electricity) |
| Electricity cost | $11.1M |
| Maintenance & operations | $1.8M |
| SLA support (TerraHash Gold) | $0.72M |
| **Annual EBITDA** | **$15.2M** |
| **EBITDA Margin** | **35.5%** |

### Expected Outcomes & Exit Strategy

**Operational Transformation (Days 1-90):**

- Hashrate: 420 PH/s → 870 PH/s (+107%)
- Uptime: 65% → 99%+ (+34 percentage points)
- Efficiency: 22.5 J/TH → 16.2 J/TH (-28%)
- Institutional-grade operations achieved within 90-day target

**Value Creation Milestones:**

- **Month 3:** Retrofit complete, performance guarantees met
- **Month 6:** 6-month operational track record, institutional tenant secured
- **Month 9:** Formal marketing process initiated, buyer diligence begins
- **Month 12:** Exit completed, 104% IRR achieved

**Buyer Profile & Exit Options:**

**Option 1: Strategic Sale to Institutional Miner**

- Target buyers: Publicly traded miners seeking capacity expansion
- Valuation: $28-32M (0.9-1.0x replacement cost)
- Appeal: Turnkey operations, no execution risk, immediate hashrate contribution

**Option 2: Long-Term Lease to Enterprise Tenant**

- Structure: 5-year lease with purchase option
- Lease rate: $2.8M annually (10% yield on exit valuation)
- Acquirer retains ownership, tenant operates under TerraHash SLA

**Option 3: Hold & Operate (if market conditions unfavorable)**

- Stabilized EBITDA: $15.2M annually
- ROI: 68% annually on total investment
- Flexibility: Can hold through unfavorable market, exit when valuations improve

**Key Success Factors:**

- Fixed-price contract: Eliminated execution risk, predictable costs
- Performance guarantees: TerraHash assumes operational risk for 90-day ramp
- Rapid transformation: 90-day turnaround creates competitive advantage vs. traditional rehab (6-9 months)
- Institutional positioning: Professional documentation and operations enable premium exit valuation
- Strategic partnerships: TerraHash ongoing SLA provides comfort to buyer/tenant

---

## Comparative Analysis: Retrofit Use Cases

### Summary Table

| Use Case | Facility Type | Capacity | Investment | Cost/MW | Payback | Hashrate Gain | Key Differentiator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **UC1: Container Retrofit** | Regional operator, 10 containers | 5 MW | $3.37M | $674K/MW | 16.2 mo | +36% | Eliminates summer throttling, rapid deployment |
| **UC2: Warehouse Retrofit** | Institutional, large facility | 25 MW | $12.98M | $519K/MW | 4.8 mo | +39% | Zone-based phasing, minimal disruption |
| **UC3: Portfolio Retrofit** | Multi-site institutional | 116 MW | $68.0M | $586K/MW | 6.1 mo | +42% | Fleet standardization, SOC2 compliance |
| **UC4: Energy Producer** | Hydro co-location, turnkey | 18 MW | $8.92M | $496K/MW | 14.7 mo | +11% | Heat recovery, SCADA integration, managed services |
| **UC5: Distressed Asset** | Rapid turnaround, exit play | 31 MW | $15.9M | $634K/MW | 12 mo | +107% | Fixed-price, 90-day transformation, 104% IRR |

### Key Insights

**Cost Efficiency:**

- Lowest cost/MW: Energy producer ($496K) due to existing infrastructure and simple integration
- Highest cost/MW: Distressed asset ($634K) due to infrastructure neglect and expedited timeline
- Optimal range: $520-590K/MW for institutional facilities with good baseline conditions

**Payback Period Drivers:**

- Fastest payback: Warehouse (4.8 months) due to high hashrate gain and electricity cost savings
- Moderate payback: Regional/portfolio (6-16 months) reflecting standard economics
- Extended payback: Energy producer (14.7 months) due to lower electricity cost base (less savings opportunity)

**Hashrate Improvement:**

- Highest gain: Distressed asset (+107%) due to poor baseline (only 60% operational at acquisition)
- Standard gain: 36-42% for well-operated facilities (container, warehouse, portfolio)
- Modest gain: Energy producer (+11%) focused on operational efficiency vs. raw capacity expansion

**Strategic Value Propositions:**

- **Container:** Eliminates seasonal throttling, enables safe overclocking, rapid ROI
- **Warehouse:** Minimal operational disruption, zone-based phasing, institutional positioning
- **Portfolio:** Fleet standardization, acquisition integration playbook, SOC2 compliance
- **Energy Producer:** Turnkey management, heat recovery, SCADA integration, <5% internal resource allocation
- **Distressed Asset:** Rapid value creation, institutional-grade transformation, attractive exit multiples

---

## Conclusion

These five use cases demonstrate the versatility and economic viability of TerraHash Stack as a Service across diverse facility types, operator profiles, and strategic objectives. Whether eliminating seasonal throttling for regional operators, standardizing multi-site institutional portfolios, enabling turnkey operations for energy producers, or rapidly transforming distressed assets for private equity exits—the TerraHash retrofit platform delivers measurable improvements in efficiency, uptime, profitability, and strategic positioning.

The consistent themes across all use cases include:

- 20-40% efficiency improvements through liquid cooling and autotuning firmware
- 99%+ uptime through predictive maintenance and automated remediation
- 60-75% labor reduction through AI-driven management
- 15-24 month payback periods (faster for larger facilities with higher baseline costs)
- Institutional-grade operations enabling strategic optionality (expansion, exit, heat recovery, compliance)

For facility operators evaluating retrofitting decisions, these use cases provide detailed blueprints for transformation planning, investment sizing, timeline expectations, and outcome validation.