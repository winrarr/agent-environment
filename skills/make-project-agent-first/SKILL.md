---
name: make-project-agent-first
description: Create, retrofit, audit, or repair a complete agent-first software project. Use when Codex needs to build a new runnable project whose goals, architecture, instructions, workflows, and verification are legible to coding agents; make an existing repository agent-first without changing its intended product; assess an agent-first setup; or realign project guidance and enforcement after the codebase evolves.
---

# Make Project Agent-First

Create a project in which an unfamiliar coding agent can discover what the project is, change it safely, run it, and prove correctness without relying on conversation history or undocumented conventions.

Treat new and existing projects as different starting states for the same target. Complete every relevant layer, but create no ceremonial artifact merely because another project has one.

## Preserve Goal Ownership

- Derive goals from the user's request. Do not invent product features, architecture goals, deployment targets, scale requirements, compatibility promises, or future work.
- Derive current facts from repository and environment evidence.
- Infer architecture only where the implementation makes it evident. Present material ambiguity instead of laundering an assumption into documentation.
- Recommend improvements when evidence supports them, stating benefit and consequence. Do not silently turn recommendations into project requirements.
- Ask only about choices that cannot be discovered and would materially change the result. Group related questions and continue autonomously elsewhere.

## Choose the Path

Inspect the target before deciding how to work. Read [references/project-modes.md](references/project-modes.md), then use the matching path:

- **Create:** build the runnable project requested by the user and its agent-first foundation together.
- **Retrofit:** preserve intended behavior and architecture while making an existing repository agent-first.
- **Audit:** report evidence-backed gaps without modifying the project unless the user also requests changes.
- **Repair:** realign stale instructions, commands, CI, and durable knowledge with current reality.

Do not reduce a create request to documentation scaffolding. Do not use a retrofit request as permission to redesign the product.

## Establish the Target State

Make these relationships true:

```text
user's actual goals
        ↓
current architecture and constraints
        ↓
clear instructions and durable knowledge
        ↓
canonical executable workflows
        ↓
automated enforcement and verification
```

Evaluate completeness by capability rather than file count. Ensure that an unfamiliar agent can:

1. Orient itself to the product, repository shape, and important boundaries.
2. Find authoritative sources and distinguish source from generated or derived output.
3. Understand real constraints and recognize changes with a wide blast radius.
4. Locate implementation, tests, operational knowledge, and rationale predictably.
5. Run, format, test, build, generate, and validate the project through canonical commands.
6. See the same important checks enforced in CI or the project's equivalent automation when such automation is relevant.
7. Keep the foundation accurate as the project evolves.

## Investigate Before Writing

For an existing repository, inspect at least:

- root and nested instruction files;
- README and current documentation;
- repository status and relevant history;
- package manifests, lockfiles, task runners, scripts, and toolchain pins;
- tests, formatters, linters, build commands, generators, and migrations;
- CI, deployment, release, and environment configuration;
- ignored files, secret handling, generated directories, and scratch output;
- component boundaries and source-of-truth relationships;
- existing local skills, hooks, commands, and tool-specific adapters.

Prefer executable evidence over prose when they disagree. Preserve unrelated work in a dirty worktree.

For a new project, establish only the product and technical decisions necessary to fulfill the request. Use the ecosystem's official initializer or conventional project layout when it fits the user's stated goals. Produce a runnable vertical slice rather than an inert directory skeleton.

## Design the Foundation

Read [references/artifact-selection.md](references/artifact-selection.md) before selecting artifacts. Apply this inclusion test to every conditional artifact:

> This artifact is needed now because it preserves or enforces ________, which already exists or has been explicitly decided.

If the blank can be filled only with a hypothetical future concern, omit the artifact. Never leave empty documents, placeholder sections, invented backlog entries, or speculative ADRs.

Always provide the capabilities of:

- a canonical root `AGENTS.md`;
- a human-facing `README.md` without duplicating operational guidance;
- discoverable run and verification commands appropriate to the project;
- repository hygiene for actual generated output, local state, and secrets;
- tests and checks proportionate to the requested behavior and risk.

Add architecture overviews, ADRs, constraints, backlogs, tech-debt registers, nested instructions, repo-local skills, generated-code guards, hooks, CI, security guidance, or release documentation only when the relevance test passes.

## Write Effective Instructions

Read [references/instruction-design.md](references/instruction-design.md) before creating or substantially restructuring instructions.

Keep `AGENTS.md` concise and operational. Prefer this information shape when relevant:

1. Orientation and component map.
2. Sources of truth and generated boundaries.
3. Autonomy and wide-blast-radius boundaries.
4. Project-specific engineering and testing principles.
5. Canonical commands.
6. Pointers to durable knowledge.
7. Maintenance rules that route new information to the correct home.

Do not encode transient implementation details, completed work, conversation history, or generic advice the agent already knows. Use nested `AGENTS.md` files only for materially different component-local guidance. Keep tool-neutral information canonical and make tool-specific surfaces point to it rather than copy it.

## Make Workflows Executable

Establish one canonical interface for each common operation. Respect an existing task runner when it is coherent; otherwise choose the smallest conventional interface for the project's ecosystem.

- Make documented commands real and runnable.
- Make tool-specific shortcuts invoke canonical commands instead of reimplementing them.
- Make CI call the same underlying checks used locally where CI is relevant.
- Protect generated artifacts at the source and with drift checks when generation is part of the project.
- Treat hooks as fast feedback, not sole enforcement.
- Pin toolchains or generators when reproducibility materially depends on their versions.
- Avoid a universal task runner when native ecosystem commands already form a clear, unified interface.

Implement actual checks; do not merely document commands that do not exist.

## Verify the Result

Run checks proportionate to the work, including:

1. Run the project or the smallest representative executable path for create work.
2. Run focused tests for implemented behavior.
3. Run the canonical project verification command.
4. Exercise generation and drift checks when relevant.
5. Compare documented commands and CI with the actual command graph.
6. Run the bundled structural validator:

```bash
python3 <skill-directory>/scripts/validate_foundation.py <project-root>
```

Treat validator warnings as prompts for judgment, not automatic reasons to add irrelevant files. Fix all errors. Resolve each warning by improving the project or confirming that the capability is intentionally satisfied another way.

Inspect the final diff for accidental duplication, placeholders, stale paths, and unrelated changes. For an audit-only request, run non-mutating checks and report findings rather than editing.

## Hand Off Completely

Report:

- the runnable project behavior created or preserved;
- the agent-first capabilities established;
- conditional artifacts added and the concrete reason each was relevant;
- conditional artifacts deliberately omitted when their absence may be surprising;
- verification performed and what it proves;
- unresolved user-owned decisions, without filling them with invented defaults.

