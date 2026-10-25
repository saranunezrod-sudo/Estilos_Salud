"""Genera README.md a partir de prompts/ y templates/README_*.md.
Uso: python3 -I scripts/build_readme.py
"""
import sys
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from prompts_lib import ROOT  # noqa: E402
from prompts_lib import all_prompt_files  # noqa: E402
from prompts_lib import parse_prompt_file  # noqa: E402
from prompts_lib import slug_anchor  # noqa: E402


IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}


def main():
    entries = []
    for path in all_prompt_files():
        meta, prompt, notes = parse_prompt_file(path)
        entries.append((path, meta, prompt, notes))

    categories = {}
    for entry in entries:
        categories.setdefault(entry[1]["category"], []).append(entry)

    out = [(ROOT / "templates" / "README_HEAD.md").read_text(encoding="utf-8").rstrip(), ""]
    out.append("## Índice\n")
    for cat in sorted(categories):
        out.append(f"### {cat}")
        for _, meta, _, _ in categories[cat]:
            out.append(f"- [{meta['title']}](#{slug_anchor(meta['title'])})")
        out.append("")

    for cat in sorted(categories):
        out.append(f"## {cat}\n")
        for path, meta, prompt, _ in categories[cat]:
            out.append(f"### {meta['title']}\n")
            out.append(f"{meta['audience']}\n")
            images = sorted(
                p for p in (ROOT / "images" / path.stem).glob("*")
                if p.suffix.lower() in IMAGE_EXTS
            )
            if images:
                out.append(" ".join(
                    f'<img src="images/{path.stem}/{quote(p.name)}" width="320" alt="Ejemplo {n} de {meta["title"]}">'
                    for n, p in enumerate(images, 1)
                ))
                out.append("\n*Imágenes orientativas: al usar IA generativa, el resultado puede variar entre generaciones, según tus fuentes y con las actualizaciones de NotebookLM.*\n")
            out.append("```yaml")
            out.append(prompt)
            out.append("```")
            out.append(f"*Archivo: [{path.name}](prompts/{path.name}) · "
                       f"Inspirado en: {meta['inspired_by']} · Adaptación: {meta['author']}*\n")

    out.append((ROOT / "templates" / "README_FOOT.md").read_text(encoding="utf-8").rstrip())
    (ROOT / "README.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"README.md generado con {len(entries)} estilos")


if __name__ == "__main__":
    main()
