# Rastreador de Gastos por Categoria

- **Concepto:** Una interfaz donde el usuario ingresa un presupuestro total y luego suma gastos individuales seleccionando una categoría (Comida, Transporte, Entretenimiento). Muestra el dinero restante e indica si te has pasado del límite
- **Por qué funciona:** Excelente combinación de inputs, menús desplegables (`<select>`), suma de acumuladores y condicionales visuales en CSS
- **Elemento interactivo JS:** Un botón "Agregar Gasto" que resta el monto al total disponible y cambia el contenedor a color rojo/alerta si el presupuesto llega a $0$ o menos
