# Instruction Design

Make correctness and maintenance predictable without turning instructions into a repository encyclopedia.

## Root `AGENTS.md`

Include only durable, project-specific operating knowledge:

- a concise product and component orientation;
- authoritative contracts, schemas, configuration, and generated boundaries;
- project-specific autonomy or approval boundaries keyed to impact;
- non-obvious engineering and testing principles;
- canonical commands and what they cover;
- pointers to architecture, constraints, decisions, operational workflows, planned work, and known debt that actually exist;
- a maintenance rule explaining where future knowledge belongs.

Do not include:

- completed-task history or release notes;
- transient implementation details recoverable from code;
- exhaustive directory listings;
- generic coding advice;
- personal tool preferences presented as project requirements;
- copied documentation that has another source of truth.

Write commands at the level users and automation should invoke. Keep low-level command composition in the task runner or scripts.

## Hierarchy

Prefer a small root file. Add nested `AGENTS.md` only when a subtree changes the operating contract. A nested file should contain local deltas and assume root guidance still applies; do not repeat the root file.

Examples of justified local guidance:

- a component uses a different language and verification command;
- a subtree is generated from another source;
- a deployment directory has material safety constraints;
- a package has a distinct architectural boundary agents routinely cross by mistake.

## Tool Adapters

Keep durable guidance tool-neutral. When a tool requires `CLAUDE.md`, command definitions, hooks, or another surface:

1. Point to the canonical source through a supported symlink or concise adapter.
2. Put only tool mechanics in the tool-specific surface.
3. Invoke canonical repository commands rather than copying their internals.
4. Avoid committing personal configuration unless the repository intentionally standardizes it.

## Commands and CI

Use a single command graph:

```text
documented command ─┐
tool shortcut ──────┼─> canonical task/script ─> formatter/linter/test/build
CI job ─────────────┘
```

This does not require one universal `check` target when separate ecosystem commands are clearer. It requires avoiding multiple independent definitions of the same check.

Keep instructions synchronized with automation. Prefer CI calling repository scripts over copying long command sequences into workflow YAML. Add drift checks for committed generated output. Ensure local checks can run without undisclosed machine state, or document the real prerequisite precisely.

## Maintenance Routing

Give future agents a compact routing rule. For example:

- revise commands in place when automation changes;
- record consequential rationale as a decision;
- record external facts and standing guardrails as constraints;
- keep implementation detail in code and tests;
- create a repo-local skill for a repeated specialized workflow;
- record only real planned outcomes or intentionally unresolved debt;
- remove stale guidance rather than appending exceptions.

Do not link files that do not exist. Create a conditional artifact when its first real entry appears.

