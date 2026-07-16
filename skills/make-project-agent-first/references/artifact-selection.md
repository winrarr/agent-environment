# Artifact Selection

Select artifacts by present need. A complete agent-first project contains every relevant capability, not every possible file.

## Core Capabilities

### Root instructions

Create `AGENTS.md` at the project root. Make it the canonical operational guide for coding agents. If an existing platform requires another filename, use a symlink or a minimal adapter when portable and supported; otherwise keep the tool-specific file narrow and point it to `AGENTS.md`.

### Human orientation

Create or improve `README.md`. Explain the product, supported setup, and basic human onboarding. Link to `AGENTS.md` for agent operating rules rather than duplicating them.

### Executable workflows

Provide discoverable commands for the operations the project actually supports: setup, run, format, test, build, generate, validate, or deploy. One project need not support every operation.

### Repository hygiene

Ignore actual local state, build output, caches, coverage output, scratch captures, and secrets. Commit intentional lockfiles and generated artifacts according to the project's real strategy.

## Conditional Artifacts

| Artifact | Add when | Do not add when |
|---|---|---|
| Architecture overview | Multiple components, important boundaries, non-obvious data flow, or deployed topology make the system hard to infer. | The directory structure and short root orientation explain the whole system. |
| ADRs | A consequential choice has credible alternatives and rationale future work may relitigate. | Recording ordinary library use, implementation detail, or a decision not yet made. |
| Constraints | External facts, compatibility promises, deployed-state realities, legal obligations, or explicit guardrails restrict implementation. | Restating preferences, architecture decisions, or speculative future limitations. |
| Backlog | Real planned outcomes need to survive beyond the current task. | Inventing a roadmap or creating an empty parking lot. |
| Tech-debt register | Material known shortcomings are intentionally left unresolved. | Logging nitpicks, fixed issues, or hypothetical improvements. |
| Nested `AGENTS.md` | A subtree has materially different boundaries, commands, generated sources, or domain rules. | Repeating root guidance or describing local implementation details. |
| Repo-local skill | A repeated, specialized, non-obvious workflow has a clear boundary and benefits from reusable guidance or scripts. | Encoding a one-off task or moving ordinary project instructions out of `AGENTS.md`. |
| Generated-code protection | Derived artifacts exist and direct edits would be lost or cause drift. | The project has no committed or easily confused generated output. |
| CI | The repository has or is being given a real remote workflow where automated checks provide value. | The user explicitly wants a local experiment with no repository automation. |
| Hooks | Immediate feedback prevents common mistakes and the relevant tool supports hooks. | A hook would be the only enforcement or require unsupported personal tooling. |
| Security guidance | Credentials, sensitive data, permissions, or trust boundaries create project-specific handling rules. | Filling a file with generic security advice. |
| Release documentation | A real distribution or deployment process has commands, ordering, or compatibility obligations. | Nothing is released or deployed yet. |

## Knowledge Routing

Keep categories distinct:

- **Instructions:** how to work in this repository now.
- **Current architecture:** what exists and how its major parts relate.
- **Decision record:** a revisitable choice and its rationale.
- **Constraint:** a fact or standing boundary current work must respect.
- **Backlog:** an explicitly intended outcome that does not exist yet.
- **Tech debt:** a known shortcoming intentionally left in current implementation.
- **Skill:** a reusable task workflow with a clear trigger and boundary.
- **Code and tests:** implementation detail and observable behavior.

When the first real item in a category appears, create its durable home and link it from `AGENTS.md`. Until then, let the routing rule describe where it should go without creating an empty artifact.

## ADR Guidance

Record one decision per ADR. Include status, date, decision, rationale, and relevant constraints. Prefer a small index describing how records are superseded. Do not rewrite accepted history to reflect a later choice; supersede it according to the project's chosen convention.

## Constraint Guidance

State the external fact or explicit guardrail first, then its practical consequence. Keep secrets out of constraints. Change a factual constraint when the underlying reality changes; remove a deliberate guardrail only through an explicit decision.

