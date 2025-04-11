from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os
import traceback
from app.transcribir import transcribir_audio

app = FastAPI()

UPLOAD_DIR = "/tmp/audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "API activa"}

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    try:
        print(f"📥 Recibiendo archivo: {file.filename}")
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print(f"💾 Archivo guardado en: {file_path}")

        resultado = transcribir_audio(file_path)

        print(f"📝 Resultado de transcripción: {resultado}")

        os.remove(file_path)
        print(f"🧹 Archivo eliminado: {file_path}")

        return JSONResponse(content=resultado)

    except Exception as e:
        print("❌ Ocurrió un error en /transcribe/:", e)
        traceback.print_exc()
        return JSONResponse(content={"error": str(e)}, status_code=500)