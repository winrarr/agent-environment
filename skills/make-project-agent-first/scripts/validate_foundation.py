#!/usr/bin/env python3
"""Validate structural properties of an agent-first project foundation."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit


LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER_RE = re.compile(
    r"(?:\[TODO[^\]]*\]|\bTODO\s*:|\bTBD\b|\bCHANGEME\b|<project[-_ ]?name>)",
    re.IGNORECASE,
)
COMMAND_SECTION_RE = re.compile(r"^#{1,6}\s+.*(?:commands?|verification|development|getting started)", re.IGNORECASE | re.MULTILINE)
FENCE_RE = re.compile(r"```(?:sh|shell|bash|console)?\s*\n.+?```", re.DOTALL)


@dataclass(frozen=True)
class Finding:
    level: str
    path: Path
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path, help="project root to validate")
    parser.add_argument(
        "--fail-on-warnings",
        action="store_true",
        help="return a failure status when warnings remain",
    )
    return parser.parse_args()


def markdown_files(root: Path) -> list[Path]:
    paths = set(root.glob("*.md"))
    paths.update(root.rglob("AGENTS.md"))
    for directory_name in ("docs", "documentation"):
        directory = root / directory_name
        if directory.is_dir():
            paths.update(directory.rglob("*.md"))
    skills = root / ".agents" / "skills"
    if skills.is_dir():
        paths.update(skills.rglob("*.md"))
    return sorted(path for path in paths if path.is_file())


def foundation_files(root: Path) -> list[Path]:
    names = {
        "AGENTS.md",
        "CLAUDE.md",
        "CONSTRAINTS.md",
        "BACKLOG.md",
        "TECH_DEBT.md",
        "architecture-overview.md",
    }
    return [path for path in markdown_files(root) if path.name in names]


def validate_required_files(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for name in ("AGENTS.md", "README.md"):
        path = root / name
        if not path.exists():
            findings.append(Finding("ERROR", path, f"required root file is missing: {name}"))
        elif not path.is_file():
            findings.append(Finding("ERROR", path, f"expected a file: {name}"))
        elif not path.read_text(encoding="utf-8").strip():
            findings.append(Finding("ERROR", path, f"required root file is empty: {name}"))
    return findings


def validate_placeholders(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    candidates = set(foundation_files(root))
    candidates.update(path for path in (root / "README.md",) if path.exists())
    for path in sorted(candidates):
        if path.is_symlink() and not path.exists():
            findings.append(Finding("ERROR", path, "broken instruction symlink"))
            continue
        if not path.is_file():
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if PLACEHOLDER_RE.search(line):
                findings.append(Finding("ERROR", path, f"placeholder on line {line_number}: {line.strip()}"))
    return findings


def link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return target.split(maxsplit=1)[0]


def validate_links(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        seen_targets: set[str] = set()
        for raw_target in LINK_RE.findall(text):
            target = link_target(raw_target)
            if target in seen_targets:
                continue
            seen_targets.add(target)
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith(("#", "mailto:")):
                continue
            relative = unquote(parsed.path)
            if not relative:
                continue
            if relative.startswith("/"):
                findings.append(Finding("WARN", path, f"non-portable absolute local link: {target}"))
                continue
            resolved = (path.parent / relative).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                findings.append(Finding("WARN", path, f"local link leaves project root: {target}"))
                continue
            if not resolved.exists():
                findings.append(Finding("ERROR", path, f"broken local link: {target}"))
    return findings


def validate_instruction_shape(root: Path) -> list[Finding]:
    agents = root / "AGENTS.md"
    if not agents.is_file():
        return []

    text = agents.read_text(encoding="utf-8")
    findings: list[Finding] = []
    if not COMMAND_SECTION_RE.search(text):
        findings.append(Finding("WARN", agents, "no commands or verification section was detected"))
    if not FENCE_RE.search(text) and "`" not in text:
        findings.append(Finding("WARN", agents, "no executable command examples were detected"))

    claude = root / "CLAUDE.md"
    if claude.is_file() and not claude.is_symlink():
        claude_text = claude.read_text(encoding="utf-8")
        if len(claude_text.splitlines()) > 40 and claude_text != text:
            findings.append(
                Finding(
                    "WARN",
                    claude,
                    "substantial tool-specific instructions may compete with canonical AGENTS.md",
                )
            )
    return findings


def main() -> int:
    args = parse_args()
    root = args.project_root.expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR {root}: project root is not a directory", file=sys.stderr)
        return 2

    findings = [
        *validate_required_files(root),
        *validate_placeholders(root),
        *validate_links(root),
        *validate_instruction_shape(root),
    ]
    findings.sort(key=lambda item: (item.level != "ERROR", str(item.path), item.message))

    for finding in findings:
        try:
            display_path = finding.path.relative_to(root)
        except ValueError:
            display_path = finding.path
        print(f"{finding.level} {display_path}: {finding.message}")

    errors = sum(finding.level == "ERROR" for finding in findings)
    warnings = sum(finding.level == "WARN" for finding in findings)
    print(f"Validation complete: {errors} error(s), {warnings} warning(s)")
    if errors or (args.fail_on_warnings and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
