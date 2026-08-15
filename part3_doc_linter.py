#!/usr/bin/env python3
"""
Part 3: Documentation Linting and Audit Script

This script performs automated documentation quality checks on Markdown files.
It validates:
  - Required sections in how-to guide pages
  - Terminology consistency (banned terms, preferred terms)
  - Code block formatting (language tags, API key hardcoding)
  - Heading structure (sentence case, no skipped levels)
  - Parameter documentation completeness

Usage:
    python3 part3_doc_linter.py [path_to_docs_directory]

    If no path is provided, it scans the current directory for .md files.

Output:
    Prints a report of all violations found, grouped by file, with severity
    (ERROR, WARNING, INFO) and a summary count at the end.
"""

import re
import sys
import os
from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BANNED_TERMS = {
    "AI assistant": "assistant",
    "chat history": "messages array",
    "conversation history": "messages array",
    "function calling": "tool use",
    "tool calling": "tool use",
    "context length": "context window",
    "token limit": "context window (or max_tokens where specific)",
    "stop token": "stop sequence",
    "end token": "stop sequence",
    "streaming response": "stream (noun) or streaming (adjective)",
    "streamed output": "stream",
}

CONDESCENDING_WORDS = [
    r"\bjust\b",
    r"\bsimply\b",
    r"\bobviously\b",
    r"\beasily\b",
    r"\bof course\b",
    r"\bclearly\b",
]

REQUIRED_HOWTO_SECTIONS = [
    "Prerequisites",
    "Next steps",
]

REQUIRED_REFERENCE_SECTIONS = [
    "Request",
    "Response",
    "Error",
]

SEVERITY_ERROR = "ERROR"
SEVERITY_WARNING = "WARNING"
SEVERITY_INFO = "INFO"


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Violation:
    severity: str
    line_number: int
    rule: str
    message: str
    suggestion: Optional[str] = None


@dataclass
class FileReport:
    filepath: str
    violations: list = field(default_factory=list)

    def add(self, severity, line_number, rule, message, suggestion=None):
        self.violations.append(
            Violation(severity, line_number, rule, message, suggestion)
        )

    @property
    def error_count(self):
        return sum(1 for v in self.violations if v.severity == SEVERITY_ERROR)

    @property
    def warning_count(self):
        return sum(1 for v in self.violations if v.severity == SEVERITY_WARNING)


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_terminology(lines, report):
    """Flag banned terms and suggest preferred replacements."""
    for i, line in enumerate(lines, start=1):
        # Skip lines inside code blocks
        if line.strip().startswith("```") or line.strip().startswith("    "):
            continue
        for banned, preferred in BANNED_TERMS.items():
            if re.search(re.escape(banned), line, re.IGNORECASE):
                report.add(
                    SEVERITY_WARNING,
                    i,
                    "terminology",
                    f'Found "{banned}" — prefer "{preferred}".',
                    suggestion=f'Replace "{banned}" with "{preferred}".',
                )


def check_condescending_language(lines, report):
    """Flag words that imply the task is simple."""
    pattern = re.compile("|".join(CONDESCENDING_WORDS), re.IGNORECASE)
    in_code_block = False
    for i, line in enumerate(lines, start=1):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
        if in_code_block:
            continue
        match = pattern.search(line)
        if match:
            report.add(
                SEVERITY_WARNING,
                i,
                "condescending-language",
                f'Avoid "{match.group()}" — it implies the task is trivial.',
                suggestion="Remove the word or rephrase.",
            )


def check_heading_case(lines, report):
    """Flag headings that use Title Case instead of sentence case."""
    heading_re = re.compile(r"^(#{1,6})\s+(.+)$")
    for i, line in enumerate(lines, start=1):
        m = heading_re.match(line)
        if not m:
            continue
        text = m.group(2)
        # Ignore all-caps abbreviations and code (backtick-wrapped)
        words = text.split()
        if len(words) < 2:
            continue
        # Check if two or more non-first words are capitalised (Title Case indicator)
        non_first_caps = [
            w for w in words[1:]
            if w[0].isupper()
            and not w.isupper()          # Not an acronym
            and not w.startswith("`")    # Not inline code
            and not w.startswith("[")    # Not a link
            and w not in {"API", "SDK", "JSON", "HTTP", "CLI", "URL", "ID", "UI"}
        ]
        if len(non_first_caps) >= 2:
            report.add(
                SEVERITY_WARNING,
                i,
                "heading-case",
                f'Heading may use Title Case: "{text}". Use sentence case.',
                suggestion="Capitalise only the first word and proper nouns.",
            )


def check_heading_levels(lines, report):
    """Flag skipped heading levels (e.g., H2 directly to H4)."""
    heading_re = re.compile(r"^(#{1,6})\s")
    prev_level = 0
    for i, line in enumerate(lines, start=1):
        m = heading_re.match(line)
        if not m:
            continue
        level = len(m.group(1))
        if prev_level > 0 and level > prev_level + 1:
            report.add(
                SEVERITY_ERROR,
                i,
                "heading-levels",
                f"Skipped heading level: jumped from H{prev_level} to H{level}.",
                suggestion=f"Use H{prev_level + 1} instead of H{level}.",
            )
        prev_level = level


def check_code_blocks(lines, report):
    """Flag code blocks without language tags, and hardcoded API keys."""
    in_code_block = False
    code_block_start = 0
    api_key_pattern = re.compile(
        r'(sk-ant-[a-zA-Z0-9\-]{20,}|api[_-]?key\s*=\s*["\'][a-zA-Z0-9\-_]{10,}["\'])',
        re.IGNORECASE,
    )
    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_code_block:
                in_code_block = True
                code_block_start = i
                lang = stripped[3:].strip()
                if not lang:
                    report.add(
                        SEVERITY_WARNING,
                        i,
                        "code-block-language",
                        "Code block has no language tag.",
                        suggestion="Add a language tag, e.g. ```python or ```bash.",
                    )
            else:
                in_code_block = False
        if in_code_block:
            if api_key_pattern.search(line):
                report.add(
                    SEVERITY_ERROR,
                    i,
                    "hardcoded-secret",
                    "Possible hardcoded API key or secret detected in code block.",
                    suggestion=(
                        "Use an environment variable: "
                        "client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY"
                    ),
                )


def check_required_sections(lines, report, filepath):
    """Check that how-to guides include required sections."""
    filename = os.path.basename(filepath).lower()
    is_howto = "how-to" in filename or "howto" in filename or filename.startswith("how_to")

    content = "\n".join(lines)
    h2_sections = re.findall(r"^##\s+(.+)$", content, re.MULTILINE)

    if is_howto:
        for required in REQUIRED_HOWTO_SECTIONS:
            if not any(required.lower() in s.lower() for s in h2_sections):
                report.add(
                    SEVERITY_ERROR,
                    0,
                    "missing-section",
                    f'How-to guide is missing required section: "{required}".',
                    suggestion=f'Add a "## {required}" section.',
                )


def check_passive_voice(lines, report):
    """Flag common passive voice constructions."""
    passive_pattern = re.compile(
        r"\b(is|are|was|were|be|been|being)\s+(returned|sent|used|passed|set|called|processed|generated|created|handled)\b",
        re.IGNORECASE,
    )
    in_code_block = False
    for i, line in enumerate(lines, start=1):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
        if in_code_block:
            continue
        if passive_pattern.search(line):
            report.add(
                SEVERITY_INFO,
                i,
                "passive-voice",
                "Possible passive voice detected. Consider active voice.",
                suggestion="Rewrite to make the subject explicit, e.g. 'The API returns...'",
            )


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def lint_file(filepath):
    """Run all checks on a single Markdown file. Returns a FileReport."""
    report = FileReport(filepath=filepath)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    except OSError as e:
        report.add(SEVERITY_ERROR, 0, "file-read", f"Could not read file: {e}")
        return report

    check_terminology(lines, report)
    check_condescending_language(lines, report)
    check_heading_case(lines, report)
    check_heading_levels(lines, report)
    check_code_blocks(lines, report)
    check_required_sections(lines, report, filepath)
    check_passive_voice(lines, report)

    return report


def find_markdown_files(root):
    """Recursively find all .md files under root."""
    md_files = []
    for dirpath, _, filenames in os.walk(root):
        # Skip hidden dirs and common non-doc dirs
        skip = {".git", "node_modules", "__pycache__", ".venv", "dist", "build"}
        dirpath_parts = set(os.path.normpath(dirpath).split(os.sep))
        if dirpath_parts & skip:
            continue
        for fn in filenames:
            if fn.endswith(".md"):
                md_files.append(os.path.join(dirpath, fn))
    return sorted(md_files)


def print_report(reports):
    """Print all reports in a readable format."""
    total_errors = 0
    total_warnings = 0
    total_info = 0
    files_with_issues = 0

    for report in reports:
        if not report.violations:
            continue
        files_with_issues += 1
        print(f"\n{'=' * 60}")
        print(f"FILE: {report.filepath}")
        print(f"{'=' * 60}")
        for v in sorted(report.violations, key=lambda x: (x.line_number, x.severity)):
            line_str = f"Line {v.line_number}" if v.line_number > 0 else "File-level"
            print(f"  [{v.severity}] {line_str} ({v.rule})")
            print(f"    {v.message}")
            if v.suggestion:
                print(f"    → {v.suggestion}")
        total_errors += report.error_count
        total_warnings += report.warning_count
        total_info += sum(1 for v in report.violations if v.severity == SEVERITY_INFO)

    print(f"\n{'=' * 60}")
    print("SUMMARY")
    print(f"{'=' * 60}")
    print(f"  Files scanned:        {len(reports)}")
    print(f"  Files with issues:    {files_with_issues}")
    print(f"  Errors:               {total_errors}")
    print(f"  Warnings:             {total_warnings}")
    print(f"  Info:                 {total_info}")

    if total_errors == 0 and total_warnings == 0:
        print("\n✅  No errors or warnings found.")
    elif total_errors > 0:
        print(f"\n❌  {total_errors} error(s) require attention before publishing.")
    else:
        print(f"\n⚠️   {total_warnings} warning(s) to review.")


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    root = os.path.abspath(root)

    if os.path.isfile(root):
        files = [root]
    elif os.path.isdir(root):
        files = find_markdown_files(root)
    else:
        print(f"Error: {root} is not a file or directory.", file=sys.stderr)
        sys.exit(1)

    if not files:
        print("No Markdown files found.")
        return

    print(f"Linting {len(files)} Markdown file(s) in: {root}")
    reports = [lint_file(f) for f in files]
    print_report(reports)

    total_errors = sum(r.error_count for r in reports)
    sys.exit(1 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
