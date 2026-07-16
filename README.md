# Agent environment

This repository is the canonical source for personal instructions and authored skills shared across coding tools.

## Contents

- `INSTRUCTIONS.md` contains the global instructions used by Codex and Claude Code.
- `OPINIONS.md` contains optional preferences that are not part of the global instruction set.
- `skills/` contains personally maintained skills. Third-party and tool-managed skills do not belong here.
- `install` exposes the canonical files in each tool's expected configuration directory.
- `check` validates the repository and the installed links.

## Set up a machine

Clone the repository anywhere, then run:

```sh
./install
./check
```

The installer derives all link targets from the clone's current location. It is idempotent and refuses to replace unmanaged files or directories.

Codex receives each complete skill directory. Claude Code receives the portable skill contents but not Codex-specific `agents/openai.yaml` metadata.

## Maintenance

Edit only the files in this repository. After adding or removing a skill, rerun `./install` and `./check`.

Keep credentials, tool settings, histories, caches, downloaded plugins, and third-party skills out of this repository.
