# DATA-BREACH.md - OPSEC Compliance Agent Instructions

**Last Updated:** 2025-11-09 12:16 PM MST
**Version:** 1.0.0
**Status:** Active
**Scope:** Ryno-Crypto-Mining-Services/ryno-assets repository

---

## 🎯 Mission

Monitor and enforce the **75% Open Source / 25% Proprietary** balance defined in the TerraHash Stack business model. Detect, document, and remediate any unauthorized disclosure of proprietary information in the public repository.

---

## 📋 Agent Responsibilities

### 1. Repository Analysis & Monitoring

**Trigger Conditions:**
- Pre-commit hook execution
- Scheduled daily scans (via GitHub Actions)
- Manual execution: `python scripts/data_breach_agent.py`

**Analysis Scope:**
- All files in repository (docs, images, configs, code)
- Commit history for recently added content
- File metadata and naming conventions

### 2. Proprietary Content Detection

**Critical Keywords & Patterns:**

#### Financial & Business Intelligence
```regex
revenue[_\s]projection|margin[_\s]analysis|pricing[_\s]strategy|
ltv[_\s]cac|customer[_\s]acquisition|competitive[_\s]positioning|
5[_\s]year[_\s]model|financial[_\s]projection
```

#### AI/ML & Algorithms
```regex
ml[_\-]model|ai[_\-]agent|predictive[_\s]maintenance|
optimization[_\s]algorithm|neural[_\s]network|training[_\s]data|
model[_\s]weights|hyperparameter
```

#### Treasury & Trading
```regex
portfolio[_\s]rebalancing|hodl[_\s]ratio|treasury[_\s]management|
hedging[_\s]strategy|automated[_\s]trading|liquidity[_\s]management|
stablecoin[_\s]allocation
```

#### NOC & Operations
```regex
noc[_\s]platform|telemetry[_\s]system|iot[_\s]sensor|
monitoring[_\s]dashboard|alert[_\s]algorithm|kpi[_\s]tracking
```

#### Industrial Scale Designs
```regex
5mw[_\s]facility|industrial[_\s]deployment|commercial[_\s]scale|
proprietary[_\s]cooling|exclusive[_\s]integration
```

#### Partnership & Legal
```regex
chilldyne[_\s]exclusive|braiins[_\s]custom|licensing[_\s]agreement|
partnership[_\s]terms|vendor[_\s]contract|confidential[_\s]agreement
```

**File Type Risk Levels:**
- **CRITICAL:** `.py`, `.js`, `.java`, `.pkl`, `.h5`, `.bin`, `.xlsx`, `.csv` (with financial data)
- **HIGH:** `.pdf` (business plans, contracts), `.pptx` (investor decks)
- **MEDIUM:** `.md` (detailed PRDs, architecture specs)
- **LOW:** `.png`, `.jpg`, `.svg` (diagrams, unless containing sensitive data)

### 3. Automated Response Actions

**When Proprietary Content Detected:**

1. **IMMEDIATE (Pre-commit):**
   ```bash
   # Block commit
   echo "❌ COMMIT BLOCKED: Proprietary content detected"
   exit 1
   ```

2. **POST-DETECTION (Already committed):**
   ```bash
   # Remove from repository
   git rm --cached <sensitive_file>
   git commit -m "OPSEC: Remove proprietary content"

   # Purge from history
   git filter-branch --force --index-filter \
     'git rm --cached --ignore-unmatch <sensitive_file>' \
     --prune-empty --tag-name-filter cat -- --all
   ```

3. **GENERATE REPORTS:**
   - `OPSEC_ALERT.md` - Public incident report
   - `RECOVERY_PLAN.md` - Remediation steps
   - `POST_MORTEM.md` - Analysis and prevention

---

## 📄 Report Templates

### OPSEC_ALERT.md Structure

```markdown
# OPSEC Alert Report

**Alert ID:** OPSEC-YYYY-MM-DD-HHMMSS
**Detected:** [ISO 8601 Timestamp]
**Severity:** [CRITICAL | HIGH | MEDIUM | LOW]
**Status:** [ACTIVE | CONTAINED | RESOLVED]

---

## Executive Summary

[2-3 sentence overview of incident]

## Detection Details

**Trigger:** [Pre-commit Hook | Daily Scan | Manual Review]
**Files Affected:** [Count]
**Content Type:** [Financial | AI/ML | Treasury | NOC | Partnership]

### Affected Files
- `path/to/file1.ext` - [Brief description, NO SENSITIVE DATA]
- `path/to/file2.ext` - [Brief description, NO SENSITIVE DATA]

## Risk Assessment

**Exposure Duration:** [Time since first commit]
**Public Visibility:** [GitHub public | Indexed by search engines]
**Potential Impact:** [Competitive | Legal | Financial]

**Risk Score:** [1-10]

## Immediate Actions Taken

1. ✅ Files removed from repository
2. ✅ Git history scrubbed
3. ✅ Recovery plan initiated
4. ✅ Stakeholders notified

## Next Steps

See: `RECOVERY_PLAN.md` and `POST_MORTEM.md`

---

**Report Generated:** [ISO 8601 Timestamp]
**Agent Version:** 1.0.0
```

### RECOVERY_PLAN.md Structure

```markdown
# Recovery Plan

**Associated Alert:** OPSEC-YYYY-MM-DD-HHMMSS
**Created:** [ISO 8601 Timestamp]
**Status:** [IN PROGRESS | COMPLETED]

---

## Phase 1: Immediate Containment (0-24 hours)

- [ ] Remove sensitive files from repository
- [ ] Scrub Git history using `git filter-branch` or BFG Repo-Cleaner
- [ ] Force push cleaned history: `git push origin --force --all`
- [ ] Notify all contributors to re-clone repository
- [ ] Update `.gitignore` to prevent re-addition

## Phase 2: Impact Assessment (24-72 hours)

- [ ] Review GitHub traffic analytics for file downloads
- [ ] Search for forks and clones on GitHub
- [ ] Check web caches (Google, Wayback Machine)
- [ ] Contact GitHub support for cache purging if needed
- [ ] Assess competitive intelligence risk

## Phase 3: Legal & Compliance (72 hours - 1 week)

- [ ] Consult legal counsel on exposure implications
- [ ] Review patent filing status (if algorithms exposed)
- [ ] Update trade secret documentation
- [ ] File DMCA takedown requests if forks contain data

## Phase 4: Process Improvement (1-2 weeks)

- [ ] Implement enhanced pre-commit hooks
- [ ] Update `CLAUDE.md` with stricter guidelines
- [ ] Conduct team training on OPSEC policies
- [ ] Establish monthly IP audit schedule

## Phase 5: Long-term Prevention (Ongoing)

- [ ] Automated daily repository scans
- [ ] Quarterly external security audits
- [ ] CLA enforcement for all contributors
- [ ] Private submodule strategy for proprietary code

---

**Plan Updated:** [ISO 8601 Timestamp]
```

### POST_MORTEM.md Structure

```markdown
# Post-Mortem Analysis

**Associated Alert:** OPSEC-YYYY-MM-DD-HHMMSS
**Incident Date:** [Date]
**Report Date:** [ISO 8601 Timestamp]
**Author:** [Name/Team]

---

## Incident Summary

**What Happened:**
[Detailed narrative of incident]

**Root Cause:**
[Technical and process failures]

**Detection Method:**
[How was breach discovered]

## Timeline

| Time | Event |
|------|-------|
| T+0  | Proprietary content committed |
| T+X  | Detection triggered |
| T+Y  | Containment initiated |
| T+Z  | Recovery completed |

## Quantifiable Damage Assessment

### Technical Impact
- **Exposure Duration:** [Hours/Days]
- **Repository Views:** [Count from GitHub Insights]
- **File Downloads:** [Estimated]
- **Forks Created:** [Count]

### Business Impact
- **Competitive Risk:** [LOW | MEDIUM | HIGH | CRITICAL]
- **IP Value at Risk:** [Estimated $USD if quantifiable]
- **Legal Exposure:** [Describe potential issues]
- **Reputation Impact:** [Assessment]

### Financial Impact
- **Remediation Costs:** [Hours * Rate]
- **Legal Consultation:** [Cost]
- **Lost Competitive Advantage:** [Estimated if applicable]

**Total Estimated Impact:** $[Amount] + [Non-monetary impacts]

## What Went Wrong

1. **Process Failures:**
   - [List specific breakdowns]

2. **Technical Failures:**
   - [Pre-commit hooks, access controls, etc.]

3. **Human Factors:**
   - [Training, awareness, mistakes]

## What Went Right

- [Things that worked during detection/response]

## Lessons Learned

### Immediate Fixes
1. [Action item 1]
2. [Action item 2]

### Long-term Improvements
1. [Strategic change 1]
2. [Strategic change 2]

## Prevention Recommendations

### Technical Controls
- Enhanced pre-commit keyword scanning
- Automated secret detection (Yelp detect-secrets)
- Private repository mirrors for sensitive development
- Submodule separation for proprietary components

### Process Controls
- Mandatory pre-commit training for all contributors
- Monthly IP audit reviews
- Quarterly security assessments
- CLA enforcement with IP assignment clauses

### Organizational Controls
- IP Committee oversight
- Clear CLAUDE.md guidelines
- Documented 75/25 open/proprietary framework
- Regular contributor awareness campaigns

---

**Report Completed:** [ISO 8601 Timestamp]
**Status:** [DRAFT | FINAL | ARCHIVED]
```

---

## 🗄️ Archive Management

**Archive Trigger Conditions:**
- `OPSEC_ALERT.md` exceeds 10,000 lines
- `RECOVERY_PLAN.md` exceeds 5,000 lines
- `POST_MORTEM.md` exceeds 5,000 lines
- 90 days have passed since last incident

**Archive Process:**

```bash
#!/bin/bash
# Create archive directory
mkdir -p opsec-archive

# Determine date range
FIRST_DATE=$(head -n 20 OPSEC_ALERT.md | grep "Detected:" | head -1 | awk '{print $2}')
LAST_DATE=$(tail -n 20 OPSEC_ALERT.md | grep "Detected:" | tail -1 | awk '{print $2}')

# Create timestamped directory
ARCHIVE_DIR="opsec-archive/report-archive-${FIRST_DATE}-${LAST_DATE}"
mkdir -p "${ARCHIVE_DIR}"

# Move files
mv OPSEC_ALERT.md "${ARCHIVE_DIR}/"
mv RECOVERY_PLAN.md "${ARCHIVE_DIR}/"
mv POST_MORTEM.md "${ARCHIVE_DIR}/"

# Create new blank templates
touch OPSEC_ALERT.md RECOVERY_PLAN.md POST_MORTEM.md

# Commit archive
git add opsec-archive/ OPSEC_ALERT.md RECOVERY_PLAN.md POST_MORTEM.md
git commit -m "chore: archive OPSEC reports ${FIRST_DATE} to ${LAST_DATE}"
```

---

## 🔧 Implementation Script

**Location:** `scripts/data_breach_agent.py`

```python
#!/usr/bin/env python3
"""
Data Breach Detection Agent for ryno-assets repository
Enforces 75% open source / 25% proprietary balance
"""

import os
import re
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple

# Proprietary content patterns
CRITICAL_PATTERNS = {
    'financial': [
        r'revenue[_\s]projection', r'margin[_\s]analysis', r'pricing[_\s]strategy',
        r'ltv[_\s]cac', r'5[_\s]year[_\s]model', r'financial[_\s]projection'
    ],
    'ai_ml': [
        r'ml[_-]model', r'ai[_-]agent', r'predictive[_\s]maintenance',
        r'optimization[_\s]algorithm', r'neural[_\s]network', r'model[_\s]weights'
    ],
    'treasury': [
        r'portfolio[_\s]rebalancing', r'hodl[_\s]ratio', r'treasury[_\s]management',
        r'automated[_\s]trading', r'hedging[_\s]strategy'
    ],
    'noc': [
        r'noc[_\s]platform', r'telemetry[_\s]system', r'iot[_\s]sensor',
        r'monitoring[_\s]dashboard', r'alert[_\s]algorithm'
    ],
    'industrial': [
        r'5mw[_\s]facility', r'industrial[_\s]deployment', r'commercial[_\s]scale'
    ],
    'partnership': [
        r'chilldyne[_\s]exclusive', r'braiins[_\s]custom', r'licensing[_\s]agreement',
        r'vendor[_\s]contract', r'confidential[_\s]agreement'
    ]
}

CRITICAL_FILENAMES = [
    'financial', 'revenue', 'pricing', 'margin', 'ltv', 'cac',
    'model', 'weights', 'algorithm', 'proprietary', 'confidential',
    'treasury', 'portfolio', 'noc', 'exclusive', 'contract'
]

HIGH_RISK_EXTENSIONS = ['.py', '.js', '.pkl', '.h5', '.bin', '.xlsx', '.pptx']

class DataBreachAgent:
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path)
        self.violations: List[Dict] = []
        self.timestamp = datetime.utcnow().isoformat()

    def scan_repository(self) -> bool:
        """Scan all files for proprietary content"""
        print(f"🔍 Starting repository scan at {self.timestamp}")

        for root, dirs, files in os.walk(self.repo_path):
            # Skip .git and archives
            dirs[:] = [d for d in dirs if d not in ['.git', 'opsec-archive', '__pycache__']]

            for file in files:
                filepath = Path(root) / file
                self._scan_file(filepath)

        if self.violations:
            print(f"❌ {len(self.violations)} violations detected!")
            return False
        else:
            print("✅ No proprietary content detected")
            return True

    def _scan_file(self, filepath: Path):
        """Scan individual file"""
        # Check filename
        filename_lower = filepath.name.lower()
        for keyword in CRITICAL_FILENAMES:
            if keyword in filename_lower:
                self._record_violation(filepath, 'filename', keyword, None)

        # Check file extension
        if filepath.suffix in HIGH_RISK_EXTENSIONS:
            self._record_violation(filepath, 'high_risk_extension', filepath.suffix, None)

        # Scan content (text files only)
        try:
            with open(filepath, 'r', errors='ignore') as f:
                content = f.read()
                for category, patterns in CRITICAL_PATTERNS.items():
                    for pattern in patterns:
                        matches = re.finditer(pattern, content, re.IGNORECASE)
                        for match in matches:
                            self._record_violation(filepath, 'content', pattern, match.group())
        except Exception:
            pass  # Binary or unreadable file

    def _record_violation(self, filepath: Path, vtype: str, pattern: str, match: str):
        """Record a violation"""
        self.violations.append({
            'file': str(filepath.relative_to(self.repo_path)),
            'type': vtype,
            'pattern': pattern,
            'match': match,
            'timestamp': self.timestamp
        })

    def generate_opsec_alert(self):
        """Generate OPSEC_ALERT.md"""
        alert_id = f"OPSEC-{datetime.utcnow().strftime('%Y-%m-%d-%H%M%S')}"
        severity = self._calculate_severity()

        content = f"""# OPSEC Alert Report

**Alert ID:** {alert_id}
**Detected:** {self.timestamp}
**Severity:** {severity}
**Status:** ACTIVE

---

## Executive Summary

Automated scan detected {len(self.violations)} potential proprietary content violations in the repository. Immediate action required to maintain 75% open source / 25% proprietary balance.

## Detection Details

**Trigger:** Automated Daily Scan
**Files Affected:** {len(set(v['file'] for v in self.violations))}
**Content Types:** {', '.join(set(self._categorize(v) for v in self.violations))}

### Affected Files

"""
        for file in set(v['file'] for v in self.violations):
            file_violations = [v for v in self.violations if v['file'] == file]
            content += f"- `{file}` - {len(file_violations)} violation(s) detected\n"

        content += f"""

## Risk Assessment

**Exposure Duration:** Under investigation
**Public Visibility:** GitHub public repository
**Potential Impact:** Competitive advantage, IP exposure

**Risk Score:** {self._calculate_risk_score()}/10

## Immediate Actions Required

1. ⚠️ Review flagged files manually
2. ⚠️ Remove confirmed proprietary content
3. ⚠️ Scrub Git history if needed
4. ⚠️ Update `.gitignore` and pre-commit hooks

## Next Steps

See: `RECOVERY_PLAN.md` and `POST_MORTEM.md`

---

**Report Generated:** {self.timestamp}
**Agent Version:** 1.0.0
"""

        with open(self.repo_path / 'OPSEC_ALERT.md', 'w') as f:
            f.write(content)

        print(f"📄 OPSEC_ALERT.md created: {alert_id}")

    def generate_recovery_plan(self):
        """Generate RECOVERY_PLAN.md"""
        alert_id = f"OPSEC-{datetime.utcnow().strftime('%Y-%m-%d-%H%M%S')}"

        content = f"""# Recovery Plan

**Associated Alert:** {alert_id}
**Created:** {self.timestamp}
**Status:** IN PROGRESS

---

## Phase 1: Immediate Containment (0-24 hours)

- [ ] Review all flagged files: {len(set(v['file'] for v in self.violations))} files
- [ ] Remove confirmed sensitive files from repository
- [ ] Scrub Git history: `git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch <file>' --prune-empty --tag-name-filter cat -- --all`
- [ ] Force push cleaned history: `git push origin --force --all`
- [ ] Notify contributors to re-clone

## Phase 2: Impact Assessment (24-72 hours)

- [ ] Check GitHub Insights for file access stats
- [ ] Search for repository forks
- [ ] Review web caches (Google, Wayback Machine)
- [ ] Assess competitive intelligence risk

## Phase 3: Legal & Compliance (72 hours - 1 week)

- [ ] Consult legal counsel
- [ ] Review patent filing status
- [ ] Update trade secret documentation
- [ ] File DMCA requests for forks if needed

## Phase 4: Process Improvement (1-2 weeks)

- [ ] Enhanced pre-commit hooks
- [ ] Update CLAUDE.md guidelines
- [ ] Team OPSEC training
- [ ] Monthly IP audit schedule

## Phase 5: Prevention (Ongoing)

- [ ] Automated daily scans
- [ ] Quarterly security audits
- [ ] CLA enforcement
- [ ] Private submodule strategy

---

**Plan Updated:** {self.timestamp}
"""

        with open(self.repo_path / 'RECOVERY_PLAN.md', 'w') as f:
            f.write(content)

        print("📄 RECOVERY_PLAN.md created")

    def generate_post_mortem(self):
        """Generate POST_MORTEM.md"""
        alert_id = f"OPSEC-{datetime.utcnow().strftime('%Y-%m-%d-%H%M%S')}"

        content = f"""# Post-Mortem Analysis

**Associated Alert:** {alert_id}
**Incident Date:** {datetime.utcnow().strftime('%Y-%m-%d')}
**Report Date:** {self.timestamp}
**Status:** DRAFT

---

## Incident Summary

**What Happened:**
Automated data breach detection agent identified {len(self.violations)} potential violations of the 75% open source / 25% proprietary policy.

**Root Cause:**
Under investigation - likely combination of:
- Insufficient pre-commit validation
- Contributor unfamiliarity with policy
- Manual file additions bypassing hooks

**Detection Method:**
Automated daily repository scan

## Quantifiable Damage Assessment

### Technical Impact
- **Violations Detected:** {len(self.violations)}
- **Files Affected:** {len(set(v['file'] for v in self.violations))}
- **Exposure Duration:** Under investigation
- **Repository Visibility:** Public (GitHub)

### Business Impact
- **Competitive Risk:** Under assessment
- **IP Value at Risk:** Under assessment
- **Legal Exposure:** Under review
- **Reputation Impact:** Minimal (proactive detection)

**Total Estimated Impact:** Under assessment

## Prevention Recommendations

### Technical Controls
1. Enhanced pre-commit keyword scanning
2. Automated secret detection
3. Private repository mirrors for development
4. Submodule separation strategy

### Process Controls
1. Mandatory OPSEC training
2. Monthly IP audits
3. Quarterly security assessments
4. CLA enforcement

### Organizational Controls
1. IP Committee oversight
2. Updated CLAUDE.md guidelines
3. Regular contributor awareness
4. Clear 75/25 framework documentation

---

**Report Status:** DRAFT
**Report Completed:** {self.timestamp}
"""

        with open(self.repo_path / 'POST_MORTEM.md', 'w') as f:
            f.write(content)

        print("📄 POST_MORTEM.md created")

    def _calculate_severity(self) -> str:
        """Calculate incident severity"""
        if len(self.violations) > 20:
            return "CRITICAL"
        elif len(self.violations) > 10:
            return "HIGH"
        elif len(self.violations) > 5:
            return "MEDIUM"
        else:
            return "LOW"

    def _calculate_risk_score(self) -> int:
        """Calculate risk score 1-10"""
        score = min(10, len(self.violations) // 2 + 3)
        return score

    def _categorize(self, violation: Dict) -> str:
        """Categorize violation type"""
        for category, patterns in CRITICAL_PATTERNS.items():
            if violation['pattern'] in patterns:
                return category.upper()
        return "GENERAL"

def main():
    agent = DataBreachAgent()

    if not agent.scan_repository():
        print("\n🚨 PROPRIETARY CONTENT DETECTED 🚨\n")
        agent.generate_opsec_alert()
        agent.generate_recovery_plan()
        agent.generate_post_mortem()
        print("\n📋 Reports generated. Review and take action immediately.")
        sys.exit(1)
    else:
        print("\n✅ Repository clean - no proprietary content detected")
        sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## 🚀 Deployment

### 1. Add to Pre-Commit Hooks

Add to `.pre-commit-config.yaml`:

```yaml
  - repo: local
    hooks:
      - id: data-breach-detection
        name: Detect proprietary content violations
        entry: python3 scripts/data_breach_agent.py
        language: system
        pass_filenames: false
        always_run: true
```

### 2. GitHub Actions (Daily Scan)

Create `.github/workflows/opsec-scan.yml`:

```yaml
name: OPSEC Daily Scan

on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight UTC
  workflow_dispatch:

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Data Breach Agent
        run: python3 scripts/data_breach_agent.py
      - name: Commit Reports (if violations)
        if: failure()
        run: |
          git config user.name "OPSEC Bot"
          git config user.email "opsec@rynocrypto.com"
          git add OPSEC_ALERT.md RECOVERY_PLAN.md POST_MORTEM.md
          git commit -m "chore: OPSEC scan detected violations"
          git push
```

---

## 📊 Metrics & Reporting

**Monthly Report:**
- Total scans executed
- Violations detected and resolved
- False positive rate
- Time to remediation
- Archive count

**Quarterly Review:**
- Policy effectiveness
- Training impact
- Process improvements
- Technology upgrades

---

**Document Version:** 1.0.0
**Maintained By:** Ryno Crypto Services Security Team
**Review Frequency:** Quarterly
**Next Review:** 2026-02-09
