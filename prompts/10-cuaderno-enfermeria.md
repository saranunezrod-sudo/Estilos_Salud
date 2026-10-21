---
title: Cuaderno de Enfermería
category: D. Retro y creativos
format: design_system
audience: Apuntes, resúmenes de estudio, formación y sesiones con aspecto de cuaderno
author: Mantenedores del repositorio
inspired_by: Neo-Retro Dev Deck / Pixel-Infographic Editorial (awesome-notebookLM-prompts)
---

# Cuaderno de Enfermería

**Ideal para:** resúmenes tipo apuntes sobre papel cuadriculado o pautado, con bloques de color, iconos pixel-art médicos y tono directo.

```
design_system:
  global_style:
    theme: "Neo-retro health notebook. Annotated study notes, controlled imperfection, assembled not aligned."
    typography:
      primary_heading: "Bold heavy slightly condensed geometric sans-serif"
      secondary_heading: "Marker handwriting for margin notes"
      body_text: "Medium sans-serif captions"
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "#FBF6E6 cream grid paper with a red margin line"
      text_main: "#111111"
      primary_color: "#00A19B"
      secondary: "#FFE14D"
      tertiary: "#5BC0EB"
      alert: "#FF6F91"
      borders: "thick black outlines"
    key_visual_elements:
      - "Stacked blocks with thick black borders and slight overlaps"
      - "Sticky notes and tape on corners"
      - "8-bit pixel icons: syringe, pill, heart pulse, stethoscope, cross"
      - "Arrows, chevrons and pixel sparks"

slide_layout_templates:
  - type: "Notebook_Cover"
    usage: "Huge title block on grid paper with sticky notes"
  - type: "Mechanism_Layers"
    usage: "Stacked colored layers with icon, title and one line"
  - type: "Steps_Procedure"
    usage: "Left-to-right boxes, last step larger"
  - type: "Mnemonic_Cheat_Sheet"
    usage: "Big acronym in a boxed frame, meaning per letter"
  - type: "Red_Flags"
    usage: "Coral blocks with warning list exactly as in the sources"

avoid: "gradients, realistic photos, soft shadows, corporate templates"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

## Notas de uso
- Variante pautada: cambia en el fondo "grid paper" por "ruled lines paper".
- Añade tus ejemplos reales en `images/10-cuaderno-enfermeria/` y ejecuta `python3 -I scripts/build_readme.py`.

> 🖼️ Las imágenes de `images/10-cuaderno-enfermeria/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
