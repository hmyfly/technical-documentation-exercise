# Standard ID: DOC-SKILL-001 (Skill Primitive Schema & Task Execution Contract)

### 1. Frontmatter Schema Requirements (Deterministic AST Assertions)
Every page documenting a Skill manifest (`SKILL.md`) or primitive configuration MUST contain a valid YAML frontmatter block adhering to the following schema rules:
* `name` (string, required): Must match regex `^[a-z0-9-_]+$`. No whitespace or uppercase characters allowed.
* `version` (semver string, required): Must follow strict semantic versioning (`MAJOR.MINOR.PATCH`, e.g., `"1.0.0"`).
* `description` (string, required): Exactly one functional sentence defining the procedural output (>= 20 characters, <= 200 characters).
* `invocation` (enum, required): Must be explicitly declared as either `"automatic"` or `"user_prompted"`.
* `context_cost` (enum, required): Must be explicitly declared as `"static"` or `"on_demand"`.
* `runtime_compatibility` (array of strings, required): Must list at least one valid Claude surface target (`"Claude.ai"`, `"Cowork"`, `"Claude for M365"`, or `"Claude Code / Agent SDK"`).
* `parameters` (object, required if inputs exist): Must be a valid JSON Schema object declaring `properties` and `required` fields.

### 2. Upfront Task-Completion Scaffolding
Every operational guide MUST lead with a standardized cognitive contract block immediately beneath the `# Title`:
* Outcome Promise Blockquote: Formatted as `> **Outcome Promise:** By the end of this guide, you will [imperative action verbs] across Claude applications.`
* Scaffolding Metadata Table: A 2-column table specifying:
  1. `Target Audience` (e.g., Integration Engineers & Enterprise Platform Builders)
  2. `Estimated TTHW (Time-to-Hello-World)` (explicitly in minutes, e.g., 10 Minutes)
  3. `Required Preconditions` (workspace tiers, auth scopes, tooling)
  4. `Tested Runtime Baseline` (e.g., Claude 3.5 Sonnet / Claude 3.7)

### 3. Atomic Package Delivery (Zero Isolated Snippets)
* Operational guides MUST provide a single-line `curl` or `git clone` command within the first 150 words to deploy a complete, verified directory bundle (`SKILL.md`, runtime scripts, reference tokens, test harness).
* Disconnected snippets that require manual file creation and indentation guesswork are strictly rejected by CI validation.

### 4. Syntactic & Code Block Conformance Rules
* Fenced Code Tagging: Every code block MUST declare an explicit language identifier (`yaml`, `json`, `bash`, `python`, or `text`). Un-tagged code fences fail pre-merge linting.
* Variable Token Standardization: Dynamic variables inside code snippets MUST follow the `<UPPERCASE_SNAKE_CASE>` convention (e.g., `<SKILL_NAME>`, `<COMPANY_NAME>`). Hardcoded synthetic company or skill names are prohibited in template specifications.
* Imperative Action Syntax: Every procedural instruction item in a numbered sequence MUST begin with an imperative action verb (*Initialize*, *Configure*, *Validate*, *Deploy*).
