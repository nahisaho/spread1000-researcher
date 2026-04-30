#!/usr/bin/env python3
"""Validate Evidence Dossier structure and required fields.

Usage: python validate_dossier.py <path-to-evidence-dossier.md>
"""

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "Identity",
    "Publications",
    "Funding",
    "Innovation Signals",
    "International Activity",
    "Interdisciplinary Impact",
    "Career Stage",
    "Sources",
]

CONFIDENCE_PATTERN = re.compile(r"evidence_confidence:\s*(high|medium|low)", re.IGNORECASE)
URL_PATTERN = re.compile(r"https?://\S+")


def validate(path: str) -> list[str]:
    text = Path(path).read_text(encoding="utf-8")
    errors: list[str] = []

    # Check required sections
    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in text:
            errors.append(f"Missing required section: ## {section}")

    # Check confidence levels in each section
    sections_with_confidence = REQUIRED_SECTIONS[1:7]  # Publications through Career Stage
    for section in sections_with_confidence:
        pattern = re.compile(
            rf"## {re.escape(section)}(.*?)(?=## |\Z)", re.DOTALL
        )
        match = pattern.search(text)
        if match and not CONFIDENCE_PATTERN.search(match.group(1)):
            errors.append(f"Section '{section}' missing evidence_confidence field")

    # Check Sources section has URLs
    sources_match = re.search(r"## Sources(.*?)(?=## |\Z)", text, re.DOTALL)
    if sources_match and not URL_PATTERN.search(sources_match.group(1)):
        errors.append("Sources section contains no URLs")

    return errors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <evidence-dossier.md>")
        sys.exit(2)

    errors = validate(sys.argv[1])
    if errors:
        print(f"FAIL — {len(errors)} issue(s):")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        print("PASS — Evidence Dossier is structurally valid.")
        sys.exit(0)
