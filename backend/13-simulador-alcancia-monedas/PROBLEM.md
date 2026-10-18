# Simulador de Alcancía de Monedas

- **Concepto:** Un programa de consola que simula una alcancía digital. El usuario ingresa repetidamente montos o monedas depositadas ($1$, $2$, $5$, $10$) hasta que decide escribir `0` o la palabra `salir`. Al final, imprime el desglose total guardado
- **Por qué funciona:** La mejor forma de practicar la estructura de un bucle `while` con condición de parada (sentinela) y acumulación de variables numéricas
- **Lógica clave:** Mantener una variable `total_acumulado = 0` y sumar cada depósito dentro del ciclo hasta detectar la condición de término
