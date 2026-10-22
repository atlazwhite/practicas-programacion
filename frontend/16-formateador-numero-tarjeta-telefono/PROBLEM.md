# Formateador de Números (Tarjeta/Teléfono)

- **Concepto:** Un campo de entrada donde el usuario escribe solo dígitos numéricos y el script les aplica formato automáticamente insertando guiones o espacios cada 4 dígitos (ej. `1234 5678 9012 3456` o `0412-123-4567`)
- **Por qué funciona:** Excelente para entender la limpieza de caracteres no numéricos y la reconstrucción de un string con formato amigable para el usuario
- **Elemento interactivo JS:** Evento `input` que remueve letras/símbolos y reorganiza los dígitos con guiones/espacios en tiempo real
