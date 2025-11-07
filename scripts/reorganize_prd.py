#!/usr/bin/env python3
"""
Script to reorganize PRD files from old structure to new structure
"""

import os
import shutil
import re
from pathlib import Path

# Mapping of old directory names to new directory names
dir_mapping = {
    "1 Market Problem Statement & Economic Drivers": "market-problem",
    "2 TerraHash Stack Retrofitting Service Goals and O": "service-goals",
    "3 Client User Personas Overview": "user-personas",
    "4 Detailed Retrofit Use Cases": "use-cases",
    "5 Key Features & System Modules": "features-modules",
    "6 Success Metrics & KPI Framework": "success-metrics",
    "7 Market Assumptions & Risk Framework": "market-assumptions",
    "8 Product Development & Rollout Timeline": "development-timeline",
    "9 Stakeholder Map & Engagement Framework": "stakeholder-map",
    "10 Known Constraints & Dependencies": "constraints",
    "11 Open Questions & Research Priorities": "research-priorities",
    "12 Comprehensive Risk Analysis & Mitigation Framew": "risk-analysis",
}

def fix_filename(filename):
    """Fix filename format (e.g., v1.0 -> v1-0, underscores to hyphens)"""
    # Replace v1.0 with v1-0
    filename = re.sub(r'v(\d+)\.(\d+)', r'v\1-\2', filename)
    # Replace underscores with hyphens
    filename = filename.replace('_', '-')
    return filename

def main():
    base_dir = Path("/Users/elvis/Documents/Git/RynoCrypto/ryno-assets")
    old_prd_base = base_dir / "docs/prd/terrahash-retrofitting/Product Requirements Document TerraHash Stack as a"
    new_prd_base = base_dir / "prd/active/terrahash-retrofitting"

    # Process each directory
    for old_dir_name, new_dir_name in dir_mapping.items():
        old_dir = old_prd_base / old_dir_name
        new_dir = new_prd_base / new_dir_name

        if not old_dir.exists():
            print(f"Warning: {old_dir} does not exist")
            continue

        # Find all .md files in this directory
        md_files = list(old_dir.glob("*.md"))

        for md_file in md_files:
            new_filename = fix_filename(md_file.name)
            new_path = new_dir / new_filename

            print(f"Copying: {md_file.name} -> {new_dir_name}/{new_filename}")
            shutil.copy2(md_file, new_path)

    # Copy root-level md files
    root_md_files = list(old_prd_base.glob("*.md"))
    for md_file in root_md_files:
        new_filename = fix_filename(md_file.name)
        new_path = new_prd_base / new_filename
        print(f"Copying root: {md_file.name} -> {new_filename}")
        shutil.copy2(md_file, new_path)

    print("\nPRD reorganization complete!")

if __name__ == "__main__":
    main()
