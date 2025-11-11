---
description: "Gracefully close a documentation session: summary of progress, update logs, and clear temporary context."
allowed-tools: ["Read", "Search", "Edit", "Bash(git:*)", "Bash(find)", "Bash(rm)", "Grep"]
author: "Ryno Crypto Services"
version: "2.0"
---

# Close Session

## Purpose
Gracefully conclude a documentation/media work session by documenting progress, validating file organization, ensuring OPSEC compliance, and preparing for the next session or contributor.

**Context**: This repository is primarily a **documentation and media asset repository**. Session closure focuses on documentation quality, file organization, naming conventions, and security compliance rather than software testing or builds.

**Reusability Note:** This workflow can be invoked:
- **Standalone**: Via `/close-session` command for manual session closure
- **Orchestrated**: As part of `/policy-initiator` command (Phase 5) for OPSEC compliance workflows

---

## Session Closing Steps

### 1. Capture Final Session State

```bash
# Show current branch and status
!git branch --show-current
!git status --porcelain

# Get uncommitted changes count
!git status --short | wc -l

# Show final commits this session (last 3 hours)
!git log --oneline --since="3 hours ago"

# List modified files
!git diff HEAD --name-status
```

### 2. Review Session Progress

**Prompt user:**

```
📋 Session Review - Documentation & Media Repository

1. What did you accomplish this session?
   ☐ Created new documentation
   ☐ Updated existing documentation
   ☐ Organized/renamed files
   ☐ Added/optimized media assets
   ☐ Updated PRDs or specifications
   ☐ OPSEC compliance work
   ☐ Other: [specify]

2. Documentation Quality Check
   ☐ All markdown files properly formatted
   ☐ Links validated and working
   ☐ Images/diagrams added where needed
   ☐ Metadata and frontmatter complete
   ☐ File naming conventions followed

3. Work Commit Status
   - ✅ All changes committed
   - 🟡 Partially committed
   - ⚠️ No, work in progress
   [User selects status]

4. What's left for next session?
   [User describes remaining documentation work]

5. Any blockers or issues?
   ☐ Missing information for documentation
   ☐ Unclear requirements
   ☐ Need stakeholder review
   ☐ Other: [specify]

6. Notes for next contributor/session?
   [User provides context]
```

### 3. Documentation Quality Validation

**Check documentation completeness:**

```bash
# Find all markdown files
!find . -name "*.md" -type f | grep -v node_modules | grep -v ".git"

# Check for broken links (if available)
# !markdown-link-check README.md 2>/dev/null

# Verify documentation structure
!ls -la docs/ prd/ specs/ 2>/dev/null

# Check for missing README files in key directories
!find . -type d -maxdepth 2 ! -path "./.*" -exec test ! -e {}/README.md \; -print
```

**Documentation Quality Checklist:**
- [ ] All new documentation has proper headers
- [ ] File references use correct format: `file_path:line_number`
- [ ] Images/diagrams are properly named and organized
- [ ] Cross-references between documents are accurate
- [ ] CLAUDE.md naming conventions followed
- [ ] No typos or grammar issues in visible sections

### 4. File Organization & Naming Convention Check

**Run organization validation:**

```bash
# Check for file naming violations (spaces, uppercase, etc.)
!find . -type f \( -name "* *" -o -name "*[A-Z]*" \) | grep -v ".git" | head -20

# Check for misplaced files
!find . -maxdepth 1 -type f -name "*.md" -o -name "*.pdf" -o -name "*.png" | grep -v "README\|LICENSE\|CLAUDE"

# List files that may need organization
!find . -type f \( -name "*.tmp" -o -name "*.bak" -o -name "*~" \) 2>/dev/null
```

**Organization Actions:**
- If naming violations found: Note for correction
- If files misplaced: Note for relocation to proper directories
- If temporary files found: Mark for cleanup

**Suggest running organization agent if issues detected:**
```
⚠️ File organization issues detected. Consider running:
python3 scripts/organization_sanitation_agent.py --mode=audit
```

### 5. OPSEC Compliance Check

**Quick security scan:**

```bash
# Check for common sensitive patterns (don't show matches, just count)
!grep -r "password\|api[_-]key\|secret\|token" . --include="*.md" --include="*.txt" | wc -l

# Check for financial data patterns
!grep -r "\$[0-9,]+\|revenue\|margin" . --include="*.md" --include="*.pdf" | wc -l
```

**If suspicious patterns detected:**
```
🔒 Potential sensitive content detected. Consider running:
python3 scripts/data_breach_agent.py
```

### 6. Ensure Work is Saved

```bash
# Check for uncommitted changes
UNCOMMITTED=$(git status --short | wc -l)

if [ $UNCOMMITTED -gt 0 ]; then
  echo "⚠️ Uncommitted changes detected:"
  git status --short
  echo ""
  echo "Options:"
  echo "1. Commit now"
  echo "2. Review changes first"
  echo "3. Leave uncommitted (not recommended)"
fi

# List unpushed commits
!git log origin/main..HEAD --oneline
```

**Actions:**
- If changes uncommitted: Prompt to commit with auto-generated message
- If commits unpushed: Prompt to push to remote
- If branch needs cleanup: Suggest cleanup for next session

### 7. Update Session Documentation

Create or update **session-work.md**:

```markdown
# Session Work Summary

**Date**: [YYYY-MM-DD HH:MM]
**Duration**: [X hours Y minutes]
**Session Type**: Documentation & Media Management

---

## Work Completed

### Documentation Created/Updated
- [Document 1] - [Brief description] (path/to/file.md)
- [Document 2] - [Brief description] (path/to/file.md)

### Media Assets Added/Organized
- [Asset 1] - [Description] (assets/path/file.png)
- [Asset 2] - [Description] (assets/path/diagram.svg)

### File Organization
- Renamed [N] files to follow naming conventions
- Relocated [N] files to proper directories
- Created new directory structure: [list]

### OPSEC & Compliance
- Data Breach Scan: [✅ Passed / ⚠️ Issues Found / ⏭️ Skipped]
- Organization Check: [✅ Passed / ⚠️ Issues Found / ⏭️ Skipped]
- Issues remediated: [summary]

---

## Files Modified

- `path/to/doc1.md` - [Description of changes]
- `path/to/doc2.md` - [Description of changes]
- `assets/images/file.png` - [Added/Updated/Renamed]

---

## Documentation Decisions

- [Decision 1]: [Rationale]
  - Example: "Used CLAUDE.md naming convention: ryno-crypto-architecture-diagram-v1-0.png"
- [Decision 2]: [Rationale]

---

## Work Remaining

### TODO
- [ ] Complete documentation for [topic]
- [ ] Add diagrams to [document]
- [ ] Review and approve [pending item]
- [ ] Update [outdated documentation]

### Known Issues
- [Issue 1]: Missing information about [topic]
- [Issue 2]: Awaiting stakeholder review for [document]

### Next Session Priorities
1. **High**: [Task] - [Why important]
2. **Medium**: [Task] - [Context]
3. **Low**: [Task] - [Nice to have]

---

## File Organization Status

**Directory Structure**: ✅ Compliant / ⚠️ Needs Work
**Naming Conventions**: ✅ Compliant / ⚠️ Violations Found
**OPSEC Compliance**: ✅ Passed / ⚠️ Review Needed

### Issues Detected
- Naming violations: [count] files
- Misplaced files: [count] files
- Sensitive content: [None / Review required]

---

## Git Summary

**Branch**: [branch-name]
**Commits this session**: [N]
**Files changed**: [N]
**Ready for push**: [yes/no]

---

## Notes

[Any additional context, observations, or important information for next session]

---

**Session Summary Generated**: [Timestamp]
**Next Session Recommended**: [Suggestions for when to continue]
```

### 8. Run Cleanup (Optional)

**Identify cleanup opportunities:**

```bash
# Find temporary files
!find . -type f \( -name "*.tmp" -o -name "*.bak" -o -name "*~" -o -name ".DS_Store" \) 2>/dev/null

# Find empty directories
!find . -type d -empty 2>/dev/null | grep -v ".git"

# Check for duplicate images (by name pattern)
!find assets -type f -name "*.png" -o -name "*.jpg" | sort | uniq -d 2>/dev/null
```

**Cleanup Actions:**
```
Temporary files found:
- [Temp file 1]: Delete? (yes/no)
- [Temp file 2]: Archive? (yes/no)

Empty directories found:
- [Directory 1]: Remove? (yes/no)

Potential duplicates:
- [File 1]: Review? (yes/no)
```

### 9. Commit Final Changes (if approved)

```bash
# Show uncommitted changes
!git status --porcelain

# Prompt user: Commit changes?
# If yes, generate commit message:

!git add session-work.md  # Always include session documentation

# Auto-generate commit message based on work
!git commit -m "$(cat <<'EOF'
docs: session work completed [date]

Session Summary:
- Documentation: [X files updated/created]
- Media assets: [Y files added/updated]
- Organization: [Z files renamed/relocated]
- OPSEC compliance: [status]

📄 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"

# Ask about pushing
!git push origin $(git branch --show-current)
```

### 10. Generate Session Summary Report

**Display formatted summary:**

```
╔════════════════════════════════════════════════════════╗
║     SESSION CLOSED SUCCESSFULLY - Documentation Work   ║
╚════════════════════════════════════════════════════════╝

📅 SESSION DATE: [Date]
⏱️  DURATION: [X]h [Y]m
📁 REPOSITORY: ryno-assets (Documentation & Media)
🌿 BRANCH: [branch-name]

📝 DOCUMENTATION WORK:
  ✅ [N] documents created/updated
  ✅ [N] media assets added/organized
  ✅ [N] files renamed for compliance
  ✅ [N] directories reorganized

🔒 OPSEC COMPLIANCE:
  ✅ Data breach scan: [status]
  ✅ Organization check: [status]
  ✅ Naming conventions: [status]

📊 REPOSITORY STATUS:
  Files Modified: [N]
  Commits: [N]
  Ready to Push: [Yes/No]

📋 NEXT SESSION:
  Priority 1: [Task]
  Priority 2: [Task]
  Priority 3: [Task]

⚠️  BLOCKERS:
  [N] issues noted
  [List if any]

📄 DOCUMENTATION:
  ✅ session-work.md updated
  ✅ Changes documented
  ✅ Context preserved

🎯 READY FOR:
  ✅ Next contributor
  ✅ Next session
  ✅ Stakeholder review (if applicable)

📤 GIT STATUS:
  Branch: [branch-name]
  Pushed: [✅ YES / ⏸️ NOT YET]
  Commits: [N] ahead of main

⏰ Session closed at: [Time]
📅 Next recommended start: [Suggestion]
```

---

## Session Closure Checklist

- [ ] Reviewed session accomplishments
- [ ] All documentation changes committed
- [ ] File naming conventions followed
- [ ] Files organized in correct directories
- [ ] OPSEC compliance verified
- [ ] session-work.md updated
- [ ] No uncommitted changes (or intentionally left)
- [ ] No temporary files remaining
- [ ] Next session priorities documented
- [ ] Blockers and issues recorded
- [ ] Commits pushed to remote (if ready)
- [ ] Ready for handoff (if needed)

---

## Key Features for Documentation Repository

- **Documentation Focus**: Emphasizes doc quality over code quality
- **File Organization**: Checks naming conventions and directory structure
- **OPSEC Integration**: References security agents for compliance
- **Media Asset Management**: Tracks image/diagram organization
- **Session Logging**: Creates comprehensive work history
- **Cleanup Suggestions**: Identifies temp files and duplicates
- **Handoff Ready**: Prepares context for next contributor

---

## When to Use /close-session

- End of each documentation session
- After adding/updating significant documentation
- After reorganizing files or directories
- After OPSEC compliance work
- Before extended time off
- End of work day
- Before handing off to another contributor
- After completing a documentation milestone

---

## Best Practices

1. **Always Document**: Record what documentation was created/updated
2. **Follow Naming**: Adhere to CLAUDE.md file naming conventions
3. **Organize Files**: Ensure files are in correct directories
4. **Run OPSEC Checks**: Use data-breach-agent for sensitive content
5. **Update Session Log**: Keep session-work.md current
6. **Note Context**: Document decisions and rationale
7. **Commit Regularly**: Don't leave large uncommitted changes
8. **Clean Up**: Remove temporary files before closing
9. **Plan Ahead**: Document priorities for next session
10. **Communicate**: Note if stakeholder review needed

---

**Document Version**: 2.0.0
**Last Updated**: 2025-11-10
**Maintained By**: Ryno Crypto Services
**Adapted From**: docs/claude/commands-templates/close-session.md
