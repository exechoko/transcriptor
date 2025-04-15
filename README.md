
# 🧠 Whisper API - Transcripción de audio con FastAPI + Whisper

Este proyecto es una API simple construida con FastAPI y OpenAI Whisper (modo CPU), que permite subir un archivo de audio y obtener la transcripción en texto.

---

## 🚀 Levantar el servicio con Docker

### 1. Clonar el repositorio (o navegar al directorio del proyecto)

```bash
https://github.com/exechoko/transcriptor.git
cd transcriptor
```

### 2. Construir e iniciar los contenedores

```bash
docker compose up --build
```

Esto construirá la imagen e iniciará la API en `http://localhost:8010`.

---

## 🛑 Detener el servicio

```bash
docker compose down
```

---

## 🧪 Endpoints disponibles

### `GET /`
Verifica si la API está activa.

**Respuesta esperada:**
```json
{
  "message": "API activa"
}
```

---

### `POST /transcribe/`
Sube un archivo de audio y devuelve la transcripción.

#### Parámetros:
- Formato: `multipart/form-data`
- Campo: `file` (archivo de audio, por ejemplo `.mp3`, `.wav`, `.m4a`, etc.)

#### Ejemplo con `curl`:
```bash
curl.exe -X POST "http://localhost:8010/transcribe/"
  -H "accept: application/json"
  -H "Content-Type: multipart/form-data"
  -F "file=@C:/Users/Usuario/Desktop/saludo.wav"
```

#### Respuesta esperada:
```json
{
  "success": true,
  "text": "Texto transcripto desde el audio"
}
```

#### En caso de error:
```json
{
  "success": false,
  "text": "Descripción del error"
}
```

---

## 📁 Estructura del proyecto

```
.
├── app/
│   ├── main.py              # API FastAPI
│   └── transcribir.py       # Función de transcripción con Whisper
├── requirements.txt         # Dependencias del proyecto
├── Dockerfile               # Imagen base de la app
├── docker-compose.yml       # Orquestación del contenedor
└── README.md                # Esta guía
```

---

## 📌 Notas
- El modelo `base` de Whisper se carga una única vez al iniciar el contenedor.
- La carpeta temporal `/tmp/audio` se usa para almacenar los audios de forma transitoria.
- Este proyecto utiliza PyTorch en modo CPU (`torch==2.1.0+cpu`), por lo tanto **no requiere GPU**.

---

💡 **Tip**: podés probar la API visualmente en `http://localhost:8010/docs` gracias a la documentación automática de Swagger.

---
