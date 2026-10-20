---
title: Botánico Acuarela
category: C. Producto y cosmética
format: design_system
audience: Fitoterapia, productos naturales, plantas medicinales y gamas de cosmética natural
status: sin probar
author: Mantenedores del repositorio
inspired_by: Royal Blue and Red watercolor (https://x.com/kottley/status/1994442047579721782) vía awesome-notebookLM-prompts
---

# Botánico Acuarela

**Ideal para:** plantas medicinales, infusiones, aceites esenciales y cosmética natural con aspecto artístico.

```
design_system:
  global_style:
    theme: "Botanical watercolor apothecary. Wet watercolor washes, calm, natural, artistic."
    typography:
      primary_heading: "Readable elegant serif"
      secondary_heading: "Italic serif for plant names"
      body_text: "Clean serif or light sans-serif on calm areas only"
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "#FBF7EF watercolor paper"
      primary_color: "#7A9E7E"
      secondary: "#2F6FA3"
      accent_color: "#C98B5E"
      text_main: "#26332B"
    key_visual_elements:
      - "Wet-on-wet watercolor with soft bleeding edges"
      - "Botanical illustrations of medicinal plants with thin ink contours"
      - "Paper grain texture"
      - "Plenty of white space, text never over busy paint"

slide_layout_templates:
  - type: "Botanical_Cover"
    usage: "Large painted plant with title on a calm area"
  - type: "Plant_Profile"
    usage: "One plant per slide, properties and precautions exactly as in the sources"
  - type: "Herb_Grid"
    usage: "Several small plant paintings with short labels"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

## Notas de uso
- Mantén propiedades y precauciones exactamente como las dice la fuente (monografías EMA/ESCOP, fichas técnicas).

> 🖼️ Las imágenes de `images/07-botanico-acuarela/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
