---
name: user-story-design
description: Generate current and future user stories, define verifiable acceptance criteria, evaluate candidate designs for story coverage and extensibility, and recommend a design. Use when asked to generate user stories or future user stories, map stories to designs, assess whether a design supports current or likely future needs, or compare design options.
---

# User Story Design

Turn product intent into user stories, design criteria, and a recommendation. Keep current implementation scope separate from future capabilities that the design should support.

## Workflow

### 1. Establish the context

- Inspect the relevant repository, documents, existing designs, and implementation when available.
- Identify actors, goals, outcomes, constraints, and important domain concepts.
- State assumptions and ask for clarification only when ambiguity materially changes the stories or design decision.

### 2. Generate the stories

- Write each story as: `As a [actor], I want [capability], so that [outcome].`
- Give each story verifiable acceptance criteria. Use concrete checks or Given/When/Then scenarios where useful.
- Separate stories into:
  - **Current**: capabilities that belong in the requested implementation scope.
  - **Future**: plausible, relevant capabilities that are not requested for implementation now but should influence design evaluation.
- Include a short reason for each future story and avoid inventing speculative features without a connection to the domain or stated goals.
- Keep stories outcome-focused; do not encode a particular implementation in the story itself.

### 3. Derive design criteria

For each story, identify the domain concepts, invariants, interfaces, data, and operational qualities the design must preserve. For future stories, identify what the current design must keep possible without requiring the future capability to be implemented now.

Treat future stories as design constraints and capability checks, not as current scope. A design may support a future story by preserving an extension point or a sound domain model; it does not need to implement the future behavior.

### 4. Compare designs

- Use the designs provided by the user. If none are provided, derive a small set of credible alternatives at the appropriate level of abstraction.
- Evaluate each design against current and future stories, acceptance criteria, simplicity, maintainability, operational cost, complexity, and risk.
- Distinguish between:
  - **Covered now**: the design supports the current story and its implementation.
  - **Supported later**: the design can accommodate the future story without undermining the domain model or forcing an avoidable redesign.
  - **Not supported**: the design conflicts with a story or makes the intended extension impractical.
- Do not add abstractions or complexity solely to accommodate a speculative future story. Make the tradeoff explicit when future support has a real cost.

Use a coverage matrix when it clarifies the decision:

| Story | Status | Design A | Design B | Notes |
| --- | --- | --- | --- | --- |
| Current or future story | Current / Future | Covered now / Supported later / Not supported | Covered now / Supported later / Not supported | Constraints and tradeoffs |

### 5. Recommend and verify

Report:

- The recommended design and the reasons for choosing it.
- Which current stories it covers and how they can be implemented incrementally.
- Which future stories it keeps possible, including any deliberate limitations.
- The main tradeoffs, risks, assumptions, and unresolved conflicts.
- Concrete checks that can verify both current coverage and future extensibility.

Implement or test current stories when requested. Do not implement future stories unless the user explicitly includes them in the current scope.
