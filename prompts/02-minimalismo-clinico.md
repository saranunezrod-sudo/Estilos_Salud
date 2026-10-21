---
title: Minimalismo Clínico
category: A. Clínico y profesional
format: design_system
audience: Sesiones clínicas, protocolos y presentaciones formales con mucho espacio en blanco
author: Mantenedores del repositorio
inspired_by: Sharp-edged Minimalism (https://x.com/yoshifujidesign/status/1997878247322001626) vía awesome-notebookLM-prompts
---

# Minimalismo Clínico

**Ideal para:** protocolos, casos clínicos, resultados de estudios y algoritmos de decisión con tono sobrio.

```
design_system:
  global_style:
    theme: "Sharp-edged clinical minimalism. Architectural, grid-based, aesthetics of whitespace."
    typography:
      primary_heading: "Inter / Helvetica Now bold, English, with a small section label such as 01. INTRODUCTION top-left"
      secondary_heading: "Small caps labels"
      body_text: "Small sans-serif with generous letter spacing and line height"
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "#FFFFFF"
      surface: "#EEF2F3"
      text_main: "#0B1F2A"
      primary_color: "#00A19B"
      dark_mode: "#0B1F2A for emphasis slides"
    key_visual_elements:
      - "Strict grid with large empty areas"
      - "Hairline dividers and oversized teal key figures"
      - "Wireframe diagrams, thin white lines on dark"
      - "Desaturated clinical photography with tiny captions"

slide_layout_templates:
  - type: "Text_Data_Split"
    usage: "Narrative left, oversized teal figure right, thin divider"
  - type: "Photo_List_Split"
    usage: "50:50 photo and bold-heading list with light descriptions"
  - type: "Decision_Flow"
    usage: "Clinical algorithm with thin lines, yes/no branches, one sentence per node"
  - type: "Vertical_Timeline"
    usage: "Thin vertical line with text branching left and right"
  - type: "Parameter_Table"
    usage: "Hairline rows, bold names left, large light values right"
  - type: "Dark_Mode_Diagram"
    usage: "Dark background, thin white lines connecting nodes"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

## Notas de uso
- Muy buen resultado con artículos científicos o guías de práctica clínica como fuente.

> 🖼️ Las imágenes de `images/02-minimalismo-clinico/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
