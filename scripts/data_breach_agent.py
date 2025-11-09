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
