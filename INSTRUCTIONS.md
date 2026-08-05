# INSTRUCTIONS.md

These are common instructions for agents across all scenarios

## General Guidelines

- Keep agent identity and internal orchestration out of project artifacts. Unless the artifact is specifically about agents or agent instructions, or the user explicitly requests it, do not mention agents, agent names, subagents, Codex, model/tool identity, or agent workflow in branch names, commit messages, author/co-author metadata, pull requests, issues, release notes, code, documentation, UI text, or other user-facing project output. Never auto-add an agent name as a co-author.
- Keep agent instructions, skills, and similar agent-facing artifacts concise and reusable. They should only express durable goals, boundaries, or general direction; do not encode case-specific implementation details, exhaustive steps, transient assumptions, or one-off task context that will quickly become stale.
- When completing a token-intensive task that is likely to recur, consider turning the reusable parts into a general mechanism, such as a script, skill, or concise agent instruction. Prefer the artifact that best fits the work: scripts for deterministic operations, skills or instructions for reusable judgment and workflow guidance. If the addition is clearly useful, appropriately scoped, and generally applicable, create it and tell the user. If its lasting value or appropriate form is uncertain, ask before creating it.
- Do not hard-wrap ordinary Markdown prose at an arbitrary line length; use line breaks when required by Markdown structure, an existing formatter, or deliberate readability.
- Do not put much weight on implementation time when making technical decisions. Estimates based on how long a human would take are a poor constraint for agents; prefer quality, simplicity, robustness, scalability, and long-term maintainability, while still considering real operational and product costs.
- When fixing a bug, reproduce it end to end when practical, then use focused checks to iterate.
- Treat pixel perfection as a correctness requirement for UI work. Find the underlying layout model that makes the result correct across relevant content, viewports, and states; do not paper over visual problems with brittle hard-coded offsets, arbitrary dimensions, or one-off tweaks. Use appropriate structural primitives, such as grid, flex, or layout constraints, and inspect rendered results critically.
- Hold engineering work to a high standard. If something clearly looks wrong, fix it when safely within scope; otherwise mention the material issue.
- When the user asks for implementation, carry it through implementation, verification, and handoff. Make reasonable low-risk assumptions; ask for guidance only when ambiguity materially changes scope or risk. Surface disagreements and explain them.
- When a breaking change is intentional, clean up obsolete adjacent code instead of preserving compatibility solely to avoid churn.
- When waiting for a long-running command, workflow, or other routine operation, use a cheap status check at a fitting interval instead of repeatedly inspecting it. Choose an initial delay and subsequent interval based on the expected duration (for example, wait five minutes before the first check, then check every minute). Investigate logs or other details only when a status check shows failure, an unexpected state, or an unusually long run.
- After changing the global agent instructions or personally maintained skills in `/home/rkth/agents`, validate the changes, commit them, and push the current branch unless the user explicitly asks not to.
- For authorized GitHub operations, source `/home/rkth/agents/.env.local` to load `GH_TOKEN`. Treat the file and variable as secrets: never display, log, commit, or include their values in project artifacts.
- For Kube Kraken repositories, source `/home/rkth/agents/.env.kube-kraken` to load the repository-scoped `GH_TOKEN`; keep this file local, ignored, and out of project artifacts.

## Code Taste

The guiding property: a function's correctness should be legible from its structure. You should trust it from its shape, not by tracing every path.

- Happy path runs straight down the middle. Handle invalid or exceptional cases first with early returns, then let the main logic proceed flat. Avoid deep nesting.
- A function does one thing at one level of abstraction. It should read like a table of contents, not orchestration interleaved with low-level detail.
- Logic lives where you would predict it does; the code's shape mirrors the problem's shape.
- Consistency beats local cleverness. Do the same kind of thing the same way everywhere: errors, naming, and how results and failures propagate. When in doubt, match the surrounding code rather than introduce a second pattern.
- Complexity belongs in the domain, not the control flow. Model the domain fully, but keep the structure expressing it flat and linear. Do not undermodel the domain for simplicity; do not add abstraction or indirection until there is a second real use for it.
- Prefer constructs whose correctness is evident from structure, for example exhaustive matching where the language supports it. Do not simulate that with clumsy if-else ladders where the language gives no guarantee.
