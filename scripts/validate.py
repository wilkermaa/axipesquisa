#!/usr/bin/env python3
"""Static source/ZIP security gate; not a test of model behavior."""
import json
import re
import sys
from pathlib import Path
from zipfile import ZipFile

try:
    import yaml
except ImportError:
    print("PyYAML ausente: pip install -r requirements-dev.txt", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "axipesquisa"
ALLOW_SUFFIX = {".md", ".json"}
EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
IDENTITY_EXCEPTIONS = set()  # Public skill should not contain any real addresses.
REQUIRED = ["Análise", "eXpansão", "Integração", "Fontes consultadas (ABNT)",
            "◌ AXI", "prompt injection", "JSON", "PNL"]


def frontmatter(path):
    text = path.read_text("utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise AssertionError("Missing YAML frontmatter")
    block = text.split("\n---\n", 1)[0][4:]
    data = yaml.safe_load(block)
    assert isinstance(data, dict), "Not a YAML mapping"
    assert data.get("name") == path.parent.name == "axipesquisa"
    assert len(data["name"]) <= 64 and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",data["name"])
    assert isinstance(data.get("description"),str) and 1 <= len(data["description"]) <= 1024
    return text, data


def check_skill():
    content, info = frontmatter(SKILL / "SKILL.md")
    for word in REQUIRED:
        assert word.casefold() in content.casefold(), f"Missing core concept: {word}"
    members = [p for p in SKILL.rglob('*') if p.is_file()]
    assert members and len(members) <= 30
    for p in members:
        assert p.is_relative_to(SKILL) and not p.is_symlink()
        assert p.suffix.lower() in ALLOW_SUFFIX, f"Unexpected skill extension: {p.name}"
        assert p.stat().st_size < 90000, f"Excessive skill asset size: {p.name}"
        contents = p.read_text('utf-8')
        found = set(EMAIL_PATTERN.findall(contents)) - IDENTITY_EXCEPTIONS
        assert not found, f"Personal email or contact in public skill {p.name}: {found}"
    ref_files = re.findall(r'`((?:references|assets)/[\w.\-/]+)`', content)
    for rel in ref_files:
        assert (SKILL / rel).is_file(), f"Dangling skill reference: {rel}"
    assert "não validada" in content.casefold() or "não validado" in content.casefold()
    return info


def check_zip(zip_path):
    with ZipFile(zip_path) as z:
        names=z.namelist()
        assert names and len(names) == len(set(names)), f"Duplicates: {zip_path}"
        assert z.testzip() is None, f"Corrupted: {zip_path}"
        for i in z.infolist():
            n=i.filename
            parts=Path(n).parts
            assert not n.startswith('/') and '..' not in parts and '\\' not in n
            assert not ((i.external_attr >> 16) & 0o170000) == 0o120000, f"Symlink in {zip_path}"
            assert i.file_size < 200_000
            assert i.compress_size == 0 or i.file_size / max(1,i.compress_size) < 150
        expected=[n for n in names if n.endswith('/SKILL.md') or n=='SKILL.md']
        assert len(expected)==1, (zip_path,expected)
        assert z.read(expected[0]).startswith(b'---\n')


def main():
    info = check_skill()
    cases=json.loads((ROOT/'tests/cases.json').read_text('utf-8'))
    assert len(cases) >= 24 and len(set(x['id'] for x in cases)) == len(cases)
    required_fields={'id','category','prompt','expected'}
    assert all(required_fields <= c.keys() for c in cases)
    zips=list((ROOT/'dist').glob('axipesquisa-*.zip'))
    if zips:
        assert len(zips)==8, f"Eight platform zips expected, found {len(zips)}"
        for path in zips: check_zip(path)
    plugin_zips=list((ROOT/'dist').glob('AXI-ChatGPT-Plugin-*.zip'))
    assert len(plugin_zips) <= 1
    for plugin_zip in plugin_zips:
        check_zip(plugin_zip)
        with ZipFile(plugin_zip) as z:
            assert 'plugin.json' in z.namelist()
            manifest=json.loads(z.read('plugin.json'))
            assert manifest['name']=='axipesquisa'
            assert manifest['$schema']=='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
            assert 'license' not in manifest, 'Do not invent license grant'
            assert 'skills/axipesquisa/SKILL.md' in z.namelist()
    print(json.dumps({'status':'passed-static-only','skill':info['name'],
                      'files':len(list(SKILL.rglob('*'))),'cases_defined':len(cases),
                      'platform_packages_checked':len(zips), 'plugin_candidates_checked':len(plugin_zips)},indent=2))

if __name__=='__main__':main()
