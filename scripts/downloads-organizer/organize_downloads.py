#!/usr/bin/env python3
"""
Organize files in a folder (e.g. Downloads) into subfolders based on
keyword matches in the file name -- and, for plain-text files, the
first few KB of content.

Usage:
    python3 organize_downloads.py                      # dry run on ~/Downloads
    python3 organize_downloads.py --apply               # actually move files
    python3 organize_downloads.py --source ~/Downloads --apply
    python3 organize_downloads.py --rules my_rules.json --apply
    python3 organize_downloads.py --apply --sort-remaining   # also bucket
                                                              # unmatched files
                                                              # by file type

By default this is a DRY RUN: it prints what it *would* do without
touching any files. Pass --apply to actually move files.

Rules live in rules.json next to this script and can be edited freely
without touching the code -- add a folder name and a list of keywords.
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

CONTENT_SNIFF_EXTENSIONS = {".txt", ".md", ".csv", ".log"}
CONTENT_SNIFF_BYTES = 8192


def load_rules(rules_path: Path):
    with open(rules_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    rules = [(r["folder"], [kw.lower() for kw in r["keywords"]]) for r in data.get("rules", [])]
    extension_fallback = {
        folder: {ext.lower().lstrip(".") for ext in exts}
        for folder, exts in data.get("extension_fallback", {}).items()
        if not folder.startswith("_")
    }
    return rules, extension_fallback


def sniff_content(path: Path) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read(CONTENT_SNIFF_BYTES).lower()
    except OSError:
        return ""


def match_folder(path: Path, rules):
    haystack = path.name.lower()
    if path.suffix.lower() in CONTENT_SNIFF_EXTENSIONS:
        haystack += "\n" + sniff_content(path)

    for folder, keywords in rules:
        if any(kw in haystack for kw in keywords):
            return folder
    return None


def match_extension_fallback(path: Path, extension_fallback):
    ext = path.suffix.lower().lstrip(".")
    for folder, exts in extension_fallback.items():
        if ext in exts:
            return folder
    return None


def unique_destination(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem, suffix, parent = dest.stem, dest.suffix, dest.parent
    counter = 1
    while True:
        candidate = parent / f"{stem} ({counter}){suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def organize(source: Path, rules, extension_fallback, apply: bool, sort_remaining: bool):
    if not source.is_dir():
        print(f"Source folder does not exist: {source}", file=sys.stderr)
        sys.exit(1)

    moved, skipped, unmatched = 0, 0, 0

    for path in sorted(source.iterdir()):
        if path.is_dir() or path.name.startswith("."):
            continue

        folder = match_folder(path, rules)
        if folder is None and sort_remaining:
            folder = match_extension_fallback(path, extension_fallback)

        if folder is None:
            unmatched += 1
            continue

        dest_dir = source / folder
        dest_path = unique_destination(dest_dir / path.name)

        action = "Would move" if not apply else "Moving"
        print(f"{action}: {path.name}  ->  {folder}/{dest_path.name}")

        if apply:
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(path), str(dest_path))
            moved += 1
        else:
            moved += 1

    skipped = 0  # reserved for future skip-logic (e.g. locked files)

    print()
    if apply:
        print(f"Done. Moved {moved} file(s). {unmatched} file(s) left unmatched.")
    else:
        print(f"Dry run complete. {moved} file(s) would be moved. "
              f"{unmatched} file(s) would be left unmatched.")
        print("Re-run with --apply to actually move the files.")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", default=str(Path.home() / "Downloads"),
                         help="Folder to organize (default: ~/Downloads)")
    parser.add_argument("--rules", default=str(Path(__file__).parent / "rules.json"),
                         help="Path to rules.json (default: rules.json next to this script)")
    parser.add_argument("--apply", action="store_true",
                         help="Actually move files. Without this flag, runs as a dry run.")
    parser.add_argument("--sort-remaining", action="store_true",
                         help="Also bucket files that don't match any keyword rule into "
                              "type-based folders (Images, PDFs, etc.) using extension_fallback.")
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    rules_path = Path(args.rules).expanduser().resolve()

    if not rules_path.is_file():
        print(f"Rules file not found: {rules_path}", file=sys.stderr)
        sys.exit(1)

    rules, extension_fallback = load_rules(rules_path)
    organize(source, rules, extension_fallback, apply=args.apply, sort_remaining=args.sort_remaining)


if __name__ == "__main__":
    main()
