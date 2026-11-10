#!/usr/bin/env python3
"""Confere contrato de versão do AXI. Não atribui validação científica."""
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from zipfile import ZipFile
import hashlib

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-(?:rc[1-9]\d*))?$")
PLATFORMS = {"chatgpt-web", "gemini-web", "grok-web", "claude-web",
             "codex", "antigravity", "grok-build-cli", "claude-code"}


def die(message):
    raise SystemExit("ERRO versão AXI: " + message)


def version_from_builder(text):
    found = re.search(r'(?m)^VERSION\s*=\s*["\']([^"\']+)["\']\s*$', text)
    if not found:
        die("scripts/build.py sem VERSION literal")
    return found.group(1)


def git(*args):
    completed = subprocess.run(["git", *args], cwd=ROOT, text=True,
                               capture_output=True, check=False)
    if completed.returncode:
        die("git " + " ".join(args) + ": " + completed.stderr.strip())
    return completed.stdout.strip()


def check_source():
    builder = (ROOT / "scripts/build.py").read_text(encoding="utf-8")
    skill = (ROOT / "skill/axipesquisa/SKILL.md").read_text(encoding="utf-8")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    version = version_from_builder(builder)
    if not SEMVER.fullmatch(version):
        die(f"formato inválido: {version}")
    found = re.search(r'(?m)^\s+version:\s*["\']?([^"\'\s]+)', skill)
    if not found or found.group(1) != version:
        die(f"Skill e build divergentes (build={version}, skill={found.group(1) if found else 'ausente'})")
    if not re.search(r"(?m)^##\s+v?" + re.escape(version) + r"(?:\s|$)", changelog):
        die(f"versão {version} ausente no CHANGELOG")
    tag = os.environ.get("GITHUB_REF_NAME", "") if os.environ.get("GITHUB_REF_TYPE") == "tag" else ""
    if tag:
        if tag != "v" + version:
            die(f"tag {tag} não corresponde à Skill {version}")
        if git("cat-file", "-t", "refs/tags/" + tag) != "tag":
            die(f"tag {tag} não é anotada")
    return version


def check_bump(version):
    # Compara apenas mudança de fontes que alteram o contrato da Skill.
    base = os.environ.get("GITHUB_BASE_REF", "")
    event = os.environ.get("GITHUB_EVENT_NAME", "")
    if event == "pull_request" and base:
        subprocess.run(["git", "fetch", "origin", base], cwd=ROOT, check=True,
                       capture_output=True, text=True)
        ref = git("merge-base", "HEAD", "origin/" + base)
    elif event == "push" and os.environ.get("GITHUB_REF_TYPE") == "branch":
        if not git("rev-list", "--parents", "-n", "1", "HEAD").count(" "):
            return
        ref = "HEAD^"
    else:
        return
    paths = git("diff", "--name-only", ref, "HEAD").splitlines()
    triggers = ("skill/axipesquisa/", "scripts/build.py")
    if not any(p.startswith(triggers) for p in paths):
        return
    prior = subprocess.run(["git", "show", f"{ref}:scripts/build.py"], cwd=ROOT,
                           capture_output=True, text=True, check=False)
    if prior.returncode:
        return
    old = version_from_builder(prior.stdout)
    def numeric(value):
        major, minor, patch = value.split("-", 1)[0].split(".")
        return tuple(map(int, (major, minor, patch)))
    if numeric(version) <= numeric(old) and version != old:
        die(f"versão retrocedeu: {old} -> {version}")
    if old == version:
        die(f"fontes da Skill alteradas sem incremento: {old}")


def check_dist(version):
    manifest_path = ROOT / "dist/manifest-sha256.json"
    if not manifest_path.is_file():
        die("manifesto de instalação ausente")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("version") != version:
        die("versão do manifesto divergente")
    entries = manifest.get("platforms", [])
    if len(entries) != 8 or {x.get("platform") for x in entries} != PLATFORMS:
        die("esperados oito instaladores distintos")
    for entry in entries:
        archive = ROOT / "dist" / entry["filename"]
        if not archive.is_file() or version not in archive.name:
            die(f"pacote ausente ou com versão incorreta: {archive}")
        data = archive.read_bytes()
        if hashlib.sha256(data).hexdigest() != entry["sha256"]:
            die(f"hash SHA256 divergente: {archive.name}")
        with ZipFile(archive) as z:
            if z.testzip() is not None:
                die(f"ZIP inválido: {archive.name}")
            candidates = [n for n in z.namelist() if n.endswith("/SKILL.md") or n == "SKILL.md"]
            if len(candidates) != 1:
                die(f"SKILL.md ausente ou duplicada: {archive.name}")
    print("AXI: oito instaladores e manifesto SHA256 verificados")


if __name__ == "__main__":
    v = check_source()
    if "--bump" in sys.argv:
        check_bump(v)
    if "--dist" in sys.argv:
        check_dist(v)
    print("AXI: versão consistente:", v)
