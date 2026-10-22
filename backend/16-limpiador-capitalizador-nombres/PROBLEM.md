# Limpiador y Capitalizador de Nombres

- **Concepto:** Un script que recibe por consola un nombre completo ingresado de forma desordenada o con mayúsculas/minúsculas mal colocadas (ej. `aLEx rÍoS`), elimina espacios extra al inicio/final y lo devuelve formateado con la inicial de cada palabra en mayúscula (`Alex Ríos`)
- **Por qué funciona:** Refuerza la iteración sobre caracteres, la transformación con funciones nativas (`toupper`/`tolower`) y el manejo de índices de espacios
- **Lógica clave:** Convertir todo a minúsculas, detectar el inicio de cada palabra e invertir únicamente el primer carácter a mayúscula
