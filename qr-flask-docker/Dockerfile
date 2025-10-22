# 1. Imagen base: Usamos una imagen oficial de Python ligera.
FROM python:3.10-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de dependencias
COPY requirements.txt .

# 4. Instalar las dependencias
# --no-cache-dir ahorra espacio en la imagen final
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del código de tu proyecto al contenedor
COPY . .

# 6. Exponer el puerto en el que Flask está corriendo (el 5000)
EXPOSE 5000

# 7. El comando para ejecutar la aplicación cuando el contenedor se inicie
CMD ["python", "app.py"]