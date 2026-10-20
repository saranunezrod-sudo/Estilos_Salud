# Awesome NotebookLM Prompts: Salud 🩺

![Licencia: CC BY 4.0](https://img.shields.io/badge/Prompts_y_docs-CC_BY_4.0-lightgrey.svg)
![Licencia: MIT](https://img.shields.io/badge/Código-MIT-green.svg)

> Colección **pública, gratuita y colaborativa** de estilos visuales y prompts para generar presentaciones con **NotebookLM** (y alternativas como Kael.im) en el ámbito sanitario: farmacia, medicina, enfermería y educación para la salud.

Pensado para que farmacéuticos, médicos, enfermeros y otros profesionales puedan **reutilizar, adaptar y compartir** diseños: presentar una gama de cosmética, preparar una sesión clínica o diseñar una campaña de farmacia.

## Cómo usarlo

1. Abre tu cuaderno en NotebookLM y añade tus **fuentes** (ficha técnica, prospecto, guía clínica, catálogo...).
2. Entra en **Studio → Presentación de diapositivas** y pulsa el icono de personalizar.
3. **Copia y pega el prompt completo, tal cual** (están en inglés a propósito: es el formato que mejor funciona). Todos incluyen la instrucción `the language should be what users said in the prompt`, así que las diapositivas saldrán en el idioma en que escribas tu petición y tus fuentes.
4. Añade debajo, si quieres, una línea con tu petición en español, por ejemplo: *"Explica a un paciente el uso paso a paso, en 8 diapositivas"*.
5. **Revisa siempre el resultado** con la fuente oficial antes de usarlo con pacientes.

## Qué tienen en común todos los prompts

- Siguen el formato **`design_system`** (el que usan los diseños de NotebookLM/Kael.im): `global_style` (tema, tipografía, paleta en hexadecimal, elementos visuales), `image_generation_prompts` y `slide_layout_templates` con nombre.
- Incluyen la cláusula `the language should be what users said in the prompt` en la tipografía.
- Añaden un bloque `healthcare_rules`: usar solo información de las fuentes, no inventar dosis ni cifras, no mostrar datos de pacientes y añadir el pie "consulta a tu profesional sanitario" en material para pacientes.

> 🎨 **Este repositorio es solo de diseño**: define cómo se ve una presentación, nunca su contenido clínico. Las instrucciones de uso de cada medicamento o producto deben salir siempre de la ficha técnica o del prospecto que cargues como fuente.

> ⚠️ **Aviso importante**: estos prompts controlan el *diseño*, no el *contenido clínico*. La inteligencia artificial puede equivocarse. Verifica dosis, pasos de uso, indicaciones y advertencias con la ficha técnica o la fuente oficial antes de entregar cualquier material. Nunca subas datos identificables de pacientes.

Las imágenes de ejemplo son **solo una guía orientativa**: al usar **IA generativa**, el resultado puede variar entre generaciones, según tus fuentes y con las actualizaciones de NotebookLM. Los estados `sin probar` / `probado` indican si el estilo ya se ha comprobado en NotebookLM con capturas en [images/](images/). ¿Lo has probado? ¡Aporta tus capturas! Consulta [CONTRIBUTING.md](CONTRIBUTING.md).
