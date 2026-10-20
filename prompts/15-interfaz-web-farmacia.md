---
title: Interfaz Web Farmacia
category: E. Herramientas digitales
format: design_system
audience: Presentar herramientas digitales, catálogos, consultas y proyectos de farmacia con aspecto de producto web moderno
status: sin probar
author: Mantenedores del repositorio
inspired_by: Estilo de landing page de producto sanitario verde sobre blanco roto (captura aportada por la persona que mantiene el repositorio)
---

# Interfaz Web Farmacia

**Ideal para:** presentar una herramienta, un buscador, un catálogo o un proyecto de farmacia comunitaria con estética de página web limpia: titular grande en tres líneas, tarjeta de interfaz, chips y cifras.

```
design_system:
  global_style:
    theme: "Clean healthcare product landing page. Calm, trustworthy, modern SaaS. Generous whitespace, soft rounded cards, one confident green accent."
    typography:
      primary_heading: "Large tight-tracking sans-serif (Inter / Helvetica Now), 3 short lines, the middle line in green"
      secondary_heading: "Small uppercase letter-spaced labels with a green dot, e.g. FOR COMMUNITY PHARMACY"
      body_text: "Regular gray-green sans-serif, 1-2 short lines, one quoted note with a thin left rule"
      numbers: "Medium-weight figures with a small caption underneath"
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "#FAFAF5 warm off-white with a very soft green haze"
      text_main: "#1F3A33 deep green-black"
      primary: "#2F6B58 forest green"
      button: "#2D5B4C"
      surface: "#FFFFFF cards with a thin #E3E8E2 border"
      chip: "#E9F0EA pale green"
    key_visual_elements:
      - "Big rounded white card with a thin outline showing a clean interface: search field, dropdown, dark green button with an arrow"
      - "Pill chips with check marks (e.g. Marketed, No prescription)"
      - "Quick-query chips with small arrows"
      - "Three key figures in a row with captions and a thin divider above"
      - "Tiny green cross icon and dot in the card header"

slide_layout_templates:
  - type: "Landing_Hero"
    usage: "Three-line headline and subtitle on the left, interface card on the right, chips and figures below"
  - type: "Feature_Cards"
    usage: "Three rounded cards, each with a small icon, title and one sentence"
  - type: "Key_Figures"
    usage: "Three large figures from the sources with captions and a thin divider"
  - type: "Interface_Mockup"
    usage: "Large card with a simplified UI relevant to the topic, with a green call-to-action button"
  - type: "Data_Source_Note"
    usage: "Soft gray-green note box stating where the data comes from"

avoid: "dark backgrounds, bright neon colors, heavy shadows, clip art, busy screenshots, invented statistics or product names"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

## Notas de uso
- Muy útil para presentar proyectos propios (buscadores, catálogos, cuadros de mando) con aspecto de producto.
- Las cifras y los textos de la tarjeta de interfaz deben salir de las fuentes: revisa que no se inventen datos.

> 🖼️ Las imágenes de `images/15-interfaz-web-farmacia/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
