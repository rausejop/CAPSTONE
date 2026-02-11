"""
Manager 6: Output & Speech Synthesis.
Converts intelligence insights into audio and maintains verbose logs.
Supports gTTS or Piper for low-latency output.
"""
import logging
from gtts import gTTS
import os
from datetime import datetime

class OutputManager:
    def __init__(self, log_file: str = "./data/pipeline.log"):
        # Configuración de Logs Verbosos (Requisito ADR-001)
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamFilter(logging.INFO)
            ]
        )
        self.logger = logging.getLogger("IntelligencePipeline")

    def log_event(self, message: str, level: str = "info"):
        """Registra cada paso del pipeline para depuración y auditoría."""
        if level == "info":
            self.logger.info(message)
        elif level == "error":
            self.logger.error(message)

    def text_to_speech(self, text: str, output_file: str = "insight_audio.mp3"):
        """
        Requirement FUNC06: Text-to-Speech (TTS).
        Generates audio briefing of the geopolitical insights.
        """
        try:
            self.log_event("Iniciando síntesis de voz...")
            tts = gTTS(text=text, lang='en') # O 'es' para español
            save_path = os.path.join("./data", output_file)
            tts.save(save_path)
            self.log_event(f"Audio generado exitosamente en: {save_path}")
            return save_path
        except Exception as e:
            self.log_event(f"Error en TTS: {e}", level="error")
            return None

    def generate_final_report(self, structured_data: dict, sentiment: dict):
        """Genera un reporte final consolidado en texto."""
        report = (
            f"--- GEOPOLITICAL INTELLIGENCE REPORT ---\n"
            f"Timestamp: {datetime.now()}\n"
            f"Source ID: {structured_data['source_id']}\n"
            f"Sentiment Analysis: {sentiment['sentiment']} (Score: {sentiment['score']})\n"
            f"Content Summary: {structured_data['content'][:200]}...\n"
            f"Integrity: {structured_data['signature_evidence']}\n"
            f"----------------------------------------"
        )
        self.log_event("Reporte final generado.")
        return report

# Ejemplo de uso
# output = OutputManager()
# output.text_to_speech("Tensions remain high in the Strait of Hormuz.")