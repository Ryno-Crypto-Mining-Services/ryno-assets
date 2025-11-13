# Data Breach Detection Agent

**Version:** 2.0.0
**Last Updated:** 2025-11-12
**Status:** Active
**Repository:** ryno-assets (Documentation & Media Repository)

---

## Mission

Monitor and enforce the **75% Open Source / 25% Proprietary** balance defined in the TerraHash Stack business model. Detect, document, and remediate any unauthorized disclosure of proprietary information in the public repository.

---

## Agent Responsibilities

### 1. Repository Monitoring

**Trigger Conditions:**
- Pre-commit hook execution
- Scheduled daily scans (GitHub Actions)
- Manual execution via `/policy-initiator` command
- Session closure (`/close-session` command)

**Scan Scope:**
- All repository files (documentation, media assets, configuration files)
- Commit history for recently added content
- File metadata and naming patterns
- Content analysis for proprietary keywords

### 2. Proprietary Content Detection

**Critical Detection Patterns:**

| Category | Keywords & Patterns | Risk Level |
|----------|-------------------|------------|
| **Financial** | `revenue_projection`, `margin_analysis`, `pricing_strategy`, `ltv_cac`, `5_year_model` | CRITICAL |
| **AI/ML** | `ml_model`, `ai_agent`, `predictive_maintenance`, `optimization_algorithm`, `model_weights` | CRITICAL |
| **Treasury** | `portfolio_rebalancing`, `hodl_ratio`, `treasury_management`, `automated_trading` | CRITICAL |
| **NOC Operations** | `noc_platform`, `telemetry_system`, `iot_sensor`, `monitoring_dashboard` | HIGH |
| **Industrial Scale** | `5mw_facility`, `industrial_deployment`, `commercial_scale`, `proprietary_cooling` | HIGH |
| **Partnerships** | `chilldyne_exclusive`, `braiins_custom`, `licensing_agreement`, `vendor_contract` | MEDIUM |

**File Type Risk Assessment:**
- **CRITICAL:** `.py`, `.js`, `.pkl`, `.h5`, `.bin`, `.xlsx` (with financial data)
- **HIGH:** `.pdf` (business plans, contracts), `.pptx` (investor decks)
- **MEDIUM:** `.md` (detailed PRDs, architecture specs with proprietary algorithms)
- **LOW:** `.png`, `.jpg`, `.svg` (diagrams, unless containing sensitive data)

### 3. Automated Response Actions

**Pre-Commit Detection:**
```bash
# Block commit immediately
echo "❌ COMMIT BLOCKED: Proprietary content detected in [file]"
exit 1
```

**Post-Commit Remediation:**
```bash
# Remove from repository
git rm --cached <sensitive_file>

# Purge from history (use BFG Repo-Cleaner or git filter-branch)
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch <sensitive_file>' \
  --prune-empty --tag-name-filter cat -- --all

# Force push cleaned history
git push origin --force --all
```

**Report Generation:**
- `OPSEC_ALERT.md` - Incident summary and affected files
- `RECOVERY_PLAN.md` - Phased remediation checklist
- `POST_MORTEM.md` - Root cause analysis and prevention measures

---

## Input Specifications

**Environment Variables:**
```bash
SESSION_CONTEXT    # JSON containing session metadata (optional)
REPO_PATH          # Repository root path (default: current directory)
```

**Command-line Arguments:**
```bash
python3 scripts/data_breach_agent.py [--repo-path PATH]
```

**Session Context Structure (if provided):**
```json
{
  "session_id": "session-2025-11-12-143022",
  "user": "developer@rynocrypto.com",
  "work_summary": "Added new TerraHash Stack PRD and architecture diagrams",
  "files_modified": ["prd/active/...", "assets/diagrams/..."]
}
```

---

## Output Specifications

### 1. OPSEC Alert Report

**File:** `OPSEC_ALERT.md`
**Generated When:** Violations detected

**Structure:**
```markdown
# OPSEC Alert Report

**Alert ID:** OPSEC-YYYY-MM-DD-HHMMSS
**Detected:** [ISO 8601 Timestamp]
**Severity:** [CRITICAL | HIGH | MEDIUM | LOW]
**Status:** [ACTIVE | CONTAINED | RESOLVED]

## Executive Summary
[2-3 sentence incident overview]

## Detection Details
- **Trigger:** [Pre-commit Hook | Daily Scan | Session Close]
- **Files Affected:** [Count]
- **Content Types:** [Financial | AI/ML | Treasury | NOC | Partnership]

### Affected Files
- `path/to/file.ext` - [Violation count] - [Brief description, NO SENSITIVE DATA]

## Risk Assessment
- **Exposure Duration:** [Time since first commit]
- **Public Visibility:** GitHub public repository
- **Potential Impact:** [Competitive | Legal | Financial]
- **Risk Score:** [1-10]

## Immediate Actions Taken
1. ✅ Files flagged for review
2. ✅ Commit blocked (if pre-commit) / History scrubbed (if post-commit)
3. ✅ Recovery plan initiated
```

### 2. Recovery Plan

**File:** `RECOVERY_PLAN.md`

**Phases:**
- **Phase 1 (0-24h):** Immediate containment, history scrubbing, force push
- **Phase 2 (24-72h):** Impact assessment, fork monitoring, cache checking
- **Phase 3 (72h-1wk):** Legal consultation, patent review, DMCA requests
- **Phase 4 (1-2wks):** Enhanced pre-commit hooks, CLAUDE.md updates, team training
- **Phase 5 (Ongoing):** Automated daily scans, quarterly audits, CLA enforcement

### 3. Post-Mortem Analysis

**File:** `POST_MORTEM.md`

**Sections:**
- Incident summary and root cause analysis
- Timeline of events (detection → containment → recovery)
- Quantifiable damage assessment (technical, business, financial impact)
- What went wrong / What went right
- Lessons learned and prevention recommendations

---

## Implementation Reference

**Script Location:** `scripts/data_breach_agent.py`

**Key Components:**
1. **DataBreachAgent Class:** Repository scanner with pattern matching
2. **Pattern Definitions:** Regex patterns for critical keywords (CRITICAL_PATTERNS dict)
3. **File Risk Assessment:** Extension-based and filename-based risk scoring
4. **Report Generators:** OPSEC_ALERT, RECOVERY_PLAN, POST_MORTEM template rendering
5. **Session Context Loader:** Reads SESSION_CONTEXT environment variable (JSON)

**Exit Codes:**
- `0` - No violations detected (repository clean)
- `1` - Violations detected (reports generated)

---

## Integration Examples

### Pre-Commit Hook Integration

**File:** `.pre-commit-config.yaml`

```yaml
repos:
  - repo: local
    hooks:
      - id: data-breach-detection
        name: Detect proprietary content violations
        entry: python3 scripts/data_breach_agent.py
        language: system
        pass_filenames: false
        always_run: true
```

### GitHub Actions Daily Scan

**File:** `.github/workflows/opsec-scan.yml`

```yaml
name: OPSEC Daily Scan

on:
  schedule:
    - cron: '0 0 * * *'  # Midnight UTC daily
  workflow_dispatch:

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run Data Breach Agent
        run: python3 scripts/data_breach_agent.py

      - name: Commit Reports (if violations detected)
        if: failure()
        run: |
          git config user.name "OPSEC Bot"
          git config user.email "opsec@rynocrypto.com"
          git add OPSEC_ALERT.md RECOVERY_PLAN.md POST_MORTEM.md
          git commit -m "chore: OPSEC scan detected violations - reports generated"
          git push
```

### Policy Initiator Orchestration

**Command:** `/policy-initiator`

The data breach agent is orchestrated by the policy-initiator command as part of Phase 2:

```bash
# Executed with session context
SESSION_CONTEXT='{...}' python3 scripts/data_breach_agent.py

# Check exit code
if [ $? -eq 1 ]; then
  echo "⚠️ Data breach detected - review OPSEC_ALERT.md"
  exit 1
fi
```

---

## Archive Management

**Trigger Conditions:**
- Report files exceed 10,000 lines (OPSEC_ALERT), 5,000 lines (RECOVERY_PLAN, POST_MORTEM)
- 90 days since last incident

**Archive Process:**
- Move reports to `opsec-archive/report-archive-{date-range}/`
- Create fresh blank templates
- Commit archive with descriptive message

---

## Metrics & Reporting

**Track Monthly:**
- Total scans executed (pre-commit, daily, manual)
- Violations detected and resolved
- False positive rate
- Average time to remediation

**Quarterly Review:**
- Policy effectiveness assessment
- Training impact evaluation
- Process improvement recommendations
- Detection pattern updates

---

**Agent Version:** 2.0.0
**Maintained By:** Ryno Crypto Services Security Team
**Review Frequency:** Quarterly
**Next Review:** 2026-02-12
