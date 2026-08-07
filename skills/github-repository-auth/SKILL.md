---
name: github-repository-auth
description: Prepare repository-scoped local credentials for authorized GitHub operations. Use when authenticated gh CLI commands, GitHub API requests, pull requests, issues, repository administration, or publishing changes require a token from this environment's .env directory.
---

# Repository GitHub Authentication

Use this workflow before any authorized GitHub operation that needs authentication.

## Locate the credentials

1. Identify the repository being operated on from its Git remote and determine its organization or repository scope.
2. Locate the checkout that contains this skill's `skills/github-repository-auth/SKILL.md`. The credential directory is `.env/` at that checkout's root, not in the target repository.
3. Read that checkout's `.env/README.md` and follow its scope-to-file mapping. Do not guess which environment file applies.

## Load and use a token

Load the selected environment file and run the authenticated command in the same shell:

```bash
set -a
source /path/to/agent-environment/.env/.env.<scope>
set +a
gh <authorized-command>
```

Use `GH_TOKEN` through `gh` or an equivalent API client's supported environment-based authentication. Keep the token out of command arguments, shell history, source files, logs, and project artifacts. Never print the environment file or token value.

After the operation, avoid retaining the credential in files or exported environment state longer than the shell session requires.
