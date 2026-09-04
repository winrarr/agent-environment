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
| Product brief or product-fit note | Intended users, representative workflows, product promise, non-goals, or validation criteria materially guide product or architecture choices. | The request is implementation-only and no durable product thesis exists; do not invent market claims or speculative success criteria. |
| Architecture overview | Multiple components, important boundaries, non-obvious data flow, or deployed topology make the system hard to infer. | The directory structure and short root orientation explain the whole system. |
| Research notes | External literature, standards, competitor behavior, or measured evidence materially informs an architectural or product choice. | The work is based only on repository behavior, ordinary implementation knowledge, or an already accepted decision. |
| Design proposal or implementation plan | Important alternatives remain unsettled, or a cross-cutting outcome needs staged work, dependencies, or evidence gates before an accepted decision. | The choice is already accepted and belongs in an ADR, or the material is ordinary implementation detail that code and tests make clear. |
| ADRs | A consequential choice has credible alternatives and rationale future work may relitigate. | Recording ordinary library use, implementation detail, or a decision not yet made. |
| Constraints | External facts, compatibility promises, deployed-state realities, legal obligations, or explicit guardrails restrict implementation. | Restating preferences, architecture decisions, or speculative future limitations. |
| Backlog | Real planned outcomes need to survive beyond the current task. | Inventing a roadmap or creating an empty parking lot. |
| Tech-debt register | Material known shortcomings are intentionally left unresolved. | Logging nitpicks, fixed issues, or hypothetical improvements. |
| Nested `AGENTS.md` | A subtree has materially different boundaries, commands, generated sources, or domain rules. | Repeating root guidance or describing local implementation details. |
| Repo-local skill | A repeated, specialized, non-obvious workflow has a clear boundary and benefits from reusable guidance or scripts. | Encoding a one-off task or moving ordinary project instructions out of `AGENTS.md`. |
| Generated-code protection | Derived artifacts exist and direct edits would be lost or cause drift. | The project has no committed or easily confused generated output. |
| Verification or evidence guide | Tests, benchmarks, measurements, or merge gates have applicability, interpretation, provenance, or coverage rules that are not obvious from commands and CI. | Canonical commands and CI fully explain the checks and no special interpretation or evidence policy exists. |
| Contributor guide | Human branch, commit, review, pull-request, or release rules form a durable contract distinct from product onboarding. | The README and automation already cover the contribution policy, or no shared contribution process exists. |
| Operational runbook or deployment guide | Deployment, migration, backup, upgrade, recovery, incident handling, or resource operations require ordered or safety-sensitive procedures. | There is no supported operational surface, or the deployment artifact and commands are self-explanatory. |
| CI | The repository has or is being given a real remote workflow where automated checks provide value. | The user explicitly wants a local experiment with no repository automation. |
| Hooks | Immediate feedback prevents common mistakes and the relevant tool supports hooks. | A hook would be the only enforcement or require unsupported personal tooling. |
| Security guidance | Credentials, sensitive data, permissions, or trust boundaries create project-specific handling rules. | Filling a file with generic security advice. |
| Release documentation | A real distribution or deployment process has commands, ordering, or compatibility obligations. | Nothing is released or deployed yet. |

## Knowledge Routing

Keep categories distinct:

- **Instructions:** how to work in this repository now.
- **Product direction:** intended users, workflows, promises, non-goals, and validation criteria.
- **Current architecture:** what exists and how its major parts relate.
- **Research:** source-backed external findings, comparisons, measurements, and explicit inferences that inform design without becoming decisions by themselves.
- **Design proposal:** unsettled alternatives, implementation plans, dependencies, and evidence gates.
- **Decision record:** a revisitable choice and its rationale.
- **Constraint:** a fact or standing boundary current work must respect.
- **Backlog:** an explicitly intended outcome that does not exist yet.
- **Tech debt:** a known shortcoming intentionally left in current implementation.
- **Skill:** a reusable task workflow with a clear trigger and boundary.
- **Verification and evidence:** test strategy, benchmark interpretation, measurement provenance, and merge gates.
- **Contribution policy:** shared human branch, review, commit, and release rules.
- **Operations:** deployment, migration, backup, upgrade, recovery, and incident procedures.
- **Code and tests:** implementation detail and observable behavior.

Research notes should identify their date, scope, source quality, relevant links,
and which conclusions are observations versus inferences. Keep recommendations
and unresolved questions explicit; move an accepted choice to an ADR and an
unfinished outcome to the backlog.

When the first real item in a category appears, create its durable home and link it from `AGENTS.md`. Until then, let the routing rule describe where it should go without creating an empty artifact.

## ADR Guidance

Record one decision per ADR. Include status, date, decision, rationale, and relevant constraints. Prefer a small index describing how records are superseded. Do not rewrite accepted history to reflect a later choice; supersede it according to the project's chosen convention.

## Constraint Guidance

State the external fact or explicit guardrail first, then its practical consequence. Keep secrets out of constraints. Change a factual constraint when the underlying reality changes; remove a deliberate guardrail only through an explicit decision.
