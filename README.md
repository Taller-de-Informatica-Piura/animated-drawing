# 🎞️ Crear animaciones GIF con Python

¡Hola! 👋
Este proyecto está pensado para que niñas y niños puedan **crear sus propias animaciones** de forma divertida usando dibujos.

Puedes hacerlo de dos maneras:

1️⃣ Dibujando en **Paint** (u otro programa).
2️⃣ Dibujando en papel y tomando fotos con una **cámara hecha con Raspberry Pi** 📷

Luego, Python une todas las imágenes y crea un **GIF animado** ✨

---

# 📁 Estructura del proyecto

El proyecto debe tener la siguiente estructura de carpetas:

```
animated_drawing/
├── createGIF.py
├── GIF_input/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   └── ...
├── cameraproj/
│   └── take_photo_v2.py
└── python_installer_windows/
```

---

# 🐍 Requisitos: instalar Python

Para que este programa funcione, es necesario tener **Python** instalado.

### Opción 1: Usar el instalador incluido

Dentro del proyecto encontrarás la carpeta:

```
python_installer_windows
```

Ahí hay un instalador de Python para Windows que puedes usar directamente.

---

### Opción 2: Descargar desde la web oficial

También puedes descargar Python desde:

👉 [https://www.python.org](https://www.python.org)

---

### ⚠️ Importante durante la instalación

* Marca la opción **"Add Python to PATH"** antes de instalar.
* Esto permite ejecutar Python desde la terminal.

---

### 📦 Instalar la librería Pillow

Este proyecto usa la librería **Pillow** para manejar imágenes.

Después de instalar Python, abre una terminal y ejecuta:

```
pip install pillow
```


### Opción 3: Instalar Thonny (recomendado para niñas y niños) 🐍

Otra forma muy fácil de usar Python es instalando **Thonny**.

Thonny es un programa pensado para aprender programación y ya viene con Python incluido.

Puedes descargarlo desde:

👉 [https://thonny.org](https://thonny.org)

---

### ▶️ Ejecutar scripts desde Thonny

1. Abre **Thonny**.
2. Ve a **File → Open** y abre `createGIF.py`.
3. Presiona el botón **Run ▶️** para ejecutar el programa.

---

### 📦 Instalar Pillow desde el administrador de paquetes de Thonny

Para que funcione el programa de animación necesitas instalar **Pillow**.

Dentro de Thonny:

1. Ve a **Tools → Manage Packages**.
2. Busca: `pillow`.
3. Presiona **Install**.

¡Y listo! 👍

---

Si no hay errores, ¡ya está listo! 👍

---

# 🖌️ Opción 1: Crear dibujos en Paint

1. Abre **Paint** (u otro programa similar).
2. Crea tus dibujos uno por uno.
3. Guarda cada dibujo como archivo **.png**.
4. Los archivos deben llamarse solo con números, en orden:

```
1.png
2.png
3.png
...
```

⚠️ **Importante**:

* Todos los archivos deben estar dentro de la carpeta `GIF_input`.
* No uses letras ni espacios, solo números.
* Todas las imágenes deben tener el mismo tamaño.

---

# 📷 Opción 2: Crear animaciones con dibujos en papel + Cámara Raspberry Pi

También puedes hacer tus dibujos en papel y tomar fotos para crear la animación 🎨➡️📸

Para esto se usa un **camera rig** (soporte de cámara) hecho con **Raspberry Pi**.

Dentro de la carpeta:

```
cameraproj/
```

encontrarás el script:

```
take_photo_v2.py
```

---

## 🕹️ ¿Qué hace este script?

Este programa permite controlar la cámara con el teclado:

* Mover la vista de la cámara (pan)
* Hacer zoom
* Tomar una foto

Así puedes acomodar tu dibujo antes de capturarlo 👍

---

## ▶️ Cómo ejecutar el script de la cámara

Este script debe ejecutarse en la **terminal del Raspberry Pi OS**.

### 1️⃣ Abrir la terminal

En la Raspberry Pi, abre la aplicación **Terminal**.

### 2️⃣ Ir a la carpeta del proyecto

Ejemplo:

```
cd ~/git/animated-drawing/cameraproj
```

### 3️⃣ Ejecutar el programa

```
python take_photo_v2.py
```

Luego usa el teclado para mover la cámara y tomar las fotos de tus dibujos.

Las imágenes que tomes debes guardarlas después dentro de la carpeta:

```
GIF_input
```

para poder crear la animación.

---

# 🐍 El script createGIF.py

El archivo `createGIF.py` es el programa que:

* Lee todas las imágenes de la carpeta `GIF_input`
* Las ordena por número
* Crea un archivo animado `.gif`

No necesitas modificar el código, salvo un detalle opcional.

---

# ⏱️ Cambiar la velocidad de la animación

Dentro del archivo encontrarás una línea como esta:

```python
duration = 400  # milliseconds per frame
```

Este valor controla cuánto tiempo se muestra cada imagen.

* Está en milisegundos.
* Número pequeño → más rápido.
* Número grande → más lento.

### Ejemplos

```python
duration = 100    # muy rápido
duration = 400    # normal
duration = 1000   # lento
```

---

# ▶️ Ejecutar el programa para crear el GIF

Necesitas usar la terminal.

### 1️⃣ Abrir terminal

* Windows: Command Prompt o PowerShell
* Mac / Linux / Raspberry Pi: Terminal

---

### 2️⃣ Ir a la carpeta del proyecto

Ejemplo en Raspberry Pi o Linux:

```
cd ~/git/animated-drawing
```

Ejemplo en Windows:

```
cd C:\animated_drawing
```

---

### 3️⃣ Ejecutar el script

```
python createGIF.py
```

Si todo está bien, se creará:

```
output.gif
```

con tu animación 🎉

---

# 🌟 ¡Listo!

Ahora puedes:

* Dibujar en la compu 💻
* Dibujar en papel ✏️
* Tomar fotos con la Raspberry Pi 📷
* Crear tus propios GIF animados ✨

¡Diviértete creando historias animadas! 🚀
