#!/usr/bin/env python3
"""Check that the library is internally consistent. Exit 1 on any error.

Checks:
  1. Every skill folder has SKILL.md and README.md.
  2. SKILL.md starts with YAML frontmatter whose `name` equals the folder name
     and which has a non-empty `description`.
  3. No folder for a skill that POLICY.md says must never be published.
  4. Every manifest.json `slug` matches its folder and `source_sha256` matches
     the SKILL.md bytes.
  5. library.json lists only real folders, uses known categories and statuses.
     A folder missing from library.json is a WARNING (new publishes land first).
  6. Every relative Markdown link in the repo resolves to a file or folder.
  7. README.md index is up to date (scripts/build_index.py --check).
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEVER_PUBLISH = {"illustrated-decodable-story-maker"}  # POLICY.md
STATUSES = {"hosted", "spec"}

errors: list[str] = []
warnings: list[str] = []


def frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    out = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip("\"'")
    return out


def check_skills() -> list[str]:
    slugs = []
    for d in sorted((ROOT / "skills").iterdir()):
        if not d.is_dir():
            continue
        slug = d.name
        slugs.append(slug)
        if slug in NEVER_PUBLISH:
            errors.append(f"{slug}: POLICY.md forbids publishing this skill")
        for f in ("SKILL.md", "README.md"):
            if not (d / f).is_file():
                errors.append(f"{slug}: missing {f}")
        if not (d / "SKILL.md").is_file():
            continue
        raw = (d / "SKILL.md").read_bytes()
        fm = frontmatter(raw.decode("utf-8"))
        if fm is None:
            errors.append(f"{slug}: SKILL.md has no frontmatter")
        else:
            if fm.get("name") != slug:
                errors.append(f"{slug}: frontmatter name {fm.get('name')!r} != folder")
            if not fm.get("description"):
                errors.append(f"{slug}: empty description")
        mpath = d / "manifest.json"
        if mpath.is_file():
            m = json.loads(mpath.read_text(encoding="utf-8"))
            if m.get("slug") != slug:
                errors.append(f"{slug}: manifest slug {m.get('slug')!r} != folder")
            if m.get("source_sha256") != hashlib.sha256(raw).hexdigest():
                errors.append(f"{slug}: manifest source_sha256 does not match SKILL.md")
    return slugs


def check_library(slugs: list[str]) -> None:
    lib = json.loads((ROOT / "library.json").read_text(encoding="utf-8"))
    cats = {c["id"] for c in lib["categories"]}
    for slug, meta in lib["skills"].items():
        if slug not in slugs:
            errors.append(f"library.json: {slug} has no folder")
        if meta.get("category") not in cats:
            errors.append(f"library.json: {slug} has unknown category {meta.get('category')!r}")
        if meta.get("status") not in STATUSES:
            errors.append(f"library.json: {slug} has unknown status {meta.get('status')!r}")
    for slug in slugs:
        if slug not in lib["skills"]:
            warnings.append(f"library.json: {slug} not categorised yet")


LINK = re.compile(r"\]\(([^)\s]+)\)")


def check_links() -> None:
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        for target in LINK.findall(md.read_text(encoding="utf-8")):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            path = target.split("#", 1)[0]
            if not path:
                continue
            if not (md.parent / path).resolve().exists():
                errors.append(f"{md.relative_to(ROOT)}: broken link {target}")


def main() -> int:
    slugs = check_skills()
    check_library(slugs)
    check_links()
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_index.py"), "--check"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        errors.append(r.stderr.strip() or "README index check failed")
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    verdict = "PASS" if not errors else "FAIL"
    print(f"VERDICT {verdict}: {len(slugs)} skills, {len(errors)} errors, {len(warnings)} warnings")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
