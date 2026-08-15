#!/usr/bin/env python3
"""
Part 3: Documentation Validation Checker

Automated system that runs against real claude.com/docs pages and validates them
against DOC-SKILL-001 style guide (Part 2).

This checker focuses on ONE class of problem: Missing or incomplete scaffolding
metadata tables (P1 violation from Part 1).

Usage:
    python docs_checker.py [url or file path]
    python docs_checker.py https://claude.com/docs/skills/how-to
    python docs_checker.py ./docs-scrape.md

Output:
    JSON report with violations, severity, and context.
"""

import re
import sys
import json
import argparse
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Tuple
from datetime import datetime


# ============================================================================
# Configuration
# ============================================================================

REQUIRED_FRONTMATTER_FIELDS = [
    "title",
    "description",
    "version",
    "package_name",
    "package_language",
    "tested_against",
]

REQUIRED_SCAFFOLDING_ROWS = [
    "Target Audience",
    "Time-to-Hello-World",
    "Prerequisites",
    "Tested Against",
    "Get Started",
]

IMPERATIVE_VERBS = {
    "initialize", "configure", "create", "deploy", "validate", "test",
    "extract", "build", "install", "set", "run", "execute", "add",
    "generate", "start", "enable", "check", "verify", "prepare"
}

CONDESCENDING_WORDS = [
    r"\bjust\b", r"\bsimply\b", r"\bobviously\b", r"\beasily\b",
    r"\bof course\b", r"\bclearly\b", r"\bbasically\b", r"\bmerely\b"
]


# ============================================================================
# Data Structures
# ============================================================================

@dataclass
class Violation:
    severity: str  # ERROR, WARNING, INFO
    line_number: int
    rule: str
    message: str
    context: Optional[str] = None
    suggestion: Optional[str] = None


@dataclass
class CheckResult:
    url: str
    title: str
    has_frontmatter: bool
    violations: List[Violation]
    checks_passed: int
    checks_failed: int
    timestamp: str


# ============================================================================
# Checkers
# ============================================================================

def extract_frontmatter(content: str) -> Tuple[Optional[str], str]:
    """Extract YAML frontmatter from markdown. Returns (frontmatter_str, body_str)."""
    if not content.startswith("---"):
        return None, content
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    
    return parts[1], parts[2]


def check_frontmatter_presence(content: str) -> Tuple[bool, str, Optional[Violation]]:
    """Check if frontmatter exists and contains required fields."""
    frontmatter, _ = extract_frontmatter(content)
    
    if not frontmatter:
        violation = Violation(
            severity="ERROR",
            line_number=1,
            rule="missing-frontmatter",
            message="Document must begin with YAML frontmatter (--- ... ---)",
            suggestion="Add YAML frontmatter with required fields: title, description, version, package_name, package_language, tested_against"
        )
        return False, "", violation
    
    # Parse frontmatter
    fields = {}
    for line in frontmatter.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    
    # Check required fields
    missing = [f for f in REQUIRED_FRONTMATTER_FIELDS if f not in fields]
    if missing:
        violation = Violation(
            severity="ERROR",
            line_number=1,
            rule="incomplete-frontmatter",
            message=f"Frontmatter missing required fields: {', '.join(missing)}",
            context=frontmatter[:200],
            suggestion=f"Add missing fields to frontmatter: {', '.join(missing)}"
        )
        return False, frontmatter, violation
    
    return True, frontmatter, None


def check_outcome_promise(content: str) -> Optional[Violation]:
    """Check for Outcome Promise blockquote."""
    if "**Outcome Promise:**" not in content:
        violation = Violation(
            severity="ERROR",
            line_number=5,  # Approximate
            rule="missing-outcome-promise",
            message="Document must include an Outcome Promise blockquote after the title",
            suggestion="Add: > **Outcome Promise:** By the end of this guide, you will [imperative verbs]."
        )
        return violation
    
    return None


def check_scaffolding_table(content: str) -> Optional[Violation]:
    """Check for scaffolding metadata table with all required rows."""
    # Look for markdown table pattern
    table_pattern = r"\|[^|]*\|[^|]*\|.*?\|"
    tables = re.findall(table_pattern, content, re.MULTILINE)
    
    if not tables:
        violation = Violation(
            severity="ERROR",
            line_number=10,  # Approximate
            rule="missing-scaffolding-table",
            message="Document must include a scaffolding metadata table with Target Audience, Time-to-Hello-World, Prerequisites, Tested Against, Get Started",
            context="No table found in document",
            suggestion="Add a 2-column table with the 5 required scaffolding rows after the Outcome Promise"
        )
        return violation
    
    # Check if all required rows are present in any table
    table_text = "\n".join(tables)
    missing_rows = [row for row in REQUIRED_SCAFFOLDING_ROWS if row not in table_text]
    
    if missing_rows:
        violation = Violation(
            severity="WARNING",
            line_number=10,
            rule="incomplete-scaffolding-table",
            message=f"Scaffolding table missing required rows: {', '.join(missing_rows)}",
            suggestion=f"Add missing rows to the scaffolding table: {', '.join(missing_rows)}"
        )
        return violation
    
    return None


def check_entry_point(content: str) -> Optional[Violation]:
    """Check for git clone or curl command in Get Started row."""
    if "git clone" not in content and "curl" not in content:
        violation = Violation(
            severity="WARNING",
            line_number=15,
            rule="missing-entry-point",
            message="Document should include a git clone or curl command for downloading the example package",
            context="No 'git clone' or 'curl' command found",
            suggestion="Add a git clone or curl command in the 'Get Started' row of the scaffolding table"
        )
        return violation
    
    return None


def check_code_blocks(lines: List[str]) -> List[Violation]:
    """Check code blocks for language tags and hardcoded secrets."""
    violations = []
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
                    violations.append(Violation(
                        severity="WARNING",
                        line_number=i,
                        rule="code-block-no-language",
                        message="Code block missing language identifier",
                        context=line[:80],
                        suggestion="Add language tag: ```python, ```bash, ```yaml, etc."
                    ))
            else:
                in_code_block = False
        
        if in_code_block and api_key_pattern.search(line):
            violations.append(Violation(
                severity="ERROR",
                line_number=i,
                rule="hardcoded-secret",
                message="Possible hardcoded API key or secret detected",
                context=line[:80],
                suggestion="Use environment variables: client = Anthropic()  # reads ANTHROPIC_API_KEY"
            ))
    
    return violations


def check_imperative_verbs(lines: List[str]) -> List[Violation]:
    """Check that procedural steps start with imperative verbs."""
    violations = []
    
    for i, line in enumerate(lines, start=1):
        # Match H2/H3 headings
        if re.match(r"^#{2,3}\s+", line):
            heading_text = re.sub(r"^#{2,3}\s+", "", line).strip()
            
            # Skip certain headings (Prerequisites, What you built, etc.)
            if any(skip in heading_text for skip in ["Prerequisites", "What you", "Next steps", "Best practices"]):
                continue
            
            # Extract first word
            first_word = heading_text.split()[0].lower() if heading_text else ""
            
            if first_word and first_word not in IMPERATIVE_VERBS and not first_word.startswith("how"):
                violations.append(Violation(
                    severity="INFO",
                    line_number=i,
                    rule="non-imperative-heading",
                    message=f"Heading '{heading_text}' should start with an imperative verb",
                    suggestion=f"Rephrase: 'Create/Configure/Validate [subject]' instead of '{heading_text}'"
                ))
    
    return violations


def check_condescending_language(lines: List[str]) -> List[Violation]:
    """Check for condescending language patterns."""
    violations = []
    pattern = re.compile("|".join(CONDESCENDING_WORDS), re.IGNORECASE)
    in_code_block = False
    
    for i, line in enumerate(lines, start=1):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
        
        if in_code_block:
            continue
        
        match = pattern.search(line)
        if match:
            violations.append(Violation(
                severity="INFO",
                line_number=i,
                rule="condescending-language",
                message=f"Avoid '{match.group()}' — it implies the task is trivial",
                context=line[:80],
                suggestion="Rewrite to be more professional and action-focused"
            ))
    
    return violations


# ============================================================================
# Main Validation Runner
# ============================================================================

def validate_document(content: str, url: str = "unknown") -> CheckResult:
    """Run all checks against a document."""
    violations = []
    checks_passed = 0
    checks_failed = 0
    
    lines = content.split("\n")
    
    # Check 1: Frontmatter presence
    has_frontmatter, frontmatter, violation = check_frontmatter_presence(content)
    if violation:
        violations.append(violation)
        checks_failed += 1
    else:
        checks_passed += 1
    
    # Extract title from frontmatter or markdown
    title = "Unknown"
    if has_frontmatter:
        fm_match = re.search(r"title:\s*(.+)", frontmatter)
        title = fm_match.group(1).strip() if fm_match else "Unknown"
    
    title_match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
    
    # Check 2: Outcome Promise
    violation = check_outcome_promise(content)
    if violation:
        violations.append(violation)
        checks_failed += 1
    else:
        checks_passed += 1
    
    # Check 3: Scaffolding table
    violation = check_scaffolding_table(content)
    if violation:
        violations.append(violation)
        checks_failed += 1
    else:
        checks_passed += 1
    
    # Check 4: Entry point (git clone / curl)
    violation = check_entry_point(content)
    if violation:
        violations.append(violation)
        checks_failed += 1
    else:
        checks_passed += 1
    
    # Check 5: Code blocks
    code_violations = check_code_blocks(lines)
    violations.extend(code_violations)
    if code_violations:
        checks_failed += len(code_violations)
    else:
        checks_passed += 1
    
    # Check 6: Imperative verbs in headings
    imperative_violations = check_imperative_verbs(lines)
    violations.extend(imperative_violations)
    checks_failed += len(imperative_violations)
    if not imperative_violations:
        checks_passed += 1
    
    # Check 7: Condescending language
    condescending_violations = check_condescending_language(lines)
    violations.extend(condescending_violations)
    checks_failed += len(condescending_violations)
    if not condescending_violations:
        checks_passed += 1
    
    return CheckResult(
        url=url,
        title=title,
        has_frontmatter=has_frontmatter,
        violations=violations,
        checks_passed=checks_passed,
        checks_failed=checks_failed,
        timestamp=datetime.now().isoformat()
    )


def print_report(result: CheckResult):
    """Print validation report in human-readable format."""
    print(f"\n{'=' * 70}")
    print(f"DOCUMENT: {result.title}")
    print(f"URL: {result.url}")
    print(f"{'=' * 70}\n")
    
    if not result.violations:
        print("✅ All checks passed!\n")
        return
    
    # Group violations by severity
    errors = [v for v in result.violations if v.severity == "ERROR"]
    warnings = [v for v in result.violations if v.severity == "WARNING"]
    info = [v for v in result.violations if v.severity == "INFO"]
    
    if errors:
        print(f"❌ ERRORS ({len(errors)})\n")
        for v in errors:
            print(f"  Line {v.line_number} ({v.rule})")
            print(f"    {v.message}")
            if v.context:
                print(f"    Context: {v.context[:60]}...")
            if v.suggestion:
                print(f"    → {v.suggestion}")
            print()
    
    if warnings:
        print(f"⚠️  WARNINGS ({len(warnings)})\n")
        for v in warnings:
            print(f"  Line {v.line_number} ({v.rule})")
            print(f"    {v.message}")
            if v.suggestion:
                print(f"    → {v.suggestion}")
            print()
    
    if info:
        print(f"ℹ️  INFO ({len(info)})\n")
        for v in info[:3]:  # Show only first 3 info messages
            print(f"  Line {v.line_number} ({v.rule})")
            print(f"    {v.message}")
            print()
    
    print(f"{'=' * 70}")
    print(f"SUMMARY: {result.checks_passed} passed, {result.checks_failed} failed")
    print(f"Timestamp: {result.timestamp}")
    print(f"{'=' * 70}\n")


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Validate documentation against DOC-SKILL-001 style guide"
    )
    parser.add_argument(
        "input",
        help="File path or URL to validate"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON instead of human-readable format"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail (exit 1) if any errors or warnings found"
    )
    
    args = parser.parse_args()
    
    # Read content
    if args.input.startswith("http"):
        print(f"Fetching {args.input}...")
        try:
            import urllib.request
            with urllib.request.urlopen(args.input) as response:
                content = response.read().decode('utf-8')
        except Exception as e:
            print(f"Error fetching URL: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        path = Path(args.input)
        if not path.exists():
            print(f"File not found: {args.input}", file=sys.stderr)
            sys.exit(1)
        with open(path) as f:
            content = f.read()
    
    # Validate
    result = validate_document(content, url=args.input)
    
    # Output
    if args.json:
        # Convert to JSON-serializable format
        report = {
            "url": result.url,
            "title": result.title,
            "has_frontmatter": result.has_frontmatter,
            "checks_passed": result.checks_passed,
            "checks_failed": result.checks_failed,
            "timestamp": result.timestamp,
            "violations": [
                {
                    "severity": v.severity,
                    "line_number": v.line_number,
                    "rule": v.rule,
                    "message": v.message,
                    "context": v.context,
                    "suggestion": v.suggestion,
                }
                for v in result.violations
            ]
        }
        print(json.dumps(report, indent=2))
    else:
        print_report(result)
    
    # Exit code
    if args.strict and result.violations:
        sys.exit(1)
    
    sys.exit(0 if not result.violations else 0)  # Always exit 0 for now


if __name__ == "__main__":
    main()
