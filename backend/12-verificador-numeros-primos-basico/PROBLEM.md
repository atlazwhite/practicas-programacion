# Verificador de Números Primos y Divisores

- **Concepto:** Un script que lee un número entero positivo ingresado por el usuario y determina si es un número primo o un número compuesto, mostrando además todos sus divisores exactos
- **Por qué funciona:** Es la mejor introducción a la optimización de bucles condicionales (`for` desde 1 hasta $N$) y al conteo de condiciones de parada
- **Lógica clave:** Un contador de divisores que se incrementa cada vez que `N % i == 0`. Si al final del bucle la cantidad de divisores es exactamente 2 (1 y él mismo), el número es primo
