# Technical Documentation Exercise

A full docs quality system:

**Audit → Standard → Checker → Adoption**

This project shows how to find doc problems, set a clear standard, check docs with code, and help teams adopt the system.

---

## What is in this repo

| File | Part | Purpose |
|---|---|---|
| [`part1-memo.md`](part1-memo.md) | Part 1 | Audit of key doc problems (P0, P1, P2) |
| [`part2-style-guide-template-beforeafter.md`](part2-style-guide-template-beforeafter.md) | Part 2 | Doc standard + template + before/after example |
| [`part3_docs_checker.py`](part3_docs_checker.py) | Part 3 | Python checker for docs quality rules |
| [`part3-README.md`](part3-README.md) | Part 3 | How checker works, tests, and CI use |
| [`part4-adoption.md`](part4-adoption.md) | Part 4 | Plan to help teams adopt the system |

---

## Quick start

```bash
git clone https://github.com/hmyfly/technical-documentation-exercise
cd technical-documentation-exercise

# Run checker on a markdown file
python3 part3_docs_checker.py part2-style-guide-template-beforeafter.md

# JSON output
python3 part3_docs_checker.py part2-style-guide-template-beforeafter.md --json

# Fail with exit code 1 if violations exist
python3 part3_docs_checker.py part2-style-guide-template-beforeafter.md --strict
```

Requires **Python 3.8+**. No external packages.

---

## The 4 parts

## Part 1: Audit

Found 3 common docs problems:

- **P0: Broken frontmatter** → tools cannot parse files
- **P1: Missing execution contract** → readers do not know what they will build
- **P2: Fragmented snippets** → users copy random code and guess setup

## Part 2: Standard (DOC-SKILL-001)

Defines what a good how-to guide must include:

- Required frontmatter fields
- Outcome Promise (what user gets by the end)
- Scaffolding table (audience, time, prereqs, versions, entry point)
- Clear step-by-step commands

## Part 3: Checker

`part3_docs_checker.py` checks markdown files for 7 rule groups:

1. Frontmatter exists and has required fields
2. Outcome Promise is present
3. Scaffolding table has all 5 rows
4. Entry command exists (`git clone` or `curl`)
5. Code blocks have language tags and no hardcoded secrets
6. Step headings use action verbs
7. No condescending language

## Part 4: Adoption

A practical rollout plan without formal authority:

1. Show real issues with evidence
2. Keep adoption easy (one command, one template)
3. Start with early adopters
4. Find blockers in teams that ignore it
5. Track outcomes, not just compliance

---

## Why this works

- Connects problem, standard, enforcement, and rollout
- Uses real tests, not only theory
- Keeps rules clear and checkable
- Focuses on value, not mandates

---

## Known limits

- Checker can over-flag reference docs
- Python-only checker today
- CI example is GitHub Actions only

---

## Next steps

1. Add doc type detection (for example: how-to vs reference)
2. Run checker on 100+ docs and tune false positives
3. Add CI gates for ERROR-level issues
4. Build a quality metrics dashboard
5. Pilot with one team and measure impact

---

## Repo status

- Checker code: ~400 lines
- Docs: ~3,500 words across all parts
- Real test runs: 2
- Last updated: **August 16, 2026**
- Status: **Ready for review**
