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

The following is the current "Creating custom skills" page from https://claude.com/docs/skills/how-to. It violates several style guide rules:

---

**Creating custom skills**

> Learn how to create, structure, and test your own custom skills

Custom skills extend Claude with specialized knowledge and workflows. This guide explains how to create, structure, and test your own skills.

Skills can range from simple instruction sets to multi-file packages with executable code. Effective skills:

* Solve a specific, repeatable task
* Have clear instructions Claude can follow
* Include examples when helpful
* Define when they should be used
* Focus on one workflow rather than trying to do everything

<Note>
  Skills follow the [Agent Skills specification](https://agentskills.io/specification) — see the specification for more in-depth information.
</Note>

## Directory structure

A skill is a directory containing at minimum a `SKILL.md` file:

```
brand-guidelines/
├── SKILL.md
├── scripts/        # Optional: executable code
├── references/     # Optional: additional documentation
└── assets/         # Optional: templates, images, data files
```

The directory name must match the `name` field in your `SKILL.md`.

## Creating a `SKILL.md` file

The `SKILL.md` file must start with YAML frontmatter containing required metadata, followed by markdown instructions.

### Required fields

```markdown
---
name: brand-guidelines
description: Apply Acme Corp brand guidelines to presentations and documents, including official colors, fonts, and logo usage.
---
```

**name**: Lowercase letters, numbers, and hyphens only. Maximum 64 characters. Must match the directory name.

**description**: Explains what the skill does and when to use it. Claude uses this to determine when to invoke your skill.

<Warning>
  Claude.ai limits descriptions to **200 characters**.
</Warning>

### Markdown body

After the frontmatter, write markdown instructions for Claude. Include:

* Step-by-step procedures
* Examples of inputs and outputs
* Templates or formatting requirements
* Edge cases to handle

Keep your main `SKILL.md` under 500 lines. Move detailed reference material to separate files.

## Adding resources

For content too detailed for `SKILL.md`, add files to your skill directory:

* **`references/`**: Additional documentation Claude can read when needed
* **`assets/`**: Templates, images, lookup tables, schemas
* **`scripts/`**: Executable code

Reference these files in `SKILL.md` so Claude knows when to load them. Keep files focused—smaller files mean less context usage.

## Packaging your skill

To upload a skill to Claude:

1. Ensure the directory name matches your skill's `name` field
2. Create a ZIP file containing the skill directory

## Testing your skill

### Before uploading

1. Review `SKILL.md` for clarity
2. Verify the description accurately reflects when Claude should use the skill
3. Check that all referenced files exist
4. Validate using `skills-ref validate ./my-skill`

### After uploading

1. Enable the skill in **Customize > Skills**
2. Try prompts that should trigger it
3. Review Claude's thinking
4. Iterate on the description

---

### After

The revised page below applies the style guide and template:

---

```markdown
---
title: How to create a custom skill
description: Build and structure a custom skill with SKILL.md manifest, optional scripts and references, then test and validate it locally before uploading.
version: 1.0.0
package_name: tutorial-create-custom-skill
package_language: bash
tested_against:
  - claude-opus-4-5
  - claude-3.5-sonnet
---

# How to create a custom skill

Custom skills extend Claude with specialized knowledge and workflows. This guide walks you through creating a focused, reusable skill that Claude can discover and invoke automatically.

> **Outcome Promise:** By the end of this guide, you will create a skill directory, structure a valid SKILL.md manifest, add optional supporting files, validate locally, and package it for upload.

| | |
|---|---|
| **Target Audience** | Developers building custom Claude skills for Claude.ai or Code |
| **Time-to-Hello-World** | 20 minutes |
| **Prerequisites** | A text editor; basic understanding of YAML syntax; familiarity with directory structures |
| **Tested Against** | Claude 3.5 Sonnet, Claude Opus 4.5 |
| **Get Started** | `git clone https://github.com/anthropic-ai/docs-examples/tree/main/tutorial-create-custom-skill` |

## Prerequisites

- A text editor (VS Code, nano, vim, etc.)
- Basic understanding of YAML and Markdown syntax
- An Anthropic API key (for testing skills later)

## Step 1: Create your skill directory

Initialize a new directory with your skill name. Use lowercase letters, numbers, and hyphens only—no spaces or uppercase characters.

```bash
mkdir my-custom-skill
cd my-custom-skill
```

This directory will contain all your skill files. The folder name must match the `name` field in your `SKILL.md` manifest.

## Step 2: Create the SKILL.md manifest

Create a `SKILL.md` file in the root of your skill directory. Begin with YAML frontmatter containing required metadata, followed by markdown instructions for Claude:

```yaml
---
name: my-custom-skill
description: Apply company brand guidelines to presentations and documents, including colors, fonts, and logo usage.
---

# Brand Guidelines

Apply these standards when creating presentations, documents, or marketing materials.

## Brand colors

- Primary: #FF6B35 (Coral)
- Secondary: #004E89 (Navy Blue)
- Accent: #F7B801 (Gold)
- Neutral: #2E2E2E (Charcoal)

## Typography

- Headers: Montserrat Bold
- Body text: Open Sans Regular
- Size guidelines: H1 32pt, H2 24pt, Body 11pt

## Logo usage

- Use full-color logo on light backgrounds
- Use white logo on dark backgrounds
- Maintain minimum 0.5 inches spacing around logo

## When to apply

Apply these guidelines when creating:
- PowerPoint presentations
- Word documents for external sharing
- Marketing materials
- Client reports

See the [assets/](assets/) folder for logo files and fonts.
```

**Required frontmatter fields:**
- `name`: Lowercase, numbers, hyphens only. Max 64 characters. Must match directory name.
- `description`: Single sentence explaining what the skill does and when to use it (max 200 characters).

**Markdown body requirements:**
- Include step-by-step procedures
- Provide examples of inputs and outputs
- Define templates or formatting requirements
- List edge cases to handle
- Keep under 500 lines (move detailed content to references/)

## Step 3: Add optional supporting files

Create subdirectories for scripts, references, and assets as needed:

```bash
mkdir -p scripts references assets
```

Your skill directory structure now looks like:

```text
my-custom-skill/
├── SKILL.md                 # [REQUIRED] Manifest and Claude instructions
├── scripts/                 # [OPTIONAL] Executable code (Python, JS, Bash)
│   └── validate.py
├── references/              # [OPTIONAL] Detailed reference docs
│   └── color_palette.json
└── assets/                  # [OPTIONAL] Templates, images, lookup tables
    └── logo.png
```

**Guidance for each folder:**
- `scripts/` — Executable code Claude can run. Declare dependencies in frontmatter with `dependencies: python>=3.8, pandas>=1.5.0`.
- `references/` — JSON, YAML, or markdown files with detailed information Claude reads when needed. Keep files focused to minimize context usage.
- `assets/` — Images, templates, PDFs, or lookup tables your skill may reference.

## Step 4: Validate your skill locally

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

Alternatively, use the official validation tool:

```bash
skills-ref validate ./my-custom-skill
```

## Step 5: Package and upload your skill

Prepare your skill for upload to Claude:

```bash
# Ensure directory name matches your skill's name field
# Create a ZIP file with correct structure:
my-custom-skill.zip
└── my-custom-skill/
    ├── SKILL.md
    ├── scripts/
    ├── references/
    └── assets/
```

Then upload via Claude.ai:

1. Go to **Customize > Skills**
2. Click **Upload skill**
3. Select your ZIP file
4. Enable the skill

## Step 6: Test your skill in Claude

After uploading, verify the skill works as expected:

1. **Enable the skill** in **Customize > Skills**
2. **Trigger it** with test prompts that should activate the skill
3. **Review Claude's thinking** (visible in Claude Code) to confirm the skill loaded
4. **Iterate on the description** if Claude isn't using it when expected

Refine your skill's `description` field to help Claude identify when to invoke it. Be specific about the task and include keywords that match user queries.

## What you built

You now have a complete, validated, uploadable skill with:

- A structured directory following the Agent Skills specification
- A `SKILL.md` manifest with required frontmatter and clear Claude instructions
- Optional supporting files (scripts, references, assets) organized by purpose
- Local validation ensuring your manifest conforms to schema before publishing
- Clear instructions for when and how Claude should use the skill

Your skill is ready to enable in Claude.ai or Claude Code.

## Best practices

- **Keep it focused**: Create separate skills for different workflows rather than one large skill
- **Write clear descriptions**: Be specific about when the skill applies; include keywords Claude can match
- **Start simple**: Begin with markdown instructions before adding scripts or complex logic
- **Use examples**: Include example inputs/outputs to help Claude understand success
- **Test incrementally**: Validate after each significant change
- **Leverage composability**: Claude can use multiple focused skills together automatically

## Next steps

- [Agent Skills specification](https://agentskills.io/specification)
- [Skills in Claude Code](https://code.claude.com/docs/en/skills)
- [Example skills repository](https://github.com/anthropics/skills/tree/main/skills)

