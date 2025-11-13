# Organization & Sanitization Agent

**Version:** 2.0.0
**Last Updated:** 2025-11-12
**Status:** Active
**Repository:** ryno-assets (Documentation & Media Repository)

---

## Mission

Maintain repository organization, enforce file naming standards defined in CLAUDE.md, and sanitize content for appropriate public disclosure. This agent operates in the gray zone between fully acceptable open-source content and critical proprietary breaches—ensuring documentation provides maximum value to the community while protecting internal competitive intelligence.

---

## Agent Responsibilities

### 1. Directory Structure Validation

**Objective:** Ensure all files are in correct directories per CLAUDE.md standards.

**Expected Structure:**
```
docs/          # Documentation (architecture, api, guides, security, operations, research)
assets/        # Media assets (images, diagrams, videos) organized by product
prd/           # Product Requirements (active, proposed, completed)
specs/         # Technical specifications (api, database, integration, protocols)
examples/      # Usage examples and templates
scripts/       # Utility scripts (validation, automation)
archive/       # Deprecated content
```

**Actions:**
- Scan for misplaced files and generate relocation recommendations
- Create missing directories
- Update internal references after relocations

### 2. File Naming Convention Enforcement

**Validation Rules (from CLAUDE.md):**

| File Type | Pattern | Example |
|-----------|---------|---------|
| **Images** | `[org]-[product]-[descriptor]-[type]-[resolution]-[version].[ext]` | `ryno-crypto-architecture-diagram-1920x1080-v1-0.png` |
| **Documents** | `[org]-[product]-[category]-[title]-[version].[ext]` | `ths-stack-prd-ai-optimization-v1-0.pdf` |
| **Markdown** | `[category]-[title]-[date-optional].md` | `prd-treasury-management.md` |

**Common Violations:**
- Spaces in filenames → Replace with hyphens
- Uppercase letters → Convert to lowercase
- Underscores → Replace with hyphens
- Version with periods (`v1.0`) → Use hyphens (`v1-0`)
- Non-descriptive names → Add org/product/descriptor components

### 3. Content Sanitization

**Objective:** Identify and redact internal information that provides limited community value but could benefit competitors.

**Redaction Categories:**

| Category | Examples | Risk Level |
|----------|----------|------------|
| **Financial Specificity** | Exact revenue numbers, precise margins, CAC details | HIGH |
| **Vendor Pricing** | Negotiated rates, volume discounts, exclusive agreements | HIGH |
| **Strategic Timelines** | Specific launch dates, internal milestones, competitive responses | MEDIUM |
| **Customer/Partner Details** | Specific names (unless public), contract terms, revenue splits | MEDIUM |
| **Technical Implementation** | Algorithm parameters, internal API URLs, optimization thresholds | MEDIUM |
| **Personnel & Org** | Internal emails, phone numbers, org charts, compensation | LOW |

**Detection Patterns:**
```regex
# Financial: \$\d{1,3}(,\d{3})+\.\d{2} | \d+%\s+margin | CAC\s+of\s+\$\d+
# Vendor: negotiated\s+(?:at|for)\s+\$[\d,]+ | vendor\s+(?:quoted|pricing):\s*\$
# Customer: (?:customer|client|partner):\s*([A-Z][a-zA-Z0-9\s]+(?:Inc|LLC|Corp))
# Internal: [\w\.-]+@(?:rynocrypto|terrahash)\.(?:com|io)
# Timeline: (?:launch|release)(?:ing|ed)?\s+(?:on|by)\s+\d{4}-\d{2}-\d{2}
# Parameters: (?:threshold|coefficient|parameter|weight)[\s:=]+[\d\.]+
```

**Acceptable Public Content:**
- High-level architecture and design principles
- General technology stack descriptions
- Industry-standard methodologies
- Educational technical concepts
- General cost ranges or orders of magnitude
- Published research and whitepapers

---

## Input Specifications

**Environment Variables:**
```bash
SESSION_CONTEXT    # JSON containing session metadata (optional)
REPO_PATH          # Repository root path (default: current directory)
```

**Command-line Arguments:**
```bash
python3 scripts/organization_sanitation_agent.py \
  --mode {audit|rename|redact|relocate|full} \
  [--execute] \
  [--repo-path PATH]
```

**Modes:**
- `audit` - Dry-run scan, generate report only (default)
- `rename` - Execute file renaming only
- `redact` - Apply content redactions only
- `relocate` - Move files to correct directories only
- `full` - Execute all operations

---

## Output Specifications

### ORGANIZATION_AUDIT_REPORT.md

**Generated When:** Every audit execution

**Structure:**
```markdown
# Repository Organization & Sanitization Audit Report

**Generated:** [ISO 8601 Timestamp]
**Mode:** [DRY RUN | LIVE EXECUTION]

## Executive Summary
- Directory Structure: [N] issues
- File Naming: [N] violations
- Content Redactions: [N] items
- File Relocations: [N] files

## 1. Directory Structure Issues
[Missing directories and recommendations]

## 2. File Naming Violations
[Table: Current File | Issues | Recommended Name]

## 3. Content Requiring Redaction
[Grouped by type: Financial, Vendor Pricing, Customer Names, etc.]
- File, line number, match, context, justification, replacement

## 4. File Relocation Recommendations
[Table: File | Current | Recommended | Reason]

## 5. Recommended Actions
[Immediate, near-term, and process improvements]

## Approval Workflow
[Commands to execute approved changes]
```

### Exit Codes

- `0` - No issues found (repository compliant) OR changes successfully executed
- `1` - Issues found (dry-run mode with violations)

---

## Implementation Reference

**Script Location:** `scripts/organization_sanitation_agent.py`

**Key Components:**
1. **OrganizationSanitationAgent Class:** Main orchestrator for all validations
2. **Directory Structure Validator:** Checks file locations against CLAUDE.md standards
3. **Filename Compliance Checker:** Validates naming conventions with auto-fix suggestions
4. **Content Scanner:** Regex-based detection of borderline sensitive information
5. **Report Generator:** Creates comprehensive ORGANIZATION_AUDIT_REPORT.md
6. **Session Context Loader:** Reads SESSION_CONTEXT environment variable (JSON)

**Redaction Strategy:**
- **Conservative approach:** Flag for human review rather than auto-redact
- **Context-aware:** Consider surrounding text to reduce false positives
- **Logged and reversible:** All changes tracked in Git with clear audit trail

---

## Integration Examples

### Pre-Commit Hook Integration

**File:** `.pre-commit-config.yaml`

```yaml
repos:
  - repo: local
    hooks:
      - id: organization-sanitation
        name: Repository organization and content sanitization
        entry: python3 scripts/organization_sanitation_agent.py --mode=audit
        language: system
        pass_filenames: false
        always_run: true
```

### GitHub Actions Weekly Audit

**File:** `.github/workflows/organization-audit.yml`

```yaml
name: Weekly Organization Audit

on:
  schedule:
    - cron: '0 0 * * 0'  # Every Sunday at midnight UTC
  workflow_dispatch:

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run Organization Audit
        run: python3 scripts/organization_sanitation_agent.py --mode=audit

      - name: Upload Audit Report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: organization-audit-report
          path: ORGANIZATION_AUDIT_REPORT.md

      - name: Create Issue if Problems Found
        if: failure()
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: '⚠️ Organization Audit: Issues Detected',
              body: 'Review ORGANIZATION_AUDIT_REPORT.md artifact.',
              labels: ['maintenance', 'organization']
            })
```

### Policy Initiator Orchestration

**Command:** `/policy-initiator`

The organization sanitation agent is orchestrated by the policy-initiator command as part of Phase 3:

```bash
# Executed with session context
SESSION_CONTEXT='{...}' python3 scripts/organization_sanitation_agent.py --mode=audit

# Check exit code
if [ $? -eq 1 ]; then
  echo "⚠️ Organization issues detected - review ORGANIZATION_AUDIT_REPORT.md"
  # Continue (non-blocking for organization issues)
fi
```

---

## Redaction Decision Matrix

Use this matrix to determine if content should be redacted:

| Criterion | Keep Public | Redact |
|-----------|-------------|--------|
| **Educational Value** | High | Low |
| **Competitive Sensitivity** | Low | High |
| **Verifiability** | Independently verifiable | Proprietary data |
| **Community Benefit** | Enables implementation | Company-specific intel |
| **Legal Risk** | None | Contractual/NDA concerns |

**Example Redactions:**

```markdown
# BEFORE
"We negotiated a rate of $0.045/kWh with our energy provider"

# AFTER
"We secured competitive energy rates below market average"

# JUSTIFICATION
Specific negotiated rates are confidential business terms with no
educational value to open-source community
```

```markdown
# BEFORE
"Customer XYZ Corp deployed 500 units generating $2.3M annual revenue"

# AFTER
"Commercial deployments at scale demonstrate viability"

# JUSTIFICATION
Specific customer identity and revenue violates privacy and reveals
competitive positioning
```

---

## Approval Workflow

### 1. Review Phase
Agent generates `ORGANIZATION_AUDIT_REPORT.md` with complete list of proposed changes, justifications, and impact assessment.

### 2. Human Review
Repository maintainer reviews each proposed change:
- [ ] Redactions justified and appropriate?
- [ ] No over-redaction (losing community value)?
- [ ] Naming changes follow CLAUDE.md?
- [ ] File relocations logical?
- [ ] All links will remain valid?

### 3. Execution

```bash
# After approval, execute specific operations
python3 scripts/organization_sanitation_agent.py --mode=rename --execute
python3 scripts/organization_sanitation_agent.py --mode=redact --execute
python3 scripts/organization_sanitation_agent.py --mode=relocate --execute

# Or execute all at once
python3 scripts/organization_sanitation_agent.py --mode=full --execute

# Review changes
git diff

# Commit
git add -A
git commit -m "chore: repository sanitization per audit $(date +%Y-%m-%d)"
git push
```

### 4. Rollback (if needed)

```bash
# Create backup before execution
git checkout -b backup-pre-sanitization-$(date +%Y%m%d)
git push origin backup-pre-sanitization-$(date +%Y%m%d)

# Revert if issues detected
git revert <commit-hash>

# Or restore specific files
git checkout backup-pre-sanitization-YYYYMMDD -- path/to/file
```

---

## Integration with Data Breach Agent

**Data Breach Agent** (critical proprietary content):
- Scope: Algorithms, complete financial models, vendor contracts, credentials
- Action: Immediate removal, incident reports, Git history scrubbing
- Trigger: Pre-commit block, daily scans

**Organization Sanitation Agent** (borderline sensitive content):
- Scope: Specific metrics, vendor pricing details, customer names, timelines
- Action: Redaction with [REDACTED], file organization
- Trigger: Weekly audits, pre-release reviews

**Escalation:** If Organization Agent detects critical content → escalate to Data Breach Agent workflow

---

## Metrics & Maintenance

**Track Monthly:**
- Files renamed per audit
- Content redactions applied
- False positive rate
- Time to remediation
- Community feedback on sanitized docs

**Maintenance Schedule:**
- **Weekly:** Automated audit via GitHub Actions
- **Monthly:** Manual review of audit trends, pattern tuning
- **Quarterly:** Effectiveness review, CLAUDE.md alignment check, process updates

**Success Criteria:**
1. Community Value: Documentation remains useful and educational
2. Competitive Protection: Business intelligence stays internal
3. Legal Compliance: No NDA or contractual violations
4. Technical Accuracy: Redactions don't create misinformation
5. Usability: Documents remain readable and actionable

---

**Agent Version:** 2.0.0
**Maintained By:** Ryno Crypto Services Repository Team
**Review Frequency:** Quarterly
**Next Review:** 2026-02-12

*"Share knowledge generously, protect competitive advantages vigilantly."*
