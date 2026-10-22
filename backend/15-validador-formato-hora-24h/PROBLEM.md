# Validador de Hora (Formatos 24h)

- **Concepto:** El usuario ingresa una hora en formato de texto `HH:MM` por consola (ej. `14:30` o `25:70`). El programa analiza si la hora es válida (horas entre $0$ y $23$, minutos entre $0$ y $59$) y muestra un mensaje de confirmación o de error explícito
- **Por qué funciona:** Enseña la extracción de subcadenas (`substring` / lectura dividida por `:`), la conversión de texto a número (`atoi` / `parseInt`) y la validación de rangos con condicionales
- **Lógica clave:** Separar las horas de los minutos y verificar las condiciones: $0 \le \text{horas} \le 23$ y $0 \le \text{minutos} \le 59$
