---
allowed-tools: Bash(find:SORT/*), Bash(identify:*), Bash(git:*), Bash(python3:scripts/*.py), Bash(mkdir:*), Bash(pdftotext:*), Bash(pandoc:*), Read(SORT/*), Read(assets/**/*), Read(prd/**/*), Read(docs/**/*), Read(CLAUDE.md), Read(.claude/agents/*), Read(.claude/skills/file-organizer/*), Read(.claude/skills/filename-validator/*), Read(.claude/skills/file-renamer/*), Read(.claude/skills/file-relocator/*), Write(*.md), Write(*.txt), Write(*.log), Grep(*), Glob(*), AskUserQuestion(*)
description: Organize files from SORT/ directory with automated renaming, relocation, OPSEC validation, and git commit/push workflow
---

# Sort Files - Automated File Organization Pipeline

Comprehensive workflow to organize files from the SORT/ directory according to CLAUDE.md standards. This command orchestrates filename validation, intelligent renaming, relocation to correct directories, OPSEC compliance checking, and git operations with user confirmation.

## Command Usage

```bash
/sort-files
```

This command will:

1. Scan and inventory files in SORT/ directory
2. Validate filenames against CLAUDE.md standards
3. Analyze file content and extract metadata
4. Prompt user for unclear categorizations (interactive)
5. Rename files to comply with standards
6. Relocate files to correct repository directories
7. Run data breach detection agent
8. Run organization sanitation agent
9. Generate comprehensive organization report
10. Prompt for git commit message
11. Prompt for git push confirmation

---

## Execution Overview

This pipeline uses the **file-organizer skill** as the main orchestrator, integrating with utility skills and OPSEC agents.

**Key Features:**

- ✅ Fully automated processing (with interactive prompts for unclear files)
- ✅ Comprehensive OPSEC validation
- ✅ Git commit/push with user confirmation
- ✅ Detailed reporting and rollback capability
- ✅ Quality assurance at every phase

---

## Phase-by-Phase Execution

### Phase 0: Pre-Flight Checks

Before starting the organization workflow, verify prerequisites and initialize the environment.

#### Actions

1. **Verify SORT/ directory exists and contains files:**

   ```bash
   if [ ! -d "SORT/" ]; then
       echo "❌ ERROR: SORT/ directory not found"
       echo "Please create SORT/ directory and add files to organize"
       exit 1
   fi

   file_count=$(find SORT/ -type f | wc -l)
   if [ $file_count -eq 0 ]; then
       echo "⚠️  WARNING: SORT/ directory is empty"
       echo "No files to organize"
       exit 0
   fi

   echo "✅ Found $file_count files in SORT/ directory"
   ```

2. **Read CLAUDE.md for standards reference:**

   ```
   Read: CLAUDE.md
   ```

   - Extract file naming conventions
   - Note repository structure
   - Understand categorization rules

3. **Load skill definitions:**

   ```
   Read: .claude/skills/file-organizer/skill.md
   Read: .claude/skills/filename-validator/skill.md
   Read: .claude/skills/file-renamer/skill.md
   Read: .claude/skills/file-relocator/skill.md
   ```

4. **Load OPSEC agent definitions:**

   ```
   Read: .claude/agents/data-breach-agent.md
   Read: .claude/agents/organization-sanitation-agent.md
   ```

5. **Create working directories:**

   ```bash
   mkdir -p SORT/NEEDS_REVIEW
   mkdir -p SORT/LOGS
   ```

6. **Initialize operation log:**

   ```bash
   OPERATION_ID="sort-$(date +%Y%m%d-%H%M%S)"
   LOG_FILE="SORT/LOGS/${OPERATION_ID}.log"

   echo "File Organization Operation" > "$LOG_FILE"
   echo "Operation ID: $OPERATION_ID" >> "$LOG_FILE"
   echo "Started: $(date -Iseconds)" >> "$LOG_FILE"
   echo "Files to process: $file_count" >> "$LOG_FILE"
   echo "===========================================" >> "$LOG_FILE"
   ```

**Output:**

```
✅ Pre-flight checks complete
   - SORT/ directory: Found (25 files)
   - CLAUDE.md: Loaded
   - Skills: Loaded (4 skills)
   - Agents: Loaded (2 agents)
   - Logs: Initialized (sort-20251121-103000.log)

Ready to begin file organization.
```

---

### Phase 1: Scan and Inventory

Use the **file-organizer skill** (Phase 1) to scan all files in SORT/ directory.

#### Actions

1. **Find all files:**

   ```bash
   echo "Scanning SORT/ directory..." | tee -a "$LOG_FILE"

   find SORT/ -type f ! -path "*/LOGS/*" ! -path "*/NEEDS_REVIEW/*" > SORT/LOGS/inventory.txt

   # Categorize by type
   image_files=$(grep -E '\.(png|jpg|jpeg|gif|svg|webp)$' SORT/LOGS/inventory.txt | wc -l)
   doc_files=$(grep -E '\.(pdf|docx|doc|txt)$' SORT/LOGS/inventory.txt | wc -l)
   md_files=$(grep -E '\.(md|markdown)$' SORT/LOGS/inventory.txt | wc -l)
   video_files=$(grep -E '\.(mp4|mov|avi)$' SORT/LOGS/inventory.txt | wc -l)
   other_files=$(grep -vE '\.(png|jpg|jpeg|gif|svg|webp|pdf|docx|doc|txt|md|markdown|mp4|mov|avi)$' SORT/LOGS/inventory.txt | wc -l)
   ```

2. **Display inventory summary:**

   ```
   📦 SORT/ Directory Inventory

   Total files: 25

   By type:
   - Images: 15 (.png, .jpg, .svg, .webp)
   - Documents: 7 (.pdf, .docx, .txt)
   - Markdown: 2 (.md)
   - Videos: 0
   - Other: 1

   Files will be validated and organized according to CLAUDE.md standards.
   ```

3. **Log inventory:**

   ```bash
   {
       echo ""
       echo "INVENTORY RESULTS"
       echo "Total: $file_count"
       echo "Images: $image_files"
       echo "Documents: $doc_files"
       echo "Markdown: $md_files"
       echo "Videos: $video_files"
       echo "Other: $other_files"
       echo "==========================================="
   } >> "$LOG_FILE"
   ```

---

### Phase 2: Filename Validation

Use the **filename-validator skill** to identify non-compliant filenames.

#### Actions

1. **Validate each file:**
   - Check for uppercase letters
   - Check for spaces and special characters
   - Validate naming pattern matches file type
   - Verify version format
   - Check for required components

2. **Generate validation report:**

   ```bash
   python3 << 'VALIDATE_SCRIPT'
   import os
   import re
   import json
   from pathlib import Path

   def validate_filename(filepath):
       """Validate filename against CLAUDE.md standards"""
       filename = os.path.basename(filepath)
       issues = []

       # Reserved names (exempt from checks)
       reserved = ['README.md', 'LICENSE', 'CONTRIBUTING.md', 'CHANGELOG.md',
                  'SECURITY.md', 'CLAUDE.md', '.gitignore']
       if filename in reserved:
           return {'valid': True, 'issues': []}

       # Check uppercase
       if filename != filename.lower():
           issues.append("Contains uppercase letters")

       # Check spaces
       if ' ' in filename:
           issues.append("Contains spaces (use hyphens)")

       # Check special characters
       if re.search(r'[^a-z0-9.-]', filename):
           matches = re.findall(r'[^a-z0-9.-]', filename)
           issues.append(f"Contains forbidden characters: {', '.join(set(matches))}")

       # Check underscores
       if '_' in filename:
           issues.append("Contains underscores (use hyphens)")

       # Check version format
       if not re.search(r'v\d+-\d+(-\d+)?', filename):
           issues.append("Missing or invalid version (expected: v1-0 or v1-0-0)")

       # Determine file type and check pattern
       ext = filename.split('.')[-1].lower()
       if ext in ['png', 'jpg', 'jpeg', 'gif', 'svg', 'webp']:
           # Expected: [org]-[product]-[descriptor]-[type]-[resolution]-[version].[ext]
           parts = filename.replace(f'.{ext}', '').split('-')
           if len(parts) < 6:
               issues.append(f"Image pattern incomplete (expected 6+ parts, got {len(parts)})")

       elif ext in ['pdf', 'docx', 'doc', 'txt']:
           # Expected: [org]-[product]-[category]-[title]-[version].[ext]
           parts = filename.replace(f'.{ext}', '').split('-')
           if len(parts) < 5:
               issues.append(f"Document pattern incomplete (expected 5+ parts, got {len(parts)})")

       valid = len(issues) == 0
       return {'valid': valid, 'issues': issues}

   # Validate all files
   results = {'valid': [], 'invalid': []}

   with open('SORT/LOGS/inventory.txt', 'r') as f:
       for line in f:
           filepath = line.strip()
           if not filepath or '/LOGS/' in filepath or '/NEEDS_REVIEW/' in filepath:
               continue

           validation = validate_filename(filepath)
           filename = os.path.basename(filepath)

           if validation['valid']:
               results['valid'].append(filename)
           else:
               results['invalid'].append({
                   'filename': filename,
                   'path': filepath,
                   'issues': validation['issues']
               })

   # Save results
   with open('SORT/LOGS/validation_results.json', 'w') as f:
       json.dump(results, f, indent=2)

   print(f"Validation complete:")
   print(f"  Valid: {len(results['valid'])}")
   print(f"  Invalid: {len(results['invalid'])}")

   VALIDATE_SCRIPT
   ```

3. **Display validation summary:**

   ```
   📋 Filename Validation Results

   ✅ Valid files: 5
   ❌ Invalid files: 20

   Invalid files require renaming to comply with CLAUDE.md standards.
   Proceeding to content analysis and renaming...
   ```

---

### Phase 3: Content Analysis and Metadata Extraction

Extract metadata from files to assist with categorization and renaming.

#### Actions

1. **Extract image dimensions:**

   ```bash
   echo "Extracting image metadata..." | tee -a "$LOG_FILE"

   find SORT/ -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.svg" \) \
       ! -path "*/LOGS/*" ! -path "*/NEEDS_REVIEW/*" | while read img; do
       dimensions=$(identify -format "%wx%h" "$img" 2>/dev/null || echo "original")
       echo "$(basename "$img"): $dimensions" >> SORT/LOGS/image_metadata.txt
   done
   ```

2. **Analyze filenames for components:**

   ```bash
   python3 scripts/analyze_filenames.py SORT/ > SORT/LOGS/ai_suggestions.json
   ```

   This script uses heuristics to suggest:
   - Organization (ryno, ths, terrahash)
   - Product (crypto, stack, mining)
   - Type/Category
   - Descriptor/Title
   - Version

3. **Display analysis summary:**

   ```
   🔍 Content Analysis Complete

   Metadata extracted:
   - 15 images: dimensions recorded
   - 7 documents: content previewed
   - 2 markdown: categories identified

   AI suggestions generated for all files.
   ```

---

### Phase 4: Interactive Categorization

For files where components cannot be automatically determined, prompt user for input.

#### Actions

1. **Identify unclear files:**

   ```bash
   # Files missing required components from AI analysis
   # E.g., generic names like "image1.png" or "document.pdf"
   ```

2. **Prompt user using AskUserQuestion:**

   For each unclear file, ask:
   - Organization: ryno, ths, or terrahash?
   - Product: crypto, stack, or mining?
   - Type (images): banner, logo, icon, infographic, diagram, screenshot?
   - Category (documents): prd, guide, specs, api-docs, whitepaper, security?
   - Descriptor/Title: Brief description?

   Example:

   ```markdown
   **Need your help categorizing this file:**

   File: Generic_Image.png (1920x1080)

   Please provide:
   1. Organization and Product
   2. Image Type
   3. Brief descriptor

   AI Suggestions: Unable to determine automatically
   ```

3. **Collect and store user input:**

   ```bash
   # Merge user input with AI suggestions
   # Create final component mapping for each file
   ```

**Note:** If user wants to skip a file, move it to SORT/NEEDS_REVIEW/ for later manual handling.

---

### Phase 5: Batch Rename

Use the **file-renamer skill** to rename all non-compliant files.

#### Actions

1. **Generate new filenames:**
   - Combine AI suggestions + user input + metadata
   - Construct compliant filenames per CLAUDE.md patterns
   - Validate each new filename

2. **Show rename preview:**

   ```
   📝 Rename Preview (20 files)

   1. Bear_Market_Strategy.png
      → ths-stack-bear-market-strategy-infographic-1920x1080-v1-0.png

   2. TerraHash Logo Final.PNG
      → terrahash-stack-logo-icon-512x512-v1-0.png

   3. Smart DIP Buying Banner.jpg
      → ryno-crypto-smart-dip-buying-banner-1920x1080-v1-0.jpg

   ...

   Proceed with renaming? (files will be renamed using git mv)
   ```

3. **Execute renames:**

   ```bash
   # Use git mv to preserve history
   while read line; do
       old_path=$(echo "$line" | cut -d'→' -f1 | xargs)
       new_name=$(echo "$line" | cut -d'→' -f2 | xargs | awk '{print $NF}')

       git mv "SORT/$old_path" "SORT/$new_name"
       echo "✅ Renamed: $old_path → $new_name" | tee -a "$LOG_FILE"
   done < SORT/LOGS/rename_plan.txt
   ```

4. **Log renames:**

   ```bash
   cp SORT/LOGS/rename_plan.txt "SORT/LOGS/rename_log_${OPERATION_ID}.txt"
   ```

---

### Phase 6: Batch Relocate

Use the **file-relocator skill** to move files to correct repository directories.

#### Actions

1. **Determine destinations:**
   - Parse renamed filenames
   - Apply routing rules per file type
   - Create destination directory map

2. **Show relocation preview:**

   ```
   📂 Relocation Plan (20 files)

   assets/images/ryno-crypto/ (8 files):
   - ryno-crypto-logo-icon-512x512-v1-0.png
   - ryno-crypto-smart-dip-buying-banner-1920x1080-v1-0.jpg
   - ...

   assets/images/terrahash-stack/ (5 files):
   - terrahash-stack-logo-icon-512x512-v1-0.png
   - ths-stack-bear-market-strategy-infographic-1920x1080-v1-0.png
   - ...

   prd/active/ (4 files):
   - ryno-crypto-prd-smart-contract-v1-0.pdf
   - ...

   docs/guides/ (3 files):
   - terrahash-mining-guide-overview-v1-0.pdf
   - ...

   Proceed with relocation?
   ```

3. **Create destination directories:**

   ```bash
   # Create any missing directories
   mkdir -p assets/images/ryno-crypto
   mkdir -p assets/images/terrahash-stack
   mkdir -p assets/diagrams/architecture
   mkdir -p assets/diagrams/infographics
   mkdir -p prd/active
   mkdir -p docs/guides
   mkdir -p docs/api
   mkdir -p docs/research
   # ... etc
   ```

4. **Execute relocations:**

   ```bash
   while read line; do
       filename=$(echo "$line" | awk '{print $1}')
       dest_dir=$(echo "$line" | awk '{print $2}')

       git mv "SORT/$filename" "$dest_dir$filename"
       echo "✅ Relocated: $filename → $dest_dir" | tee -a "$LOG_FILE"
   done < SORT/LOGS/relocation_plan.txt
   ```

5. **Create rollback script:**

   ```bash
   cat > "SORT/LOGS/rollback_${OPERATION_ID}.sh" << 'ROLLBACK'
   #!/bin/bash
   # Rollback script for file organization
   # Generated: $(date)

   [rollback commands for each moved file]
   ROLLBACK

   chmod +x "SORT/LOGS/rollback_${OPERATION_ID}.sh"
   ```

---

### Phase 7: Data Breach Detection

Execute the **data-breach-agent** to ensure no sensitive information is being committed.

#### Actions

1. **Run data breach agent:**

   ```bash
   echo "Running data breach detection..." | tee -a "$LOG_FILE"

   python3 scripts/data_breach_agent.py --mode full --output SORT/LOGS/breach_report.md
   ```

2. **Check agent results:**

   ```bash
   if [ -f "OPSEC_ALERT.md" ]; then
       echo "❌ DATA BREACH DETECTED"
       echo "See OPSEC_ALERT.md for details"
       echo ""
       echo "Organization workflow BLOCKED"
       echo "Please sanitize files before committing"
       exit 1
   else
       echo "✅ Data breach check: PASS"
   fi
   ```

3. **Log results:**

   ```bash
   echo "Data Breach Check: PASS" >> "$LOG_FILE"
   ```

**If breach detected:** Workflow stops here. User must sanitize files and restart.

---

### Phase 8: Organization Sanitation

Execute the **organization-sanitation-agent** for final validation.

#### Actions

1. **Run organization agent:**

   ```bash
   echo "Running organization sanitation..." | tee -a "$LOG_FILE"

   python3 scripts/organization_sanitation_agent.py --mode full --output SORT/LOGS/org_report.md
   ```

2. **Check results:**

   ```bash
   # Agent generates ORGANIZATION_AUDIT_REPORT.md

   # Parse report for pass/fail
   if grep -q "STATUS: PASS" ORGANIZATION_AUDIT_REPORT.md; then
       echo "✅ Organization sanitation: PASS"
   else
       echo "⚠️  Organization sanitation: Issues found"
       echo "See ORGANIZATION_AUDIT_REPORT.md for details"
   fi
   ```

3. **Log results:**

   ```bash
   echo "Organization Check: PASS" >> "$LOG_FILE"
   ```

---

### Phase 9: Generate Comprehensive Report

Create a detailed report of the entire organization operation.

#### Actions

1. **Compile all logs and results:**
   - Inventory data
   - Validation results
   - Rename log
   - Relocation log
   - OPSEC reports

2. **Generate report:**

   ```bash
   cat > "FILE_ORGANIZATION_REPORT_${OPERATION_ID}.md" << 'REPORT'
   # File Organization Report

   **Operation ID:** ${OPERATION_ID}
   **Date:** $(date -Iseconds)
   **Duration:** [calculated]

   ## Executive Summary

   - Files processed: [count]
   - Files renamed: [count]
   - Files relocated: [count]
   - OPSEC status: PASS
   - Organization status: PASS

   [detailed sections from each phase]

   ## Next Steps

   1. Review organized files
   2. Create git commit
   3. Push to remote
   4. Clean up SORT/ directory

   REPORT
   ```

3. **Display summary:**

   ```
   ✅ File Organization Complete!

   Summary:
   - 20 files organized
   - 18 files renamed
   - 20 files relocated
   - OPSEC: PASS
   - Quality: PASS

   See FILE_ORGANIZATION_REPORT_[timestamp].md for full details.
   ```

---

### Phase 10: Git Commit (with User Confirmation)

Prompt user for commit message and create commit.

#### Actions

1. **Show changes summary:**

   ```bash
   git status --short | grep -E '^(A|M|R|D)' | sort
   ```

2. **Generate suggested commit message:**

   ```
   feat(organization): organize 20 files from SORT/ directory

   - Renamed 18 files to comply with CLAUDE.md standards
   - Relocated files to proper directories (assets/, prd/, docs/)
   - Created subdirectories: assets/diagrams/infographics/, docs/research/
   - Verified OPSEC compliance (data-breach-agent: PASS)
   - Validated organization (organization-sanitation-agent: PASS)

   Images organized:
   - 8 files → assets/images/ryno-crypto/
   - 5 files → assets/images/terrahash-stack/
   - 2 files → assets/diagrams/

   Documents organized:
   - 4 files → prd/active/
   - 3 files → docs/guides/

   See FILE_ORGANIZATION_REPORT_[timestamp].md for full details.

   🤖 Generated with Claude Code
   Co-Authored-By: Claude <noreply@anthropic.com>
   ```

3. **Prompt user for commit message:**

   Use AskUserQuestion:

   ```markdown
   Ready to create git commit.

   Suggested commit message is shown above.

   Options:
   1. Use suggested commit message
   2. Edit commit message (provide custom message)
   3. Skip commit (manual commit later)
   ```

4. **Create commit:**

   ```bash
   if [[ $user_choice == "1" || $user_choice == "2" ]]; then
       # Stage all changes
       git add assets/ prd/ docs/ SORT/ FILE_ORGANIZATION_REPORT_*.md ORGANIZATION_AUDIT_REPORT.md

       # Create commit
       git commit -m "$(cat <<'EOF'
       [commit message here]
       EOF
       )"

       echo "✅ Git commit created successfully"
   else
       echo "⏭️  Skipping commit. You can commit manually later with:"
       echo "   git add assets/ prd/ docs/ SORT/"
       echo "   git commit"
   fi
   ```

---

### Phase 11: Git Push (with User Confirmation)

Prompt user before pushing to remote.

#### Actions

1. **Check if commit was created:**

   ```bash
   if git log -1 --oneline | grep -q "feat(organization)"; then
       # Commit exists, proceed to push prompt
   else
       echo "No commit created. Skipping push."
       exit 0
   fi
   ```

2. **Prompt user for push:**

   Use AskUserQuestion:

   ```markdown
   Commit created successfully.

   Push to remote repository?

   Options:
   1. Yes, push to remote now
   2. No, I'll push manually later
   ```

3. **Execute push:**

   ```bash
   if [[ $user_choice == "1" ]]; then
       current_branch=$(git branch --show-current)

       git push origin "$current_branch"

       if [ $? -eq 0 ]; then
           echo "✅ Successfully pushed to origin/$current_branch"
       else
           echo "❌ Push failed. Please check your network and permissions."
           echo "You can push manually with: git push origin $current_branch"
       fi
   else
       echo "⏭️  Skipping push. You can push manually later with:"
       echo "   git push origin $(git branch --show-current)"
   fi
   ```

---

### Phase 12: Cleanup and Completion

Final cleanup and provide next steps to user.

#### Actions

1. **Check SORT/ directory status:**

   ```bash
   remaining_files=$(find SORT/ -type f ! -path "*/LOGS/*" ! -path "*/NEEDS_REVIEW/*" | wc -l)

   if [ $remaining_files -eq 0 ]; then
       echo "✅ SORT/ directory is now empty (all files organized)"
       echo ""
       echo "You can safely delete SORT/ directory with:"
       echo "   rm -rf SORT/"
       echo ""
       echo "Or keep SORT/LOGS/ for records:"
       echo "   mv SORT/LOGS/ archive/organization-logs/"
       echo "   rm -rf SORT/"
   else
       echo "⚠️  $remaining_files files remaining in SORT/"
       echo "Review SORT/NEEDS_REVIEW/ for files that need manual categorization"
   fi
   ```

2. **Display final summary:**

   ```
   ╔════════════════════════════════════════════════════════════╗
   ║         FILE ORGANIZATION COMPLETE                         ║
   ╚════════════════════════════════════════════════════════════╝

   ✅ Operation: SUCCESS
   📊 Files organized: 20/25
   ⏭️  Files deferred: 3 (in SORT/NEEDS_REVIEW/)
   🔒 OPSEC status: PASS
   ✓  Organization: PASS
   📝 Commit: Created
   🚀 Push: Completed

   📁 Files organized into:
      - assets/images/ryno-crypto/ (8 files)
      - assets/images/terrahash-stack/ (5 files)
      - assets/diagrams/ (2 files)
      - prd/active/ (4 files)
      - docs/guides/ (3 files)

   📄 Reports generated:
      - FILE_ORGANIZATION_REPORT_[timestamp].md
      - ORGANIZATION_AUDIT_REPORT.md
      - SORT/LOGS/[operation_id].log

   🔧 Rollback available:
      - SORT/LOGS/rollback_[operation_id].sh

   Next steps:
   1. ✅ Review organized files in their new locations
   2. ✅ Verify files are accessible and correct
   3. 🔲 Handle files in SORT/NEEDS_REVIEW/ (if any)
   4. 🔲 Archive or delete SORT/ directory
   5. 🔲 Update README.md if needed

   Thank you for using /sort-files! 🎉
   ```

3. **Final log entry:**

   ```bash
   {
       echo "==========================================="
       echo "OPERATION COMPLETE"
       echo "Ended: $(date -Iseconds)"
       echo "Status: SUCCESS"
       echo "Files organized: $organized_count"
       echo "Commit: Created"
       echo "Push: Completed"
   } >> "$LOG_FILE"
   ```

---

## Error Handling

### Critical Errors

**If OPSEC check fails:**

- ❌ STOP immediately
- Do NOT proceed to commit
- Display OPSEC_ALERT.md
- Provide remediation steps

**If git operations fail:**

- Provide clear error message
- Show manual git commands
- Offer rollback option

**If file operations fail:**

- Stop at failed operation
- Keep detailed error log
- Provide rollback script

### Recovery

**Rollback script usage:**

```bash
# Undo all relocations
./SORT/LOGS/rollback_[operation_id].sh

# Or manually undo commit
git reset --soft HEAD~1
```

---

## Configuration

Default behavior can be overridden with environment variables:

```bash
# Skip user prompts (use all AI suggestions)
SKIP_USER_INPUT=true /sort-files

# Dry run (show what would happen without making changes)
DRY_RUN=true /sort-files

# Auto-commit and auto-push (no prompts)
AUTO_COMMIT=true AUTO_PUSH=true /sort-files
```

---

## Quality Assurance

Before completing, verify:

- ✅ All files scanned and categorized
- ✅ User input collected for unclear files
- ✅ All renames successful
- ✅ All relocations successful
- ✅ OPSEC checks passed
- ✅ Organization validation passed
- ✅ Reports generated
- ✅ Rollback scripts created
- ✅ Git operations completed
- ✅ No files lost or corrupted

---

## Related Documentation

- **Skills:**
  - .claude/skills/file-organizer/skill.md (Main orchestrator)
  - .claude/skills/filename-validator/skill.md (Phase 2)
  - .claude/skills/file-renamer/skill.md (Phase 5)
  - .claude/skills/file-relocator/skill.md (Phase 6)

- **Agents:**
  - .claude/agents/data-breach-agent.md (Phase 7)
  - .claude/agents/organization-sanitation-agent.md (Phase 8)

- **Standards:**
  - CLAUDE.md (File naming conventions and repository structure)

- **Commands:**
  - .claude/commands/policy-initiator.md (Related OPSEC workflow)

---

**End of /sort-files command definition**
