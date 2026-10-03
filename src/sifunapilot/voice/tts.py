from typing import Optional


class TTSEngine:
    def __init__(self) -> None:
        self.enabled = False

    def speak(self, text: str) -> str:
        if not self.enabled:
            return f"🔇 TTS disabled - would say: {text}"
        return f"✓ Speaking: {text}"


def get_tts() -> TTSEngine:
    return TTSEngine()
