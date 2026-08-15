# Technical Documentation Exercise — Anthropic Submission

This repository contains my submission for the Anthropic Technical Documentation and Content Engineer take-home exercise.

## Contents

| File | Part | Description |
|---|---|---|
| [`part1-memo.md`](part1-memo.md) | Part 1 | Memo: documentation strategy recommendations |
| [`part2-style-guide-template-beforeafter.md`](part2-style-guide-template-beforeafter.md) | Part 2 | Style guide excerpt, how-to guide content template, and before/after page revision |
| [`part3_doc_linter.py`](part3_doc_linter.py) | Part 3 | Python documentation linting script |
| [`part3-doc-linter-readme.md`](part3-doc-linter-readme.md) | Part 3 | Linter usage, design notes, and sample output |
| [`part4-reflections.md`](part4-reflections.md) | Part 4 | Reflections on documentation practice |

## Quick start (Part 3)

```bash
# Run the linter on all Markdown files in this repo
python3 part3_doc_linter.py .

# Run on a specific file
python3 part3_doc_linter.py part1-memo.md
```

No external dependencies. Requires Python 3.8+.