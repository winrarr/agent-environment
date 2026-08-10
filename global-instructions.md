# Global instructions

## General Guidelines

- Keep agent identity and internal orchestration out of project artifacts. Unless the artifact is specifically about agents or agent instructions, or the user explicitly requests it, do not mention agents, agent names, subagents, Codex, model/tool identity, or agent workflow in branch names, commit messages, author/co-author metadata, pull requests, issues, release notes, code, documentation, UI text, or other user-facing project output. Never auto-add an agent name as a co-author.
- Keep agent instructions, skills, and similar agent-facing artifacts concise, reusable, and durable. Express durable goals, boundaries, and general direction rather than case-specific implementation details, exhaustive steps, transient assumptions, or one-off context that will quickly become stale.
- Write backlog items with the goal, rationale, constraints, and verifiable acceptance criteria. Treat implementation details as context or hypotheses, not instructions; the agent should inspect the current state and adapt its approach when evidence warrants it while still meeting the goal and constraints.
- When completing a token-intensive task likely to recur, consider capturing its reusable parts in a script, skill, or concise instruction. Use scripts for deterministic work and skills or instructions for judgment or workflow. If the addition is useful, well-scoped, and generally applicable, create it and tell the user; if its lasting value or form is uncertain, ask before creating it.
- Do not hard-wrap ordinary Markdown prose at an arbitrary line length; use line breaks when required by Markdown structure, an existing formatter, or deliberate readability.
- Treat human implementation-time estimates as a weak constraint for agents. Prioritize quality, simplicity, robustness, scalability, and long-term maintainability, while considering operational and product costs.
- When fixing a bug, reproduce it end to end when practical, then use focused checks to iterate and verify the fix.
- Treat pixel perfection as a correctness requirement for UI work. Find the underlying layout model that makes the result correct across relevant content, viewports, and states; avoid brittle hard-coded offsets, arbitrary dimensions, and one-off tweaks. Use appropriate structural primitives, such as grid, flex, or layout constraints, and inspect rendered results critically.
- Hold engineering work to a high standard. Fix clearly wrong issues when safely within scope; otherwise mention material issues. For implementation requests, carry the work through implementation, verification, and handoff. Make reasonable low-risk assumptions, ask for guidance only when ambiguity materially changes scope or risk, and surface disagreements and explain them so misunderstandings can be identified and resolved.
- When a breaking change is intentional, clean up obsolete adjacent code instead of preserving compatibility solely to avoid churn.
- For long-running commands, workflows, or other routine operations, use inexpensive periodic status checks at intervals appropriate to the expected duration rather than repeatedly inspecting them. Investigate logs or other details only after a status check shows failure, an unexpected state, or an unusually long run.

## Code Taste

Write code so its correctness is evident from its structure, not from tracing every possible path.

- Handle invalid and exceptional cases first, with early returns; keep the happy path and control flow flat with minimal nesting.
- Keep complexity in the domain model rather than the control flow. Design with the full domain model in mind, even when implementing only a slice.
- Implement only the needed slice when appropriate, provided its design supports extending it to the rest of the domain later; do not simplify the domain model for short-term or control-flow convenience.
- Do not add abstractions or indirection until there is a second real use.
- Keep each function at one level of abstraction and give it one responsibility; separate orchestration from low-level detail.
- Place logic where it naturally belongs; let the code structure mirror the problem.
- Consistency beats local cleverness. Do the same kind of thing the same way everywhere: errors, naming, and how results and failures propagate. When in doubt, match the surrounding code rather than introduce a second pattern.
- Prefer constructs whose correctness is evident from their structure, such as exhaustive matching where the language supports it, rather than clumsy if/else ladders that provide no equivalent guarantee.
