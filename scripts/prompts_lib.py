"""Utilidades compartidas para leer los archivos de prompts/."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "prompts"
FENCE = "```"


def parse_prompt_file(path):
    """Devuelve (meta, prompt, notas) de un archivo de estilo."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        raise ValueError("falta el front matter (--- ... ---)")
    meta = {}
    for line in m.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep:
            meta[key.strip()] = value.strip()
    body = m.group(2)
    start = body.find(FENCE)
    if start == -1:
        raise ValueError("falta el bloque de código con el prompt")
    start = body.index("\n", start) + 1
    end = body.find("\n" + FENCE, start)
    if end == -1:
        raise ValueError("bloque de código sin cerrar")
    prompt = body[start:end]
    notes = body[end + len(FENCE) + 1:].strip()
    return meta, prompt, notes


def all_prompt_files():
    return sorted(PROMPTS_DIR.glob("[0-9][0-9]-*.md"))


def slug_anchor(title):
    """Ancla estilo GitHub para un título."""
    s = title.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s+", "-", s.strip())
