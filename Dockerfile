FROM python:3.10-slim

# Instala ffmpeg y dependencias básicas
RUN apt-get update && \
    apt-get install -y ffmpeg libavcodec-extra libgl1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Crea el directorio de trabajo
WORKDIR /app

# Copia el archivo de requirements
COPY requirements.txt .

# Instala dependencias de Python
RUN pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt

# Copia el resto del código
COPY ./app ./app

# Expone el puerto que usará FastAPI
EXPOSE 8010

# Comando para iniciar la app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8010"]
