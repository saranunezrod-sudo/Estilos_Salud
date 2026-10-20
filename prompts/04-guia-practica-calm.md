---
title: Guía de Práctica Calm
category: A. Clínico y profesional
format: design_system
audience: Protocolos, guías de práctica clínica y procedimientos normalizados de trabajo
status: sin probar
author: Mantenedores del repositorio
inspired_by: Anti-Gravity / Living Artifact (awesome-notebookLM-prompts)
---

# Guía de Práctica Calm

**Ideal para:** convertir un protocolo o una guía extensa en un documento visual sereno y ordenado.

```
design_system:
  global_style:
    theme: "Calm clinical practice. A living protocol: complexity becoming clear steps. Airy, no visual noise."
    typography:
      primary_heading: "Clean modern rounded sans-serif, medium-bold, calm authority"
      secondary_heading: "Small light English labels"
      body_text: "Clean sans-serif, one concise sentence under each headline, no long paragraphs"
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "#FFFFFF"
      text_main: "#1B2631"
      primary_color: "#0072CE"
      gradient: "very low-opacity blue to cyan to mint on corners only, never behind text"
    key_visual_elements:
      - "Thin-line outline icons (cross, stethoscope, checklist, syringe)"
      - "Soft rounded cards with subtle shadows"
      - "Dense list turning into a clean checklist or pathway"
      - "Left-aligned layouts with wide margins"

slide_layout_templates:
  - type: "Calm_Cover"
    usage: "Left-aligned headline, one sentence, soft corner gradient"
  - type: "Text_Left_Visual_Right"
    usage: "One idea per slide with a thin-line diagram"
  - type: "Three_Column_Cards"
    usage: "Icon, title and 1-2 lines per card"
  - type: "Pathway_Flow"
    usage: "Sequential steps with directional arrows"

avoid: "pixel art, thick borders, bright blocks, collage, stickers, emojis, hype language"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

> 🖼️ Las imágenes de `images/04-guia-practica-calm/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
