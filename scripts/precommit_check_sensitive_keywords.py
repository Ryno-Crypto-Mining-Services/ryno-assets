#!/usr/bin/env python3
import re
import sys
from pathlib import Path

# Refined keywords - removed overly broad terms for a crypto mining business
SENSITIVE_KEYWORDS = [
    r"\bai[_\-]?model\b",  # AI model references
    r"\bml[_\-]?agent\b",  # ML agent references
    r"\bconfidential\b",  # Marked confidential
    r"\btreasury[_\-]algorithm\b",  # Specific treasury algorithms (not general treasury mgmt)
    r"\bhedge[_\-]strategy\b",  # Specific hedge strategies (not general hedging)
    r"\bcustomer[_\-]?data\b",  # Customer PII/data
    r"\bnoc[_\-]?platform\b",  # NOC platform specifics
    r"\bpredictive[_\-]algorithm\b",  # Specific predictive algorithms
    r"\bportfolio[_\-]strategy\b",  # Specific portfolio strategies
    r"\bsecret[_\-]?key\b",  # Actual secret keys (not general "secret")
    r"\bprivate[_\-]?key\b",  # Private keys (not general "private")
    r"\bexclusive[_\-]partnership\b",  # Exclusive partnership agreements
    r"\binternal[_\-]?only\b",  # Internal only docs
    r"\bdo[_\-]?not[_\-]?share\b",  # Explicit restriction
    r"\bproduction[_\-]?credentials\b",  # Production credentials
]

KEYWORD_PATTERN = re.compile("|".join(SENSITIVE_KEYWORDS), re.IGNORECASE)

# Text file extensions to scan
TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".rst",
    ".yaml",
    ".yml",
    ".json",
    ".toml",
    ".py",
    ".js",
    ".ts",
    ".sh",
    ".bash",
    ".zsh",
    ".html",
    ".css",
    ".scss",
    ".xml",
    ".env",
    ".conf",
    ".cfg",
    ".ini",
}


def should_scan_file(filepath):
    """Only scan known text file extensions."""
    path = Path(filepath)
    return path.suffix.lower() in TEXT_EXTENSIONS


def scan_file_content(filepath):
    """Scan text file content for sensitive keywords."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="strict") as f:
            for i, line in enumerate(f, 1):
                if KEYWORD_PATTERN.search(line):
                    preview = line.strip()[:100]
                    print(
                        f"Sensitive content keyword found in {filepath}:{i}: {preview}"
                    )
                    return True
    except (UnicodeDecodeError, IOError):
        # Skip files that can't be read as text
        return False
    return False


def main():
    failed = False

    for filepath in sys.argv[1:]:
        # Only scan files with text extensions
        if not should_scan_file(filepath):
            continue

        # Check filename
        filename = Path(filepath).name
        if KEYWORD_PATTERN.search(filename):
            print(f"Sensitive keyword found in filename: {filepath}")
            failed = True
            continue

        # Check file content
        if scan_file_content(filepath):
            failed = True

    if failed:
        print("✖ Commit blocked: Remove or relocate sensitive/proprietary files.")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
