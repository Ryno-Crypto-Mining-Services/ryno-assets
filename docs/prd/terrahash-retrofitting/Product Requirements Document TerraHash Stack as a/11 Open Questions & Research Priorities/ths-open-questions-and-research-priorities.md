# TerraHash Stack as a Service: Open Questions & Research Priorities

<aside>
💡

- **Critical unresolved questions span product, go-to-market, financial, operational, strategic, and regulatory domains** that require systematic research before becoming business-critical risks
- **Product uncertainties center on packaging strategy, bear market viability, and technology dependencies**—particularly whether to remain reliant on Chilldyne cooling or develop proprietary solutions
- **Customer acquisition economics remain unclear** with unvalidated assumptions about CAC ($50-500K), sales cycles (60-180 days), and optimal LTV:CAC ratios across three distinct personas
- **Pricing strategy requires validation** between fixed-fee SLA, revenue-share, and performance-based models, with customer preferences and unit economics still uncertain
- **Competitive positioning needs refinement** as TerraHash must choose between technology leadership, cost leadership, service excellence, or integrated platform differentiation
- **Channel strategy remains undecided** between direct sales, channel partnerships, or hybrid approaches, with unknown partner economics and potential channel conflict risks
- **Each question is prioritized by impact and urgency** with defined research methodologies and decision points tied to specific phases of the 5-year roadmap
- **Resolution timeline ranges from immediate (30-60 days) to medium-term (6-12 months)** depending on criticality to business model validation and scaling decisions
</aside>

## Executive Overview

While TerraHash Stack as a Service represents a compelling business opportunity with validated technology and proven customer demand, numerous **critical questions** remain unanswered across **product**, **go-to-market**, **financial**, **operational**, **strategic**, and **regulatory** domains. This document systematically identifies these open questions, categorizes them by priority and urgency, and establishes research methodologies to resolve uncertainties before they become business-critical risks.

Each question is evaluated on:

- **Impact**: Critical (business-threatening if unresolved), High (major strategic implications), Medium (meaningful tactical impact), Low (informational)
- **Urgency**: Immediate (must resolve within 30-60 days), Near-term (resolve within 3-6 months), Medium-term (resolve within 6-12 months)
- **Research Method**: Customer interviews, market analysis, technical proof-of-concept, financial modeling, expert consultation, pilot program
- **Decision Point**: What decision depends on answering this question?

The resolution of these questions will shape TerraHash's product roadmap, go-to-market strategy, capital allocation decisions, and long-term competitive positioning.

---

## PART 1: PRODUCT OPEN QUESTIONS

### 1.1 Core Product Value Proposition & Differentiation

**Question 1.1.1: What is the optimal product packaging strategy—unbundled services vs. integrated platform?**

**Current Hypothesis:** TerraHash should offer tiered SLA packages (Silver, Gold, Platinum, Enterprise) bundling retrofit + ongoing services, with optional add-on modules (treasury, heat recovery, MaaS).

**Open Questions:**

- **Unbundled Demand:** What percentage of customers would purchase retrofit-only (no ongoing SLA) vs. integrated platform? Does unbundled demand represent 10%, 30%, or 50%+ of TAM?
- **Module Adoption Sequencing:** Do customers adopt treasury module before or after experiencing base AI platform? What is typical time-to-adoption for additional modules?
- **Price Elasticity:** How sensitive are customers to SLA pricing? Would 20% price reduction drive 50%+ volume increase, or is demand relatively inelastic?
- **Competitive Alternatives:** Are customers comparing TerraHash to equipment vendors (Chilldyne), firmware providers (Braiins), mining services companies (Core Scientific), or building in-house solutions?

**Research Method:**

1. **Customer Interviews (N=20-30):** Structured interviews with mix of existing customers and qualified prospects across all three personas
2. **Conjoint Analysis:** Survey-based pricing sensitivity analysis with 100+ respondents
3. **Competitive Win/Loss Analysis:** Interview lost deals to understand competitive positioning
4. **A/B Pricing Test:** Test different packaging/pricing models with 10-15 pilot customers in Phase 1

**Decision Point:** Finalize product packaging and pricing strategy for Phase 2 scaling (Month 6-7)

**Impact:** High | **Urgency:** Immediate (60 days)

---

**Question 1.1.2: Can TerraHash deliver sufficient ROI to justify customer investment in bear market conditions?**

**Current Hypothesis:** 18-24 month payback period is acceptable to customers when BTC price is $80K+, but may not be compelling if BTC crashes to $40-50K range.

**Open Questions:**

- **Bear Market Viability:** At what BTC price does TerraHash retrofit ROI become unattractive (payback >36 months)? Is there a "floor price" below which no customers will invest?
- **Efficiency Thresholds:** If TerraHash delivers 25% efficiency improvement (vs. 35% best-case), is ROI still compelling? Where is the minimum viable efficiency gain threshold?
- **Operating Cost Sensitivity:** How much do electricity costs need to decrease (or how much do efficiency gains need to increase) to maintain 18-month payback if BTC price drops 50%?
- **Competitive Alternatives:** In bear market, do customers prefer CapEx-light alternatives (firmware-only upgrades, pool optimization) vs. TerraHash's CapEx-intensive retrofit approach?

**Research Method:**

1. **Scenario Modeling:** Build detailed financial models for customer ROI under bear ($40K BTC), base ($100K), bull ($150K+) scenarios
2. **Historical Analysis:** Study 2022 bear market miner behavior—which companies invested in efficiency vs. shut down operations?
3. **Customer Interviews:** Ask customers "at what BTC price would you NOT invest in TerraHash retrofit?" to establish price floor
4. **Pilot Program:** Offer flexible pricing (revenue share, performance-based) to test alternative business models in bear market

**Decision Point:** Establish minimum BTC price threshold for customer acquisition; develop contingency pricing models for bear market (Month 3-4)

**Impact:** Critical | **Urgency:** Immediate (30-60 days)

---

**Question 1.1.3: What is the optimal feature prioritization for AI platform development?**

**Current Hypothesis:** Predictive maintenance (80-85% accuracy) is highest-value AI feature, followed by fleet optimization, then market intelligence.

**Open Questions:**

- **Feature Value Ranking:** Do customers value predictive maintenance >fleet optimization >market intelligence, or is ranking different? What features drive most retention and expansion revenue?
- **Accuracy Thresholds:** Is 80% predictive maintenance accuracy "good enough," or do customers demand 90%+ before trusting AI recommendations?
- **False Positive Tolerance:** How many false positives (predicted failures that don't occur) will customers tolerate before losing trust in AI platform?
- **Competitive Benchmarks:** What AI capabilities do competitors offer? Is TerraHash ahead, at parity, or behind industry best practices?

**Research Method:**

1. **Customer Feature Voting:** Survey existing customers to rank feature priorities (Kano model analysis)
2. **Usage Analytics:** Track which AI platform features customers use most frequently, correlate with retention/expansion
3. **Competitive Benchmarking:** Analyze competitor AI platforms (if available), identify feature gaps
4. **A/B Testing:** Deploy alternative AI models to subset of customers, measure impact on satisfaction and expansion revenue

**Decision Point:** Finalize AI platform product roadmap for next 12-18 months (Month 4-5)

**Impact:** High | **Urgency:** Near-term (3-6 months)

---

### 1.2 Technology & Architecture Decisions

**Question 1.2.1: Should TerraHash develop proprietary cooling technology or remain dependent on Chilldyne?**

**Current Hypothesis:** Chilldyne partnership is sufficient for Phase 1-2, but TerraHash should develop backup cooling technology or in-house capability by Phase 3 to reduce single-source dependency.

**Open Questions:**

- **Development Cost:** What is total cost (CapEx + time + talent) to develop proprietary CDU technology competitive with Chilldyne? Is it $5M, $15M, or $50M+ investment?
- **Time to Market:** How long would it take TerraHash to design, validate, and commercialize proprietary cooling technology? 12 months, 24 months, or 36+ months?
- **Performance Parity:** Can TerraHash realistically achieve performance parity with Chilldyne's 10+ years of cooling R&D? Or would proprietary solution be 10-20% less efficient?
- **Strategic Alternatives:** Are there viable alternative CDU vendors (Fog Hashing, GRC, LiquidStack) that could serve as backup suppliers without requiring proprietary development?

**Research Method:**

1. **Technology Feasibility Study:** Engage mechanical engineering consultants to assess technical feasibility, cost, timeline for proprietary CDU development
2. **Alternative Vendor Evaluation:** Evaluate 3-5 alternative cooling vendors on performance, cost, reliability, supply capacity
3. **Financial Modeling:** Build NPV analysis comparing Chilldyne dependency vs. proprietary development vs. dual-sourcing
4. **Strategic Review:** Quarterly executive team assessment of Chilldyne relationship health and backup technology needs

**Decision Point:** Decide whether to initiate proprietary cooling R&D program by Month 12-18 (Phase 2-3 transition)

**Impact:** High | **Urgency:** Medium-term (6-12 months)

---

**Question 1.2.2: What is the optimal firmware strategy—Braiins-only, multi-firmware support, or in-house development?**

**Current Hypothesis:** BraiinsOS is sufficient for Phase 1-2, but TerraHash should develop firmware flexibility (VNish, Hive OS support) and eventually in-house capability.

**Open Questions:**

- **Multi-Firmware Complexity:** How much engineering effort required to support 2-3 firmware platforms vs. Braiins-only? Is it 20% additional complexity or 100%+ (effectively doubling engineering workload)?
- **Customer Preference:** Do customers have strong firmware preferences (e.g., "we only use VNish"), or are they firmware-agnostic as long as performance delivered?
- **In-House Development ROI:** What is business case for in-house firmware capability? Would $2-3M annual investment (2-3 firmware engineers) yield sufficient cost savings or competitive differentiation?
- **Open Source vs. Proprietary:** Should TerraHash develop open source firmware (community goodwill, transparency) or proprietary (competitive moat, IP protection)?

**Research Method:**

1. **Customer Interviews:** Ask customers about firmware preferences, willingness to switch firmware for better performance/cost
2. **Engineering Assessment:** Task engineering team with estimating effort/cost for multi-firmware support and in-house development
3. **Competitive Analysis:** Research which firmware platforms competitors support; identify market differentiation opportunities
4. **Pilot Program:** Test VNish or Hive OS integration with 3-5 pilot customers to validate multi-firmware approach

**Decision Point:** Finalize firmware strategy (Braiins-only vs. multi-firmware) by Month 9-12 (Phase 2)

**Impact:** Medium-High | **Urgency:** Near-term (3-6 months)

---

**Question 1.2.3: How should TerraHash balance edge compute vs. cloud-based AI platform architecture?**

**Current Hypothesis:** Hybrid architecture with cloud-based ML training and edge inference at customer facilities via ServerDomes partnership is optimal.

**Open Questions:**

- **Edge Compute ROI:** Do benefits of edge compute (lower latency, data sovereignty, offline resilience) justify cost vs. pure cloud architecture? Is ServerDomes partnership cost-effective?
- **Customer Deployment Complexity:** Does edge compute deployment add significant project complexity (hardware installation, network configuration, troubleshooting)? Would pure cloud be simpler?
- **Data Privacy Requirements:** What percentage of customers have data sovereignty requirements mandating on-premises edge compute vs. cloud-only acceptable?
- **Scalability Trade-offs:** Does edge compute architecture limit TerraHash's ability to rapidly deploy platform improvements (must update edge nodes vs. instant cloud deployment)?

**Research Method:**

1. **Architecture Cost Analysis:** Compare total cost of ownership (TCO) for edge vs. cloud-only architecture at scale (1,000 MW deployed)
2. **Customer Interviews:** Survey customers on data privacy requirements, edge vs. cloud preferences
3. **Performance Testing:** Measure latency, reliability, incident response times for edge vs. cloud deployments
4. **Pilot Program:** Deploy pure cloud architecture to subset of customers, compare operational metrics vs. edge deployments

**Decision Point:** Finalize AI platform architecture strategy (edge vs. cloud balance) by Month 6-9 (Phase 1-2 transition)

**Impact:** Medium | **Urgency:** Near-term (3-6 months)

---

## PART 2: GO-TO-MARKET OPEN QUESTIONS

### 2.1 Customer Acquisition & Sales Strategy

**Question 2.1.1: What is the optimal customer acquisition cost (CAC) and sales cycle for each customer persona?**

**Current Hypothesis:** Regional operators = $50-100K CAC, 60-90 day sales cycle; Institutional miners = $150-300K CAC, 90-120 day cycle; Energy producers = $300-500K CAC, 120-180 day cycle.

**Open Questions:**

- **CAC by Channel:** What is CAC for direct sales vs. channel partners vs. inbound marketing vs. referrals? Which channels most cost-effective?
- **Sales Cycle Variation:** Do some customers have 30-day sales cycles while others take 12+ months? What drives variation—deal size, customer sophistication, competitive dynamics?
- **LTV:CAC Ratio Targets:** What LTV:CAC ratio is sustainable for TerraHash? Is 3:1 adequate, or does business model require 5:1 or higher?
- **Payback Period:** How long does it take to recover CAC—6 months, 12 months, 18 months? Does payback period vary by customer persona or SLA tier?

**Research Method:**

1. **Sales Pipeline Analysis:** Track detailed metrics for first 50 customers (CAC, cycle length, win rate) by persona and channel
2. **Cohort Analysis:** Calculate LTV for early customer cohorts, project LTV:CAC ratios
3. **Channel Experimentation:** Test multiple acquisition channels (conferences, Google Ads, LinkedIn, partnerships) and measure ROI
4. **Competitive Benchmarking:** Research SaaS/infrastructure company benchmarks for CAC, LTV:CAC, payback period

**Decision Point:** Establish target CAC and channel mix for Phase 2 scaling (Month 6-9)

**Impact:** Critical | **Urgency:** Immediate (60-90 days)

---

**Question 2.1.2: Should TerraHash pursue direct sales model, channel partnerships, or hybrid approach?**

**Current Hypothesis:** Direct sales for large institutional and energy producer customers; channel partners (consultants, equipment vendors) for regional operators.

**Open Questions:**

- **Channel Partner Economics:** What revenue share or commission structure attracts quality channel partners without destroying TerraHash economics? Is 10%, 20%, or 30% appropriate?
- **Channel Conflict:** If TerraHash sells direct AND through channels, how to avoid channel conflict and partner dissatisfaction?
- **Partner Capacity:** Do sufficient channel partners exist with relevant customer relationships and credibility in bitcoin mining market?
- **Control vs. Scale Trade-off:** Does channel strategy enable faster scaling (more reach) but sacrifice customer experience control and margins?

**Research Method:**

1. **Channel Partner Research:** Identify and interview 10-15 potential channel partners (consultants, equipment vendors) to assess interest, capabilities, economics
2. **Pilot Program:** Launch pilot channel program with 2-3 partners, track lead quality, conversion rates, customer satisfaction
3. **Economics Modeling:** Build financial model comparing direct sales vs. channel economics under different growth scenarios
4. **Competitive Analysis:** Research how competitors (equipment vendors, mining services) structure channel programs

**Decision Point:** Finalize go-to-market channel strategy by Month 9-12 (Phase 2)

**Impact:** High | **Urgency:** Near-term (3-6 months)

---

**Question 2.1.3: What is optimal pricing strategy—fixed-fee, revenue-share, performance-based, or hybrid?**

**Current Hypothesis:** Fixed-fee SLA pricing ($5-10K/MW/month) is simplest and most predictable; revenue-share and performance-based pricing reserved for special situations (distressed operators, energy producers).

**Open Questions:**

- **Customer Preference:** Do customers prefer predictable fixed fees vs. variable revenue-share? Does preference vary by persona or financial situation?
- **Revenue-Share Economics:** If TerraHash charges 15-25% of gross mining revenue, what are expected revenues vs. fixed-fee model? Higher or lower?
- **Performance Risk:** In performance-based model (TerraHash guarantees minimum efficiency), what is risk of underperformance and financial penalties?
- **Competitive Differentiation:** Does flexible pricing (offering multiple models) differentiate TerraHash vs. competitors, or create confusion and complexity?

**Research Method:**

1. **Customer Interviews:** Survey 20-30 customers on pricing model preferences, willingness to share revenue data
2. **Financial Modeling:** Build detailed NPV models comparing fixed-fee vs. revenue-share vs. performance-based economics
3. **Pilot Program:** Test alternative pricing models with 5-10 customers in Phase 1, measure customer satisfaction and TerraHash profitability
4. **Competitive Analysis:** Research how mining services companies, equipment vendors price services

**Decision Point:** Finalize pricing strategy and models by Month 4-6 (Phase 1)

**Impact:** High | **Urgency:** Immediate (60-90 days)

---

### 2.2 Market Positioning & Competitive Strategy

**Question 2.2.1: How should TerraHash position against emerging competition—technology leader, cost leader, service excellence, or integrated platform?**

**Current Hypothesis:** Position as integrated platform combining best-in-class cooling, firmware, and AI management with superior customer service.

**Open Questions:**

- **Differentiation Sustainability:** Can TerraHash sustain technology leadership, or will competitors rapidly close gaps? What is sustainable competitive moat—technology, partnerships, operational excellence, or customer relationships?
- **Brand Positioning:** Should TerraHash emphasize sustainability (carbon-neutral mining), profitability (maximize ROI), innovation (AI-driven optimization), or reliability (99%+ uptime)?
- **Competitive Response:** How will competitors (equipment vendors, mining services, firmware providers) respond to TerraHash? Will they launch competing offerings, acquire TerraHash, or partner?
- **Market Expansion vs. Defense:** Should TerraHash aggressively pursue market share growth (lower prices, aggressive sales) or focus on defending early customer base and maximizing profitability?

**Research Method:**

1. **Customer Perception Research:** Survey customers and prospects on TerraHash brand perception vs. competitors (brand tracking study)
2. **Competitive Intelligence:** Systematic monitoring of competitor product launches, partnerships, pricing changes
3. **Strategic Planning Workshop:** Executive team and board strategic offsite to define competitive positioning and response strategies
4. **Industry Expert Interviews:** Consult with 5-10 mining industry experts, investors, analysts on competitive landscape evolution

**Decision Point:** Finalize competitive positioning strategy by Month 6-9 (Phase 1-2 transition)

**Impact:** Critical | **Urgency:** Near-term (3-6 months)

---

**Question 2.2.2: What is the optimal geographic expansion strategy—U.S. focus, North America (Canada), or international (Europe, Latin America, Asia)?**

**Current Hypothesis:** Focus on U.S. in Phase 1-2, expand to Canada in Phase 3, evaluate Europe and Latin America in Phase 4 based on market conditions.

**Open Questions:**

- **International TAM:** What is addressable market size in Canada (estimated 100-200 MW?), Europe, Latin America, Asia? Does international TAM justify expansion investment?
- **Regulatory Complexity:** How much more complex is regulatory compliance in Canada, EU vs. U.S.? Does complexity offset market opportunity?
- **Operational Challenges:** Can TerraHash effectively manage international operations (project delivery, NOC support, customer service) from U.S. headquarters, or does international expansion require local offices and staff?
- **Partnership Strategy:** Should TerraHash pursue direct international expansion vs. international partnerships or licensing agreements?

**Research Method:**

1. **Market Sizing Analysis:** Research bitcoin mining capacity and growth in Canada, Europe, Latin America, Asia; estimate TAM
2. **Regulatory Research:** Engage international legal consultants to assess regulatory complexity and compliance costs
3. **Customer Interviews:** Interview international mining operators to assess demand for TerraHash services
4. **Pilot Program:** Test international expansion with 1-2 Canadian customers in Phase 2, validate operational model before broader expansion

**Decision Point:** Decide whether to expand to Canada by Month 12-18 (Phase 2-3 transition)

**Impact:** Medium-High | **Urgency:** Medium-term (6-12 months)

---

## PART 3: FINANCIAL OPEN QUESTIONS

### 3.1 Unit Economics & Profitability

**Question 3.1.1: What are sustainable gross margins and operating margins at scale?**

**Current Hypothesis:** Retrofit services = 18-22% gross margin; SLA services = 70-80% gross margin; blended = 35-45% gross margin. Operating margin = 20-25% at scale (Year 3-4).

**Open Questions:**

- **Margin Erosion Risk:** Will competitive pressure force TerraHash to reduce prices, compressing margins from 35-45% to 20-30% or lower?
- **Cost Structure Scalability:** Can TerraHash achieve target operating margins (20-25%) or will hidden costs (NOC staffing, field support, customer acquisition) keep margins at 10-15%?
- **Pricing Power:** Does TerraHash have pricing power to increase SLA fees 5-10% annually, or is pricing effectively commoditized?
- **Module Attach Rates:** What percentage of customers adopt treasury, heat recovery, MaaS modules? Do high-margin modules drive blended margins from 35% to 50%+?

**Research Method:**

1. **Cohort Profitability Analysis:** Track detailed P&L for first customer cohorts; calculate gross and operating margins by customer, segment, SLA tier
2. **Cost Analysis:** Rigorous bottom-up cost modeling for scaled operations (1,000 MW); identify cost drivers and optimization opportunities
3. **Pricing Sensitivity:** Test price increases with subset of customers; measure churn and margin impact
4. **Competitive Benchmarking:** Research comparable SaaS, infrastructure, mining services companies for margin benchmarks

**Decision Point:** Finalize financial projections and margin targets for Series A/B fundraising (Month 3-6)

**Impact:** Critical | **Urgency:** Immediate (60-90 days)

---

**Question 3.1.2: What is optimal revenue mix between one-time retrofit and recurring SLA services?**

**Current Hypothesis:** Target 70-80% recurring revenue by Year 3, achieved through SLA services, treasury module, heat recovery revenue share.

**Open Questions:**

- **Valuation Impact:** Do investors value TerraHash as SaaS company (10-15x revenue multiple) or services company (2-4x revenue)? Does revenue mix dramatically impact valuation?
- **Cash Flow Trade-off:** Does pursuing recurring revenue sacrifice near-term cash flow (lower upfront retrofit margins) for long-term value (predictable SLA revenue)?
- **Customer Preference:** Do customers prefer one-time retrofit purchase vs. ongoing SLA commitment? Does forcing SLA reduce TAM?
- **Competitive Dynamics:** Do competitors focus on one-time equipment sales vs. recurring services? What is market norm?

**Research Method:**

1. **Investor Interviews:** Consult with 10-15 VC/growth equity investors to understand valuation frameworks for different revenue mixes
2. **Financial Modeling:** Build DCF models comparing revenue mix scenarios (50/50 vs. 70/30 vs. 80/20 recurring/one-time)
3. **Customer Research:** Survey customers on pricing model preferences (one-time vs. recurring)
4. **Competitive Benchmarking:** Analyze public mining services, datacenter infrastructure companies for revenue mix benchmarks

**Decision Point:** Finalize revenue mix strategy and financial targets for fundraising (Month 3-6)

**Impact:** Critical | **Urgency:** Immediate (60-90 days)

---

**Question 3.1.3: What is customer lifetime value (LTV) and retention economics?**

**Current Hypothesis:** Average customer lifetime = 5-7 years; LTV = $5-15M depending on facility size and SLA tier; 90%+ annual retention rate.

**Open Questions:**

- **Retention Drivers:** What drives customer retention—SLA performance, pricing, relationship, switching costs, or competitive alternatives? Which factors most predictive of churn?
- **Expansion Revenue:** What percentage of customers upgrade SLA tiers (Silver→Gold→Platinum) or adopt additional modules? What drives expansion?
- **Churn Risk Factors:** What early warning indicators predict customer churn—payment delays, low platform usage, declining hashrate, support tickets?
- **Lifetime Definition:** Is 5-7 year lifetime realistic, or do equipment refresh cycles (3-4 years) create natural churn events? Does TerraHash capture second retrofit cycle?

**Research Method:**

1. **Cohort Analysis:** Track retention, expansion, churn for first customer cohorts over 12-24 months
2. **Churn Analysis:** Conduct exit interviews with churned customers to understand root causes
3. **Predictive Modeling:** Build ML model to predict churn risk based on customer behavior, engagement, satisfaction metrics
4. **Customer Success Experimentation:** Test different customer success strategies (QBRs, executive sponsors, proactive optimization) and measure impact on retention

**Decision Point:** Establish LTV targets and retention strategies by Month 6-12 (Phase 1-2)

**Impact:** High | **Urgency:** Near-term (3-6 months)

---

### 3.2 Capital Requirements & Fundraising

**Question 3.2.1: How much capital does TerraHash need to raise, and what is optimal fundraising strategy?**

**Current Hypothesis:** $50-100M Series A to fund Phase 1-3 growth, achieve profitability by Year 3, maintain 18-24 months cash runway.

**Open Questions:**

- **Capital Efficiency:** Can TerraHash achieve same growth with $30-50M (aggressive cost discipline) vs. $50-100M (comfortable cash cushion)? What is risk/reward trade-off?
- **Fundraising Timing:** Should TerraHash raise large Series A upfront vs. staged financing (Series A → Series B) as milestones achieved? Which minimizes dilution?
- **Valuation Expectations:** What pre-money valuation is reasonable for TerraHash at Series A stage—$50M, $150M, $300M? How does valuation impact dilution and founder control?
- **Investor Type:** Should TerraHash target VC (growth focus), growth equity (profitability focus), strategic investors (mining companies, equipment vendors), or crypto/blockchain funds?

**Research Method:**

1. **Financial Modeling:** Build detailed 5-year financial model with multiple capital scenarios; calculate cash runway, dilution, equity ownership
2. **Fundraising Market Research:** Consult with investment bankers, VCs to understand market terms (valuation, dilution, governance)
3. **Strategic Investor Outreach:** Identify and approach potential strategic investors to gauge interest, terms
4. **Capital Efficiency Benchmarking:** Research comparable companies' capital raised, burn rates, time to profitability

**Decision Point:** Initiate Series A fundraising by Month 3-6 (Phase 1)

**Impact:** Critical | **Urgency:** Immediate (30-60 days)

---

**Question 3.2.2: Should TerraHash pursue debt financing (credit facility, equipment financing) in addition to equity?**

**Current Hypothesis:** Revolving credit facility ($20-40M) for working capital; potentially equipment financing for customer retrofits to reduce working capital burden.

**Open Questions:**

- **Debt Availability:** Can TerraHash access debt financing at Series A stage (typically requires profitability or strong unit economics)? What terms (interest rate, covenants)?
- **Debt vs. Equity Trade-off:** Does debt financing reduce equity dilution enough to justify interest expense and covenants? Or is equity simpler/better?
- **Asset-Based Lending:** Can TerraHash use inventory (CDUs, equipment) and receivables as collateral for asset-based lending (ABL)? What advance rates?
- **Equipment Financing:** Should TerraHash finance customer equipment purchases (offering financing as service to customers), or keep balance sheet simple?

**Research Method:**

1. **Lender Outreach:** Approach 5-10 venture debt lenders, asset-based lenders to understand availability, terms, covenants
2. **Financial Modeling:** Model debt vs. equity scenarios; calculate impact on dilution, cash flow, financial flexibility
3. **Covenant Analysis:** Assess whether TerraHash can reliably meet typical debt covenants (revenue, EBITDA, liquidity) given business volatility
4. **Peer Benchmarking:** Research how comparable companies use debt financing in early growth stages

**Decision Point:** Decide whether to pursue debt financing alongside Series A equity (Month 4-6)

**Impact:** Medium-High | **Urgency:** Near-term (3-6 months)

---

## PART 4: OPERATIONAL OPEN QUESTIONS

### 4.1 Delivery & Execution

**Question 4.1.1: Can TerraHash reliably achieve 75%+ on-time delivery rate at scale?**

**Current Hypothesis:** 70-75% on-time delivery achievable in Phase 1 (50-100 MW); maintaining this rate at 500-1,000 MW scale requires systematic process improvement and automation.

**Open Questions:**

- **Scalability Bottlenecks:** What operational bottlenecks emerge at 100 MW, 300 MW, 500 MW scale—project management capacity, technician availability, equipment supply, customer coordination?
- **Process Standardization:** Can TerraHash standardize retrofit process to reduce project duration from 14 weeks to 10 weeks? What process improvements have biggest impact?
- **Geographic Expansion:** Does expanding to new states/regions reduce on-time delivery (unfamiliar permitting, new contractor relationships) or improve it (regional hubs reduce travel time)?
- **Quality vs. Speed Trade-off:** Does optimizing for speed (shorter project timelines) compromise quality (higher defect rates, lower customer satisfaction)?

**Research Method:**

1. **Process Improvement Program:** Implement Lean/Six Sigma process improvement methodology; track cycle time, quality, customer satisfaction improvements
2. **Capacity Planning:** Build detailed capacity model projecting technician, PM, equipment needs at different growth scenarios
3. **Pilot Programs:** Test process improvements (pre-fabrication, modular installation, contractor training) with subset of projects
4. **Customer Feedback:** Regular customer surveys to assess satisfaction with delivery timeline, quality, communication

**Decision Point:** Establish operational delivery targets and capacity plan for Phase 2-3 scaling (Month 6-12)

**Impact:** High | **Urgency:** Near-term (3-6 months)

---

**Question 4.1.2: What is optimal technician staffing model—full-time employees vs. contractors vs. hybrid?**

**Current Hypothesis:** Hybrid model with core FTE team (20-30%) and contractor network (70-80%) provides flexibility and cost efficiency.

**Open Questions:**

- **Cost Structure:** Is FTE model (higher fixed costs, lower variable costs) more economical than contractor model (lower fixed, higher variable) at different scales?
- **Quality Control:** Do FTE technicians deliver higher quality work than contractors? Does quality gap justify higher FTE costs?
- **Scalability:** Does contractor model enable faster scaling (hire contractors on-demand) vs. FTE model (slower hiring, training)?
- **Retention Risk:** Do FTE technicians stay longer (lower turnover) vs. contractors (transient)? What is impact on project continuity and customer relationships?

**Research Method:**

1. **Cost Analysis:** Build detailed cost model comparing FTE vs. contractor costs at different scale scenarios
2. **Quality Analysis:** Track defect rates, customer satisfaction, rework for FTE-delivered vs. contractor-delivered projects
3. **Pilot Program:** Test different staffing models (FTE-heavy, contractor-heavy, hybrid) across different regions
4. **Retention Analysis:** Track FTE vs. contractor retention rates, training costs, project continuity

**Decision Point:** Finalize technician staffing strategy by Month 9-12 (Phase 2)

**Impact:** Medium-High | **Urgency:** Near-term (3-6 months)

---

### 4.2 Organizational Design & Talent

**Question 4.2.1: What is optimal organizational structure for scaling from 35 FTE to 200+ FTE?**

**Current Hypothesis:** Functional organization (Engineering, Operations, Sales, Finance) in Phase 1-2; transition to product/geographic matrix in Phase 3-4.

**Open Questions:**

- **Organizational Model:** Should TerraHash organize by function, geography, customer segment, or product line? What model best supports growth and customer satisfaction?
- **Span of Control:** What is optimal span of control for managers—5-7 direct reports (tight control) vs. 10-15 (leverage)? Does optimal span vary by function?
- **Centralization vs. Decentralization:** Should key functions (NOC, customer success, project management) be centralized (economies of scale) or decentralized (regional responsiveness)?
- **Leadership Hiring:** When should TerraHash hire VP-level leaders for each function—immediately, at 50 FTE, at 100 FTE? What triggers leadership hires?

**Research Method:**

1. **Organizational Design Workshop:** Engage organizational design consultant to assess current structure and recommend future state
2. **Benchmarking:** Research organizational structures of comparable high-growth infrastructure/SaaS companies
3. **Scenario Planning:** Model different organizational structures under different growth scenarios; assess trade-offs
4. **Leadership Assessment:** Conduct 360 reviews of current leadership team; identify gaps and hiring priorities

**Decision Point:** Finalize organizational structure and leadership hiring plan by Month 6-9 (Phase 1-2 transition)

**Impact:** High | **Urgency:** Near-term (3-6 months)

---

## PART 5: STRATEGIC OPEN QUESTIONS

### 5.1 Long-Term Strategic Direction

**Question 5.1.1: What is TerraHash's long-term strategic vision—mining services platform, diversified digital infrastructure, or acquisition target?**

**Current Hypothesis:** Build TerraHash as mining services platform through Phase 3-4; evaluate strategic alternatives (IPO, acquisition, continued growth) at $500M+ revenue scale.

**Open Questions:**

- **Market Evolution:** How will bitcoin mining industry evolve 5-10 years—consolidation (fewer, larger operators), fragmentation (many small operators), or AI/HPC pivot (miners become datacenter providers)?[web:305][web:306]
- **TerraHash Positioning:** Should TerraHash position as pure-play mining platform vs. diversified digital infrastructure company (mining + AI/HPC)? Does diversification increase or decrease value?[web:305][web:312]
- **Exit Strategy:** Is TerraHash building for IPO, strategic acquisition by mining company, acquisition by infrastructure company, or long-term private growth?
- **Competitive Endgame:** What is sustainable competitive position in mature market—high-volume/low-margin commodity provider vs. high-value/high-margin premium provider?

**Research Method:**

1. **Industry Trend Analysis:** Research long-term mining industry trends, expert forecasts, technology roadmaps[web:233][web:306]
2. **Strategic Planning:** Annual board/executive strategic offsite to assess market evolution and TerraHash positioning
3. **Investor Interviews:** Consult with VCs, growth equity, strategic investors on exit scenarios and valuation expectations
4. **Scenario Planning:** Develop 3-5 strategic scenarios for mining industry evolution; assess TerraHash response strategies

**Decision Point:** Articulate long-term strategic vision by Month 12-18 (Phase 2-3)

**Impact:** Critical | **Urgency:** Medium-term (6-12 months)

---

**Question 5.1.2: Should TerraHash pursue vertical integration (acquire Chilldyne, develop in-house capabilities) or remain focused pure-play platform?**

**Current Hypothesis:** Remain focused platform in Phase 1-3; consider selective vertical integration (Chilldyne acquisition, in-house firmware) in Phase 4 if strategic rationale compelling.

**Open Questions:**

- **Vertical Integration Value:** Would acquiring Chilldyne create significant strategic value (supply security, margin capture, technology control) or distract from core business?
- **Capital Allocation:** Is vertical integration best use of capital vs. geographic expansion, product development, or returning capital to shareholders?
- **Execution Risk:** Does TerraHash have capability to successfully integrate and operate acquired companies (manufacturing, firmware engineering)?
- **Market Timing:** If vertical integration is strategic goal, what is optimal timing—now (lock in relationships), later (after scale achieved), or never?

**Research Method:**

1. **M&A Analysis:** Engage investment bankers to assess Chilldyne valuation, acquisition financing, integration risks
2. **Strategic Value Assessment:** Model financial and strategic value of Chilldyne acquisition vs. status quo partnership
3. **Capability Assessment:** Evaluate TerraHash's organizational capacity to integrate and operate manufacturing business
4. **Alternative Strategies:** Evaluate alternatives to acquisition (equity investment, joint venture, exclusive partnership extension)

**Decision Point:** Decide whether to pursue Chilldyne acquisition or alternative strategic partnership by Month 18-24 (Phase 3)

**Impact:** High | **Urgency:** Medium-term (12-18 months)

---

**Question 5.1.3: How should TerraHash address AI/HPC pivot risk if bitcoin mining becomes less attractive?**

**Current Hypothesis:** Monitor AI/HPC opportunity but remain focused on bitcoin mining through Phase 3; maintain optionality for diversification if mining economics deteriorate.

**Open Questions:**

- **Mining vs. AI Economics:** Are mining facilities pivoting to AI/HPC because it's more profitable, or because mining profitability collapsed? What is long-term AI/HPC opportunity?[web:305][web:312]
- **TerraHash Capabilities:** Does TerraHash cooling/AI platform expertise transfer to AI/HPC datacenters, or would diversification require entirely new capabilities?
- **Competitive Position:** If TerraHash pursues AI/HPC, is it competing against established datacenter providers (Equinix, Digital Realty) with massive advantages?
- **Strategic Focus:** Does maintaining AI/HPC optionality distract from bitcoin mining focus, or is it prudent risk management?

**Research Method:**

1. **Market Analysis:** Research AI/HPC datacenter market opportunity, growth, competitive landscape[web:305][web:310][web:313]
2. **Customer Interviews:** Ask mining customers if they're considering AI/HPC pivot; understand decision drivers
3. **Capability Assessment:** Evaluate TerraHash's technical and commercial capabilities for AI/HPC market entry
4. **Pilot Program:** Test AI/HPC cooling optimization with 1-2 customers to validate technology transfer

**Decision Point:** Decide whether to pursue AI/HPC diversification by Month 18-24 (Phase 3)

**Impact:** Medium-High | **Urgency:** Medium-term (12-24 months)

---

## PART 6: REGULATORY OPEN QUESTIONS

### 6.1 Regulatory Evolution & Compliance

**Question 6.1.1: How will cryptocurrency mining regulations evolve over next 3-5 years, and how should TerraHash position?**

**Current Hypothesis:** Federal and state regulations will tighten (energy reporting, emissions restrictions, local permitting) but mining will remain legal in most jurisdictions through 2027-2028.

**Open Questions:**

- **Federal Regulation Probability:** What is probability of federal mining restrictions (energy surcharges, mandatory reporting, mining bans) by 2027? Low (10%), moderate (40%), or high (70%)?
- **State-Level Contagion:** If New York-style moratoria spread to 5-10+ states, does TAM shrink sufficiently to threaten business model?
- **International Safe Havens:** If U.S. regulations become restrictive, are there viable international markets (Canada, Latin America, Middle East) to sustain growth?
- **Compliance as Competitive Advantage:** Can TerraHash position strong compliance/sustainability as competitive advantage (attract ESG-focused investors, institutional customers)?

**Research Method:**

1. **Regulatory Monitoring:** Systematic tracking of federal/state legislative proposals, rulemaking, court decisions
2. **Industry Advocacy:** Active participation in Bitcoin Mining Council, industry associations to shape policy
3. **Expert Consultation:** Engage regulatory consultants, legal experts to assess regulatory evolution scenarios
4. **Scenario Planning:** Develop regulatory scenarios (permissive, moderate, restrictive) and TerraHash response strategies

**Decision Point:** Establish regulatory risk management strategy by Month 6-12 (Phase 1-2)

**Impact:** High | **Urgency:** Near-term (3-6 months)

---

**Question 6.1.2: Should TerraHash proactively pursue sustainability certifications (carbon-neutral, ESG) or wait for customer/regulatory demand?**

**Current Hypothesis:** Develop sustainability reporting capability in Phase 1-2; pursue formal certifications (carbon-neutral, ESG ratings) in Phase 3 if customer demand or regulatory requirements emerge.

**Open Questions:**

- **Customer Demand:** What percentage of customers value sustainability certifications enough to pay premium or choose TerraHash over competitors?
- **Investor Demand:** Do ESG-focused investors provide better valuations or access to capital that justify certification costs?
- **Certification ROI:** What is cost (time, consulting fees, operational changes) to achieve carbon-neutral or B-Corp certification? Does benefit justify cost?
- **Greenwashing Risk:** If TerraHash pursues sustainability positioning without strong evidence, does it create reputational risk?

**Research Method:**

1. **Customer Research:** Survey customers on importance of sustainability, willingness to pay for carbon-neutral operations
2. **Investor Research:** Interview ESG-focused investors to understand certification impact on valuation, fundraising
3. **Cost-Benefit Analysis:** Estimate costs for carbon-neutral certification, B-Corp certification; model ROI scenarios
4. **Competitive Analysis:** Research which competitors pursue sustainability positioning; assess market differentiation

**Decision Point:** Decide whether to pursue sustainability certifications by Month 12-18 (Phase 2-3)

**Impact:** Medium | **Urgency:** Medium-term (6-12 months)

---

## PART 7: OPEN QUESTIONS PRIORITIZATION MATRIX

### Critical Priority Questions (Must Resolve Immediately: 30-60 Days)

| Question | Category | Impact | Urgency | Research Method | Owner |
| --- | --- | --- | --- | --- | --- |
| Can TerraHash deliver sufficient ROI in bear market? | Product | Critical | Immediate | Scenario modeling, customer interviews | CEO, CFO |
| What is optimal CAC and sales cycle? | GTM | Critical | Immediate | Sales pipeline analysis, cohort analysis | CRO |
| What are sustainable gross/operating margins? | Financial | Critical | Immediate | Cohort profitability, cost analysis | CFO |
| What is optimal revenue mix (retrofit vs. recurring)? | Financial | Critical | Immediate | Investor interviews, financial modeling | CFO, CEO |
| How much capital to raise and from whom? | Financial | Critical | Immediate | Financial modeling, fundraising research | CFO, CEO |
| What is optimal product packaging/pricing? | Product | High | Immediate | Customer interviews, conjoint analysis | VP Product |

### High Priority Questions (Resolve Within 3-6 Months)

| Question | Category | Impact | Urgency | Research Method | Owner |
| --- | --- | --- | --- | --- | --- |
| Optimal feature prioritization for AI platform | Product | High | Near-term | Customer feature voting, usage analytics | VP Product, CTO |
| Direct sales vs. channel strategy | GTM | High | Near-term | Channel partner research, pilot program | CRO |
| Competitive positioning strategy | GTM | Critical | Near-term | Customer perception research, strategic planning | CEO |
| Customer LTV and retention economics | Financial | High | Near-term | Cohort analysis, churn analysis | VP Customer Success |
| Braiins-only vs. multi-firmware strategy | Product | Medium-High | Near-term | Customer interviews, engineering assessment | CTO |
| Organizational structure for scaling | Operational | High | Near-term | Org design workshop, benchmarking | CEO, VP HR |

### Medium Priority Questions (Resolve Within 6-12 Months)

| Question | Category | Impact | Urgency | Research Method | Owner |
| --- | --- | --- | --- | --- | --- |
| Proprietary cooling vs. Chilldyne dependency | Product | High | Medium-term | Feasibility study, alternative vendor evaluation | CTO, COO |
| Geographic expansion strategy (Canada, international) | GTM | Medium-High | Medium-term | Market sizing, regulatory research | CEO, VP Sales |
| Debt vs. equity financing strategy | Financial | Medium-High | Medium-term | Lender outreach, financial modeling | CFO |
| Regulatory evolution and positioning | Regulatory | High | Near-term | Regulatory monitoring, expert consultation | General Counsel |
| Long-term strategic vision and exit strategy | Strategic | Critical | Medium-term | Industry trend analysis, investor interviews | CEO, Board |

### Lower Priority Questions (Informational, Resolve 12+ Months)

| Question | Category | Impact | Urgency | Research Method | Owner |
| --- | --- | --- | --- | --- | --- |
| Vertical integration (Chilldyne acquisition) | Strategic | High | Long-term | M&A analysis, capability assessment | CEO, CFO |
| AI/HPC diversification opportunity | Strategic | Medium-High | Long-term | Market analysis, pilot program | CEO, CTO |
| Sustainability certifications ROI | Regulatory | Medium | Medium-term | Customer research, cost-benefit analysis | COO |

---

## CONCLUSION: RESEARCH EXECUTION FRAMEWORK

TerraHash faces numerous critical open questions that must be systematically resolved to de-risk the business model and enable confident scaling. Success requires:

1. **Prioritized Execution:** Focus immediately on Critical Priority questions (30-60 days); sequence High Priority questions (3-6 months); defer Lower Priority questions until Phase 2-3
2. **Disciplined Research:** Follow structured research methodologies; avoid "analysis paralysis" or premature decision-making without data
3. **Decision-Oriented:** Each question must lead to concrete decision and action; research for sake of research wastes time and capital
4. **Iterative Learning:** As market conditions evolve, continuously update open questions list; some questions become more/less critical over time
5. **Cross-Functional Ownership:** Assign clear ownership for each question; ensure adequate resources (time, budget, expertise) to resolve

Quarterly review of open questions status, emerging new questions, and research progress will ensure TerraHash maintains learning velocity and makes data-driven strategic decisions throughout hypergrowth journey.

---

**Document Control:**

- **Version:** 1.0
- **Date:** October 30, 2025
- **Next Review:** Monthly (Phase 1), Quarterly (Phase 2+)
- **Owner:** Chief Executive Officer / Chief Strategy Officer