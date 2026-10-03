import pyttsx3
from typing import Optional


class TTSEngine:
    def __init__(self) -> None:
        self.enabled = True
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 180)
            self.engine.setProperty('volume', 1.0)
        except Exception:
            self.engine = None
            self.enabled = False

    def speak(self, text: str) -> str:
        if not self.enabled or not self.engine or not text:
            return f"🔇 {text}"
        try:
            self.engine.say(text)
            self.engine.runAndWait()
            return f"✓ Spoken: {text}"
        except Exception as e:
            return f"✗ TTS error: {e}"


def get_tts() -> TTSEngine:
    return TTSEngine()
