## Systems Audit & Architecture: Upgrading Skills into an Executable Docs Pipeline

**Date:** August 2026  
**Subject:** From "Publishing Information" to "Designing Task Completion"

---

### Executive Summary

The core failure across [claude.com/docs](https://claude.com/docs) is treating documentation as a static repository of descriptive text rather than an engineered interface for successful task completion.
In an agent-native ecosystem, documentation has two first-class consumers: human engineers and autonomous AI agents (ingesting via llms.txt). When documentation merely describes features instead of validating executable contracts, both humans and agents fail at runtime due to unvalidated SKILL.md manifests, untracked schema drift, and ambiguous execution boundaries across surfaces (Claude.ai, Cowork, M365, Agent SDK).

---

### Prioritized Audit Findings

- P0 — Unvalidated Markdown Contracts (SKILL.md) Across Dual Audiences:
Guides present SKILL.md files as informal text samples without machine-enforced JSON/YAML schemas or build-time AST validation in CI. This causes silent runtime failures for developers and non-deterministic parameter hallucinations for autonomous agents ingesting llms.txt.
- P1 — Omission of Upfront Execution Contracts & Scaffolding:
Pages lack an upfront task-completion contract: explicit outcome promise, audience tiering, estimated Time-to-Hello-World (TTHW), and runtime preconditions (workspace tiers, tool permissions like bash, OAuth scopes).
- P2 — Fragmented Snippets vs. Atomic Task-Execution Packages:
Guides force manual file assembly from isolated snippets instead of providing a downloadable, CI-tested Minimal Working Example (MWE) bundle (e.g., cloneable repository with automated schema assertions).

---

### Adopt a "Docs as Code" Workflow - Information Architecture & HTTP 301 Consolidation

All fragmented Skill routes consolidate into an execution-first specification hierarchy:

```text
[claude.com/docs/skills/](https://claude.com/docs/skills/)
├── index.md                      <-- Execution Lifecycle & Cross-Surface Compatibility Matrix
├── authoring.md                  <-- Task-Completion Contract, MWE Quickstart & CLI Verification
├── schema-reference.md           <-- Declarative YAML/JSON Schema & AST Validation Rules
├── testing-and-evals.md          <-- Pre-commit AST Linting & Headless Eval Testing (CI/CD)
└── reference/
    ├── errors.md                 <-- Standardized Error Codes & Remediation Matrix
    └── examples/                 <-- Downloadable, CI-Asserted Minimal Working Packages
```
Routing & Context Preservation: Permanently redirect legacy routes (/docs/skills/how-to - 301 - /docs/skills/authoring) and update [claude.com/docs/llms.txt](https://claude.com/docs/llms.txt) synchronously in the same deployment commit.
Dual-Consumer Execution Standard: Every operational guide must open with an upfront outcome promise, audience scope, TTHW target, and a single-line curl command to clone a verified reference bundle ready for immediate local testing by developers or IDE agents.

---

### Quantitative Telemetry & Observability

Documentation effectiveness is measured by task completion velocity and schema integrity across data warehouse telemetry and automated CI logs:

| Core Metric | SLA Target | Diagnostic Signal & Calculation |
|---|---|---|
| Doc-to-Run Latency | < 45s | Time delta between page load and initial code-copy or package download event |
| Task Completion Rate | > 85% | Ratio of page visits that lead to a successful local CLI manifest validation ping |
| Schema Pass Rate | > 95% | Ratio of valid Skill manifests vs. client parse rejections in app telemetry |
| Snippet Execution Drift (SED) | 0 build errors | Nightly headless CI job executing doc snippets and MWE packages against the Claude API |

