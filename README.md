# 🎞️ Crear animaciones GIF con Python

Este proyecto permite crear una **animación GIF** a partir de varios dibujos hechos en **Paint** (u otro editor de imágenes), usando un script en **Python** llamado `createGIF.py`.

La idea es simple:  
cada imagen es un cuadro de la animación, y Python las une en un solo archivo `.gif`.

---

## 📁 Estructura del proyecto

El proyecto debe tener la siguiente estructura de carpetas:

animated_drawing/
├── createGIF.py
├── GIF_input/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   └── ...
└── python_installer_windows/


---

## 🐍 Requisitos: instalar Python

Para que este programa funcione, es necesario tener **Python** instalado en el sistema.

### Opción 1: Usar el instalador incluido

Dentro del proyecto encontrarás la carpeta: python_installer_windows


Ahí hay un instalador de Python para Windows que puedes usar directamente.

### Opción 2: Descargar desde la web oficial

También puedes descargar Python desde:

👉 https://www.python.org

### ⚠️ Importante durante la instalación

- Marca la opción **"Add Python to PATH"** antes de instalar
- Esto es necesario para poder ejecutar Python desde la terminal

### 📦 Instalar la librería Pillow

Este proyecto usa la librería **Pillow** para manejar imágenes.

Después de instalar Python, abre una terminal y ejecuta: pip install pillow


Si el comando funciona sin errores, ya tienes todo listo 👍


---
## 🖌️ Paso 1: Crear los dibujos

1. Abre **Paint** (u otro programa similar).
2. Crea tus dibujos uno por uno.
3. Guarda cada dibujo como archivo **.png**.
4. Los archivos deben llamarse **solo con números**, en orden:


⚠️ **Importante**:
- Todos los archivos deben estar dentro de la carpeta `GIF_input`
- No uses letras ni espacios en los nombres, solo numeros.
- Todas las imágenes deben tener el mismo tamaño

---

## 🐍 Paso 2: El script `createGIF.py`

El archivo `createGIF.py` es el programa en Python que:

- Lee todas las imágenes de la carpeta `GIF_input`
- Las ordena por número
- Crea un archivo animado `.gif`

No es necesario modificar el código, **solo un parámetro opcional**.

---

## ⏱️ Cambiar la velocidad de la animación

Dentro del archivo `createGIF.py` encontrarás una línea similar a esta:

```python
duration = 400  # milliseconds per frame

Este valor controla **cuánto tiempo se muestra cada imagen**.

- El valor está en **milisegundos**
- Un número más pequeño → animación más rápida
- Un número más grande → animación más lenta

### Ejemplos

```python
duration = 100    # muy rápido
duration = 400    # velocidad normal
duration = 1000   # lento
```

---

## ▶️ Paso 3: Ejecutar el programa

Para ejecutar el programa es necesario usar la **terminal** (Command Prompt / PowerShell / Terminal).

### 1️⃣ Abrir la terminal

- En **Windows**: abre *Command Prompt* o *PowerShell*
- En **Mac / Linux**: abre *Terminal*

### 2️⃣ Ir a la carpeta del proyecto

Usa el comando `cd` para moverte a la carpeta donde está el archivo `createGIF.py`.

Ejemplo:

cd C:\animated_drawing

Una vez dentro de la carpeta correcta, ejecuta el script con Python:

python createGIF.py

Si todo está correcto, el programa creará un archivo llamado **`output.gif`**  
en la **misma carpeta del proyecto**, que contiene tu animación 🎉


