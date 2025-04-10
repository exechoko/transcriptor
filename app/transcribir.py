import whisper
import os

modelo = whisper.load_model("base")  # Carga única

os.environ["PATH"] += os.pathsep + "/usr/bin"  # Asegura ffmpeg en Linux

def transcribir_audio(ruta_audio):
    try:
        resultado = modelo.transcribe(ruta_audio)
        return {"success": True, "text": resultado["text"]}
    except Exception as e:
        return {"success": False, "text": str(e)}