from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os
from app.transcribir import transcribir_audio

app = FastAPI()

UPLOAD_DIR = "/tmp/audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resultado = transcribir_audio(file_path)

    os.remove(file_path)

    return JSONResponse(content=resultado)