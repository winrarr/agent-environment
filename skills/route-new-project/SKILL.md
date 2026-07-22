---
name: route-new-project
description: Choose the name and base directory for a new project. Use when creating, scaffolding, initializing, or starting a new project, especially when the user has not supplied a project name or destination path.
---

# Route New Project

Choose the project name and location with minimal interruption.

## Choose the Name

- Use the user's explicit project name when provided.
- Otherwise, infer a concise, descriptive name from the requested product and follow the ecosystem's conventional project and directory naming style.
- Propose the inferred name and ask the user whether it sounds good before creating the project.

## Choose the Location

Before choosing or creating the directory, determine whether the project is personal or work-related.

- If the prompt makes the classification clear, proceed without asking.
- If the classification is unclear, ask the user whether the project is personal or work-related and wait for the answer.
- When both the name and classification need confirmation, ask about them together in one concise message.
- Place personal projects under `~/Documents/dev/`.
- Place work projects under `~/Documents/work/dev/`.
- Let an explicit destination path from the user override these defaults.
