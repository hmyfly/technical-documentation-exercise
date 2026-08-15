# Part 3: Documentation Linting Script

## Overview

`part3_doc_linter.py` is a Python script that performs automated quality checks on Markdown documentation files. It is designed to enforce a documentation style guide at the point of contribution, before human review.

The script checks for:

| Check | Severity | Description |
|---|---|---|
| Terminology | WARNING | Flags banned terms and suggests preferred replacements |
| Condescending language | WARNING | Flags "just," "simply," "obviously," etc. |
| Heading case | WARNING | Detects Title Case in headings; enforces sentence case |
| Heading levels | ERROR | Detects skipped heading levels (e.g., H2 → H4) |
| Code block language tags | WARNING | Flags code blocks without a language identifier |
| Hardcoded secrets | ERROR | Detects possible API keys in code blocks |
| Required sections | ERROR | Checks how-to guides for required sections (Prerequisites, Next steps) |
| Passive voice | INFO | Flags common passive voice constructions |

## Usage

```bash
# Lint all Markdown files in the current directory (recursive)
python3 part3_doc_linter.py

# Lint a specific directory
python3 part3_doc_linter.py path/to/docs/

# Lint a single file
python3 part3_doc_linter.py path/to/file.md
```

Exit codes:
- `0` — no errors (warnings may be present)
- `1` — one or more errors found

## Sample output

The following output was produced by running the linter against the documentation files in this repository:

```
Linting 3 Markdown file(s) in: /home/runner/work/technical-documentation-exercise/technical-documentation-exercise

============================================================
FILE: .../part1-memo.md
============================================================
  [WARNING] Line 1 (heading-case)
    Heading may use Title Case: "Memo: Improving API Documentation Quality...". Use sentence case.
    → Capitalise only the first word and proper nouns.
  [WARNING] Line 37 (terminology)
    Found "conversation history" — prefer "messages array".
    → Replace "conversation history" with "messages array".

  ... (additional warnings)

============================================================
FILE: .../part2-style-guide-template-beforeafter.md
============================================================
  [WARNING] Line 26 (condescending-language)
    Avoid "Simply" — it implies the task is trivial.
    → Remove the word or rephrase.
  [WARNING] Line 38 (terminology)
    Found "AI assistant" — prefer "assistant".
    → Replace "AI assistant" with "assistant".

  ... (additional warnings — note: the style guide intentionally
       lists banned terms in a comparison table; in a production
       linter, these lines would be exempt via a noqa-style comment)

============================================================
SUMMARY
============================================================
  Files scanned:        3
  Files with issues:    2
  Errors:               0
  Warnings:             27
  Info:                 0

⚠️   27 warning(s) to review.
```

**Interpretation:** The warnings on the Part 2 file are expected — the style guide uses a comparison table that deliberately contains the banned terms it is documenting. In production, individual lines can be suppressed with a `<!-- lint-disable -->` comment. No errors were found, meaning no hardcoded secrets, no skipped heading levels, and no missing required sections.

## Design decisions

**Rule severity tiers:** Errors block publishing (secrets, skipped headings, missing required sections). Warnings should be resolved before review but do not block CI. Info notices are suggestions only.

**No external dependencies:** The script uses only Python standard library modules. This makes it easy to add to any CI pipeline without a package install step.

**Extensibility:** New checks can be added as standalone functions that accept `(lines, report)` and call `report.add(...)`. The main runner calls each check in sequence.

**CI integration:** The script exits with code `1` if errors are found, making it suitable as a CI gate. Example GitHub Actions step:

```yaml
- name: Lint documentation
  run: python3 part3_doc_linter.py docs/
```
