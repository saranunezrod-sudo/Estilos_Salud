---
title: Film Scrapbook
category: D. Retro y creativos
format: design_system
audience: Historias, biografías, casos narrados, historia de la farmacia y presentaciones tipo documental
author: Mantenedores del repositorio
inspired_by: Film Scrapbook (ejemplo de design_system aportado por la persona que mantiene el repositorio)
---

# Film Scrapbook

**Ideal para:** contar una historia con tono personal y nostálgico: trayectorias profesionales, historia de un medicamento o de la farmacia, casos narrados o cualquier presentación estilo documental "entre bambalinas". Negro carbón y crema, tiras de película, papel rasgado y subrayados mostaza dibujados a mano.

```
description: "A tactile and nostalgic aesthetic designed for storytelling, biographies, and documentary-style presentations. It pairs the clean Open Sauce sans-serif with the technical Fira Code monospace. Characterized by a charcoal black and cream palette, it features film strip borders, ripped paper textures, and hand-drawn mustard yellow highlights to create a personal, 'behind-the-scenes' scrapbook atmosphere."

design_system:
  global_style:
    theme: "Film Scrapbook. Personal and nostalgic design with film textures and hand-drawn highlights."
    typography:
      primary_heading: "Open Sauce, sans-serif"
      secondary_heading: "Fira Code, monospace"
      body_text: "Fira Code, regular"
      language: "the language should be what users said in the prompt"
    color_palette:
      primary: "#C0CA33" # Mustard Yellow Highlight
      secondary: "#F5F5DC" # Old Paper Cream
      background: "#121212" # Charcoal Black
      surface: "#F5F5DC" # Cream Surface for paper notes
      text_main: "#F5F5DC" # Cream text on dark
      text_secondary: "#121212" # Dark text on paper
    key_visual_elements:
      - "Vertical film strip borders and vintage camera reel motifs"
      - "Ripped paper textures used as containers for secondary text"
      - "Hand-drawn mustard yellow circles and underlines to emphasize words"
      - "Simple doodle-style icons (smileys, arrows, stars) in yellow and white"

  image_generation_prompts:
    style_guidelines: "Vintage film scrapbook aesthetic, charcoal black and cream palette, film strips, ripped paper, hand-drawn yellow circles, Fira Code font vibe, grainy documentary atmosphere."
    themes:
      - target: "Story Introduction"
        prompt_elements: "A vintage film strip on the side of a charcoal black background, a piece of ripped cream paper in the center, hand-drawn yellow arrow."
      - target: "Historical Context"
        prompt_elements: "A grainy black and white photo framed like a polaroid, mustard yellow scribbles, old paper texture."

slide_layout_templates:
  - type: "Scrapbook_Title"
    usage: "Title in Open Sauce on black with film strips on the edges and a hand-drawn circle around a key word"
  - type: "Ripped_Note_Slide"
    usage: "Body text in Fira Code placed over a large ripped paper graphic in the center"
  - type: "Film_Strip_Gallery"
    usage: "Multiple photos arranged as if they were part of a continuous film reel"
  - type: "Doodle_Resource_Page"
    usage: "Icons and links surrounded by hand-drawn scribbles and smiley faces on a cream background"

healthcare_rules: "Use only the provided sources. Never invent doses, indications or figures; leave a marked blank if data is missing. No real patient data. Patient-facing slides end with a small footer: Consult your healthcare professional (in the user's language)."
```

## Notas de uso
- Funciona bien para narrativa: línea temporal de una trayectoria, evolución de un tratamiento o historia de una botica.
- Añade tus ejemplos reales en `images/08-film-scrapbook/` y ejecuta `python3 -I scripts/build_readme.py`.

> 🖼️ Las imágenes de `images/08-film-scrapbook/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.
