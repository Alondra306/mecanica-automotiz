# Imagen base con Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos del proyecto
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto (ajústalo si usas otro)
EXPOSE 5000

# Comando para iniciar la app (ajusta según el framework)
CMD ["python", "app.py"]
