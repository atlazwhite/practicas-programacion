# 🚀 Repositorio Comunitario de Prácticas para Principiantes

¡Bienvenido/a al repositorio de ejercicios y proyectos para estudiantes de programación! 

Este espacio está diseñado como un **punto de encuentro y aprendizaje colaborativo**. Aquí encontrarás ejercicios prácticos nivel inicial divididos por áreas (Frontend y Backend) con el fin de reforzar tus habilidades básicas, explorar cómo otros miembros de la comunidad han resuelto los mismos retos y aprender a contribuir a proyectos de código abierto mediante Pull Requests (PR).

---

## 📂 Estructura del Repositorio

El proyecto se organiza en dos áreas principales:

```text
.
├── frontend/       # Proyectos en HTML, CSS y JavaScript (sin librerías ni frameworks)
│   ├── 01-calculadora-propinas/
│   ├── 02-conversor-unidades/
│   ├── 03-promedio-notas/
│   ├── 04-generador-memes/
│   ├── 05-contador-clics-temporizador/
│   ├── 06-galeria-reproductor-imagenes/
│   └── 07-lista-tareas-ultra-simple/
│
└── backend/        # Ejercicios en C, C++, Java, Rust, Python,... (el que quieras)
    ├── 01-analizador-cifrado-cesar/
    ├── 02-inversor-palindromos/
    ├── 03-histograma-vocales/
    ├── 04-generador-contrasenas/
    ├── 05-simulador-dado-moneda/
    ├── 06-tablas-multiplicar-formateadas/
    └── 07-conversor-tiempo-segundos/
```

Dentro de cada directorio de ejercicio encontrarás un archivo `PROBLEM.md` con la explicación detallada del reto y una carpeta `solutions/` con las contribuciones de los estudiantes.

---

## 🎯 Proyectos Disponibles

### 🎨 Frontend

1. [**Calculadora de Propinas / Presupuesto:** Cálculo en tiempo real a partir de entradas numéricas](./frontend/01-calculadora-propinas/PROBLEM.md)
2. [**Conversor de Unidades Interactivo:** Conversión fluida de temperaturas o divisas ficticias](./frontend/02-conversor-unidades/PROBLEM.md)
3. [**Simulador de Promedio de Notas:** Procesamiento de calificaciones y cambio de estados visuales](./frontend/03-promedio-notas/PROBLEM.md)
4. [**Generador de Memes / Frases:** Manipulación de texto y atributos de imagen en el DOM](./frontend/04-generador-memes/PROBLEM.md)
5. [**Contador de Clics con Temporizador:** Uso de eventos de tiempo (`setInterval`) y conteo de clics](./frontend/05-contador-clics-temporizador/PROBLEM.md)
6. [**Galería / Reproductor de Imágenes:** Manejo de arreglos e índice dinámico para cambiar el `src`](./frontend/06-galeria-reproductor-imagenes/PROBLEM.md)
7. [**Lista de Tareas Ultra Simple:** Creación dinámica de elementos del DOM (`createElement` / `appendChild`)](./frontend/07-lista-tareas-ultra-simple/PROBLEM.md)

### ⚙️ Backend

1. [**Analizador de Texto y Cifrado César:** Manipulación de caracteres y desplazamientos ASCII](./backend/01-calculadora-propinas/PROBLEM.md)
2. [**Inversor de Cadenas y Detector de Palíndromos:** Recorrido inverso de arreglos e índices](./backend/02-conversor-unidades/PROBLEM.md)
3. [**Histograma de Vocales:** Conteo y representación gráfica simple mediante caracteres](./backend/03-promedio-notas/PROBLEM.md)
4. [**Generador de Contraseñas Seguras:** Selección aleatoria dentro de tablas ASCII/conjuntos](./backend/04-generador-memes/PROBLEM.md)
5. [**Simulador de Dado / Moneda:** Uso de funciones aleatorias y condicionales simples](./backend/05-simulador-dado-moneda/PROBLEM.md)
6. [**Tablas de Multiplicar Formateadas:** Iteración con bucles `for` y salida alineada por consola](./backend/06-tablas-multiplicar-formateadas/PROBLEM.md)
7. [**Conversor de Tiempo a Segundos:** Operadores aritméticos de división entera y módulo (`%`)](./backend/07-conversor-tiempo-segundos/PROBLEM.md)

---

## 🤝 Cómo Contribuir (tu primer Pull Request)

¡Subir tu solución es muy sencillo y te ayudará a practicar el flujo real de trabajo con Git! Sigue estos pasos:

### 1. Haz un Fork del Repositorio

Haz clic en el botón **Fork** (arriba a la derecha) para crear una copia de este repositorio en tu cuenta de GitHub.

### 2. Clona tu Fork

Abre tu terminal y descarga tu copia localmente:

```bash
git clone https://github.com/<tu-usuario>/<nombre-del-repositorio.git>
cd <nombre-del-repositorio>
```

### 3. Crea una Rama (Branch)

Crea una rama específica para tu solución:

```bash
git checkout -b solucion/<nombre-ejercicio-tu-usuario>
# Ejemplo: git checkout -b solucion/conversor-unidades-pedrocastro
```

### 4. Agrega tu Solución

Navega hasta la carpeta del ejercicio correspondiente y crea una subcarpeta dentro de `solutions/` con tu nombre de usuario de GitHub:

* **Frontend:** `frontend/02-conversor-unidades/solutions/<tu-usuario>/`
* **Backend:** `backend/01-analizador-cifrado-cesar/solutions/<tu-usuario>/`

### 5. Guarda y Envía tus Cambios

```bash
git add .
git commit -m "feat: agrega solucion a conversor de unidades"
git push origin solucion/<nombre-ejercicio-tu-usuario>
```

### 6. Abre un Pull Request (PR)

1. Ve a tu repositorio en GitHub
2. Verás un botón verde que dice **"Compare & pull request"**
3. Escribe un título claro (ej.: `Solución Conversor de Unidades - JS`) y describe brevemente qué aprendiste y qué tecnologías usaste
4. ¡Envía el Pull Request! Un revisor lo analizará para integrarlo al proyecto principal

---

## 📜 Reglas de Convivencia y Código

* **Código limpio y legible:** Intenta comentar las partes clave de tu lógica para que otros principiantes puedan entenderla
* **Respeto mutuo:** Este es un espacio seguro para aprender. Todas las dudas y soluciones son válidas
* **Sin dependencias pesadas:** Intenta resolver los retos utilizando las herramientas estándar de cada lenguaje (Vanilla JS, librerías estándar de C/C++/Java/Rust/Python)

---

## 💡 ¿Necesitas Ayuda?

Si te atascas en algún reto o no sabes cómo hacer el PR, puedes consultarlo vía **Discord** en el canal dedicado o abrir un **Issue** en este repositorio con la etiqueta `duda` o preguntar directamente en las revisiones de código de tus compañeros. ¡Aprender en comunidad es más fácil!
