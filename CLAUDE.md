# CLAUDE.md

## AI Agent Instructions & Repository Configuration

**Last Updated:** 2025-11-07
**Repository:** Ryno Crypto Services & TerraHash Stack Technical Documentation
**Version:** 2.0.0

---

## Table of Contents

1. [Purpose & Scope](#purpose--scope)
2. [File Naming Conventions](#file-naming-conventions)
3. [Repository Structure](#repository-structure)
4. [Documentation Standards](#documentation-standards)
5. [Pre-Commit Hook Requirements](#pre-commit-hook-requirements)
6. [Contribution Guidelines](#contribution-guidelines)
7. [Code & Content Standards](#code--content-standards)
8. [AI Agent Workflow](#ai-agent-workflow)
9. [License & Legal](#license--legal)

---

## Purpose & Scope

This repository contains technical documentation, product requirements documents (PRDs), architecture diagrams, and media assets for **Ryno Crypto Services** and the **TerraHash Stack** platform. This CLAUDE.md file provides comprehensive guidelines for both human contributors and AI coding assistants (Claude, Copilot, Cursor, Gemini, Cline, etc.) to maintain consistency, quality, and compliance across all repository contributions.

### Repository Contents

- Technical specifications and architecture documents
- Product Requirements Documents (PRDs)
- API documentation and integration guides
- Media assets (images, diagrams, videos)
- Service documentation and operational guides
- Research papers and whitepapers

---

## File Naming Conventions

All files in this repository **MUST** follow these standardized naming conventions to ensure consistency, discoverability, and automated processing.

### General Rules

**Universal Requirements:**

- Use **lowercase letters only**
- Replace spaces with **hyphens** (`-`)
- Limit filenames to **50 characters** (excluding extension)
- Use **semantic versioning** format: `v[major]-[minor]-[patch]` (e.g., `v1-0-0`, `v2-1-3`)
- Include dates in **ISO 8601 format**: `YYYY-MM-DD` or `YYYYMMDD`
- Avoid special characters: `* & % $ @ ! # ? ( ) [ ] { } ' " ; : < > | \ / ~`
- Use **descriptive, meaningful names** that convey content without opening the file
- Always include proper file extension

### Image Files

**Pattern:** `[org]-[product]-[descriptor]-[type]-[resolution]-[version].[format]`

**Components:**

- `[org]`: Organization identifier (e.g., `ryno`, `ths`, `terrahash`)
- `[product]`: Product/service name (e.g., `crypto`, `stack`, `mining`)
- `[descriptor]`: Content description (e.g., `smart-dip-buying`, `system-architecture`, `comparison-matrix`)
- `[type]`: Image type (e.g., `banner`, `logo`, `hero`, `icon`, `infographic`, `diagram`, `thumbnail`, `screenshot`)
- `[resolution]`: Width x height (e.g., `1920x1080`, `800x600`, `original`)
- `[version]`: Semantic version (e.g., `v1-0`, `v1-1`, `v2-0`)
- `[format]`: File format (e.g., `png`, `jpg`, `svg`, `webp`, `gif`)

**Examples:**

```
ryno-crypto-dip-buying-banner-1920x1080-v1-0.png
ths-stack-architecture-diagram-2560x1440-v2-1.svg
terrahash-mining-process-infographic-original-v1-0.jpg
ryno-crypto-logo-icon-512x512-v1-0.png
```

**Optional Components:**

- `[license]`: Add if multiple licenses in use (e.g., `-cc`, `-mit`, `-proprietary`)
- `[date]`: Add for time-sensitive content (e.g., `-20251107`)

### Document Files

**Pattern:** `[org]-[product]-[category]-[title]-[version].[format]`

**Components:**

- `[org]`: Organization identifier (e.g., `ryno`, `ths`, `terrahash`)
- `[product]`: Product/service name (e.g., `crypto`, `stack`, `mining`)
- `[category]`: Document category (e.g., `prd`, `specs`, `api-docs`, `guide`, `whitepaper`, `service`, `architecture`, `security`)
- `[title]`: Descriptive title using hyphens (e.g., `smart-contract-implementation`, `user-authentication`, `data-pipeline`)
- `[version]`: Semantic version (e.g., `v1-0`, `v1-1`, `v2-0`)
- `[format]`: File format (e.g., `pdf`, `md`, `docx`, `txt`)

**Examples:**

```
ryno-crypto-prd-smart-contract-v1-0.pdf
ths-stack-specs-data-pipeline-v2-1.md
terrahash-mining-guide-getting-started-v1-0.pdf
ryno-crypto-api-docs-authentication-v3-0.md
ths-stack-whitepaper-consensus-mechanism-v1-0.pdf
```

### Markdown Files

**Pattern:** `[category]-[title]-[date-optional].[format]`

**Examples:**

```
prd-token-economics.md
specs-api-gateway.md
guide-deployment-procedures.md
security-audit-report-20251107.md
meeting-notes-architecture-review-20251107.md
```

### Source Code Files

**Follow language-specific conventions:**

- **Python**: `snake_case.py` (e.g., `data_processor.py`, `api_client.py`)
- **JavaScript/TypeScript**: `kebab-case.js` or `camelCase.js` (e.g., `data-processor.js`, `api-client.ts`)
- **Java/C#**: `PascalCase.java` (e.g., `DataProcessor.java`, `ApiClient.cs`)
- **General**: Use lowercase with hyphens or underscores consistently

### Configuration Files

**Standard names (do not modify):**

```
.gitignore
.pre-commit-config.yaml
package.json
requirements.txt
Dockerfile
docker-compose.yml
```

### Data Files

**Pattern:** `[category]-[descriptor]-[date]-[version].[format]`

**Examples:**

```
dataset-user-analytics-20251107-v1-0.csv
export-transaction-history-20251107-v1-0.json
backup-database-snapshot-20251107.sql
```

---

## Repository Structure

The repository follows a standardized directory structure for optimal organization and discoverability.

### Root Directory Layout

```
.
├── README.md                      # Project overview and quick start guide
├── CLAUDE.md                      # This file - AI agent instructions
├── CONTRIBUTING.md                # Contribution guidelines and workflows
├── LICENSE                        # Repository license terms
├── SECURITY.md                    # Security policies and reporting
├── CHANGELOG.md                   # Version history and release notes
├── .gitignore                     # Git ignore patterns
├── .pre-commit-config.yaml        # Pre-commit hook configuration
├── docs/                          # Documentation files
├── assets/                        # Media and static assets
├── prd/                          # Product Requirements Documents
├── specs/                        # Technical specifications
├── examples/                     # Usage examples and templates
├── scripts/                      # Utility scripts and automation
├── tests/                        # Test files and test data
└── archive/                      # Deprecated or archived content
```

### Directory Descriptions

#### `/docs/` - Documentation

Organized by topic with subdirectories:

```
docs/
├── architecture/                  # System architecture documents
├── api/                          # API documentation
├── guides/                       # User and developer guides
├── security/                     # Security documentation
├── operations/                   # Operational procedures
└── research/                     # Research papers and analysis
```

#### `/assets/` - Media Assets

Organized by type and product:

```
assets/
├── images/
│   ├── ryno-crypto/              # Ryno Crypto images
│   ├── terrahash-stack/          # TerraHash Stack images
│   └── shared/                   # Shared assets
├── diagrams/
│   ├── architecture/             # Architecture diagrams
│   ├── flowcharts/              # Process flowcharts
│   └── infographics/            # Infographic assets
├── videos/                       # Video assets
└── templates/                    # Design templates
```

#### `/prd/` - Product Requirements Documents

```
prd/
├── active/                       # Current PRDs
├── proposed/                     # Proposed features
└── completed/                    # Implemented PRDs
```

#### `/specs/` - Technical Specifications

```
specs/
├── api/                         # API specifications
├── database/                    # Database schemas
├── integration/                 # Integration specifications
└── protocols/                   # Protocol definitions
```

#### `/examples/` - Usage Examples

```
examples/
├── api-usage/                   # API usage examples
├── integration/                 # Integration examples
└── templates/                   # Document templates
```

#### `/scripts/` - Utility Scripts

```
scripts/
├── validation/                  # Validation scripts
├── deployment/                  # Deployment scripts
├── data-processing/             # Data processing utilities
└── automation/                  # Automation scripts
```

---

## Documentation Standards

### README.md Requirements

The **root README.md** must include:

1. **Project title and description**
2. **Table of contents** (for documents > 200 lines)
3. **Quick start guide**
4. **Repository structure overview**
5. **Contribution guidelines** (or link to CONTRIBUTING.md)
6. **License information**
7. **Contact information**
8. **Links to key documentation**

### Markdown Style Guide

**Formatting:**

- Use `#` for H1, `##` for H2, `###` for H3 (never skip levels)
- Use **bold** for emphasis on key terms
- Use *italics* for definitions or secondary emphasis
- Use `code blocks` for file names, commands, and code snippets
- Use bulleted lists for unordered items
- Use numbered lists for sequential steps
- Include code block language identifiers for syntax highlighting

**Structure:**

- Start documents with a title (`#`)
- Include a brief summary paragraph
- Use clear hierarchical headings
- Add a table of contents for long documents (> 500 words)
- End with references, citations, or related links

**Writing Style:**

- Use active voice
- Write in present tense
- Be concise and clear
- Define technical terms on first use
- Use consistent terminology throughout
- Include examples where helpful

### Technical Documentation Requirements

**All technical documents must include:**

1. **Version number and date**
2. **Author/maintainer information**
3. **Purpose and scope**
4. **Prerequisites or dependencies**
5. **Detailed content with examples**
6. **References and related documents**
7. **Changelog section** (for versioned documents)

### ISO 15489 Compliance

This repository follows **ISO 15489** records management principles:

- **Authenticity**: Documents are genuine and created by identified authors
- **Reliability**: Content is trustworthy and complete
- **Integrity**: Documents are protected from unauthorized alteration
- **Useability**: Documents are findable, retrievable, and understandable

**Metadata Requirements:**

Each significant document should include:

- Title
- Author(s)
- Creation date
- Last modified date
- Version number
- Keywords/tags
- Related documents
- License/copyright

---

## Pre-Commit Hook Requirements

This repository uses **pre-commit hooks** to automatically validate and fix common issues before commits. All contributors must install and use these hooks.

### Installation

```bash
# Install pre-commit
pip install pre-commit

# Install hooks from .pre-commit-config.yaml
pre-commit install

# Run hooks manually on all files
pre-commit run --all-files
```

### Automated Validations

The pre-commit hooks will automatically:

1. **File naming validation:**
   - Convert uppercase letters to lowercase
   - Replace spaces with hyphens
   - Remove invalid special characters
   - Verify file extensions match content
   - Enforce naming convention patterns

2. **Content validation:**
   - Check for syntax errors (JSON, YAML, Markdown)
   - Validate no merge conflict markers
   - Check for trailing whitespace
   - Ensure files end with newline
   - Validate no private keys or secrets

3. **Code quality:**
   - Run linters (language-specific)
   - Format code (prettier, black, etc.)
   - Check import sorting
   - Validate no debug statements

4. **File size and type:**
   - Prevent commits of large files (> 5MB)
   - Warn on binary files
   - Check for forbidden file types

### Pre-Commit Configuration

The `.pre-commit-config.yaml` includes:

```yaml
repos:
  # File validation
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: check-added-large-files
        args: ['--maxkb=5120']
      - id: check-case-conflict
      - id: check-merge-conflict
      - id: check-yaml
      - id: check-json
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: mixed-line-ending
      - id: detect-private-key

  # Filename validation (custom)
  - repo: local
    hooks:
      - id: validate-filename
        name: Validate Filename Convention
        entry: scripts/validate-filenames.py
        language: python
        pass_filenames: true

  # Markdown linting
  - repo: https://github.com/markdownlint/markdownlint
    rev: v0.12.0
    hooks:
      - id: markdownlint

  # Remove forbidden patterns
  - repo: local
    hooks:
      - id: check-spaces-in-filenames
        name: No spaces in filenames
        entry: 'Filename contains spaces'
        language: pygrep
        files: '.*\s.*'
```

### Custom Filename Validation Script

Location: `scripts/validate-filenames.py`

This script enforces repository-specific naming conventions for images and documents.

---

## Contribution Guidelines

### Before Contributing

1. **Read the CONTRIBUTING.md** file thoroughly
2. **Install pre-commit hooks** (`pre-commit install`)
3. **Review existing documentation** to understand patterns
4. **Check for related issues** or PRs to avoid duplication
5. **Familiarize yourself with file naming conventions**

### Contribution Workflow

1. **Fork or clone** the repository
2. **Create a feature branch** from `main`:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** following all guidelines in this document
4. **Run pre-commit hooks**:

   ```bash
   pre-commit run --all-files
   ```

5. **Write clear commit messages**:
   - Use imperative mood ("Add feature" not "Added feature")
   - Limit first line to 50 characters
   - Add detailed description if needed
   - Reference issues (`Closes #123`, `Fixes #456`)
6. **Push to your branch** and **create a pull request**
7. **Respond to review feedback** promptly

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes (no code change)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Example:**

```
feat(prd): add smart contract PRD for token economics

- Added comprehensive PRD for token economics implementation
- Included technical specifications and acceptance criteria
- Added diagrams for token flow and distribution

Closes #234
```

### Pull Request Guidelines

**PR Title Format:** `<type>: <description>`

**PR Description Must Include:**

- Summary of changes
- Motivation and context
- Related issue numbers
- Type of change (feature, bug fix, documentation)
- Checklist:
  - [ ] Pre-commit hooks pass
  - [ ] Documentation updated
  - [ ] Files follow naming conventions
  - [ ] No sensitive information included
  - [ ] LICENSE terms accepted

### Review Process

1. **Automated checks** must pass (pre-commit hooks, CI/CD)
2. **Human review** by at least one maintainer
3. **AI-assisted review** for code quality and documentation
4. **Address feedback** and update PR
5. **Maintainer approval** required before merge
6. **Squash and merge** to maintain clean history

---

## Code & Content Standards

### Documentation Quality

**All documentation must be:**

- **Accurate**: Factually correct and up-to-date
- **Complete**: Covers all necessary information
- **Clear**: Easy to understand for target audience
- **Concise**: No unnecessary verbosity
- **Consistent**: Follows established patterns
- **Accessible**: Properly formatted for readability

### Technical Accuracy

- **Verify all technical details** before committing
- **Include version numbers** for software, APIs, protocols
- **Date-stamp time-sensitive information**
- **Cite sources** for external information
- **Include examples** that actually work

### Sensitive Information

**NEVER commit:**

- API keys, tokens, or credentials
- Private keys or certificates
- Passwords or secrets
- Personal identifiable information (PII)
- Proprietary information from third parties
- Internal IP addresses or server names

**Instead:**

- Use environment variables
- Reference secrets management systems
- Use placeholders in examples
- Document where to obtain credentials

### License Compliance

- All contributions are subject to repository LICENSE
- Do not include code with incompatible licenses
- Properly attribute third-party content
- Include license headers where required

---

## AI Agent Workflow

This section provides specific guidance for AI coding assistants (Claude, Copilot, Cursor, Gemini, Cline, etc.).

### Context and Awareness

When working in this repository, AI agents should:

1. **Always read this CLAUDE.md** file first for current guidelines
2. **Check README.md** for project-specific context
3. **Review existing files** in the target directory for patterns
4. **Verify file naming conventions** before creating new files
5. **Understand the repository structure** to place files correctly

### File Creation Guidelines

**When creating new files:**

1. **Determine appropriate directory** based on file type and purpose
2. **Follow naming convention** exactly as specified
3. **Include required metadata** (title, author, date, version)
4. **Use existing files as templates** when possible
5. **Add references** to related documentation
6. **Update README.md** if adding new directory or significant content

### Code Generation

**When generating code or scripts:**

1. **Follow language-specific conventions**
2. **Include comprehensive docstrings/comments**
3. **Add error handling and validation**
4. **Provide usage examples**
5. **Consider security implications**
6. **Test before committing** (if possible)

### Documentation Generation

**When creating or updating documentation:**

1. **Use clear, professional language**
2. **Include table of contents** for long documents
3. **Add diagrams or examples** where helpful
4. **Cross-reference related documents**
5. **Follow markdown style guide**
6. **Include version and date information**

### Quality Checks

**Before suggesting commits, AI agents should verify:**

- [ ] Filename follows naming convention
- [ ] File is in correct directory
- [ ] No sensitive information included
- [ ] Markdown is properly formatted
- [ ] Links are valid (if applicable)
- [ ] Code is syntactically valid (if applicable)
- [ ] No spelling or grammar errors
- [ ] Consistent with repository patterns

### Prohibited Actions

**AI agents must NOT:**

- Create files with spaces in names
- Use uppercase in filenames (except README, LICENSE, etc.)
- Include sensitive information or secrets
- Violate naming conventions
- Create unnecessarily complex structures
- Ignore repository standards
- Make assumptions about undocumented patterns

### Recommended Actions

**AI agents should proactively:**

- Suggest improvements to documentation
- Identify inconsistencies in existing files
- Recommend better organization when appropriate
- Flag potential security issues
- Offer to create missing documentation
- Help maintain consistency across repository

### Error Handling

**If uncertain about guidelines:**

1. **Ask for clarification** rather than making assumptions
2. **Reference specific sections** of this document
3. **Provide options** with trade-offs explained
4. **Suggest creating an issue** for ambiguous cases
5. **Default to conservative approach** (don't break things)

### Continuous Improvement

**AI agents should:**

- Learn from repository patterns over time
- Adapt to project-specific conventions
- Suggest updates to this CLAUDE.md when appropriate
- Help identify and fix inconsistencies
- Contribute to documentation quality

---

## License & Legal

### Contributor License Agreement (CLA)

By contributing to this repository, you agree to the following terms:

1. **Ownership**: You retain copyright to your contributions
2. **License Grant**: You grant Ryno Crypto Services and TerraHash Stack project a perpetual, irrevocable, worldwide, royalty-free license to use, modify, and distribute your contributions
3. **Originality**: You affirm that contributions are your original work or you have rights to submit them
4. **No Infringement**: Your contributions do not infringe on any third-party rights
5. **Compliance**: Your contributions comply with all applicable laws and regulations

### Content Licensing

**Unless otherwise specified:**

- **Technical Documents & PRDs**: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- **Media Assets**: CC BY 4.0 (unless marked otherwise)
- **Source Code**: See LICENSE file in repository root

### Proprietary Content

- Some modules may have separate proprietary licenses
- Check individual directories for `LICENSE` files
- Respect all license restrictions
- Do not submit proprietary content without authorization

### Attribution

- Contributors will be credited in commit history
- Significant contributions may be acknowledged in README.md
- Media asset creators should be attributed per CC BY 4.0
- Use CONTRIBUTORS.md for formal attribution list

### Warranty and Liability

**ALL CONTENT PROVIDED "AS IS":**

- No warranty of accuracy, completeness, or suitability
- Contributors not liable for damages from use of content
- Use at your own risk
- Verify all information independently

### Security and Responsible Disclosure

- Report security issues privately to: <security@rynocrypto.com>
- Do not publicly disclose vulnerabilities before patching
- Follow responsible disclosure practices
- See SECURITY.md for detailed policy

---

## Questions and Support

**For questions about:**

- **General guidelines**: Review this CLAUDE.md and CONTRIBUTING.md
- **Technical issues**: Open an issue on GitHub
- **Security concerns**: Email <security@rynocrypto.com>
- **Legal/licensing**: Email <legal@rynocrypto.com>
- **Contributions**: Contact repository maintainers

**Maintainers:**

- Monitored via GitHub issues and pull requests
- Response time: 1-3 business days
- For urgent matters: Contact directly via provided emails

---

## Document Version History

| Version | Date       | Changes                                      | Author          |
|---------|------------|----------------------------------------------|-----------------|
| 2.0.0   | 2025-11-07 | Major revision with comprehensive guidelines | AI Assistant    |
| 1.0.0   | 2025-11-07 | Initial CLAUDE.md creation                  | Original Author |

---

**Thank you for contributing to Ryno Crypto Services and TerraHash Stack!** 🚀

By following these guidelines, you help maintain a high-quality, well-organized repository that benefits all contributors and users.

---

*This document is maintained in accordance with ISO 15489 records management standards and follows industry best practices for repository organization, file naming conventions, and documentation quality.*
