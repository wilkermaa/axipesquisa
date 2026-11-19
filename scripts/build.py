#!/usr/bin/env python3
"""Deterministic, data-only AXI skill packager. No network or executable skill code."""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "axipesquisa"
DIST = ROOT / "dist"
VERSION = "2.3.8"

PLATFORMS = {
    "chatgpt-web": "axipesquisa/",
    "gemini-web": "",
    "grok-web": "",
    "claude-web": "axipesquisa/",
    "codex": ".agents/skills/axipesquisa/",
    "antigravity": ".agents/skills/axipesquisa/",
    "grok-build-cli": ".grok/skills/axipesquisa/",
    "claude-code": ".claude/skills/axipesquisa/",
}


PLATFORM_GUIDES = {
    "chatgpt-web": ("ChatGPT Web", "Mermaid renderizado em Prévia, não apenas código `flowchart TD`.", "references/CHATGPT-DIAGRAMAS.md"),
    "gemini-web": ("Gemini Web", "IMAGEM VISÍVEL OBRIGATÓRIA na microfase I quando houver fluxo fiel. Solicitar/acionar a geração DIRETA DE IMAGEM do Gemini (PNG ou SVG já desenhado), exibir na própria conversa e conferir blocos, setas e rótulos. Não substituir por tabela, ASCII, Mermaid puro, HTML/app interativo ou arquivo sem prévia. Canvas com SVG é apenas fallback quando gerar realmente imagem visível, sem presumir compatibilidade Skill+Canvas. Se não houver figura exibida, marcar entrega parcial; nunca declarar concluído.", "references/GEMINI-DIAGRAMAS.md"),
    "claude-web": ("Claude Web", "Visual personalizado HTML/SVG inline, com Artifact renderizado como alternativa.", "references/CLAUDE-DIAGRAMAS.md"),
    "grok-web": ("Grok Web", "Arquivo SVG com cartão de prévia inline; HTML Preview em Projects como alternativa.", "references/GROK-DIAGRAMAS.md"),
    "codex": ("Codex CLI/IDE", "Renderer Mermaid/visual local realmente disponível, com prévia ou arquivo real.", "references/PLATAFORMAS-VISUAIS.md"),
    "claude-code": ("Claude Code", "HTML/SVG local em prévia da IDE ou arquivo visual válido.", "references/PLATAFORMAS-VISUAIS.md"),
    "antigravity": ("Antigravity", "Mermaid/SVG em prévia de IDE ou arquivo visual realmente criado.", "references/PLATAFORMAS-VISUAIS.md"),
    "grok-build-cli": ("Grok Build CLI", "Mermaid renderizado em visualização real ou SVG em renderer local.", "references/PLATAFORMAS-VISUAIS.md"),
}

def platform_guide(platform):
    name, route, reference = PLATFORM_GUIDES[platform]
    return (f'# AXI-Pesquisa {VERSION} — {name}\n\n' 
            f'**Rota visual específica desta instalação:** {route}\n\n'
            '**Leitura integral obrigatória:** comece por `SKILL.md` completo; continue um arquivo por vez, de A até X e I, conforme `references/FLUXO-LEITURA-INTEGRAL.md`. '
            'Todas as respostas explicativas ou de pesquisa devem registrar `Fontes consultadas (ABNT)` e fontes efetivamente consultadas ou ausência de consulta.\n\n'
            f'**Manual da plataforma:** `{reference}`. '
            '**Critério de aceite:** fluxo representável exige IMAGEM renderizada na tela ou em prévia; arquivo não aberto, tabela, ASCII, HTML, código ou só promessa não bastam. A instrução não prova execução, testar e registrar o estado real. PDF não obrigatório.\n').encode('utf-8')

def info(name):


    assert not name.startswith("/") and ".." not in Path(name).parts
    zi = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    zi.create_system = 3
    zi.external_attr = (0o100644 << 16)  # regular file; no symlink/executable flag
    zi.compress_type = ZIP_DEFLATED
    return zi


def write_zip(dest, members):
    dest.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(dest, "w", compression=ZIP_DEFLATED, compresslevel=9) as z:
        for arc, data in sorted(members.items()):
            if arc.startswith("/") or ".." in Path(arc).parts or "\\" in arc:
                raise ValueError(f"unsafe archive path: {arc}")
            z.writestr(info(arc), data, compress_type=ZIP_DEFLATED, compresslevel=9)
    with ZipFile(dest) as z:
        if z.testzip() is not None:
            raise AssertionError(f"Corrupt ZIP: {dest}")
    return {"filename": dest.name, "bytes": dest.stat().st_size,
            "sha256": hashlib.sha256(dest.read_bytes()).hexdigest(),
            "entries": len(members)}


def build():
    source_files = sorted(p for p in SKILL.rglob("*") if p.is_file())
    assert source_files and (SKILL / "SKILL.md").is_file()
    for p in source_files:
        assert p.suffix in (".md", ".json")
        assert not p.is_symlink()
    outputs = []
    for platform, prefix in PLATFORMS.items():
        members = {prefix + p.relative_to(SKILL).as_posix(): p.read_bytes() for p in source_files}
        members[prefix + "INSTALADOR-PLATAFORMA.md"] = platform_guide(platform)
        dest = DIST / f"axipesquisa-{VERSION}-{platform}.zip"
        outputs.append({"platform": platform, **write_zip(dest, members)})
    # Independent portable ChatGPT plugin candidate. Not an approved directory listing.
    # License scope is documented in LICENSE and LICENSE-CONTENT.md; do not assume manifest license field is accepted by provider.
    plugin = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": "axipesquisa", "version": VERSION,
        "description": "Fluxo de pesquisa e explicação AXI: análise de partes, comparações críticas e integração prática."
    }
    plugin_members={"plugin.json":(json.dumps(plugin,ensure_ascii=False,indent=2)+"\n").encode()}
    plugin_members.update({"skills/axipesquisa/"+p.relative_to(SKILL).as_posix(): p.read_bytes() for p in source_files})
    plugin_path=DIST/f"AXI-ChatGPT-Plugin-v{VERSION}.zip"
    plugin_result=write_zip(plugin_path,plugin_members)
    manifest = {"project":"axipesquisa", "version":VERSION,
                "chatgpt_plugin_candidate":plugin_result,
                "note":"Static integrity only; no model/web-product acceptance tests.",
                "platforms":outputs}
    manifest_bytes = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    (DIST / "manifest-sha256.json").write_bytes(manifest_bytes)

    # Single public GitHub upload-ready repository snapshot, plus per-platform releases.
    members = {}
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.is_symlink():
            continue
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(".git/") or "/__pycache__/" in rel or rel.endswith(".pyc"):
            continue
        if rel.startswith("dist/") and not (rel.startswith("dist/axipesquisa-") and rel.endswith(".zip") or rel.startswith("dist/AXI-ChatGPT-Plugin-") or rel=="dist/manifest-sha256.json"):
            continue
        if p.name.startswith("config.local") or p.name.startswith(".env"):
            continue
        members[f"axipesquisa-v{VERSION}/{rel}"] = p.read_bytes()
    result = write_zip(DIST / f"AXI-Pesquisa-v{VERSION}-GitHub.zip", members)
    print(json.dumps({"platforms":outputs,"repository":result},indent=2,ensure_ascii=False))
    return manifest

if __name__ == "__main__":
    build()
