---
allowed-tools: Bash(python3:scripts/*.py), Bash(git:*), Read(session-work.md), Read(.claude/commands/*), Write(session-work.md), Grep(*)
description: Execute OPSEC policy enforcement pipeline with data breach detection and organization sanitization
---

# Policy Initiator - OPSEC Compliance Pipeline

Execute the complete OPSEC policy enforcement workflow to ensure repository compliance with security policies and organizational standards. This command orchestrates data breach detection, organization sanitization, session documentation, and git operations.

## Execution Overview

This pipeline consists of 7 phases that can be executed with varying levels of automation:

1. **Phase 0**: Load session context from previous work
2. **Phase 1**: Select agent execution mode (interactive or auto)
3. **Phase 2**: Execute data breach detection agent (if selected)
4. **Phase 3**: Execute organization sanitization agent (if selected)
5. **Phase 4**: Run pre-commit hooks validation
6. **Phase 5**: Document work via session-close workflow
7. **Phase 6**: Prompt for git commit and push

---

## Phase 0: Load Session Context

Before executing any agents, load context from previous work sessions to provide continuity.

### Actions:

1. **Read session-close workflow** to understand the documentation structure:
   ```
   Read: .claude/commands/session-close.md
   ```

2. **Check for existing session documentation**:
   - If `session-work.md` exists in the repository root, read it
   - Extract previous session information:
     - Last session date
     - Files modified
     - Work completed
     - Decisions made

3. **Prepare session context** for agents:
   - Create a JSON structure with previous work context
   - This will be passed to agents via the `SESSION_CONTEXT` environment variable
   - Format:
     ```json
     {
       "previous_work": "content of session-work.md",
       "last_session_date": "ISO 8601 timestamp",
       "files_modified": ["list", "of", "files"]
     }
     ```

**Note:** If this is the first run, session context will be empty. This is expected behavior.

---

## Phase 1: Agent Execution Selection

**IMPORTANT:** Ask the user which agents to execute. This allows flexibility based on the nature of the commit.

### User Prompt:

Present the following options to the user:

```
Select OPSEC agent execution mode:

1. Full execution (Data Breach + Organization agents)
   - Runs both agents in parallel for comprehensive checks
   - Recommended for commits with new files or significant changes

2. Data Breach Detection only
   - Checks for proprietary/confidential information only
   - Faster for minor updates to known-safe content

3. Organization Sanitization only
   - Validates file naming and structure only
   - Good for reorganization work

4. Skip agents (proceed to pre-commit hooks)
   - Use when confident changes are compliant
   - Not recommended for first-time contributors

Enter choice (1-4):
```

### Store User Selection:
- Record the user's choice for Phase 2-3 execution
- If user provides invalid input, reprompt
- Default to option 1 (Full execution) if unclear

---

## Phase 2: Data Breach Detection Agent

**Condition:** Execute only if user selected options 1 or 2 in Phase 1.

### Execution:

1. **Prepare environment**:
   - Set `SESSION_CONTEXT` environment variable with context from Phase 0
   - Set `REPO_PATH` to current directory

2. **Run data breach agent**:
   ```bash
   SESSION_CONTEXT='<json_from_phase_0>' python3 scripts/data_breach_agent.py
   ```

3. **Monitor execution**:
   - Agent returns exit code 0 if no violations detected
   - Agent returns exit code 1 if violations found
   - Agent generates reports: `OPSEC_ALERT.md`, `RECOVERY_PLAN.md`, `POST_MORTEM.md`

4. **Handle violations** (if exit code 1):
   - Display summary of violations detected
   - Read and present `OPSEC_ALERT.md` to user
   - Ask user: "Violations detected. Options: (abort/continue/review)"
     - **abort**: Exit pipeline immediately
     - **continue**: Proceed with warning (log decision)
     - **review**: Display full OPSEC_ALERT.md and reprompt

**Parallel Execution Note:** If user selected option 1 (Full execution), Phase 2 and Phase 3 can run concurrently. Launch both agents and wait for both to complete before proceeding to Phase 4.

---

## Phase 3: Organization Sanitization Agent

**Condition:** Execute only if user selected options 1 or 3 in Phase 1.

### Execution:

1. **Prepare environment**:
   - Set `SESSION_CONTEXT` environment variable with context from Phase 0
   - Set `REPO_PATH` to current directory
   - Set `DRY_RUN=true` (always start with audit)

2. **Run organization agent in audit mode**:
   ```bash
   SESSION_CONTEXT='<json_from_phase_0>' python3 scripts/organization_sanitation_agent.py --mode=audit
   ```

3. **Monitor execution**:
   - Agent returns exit code 0 if repository compliant or fixes applied
   - Agent returns exit code 1 if issues found (dry-run mode)
   - Agent generates report: `ORGANIZATION_AUDIT_REPORT.md`

4. **Handle findings** (if exit code 1):
   - Display summary of issues found:
     - Directory structure issues
     - File naming violations
     - Content requiring redaction
     - File relocations recommended
   - Read and present relevant sections of `ORGANIZATION_AUDIT_REPORT.md`
   - Ask user: "Issues found. Apply automatic fixes? (yes/no/review)"
     - **yes**: Re-run agent with `--execute` flag to apply fixes
     - **no**: Continue pipeline with warnings
     - **review**: Display full report and reprompt

5. **Apply fixes if approved**:
   ```bash
   python3 scripts/organization_sanitation_agent.py --mode=audit --execute
   ```

**Parallel Execution Note:** If user selected option 1 (Full execution), run concurrently with Phase 2.

---

## Phase 4: Pre-Commit Hooks Validation

Run repository pre-commit hooks to catch any additional issues.

### Actions:

1. **Check if pre-commit is configured**:
   ```bash
   test -f .pre-commit-config.yaml && echo "configured" || echo "not configured"
   ```

2. **If configured, run hooks**:
   ```bash
   pre-commit run --all-files
   ```

3. **Handle hook failures**:
   - If hooks fail, display error messages
   - Ask user: "Pre-commit hooks failed. Options: (fix/skip/abort)"
     - **fix**: Give user time to fix issues, then re-run hooks
     - **skip**: Continue pipeline (not recommended, log decision)
     - **abort**: Exit pipeline

**Note:** Pre-commit hooks may auto-fix some issues. If files are modified, notify user and ask whether to review changes.

---

## Phase 5: Session Documentation

Execute the session-close workflow to document work completed in this session.

### Actions:

1. **Check git status** (run in parallel):
   ```bash
   git status
   git log --oneline -10
   git diff HEAD
   ```

2. **Review recent work**:
   - Examine the conversation history and changes made
   - Identify files created, modified, or deleted
   - Note any features added, bugs fixed, or refactoring completed

3. **Create/Update session-work.md**:
   - Document current session with structure:
     ```markdown
     # Session Work Summary

     **Date**: [Current timestamp]
     **Session**: OPSEC Policy Initiator Execution

     ## Work Completed

     ### Pipeline Execution
     - Agent mode selected: [Full/Data Breach/Organization/Skip]

     ### Security Checks
     - Data Breach Detection: [Passed/Failed/Skipped]
     - Organization Sanitization: [Passed/Failed/Skipped]

     ### Issues Detected
     [Summary of any violations or issues]

     ### Remediation Actions
     [Actions taken to address issues]

     ## Files Modified
     [List of files with changes]

     ## Technical Decisions
     - Agent execution mode: [rationale]
     - Issue remediation: [how issues were handled]

     ## Git Summary
     **Branch**: [current branch]
     **Files changed**: [count]
     **Ready for commit**: [yes/no]
     ```

4. **Stage session-work.md**:
   ```bash
   git add session-work.md
   ```

---

## Phase 6: Git Commit

Prompt user for approval before committing changes.

### Actions:

1. **Check if there are changes to commit**:
   ```bash
   git diff --cached --quiet && echo "no changes" || echo "has changes"
   ```

2. **If no changes**, skip to Phase 7.

3. **If changes exist, generate commit message**:
   - Analyze staged changes
   - Draft commit message following repository conventions:
     ```
     <type>(<scope>): <description>

     [Optional body explaining changes]

     Generated with Claude Code
     Co-Authored-By: Claude <noreply@anthropic.com>
     ```
   - Types: chore, feat, fix, docs, refactor, test
   - Scope: opsec, documentation, organization, security

4. **Present commit message to user**:
   ```
   📝 Proposed commit message:
   ----------------------------------------------------------------------
   chore(opsec): policy initiator execution - [date]

   - Executed data breach detection: [status]
   - Executed organization sanitization: [status]
   - Applied fixes: [summary]
   - Updated session documentation

   Generated with Claude Code
   Co-Authored-By: Claude <noreply@anthropic.com>
   ----------------------------------------------------------------------
   ```

5. **Prompt for commit approval**:
   ```
   ❓ Proceed with git commit? (yes/no/edit)
   ```
   - **yes**: Execute commit
   - **no**: Abort (changes remain staged)
   - **edit**: Allow user to modify commit message, then reprompt

6. **Execute commit**:
   ```bash
   git commit -m "$(cat <<'EOF'
   <commit_message_here>
   EOF
   )"
   ```

7. **Confirm commit**:
   - Display commit hash
   - Show commit summary

---

## Phase 7: Git Push

Prompt user for approval before pushing to remote.

### Actions:

1. **Check current branch**:
   ```bash
   git branch --show-current
   ```

2. **Check if remote is configured**:
   ```bash
   git remote -v
   ```

3. **If remote exists, prompt for push**:
   ```
   ❓ Push changes to remote? (yes/no)

   Current branch: [branch-name]
   Remote: [remote-url]
   ```
   - **yes**: Execute push
   - **no**: Exit (commit remains local)

4. **Execute push**:
   ```bash
   git push
   ```

5. **Confirm push**:
   - Display push result
   - Show remote branch status

6. **Final summary**:
   ```
   ✅ OPSEC Policy Initiator Complete

   Summary:
   - Agents executed: [list]
   - Issues detected: [count]
   - Fixes applied: [count]
   - Commit: [hash]
   - Push: [success/skipped]

   Session documented in: session-work.md
   ```

---

## Error Handling

Throughout the pipeline, handle errors gracefully:

1. **Agent Failures**:
   - Display error messages clearly
   - Offer options: abort, continue with warning, retry
   - Log all decisions in session-work.md

2. **Git Operation Failures**:
   - Display git error messages
   - Check for common issues (conflicts, authentication, etc.)
   - Provide remediation guidance

3. **User Interruption**:
   - If user aborts at any phase, document where pipeline stopped
   - Preserve all work completed so far
   - Provide resume instructions in session-work.md

---

## Parallel Execution Opportunities

The following operations can be executed in parallel for performance:

### Phase 0 - Session Context Loading:
```bash
# Read multiple files in parallel
cat .claude/commands/session-close.md &
cat session-work.md &  # if exists
wait
```

### Phase 2-3 - Agent Execution (if Full mode selected):
```bash
# Launch both agents concurrently
SESSION_CONTEXT='...' python3 scripts/data_breach_agent.py &
PID1=$!
SESSION_CONTEXT='...' python3 scripts/organization_sanitation_agent.py --mode=audit &
PID2=$!

# Wait for both to complete
wait $PID1
BREACH_EXIT=$?
wait $PID2
ORG_EXIT=$?

# Handle results from both
```

### Phase 5 - Git Status Checks:
```bash
# Parallel git operations
git status &
git log --oneline -10 &
git diff HEAD &
wait
```

---

## Notes

- **First-time execution**: If this is the first time running the policy initiator, some files (like session-work.md) may not exist. This is normal.

- **Automation mode**: For fully automated execution (CI/CD), set environment variable `POLICY_INITIATOR_AUTO=true` to skip all prompts and use defaults.

- **Audit trail**: All decisions, violations, and remediations are documented in session-work.md for compliance tracking.

- **Extensibility**: Additional agents can be added to Phase 2-3 by following the same pattern.

---

**Last Updated**: 2025-11-10
**Version**: 2.0.0
**Maintained By**: Ryno Crypto Services Security Team
