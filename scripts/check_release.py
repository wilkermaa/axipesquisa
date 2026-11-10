#!/usr/bin/env python3
"""Enforce AXI public source version parity and annotated git tag.

Never creates tags/pushes automatically. --git-tag validates real local Git.
"""
from __future__ import annotations
import argparse
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"\d+\.\d+\.\d+\Z")


def run_git(*args: str) -> str:
    result = subprocess.run(["git", "-C", str(ROOT), *args], text=True, capture_output=True)
    if result.returncode:
        raise AssertionError(f"Git command failed ({' '.join(args)}): {result.stderr.strip()}")
    return result.stdout.strip()


def version_tuple(value: str) -> tuple[int, int, int]:
    if not SEMVER.fullmatch(value):
        raise AssertionError(f"Non-SemVer public release version: {value!r}")
    return tuple(map(int, value.split('.')))


def check_source() -> str:
    version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
    version_tuple(version)
    build = (ROOT / 'scripts/build.py').read_text(encoding='utf-8')
    skill = (ROOT / 'skill/axipesquisa/SKILL.md').read_text(encoding='utf-8')
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    rafaell = (ROOT / 'docs/ENCAMINHAMENTO-RAFAELL.md').read_text(encoding='utf-8')
    contrib = (ROOT / 'CONTRIBUTING.md').read_text(encoding='utf-8')
    for label, condition in {
        'build.py': f'VERSION = "{version}"' in build,
        'frontmatter SKILL': f'version: "{version}"' in skill,
        'title SKILL': f'método AXI, versão {version}' in skill,
        'README current version': f'**Versão {version}' in readme,
        'Rafaell current version': f'a distribuição atual é {version}' in rafaell,
        'release notes': (ROOT/f'docs/RELEASE-v{version}.md').is_file(),
        'org policy': 'toda modificação' in (ROOT/'docs/POLITICA-ORGANIZACIONAL-VERSOES.md').read_text(encoding='utf-8').lower(),
        'contribution policy': 'tag anotada' in contrib,
        'release and method distinct': '2.2.0-rc2' in rafaell,
        'publication not falsely claimed': 'software experimental publicado' not in readme,
        'skill examples included': 'references/EXEMPLOS-E-TESTES.md' in skill,
        'installer in skill': (ROOT/'skill/axipesquisa/README-INSTALACAO.md').is_file(),
    }.items():
        if not condition:
            raise AssertionError(f'Release source policy failure: {label}')
    print(f'[PASS] source release parity v{version}')
    return version


def check_tag(version: str) -> None:
    tag = f'v{version}'
    kind = run_git('cat-file', '-t', f'refs/tags/{tag}')
    assert kind == 'tag', f'Release tag must be annotated, not lightweight: {tag}'
    commit = run_git('rev-parse', 'HEAD')
    tagged_commit = run_git('rev-parse', f'refs/tags/{tag}^{{commit}}')
    assert tagged_commit == commit, f'Tag {tag} points to {tagged_commit}, HEAD is {commit}'
    assert run_git('status', '--porcelain') == '', 'Tagged release working tree is dirty'
    print(f'[PASS] local annotated git tag {tag} at {commit}')


def compare_base(base: str, version: str) -> None:
    base_ver = run_git('show', f'{base}:VERSION').strip()
    assert version_tuple(version) > version_tuple(base_ver), (
        f'Every change merged to main needs a new version: {version} not greater than {base_ver}')
    print(f'[PASS] proposed version v{version} > base v{base_ver}')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', action='store_true', help='check metadata parity (default)')
    parser.add_argument('--git-tag', action='store_true', help='verify annotated vX.Y.Z tag at HEAD')
    parser.add_argument('--compare-base', metavar='GIT_REF', help='verify PR version increases from base')
    args = parser.parse_args()
    version = check_source()
    if args.compare_base:
        compare_base(args.compare_base, version)
    if args.git_tag:
        check_tag(version)

if __name__ == '__main__':
    main()
