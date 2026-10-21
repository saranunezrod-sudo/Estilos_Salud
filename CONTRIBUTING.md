# Cómo contribuir

¡Gracias por aportar! Este repositorio es de y para profesionales sanitarios. No hace falta saber programar: un estilo es un archivo de texto.

## Formas de contribuir
- **Conversar**: comparte resultados, ideas y dudas en [Discussions](https://github.com/saranunezrod-sudo/Estilos_Salud/discussions) antes de abrir un pull request.
- **Proponer un estilo nuevo** (issue con la plantilla *Proponer un nuevo estilo*, o pull request directo).
- **Probar un estilo** en NotebookLM y compartir capturas del resultado (sin datos de pacientes).
- **Mejorar un prompt** existente o corregir erratas.
- **Traducir o ampliar** la documentación.

## Pasos para añadir un estilo (pull request)
1. Haz un *fork* del repositorio y crea una rama: `estilo/nombre-corto`.
2. Copia [templates/STYLE_TEMPLATE.md](templates/STYLE_TEMPLATE.md) a `prompts/NN-nombre.md` (el siguiente número libre, por ejemplo `16-mi-estilo.md`).
3. Rellena el encabezado (título, categoría, formato, para quién, autor, inspiración) y pega el prompt en el bloque de código.
4. Guarda 2-3 capturas del resultado en `images/NN-nombre/` (opcional pero muy recomendado).
5. Ejecuta las comprobaciones:
   ```
   python3 -I scripts/check_prompts.py
   python3 -I scripts/build_readme.py
   ```
   El segundo comando regenera el `README.md`; incluye el cambio en tu PR. **No edites el README a mano.**
6. Abre el pull request y completa la lista de comprobación.

## Reglas de un buen prompt
1. **Formato `design_system`**: `description`, `global_style` (theme, typography, color_palette, key_visual_elements), `image_generation_prompts` y `slide_layout_templates`. Son concretos: colores en hexadecimal, tipografías, elementos visuales y layouts con nombre. Mira cualquier archivo de `prompts/` como ejemplo.
2. **En inglés**, con la cláusula `the language should be what users said in the prompt` para que la salida esté en el idioma del usuario.
3. **Bloque `healthcare_rules` obligatorio** (ver la plantilla): no inventar dosis, indicaciones ni cifras, y no mostrar datos de pacientes.
4. **Sin contenido clínico concreto**: el prompt define el diseño, no las dosis ni las pautas. Eso viene de las fuentes del usuario.
5. **Accesibilidad**: contraste suficiente, tamaños legibles y no depender solo del color para transmitir significado.
6. **Sin promoción**: nada de marcas comerciales ni claims de producto dentro del prompt.

## Datos, imágenes y derechos
- **Nunca** subas datos o imágenes identificables de pacientes.
- Sube solo imágenes que hayas generado tú o que puedas compartir. Si el resultado contiene logotipos o packaging de una marca, usa material genérico.
- Si te inspiras en el estilo de otra persona, cítala en `inspired_by` con enlace.

## Autoría y licencia
- Al contribuir aceptas publicar tu aportación bajo **CC BY 4.0** (prompts, documentación e imágenes) o **MIT** (código en `scripts/`).
- Tu nombre o usuario de GitHub figurará en el campo `author` del estilo.

## Revisión
Quienes mantienen el repositorio revisarán el PR comprobando estructura, bloque sanitario y licencias. Las sugerencias de cambios son una forma de mejorar el estilo, no una crítica.

Consulta también el [Código de conducta](CODE_OF_CONDUCT.md).
