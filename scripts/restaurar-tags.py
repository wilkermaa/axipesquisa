#!/usr/bin/env python3
"""Restaura snapshots reais em commits e tags, mantendo acervo-drive intocado."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

REPO = Path(os.getenv('GITHUB_WORKSPACE') or os.getcwd()).resolve()
SOURCE_ROOT = REPO / 'versoes'
EXPECTED_ARCHIVE = '902d3ad5cf9d97d4cfdd04f20b26a96a61fd9d1d'
VERSIONS = [
    ('v1.0', 'docs', 'v1.0/documentacao', ''),
    ('v2.0.0', 'zip', 'v2.0.0/pacotes/axipesquisa-v2-completo.zip', ''),
    ('v2.1.0-rc1', 'docs', 'v2.1.0-rc1', ''),
    ('v2.2.0-rc2', 'zip', 'v2.2.0-rc2/pacotes/AXI-Pesquisa-v2.2.0-rc2-GitHub.zip', 'axipesquisa-v2.2.0-rc2'),
    ('v2.2.0-rc3', 'zip', 'v2.2.0-rc3/pacotes/AXI-Pesquisa-v2.2.0-rc3-GitHub.zip', 'axipesquisa-v2.2.0-rc3'),
    ('v2.2.0-rc4', 'zip', 'v2.2.0-rc4/pacotes/AXI-PESQUISA-v2.2.0-rc4-GITHUB.zip', 'axipesquisa-v2.2.0-rc4'),
    ('v2.2.1', 'zip', 'v2.2.1/pacotes/AXI-PESQUISA-v2.2.1-CODIGO-PARA-GITHUB.zip', ''),
    ('v2.2.2', 'zip', 'v2.2.2/pacotes/AXI-PESQUISA-v2.2.2-CODIGO-PARA-GITHUB.zip', ''),
]

def git(*args: str) -> str:
    cp = subprocess.run(['git', '-C', str(REPO), *args], text=True, capture_output=True)
    if cp.returncode:
        raise RuntimeError(f"Git failed: {' '.join(args)}\n{cp.stderr}\n{cp.stdout}")
    return cp.stdout.strip()

def unzip_safe(archive: Path, root: Path, strip_prefix: str) -> None:
    with zipfile.ZipFile(archive) as z:
        for info in z.infolist():
            p = PurePosixPath(info.filename)
            if p.is_absolute() or '..' in p.parts or '\\' in info.filename:
                raise ValueError(f'Unsafe ZIP path: {info.filename}')
            if (info.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError(f'Symlinks not permitted: {info.filename}')
            pieces = list(p.parts)
            if strip_prefix:
                if not pieces or pieces[0] != strip_prefix:
                    raise ValueError(f'Unexpected ZIP root: {info.filename}')
                pieces = pieces[1:]
            if not pieces or info.is_dir():
                continue
            out = root.joinpath(*pieces)
            out.parent.mkdir(parents=True, exist_ok=True)
            with z.open(info) as inp, out.open('wb') as fp:
                shutil.copyfileobj(inp, fp)
            if ((info.external_attr >> 16) & 0o777) & 0o111:
                out.chmod(0o755)

def main() -> None:
    if git('rev-parse', '--abbrev-ref', 'HEAD') != 'main':
        raise RuntimeError('Execute apenas a partir da main')
    if git('rev-parse', 'refs/remotes/origin/acervo-drive') != EXPECTED_ARCHIVE:
        raise RuntimeError('Branch de arquivo mudou; operacao cancelada')
    if not SOURCE_ROOT.exists():
        raise RuntimeError('Acervo de origem ausente')
    collision = set(git('tag', '--list').splitlines()) & {v for v, *_ in VERSIONS}
    if collision:
        raise RuntimeError(f'Tags existentes nao serao sobrescritas: {collision}')

    backup = Path(tempfile.mkdtemp(prefix='axi-drive-history-'))
    shutil.copytree(SOURCE_ROOT, backup / 'versoes')
    tree = backup / 'versoes'
    git('config', 'user.name', 'github-actions[bot]')
    git('config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
    git('switch', '-c', 'restauracao-temporaria')

    for version, typ, relative, prefix in VERSIONS:
        git('rm', '-rf', '-q', '--', '.')
        git('clean', '-fdx', '-q')
        source = tree / relative
        if typ == 'zip':
            unzip_safe(source, REPO, prefix)
        else:
            dest = REPO / 'docs' / 'acervo-parcial'
            dest.mkdir(parents=True, exist_ok=True)
            for file in source.glob('*.md'):
                shutil.copy2(file, dest / file.name)
            (REPO / 'README.md').write_text(
                f'# AXI Pesquisa {version} — registro documental parcial\n\n'
                'Os documentos disponiveis desta versao foram preservados como registro historico. '
                '**Nao foi localizada distribuicao instalavel completa no acervo desta versao**. '
                'Esta tag nao deve ser tratada como release funcional validada.\n', encoding='utf-8')
        git('add', '-A')
        if not git('diff', '--cached', '--name-only'):
            raise RuntimeError(f'Snapshot vazio: {version}')
        git('commit', '-m', f'release: restaurar snapshot AXI {version} do Drive')
        git('tag', '-a', version, '-m', f'AXI Pesquisa {version} - snapshot Drive 10/11/2026')
        print(f'CREATED {version} {git("rev-parse", "HEAD")}', flush=True)

    git('push', '--atomic', 'origin', 'HEAD:refs/heads/main', '--follow-tags')
    print('PUSH_COMPLETE', flush=True)

    if shutil.which('gh') and os.getenv('GH_TOKEN'):
        for version, typ, _relative, _prefix in VERSIONS:
            note = 'Snapshot historico restaurado do Google Drive. Metodo experimental; eficacia cientifica independente nao demonstrada.'
            if typ == 'docs':
                note += '\n\nRegistro documental parcial: nao corresponde a uma distribuicao instalavel completa.'
            cmd = ['gh', 'release', 'create', version, '--verify-tag',
                   '--repo', 'wilkermaa/axipesquisa', '--title', f'AXI Pesquisa {version}', '--notes', note]
            if 'rc' in version or typ == 'docs':
                cmd.append('--prerelease')
            if version == 'v2.2.2':
                cmd.append('--latest')
                cmd.extend(str(p) for p in sorted((tree / 'v2.2.2' / 'instaladores').glob('*.zip')))
            result = subprocess.run(cmd, text=True, capture_output=True)
            if result.returncode:
                print(f'RELEASE_PENDING {version}: {result.stderr}', file=sys.stderr)
            else:
                print(f'RELEASE_CREATED {version}', flush=True)

if __name__ == '__main__':
    main()
