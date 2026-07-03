#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///

# --- How to run ---
# python3 scripts/validate_plugin.py
# uv run scripts/validate_plugin.py

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Final, NamedTuple, TypedDict


ROOT: Final = Path(__file__).resolve().parents[1]
REQUIRED_FILES: Final = (
    ".codex-plugin/plugin.json",
    "skills/hello-ralphthon-icml/SKILL.md",
    "commands/hello-ralphthon-icml.md",
    "README.md",
)
PLUGIN_FIELDS: Final = (
    "name",
    "version",
    "description",
    "homepage",
    "repository",
    "license",
    "keywords",
    "skills",
    "interface",
)
SKILL_FIELDS: Final = ("name", "description", "metadata")
SKILL_METADATA_FIELDS: Final = ("priority", "docs", "pathPatterns", "promptSignals")
COMMAND_FIELDS: Final = ("description",)


class PluginManifest(TypedDict):
    name: str
    version: str
    description: str
    homepage: str
    repository: str
    license: str
    keywords: list[str]
    skills: str
    interface: dict[str, str | list[str]]


class ValidationError(NamedTuple):
    path: Path
    message: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def add_error(errors: list[ValidationError], relative_path: str, message: str) -> None:
    errors.append(ValidationError(path=Path(relative_path), message=message))


def frontmatter(text: str) -> list[str]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return []

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return lines[1:index]

    return []


def top_level_keys(lines: list[str]) -> set[str]:
    keys: set[str] = set()
    for line in lines:
        if not line or line.startswith(" ") or ":" not in line:
            continue
        key = line.split(":", maxsplit=1)[0].strip()
        if key:
            keys.add(key)
    return keys


def nested_keys(lines: list[str], parent: str) -> set[str]:
    keys: set[str] = set()
    in_parent = False
    for line in lines:
        if not line.strip():
            continue
        if not line.startswith(" "):
            in_parent = line.strip() == f"{parent}:"
            continue
        if in_parent and line.startswith("  ") and not line.startswith("    ") and ":" in line:
            key = line.split(":", maxsplit=1)[0].strip()
            if key:
                keys.add(key)
    return keys


def load_manifest(path: Path) -> PluginManifest | None:
    try:
        raw = json.loads(read_text(path))
    except json.JSONDecodeError as error:
        raise RuntimeError(f"invalid JSON: {error}") from error

    return raw


def validate_required_files(errors: list[ValidationError]) -> None:
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            add_error(errors, relative_path, "required file is missing")


def validate_plugin_manifest(errors: list[ValidationError]) -> None:
    relative_path = ".codex-plugin/plugin.json"
    path = ROOT / relative_path
    if not path.is_file():
        return

    try:
        manifest = load_manifest(path)
    except RuntimeError as error:
        add_error(errors, relative_path, str(error))
        return

    if manifest is None:
        add_error(errors, relative_path, "manifest is empty")
        return

    for field in PLUGIN_FIELDS:
        if field not in manifest:
            add_error(errors, relative_path, f"missing field: {field}")

    if manifest.get("name") != "ralphthon-icml":
        add_error(errors, relative_path, "name must be ralphthon-icml")
    if manifest.get("skills") != "./skills/":
        add_error(errors, relative_path, "skills must point to ./skills/")
    if not manifest.get("keywords"):
        add_error(errors, relative_path, "keywords must not be empty")
    if "commands" in manifest:
        add_error(errors, relative_path, "commands should be discovered from commands/, not plugin.json")


def validate_skill_frontmatter(errors: list[ValidationError]) -> None:
    relative_path = "skills/hello-ralphthon-icml/SKILL.md"
    path = ROOT / relative_path
    if not path.is_file():
        return

    lines = frontmatter(read_text(path))
    if not lines:
        add_error(errors, relative_path, "frontmatter is missing")
        return

    keys = top_level_keys(lines)
    metadata = nested_keys(lines, "metadata")
    for field in SKILL_FIELDS:
        if field not in keys:
            add_error(errors, relative_path, f"missing frontmatter field: {field}")
    for field in SKILL_METADATA_FIELDS:
        if field not in metadata:
            add_error(errors, relative_path, f"missing metadata field: {field}")


def validate_command_frontmatter(errors: list[ValidationError]) -> None:
    relative_path = "commands/hello-ralphthon-icml.md"
    path = ROOT / relative_path
    if not path.is_file():
        return

    text = read_text(path)
    lines = frontmatter(text)
    if not lines:
        add_error(errors, relative_path, "frontmatter is missing")
        return

    keys = top_level_keys(lines)
    for field in COMMAND_FIELDS:
        if field not in keys:
            add_error(errors, relative_path, f"missing frontmatter field: {field}")

    for heading in ("Preflight", "Plan", "Commands", "Verification", "Summary", "Next Steps"):
        if f"## {heading}" not in text:
            add_error(errors, relative_path, f"missing section: {heading}")


def main() -> int:
    errors: list[ValidationError] = []
    validate_required_files(errors)
    validate_plugin_manifest(errors)
    validate_skill_frontmatter(errors)
    validate_command_frontmatter(errors)

    if errors:
        print("Validation failed")
        for error in errors:
            print(f"- {error.path}: {error.message}")
        return 1

    print("Validation passed")
    print(f"- plugin: {ROOT.name}")
    print(f"- checked files: {len(REQUIRED_FILES)}")
    print("- skill: hello-ralphthon-icml")
    print("- command: /hello-ralphthon-icml")
    return 0


if __name__ == "__main__":
    sys.exit(main())
