# Part 1: Systems Audit & Architecture - Upgrading Skills into an Executable Docs Pipeline

---

## Executive Summary
**From "Publishing Information" to "Designing Task Completion"**

The core failure across [claude.com/docs](https://claude.com/docs) is treating documentation as a static repository of descriptive text rather than an engineered interface for successful task completion. Operational guides (how-tos) must commit upfront to specific outcomes, time estimates, and prerequisites—then deliver downloadable, tested packages that developers can run immediately, not isolated code snippets requiring manual assembly.

In an agent-native ecosystem, documentation has two first-class consumers: human engineers and autonomous AI agents (ingesting via llms.txt). When documentation merely describes features instead of enabling immediate, validated action, both audiences fail. This audit identifies three priority gaps and proposes a "docs as code" workflow that treats guides as executable specifications with machine-validated frontmatter, consistent scaffolding, and atomic package delivery.

---

## Prioritized Audit Findings

**P0 — Unvalidated Frontmatter Contracts (SKILL.md) Across Dual Audiences**

Guides present `SKILL.md` files as informal text samples without machine-enforced schema validation. Required metadata fields (`title`, `description`, `version`, `package_name`, `package_language`, `tested_against`) are not validated at build time via CI linting. This causes:
- Developers upload malformed manifests (missing fields, incorrect semver, invalid regex patterns)
- AI agents fail silent parse validation when reading manifests from llms.txt
- No single source of truth for what makes a valid manifest

**Fix:** Implement local `test_manifest.py` validation in every package and CI gates that enforce frontmatter schema before merge.

---

**P1 — Omission of Upfront Execution Contracts & Scaffolding**

Pages lack an upfront task-completion contract. Effective guides must open with:
- **Outcome Promise:** Explicit imperative statement of what readers will accomplish
- **Scaffolding Metadata Table:** Target audience, time-to-hello-world (in minutes), prerequisites, tested model versions, downloadable package link
- **Entry Point:** Single-line `git clone` or `curl` command to download a complete, working package

Current docs bury these details or omit them entirely, forcing readers to infer outcomes and prerequisites by reading prose.

**Fix:** Every how-to guide MUST include frontmatter metadata + scaffolding table immediately after the title.

---

**P2 — Fragmented Snippets vs. Atomic Task-Execution Packages**

Guides force manual file assembly from isolated code snippets instead of providing downloadable, CI-tested packages. Developers must:
- Copy individual code blocks from docs
- Create directory structures manually
- Guess correct indentation, file placement, and dependencies
- Run unvalidated examples that may have drifted from current API versions

Result: High friction, low completion rates, wasted developer time on setup instead of actual task work.

**Fix:** Every code example MUST be extracted from a downloadable package (git clone or curl). Packages include `SKILL.md`, executable scripts, references, and a local `test_manifest.py` validation test. All packages are validated in CI before publication.

---

## Implementation: Style Guide & Content Template

**Frontmatter Schema (DOC-SKILL-001)**

Every how-to guide MUST include YAML frontmatter with these required fields:

```yaml
title: How to [verb phrase]
description: [One sentence outcome, 20–200 characters]
version: 1.0.0  # Semantic versioning (MAJOR.MINOR.PATCH)
package_name: tutorial-[slug]  # Must match regex ^[a-z0-9-]+$
package_language: python  # One of: python, typescript, bash, json, yaml
tested_against:
  - claude-opus-4-5
  - claude-3.5-sonnet
```

**Scaffolding Metadata Table (Upfront Contract)**

Immediately after `# Title`, include:

| Field | Content |
|---|---|
| **Target Audience** | Specific role or use case (e.g., "Python SDK users building with streaming") |
| **Time-to-Hello-World** | Explicit minutes (e.g., "10 minutes") |
| **Prerequisites** | Specific tool versions and requirements |
| **Tested Against** | Claude models tested with this guide |
| **Get Started** | `git clone` or `curl` command to download package |

**Outcome Promise Blockquote**

```markdown
> **Outcome Promise:** By the end of this guide, you will [imperative action verbs: create, deploy, validate, test].
```

---

## Validation & Quality Gates

Every guide with executable code MUST include a downloadable package. Packages MUST:

1. **Include `test_manifest.py`** — Local validation script developers run before commit
   ```bash
   python test_manifest.py
   # ✅ SKILL.md validation PASSED
   ```

2. **Include `SKILL.md`** with required frontmatter + clear Claude instructions

3. **Include optional supporting files** — Scripts, references, assets organized in `scripts/`, `references/`, `assets/` folders

4. **Pass CI validation** — All packages tested in nightly CI jobs:
   - Schema validation (frontmatter conforms to DOC-SKILL-001)
   - Manifest parsing (valid YAML, no syntax errors)
   - Example execution (code snippets run without errors against Claude API)
   - Package structure verification (required files present, no orphaned files)

5. **Be downloadable via single command**
   ```bash
   git clone https://github.com/anthropic-ai/docs-examples/tree/main/tutorial-[slug]
   ```

---

## Code & Syntax Conformance Rules

- **Every code block** MUST declare a language identifier (`python`, `bash`, `typescript`, `json`, `yaml`, `text`)
- **Every variable** MUST use `<UPPERCASE_SNAKE_CASE>` convention (e.g., `<API_KEY>`, `<SKILL_NAME>`)
- **Every procedural step** MUST begin with an imperative action verb: *Initialize*, *Configure*, *Create*, *Deploy*, *Validate*, *Test*, *Extract*
- **No condescending language** — Avoid "simply," "just," "obviously," "easily"
- **Active voice preferred** — "The API returns X" instead of "X is returned by the API"

---

## Metrics & Observability

Documentation effectiveness is measured by task completion velocity and schema integrity:

| Metric | Target | Why It Matters |
|---|---|---|
| **Doc-to-Run Latency** | < 60 seconds | Time from page load to first git clone or code execution event. Indicates whether entry point is obvious. |
| **Package Download Rate** | > 70% | Percentage of page visits that result in downloading the working package. Indicates whether scaffolding table motivates action. |
| **Local Validation Pass Rate** | > 90% | Percentage of downloaded packages that pass `test_manifest.py` on first run. Indicates quality of templates. |
| **Snippet Execution Drift** | 0 failures | Nightly CI job executes all doc code examples against current Claude API. Detects stale or broken examples. |

---

## Roadmap: Information Architecture

Consolidate fragmented skill routes into execution-first hierarchy:

```
[claude.com/docs/skills/](https://claude.com/docs/skills/)
├── index.md                    # Overview & skill use cases
├── how-to/
│   ├── create-a-custom-skill.md
│   ├── test-your-skill.md
│   ├── package-for-upload.md
│   └── ... (other how-tos)
├── reference/
│   ├── skill-manifest-schema.md
│   ├── errors.md
│   └── examples/               # Downloadable packages
└── concepts/
    ├── when-to-use-skills.md
    ├── skill-scope.md
    └── composability.md
```

**Action:** 301-redirect legacy routes (`/docs/skills/how-to` → `/docs/skills/how-to/create-a-custom-skill`) and update [claude.com/docs/llms.txt](https://claude.com/docs/llms.txt) to reference canonical URLs.

---

## Key Principles

1. **Docs as Executable Specifications** — Every operational guide is a specification: it declares what readers will accomplish, validates that specification in CI, and distributes a tested package.

2. **Dual-Audience Design** — Human developers read the scaffolding table and outcome promise. AI agents (via llms.txt) parse valid YAML frontmatter and locate downloadable packages.

3. **Zero Friction Entry** — A reader should be able to clone and run a working example within 60 seconds of landing on the page. The `git clone` command appears in the scaffolding table, not buried in prose.

4. **Build-Time Validation** — Invalid manifests fail CI before publication. Developers and agents never encounter malformed specs.

5. **Atomic Delivery** — Code examples are never isolated snippets. They're always part of a downloadable package with clear file structure, validated manifest, and passing tests.

---

## Conclusion

This audit proposes treating documentation not as information published to readers, but as engineered interfaces for task completion. By adding upfront execution contracts (outcome promise + scaffolding), enforcing schema validation (test_manifest.py in every package), and delivering atomic packages (not isolated snippets), Anthropic docs can serve both human developers and autonomous agents with clarity, speed, and confidence that examples work.
