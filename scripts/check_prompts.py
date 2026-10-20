"""Valida los prompts de prompts/. Uso: python3 -I scripts/check_prompts.py"""
import re
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from prompts_lib import all_prompt_files  # noqa: E402
from prompts_lib import parse_prompt_file  # noqa: E402

REQUIRED_META = ["title", "category", "format", "audience", "status", "author", "inspired_by"]
VALID_STATUS = {"sin probar", "probado"}
LANG_CLAUSE = "the language should be what users said in the prompt"
LANG_CLAUSE_ALT = "the language what users requested in the prompt"


def check(path):
    errors = []
    try:
        meta, prompt, _ = parse_prompt_file(path)
    except ValueError as e:
        return [str(e)]
    for key in REQUIRED_META:
        if not meta.get(key):
            errors.append(f"front matter: falta '{key}'")
    if meta.get("format") != "design_system":
        errors.append("front matter: 'format' debe ser 'design_system'")
    if meta.get("status") not in VALID_STATUS:
        errors.append(f"front matter: 'status' debe ser uno de {sorted(VALID_STATUS)}")
    low = prompt.lower()
    if LANG_CLAUSE not in low and LANG_CLAUSE_ALT not in low:
        errors.append(f"falta la cláusula de idioma: '{LANG_CLAUSE}'")
    if "invent" not in low:
        errors.append("falta el bloque sanitario 'Content Fidelity' (no inventar datos)")
    if "real patient" not in low:
        errors.append("falta el bloque sanitario 'Safety' (sin datos de pacientes)")
    for block in ("design_system:", "global_style:", "typography:", "color_palette:",
                  "key_visual_elements:", "slide_layout_templates:", "healthcare_rules:"):
        if block not in prompt:
            errors.append(f"falta el bloque '{block}'")
    if re.search(r"\b\d+\s?(mg|mcg|µg|ml|UI|IU)\b", prompt):
        errors.append("contiene una cantidad con unidad de dosis (mg/ml/UI...): no incluyas dosis")
    for h in re.findall(r"#[0-9A-Fa-f]+", prompt):
        if len(h) - 1 not in (3, 6, 8) and not re.fullmatch(r"#\d+", h):
            errors.append(f"código de color dudoso: {h}")
    return errors


def main():
    files = all_prompt_files()
    if not files:
        print("No hay prompts en prompts/")
        return 1
    failed = 0
    seen = set()
    for path in files:
        errs = check(path)
        prefix = path.name[:2]
        if prefix in seen:
            errs.append("número de archivo duplicado")
        seen.add(prefix)
        if errs:
            failed += 1
            print(f"FALLO {path.name}")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"ok    {path.name}")
    print(f"\n{len(files) - failed}/{len(files)} correctos")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
