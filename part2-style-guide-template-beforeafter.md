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
* Outcome Promise Blockquote: Formatted as ` **Outcome Promise:** By the end of this guide, you will [imperative action verbs] across Claude applications.`
* Scaffolding Metadata Table: A 2-column table specifying:
  1. `Target Audience` (e.g., Integration Engineers & Enterprise Platform Builders)
  2. `Estimated TTHW (Time-to-Hello-World)` (explicitly in minutes, e.g., 10 Minutes)
  3. `Required Preconditions` (workspace tiers, auth scopes, tooling)
  4. `Tested Runtime Baseline` (e.g., Claude 3.5 Sonnet / Claude 3.7)

#### 3. Atomic Package Delivery (Zero Isolated Snippets)
* Operational guides MUST provide a single-line `curl` or `git clone` command within the first 150 words to deploy a complete, verified directory bundle (`SKILL.md`, runtime scripts, reference tokens, test harness).
* Disconnected snippets that require manual file creation and indentation guesswork are strictly rejected by CI validation.

#### 4. Syntactic & Code Block Conformance Rules
* Fenced Code Tagging: Every code block MUST declare an explicit language identifier (`yaml`, `json`, `bash`, `python`, or `text`). Un-tagged code fences fail pre-merge linting.
* Variable Token Standardization: Dynamic variables inside code snippets MUST follow the `<UPPERCASE_SNAKE_CASE>` convention (e.g., `<SKILL_NAME>`, `<COMPANY_NAME>`). Hardcoded synthetic company or skill names are prohibited in template specifications.
* Imperative Action Syntax: Every procedural instruction item in a numbered sequence MUST begin with an imperative action verb (*Initialize*, *Configure*, *Validate*, *Deploy*).

---

## Content-Type Template: How-to Guide

```
---
title: How to [verb phrase — specific task]
description: [One sentence: what the reader will accomplish and what they need to start.]
---

# How to [verb phrase]

[One to two sentences: the goal of this guide and its expected outcome. Do not start with "This guide will..."]

## Prerequisites

- [Specific requirement 1, e.g., An Anthropic API key]
- [Specific requirement 2, e.g., Python 3.8+ with the anthropic SDK installed]

## [Step 1: Verb phrase]

[One to two sentences introducing what this step accomplishes and why.]

[Code block if applicable]

[Brief explanation of what happened or what to look for in the output.]

## [Step 2: Verb phrase]

...

## [Step N: Verb phrase]

...

## What you built

[One to two sentences summarizing what the reader has accomplished. Be concrete.]

## Next steps

- [Link to related how-to or concept page]
- [Link to relevant reference section]
```

**Template usage notes:**

- Limit how-to guides to a single, completable task. If the guide requires more than six steps, consider splitting it.
- Every step should be a distinct action. If a step is "understand X," it belongs in a Concepts page, not a how-to.
- The title must be a verb phrase starting with an infinitive: `How to stream responses`, `How to use tool use`, `How to handle rate limit errors`.
- Do not include troubleshooting sections inline. Link to a dedicated troubleshooting page if one exists.

---

## Before/After Page Revision

### Before

The following is an example of a documentation page that violates several style guide rules:

---

**Working with the Anthropic API**

The Anthropic API is a great way to utilize our AI models. In order to get started, you will first need to make sure that you have obtained an API key. Once you have done this, you can begin to make API calls.

Making a request is very simple. All you have to do is send some JSON data to our endpoint. The AI will then process your message and generate a response for you that you can then use in your application.

Here is an example:

```
import anthropic
client = anthropic.Anthropic(api_key="YOUR_KEY")
response = client.messages.create(model="claude-opus-4-5", max_tokens=100, messages=[{"role": "user", "content": "Hi"}])
print(response)
```

Please note that there are various parameters you can set. The max_tokens parameter can be utilized to control the length of the AI's output. The temperature setting can also be adjusted. Higher temperatures will cause more creative or random outputs from the AI system.

You might also want to handle errors. If something goes wrong, the API could return an error. You should probably catch these.

---

### After

The revised page below applies the style guide:

---

**Send your first message**

This guide shows you how to send a message to the Claude API and read the response. You will need a valid API key and the `anthropic` Python SDK installed.

## Prerequisites

- An [Anthropic API key](https://console.anthropic.com/)
- Python 3.8 or later
- The `anthropic` SDK: `pip install anthropic`

## Send a message

Set your API key as an environment variable, then send a message to the Messages endpoint:

```python
import anthropic

client = anthropic.Anthropic()  # Reads ANTHROPIC_API_KEY from environment

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)

print(message.content)
```

The API returns a `Message` object. The `content` field contains a list of content blocks. For a plain text response, `message.content[0].text` contains the text string.

## Control output length

Use `max_tokens` to set an upper bound on the number of tokens the model generates. The model may stop before this limit if it reaches a natural endpoint.

```python
message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=256,       # Stop after at most 256 tokens
    messages=[...]
)
```

> **Note:** Setting `max_tokens` too low may cause the response to be cut off mid-sentence. Start with 1024 for most tasks and adjust based on your use case.

## Handle errors

Wrap API calls in a `try/except` block to handle rate limit errors and API errors gracefully:

```python
import anthropic

client = anthropic.Anthropic()

try:
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": "Hello, Claude"}]
    )
    print(message.content)
except anthropic.RateLimitError as e:
    print(f"Rate limit reached: {e}")
except anthropic.APIError as e:
    print(f"API error: {e}")
```

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
