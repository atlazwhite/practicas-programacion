# Generador de Colores Hexadecimales

- **Concepto:** Un botón que, al hacer clic, genera un código de color hexadecimal aleatorio (ej. `#3A86EF`), cambia el fondo de la página a ese color y muestra el código generado para copiar
- **Por qué funciona:** Introduce la generación de números aleatorios combinada con formato de cadenas de texto y manipulación directa de `document.body.style.backgroundColor`
- **Elemento interactivo JS:** Evento `click` en un botón central que refresca el color de fondo e inserta el texto del código de color en pantalla
