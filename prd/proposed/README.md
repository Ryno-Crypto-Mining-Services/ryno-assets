# Proposed PRDs

**Status:** Ideas & Planning Stage
**Last Updated:** 2025-11-09

---

## Purpose

This directory contains Product Requirements Documents (PRDs) for features, services, and products that are in the **ideation and planning phase**. These PRDs represent concepts under consideration that have not yet been approved for active development.

## Definition

**Proposed PRDs** are:
- Ideas and concepts in early exploration
- Features being researched and evaluated
- Products undergoing feasibility analysis
- Projects awaiting stakeholder approval
- Drafts in active review and iteration

## Entry Criteria

A PRD is placed in `/prd/proposed/` when:

- ✅ Initial concept has been documented
- ✅ Problem statement is clearly defined
- ✅ High-level goals and objectives are outlined
- ✅ Basic market or user need is identified
- ⚠️ **NOT yet approved for development**
- ⚠️ **NOT yet funded or resourced**

## Exit Criteria

A PRD moves from **proposed** to **active** when:

- ✅ Stakeholder approval obtained
- ✅ Budget and resources allocated
- ✅ Development team assigned
- ✅ Implementation timeline established
- ✅ Success metrics defined and agreed upon
- ✅ Technical feasibility confirmed

## File Naming Convention

All files in this directory must follow the CLAUDE.md naming standards:

**Pattern:** `[org]-[product]-[category]-[title]-[version].md`

**Examples:**
```
ryno-crypto-prd-smart-contract-v1-0.md
ths-stack-prd-data-pipeline-v1-0.md
terrahash-mining-prd-cooling-system-v1-0.md
```

**Required Components:**
- Use **lowercase** only
- Replace spaces with **hyphens** (`-`)
- Include **semantic versioning** (`v1-0`, `v1-1`, `v2-0`)
- Use `.md` extension for markdown files

## Document Structure

Proposed PRDs should include:

1. **Title and Version**
2. **Status:** "Proposed - Under Review"
3. **Author and Date**
4. **Executive Summary**
   - Problem statement
   - Proposed solution overview
   - Key value proposition
5. **Market Context**
   - User needs or market gap
   - Competitive landscape (if known)
6. **High-Level Goals**
   - What success looks like
   - Measurable outcomes (if defined)
7. **Open Questions**
   - Unknowns requiring research
   - Technical feasibility concerns
   - Resource requirements
8. **Next Steps**
   - Actions needed for approval
   - Stakeholders to consult
   - Research tasks

## Review Process

**Proposed PRDs undergo:**

1. **Initial Draft Review** - Internal team review for clarity
2. **Stakeholder Feedback** - Input from relevant parties
3. **Feasibility Assessment** - Technical and resource evaluation
4. **Approval Decision** - Move to active, revise, or reject

**Timeline:** Typically 2-8 weeks depending on complexity

## Status Labels

Use these status labels in PRD frontmatter:

- `Status: Proposed - Draft` - Initial documentation
- `Status: Proposed - In Review` - Under stakeholder review
- `Status: Proposed - Revision Needed` - Requires updates
- `Status: Proposed - Approved` - Ready to move to active
- `Status: Proposed - Rejected` - Not moving forward

## Examples

**What Belongs Here:**

- New product ideas being explored
- Feature proposals awaiting approval
- Research-driven product concepts
- Strategic initiatives under consideration
- Experimental projects requiring validation

**What Does NOT Belong Here:**

- Approved projects (move to `/prd/active/`)
- Completed projects (move to `/prd/completed/`)
- Technical specifications (use `/specs/`)
- Meeting notes or brainstorming docs (use `/docs/`)

## Best Practices

1. **Keep PRDs Concise** - Focus on core concept, not implementation details
2. **Update Regularly** - Document new learnings and decisions
3. **Version Control** - Increment version on significant changes
4. **Cross-Reference** - Link to related research, specs, or documents
5. **Set Timelines** - Include expected review/decision dates
6. **Identify Owners** - Assign champion or sponsor for each PRD

## Moving Forward

When a proposed PRD is approved:

1. Update status to `Status: Active - In Development`
2. Move file from `/prd/proposed/` to `/prd/active/`
3. Update version if significant changes made during approval
4. Assign development team and timeline
5. Add to project tracking system

## Questions?

For questions about PRD standards or lifecycle management:

- Review: `/CONTRIBUTING.md`
- Standards: `/CLAUDE.md`
- Contact: Repository maintainers

---

**Directory Maintained By:** Ryno Crypto Services Product Team
**Review Frequency:** Monthly
**Last Audit:** 2025-11-09
