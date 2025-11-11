#!/usr/bin/env python3
"""
Organization & Sanitization Agent for ryno-assets repository
Enforces CLAUDE.md naming conventions and content hygiene
"""

import os
import re
import sys
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional

class OrganizationSanitationAgent:
    def __init__(self, repo_path: str = '.', dry_run: bool = True):
        self.repo_path = Path(repo_path)
        self.dry_run = dry_run
        self.timestamp = datetime.utcnow().isoformat()
        self.violations = []
        self.redactions = []
        self.relocations = []

        # Load session context if available
        self.session_context = self._load_session_context()

    def _load_session_context(self) -> Optional[Dict]:
        """Load session context from environment variable"""
        context_str = os.environ.get('SESSION_CONTEXT')
        if context_str:
            try:
                return json.loads(context_str)
            except json.JSONDecodeError:
                print("⚠️  Invalid SESSION_CONTEXT, ignoring")
        return None

    def run_full_audit(self):
        """Execute complete repository audit"""
        print("🔍 Starting Organization & Sanitization Audit")
        print(f"Timestamp: {self.timestamp}")
        print(f"Mode: {'DRY RUN' if self.dry_run else 'LIVE EXECUTION'}")
        if self.session_context:
            print(f"📋 Session context loaded from previous work")
        print()

        # Phase 1: Directory structure
        self._validate_directory_structure()

        # Phase 2: File naming
        self._validate_file_naming()

        # Phase 3: Content sanitization
        self._scan_content_for_redaction()

        # Phase 4: Generate report
        self._generate_report()

        # Phase 5: Execute fixes (if not dry run)
        if not self.dry_run:
            self._execute_fixes()

        return self._get_summary()

    def _validate_directory_structure(self):
        """Check for misplaced files"""
        print("📁 Phase 1: Validating directory structure...")

        required_dirs = [
            'docs', 'assets', 'prd', 'specs', 'examples',
            'scripts', 'tests', 'archive'
        ]

        for dir_name in required_dirs:
            dir_path = self.repo_path / dir_name
            if not dir_path.exists():
                self.violations.append({
                    'type': 'missing_directory',
                    'path': dir_name,
                    'recommendation': f'Create directory: {dir_name}/'
                })

        # Scan for misplaced files
        for root, dirs, files in os.walk(self.repo_path):
            # Skip .git and hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            current_dir = Path(root).relative_to(self.repo_path)

            for file in files:
                filepath = Path(root) / file
                recommended_location = self._recommend_file_location(filepath)

                if recommended_location and str(current_dir) != recommended_location:
                    self.relocations.append({
                        'file': str(filepath.relative_to(self.repo_path)),
                        'current': str(current_dir),
                        'recommended': recommended_location,
                        'reason': self._get_relocation_reason(filepath, recommended_location)
                    })

    def _recommend_file_location(self, filepath: Path) -> Optional[str]:
        """Recommend proper location for file"""
        name_lower = filepath.name.lower()

        # PRDs
        if 'prd' in name_lower or 'product-requirement' in name_lower:
            return 'prd/active'

        # Specifications
        if 'spec' in name_lower or 'specification' in name_lower:
            if 'api' in name_lower:
                return 'specs/api'
            return 'specs'

        # Guides and documentation
        if 'guide' in name_lower or 'tutorial' in name_lower:
            return 'docs/guides'

        # Architecture
        if 'architecture' in name_lower or 'system-design' in name_lower:
            return 'docs/architecture'

        # Images
        if filepath.suffix in ['.png', '.jpg', '.jpeg', '.svg', '.gif', '.webp']:
            if 'diagram' in name_lower:
                return 'assets/diagrams'
            return 'assets/images'

        # Videos
        if filepath.suffix in ['.mp4', '.mov', '.avi', '.webm']:
            return 'assets/videos'

        return None

    def _get_relocation_reason(self, filepath: Path, recommended: str) -> str:
        """Explain why file should be relocated"""
        if 'prd' in recommended:
            return "PRD documents should be in /prd/ directory"
        if 'specs' in recommended:
            return "Technical specifications belong in /specs/"
        if 'assets' in recommended:
            return "Media files should be organized in /assets/"
        if 'docs' in recommended:
            return "Documentation should be in /docs/ subdirectories"
        return "Better organization alignment"

    def _validate_file_naming(self):
        """Check files against CLAUDE.md naming conventions"""
        print("📝 Phase 2: Validating file naming conventions...")

        for root, dirs, files in os.walk(self.repo_path):
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            for file in files:
                filepath = Path(root) / file

                # Skip certain files
                if file in ['README.md', 'LICENSE', 'CHANGELOG.md', 'CONTRIBUTING.md',
                           'SECURITY.md', 'CLAUDE.md', '.gitignore']:
                    continue

                violations = self._check_filename_compliance(filepath)
                if violations:
                    recommended_name = self._generate_compliant_filename(filepath)
                    self.violations.append({
                        'type': 'naming_violation',
                        'file': str(filepath.relative_to(self.repo_path)),
                        'violations': violations,
                        'recommended': recommended_name
                    })

    def _check_filename_compliance(self, filepath: Path) -> List[str]:
        """Check filename for violations"""
        violations = []
        name = filepath.stem

        # Check for spaces
        if ' ' in name:
            violations.append("Contains spaces")

        # Check for uppercase
        if name != name.lower():
            violations.append("Contains uppercase letters")

        # Check for underscores (prefer hyphens)
        if '_' in name:
            violations.append("Contains underscores (prefer hyphens)")

        # Check length
        if len(name) > 50:
            violations.append(f"Too long ({len(name)} chars, max 50)")

        # Check for version format if present
        if 'v' in name and '.' in name:
            if not re.search(r'v\d+-\d+', name):
                violations.append("Version should use hyphens (v1-0 not v1.0)")

        # Check for descriptiveness
        if len(name) < 5 and filepath.suffix not in ['.md', '.py', '.js']:
            violations.append("Name too short, not descriptive")

        return violations

    def _generate_compliant_filename(self, filepath: Path) -> str:
        """Generate CLAUDE.md compliant filename"""
        name = filepath.stem
        ext = filepath.suffix

        # Basic sanitization
        name = name.lower()
        name = re.sub(r'\s+', '-', name)
        name = re.sub(r'_', '-', name)
        name = re.sub(r'\.', '-', name)

        # Fix version format
        name = re.sub(r'v(\d+)\.(\d+)', r'v\1-\2', name)

        # Remove invalid characters
        name = re.sub(r'[^a-z0-9\-]', '', name)

        # Truncate if too long
        if len(name) > 50:
            name = name[:50].rstrip('-')

        # Try to add missing components for images/docs
        if not self._has_org_prefix(name):
            name = self._add_org_prefix(name, filepath)

        return name + ext

    def _has_org_prefix(self, name: str) -> bool:
        """Check if filename has org prefix"""
        return name.startswith(('ryno-', 'ths-', 'terrahash-'))

    def _add_org_prefix(self, name: str, filepath: Path) -> str:
        """Add appropriate org prefix"""
        # Heuristic: if in terrahash directory or contains 'stack'
        if 'terrahash' in str(filepath) or 'stack' in name:
            return f'ths-stack-{name}'
        return f'ryno-crypto-{name}'

    def _scan_content_for_redaction(self):
        """Scan text files for borderline sensitive content"""
        print("🔍 Phase 3: Scanning content for sanitization...")

        text_extensions = ['.md', '.txt', '.pdf', '.doc', '.docx']

        for root, dirs, files in os.walk(self.repo_path):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['archive', 'opsec-archive']]

            for file in files:
                filepath = Path(root) / file

                if filepath.suffix.lower() in text_extensions:
                    self._analyze_file_content(filepath)

    def _analyze_file_content(self, filepath: Path):
        """Analyze individual file for sensitive content"""
        try:
            # Handle PDFs differently
            if filepath.suffix == '.pdf':
                self._flag_pdf_for_manual_review(filepath)
                return

            with open(filepath, 'r', errors='ignore') as f:
                content = f.read()

            findings = self._detect_borderline_content(content, filepath)

            if findings:
                self.redactions.extend(findings)

        except Exception as e:
            print(f"⚠️  Could not read {filepath}: {e}")

    def _detect_borderline_content(self, content: str, filepath: Path) -> List[Dict]:
        """Detect content that should be redacted"""
        findings = []

        # Pattern 1: Specific dollar amounts
        dollar_pattern = r'\$\d{1,3}(?:,\d{3})+(?:\.\d{2})?'
        for match in re.finditer(dollar_pattern, content):
            if self._is_sensitive_context(content, match):
                findings.append({
                    'file': str(filepath.relative_to(self.repo_path)),
                    'type': 'specific_financial_amount',
                    'line': self._get_line_number(content, match.start()),
                    'match': match.group(),
                    'context': self._get_context(content, match),
                    'justification': 'Specific financial amounts provide competitive intelligence without adding value to open-source community',
                    'recommended_replacement': '[REDACTED - Financial Details]'
                })

        # Pattern 2: Percentage margins
        margin_pattern = r'\d+(?:\.\d+)?%\s+(?:margin|profit|markup|discount)'
        for match in re.finditer(margin_pattern, content, re.IGNORECASE):
            findings.append({
                'file': str(filepath.relative_to(self.repo_path)),
                'type': 'margin_disclosure',
                'line': self._get_line_number(content, match.start()),
                'match': match.group(),
                'context': self._get_context(content, match),
                'justification': 'Specific margin percentages reveal pricing strategy with limited educational value',
                'recommended_replacement': '[REDACTED - Margin Information]'
            })

        # Pattern 3: Customer names
        customer_pattern = r'(?:customer|client|partner):\s*([A-Z][a-zA-Z0-9\s]+(?:Inc|LLC|Corp|Ltd))'
        for match in re.finditer(customer_pattern, content):
            if not self._is_public_company(match.group(1)):
                findings.append({
                    'file': str(filepath.relative_to(self.repo_path)),
                    'type': 'customer_identification',
                    'line': self._get_line_number(content, match.start()),
                    'match': match.group(),
                    'context': self._get_context(content, match),
                    'justification': 'Specific customer names without public consent risk privacy and competitive disclosure',
                    'recommended_replacement': '[REDACTED - Customer Name]'
                })

        # Pattern 4: Internal emails/contacts
        email_pattern = r'[\w\.-]+@rynocrypto\.com|[\w\.-]+@terrahash\.(?:com|io)'
        for match in re.finditer(email_pattern, content):
            if not self._is_public_contact(match.group()):
                findings.append({
                    'file': str(filepath.relative_to(self.repo_path)),
                    'type': 'internal_contact',
                    'line': self._get_line_number(content, match.start()),
                    'match': match.group(),
                    'context': self._get_context(content, match),
                    'justification': 'Internal email addresses increase spam/phishing risk without providing public value',
                    'recommended_replacement': 'support@rynocrypto.com'
                })

        # Pattern 5: Specific dates for unreleased features
        launch_date_pattern = r'(?:launch|release|deploy)(?:ing|ed)?\s+(?:on|by)\s+(\d{4}-\d{2}-\d{2}|\w+\s+\d{1,2},?\s+\d{4})'
        for match in re.finditer(launch_date_pattern, content, re.IGNORECASE):
            if self._is_future_date(match.group(1)):
                findings.append({
                    'file': str(filepath.relative_to(self.repo_path)),
                    'type': 'unreleased_timeline',
                    'line': self._get_line_number(content, match.start()),
                    'match': match.group(),
                    'context': self._get_context(content, match),
                    'justification': 'Specific future launch dates create competitive risk and commitment pressure',
                    'recommended_replacement': '[REDACTED - Timeline]'
                })

        # Pattern 6: Proprietary algorithm parameters
        param_pattern = r'(?:threshold|coefficient|factor|parameter|weight)[\s:=]+[\d\.]+(?!\s*(?:MHz|GHz|kW|MW|°C|TB|GB))'
        for match in re.finditer(param_pattern, content, re.IGNORECASE):
            if self._is_optimization_context(content, match):
                findings.append({
                    'file': str(filepath.relative_to(self.repo_path)),
                    'type': 'algorithm_parameter',
                    'line': self._get_line_number(content, match.start()),
                    'match': match.group(),
                    'context': self._get_context(content, match),
                    'justification': 'Specific optimization parameters represent proprietary tuning knowledge',
                    'recommended_replacement': '[REDACTED - Optimization Parameter]'
                })

        # Pattern 7: Vendor pricing
        vendor_price_pattern = r'(?:negotiated|contracted|purchased)\s+(?:at|for)\s+\$[\d,]+|vendor\s+(?:quoted|pricing):\s*\$[\d,]+'
        for match in re.finditer(vendor_price_pattern, content, re.IGNORECASE):
            findings.append({
                'file': str(filepath.relative_to(self.repo_path)),
                'type': 'vendor_pricing',
                'line': self._get_line_number(content, match.start()),
                'match': match.group(),
                'context': self._get_context(content, match),
                'justification': 'Negotiated vendor pricing is confidential business information',
                'recommended_replacement': '[REDACTED - Vendor Pricing]'
            })

        return findings

    def _is_sensitive_context(self, content: str, match) -> bool:
        """Check if dollar amount is in sensitive context"""
        context = content[max(0, match.start()-50):match.end()+50].lower()
        sensitive_keywords = ['revenue', 'margin', 'profit', 'cost', 'expense', 'cac', 'ltv']
        return any(keyword in context for keyword in sensitive_keywords)

    def _is_optimization_context(self, content: str, match) -> bool:
        """Check if parameter is in optimization context"""
        context = content[max(0, match.start()-100):match.end()+100].lower()
        opt_keywords = ['optimization', 'tuning', 'algorithm', 'model', 'ai', 'ml', 'performance']
        return any(keyword in context for keyword in opt_keywords)

    def _is_public_company(self, company_name: str) -> bool:
        """Check if company is publicly known partner"""
        public_partners = ['chilldyne', 'braiins', 'serverdomes', 'bitmain']
        return any(partner in company_name.lower() for partner in public_partners)

    def _is_public_contact(self, email: str) -> bool:
        """Check if email is public-facing"""
        public_contacts = ['support@', 'info@', 'sales@', 'security@', 'legal@']
        return any(contact in email.lower() for contact in public_contacts)

    def _is_future_date(self, date_str: str) -> bool:
        """Check if date is in the future"""
        # Simplified check - implement proper date parsing
        try:
            if '2026' in date_str or '2027' in date_str:
                return True
        except:
            pass
        return False

    def _flag_pdf_for_manual_review(self, filepath: Path):
        """Flag PDFs for manual review"""
        if any(keyword in filepath.name.lower() for keyword in ['financial', 'business', 'jv', 'partnership', 'contract']):
            self.redactions.append({
                'file': str(filepath.relative_to(self.repo_path)),
                'type': 'pdf_manual_review',
                'line': 'N/A',
                'match': 'PDF Document',
                'context': 'Binary file requires manual review',
                'justification': 'PDF may contain embedded financial, partnership, or confidential information',
                'recommended_replacement': 'Manual review required'
            })

    def _get_line_number(self, content: str, position: int) -> int:
        """Get line number for position in content"""
        return content[:position].count('\n') + 1

    def _get_context(self, content: str, match) -> str:
        """Get surrounding context for match"""
        start = max(0, match.start() - 100)
        end = min(len(content), match.end() + 100)
        context = content[start:end]
        return context.replace('\n', ' ').strip()

    def _generate_report(self):
        """Generate comprehensive audit report"""
        print("\n📊 Phase 4: Generating audit report...")

        report = f"""# Repository Organization & Sanitization Audit Report

**Generated:** {self.timestamp}
**Agent Version:** 1.0.0
**Mode:** {'DRY RUN (No changes made)' if self.dry_run else 'LIVE EXECUTION'}

---

## Executive Summary

**Total Issues Found:** {len(self.violations) + len(self.redactions) + len(self.relocations)}

- **Directory Structure:** {len([v for v in self.violations if v['type'] == 'missing_directory'])} issues
- **File Naming:** {len([v for v in self.violations if v['type'] == 'naming_violation'])} violations
- **Content Redactions:** {len(self.redactions)} items requiring sanitization
- **File Relocations:** {len(self.relocations)} files misplaced

---

## 1. Directory Structure Issues

"""

        dir_issues = [v for v in self.violations if v['type'] == 'missing_directory']
        if dir_issues:
            report += "### Missing Directories\n\n"
            for issue in dir_issues:
                report += f"- `{issue['path']}/` - {issue['recommendation']}\n"
        else:
            report += "✅ All required directories present.\n"

        report += "\n---\n\n## 2. File Naming Violations\n\n"

        naming_violations = [v for v in self.violations if v['type'] == 'naming_violation']
        if naming_violations:
            report += "### Files Requiring Renaming\n\n"
            report += "| Current File | Issues | Recommended Name |\n"
            report += "|--------------|--------|------------------|\n"
            for v in naming_violations[:20]:  # Limit to first 20 for readability
                issues = ', '.join(v['violations'])
                report += f"| `{v['file']}` | {issues} | `{v['recommended']}` |\n"

            if len(naming_violations) > 20:
                report += f"\n*...and {len(naming_violations) - 20} more files*\n"
        else:
            report += "✅ All filenames compliant with CLAUDE.md standards.\n"

        report += "\n---\n\n## 3. Content Requiring Redaction\n\n"

        if self.redactions:
            report += "### Borderline Sensitive Information\n\n"
            report += "The following content should be reviewed and potentially redacted to maintain appropriate public disclosure boundaries:\n\n"

            # Group by type
            by_type = {}
            for r in self.redactions:
                by_type.setdefault(r['type'], []).append(r)

            for rtype, items in by_type.items():
                report += f"\n#### {rtype.replace('_', ' ').title()} ({len(items)} instances)\n\n"
                for item in items[:10]:  # Limit per type
                    report += f"**File:** `{item['file']}` (Line {item['line']})\n\n"
                    report += f"- **Match:** `{item['match']}`\n"
                    report += f"- **Context:** {item['context'][:100]}...\n"
                    report += f"- **Justification:** {item['justification']}\n"
                    report += f"- **Replacement:** `{item['recommended_replacement']}`\n\n"

                if len(items) > 10:
                    report += f"*...and {len(items) - 10} more instances*\n\n"
        else:
            report += "✅ No borderline sensitive content detected.\n"

        report += "\n---\n\n## 4. File Relocation Recommendations\n\n"

        if self.relocations:
            report += "### Misplaced Files\n\n"
            report += "| File | Current Location | Recommended Location | Reason |\n"
            report += "|------|------------------|----------------------|--------|\n"
            for r in self.relocations[:20]:
                report += f"| `{Path(r['file']).name}` | `{r['current']}/` | `{r['recommended']}/` | {r['reason']} |\n"

            if len(self.relocations) > 20:
                report += f"\n*...and {len(self.relocations) - 20} more files*\n"
        else:
            report += "✅ All files in appropriate directories.\n"

        report += f"""

---

## 5. Recommended Actions

### Immediate (Before Next Commit)

1. **Review flagged content** in section 3
2. **Approve or reject redactions** with justification
3. **Run agent in LIVE mode** if redactions approved
4. **Rename files** per section 2 recommendations

### Near-term (This Week)

1. **Relocate misplaced files** per section 4
2. **Create missing directories** per section 1
3. **Update internal links** after relocations
4. **Commit changes** with clear message

### Process Improvements

1. **Pre-commit hook** integration for auto-detection
2. **Monthly audits** using this agent
3. **Team training** on CLAUDE.md standards
4. **Documentation review** checklist

---

## Approval Workflow

**To approve and execute changes:**

```bash
# Review this report carefully
cat ORGANIZATION_AUDIT_REPORT.md

# Execute file renames
python3 scripts/organization_sanitation_agent.py --mode=rename --execute

# Execute content redactions
python3 scripts/organization_sanitation_agent.py --mode=redact --execute

# Execute file relocations
python3 scripts/organization_sanitation_agent.py --mode=relocate --execute

# Commit all changes
git add -A
git commit -m "chore: repository sanitization and organization"
```

---

**Report Generated:** {self.timestamp}
**Status:** {'PREVIEW ONLY - No changes made' if self.dry_run else 'CHANGES EXECUTED'}
"""

        report_path = self.repo_path / 'ORGANIZATION_AUDIT_REPORT.md'
        with open(report_path, 'w') as f:
            f.write(report)

        print(f"📄 Report saved: {report_path}")

        # Also print summary to console
        print("\n" + "="*60)
        print("AUDIT SUMMARY")
        print("="*60)
        print(f"Directory Issues: {len([v for v in self.violations if v['type'] == 'missing_directory'])}")
        print(f"Naming Violations: {len([v for v in self.violations if v['type'] == 'naming_violation'])}")
        print(f"Content Redactions: {len(self.redactions)}")
        print(f"File Relocations: {len(self.relocations)}")
        print("="*60)

    def _execute_fixes(self):
        """Execute approved changes"""
        print("\n🔧 Phase 5: Executing fixes...")

        # Create missing directories
        for v in self.violations:
            if v['type'] == 'missing_directory':
                dir_path = self.repo_path / v['path']
                dir_path.mkdir(parents=True, exist_ok=True)
                print(f"✅ Created: {v['path']}/")

        # Rename files
        for v in self.violations:
            if v['type'] == 'naming_violation':
                old_path = self.repo_path / v['file']
                new_name = v['recommended']
                new_path = old_path.parent / new_name

                if old_path.exists():
                    shutil.move(str(old_path), str(new_path))
                    print(f"✅ Renamed: {v['file']} → {new_name}")

        # Apply content redactions
        files_to_redact = {}
        for r in self.redactions:
            if r['type'] != 'pdf_manual_review':
                files_to_redact.setdefault(r['file'], []).append(r)

        for filepath, redaction_list in files_to_redact.items():
            self._apply_redactions(filepath, redaction_list)

        # Relocate files
        for r in self.relocations:
            old_path = self.repo_path / r['file']
            new_dir = self.repo_path / r['recommended']
            new_dir.mkdir(parents=True, exist_ok=True)
            new_path = new_dir / old_path.name

            if old_path.exists():
                shutil.move(str(old_path), str(new_path))
                print(f"✅ Relocated: {r['file']} → {r['recommended']}/")

        print("\n✅ All approved fixes executed")

    def _apply_redactions(self, filepath: str, redaction_list: List[Dict]):
        """Apply redactions to file content"""
        full_path = self.repo_path / filepath

        try:
            with open(full_path, 'r', errors='ignore') as f:
                content = f.read()

            # Sort by position (reverse) to maintain positions
            redaction_list.sort(key=lambda x: x['line'], reverse=True)

            for redaction in redaction_list:
                # Simple replacement (in production, use more sophisticated matching)
                content = content.replace(redaction['match'], redaction['recommended_replacement'])

            with open(full_path, 'w') as f:
                f.write(content)

            print(f"✅ Applied {len(redaction_list)} redactions to: {filepath}")

        except Exception as e:
            print(f"❌ Failed to redact {filepath}: {e}")

    def _get_summary(self) -> Dict:
        """Return audit summary"""
        return {
            'timestamp': self.timestamp,
            'total_issues': len(self.violations) + len(self.redactions) + len(self.relocations),
            'directory_issues': len([v for v in self.violations if v['type'] == 'missing_directory']),
            'naming_violations': len([v for v in self.violations if v['type'] == 'naming_violation']),
            'content_redactions': len(self.redactions),
            'file_relocations': len(self.relocations),
            'mode': 'dry_run' if self.dry_run else 'live'
        }

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Repository Organization & Sanitization Agent')
    parser.add_argument('--mode', choices=['audit', 'rename', 'redact', 'relocate', 'full'],
                       default='audit', help='Operation mode')
    parser.add_argument('--execute', action='store_true',
                       help='Execute changes (default is dry-run)')
    parser.add_argument('--repo-path', default='.',
                       help='Path to repository')

    args = parser.parse_args()

    agent = OrganizationSanitationAgent(
        repo_path=args.repo_path,
        dry_run=not args.execute
    )

    if args.mode == 'audit':
        summary = agent.run_full_audit()
    else:
        print(f"Mode {args.mode} not yet implemented")
        sys.exit(1)

    # Exit code based on findings
    if summary['total_issues'] > 0:
        print(f"\n⚠️  {summary['total_issues']} issues found")
        if args.execute:
            print("✅ Changes applied")
            sys.exit(0)
        else:
            print("ℹ️  Run with --execute to apply changes")
            sys.exit(1)
    else:
        print("\n✅ Repository fully compliant")
        sys.exit(0)

if __name__ == '__main__':
    main()
