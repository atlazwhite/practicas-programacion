# Validador de Formato de Correo

- **Concepto:** Un campo de texto para ingresar un correo electrónico que evalúa si el formato es válido (contiene `@`, punto `.`, sin espacios) mientras el usuario escribe, cambiando el borde del campo de rojo a verde y mostrando un mensaje dinámico
- **Por qué funciona:** Enseña la lectura de cadenas de texto con métodos nativos (`includes()`, `indexOf()`) y el control dinámico de estilos o clases en el DOM
- **Elemento interactivo JS:** Evento `input` que verifica si el valor incluye `@` y un dominio posterior, cambiando el estado visual de un `<span>` con el mensaje de error/éxito
