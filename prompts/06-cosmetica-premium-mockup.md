---
title: Cosmética Premium Mockup
category: C. Producto y cosmética
format: design_system
audience: Presentar productos cosméticos y dermocosméticos a clientes, equipo de farmacia o proveedores
status: sin probar
author: Mantenedores del repositorio
inspired_by: Studio / Mockup / Premium (https://note.com/yoshifujidesign/n/n7412bccb5762) vía awesome-notebookLM-prompts
---

# Cosmética Premium Mockup

**Ideal para:** fichas de producto, lanzamientos, formación de mostrador y catálogos con estética de estudio.

```
design_system:
  global_style:
    theme: "Premium clean-beauty packshot. Refined, professional, showcase in perfection."
    typography:
      primary_heading: "Elegant blocky sans-serif or high-contrast serif, English large"
      secondary_heading: "Small subtitle in the user's language"
      body_text: "Thin gray sans-serif"
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "#FFFFFF or warm #F6F3EF"
      dark_slides: "#0F2A33"
      primary_color: "#00A19B"
      accent_color: "#E8C9A0 champagne"
      surface: "#DCEBEA"
    key_visual_elements:
      - "3D packshots of generic tubes, pump bottles and jars on light stone podiums"
      - "Water droplets, soft shadows and glass reflections"
      - "Product as hero, partly cropped by the edge"
      - "Rounded cards for active ingredients"

slide_layout_templates:
  - type: "Hero_Product"
    usage: "Centered product on a podium with ultra-bold title"
  - type: "Active_Ingredients_Cards"
    usage: "One rounded card per ingredient from the sources"
  - type: "Split_Numbers"
    usage: "Large figures from the sources left, description right"
  - type: "How_To_Use"
    usage: "Three or four numbered steps with line icons, only from the sources"
  - type: "Precautions_Card"
    usage: "Small card with precautions exactly as in the sources"

avoid: "invented claims, percentages, certifications, brand logos"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

> 🖼️ Las imágenes de `images/06-cosmetica-premium-mockup/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
