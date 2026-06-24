#!/usr/bin/env python3
"""Static HTML checks for document-visualizer outputs."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


PLACEHOLDER_RE = re.compile(
    r"TODO|PLACEHOLDER|Lorem ipsum|模块标题|Replace with source-backed",
    re.I,
)


class _HTMLProbe(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: list[str] = []
        self.attrs: list[tuple[str, dict[str, str | None]]] = []
        self.title_text: list[str] = []
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.append(tag)
        self.attrs.append((tag, dict(attrs)))
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_text.append(data.strip())


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: html_check.py <file.html>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: not found: {path}", file=sys.stderr)
        return 2

    raw = path.read_text(encoding="utf-8", errors="ignore")
    parser = _HTMLProbe()
    parser.feed(raw)

    errors: list[str] = []
    warnings: list[str] = []

    if "html" not in parser.tags:
        errors.append("missing <html>")
    if "meta" not in parser.tags:
        warnings.append("no <meta> tags found")
    if "main" not in parser.tags:
        warnings.append("missing semantic <main>")
    if not "".join(parser.title_text).strip():
        warnings.append("empty <title>")

    if PLACEHOLDER_RE.search(raw):
        errors.append("placeholder text found")
    if re.search(r"debug|redline|screenshot-arrow", raw, re.I):
        warnings.append("debug-like marker found")
    if re.search(r"来源|类型|风格|范围|生成方式", raw) and "meta" in raw.lower():
        warnings.append("possible visible meta/source block; confirm user requested it")
    if re.search(r"letter-spacing\s*:\s*-[0-9.]+", raw):
        errors.append("negative letter-spacing found")
    if re.search(r"width\s*:\s*(?:10[9-9][0-9]|[2-9][0-9]{3,})px", raw):
        warnings.append("fixed width above 1080px found")

    for tag, attrs in parser.attrs:
        if tag == "img" and not attrs.get("alt"):
            warnings.append("image without alt text")
            break

    for msg in errors:
        print(f"ERROR: {msg}")
    for msg in warnings:
        print(f"WARN: {msg}")

    if errors:
        return 1
    print(f"OK: {path} ({len(parser.tags)} tag(s), {len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
