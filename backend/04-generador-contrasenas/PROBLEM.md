# Generador de Contraseñas Seguras en Consola

- **Concepto:** Un programa que solicita al usuario la longitud deseada para una contraseña y la construye combinando letras mayúsculas, minúsculas, números y símbolos aleatorios
- **Por qué funciona:** Conecta el uso de tablas/rangos ASCII o arreglos de caracteres con la generación de números aleatorios para seleccionar posiciones
- **Lógica clave:** Un ciclo `for` que itera $N$ veces (según la longitud ingresada), seleccionando en cada paso un carácter aleatorio de un conjunto predefinido
