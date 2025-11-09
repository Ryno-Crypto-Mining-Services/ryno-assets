# Active PRDs

**Status:** In Development & Implementation
**Last Updated:** 2025-11-09

---

## Purpose

This directory contains Product Requirements Documents (PRDs) for features, services, and products that are **actively being developed and implemented**. These PRDs represent approved projects with allocated resources and active development teams.

## Definition

**Active PRDs** are:
- Approved projects with assigned teams
- Features currently in development
- Products being actively built
- Projects with allocated budget and timeline
- Work items in progress toward delivery

## Entry Criteria

A PRD is placed in `/prd/active/` when:

- ✅ **Stakeholder approval obtained**
- ✅ **Budget and resources allocated**
- ✅ **Development team assigned**
- ✅ **Implementation timeline established**
- ✅ **Success metrics defined**
- ✅ **Technical architecture approved**
- ✅ Moved from `/prd/proposed/` after approval

## Exit Criteria

A PRD moves from **active** to **completed** when:

- ✅ All features and functionality implemented
- ✅ Testing and QA completed successfully
- ✅ Deployed to production environment
- ✅ Success metrics being tracked
- ✅ Documentation finalized
- ✅ Handoff to operations/support complete

## File Naming Convention

All files in this directory must follow the CLAUDE.md naming standards:

**Pattern:** `[org]-[product]-[category]-[title]-[version].md`

**Examples:**
```
ryno-crypto-prd-smart-contract-v1-0.md
ths-stack-prd-data-pipeline-v2-0.md
terrahash-mining-prd-cooling-system-v1-1.md
```

**Required Components:**
- Use **lowercase** only
- Replace spaces with **hyphens** (`-`)
- Include **semantic versioning** (`v1-0`, `v1-1`, `v2-0`)
- Increment version as scope changes during development
- Use `.md` extension for markdown files

## Document Structure

Active PRDs should include:

1. **Title and Version**
2. **Status:** "Active - In Development"
3. **Team and Timeline**
   - Product Owner
   - Development Team
   - Start Date
   - Target Completion Date
4. **Executive Summary**
   - Problem statement
   - Solution overview
   - Business value
5. **Detailed Requirements**
   - Functional requirements
   - Non-functional requirements
   - Acceptance criteria
6. **Technical Architecture**
   - System design overview
   - Integration points
   - Dependencies
7. **Success Metrics and KPIs**
   - Measurable outcomes
   - Performance targets
   - User adoption goals
8. **Development Timeline**
   - Milestones and phases
   - Sprint plans (if applicable)
   - Release schedule
9. **Risk Management**
   - Known risks and mitigations
   - Blockers and dependencies
   - Contingency plans
10. **Progress Tracking**
    - Current status
    - Completed work
    - Remaining tasks

## Development Process

**Active PRDs are managed through:**

1. **Sprint Planning** - Regular iteration planning
2. **Progress Updates** - Weekly or bi-weekly status updates
3. **Stakeholder Reviews** - Demo sessions and feedback
4. **Scope Management** - Change requests and approvals
5. **Quality Assurance** - Testing and validation throughout

**Update Frequency:** At minimum, update status every 2 weeks

## Status Labels

Use these status labels in PRD frontmatter:

- `Status: Active - Sprint 1` - Early development
- `Status: Active - Feature Complete` - Code complete, testing in progress
- `Status: Active - In QA` - Quality assurance phase
- `Status: Active - Pre-Launch` - Final preparations
- `Status: Active - Blocked` - Waiting on dependencies
- `Status: Active - On Hold` - Temporarily paused

## Version Management

**Version increments for active PRDs:**

- **Patch** (v1-0 → v1-1): Minor clarifications, no scope change
- **Minor** (v1-0 → v2-0): Scope adjustments, new requirements
- **Major** (v1-0 → v2-0 with significant changes): Major pivot or redesign

Always update version when making substantial changes to requirements.

## Examples

**What Belongs Here:**

- Features actively being coded
- Products in beta or alpha testing
- Services being deployed to production
- Improvements being rolled out incrementally
- Projects with active sprint cycles

**What Does NOT Belong Here:**

- Ideas not yet approved (keep in `/prd/proposed/`)
- Completed and shipped projects (move to `/prd/completed/`)
- Maintenance tasks (use issue tracking)
- Technical debt items (use `/docs/` or issue tracker)

## Best Practices

1. **Keep PRDs Current** - Update as scope or timeline changes
2. **Document Decisions** - Record key architectural and design decisions
3. **Track Blockers** - Maintain visibility on impediments
4. **Communicate Changes** - Notify stakeholders of significant updates
5. **Link to Work Items** - Reference related issues, tasks, or tickets
6. **Maintain Traceability** - Connect requirements to implementation

## Progress Reporting

Each active PRD should include:

- **Current Sprint/Phase**
- **Percent Complete** (estimate)
- **Upcoming Milestones**
- **Recent Accomplishments**
- **Blockers and Risks**
- **Next Steps**

## Collaboration

**Active development involves:**

- Product Owners - Requirements and prioritization
- Engineering Team - Implementation
- QA/Testing - Quality validation
- Design Team - UX/UI (if applicable)
- Stakeholders - Review and feedback

## Moving to Completion

When an active PRD is ready to move to completed:

1. **Verify all acceptance criteria met**
2. **Confirm production deployment**
3. **Update status to `Status: Completed - Live`**
4. **Move file from `/prd/active/` to `/prd/completed/`**
5. **Archive supporting documentation**
6. **Schedule post-launch review**
7. **Document lessons learned**

## Handling Changes

**If requirements change significantly:**

1. Evaluate impact on timeline and budget
2. Get stakeholder approval for scope change
3. Update PRD and increment version
4. Communicate changes to team
5. Adjust project plan accordingly

**If project is paused or cancelled:**

1. Update status to `Status: Active - On Hold` or `Status: Cancelled`
2. Document reason for pause/cancellation
3. Archive if cancelled, or keep in active/ if on hold
4. Communicate to all stakeholders

## Questions?

For questions about PRD standards or lifecycle management:

- Review: `/CONTRIBUTING.md`
- Standards: `/CLAUDE.md`
- Contact: Repository maintainers

---

**Directory Maintained By:** Ryno Crypto Services Product Team
**Review Frequency:** Weekly
**Last Audit:** 2025-11-09
