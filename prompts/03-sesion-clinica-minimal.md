---
title: Sesión Clínica Minimal
category: A. Clínico y profesional
format: design_system
audience: Sesiones y charlas con poco texto y mucho impacto visual
author: Mantenedores del repositorio
inspired_by: For Seminar Use, Minimal Text (Kawai, https://x.com/kawai_design) vía awesome-notebookLM-prompts
---

# Sesión Clínica Minimal

**Ideal para:** charlas y formación en las que tú explicas y la diapositiva solo acompaña.

```
design_system:
  global_style:
    theme: "Minimal-text clinical seminar. Editorial, confident, one idea per slide."
    typography:
      primary_heading: "Large dynamic sans-serif, tight tracking, mixed scale"
      secondary_heading: "Small uppercase labels"
      body_text: "Light clean sans-serif, maximum two short lines per slide"
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "#FFFFFF"
      text_main: "#111111"
      primary_color: "#0072CE"
      accent_color: "#0072CE used once per slide"
    key_visual_elements:
      - "High-quality editorial portraits of healthcare professionals"
      - "Clean photography of medical products"
      - "Oversized typography overlapping photos"
      - "Lots of white space"

slide_layout_templates:
  - type: "Portrait_Cover"
    usage: "Editorial portrait with oversized overlapping title"
  - type: "One_Sentence"
    usage: "A single sentence in large type with abundant white space"
  - type: "Photo_Full_Bleed"
    usage: "Full-slide photo with one short caption"
  - type: "Number_Focus"
    usage: "One figure from the sources in huge type with a thin label"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

## Notas de uso
- Ideal cuando la fuente es larga y solo quieres ideas fuerza por slide.

> 🖼️ Las imágenes de `images/03-sesion-clinica-minimal/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
