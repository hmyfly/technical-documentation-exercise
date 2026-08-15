# Part 2: Style Guide, Content Template, and Before/After

This file contains three components:
1. [Style Guide Excerpt](#style-guide-excerpt)
2. [Content-Type Template: How-to Guide](#content-type-template-how-to-guide)
3. [Before/After Page Revision](#beforeafter-page-revision)

---

## Style Guide Excerpt

### Standard ID: DOC-SKILL-001 (Skill Primitive Schema & Task Execution Contract)

#### 1. Frontmatter Schema Requirements (Deterministic AST Assertions)
Every page documenting a Skill manifest (`SKILL.md`) or primitive configuration MUST contain a valid YAML frontmatter block adhering to the following schema rules:
* `title` (string)
* `description` (string)
* `version` (semver)
* `package_name` (string)
* `package_language` (string)
* `tested_against` (list of models)

#### 2. Upfront Task-Completion Scaffolding
Every operational guide MUST lead with a standardized cognitive contract block:
* Outcome Promise: Formatted as ` **Outcome Promise:** By the end of this guide, you will [imperative action verbs] across Claude applications.`
* Scaffolding Metadata Table: A 2-column table specifying:
  1. `Target Audience` (e.g., Integration Engineers & Enterprise Platform Builders)
  2. `Estimated TTHW (Time-to-Hello-World)` (explicitly in minutes, e.g., 10 Minutes)
  3. `Prerequisites` (workspace tiers, auth scopes, tooling)
  4. `Tested Against` (e.g., Claude 3.5 Sonnet / Claude 3.7)

#### 3. Atomic Package Delivery (Zero Isolated Snippets)
If a guide includes working code, it MUST be bundled as a downloadable package deployed via a single `curl` or `git clone` command. The bundle MUST include:
- `package.json` / `pyproject.toml` (dependencies)
- Executable script(s) matching the guide's steps
- README with setup and run instructions
- (Optional) Test script verifying the example works

#### 4. Syntactic & Code Block Conformance Rules
* Fenced Code Tagging: Every code block MUST declare an explicit language identifier (`yaml`, `json`, `bash`, `python`, or `text`). Un-tagged code fences fail pre-merge linting.
* Variable Token Standardization: Dynamic variables inside code snippets MUST follow the `<UPPERCASE_SNAKE_CASE>` convention (e.g., `<SKILL_NAME>`, `<COMPANY_NAME>`). Hardcoded synthetic company or skill names are prohibited in template specifications.
* Imperative Action Syntax: Every procedural instruction item in a numbered sequence MUST begin with an imperative action verb (*Initialize*, *Configure*, *Validate*, *Deploy*).

---

## Content-Type Template: How-to Guide

---
```
title: How to [verb phrase — specific task]
description: [One sentence outcome: what the reader will accomplish, 20–200 characters]
version: 1.0.0
package_name: tutorial-[slug]
package_language: python  # or typescript, bash, etc.
tested_against:
  - claude-opus-4-5
  - claude-3.5-sonnet
```
---

### Authoring <PRIMITIVE_NAME>

**Outcome Promise:** By the end of this guide, you will author, validate against schema, locally test, and trigger a custom `<PRIMITIVE_NAME>` across Claude applications.

| Task Scaffolding Dimension | Specification Contract |
| :--- | :--- |
| Target Audience | e.g., Integration Engineers & Enterprise Platform Builders |
| Estimated TTHW (Time-to-Hello-World) | explicitly in minutes, e.g., 10 Minutes |
| Prerequisites | workspace tiers, auth scopes, tooling |
| Tested Against | e.g., Claude 3.5 Sonnet / Claude 3.7 |

---
### Quickstart: Clone Minimal Working Package

```bash
# Clone the canonical minimal working package
curl -L [https://claude.com/assets/skills/](https://claude.com/assets/skills/)<PRIMITIVE_SLUG>-template.tar.gz | tar -xz
cd <PRIMITIVE_SLUG>-template
```
---
#### Package Anatomy
```text
<PRIMITIVE_SLUG>-template/
├── SKILL.md              # [REQUIRED] Frontmatter schema contract & operational prompt
├── scripts/              # [OPTIONAL] Validated deterministic helper binaries
│   └── run.py
├── references/           # [OPTIONAL] Machine-readable payloads (JSON/YAML)
│   └── tokens.json
└── test_manifest.py     # [REQUIRED] Pre-commit schema assertion test
```
### Step-by-Step Implementation
#### Step 1: Unpack Reference Directory
```bash
curl -L [https://claude.com/assets/skills/](https://claude.com/assets/skills/)<PRIMITIVE_SLUG>-template.tar.gz | tar -xz
cd <PRIMITIVE_SLUG>-template
```
#### Step 2: Configure Manifest Variables
Open SKILL.md and customize the predefined YAML frontmatter and prompt directives. Replace all template placeholders (<SKILL_IDENTIFIER>, <COMPANY_NAME>) with your domain values.
#### Step 3: Validate Manifest Schema Locally
```Python
python test_manifest.py
```
#### Step 4: Deploy to Target Surface
Upload the validated package directory to your workspace settings panel or commit to your project repository.

---

## Before/After Page Revision

### Before

The following is an example of a documentation page that violates several style guide rules:

---


---

### After

The revised page below applies the style guide:

---


## Next steps

- [Stream responses in real time](../how-to/stream-responses.md)
- [Messages API reference](../reference/messages.md)
- [Error codes reference](../reference/errors.md)

---

### Annotation: What Changed and Why

| Issue in "Before" | Fix in "After" | Style Guide Rule |
|---|---|---|
| Filler phrases: "is a great way to utilize," "All you have to do is" | Direct, action-oriented language | Voice and Tone |
| Refers to model as "AI," "AI system" | Uses "Claude," "the model," "API" | Terminology |
| Unformatted, single-line code example | Properly formatted, multi-line Python with env-based auth | Code Examples |
| `print(response)` prints the full object — not useful | `print(message.content)` with explanation of the field | Code Examples |
| Vague error guidance: "you should probably catch these" | Concrete try/except block with specific exception types | Code Examples |
| No structure; reads as a wall of prose | H2 sections for each task; scannable | Headings |
| `temperature` mentioned without definition | Removed (belongs in a separate reference entry, not this guide) | Content type discipline |
