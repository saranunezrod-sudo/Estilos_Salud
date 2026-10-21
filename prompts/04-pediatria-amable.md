---
title: Pediatría Amable
category: B. Educación al paciente
format: design_system
audience: Niños y familias; explicar procedimientos, vacunas o hábitos de forma amigable
author: Mantenedores del repositorio
inspired_by: Deformed Flat Persona (Kawai, https://x.com/kawai_design) vía awesome-notebookLM-prompts
---

# Pediatría Amable

**Ideal para:** materiales para niños y familias con personajes planos, trazo grueso y pocos colores.

```
design_system:
  global_style:
    theme: "Friendly flat pediatric style. Calm, reassuring, playful but never babyish. One short sentence per slide."
    typography:
      primary_heading: "Very large rounded sans-serif"
      secondary_heading: "Handwritten-style accent labels"
      body_text: "Rounded sans-serif in words a 7-year-old understands"
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "one solid flat color per slide"
      primary_color: "#7FD1C7"
      secondary: "#FFD36E"
      accent_color: "#FF8E7A"
      text_main: "#2B2B2B"
    key_visual_elements:
      - "Slightly deformed child and friendly healthcare professional"
      - "Thick outlines, flat colors, up to 3 colors per slide"
      - "Round kind faces, never scary"
      - "Stethoscope, thermometer, plaster drawn as cute simple shapes"

slide_layout_templates:
  - type: "Character_Cover"
    usage: "Large character with big rounded title"
  - type: "Story_Step"
    usage: "One illustrated step with one short sentence"
  - type: "Brave_Badge_Ending"
    usage: "Sticker-style badge, no promises about pain unless in the sources"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

## Notas de uso
- Funciona bien para explicar "qué va a pasar" antes de una vacuna o una analítica.
- Revisa que el texto no genere miedo ni prometa que "no dolerá" si la fuente no lo dice.

> 🖼️ Las imágenes de `images/04-pediatria-amable/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
