# Part 1: Systems Audit & Architecture
## From Publishing Information to Designing Task Completion

---

## Executive Summary

The main problem with these docs is simple: they explain features, but they do not help people finish tasks.

Good docs should do two things well:
- Help people get the job done fast
- Help AI tools read and use the content safely

Right now, the docs are too vague, too split up, and too hard to run. They need clear structure, working examples, and strong checks before they are published.

---

## Prioritized Audit Findings

**P0 — Unchecked SKILL.md files break trust**

`SKILL.md` files are treated like loose text files, not checked documents. Required fields can be missing, wrong, or hard for AI tools to read.

This causes:
- Missing fields
- Bad version numbers
- Parse errors for AI tools
- No single source of truth

**Fix:** Add a local `test_manifest.py` check and block bad files in CI.

---

**P1 — Docs do not start with the right setup**

Many pages do not say upfront what the reader will do, who the page is for, or how long it will take.

A good guide should start with:
- A clear outcome
- A small table with key details
- A simple `git clone` or `curl` command

**Fix:** Put this setup right after the title on every how-to page.

---

**P2 — Snippets are not enough**

Many docs use small code snippets that readers must copy and build by hand.

This makes people:
- Hunt for files
- Guess folder structure
- Fix spacing and setup issues
- Waste time on setup instead of the task

**Fix:** Give people complete, tested packages they can download and run.

---

## Implementation: Style Guide & Content Template

**Frontmatter Schema (DOC-SKILL-001)**

Every how-to guide MUST include YAML frontmatter with these required fields:

```yaml
title: How to [verb phrase]
description: [One sentence outcome, 20–200 characters]
version: 1.0.0
package_name: tutorial-[slug]
package_language: python
tested_against:
  - claude-opus-4-5
  - claude-3.5-sonnet
```

**Scaffolding Metadata Table (Upfront Contract)**

Right after `# Title`, include:

| Field | Content |
|---|---|
| **Target Audience** | Specific role or use case |
| **Time-to-Hello-World** | Number of minutes to finish |
| **Prerequisites** | Specific tools and versions |
| **Tested Against** | Claude models used for testing |
| **Get Started** | `git clone` or `curl` command |

**Outcome Promise Blockquote**

```markdown
> **Outcome Promise:** By the end of this guide, you will create, deploy, validate, and test the task.
```

---

## Validation & Quality Gates

Every guide with executable code MUST include a downloadable package. Packages MUST:

1. Include `test_manifest.py` for local checks
   ```bash
   python test_manifest.py
   # ✅ SKILL.md validation PASSED
   ```

2. Include `SKILL.md` with required frontmatter and clear Claude instructions

3. Include supporting files in `scripts/`, `references/`, and `assets/`

4. Pass CI checks for:
   - Frontmatter schema
   - YAML parsing
   - Example execution
   - Package structure

5. Be downloadable with one command
   ```bash
   git clone https://github.com/anthropic-ai/docs-examples/tree/main/tutorial-[slug]
   ```

---

## Code & Syntax Conformance Rules

- Every code block MUST declare a language
- Every variable MUST use `<UPPERCASE_SNAKE_CASE>`
- Every step MUST begin with an action verb
- Avoid weak words like “simply” and “just”
- Use active voice

---

## Metrics & Observability

Track success with a few clear measures:

| Metric | Target | Why It Matters |
|---|---|---|
| **Doc-to-Run Latency** | Under 60 seconds | Shows whether the next step is clear |
| **Package Download Rate** | Over 70% | Shows whether people trust the page |
| **Local Validation Pass Rate** | Over 90% | Shows whether the package works |
| **Snippet Execution Drift** | 0 failures | Shows whether docs stay current |

---

## Roadmap: Information Architecture

Make the skills docs easier to browse:

```text
[claude.com/docs/skills/](https://claude.com/docs/skills/)
├── index.md
├── how-to/
│   ├── create-a-custom-skill.md
│   ├── test-your-skill.md
│   └── package-for-upload.md
├── reference/
│   ├── skill-manifest-schema.md
│   ├── errors.md
│   └── examples/
└── concepts/
    ├── when-to-use-skills.md
    ├── skill-scope.md
    └── composability.md
```

**Action:** Redirect old routes and update `llms.txt` to point to the new structure.

---

## Key Principles

1. **Docs as Executable Specifications** — Every guide should say what it helps people do, check itself in CI, and ship a tested package.
2. **Dual-Audience Design** — People read the table and outcome. AI tools read the frontmatter and find the package.
3. **Zero Friction Entry** — Readers should be able to clone and run a working example in under 60 seconds.
4. **Build-Time Validation** — Bad manifests should fail before publish time.
5. **Atomic Delivery** — Examples should be complete packages, not loose snippets.

---

## Conclusion

This audit recommends a shift from publishing information to designing task completion.

The best path is clear:
- Start with the goal
- Show the setup
- Give a working package
- Check everything before publish time
