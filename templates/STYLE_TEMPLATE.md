---
title: Nombre del estilo
category: A. Clínico y profesional
format: design_system
audience: Para quién y para qué sirve (una línea)
status: sin probar
author: Tu nombre o usuario de GitHub
inspired_by: Estilo del repo original o fuente en que te basas (con enlace)
---

# Nombre del estilo

**Ideal para:** una frase.

```
<<< Pega aquí el prompt completo, en inglés >>>
```

## Notas de uso
- Qué tipo de fuente funciona mejor.
- Qué conviene revisar en el resultado.

## Imágenes
Guarda 2-3 imágenes en `images/NN-nombre/` con nombres descriptivos (no "captura de pantalla"). Son una guía orientativa; no incluyas datos de pacientes.

> 🖼️ Las imágenes de `images/NN-nombre/` son solo una **guía orientativa** del estilo: el resultado real puede variar según tus fuentes y la herramienta.

---

## Estructura obligatoria del prompt (formato `design_system`)

```
description: "Frase de 2-3 líneas con la atmósfera del estilo."

design_system:
  global_style:
    theme: "Nombre del estilo y su idea central"
    typography:
      primary_heading: "..."
      secondary_heading: "..."
      body_text: "..."
      language: "the language should be what users said in the prompt"
    color_palette:
      background: "#FFFFFF"
      primary: "#00A19B"
      accent_color: "#..."
      text_main: "#111111"
    key_visual_elements:
      - "Elemento visual 1"
      - "Elemento visual 2"

  image_generation_prompts:
    style_guidelines: "Resumen en una línea de la estética."
    themes:
      - target: "Nombre de la slide"
        prompt_elements: "Qué debe aparecer en la imagen."

slide_layout_templates:
  - type: "Nombre_Del_Layout"
    usage: "Para qué se usa y cómo se ve."

healthcare_rules:
  content_fidelity: "Use only information found in the provided sources. Never invent doses, indications, contraindications, figures or references. If a piece of data is missing, leave a clearly marked empty placeholder instead of guessing."
  safety: "Never show personal data of real patients. For patient-facing material, add a small footer: 'Consult your healthcare professional' (translated into the language the user wrote in)."
```

Opcionales: `numbers`, `rules` o `avoid` (qué evitar).
