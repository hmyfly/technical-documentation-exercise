# Part 2: Style Guide, Content Template, and Before/After

This file contains three components:
1. [Style Guide Excerpt](#style-guide-excerpt)
2. [Content-Type Template: How-to Guide](#content-type-template-how-to-guide)
3. [Before/After Page Revision](#beforeafter-page-revision)

---

## Style Guide Excerpt

### Standard ID: DOC-SKILL-001 (Skill Primitive Schema & Task Execution Contract)

#### 1. Frontmatter Schema Requirements

Every page documenting a Skill manifest (`SKILL.md`) or primitive configuration MUST contain a valid YAML frontmatter block adhering to the following schema rules:

* `title` (string, required): Verb phrase starting with "How to"
* `description` (string, required): Exactly one functional sentence (>= 20, <= 200 characters)
* `version` (semver string, required): `MAJOR.MINOR.PATCH` format
* `package_name` (string, required): Must match regex `^[a-z0-9-]+$`
* `package_language` (string, required): One of `python`, `typescript`, `bash`, `json`, `yaml`
* `tested_against` (array of strings, required): List of Claude models tested

#### 2. Upfront Task-Completion Scaffolding

Every operational guide MUST lead with a standardized cognitive contract block immediately beneath the `# Title`:

* **Outcome Promise Blockquote:** `> **Outcome Promise:** By the end of this guide, you will [imperative action verbs].`
* **Scaffolding Metadata Table:** A 2-column table specifying:
  1. `Target Audience` (e.g., SDK users building custom skills)
  2. `Time-to-Hello-World` (explicitly in minutes)
  3. `Prerequisites` (specific tool versions and requirements)
  4. `Tested Against` (e.g., Claude 3.5 Sonnet / Claude Opus 4.5)
  5. `Get Started` (git clone or curl command to download package)

#### 3. Atomic Package Delivery (Zero Isolated Snippets)

* Operational guides MUST provide a single-line `curl` or `git clone` command within the first section to deploy a complete, verified directory bundle.
* Every code example MUST be extracted from the downloadable package and tested before publication.
* Disconnected snippets that require manual file creation are strictly rejected.

#### 4. Syntactic & Code Block Conformance Rules

* **Fenced Code Tagging:** Every code block MUST declare an explicit language identifier (`yaml`, `json`, `bash`, `python`, or `text`).
* **Variable Token Standardization:** Dynamic variables MUST follow `<UPPERCASE_SNAKE_CASE>` convention.
* **Imperative Action Syntax:** Every procedural step MUST begin with an imperative action verb (*Initialize*, *Configure*, *Validate*, *Deploy*, *Create*, *Extract*).

---

## Content-Type Template: How-to Guide

````markdown
---
title: How to [verb phrase — specific task]
description: [One sentence outcome, 20–200 characters]
version: 1.0.0
package_name: tutorial-[slug]
package_language: python
tested_against:
  - claude-opus-4-5
  - claude-3.5-sonnet
---

# How to [verb phrase]

[One to two sentences: the goal and what you'll accomplish. No "This guide will..." phrasing.]

> **Outcome Promise:** By the end of this guide, you will [imperative action verbs: create, deploy, integrate, stream].

| | |
|---|---|
| **Target Audience** | [Specific role, e.g., Python SDK users] |
| **Time-to-Hello-World** | [X minutes] |
| **Prerequisites** | [Specific tool versions and requirements] |
| **Tested Against** | Claude 3.5 Sonnet, Claude Opus 4.5 |
| **Get Started** | `git clone https://github.com/anthropic-ai/docs-examples/tree/main/<PACKAGE_NAME>` |

## Prerequisites

- [Specific requirement 1]
- [Specific requirement 2]

## Step 1: [Verb phrase]

[One to two sentences introducing what this step accomplishes.]

```python
# Code example
```

[Brief explanation of the output.]

## Step 2: [Verb phrase]

[Instructions and code.]

## What you built

[Concrete summary of what reader has accomplished.]

## Next steps

- [Related how-to guide]
- [Reference section]
- [Conceptual guide]
````

---

## Before/After Page Revision

### Before

The following is an example of a documentation page that violates several style guide rules. This is based on typical "Packaging Your Skill" guidance:

---

**Packaging Your Skill**

To package your own skill for Claude, follow these steps. Your skill is a folder. At minimum, it must contain a `SKILL.md` file. The folder name must match the `name` field in your `SKILL.md`.

First, create the SKILL.md file. This file begins with YAML frontmatter:

```
name: brand-guidelines
description: Apply Acme Corp brand guidelines to presentations and documents, including official colors, fonts, and logo usage.
```

The `name` field should be lowercase, numbers, and hyphens only. It must be ≤64 chars and match the directory name. The `description` field explains what the skill does, up to 200 chars (Claude.ai limit).

After the frontmatter, add markdown instructions for Claude:
- Step-by-step guides
- Input/output examples
- Templates or formats
- Edge cases to consider

You can include optional subfolders like `scripts/` (for code), `references/` (for docs), and `assets/` (for templates, images, data). Keep your `SKILL.md` file manageable—it should be ≤500 lines; move extras to reference files. Make instructions clear and focused on one workflow.

Here's an example directory structure:

```
brand-guidelines/
├── SKILL.md
├── scripts/
│   └── validate_branding.py
├── references/
│   └── color_palette.json
└── assets/
    └── logo.png
```

By following this structure and guidelines, you'll ensure your skill is packaged correctly and ready for use with Claude.

---

### After

The revised page below applies the style guide and template:

---

```markdown
---
title: How to package your skill
description: Create a skill folder structure and SKILL.md manifest that Claude can recognize and load, ready for testing and deployment.
version: 1.0.0
package_name: tutorial-packaging-skill
package_language: bash
tested_against:
  - claude-opus-4-5
  - claude-3.5-sonnet
---

# How to package your skill

Create a structured skill directory with a valid `SKILL.md` manifest and optional supporting files. By the end of this guide, you'll have a complete, validated skill package ready to deploy.

> **Outcome Promise:** By the end of this guide, you will create a skill package, structure required and optional directories, configure your SKILL.md manifest, and validate it locally.

| | |
|---|---|
| **Target Audience** | SDK users building custom skills for Claude |
| **Time-to-Hello-World** | 15 minutes |
| **Prerequisites** | A text editor, basic familiarity with YAML and directory structure |
| **Tested Against** | Claude 3.5 Sonnet, Claude Opus 4.5 |
| **Get Started** | `git clone https://github.com/anthropic-ai/docs-examples/tree/main/tutorial-packaging-skill` |

## Prerequisites

- A text editor (VS Code, nano, vim, etc.)
- Basic understanding of YAML syntax
- An Anthropic API key (for testing your skill later)

## Step 1: Create the skill directory

Initialize a new directory with your skill name. Use lowercase letters, numbers, and hyphens only—no spaces or uppercase characters.

```bash
mkdir my-custom-skill
cd my-custom-skill
```

This directory will contain all your skill files. The folder name must match the `name` field in your `SKILL.md` manifest.

## Step 2: Create the SKILL.md manifest

Create a `SKILL.md` file in the root of your skill directory. Begin with YAML frontmatter that defines your skill's identity:

```yaml
---
name: my-custom-skill
description: Apply company brand guidelines to documents, including colors, fonts, and logo usage.
version: 1.0.0
---

# Brand Guidelines Skill

When the user asks you to apply brand guidelines, follow these rules:

## Color Palette

- Primary: #0052CC (Blue)
- Secondary: #F0F0F0 (Light Gray)
- Accent: #FF6B6B (Red)

## Typography

- Headings: Sans-serif, 18pt minimum
- Body text: Sans-serif, 12pt minimum
- Always use sentence case, not Title Case

## Logo Usage

- Minimum size: 100x100 pixels
- Always maintain aspect ratio
- Never rotate or distort
```

**Manifest field requirements:**
- `name`: Lowercase, numbers, hyphens only. Max 64 characters. Must match directory name.
- `description`: Single sentence explaining what the skill does (20–200 characters).
- `version`: Semantic versioning (`MAJOR.MINOR.PATCH`). Start with `1.0.0`.

## Step 3: Add optional supporting files

Create subdirectories for scripts, references, and assets as needed:

```bash
mkdir -p scripts references assets
```

Your skill directory structure now looks like:

```text
my-custom-skill/
├── SKILL.md                 # [REQUIRED] Manifest and instructions
├── scripts/                 # [OPTIONAL] Helper scripts or code
│   └── validate.py
├── references/              # [OPTIONAL] Reference data and docs
│   └── color_palette.json
└── assets/                  # [OPTIONAL] Images, templates, data files
    └── logo.png
```

- `scripts/` — Python, bash, or other code supporting your skill.
- `references/` — JSON, YAML, or markdown files with detailed information.
- `assets/` — Images, templates, PDFs, or other binary files.

## Step 4: Validate your manifest

Copy the `test_manifest.py` file into your skill root directory and run it:

```bash
cp ../test_manifest.py .
python test_manifest.py
```

Expected output:

```text
✅ SKILL.md validation PASSED
```

If validation fails, review the error messages and correct your `SKILL.md` frontmatter.

## What you built

You now have a complete, validated skill package with:

- A structured directory following Anthropic conventions
- A `SKILL.md` manifest with required frontmatter and Claude instructions
- Optional subdirectories for scripts, references, and assets
- Local validation ensuring your manifest is correct before publishing

Your skill is ready to test with Claude or commit to a repository.

## Next steps

- [How to test your skill with Claude](./how-to-test-your-skill.md)
- [SKILL.md schema reference](../reference/skill-schema.md)
- [Understanding skill scope and limitations](../concepts/skill-scope.md)
```

---

### Annotation: What Changed and Why

| Issue in "Before" | Fix in "After" | Style Guide Rule |
|---|---|---|
| Wall of prose; no clear task breakdown | Structured into 4 actionable steps with H2 headings | Imperative action verbs; Content discipline |
| Vague guidance: "add markdown instructions" | Concrete SKILL.md example showing frontmatter and actual branding rules | Atomic package delivery; Code examples |
| Directory structure shown as afterthought | Package anatomy presented early in Step 3 with purpose for each folder | Task-completion scaffolding |
| No validation mentioned | Step 4 provides `test_manifest.py` script for automatic validation | Zero isolated snippets |
| Filler language: "you'll ensure your skill is packaged correctly" | Specific outcome: "Your skill is ready to test with Claude or commit" | Direct, action-oriented voice |
| No frontmatter or related links | Frontmatter block at top; scaffolding table with time estimate; "Next steps" links | Outcome promise; Cognitive contract |
| Optional folders mentioned without rationale | Each folder explained with concrete examples (e.g., "JSON files for data") | Content clarity and completeness |
| No entry point for beginners | "Get Started" shows `git clone` command; package is downloadable and customizable | Atomic package delivery |
