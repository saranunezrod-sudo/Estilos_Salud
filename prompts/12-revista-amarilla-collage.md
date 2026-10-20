---
title: Revista Amarilla Collage
category: D. Retro y creativos
format: design_system
audience: Novedades normativas, reglas de dispensación y formación de equipo con tono de revista de moda y collage
status: sin probar
author: Mantenedores del repositorio
inspired_by: Estilo editorial amarillo y negro con fotografía en blanco y negro, cinta adhesiva y papel rasgado (capturas aportadas por la persona que mantiene el repositorio)
---

# Revista Amarilla Collage

**Ideal para:** convertir normativa o procedimientos densos (recetas, plazos, sustituciones) en una revista de moda irreverente: portada tipo "The Issue", polaroids, cinta, pegatinas y tablas sobre papel rasgado.

```
design_system:
  global_style:
    theme: "High-fashion magazine collage. Bold, irreverent, editorial scrapbook. Dense rules become punchy, scannable pages."
    typography:
      primary_heading: "Ultra-condensed high-contrast display serif, black, tightly stacked, very large, italic on covers"
      secondary_heading: "Handwritten marker script for notes, arrows and stickers"
      body_text: "Bold condensed sans-serif in black boxes with white text, or on white paper strips"
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "#F7E03C saturated yellow on every slide"
      ink: "#111111"
      paper: "#FFFFFF torn paper and polaroid frames"
      accent_color: "#C0452B used only for a cover frame or alerts"
    key_visual_elements:
      - "High-contrast black and white fashion photography of generic models and products, tilted polaroid frames"
      - "Black tape strips at the corners, torn paper cutouts, scribbled arrows and crossed-out marks"
      - "Round stickers and small medical symbols (caduceus, pills)"
      - "Tables on ripped white paper with thick black headers and rows"
      - "Rule boxes: white text on solid black"

slide_layout_templates:
  - type: "Issue_Cover"
    usage: "Giant stacked serif title, big photo with tape, sticker, handwritten tagline"
  - type: "Polaroid_Pair"
    usage: "Two tilted photos A and B with notes and black info boxes below"
  - type: "Torn_Paper_Table"
    usage: "Table on ripped paper with arrows and a sticker, black rule box at the bottom"
  - type: "Photo_Left_Text_Right"
    usage: "Large photo with tape on the left, serif title and bullets on the right"
  - type: "Flow_Boxes"
    usage: "Outlined boxes joined by thick hand-drawn arrows with a gold rule at the bottom"

avoid: "gradients, soft shadows, pastel colors, tidy corporate layouts, fake data not in the sources"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

## Notas de uso
- Ideal con normativa o circulares como fuente. Revisa plazos, años y cifras, porque el estilo las pone muy grandes.
- Si la fuente no indica una fecha o un plazo, el prompt pide dejar un hueco en lugar de inventarlo.

> 🖼️ Las imágenes de `images/12-revista-amarilla-collage/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
