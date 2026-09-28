---
name: github-repository-auth
description: Select repository-appropriate authentication for authorized GitHub operations. Use the default gh CLI authentication for Winrarr repositories; use a local .env token only for other repository scopes listed in the credential mapping.
---

# Repository GitHub Authentication

Determine the GitHub owner of the target repository from its remote before choosing credentials.

## Choose authentication by repository owner

### Winrarr repositories

For repositories owned by `Winrarr`, use the existing default `gh` CLI authentication. Run `gh` normally without sourcing a local environment file or overriding its authentication with a token from `.env`.

If you need to check which account the CLI will use, run `gh auth status --hostname github.com`.

### Other repository owners

For any other owner, resolve `~/.codex/AGENTS.md` and use the `.env/README.md` beside its resolved target as the credential mapping. The `.env/` directory beside that target is the credential directory; do not derive its location from this skill or the target repository. If `~/.codex/AGENTS.md` cannot be resolved, report that the credential mapping cannot be located rather than searching other checkouts.

Use an environment file only when the mapping has an exact matching scope. If there is no matching entry, do not guess; report that no credential mapping is defined.

Load the mapped environment file and run the authenticated command in the same shell:

```bash
global_instructions_file=$(realpath "$HOME/.codex/AGENTS.md")
credentials_dir="$(dirname "$global_instructions_file")/.env"
set -a
source "$credentials_dir/.env.<scope>"
set +a
gh <authorized-command>
```

Use `GH_TOKEN` through `gh` or an equivalent API client's supported environment-based authentication. Keep the token out of command arguments, shell history, source files, logs, and project artifacts. Never print the environment file or token value.

After the operation, avoid retaining the credential in files or exported environment state longer than the shell session requires.
