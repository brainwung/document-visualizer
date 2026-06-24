#!/usr/bin/env python3
"""Dependency-free package checks for the document-visualizer skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "RULES.md",
    "CATALOG.md",
    "agents/openai.yaml",
    "assets/html/base.html",
    "scripts/html_check.py",
    "scripts/svg_check.py",
    "scripts/skill_check.py",
    "templates/minimalist/design.md",
    "templates/minimalist-dark/design.md",
    "templates/soft-blocks/design.md",
]


def _frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    if not text.startswith("---\n"):
        return {}, ["SKILL.md must start with YAML frontmatter"]
    end = text.find("\n---", 4)
    if end == -1:
        return {}, ["SKILL.md frontmatter is not closed"]

    data: dict[str, str] = {}
    errors: list[str] = []
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        key, value = match.groups()
        data[key] = value.strip().strip('"').strip("'")
    return data, errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            errors.append(f"missing required file: {rel}")

    skill_path = root / "SKILL.md"
    if skill_path.exists():
        data, fm_errors = _frontmatter(skill_path.read_text(encoding="utf-8"))
        errors.extend(fm_errors)
        keys = set(data)
        if "name" not in data:
            errors.append("frontmatter missing name")
        if "description" not in data:
            errors.append("frontmatter missing description")
        extra = keys - {"name", "description"}
        if extra:
            errors.append(f"frontmatter contains unsupported keys: {', '.join(sorted(extra))}")
        if data.get("name") != "document-visualizer":
            errors.append("frontmatter name must be document-visualizer")
        description = data.get("description", "")
        if len(description) < 80:
            warnings.append("description may be too short to trigger reliably")
        if len(description) > 700:
            warnings.append("description is long; keep trigger boundary concise")
        body = skill_path.read_text(encoding="utf-8")
        for rel in ["RULES.md", "CATALOG.md", "assets/html/base.html", "scripts/html_check.py", "scripts/skill_check.py"]:
            if rel not in body:
                warnings.append(f"SKILL.md does not reference {rel}")

    for msg in errors:
        print(f"ERROR: {msg}")
    for msg in warnings:
        print(f"WARN: {msg}")

    if errors:
        return 1
    print(f"OK: {root} ({len(REQUIRED_FILES)} required file(s), {len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
