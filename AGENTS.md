# Agent Environment Repository

This repository is the canonical source for personal instructions and authored skills shared across coding tools.

## Sources of truth

- Edit `global-instructions.md` for global instructions. `install` exposes it as Codex `AGENTS.md` and Claude Code `CLAUDE.md`; do not edit those installed paths directly.
- Edit skill source under `skills/`. Each skill's `SKILL.md` is its operational source, and `agents/openai.yaml` contains optional Codex interface metadata.
- Keep `.env/` local and ignored. Credential loading and scope selection belong to the `github-repository-auth` skill; never add credential values to tracked files.
- Keep `README.md` focused on human setup and orientation rather than duplicating operational instructions.

## Canonical commands

```sh
./install
./check
```

Run both commands after changing instructions, skills, the installer, or the checker. `install` refreshes the tool links for this checkout; `check` validates the source layout and installed links.

## Maintenance

Keep global guidance in `global-instructions.md`, repository-specific guidance here, and specialized reusable workflows in skills. Inspect the final diff for accidental credential or generated-state changes before committing.

When editing anything in this repository, first identify the goal of each affected artifact. Preserve that goal while tightening phrasing or structure where useful; do not change that goal without the user's agreement.

After changing the global agent instructions or personally maintained skills in this repository, validate the changes, commit them, and push the current branch unless the user explicitly asks not to.
