#!/usr/bin/env python3
"""Check that local resources referenced in index.html exist."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

pattern = re.compile(r'(?:src|href)="([^"]+)"')
content = INDEX.read_text()
missing = []

for match in pattern.finditer(content):
    url = match.group(1).strip()
    if url.startswith(("http://", "https://", "mailto:", "#", "javascript:")):
        continue
    url = url.split("#", 1)[0].split("?", 1)[0]
    path = ROOT / url.lstrip("/")
    if not path.exists():
        missing.append(url)

if missing:
    print("Missing resources:")
    for m in missing:
        print(f" - {m}")
    sys.exit(1)
else:
    print("All referenced local resources exist.")
