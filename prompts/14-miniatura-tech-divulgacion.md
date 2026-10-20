---
title: Miniatura Tech Divulgación
category: F. Personajes e ilustración
format: design_system
audience: Divulgación y formación sobre tecnología, IA y salud digital con portada tipo miniatura de vídeo
status: sin probar
author: Mantenedores del repositorio
inspired_by: Estilo de miniatura de formación tecnológica con presentadora ilustrada y fondo azul noche (captura aportada por la persona que mantiene el repositorio)
---

# Miniatura Tech Divulgación

**Ideal para:** cursos y charlas de IA, herramientas digitales y datos en salud, con una persona ilustrada en bata que acompaña cada idea, etiqueta naranja y tarjetas con iconos.

```
design_system:
  global_style:
    theme: "Tech explainer video thumbnail. Dark navy interface background, a friendly illustrated expert character, big bold question titles. Energetic, approachable, modern."
    typography:
      primary_heading: "Extra-bold condensed sans-serif, uppercase, huge, white and light cyan, 2-3 stacked lines"
      secondary_heading: "Heavy sans-serif uppercase inside an orange label bar with the section number, e.g. 01"
      body_text: "Light geometric sans-serif, white, 1-2 short lines as subtitle"
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "#0B1F33 deep navy with faint blurred UI panels"
      primary: "#6FD3F5 light cyan"
      accent_color: "#F5A833 orange for label bars and small squares"
      secondary: "#5ED6B5 mint for icon outlines"
      text_main: "#FFFFFF"
    protagonist: "A recurring semi-realistic illustrated female presenter, wearing round glasses and a white lab coat, expressive thoughtful pose (hand on chin, pointing, thumbs up), placed on the right third of the slide. Same face, hair and glasses on every slide. Only pose and expression change."
    key_visual_elements:
      - "Rounded icon cards with thin glowing outlines (network, chat bubble, document, shield)"
      - "Large floating question mark or exclamation with small spark lines"
      - "Small pixel squares in the corners and thin gradient lines"
      - "Text on the left, character on the right, icons at the bottom-left"

slide_layout_templates:
  - type: "Thumbnail_Cover"
    usage: "Orange numbered label, stacked giant title, subtitle, two icon cards, character on the right"
  - type: "Concept_Cards"
    usage: "Three rounded icon cards joined by dotted lines with a one-word caption each"
  - type: "Character_Says"
    usage: "Large character with a short speech bubble stating one key idea"
  - type: "Step_Flow"
    usage: "Numbered orange labels linked by thin glowing lines"

avoid: "cluttered screenshots, small text, light backgrounds, cartoon mascots, stock-photo people, invented logos"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

## Notas de uso
- El personaje es una ilustración genérica. No uses la imagen de una persona real como protagonista sin su permiso.
- Para mantener la misma presentadora en todas las diapositivas, sube una imagen de referencia como fuente del cuaderno y pruébalo.

> 🖼️ Las imágenes de `images/14-miniatura-tech-divulgacion/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
