# Project Modes

Use one target state with a workflow adapted to the project's starting condition.

## Create

Use when the user asks for a new project or the destination contains no meaningful implementation.

1. Clarify the product outcome and only the technical choices needed to deliver it.
2. Inspect the environment for available toolchains and explicit user preferences.
3. Select conventional foundations that fit the stated goal; explain choices that materially constrain future work.
4. Create the actual runnable project and representative tests.
5. Establish agent instructions, canonical commands, repository hygiene, and relevant automation alongside the implementation.
6. Run the project and verification end to end.

Do not create an elaborate platform around a small request. Do not call a generated framework shell complete when the user requested working behavior.

## Retrofit

Use when meaningful implementation already exists.

1. Read instructions that govern the repository before taking action.
2. Inspect code, tests, commands, CI, deployment, documentation, and relevant history.
3. Build an evidence-backed map of the current system and identify contradictions or missing capabilities.
4. Preserve existing conventions when they work. Consolidate competing conventions rather than adding another layer.
5. Make the smallest coherent set of changes that reaches the complete target state.
6. Avoid application redesign unless it is required by the user's project goal or separately approved.
7. Verify both the existing behavior and the new operating foundation.

Treat existing uncommitted changes as user work. Do not rewrite or discard them to simplify the retrofit.

## Audit

Use when the user asks for an assessment, review, or report without asking for changes.

Evaluate:

- orientation quality;
- instruction scope and hierarchy;
- sources of truth and protected derived output;
- command discoverability and correctness;
- local/CI parity;
- tests and validation relative to risk;
- durable homes for current architecture, decisions, constraints, planned work, and known debt when each exists;
- stale, duplicated, contradictory, or tool-specific guidance;
- repository hygiene and secret safety.

Support findings with paths and executable evidence. Distinguish missing capability from optional artifact. Do not create files during an audit.

## Repair

Use when an agent-first foundation exists but has drifted.

1. Treat executable behavior and current code as evidence, not automatic proof that documentation is wrong; investigate intent and history where needed.
2. Update canonical sources in place.
3. Remove obsolete duplication instead of preserving compatibility between internal instruction systems without a real consumer.
4. Reconnect wrappers, hooks, and CI to canonical commands.
5. Update or remove stale decisions, constraints, and workflows according to their own history rules.
6. Re-run structural and project verification.

