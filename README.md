# 🚀 Generador de Códigos QR con Flask y Docker

Este es un pequeño proyecto personal: un microservicio web simple que genera códigos QR dinámicamente. Está construido con **Flask** (Python) y está completamente *dockerizado* para un despliegue rápido y sencillo.

## 📋 Características

* **Interfaz web simple:** Un formulario HTML para introducir texto o una URL y generar un QR en la misma página.
* **API directa:** Expone un endpoint `/qr` para generar la imagen PNG directamente (ej. `/qr?data=hola`).
* **Dockerizado:** Listo para construir y ejecutar en un contenedor aislado con un solo comando.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.10+
* **Framework Web:** Flask
* **Generación de QR:** `qrcode[pil]`
* **Contenedorización:** Docker

---

## 🚀 Cómo Ejecutarlo (Método recomendado: Docker)

La forma más fácil y rápida de poner en marcha el servicio es usando Docker.

### 1. Clona este repositorio

```bash
git clone https://github.com/CalvaryBloom/Qr_Generator
cd Qr_Generator
```

### 2. Construye la imagen de Docker

Este comando lee el `Dockerfile` y empaqueta la aplicación con todas sus dependencias.

```bash
docker build -t qr-service .
```

### 3. Ejecuta el contenedor

Este comando inicia la aplicación. Mapea el puerto 5001 de tu máquina al puerto 5000 del contenedor.

```bash
docker run -d -p 5001:5000 --name mi-qr-app qr-service
```

### 4. ¡Accede a la aplicación!

Abre tu navegador y visita: `http://localhost:5001`

---

## 🔧 Ejecución en Local (Sin Docker)

Si prefieres ejecutarlo directamente en tu máquina local para desarrollo:

### 1. Clona el repositorio (si no lo has hecho)

```bash
git clone https://github.com/CalvaryBloom/Qr_Generator
cd Qr_Generator
```

### 2. Crea y activa un entorno virtual (recomendado)

```bash
# Para Mac/Linux
python3 -m venv venv
source venv/bin/activate

# Para Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Inicia la aplicación Flask

```bash
python app.py
```

### 5. ¡Accede a la aplicación!

Abre tu navegador y visita: `http://localhost:5000` (nota que el puerto es 5000 por defecto al correrlo localmente).

---

## ⚙️ Uso de la Aplicación

Una vez que la aplicación esté en funcionamiento (ya sea local o en Docker), puedes usarla de dos maneras:

### 1. Interfaz Web (UI)

Visita la ruta raíz (`http://localhost:5001`) para ver un formulario. Escribe el texto que deseas codificar y presiona "Generar QR". La imagen aparecerá en la misma página.

### 2. API Directa

Puedes usar el endpoint `/qr` para obtener directamente la imagen PNG. Esto es útil para integrar con otras aplicaciones.

**Ejemplo de uso:**

```
http://localhost:5001/qr?data=Este texto se convertirá en QR
```