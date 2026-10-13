# Agent environment

This repository is the canonical source for personal instructions and authored skills shared across Codex, Claude Code, and Copilot CLI.

## Contents

- `AGENTS.md` contains repository-local maintenance instructions for working on this repository.
- `global-instructions.md` contains the global instructions used by Codex, Claude Code, and Copilot CLI.
- `skills/` contains personally maintained skills. Third-party and tool-managed skills do not belong here.
- `install` exposes the canonical files in each tool's expected configuration directory.
- `check` validates the repository and the installed links.

When working in this repository, read `AGENTS.md` in addition to the global instructions.

## Set up a machine

Clone the repository anywhere, then run:

```sh
./install
./check
```

The installer derives all link targets from the clone's current location. It is idempotent and refuses to replace unmanaged files or directories.

Codex and Copilot CLI receive each complete skill directory. Claude Code receives the portable skill contents but not Codex-specific `agents/openai.yaml` metadata. The installer uses `COPILOT_HOME` when set, or `~/.copilot` by default.

By default, `./install` installs every skill for Codex, Claude Code, and Copilot CLI. Use repeatable `--agent` and `--skill` options to limit the installation; selecting agents also installs the global instructions for those agents:

```sh
./install --agent copilot --skill github-repository-auth
./install --agent codex --agent copilot --skill route-new-project --skill user-story-design
./check --agent copilot --skill github-repository-auth
```

Omitting `--agent` selects all agents, and omitting `--skill` selects all skills. `./check` accepts the same selectors. The installer only adds or refreshes selected links; it leaves existing installations for unselected agents and skills untouched.

## Maintenance

Edit only the files in this repository. After adding or removing a skill, rerun `./install` and `./check`.

Keep credentials, tool settings, histories, caches, downloaded plugins, and third-party skills out of this repository.
