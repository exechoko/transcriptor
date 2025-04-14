import whisper
import os
import traceback
import logging
import time

logging.basicConfig(level=logging.INFO)

try:
    modelo = whisper.load_model("small")
    logging.info("Modelo Whisper cargado exitosamente")
except Exception as e:
    logging.error(f"Error cargando el modelo: {str(e)}")
    raise

def transcribir_audio(ruta_audio):
    try:
        logging.info(f"🧪 Transcribiendo: {ruta_audio}")
        inicio = time.time()
        resultado = modelo.transcribe(ruta_audio, fp16=False)  # Forzar CPU
        duracion = time.time() - inicio
        logging.info(f"✅ Transcripción terminada en {duracion:.2f} segundos")
        logging.info(f"📝 Resultado: {resultado['text']}")
        return {"success": True, "text": resultado["text"]}
    except Exception as e:
        logging.error(f"❌ Error en transcripción: {str(e)}")
        traceback.print_exc()
        return {"success": False, "error": str(e)}