---
title: Boletín Sanitario
category: A. Clínico y profesional
format: design_system
audience: Novedades, alertas y resúmenes para equipos sanitarios y sesiones internas de farmacia u hospital
author: Mantenedores del repositorio
inspired_by: Modern Newspaper (https://x.com/mmmiyama_D/status/1998528702150488069) vía awesome-notebookLM-prompts
---

# Boletín Sanitario

**Ideal para:** novedades terapéuticas, alertas de seguridad y resúmenes de guías con aspecto de medio de salud moderno.

```
design_system:
  global_style:
    theme: "Modern health newspaper. Smart pop health news, clinical rigor x readability. 1 slide = 1 message."
    typography:
      primary_heading: "Extra-bold sans-serif, ultra-massive (30-50% of the slide), short 2-5 word headlines"
      secondary_heading: "Ultra-thin English sans-serif in the gaps"
      body_text: "Small clean sans-serif, headline-to-body ratio 10:1 or more. No markdown symbols in slide text"
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "#FFFFFF or cool gray #F5F5F5"
      text_main: "#111111"
      primary_color: "#00A19B"
      accent_color: "#E5322D"
      highlight: "#FFE14D marker lines behind key numbers"
    key_visual_elements:
      - "Asymmetric Swiss grid, title far top-left or bottom-left"
      - "Monochrome cutouts of healthcare professionals"
      - "Clean photos of medicines and devices on blown-out backgrounds"
      - "Fluorescent marker highlights"

slide_layout_templates:
  - type: "Asymmetric_Cover"
    usage: "Huge short title with a tiny benefit-driven subtitle"
  - type: "Giant_Number"
    usage: "One key figure from the sources at massive scale"
  - type: "Text_Void_Contrast"
    usage: "Packed text on one half, empty space on the other"
  - type: "Punchline_Center"
    usage: "Key takeaway in the center or bleeding off the edge"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

## Notas de uso
- Funciona bien con resúmenes de guías, notas informativas de la AEMPS o artículos de revistas.
- Revisa que las cifras de los titulares gigantes coincidan con la fuente.

> 🖼️ Las imágenes de `images/01-boletin-sanitario/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
