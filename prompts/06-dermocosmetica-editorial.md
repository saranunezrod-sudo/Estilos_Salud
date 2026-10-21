---
title: Dermocosmética Editorial
category: C. Producto y cosmética
format: design_system
audience: Campañas de farmacia, consejos de cuidado de la piel y presentaciones de gama
status: probado
author: Mantenedores del repositorio
inspired_by: Magazine style (https://x.com/tetumemo/status/1996930284500201685) vía awesome-notebookLM-prompts
---

# Dermocosmética Editorial

**Ideal para:** presentar una gama o una rutina con aspecto de revista de belleza sofisticada.

```
design_system:
  global_style:
    theme: "Sophisticated skincare magazine. Mature-cute, feminine, trendy, polished and trustworthy."
    typography:
      primary_heading: "Sophisticated gothic sans-serif or elegant serif"
      secondary_heading: "Hand-drawn font for comments and bubbles"
      body_text: "Clean small sans-serif"
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "#EBD3CF dusty blush, matte"
      text_main: "#2F2F33"
      secondary: "#FFFFFF"
      accent_color: "#00A19B"
    key_visual_elements:
      - "Large deep-etched cutout of the product in the center"
      - "Hand-drawn speech bubbles asymmetrically in the margins"
      - "Small numbered sections NO.1, NO.2"
      - "Vertical white text box at the edge and L-shaped crop marks in the corners"

slide_layout_templates:
  - type: "Magazine_Cover"
    usage: "Central cutout product, asymmetric bubbles, catchy vertical line"
  - type: "Numbered_Advice"
    usage: "Main points as NO.1, NO.2 sections around the product"
  - type: "Ingredient_Spotlight"
    usage: "One ingredient from the sources in a white box with a hand-drawn arrow"

avoid: "childish vivid colors, flashy gradients, heavy shadows, miracle or guaranteed claims"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

## Notas de uso
- Probado en NotebookLM en octubre de 2026.

> 🖼️ Las imágenes de `images/06-dermocosmetica-editorial/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
