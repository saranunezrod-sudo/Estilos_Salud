---
title: Monigote Científico
category: F. Personajes e ilustración
format: design_system
audience: Divulgación sanitaria con un protagonista recurrente: explicar la piel, el acné, las hormonas, la microbiota o cualquier concepto con dibujos a mano
status: sin probar
author: Mantenedores del repositorio
inspired_by: Estilo personal de doodle a tinta sobre papel crema con monigote científico (autoría de la persona que mantiene el repositorio)
---

# Monigote Científico

**Ideal para:** series de diapositivas divulgativas con el mismo protagonista: un monigote de cabeza redonda, gafas y bata blanca que comenta cada concepto. Dibujo a línea negra sobre papel crema, esquemas tipo corte de piel y personajes que representan bacterias, hormonas o células.

```
design_system:
  global_style:
    theme: "Hand-drawn doodle explainer. Minimalist black ink line art on cream paper, like a sketchbook. Friendly, humorous, one idea per slide."
    typography:
      primary_heading: "Bold hand-lettered uppercase block letters"
      secondary_heading: "Small hand-lettered uppercase labels with arrows, max 8 words"
      body_text: "Short hand-lettered phrases"
      language: "the language should be what users said in the prompt"
      rules: "Spell every word correctly. Never repeat a label."
    color_palette:
      background: "#F3EEDD cream paper"
      ink: "#111111 thick black outline, mostly unfilled line art"
      chalkboard: "#161616 with white chalk lettering for emphasis slides"
      accent_color: "#D94B3F tiny touches only"
    protagonist: "Recurring stick-figure scientist, always identical: huge perfectly round head with a tiny tuft of hair, round black glasses, big oval black eyes, simple smile, long white lab coat with two pockets, arms crossed, stick legs, small flat shoes. Only pose and expression change. Appears small beside each diagram, commenting on it."
    key_visual_elements:
      - "Clean cross-section diagrams (skin layers, pores) in line art with hatching"
      - "Cute mini characters with faces for bacteria, hormones and cells"
      - "Thick black frames, chalkboard or notebook-page layouts"

slide_layout_templates:
  - type: "Character_Intro"
    usage: "Large protagonist with one short title"
  - type: "Cross_Section_Diagram"
    usage: "Labelled anatomy with arrows, protagonist in a corner"
  - type: "Chalkboard_Slide"
    usage: "Dark board with white chalk title"
  - type: "Comic_Panels"
    usage: "Three framed panels for steps"

avoid: "color fills, gradients, 3D, photos, long paragraphs, misspelled words"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

## Notas de uso
- Imagen de referencia del protagonista: [images/12-monigote-cientifico/protagonista.png](../images/12-monigote-cientifico/protagonista.png).
- Para que mantenga el mismo personaje, prueba además a subir esa imagen como fuente del cuaderno.
- La IA suele cometer erratas en las etiquetas dibujadas (por ejemplo "EQUILRBO"). La regla de ortografía ayuda, pero revisa siempre los textos de cada diapositiva.
- Si cambias el aspecto del protagonista, edita solo la clave `protagonist`.

> 🖼️ Las imágenes de `images/12-monigote-cientifico/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
