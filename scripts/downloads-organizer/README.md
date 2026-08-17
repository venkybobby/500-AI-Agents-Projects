# Downloads Organizer

A small, dependency-free Python script that organizes files in a folder
(e.g. `~/Downloads`) into subfolders based on keywords found in the file
name -- and, for plain text files, the first few KB of content.

Example: any file with "saro" in its name (`SARO_Report_Q1.pdf`,
`saro-notes.txt`, ...) is moved into a `SARO/` subfolder. Any file
mentioning "FDE interview" is moved into an `FDE Interview/` subfolder.

This runs locally on **your own machine** -- it has no access to any
remote server, so you need to download this script and run it yourself.

## Setup

1. Download `organize_downloads.py` and `rules.json` (keep them in the
   same folder).
2. Requires Python 3.7+, already installed on macOS/Linux. On Windows,
   install from [python.org](https://www.python.org/).

## Usage

Dry run first (default) -- shows what would happen without moving anything:

```bash
python3 organize_downloads.py
```

This scans `~/Downloads` by default. Point it elsewhere with `--source`:

```bash
python3 organize_downloads.py --source "/path/to/your/Downloads"
```

Once the plan looks right, actually move the files:

```bash
python3 organize_downloads.py --apply
```

Also bucket everything that didn't match a keyword rule into type-based
folders (Images, PDFs, Spreadsheets, ...):

```bash
python3 organize_downloads.py --apply --sort-remaining
```

## Customizing categories

Edit `rules.json` -- no code changes needed. Each rule is a destination
folder name plus a list of keywords to match (case-insensitive):

```json
{
  "folder": "SARO",
  "keywords": ["saro"]
}
```

Add as many rules as you like, e.g. for other projects, clients, or
document types. Rules are checked top to bottom; the first match wins.

The `extension_fallback` section (only used with `--sort-remaining`)
maps file extensions to type-based folder names for anything that
doesn't match a keyword rule.

## Safety notes

- Runs as a **dry run by default**. Nothing is moved until you pass `--apply`.
- Never overwrites an existing file -- if `SARO/report.pdf` already
  exists, the incoming file is renamed `report (1).pdf`.
- Only top-level files in the source folder are scanned; subfolders
  (including ones this script already created) are left alone, so it's
  safe to re-run repeatedly as new files arrive.
