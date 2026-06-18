#!/usr/bin/env python3
"""Basic SVG sanity checks for document-visualizer outputs."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def _num(value: str | None) -> float | None:
    if not value:
        return None
    match = re.match(r"^\s*([0-9]+(?:\.[0-9]+)?)", value)
    return float(match.group(1)) if match else None


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: svg_check.py <file.svg>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: not found: {path}", file=sys.stderr)
        return 2

    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        print(f"ERROR: invalid XML: {exc}", file=sys.stderr)
        return 1

    tag = root.tag.split("}")[-1]
    if tag != "svg":
        print("ERROR: root element is not <svg>", file=sys.stderr)
        return 1

    width = _num(root.get("width"))
    height = _num(root.get("height"))
    view_box = root.get("viewBox")
    errors: list[str] = []
    warnings: list[str] = []

    if width is None or height is None:
        errors.append("missing numeric width or height")
    elif width < 300 or height < 300:
        warnings.append(f"canvas may be too small: {width:g}x{height:g}")

    if not view_box:
        errors.append("missing viewBox")

    texts = [el for el in root.iter() if el.tag.split("}")[-1] == "text"]
    if not texts:
        warnings.append("no editable <text> elements found")

    tiny_text_count = 0
    empty_text_count = 0
    for el in texts:
        content = "".join(el.itertext()).strip()
        if not content:
            empty_text_count += 1
        size = _num(el.get("font-size"))
        style = el.get("style") or ""
        if size is None:
            match = re.search(r"font-size\s*:\s*([0-9.]+)", style)
            size = float(match.group(1)) if match else None
        if size is not None and size < 12:
            tiny_text_count += 1

    if empty_text_count:
        warnings.append(f"{empty_text_count} empty text element(s)")
    if tiny_text_count:
        warnings.append(f"{tiny_text_count} text element(s) below 12px")

    raw = path.read_text(encoding="utf-8", errors="ignore")
    if re.search(r"TODO|PLACEHOLDER|Lorem ipsum", raw, re.I):
        warnings.append("placeholder-like text found")

    for msg in errors:
        print(f"ERROR: {msg}")
    for msg in warnings:
        print(f"WARN: {msg}")

    if errors:
        return 1
    print(f"OK: {path} ({len(texts)} text element(s), {len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
