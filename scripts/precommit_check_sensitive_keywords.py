#!/usr/bin/env python3
import re
import sys
from pathlib import Path

SENSITIVE_KEYWORDS = [
    r"ai[_\-]?model",
    r"ml[_\-]?agent",
    r"proprietary",
    r"confidential",
    r"treasury",
    r"hedge",
    r"financials?",
    r"revenue",
    r"pricing",
    r"customer[_\-]?data",
    r"margin",
    r"noc[_\-]?platform",
    r"predictive",
    r"portfolio",
    r"contract",
    r"secret",
    r"private",
    r"partnership",
    r"chilldyne",
    r"braiins",
    r"exclusive",
    r"5mw",
    r"industrial",
]

KEYWORD_PATTERN = re.compile("|".join(SENSITIVE_KEYWORDS), re.IGNORECASE)


def scan_file_content(filepath):
    try:
        with open(filepath, errors="ignore") as f:
            for i, line in enumerate(f, 1):
                if KEYWORD_PATTERN.search(line):
                    print(f"Sensitive content keyword found in {filepath}:{i}: {line.strip()}")
                    return True
    except Exception:
        pass  # binary or unreadable files
    return False


def main():
    failed = False
    for filepath in sys.argv[1:]:
        # check filename
        if KEYWORD_PATTERN.search(Path(filepath).name):
            print(f"Sensitive keyword found in filename: {filepath}")
            failed = True
        # check content
        if scan_file_content(filepath):
            failed = True
    if failed:
        print("✖ Commit blocked: Remove or relocate sensitive/proprietary files.")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
