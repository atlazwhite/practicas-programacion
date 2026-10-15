# Medidor de Fuerza de Contraseña

- **Concepto:** Un campo de entrada (`<input type="password">`) que muestra en tiempo real si una contraseña es "Débil", "Media" o "Fuerte" cambiando una barra visual de color (rojo, amarillo, verde)
- **Por qué funciona:** Enseña a evaluar la longitud de un string y la presencia de ciertos caracteres (`length`, condiciones simples) mientras se modifica el ancho y color de un `<div>` vía CSS
- **Elemento interactivo JS:** Evento `input` que evalúa el texto tipeado y actualiza dinámicamente las clases CSS o estilos de la barra
