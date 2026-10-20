---
title: Duotono Números Gigantes
category: D. Retro y creativos
format: design_system
audience: Informes, estudios y resúmenes ejecutivos numerados con estética tecnológica y editorial
status: sin probar
author: Mantenedores del repositorio
inspired_by: Estilo de informe en duotono morado con numeración gigante recortada (captura aportada por la persona que mantiene el repositorio)
---

# Duotono Números Gigantes

**Ideal para:** informes anuales, estudios y resúmenes ejecutivos en los que cada sección abre con un número enorme recortado por el borde sobre una imagen técnica en duotono.

```
design_system:
  global_style:
    theme: "Tech editorial report. Duotone grainy imagery, giant cropped section numbers, bold and futuristic, a calm authority."
    typography:
      primary_heading: "Wide rounded geometric techno sans-serif (Orbitron / Michroma style), all lowercase, white-lilac"
      secondary_heading: "Same family in a small mustard edition label"
      body_text: "Clean sans-serif, small, high contrast on the dark duotone"
      numerals: "Giant section number covering 60-100% of the slide height, cropped by the left edge, in pale lilac"
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "#5B4A8C violet duotone with fine film grain"
      secondary: "#3E5A1E dark green as the second duotone tone"
      text_main: "#E8E8F0"
      accent_color: "#F2B233 mustard, only for small labels"
    key_visual_elements:
      - "Duotone (violet and green) macro photography of machinery, circuitry, cables or lab equipment, with strong grain"
      - "Giant cropped numerals 01, 02, 03 as section dividers"
      - "Title block of 3-4 short lowercase lines on the right"
      - "Lots of empty duotone space, no boxes or borders"

slide_layout_templates:
  - type: "Giant_Number_Opener"
    usage: "Huge cropped number on the left, section title and edition label on the right"
  - type: "Executive_Summary"
    usage: "Short lowercase title at the bottom right, three key figures from the sources in light type"
  - type: "Duotone_Full_Image"
    usage: "Full-slide duotone photo with a single sentence"
  - type: "Data_On_Duotone"
    usage: "Thin white chart lines or large numbers over a darkened duotone image"

avoid: "bright multicolor palettes, boxes with borders, serif fonts, clip art, long paragraphs"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

## Notas de uso
- Funciona muy bien con informes y estudios con secciones numeradas. Si no hay imágenes en las fuentes, el estilo recurre a texturas técnicas en duotono.

> 🖼️ Las imágenes de `images/13-duotono-numeros-gigantes/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
