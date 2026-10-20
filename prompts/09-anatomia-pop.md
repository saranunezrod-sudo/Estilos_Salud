---
title: Anatomía Pop
category: D. Retro y creativos
format: design_system
audience: Formación creativa, divulgación del cuerpo humano, cursos y jornadas con tono desenfadado
status: sin probar
author: Mantenedores del repositorio
inspired_by: Classic / Pop, Sculpture x Vaporwave (https://note.com/yoshifujidesign/n/n7412bccb5762) vía awesome-notebookLM-prompts
---

# Anatomía Pop

**Ideal para:** captar la atención en divulgación y formación con modelos anatómicos y esculturas clásicas con objetos pop.

```
design_system:
  global_style:
    theme: "Anatomical model pop art. Marble busts and plaster models x neon pop gadgets, humorous and surreal."
    typography:
      primary_heading: "Ultra-bold sans-serif"
      secondary_heading: "Bold sans-serif subheads"
      body_text: "Clean sans-serif"
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "solid saturated color changing each slide: cyan #19D3F3, magenta #FF2E93, yellow #FFE600, lime #B6FF00"
      text_main: "white or black, highest contrast"
      accent_color: "complementary to the background"
    key_visual_elements:
      - "White marble busts and plaster skull, heart, lungs, hand"
      - "Sunglasses, headphones, masks, smartphones, sneakers"
      - "Sharp clean cutouts"
      - "Never reuse the same model on two slides"

slide_layout_templates:
  - type: "Pop_Cover"
    usage: "Bust with sunglasses in extreme close-up"
  - type: "Organ_Spotlight"
    usage: "One organ with pop accessories and a bubble with a point from the sources"
  - type: "Split_Duality"
    usage: "Two color halves, bust holding a different object in each hand"
  - type: "QR_Closing"
    usage: "Bust holding a QR code panel"

avoid: "real patients, mocking illnesses or disabilities"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

> 🖼️ Las imágenes de `images/09-anatomia-pop/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
