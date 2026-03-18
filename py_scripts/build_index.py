"""
build_index.py

Walks all prompt (.md) and conversation (.qmd) files, extracts YAML
frontmatter, and writes a search-index.json to the repo root.

Usage:
    cd /path/to/my-ai-assistant
    python py_scripts/build_index.py

Output:
    search-index.json  — array of records, one per file, with frontmatter
                         fields plus a "file" path relative to repo root.
"""

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter from a markdown/qmd file as a dict."""
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}

    fm_text = match.group(1)
    result = {}

    # Parse simple key: value pairs (handles strings, numbers, null)
    # and block-sequence lists (tags: \n  - item)
    lines = fm_text.splitlines()
    current_key = None
    current_list = None

    for line in lines:
        # Block sequence item
        if current_list is not None and re.match(r"^  - (.+)", line):
            current_list.append(re.match(r"^  - (.+)", line).group(1).strip())
            continue

        # New top-level key
        kv = re.match(r"^(\w[\w-]*):\s*(.*)", line)
        if kv:
            if current_list is not None:
                result[current_key] = current_list
                current_list = None

            key, val = kv.group(1), kv.group(2).strip()

            if val == "" or val == "~":
                # Could be start of block sequence or null
                current_key = key
                current_list = []
            elif val.lower() == "null" or val == "[]":
                result[key] = []
                current_key = None
            elif val.startswith("[") and val.endswith("]"):
                # Inline sequence
                items = [i.strip().strip("'\"") for i in val[1:-1].split(",") if i.strip()]
                result[key] = items
                current_key = None
            else:
                result[key] = val.strip("'\"")
                current_key = None
        else:
            # Non-matching line ends any open list
            if current_list is not None:
                result[current_key] = current_list
                current_list = None
            current_key = None

    if current_list is not None:
        result[current_key] = current_list

    return result


def build_index():
    records = []

    globs = [
        ("prompts", "**/*.md"),
        ("conversations", "**/*.qmd"),
    ]

    for folder, pattern in globs:
        base = REPO_ROOT / folder
        for path in sorted(base.rglob(pattern.replace("**/", ""))):
            # Skip listing index pages themselves
            if path.name == "index.qmd":
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except Exception:
                continue

            fm = parse_frontmatter(text)
            if not fm:
                continue

            record = {
                "file": str(path.relative_to(REPO_ROOT)),
                "type": "prompt" if folder == "prompts" else "conversation",
                **fm,
            }
            records.append(record)

    out_path = REPO_ROOT / "search-index.json"
    out_path.write_text(json.dumps(records, indent=2, default=str), encoding="utf-8")
    print(f"Wrote {len(records)} records to {out_path}")


if __name__ == "__main__":
    build_index()
