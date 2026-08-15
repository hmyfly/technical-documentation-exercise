# Part 2: Style Guide, Content Template, and Before/After

This file contains three components:
1. [Style Guide Excerpt](#style-guide-excerpt)
2. [Content-Type Template: How-to Guide](#content-type-template-how-to-guide)
3. [Before/After Page Revision](#beforeafter-page-revision)

---

## Style Guide Excerpt

### Anthropic Developer Documentation Style Guide (Excerpt)

#### Voice and Tone

Write for a developer audience. Assume technical competence; do not over-explain standard programming concepts. Be direct, precise, and respectful of the reader's time.

| ✅ Do | ❌ Don't |
|---|---|
| "Send a request to the Messages endpoint." | "In order to begin utilizing the Messages endpoint, you will want to send a request." |
| "The model returns a `Message` object." | "The AI will give back a Message object for you." |
| "Set `max_tokens` to limit output length." | "You can optionally set the max_tokens parameter if you want to." |

**Tone principles:**
- **Confident, not arrogant.** State facts directly. Avoid hedging with "should," "might," "could" when describing deterministic behavior.
- **Helpful, not condescending.** Do not over-explain. Do not preface instructions with "Simply" or "Just"—it signals the writer, not the reader.
- **Precise, not pedantic.** Use exact terminology consistently. Avoid synonyms that could imply behavioral differences where there are none.

---

#### Terminology

Use the following terms consistently across all documentation.

| Use | Do not use |
|---|---|
| `model` | AI, artificial intelligence, system, bot |
| `assistant` | AI assistant, Claude assistant (unless branding requires) |
| `messages` array | conversation, chat history, conversation history |
| `tool use` | function calling, tool calling |
| `context window` | context length, token limit (unless referring specifically to limits) |
| `prompt` | instruction, query (in most contexts) |
| `stream` (noun/verb) | streaming response, streamed output |
| `stop sequence` | stop token, end token |

---

#### Code Examples

Every code example must:

1. Be runnable as written, or include a clear note about required substitutions (e.g., `YOUR_API_KEY`).
2. Include language-tagged fenced code blocks.
3. Follow the canonical example order: **Python first, then curl**, then other languages if relevant.
4. Use the most recent stable SDK version unless the example is explicitly documenting a version difference.
5. Include inline comments only when the code does something non-obvious. Do not comment every line.

**Python example format:**

```python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)

print(message.content)
```

**curl example format:**

```bash
curl https://api.anthropic.com/v1/messages \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --header "content-type: application/json" \
  --data '{
    "model": "claude-opus-4-5",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Hello, Claude"}]
  }'
```

---

#### Parameter Documentation

Each parameter entry must include:

- **Name** — exact field name as it appears in the API, formatted as inline code.
- **Type** — data type (string, integer, array, object, boolean).
- **Required / Optional** — explicit label.
- **Default** — the default value if optional, or "None" if there is no default.
- **Description** — one to three sentences. What it does, not just what it is. Include behavioral notes (e.g., "Values above 1.0 increase randomness").
- **Constraints** — valid range, allowed values, or format requirements.

---

#### Headings

- Use sentence case for all headings: `Send your first message`, not `Send Your First Message`.
- Do not skip heading levels (do not go from H2 to H4).
- Keep headings descriptive and action-oriented in how-to guides: `Configure streaming`, not `Streaming configuration`.

---

#### Notes, Warnings, and Tips

Use callout blocks sparingly. Each callout should contain information the reader might otherwise skip but genuinely needs.

- **Note:** Additional context or clarification that is helpful but not critical.
- **Warning:** Actions that could cause data loss, unexpected charges, or security risk.
- **Tip:** Non-obvious shortcuts or best practices.

Do not use callouts to repeat information already stated in the main body.

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
